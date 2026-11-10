"""Step 2: fetch full text for every in-window item and store it in data/raw/.

One JSON file per item: data/raw/<source_id>/<YYYY-MM-DD>_<slug>.json with
    id, source, source_name, voice, author, date, url, title, kind, text, word_count, fetched_at

Usage:
    python -m src.fetch                    # all sources, last 365 days
    python -m src.fetch zvi hn             # only some sources
    python -m src.fetch --days 2           # (daily digest) only recent items
Re-running skips files that already exist.
No API key is used here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone

from bs4 import BeautifulSoup

from .config import BACKFILL_DAYS, RAW_DIR, SOURCES, SOURCES_BY_ID, now_utc, window_start
from .feeds import (html_to_text, list_feed, list_latentspace_archive,
                    list_substack_archive, list_tunguz_archive)
from .hn import fetch_thread, is_relevant, list_ask_hn
from .http_client import PoliteSession

HN_TOP_COMMENTS = 25        # top-level comments kept per thread
HN_REPLIES_PER_COMMENT = 2  # direct replies kept under each
HN_MAX_COMMENT_WORDS = 250

_STRIP = ["script", "style", "noscript", "nav", "header", "footer", "aside", "form",
          "button", "svg", "iframe"]


def slugify(s: str, n: int = 60) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:n] or hashlib.sha1(s.encode()).hexdigest()[:10]


def main_text(html: str, selectors=("article", "main")) -> tuple[str, str]:
    """Return (text, author) from a post page."""
    soup = BeautifulSoup(html, "html.parser")
    meta = soup.find("meta", attrs={"name": "author"})
    author = meta.get("content", "") if meta else ""
    el = None
    for sel in selectors:
        el = soup.select_one(sel)
        if el and len(el.get_text(" ").split()) > 50:
            break
    el = el or soup.body or soup
    for t in el.find_all(_STRIP):
        t.decompose()
    return html_to_text(str(el)), author


class Writer:
    def __init__(self, src_id: str):
        self.src = SOURCES_BY_ID.get(src_id, {"id": src_id, "name": "Hacker News — Ask HN",
                                              "voice": "community", "author": ""})
        self.dir = RAW_DIR / src_id
        self.dir.mkdir(parents=True, exist_ok=True)
        self.written = self.skipped = self.failed = 0
        self._hashes: set[str] = set()

    def path(self, date: datetime, url: str):
        tail = url.rstrip("/").split("/")[-1].split("?")[0] or url
        return self.dir / f"{date:%Y-%m-%d}_{slugify(tail)}.json"

    def exists(self, date, url) -> bool:
        if self.path(date, url).exists():
            self.skipped += 1
            return True
        return False

    def write(self, *, date: datetime, url: str, title: str, text: str,
              author: str = "", kind: str = "post", **extra):
        h = hashlib.sha1(text.encode()).hexdigest()
        if h in self._hashes:  # exact duplicate (e.g. AINews same-day re-posts)
            return
        self._hashes.add(h)
        rec = {
            "id": f"{self.src['id']}:{self.path(date, url).stem}",
            "source": self.src["id"], "source_name": self.src["name"],
            "voice": self.src["voice"],
            "author": author or self.src.get("author", ""),
            "date": date.isoformat(), "url": url, "title": title, "kind": kind,
            "word_count": len(text.split()), "fetched_at": now_utc().isoformat(),
            **extra, "text": text,
        }
        self.path(date, url).write_text(json.dumps(rec, ensure_ascii=False, indent=1))
        self.written += 1


def _fetch_pages(w: Writer, sess: PoliteSession, items: list[dict], selectors, kind="post"):
    for it in items:
        if w.exists(it["date"], it["url"]):
            continue
        try:
            r = sess.get(it["url"])
            r.raise_for_status()
            text, author = main_text(r.text, selectors)
            w.write(date=it["date"], url=it["url"], title=it["title"], text=text,
                    author=it.get("author") or author, kind=it.get("kind") or kind)
        except Exception as e:
            w.failed += 1
            print(f"  ! {w.src['id']} {it['url']}: {e!r}"[:200], file=sys.stderr)


# ---------------------------------------------------------------- per-source fetchers
def fetch_ainews(since):
    """news.smol.ai issues (until it moved), then AINews issues on latent.space."""
    w, s = Writer("ainews"), PoliteSession()
    smol = [e for e in list_feed(s, SOURCES_BY_ID["ainews"]["feed"]) if e["date"] and e["date"] >= since]
    _fetch_pages(w, s, smol, ("article", "main"), kind="ainews")
    return w


def fetch_latentspace(since):
    w, s = Writer("latentspace"), PoliteSession()
    posts = list_latentspace_archive(s, since)
    _fetch_pages(w, s, [p for p in posts if p["kind"] == "post"], ("article", "main"))
    # AINews issues published on latent.space after news.smol.ai stopped.
    smol = [e["date"] for e in list_feed(s, SOURCES_BY_ID["ainews"]["feed"]) if e["date"]]
    cutoff = max(smol) + timedelta(days=1) if smol else since
    aw = Writer("ainews")
    _fetch_pages(aw, s, [p for p in posts if p["kind"] == "ainews" and p["date"] >= cutoff],
                 ("article", "main"), kind="ainews")
    w.written += aw.written; w.skipped += aw.skipped; w.failed += aw.failed
    return w


def fetch_substack(src_id, since):
    src, w, s = SOURCES_BY_ID[src_id], Writer(src_id), PoliteSession()
    posts = list_substack_archive(s, src["site"], since)
    free = [p for p in posts if p["audience"] == "everyone"]  # skip paid-only (decision 1)
    w.paid_skipped = len(posts) - len(free)
    for p in free:
        if w.exists(p["date"], p["url"]):
            continue
        try:
            r = s.get(f"{src['site'].rstrip('/')}/api/v1/posts/{p['slug']}")
            r.raise_for_status()
            j = r.json()
            text = html_to_text(j.get("body_html") or "")
            if len(text.split()) < 50:  # fall back to the public page
                text, _ = main_text(s.get(p["url"]).text, ("div.body", "article"))
            w.write(date=p["date"], url=p["url"], title=p["title"], text=text,
                    author=p["author"], kind=p.get("kind") or "post",
                    subtitle=j.get("subtitle") or "")
        except Exception as e:
            w.failed += 1
            print(f"  ! {src_id} {p['url']}: {e!r}"[:200], file=sys.stderr)
    return w


def fetch_feed_site(src_id, since):
    """Plain RSS sites (Hamel, Eugene Yan): list from feed, full text from the page."""
    src, w, s = SOURCES_BY_ID[src_id], Writer(src_id), PoliteSession()
    items = [e for e in list_feed(s, src["feed"]) if e["date"] and e["date"] >= since]
    _fetch_pages(w, s, items, ("#quarto-document-content", "article", "main", ".post"))
    return w


def fetch_tunguz(since):
    w, s = Writer("tomtunguz"), PoliteSession()
    _fetch_pages(w, s, list_tunguz_archive(s, since), (".post-content", "article", "main"))
    return w


_MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def fetch_simonwillison(since):
    """Walk day archives; keep long-form entries and commented links (decision 2)."""
    w, s = Writer("simonwillison"), PoliteSession()
    day = since.replace(hour=0, minute=0, second=0, microsecond=0)
    end = now_utc()
    while day <= end:
        url = f"https://simonwillison.net/{day.year}/{_MONTHS[day.month - 1]}/{day.day}/"
        day_dt, day = day, day + timedelta(days=1)
        try:
            r = s.get(url)
            if r.status_code == 404:
                continue
            r.raise_for_status()
        except Exception as e:
            w.failed += 1
            print(f"  ! simonwillison {url}: {e!r}"[:200], file=sys.stderr)
            continue
        soup = BeautifulSoup(r.text, "html.parser")
        for seg in soup.select("div.segment"):
            classes = set(seg.get("class", []))
            kind = "entry" if "entry" in classes else "link" if "blogmark" in classes else None
            if not kind:
                continue
            a = seg.find("a", href=re.compile(rf"^/{day_dt.year}/{_MONTHS[day_dt.month - 1]}/{day_dt.day}/[^/]+/$"))
            if not a:
                continue
            post_url = "https://simonwillison.net" + a["href"]
            if w.exists(day_dt, post_url):
                continue
            h = seg.find(["h2", "h3"]) or seg.select_one("p strong a")  # blogmark: linked title
            title = h.get_text(" ", strip=True) if h else a.get_text(" ", strip=True)
            try:
                if kind == "entry":  # full text lives on the permalink page
                    pr = s.get(post_url)
                    pr.raise_for_status()
                    text, _ = main_text(pr.text, ("div.entry", "div.entryPage", "article", "main"))
                else:
                    for t in seg.find_all(_STRIP):
                        t.decompose()
                    text = html_to_text(str(seg))
                w.write(date=day_dt, url=post_url, title=title, text=text,
                        author="Simon Willison", kind=kind)
            except Exception as e:
                w.failed += 1
                print(f"  ! simonwillison {post_url}: {e!r}"[:200], file=sys.stderr)
    return w


def _clip(text: str, n: int) -> str:
    words = text.split()
    return " ".join(words[:n]) + (" …" if len(words) > n else "")


def _descendants(c: dict) -> int:
    return sum(1 + _descendants(k) for k in c.get("children") or [] if k.get("text"))


def fetch_hn(since):
    """Relevant Ask HN threads + top comments (ranked by reply count, a proxy for engagement)."""
    w, s = Writer("hn"), PoliteSession()
    stories = [st for st in list_ask_hn(s, since) if is_relevant(st)]
    for st in stories:
        if w.exists(st["date"], st["url"]):
            continue
        try:
            item = fetch_thread(s, st["id"])
            tops = [c for c in item.get("children") or [] if c.get("text")]
            tops.sort(key=_descendants, reverse=True)
            parts = [f"[{st['author']}] {st['title']}\n{st['text']}".strip(), "", "--- Top comments ---"]
            commenters = []
            for c in tops[:HN_TOP_COMMENTS]:
                parts.append(f"\n[{c.get('author')}] {_clip(html_to_text(c['text']), HN_MAX_COMMENT_WORDS)}")
                commenters.append(c.get("author"))
                replies = [k for k in c.get("children") or [] if k.get("text")]
                replies.sort(key=_descendants, reverse=True)
                for k in replies[:HN_REPLIES_PER_COMMENT]:
                    parts.append(f"  ↳ [{k.get('author')}] {_clip(html_to_text(k['text']), HN_MAX_COMMENT_WORDS)}")
                    commenters.append(k.get("author"))
            w.write(date=st["date"], url=st["url"], title=st["title"], text="\n".join(parts),
                    author=st["author"], kind="ask_hn", points=st["points"],
                    num_comments=st["num_comments"], commenters=commenters)
        except Exception as e:
            w.failed += 1
            print(f"  ! hn {st['url']}: {e!r}"[:200], file=sys.stderr)
    return w


def jobs(since, only=None):
    table = {
        "ainews": lambda: fetch_ainews(since),
        "latentspace": lambda: fetch_latentspace(since),
        "simonwillison": lambda: fetch_simonwillison(since),
        "tomtunguz": lambda: fetch_tunguz(since),
        "hn": lambda: fetch_hn(since),
    }
    for src in SOURCES:
        if src["id"] in table:
            continue
        if src["platform"] == "substack":
            table[src["id"]] = (lambda i: lambda: fetch_substack(i, since))(src["id"])
        else:
            table[src["id"]] = (lambda i: lambda: fetch_feed_site(i, since))(src["id"])
    return {k: v for k, v in table.items() if not only or k in only}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sources", nargs="*")
    ap.add_argument("--days", type=int, default=BACKFILL_DAYS)
    a = ap.parse_args()
    since = window_start(a.days)
    todo = jobs(since, a.sources or None)
    summary = {}
    # One worker per source; each has its own per-host rate limit.
    with ThreadPoolExecutor(max_workers=len(todo)) as ex:
        futs = {ex.submit(fn): sid for sid, fn in todo.items()}
        for f in as_completed(futs):
            sid = futs[f]
            try:
                w = f.result()
                summary[sid] = {"written": w.written, "skipped_existing": w.skipped,
                                "failed": w.failed,
                                "paid_skipped": getattr(w, "paid_skipped", 0)}
            except Exception as e:
                traceback.print_exc()
                summary[sid] = {"error": repr(e)[:200]}
            print(f"✓ {sid}: {summary[sid]}", file=sys.stderr, flush=True)
    counts = {d.name: len(list(d.glob("*.json"))) for d in sorted(RAW_DIR.iterdir()) if d.is_dir()}
    report = {"ran_at": now_utc().isoformat(), "since": since.isoformat(),
              "this_run": summary, "files_on_disk": counts, "total_files": sum(counts.values())}
    (RAW_DIR / "fetch_report.json").write_text(json.dumps(report, indent=1))
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
