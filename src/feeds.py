"""Listing posts from RSS/Atom feeds and public archives.

Each lister returns a list of dicts with at least:
    title, url, date (aware datetime, UTC), author
and optionally: html (full or partial body from the feed), audience
("everyone" | "only_paid" | ...), wordcount, kind.
"""
from __future__ import annotations

import re
import warnings
from collections import Counter
from datetime import datetime, timezone
from calendar import timegm

import feedparser
from bs4 import BeautifulSoup
from dateutil import parser as dateparser

from bs4 import MarkupResemblesLocatorWarning

from .http_client import PoliteSession, RobotsDisallowed

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

PAYWALL_MARKERS = re.compile(
    r"(keep reading with a \d+-day free trial|this post is for paid subscribers|"
    r"subscribe to (keep|continue) reading|upgrade to paid|for paying subscribers only|"
    r"read more\s*$)",
    re.I,
)


def html_to_text(html: str) -> str:
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(["script", "style", "noscript"]):
        t.decompose()
    text = soup.get_text("\n")
    return re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+", " ", text)).strip()


def _to_dt(struct) -> datetime | None:
    if not struct:
        return None
    return datetime.fromtimestamp(timegm(struct), tz=timezone.utc)


def parse_iso(s: str | None) -> datetime | None:
    if not s:
        return None
    d = dateparser.isoparse(s) if "T" in s else dateparser.parse(s)
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


# ---------------------------------------------------------------- RSS / Atom
def list_feed(session: PoliteSession, feed_url: str) -> list[dict]:
    r = session.get(feed_url)
    r.raise_for_status()
    f = feedparser.parse(r.content)
    out = []
    for e in f.entries:
        html = ""
        if e.get("content"):
            html = max((c.get("value", "") for c in e.content), key=len)
        html = html or e.get("summary", "")
        out.append({
            "title": (e.get("title") or "").strip(),
            "url": e.get("link"),
            "date": _to_dt(e.get("published_parsed") or e.get("updated_parsed")),
            "author": e.get("author") or "",
            "html": html,
        })
    return out


def looks_paywalled(html: str) -> bool:
    text = html_to_text(html)
    return bool(PAYWALL_MARKERS.search(text[-400:])) or len(text.split()) < 120


# ---------------------------------------------------------------- Substack
def list_substack_archive(session: PoliteSession, site: str, since: datetime,
                          max_pages: int = 60) -> list[dict]:
    """Walk Substack's public archive JSON (cursor-paginated) back to `since`.

    Raises RobotsDisallowed if the site's robots.txt disallows /api/.
    """
    base = site.rstrip("/") + "/api/v1/archive"
    params = {"sort": "new", "limit": 25}
    out: list[dict] = []
    for _ in range(max_pages):
        r = session.get(base, params=params)
        r.raise_for_status()
        data = r.json()
        posts = data["posts"] if isinstance(data, dict) else data
        if not posts:
            break
        stop = False
        for p in posts:
            d = parse_iso(p.get("post_date"))
            if d and d < since:
                stop = True
                continue
            bylines = p.get("publishedBylines") or []
            out.append({
                "title": p.get("title") or "",
                "url": p.get("canonical_url"),
                "slug": p.get("slug"),
                "date": d,
                "author": ", ".join(b.get("name", "") for b in bylines),
                "audience": p.get("audience"),
                "wordcount": p.get("wordcount"),
                "kind": p.get("type"),  # newsletter | podcast | thread | ...
            })
        cursor = data.get("nextCursor") if isinstance(data, dict) else None
        if stop or not cursor:
            break
        params = {"sort": "new", "limit": 25, "cursor": cursor}
    return out


# ---------------------------------------------------------------- Latent Space
_LS_CARD = re.compile(
    r'href="(/p/[^"]+)"[^>]*>(.*?)</a>.*?<time[^>]*datetime="([^"]+)"', re.S)


def list_latentspace_archive(session: PoliteSession, since: datetime,
                             max_pages: int = 80) -> list[dict]:
    """latent.space left Substack; its archive is server-rendered at /archive/?page=N."""
    out: dict[str, dict] = {}
    for page in range(1, max_pages + 1):
        url = "https://latent.space/archive/" + (f"?page={page}" if page > 1 else "")
        r = session.get(url)
        if r.status_code == 404:
            break
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        found = 0
        oldest = None
        for t in soup.find_all("time", attrs={"datetime": True}):
            # The card containing this <time> also contains the post link.
            card = t
            link = None
            for _ in range(6):
                card = card.parent
                if card is None:
                    break
                link = card.find("a", href=re.compile(r"^/p/"))
                if link:
                    break
            if not link:
                continue
            d = parse_iso(t["datetime"])
            href = link["href"]
            oldest = d if oldest is None or d < oldest else oldest
            if d < since or href in out:
                continue
            title = link.get_text(" ", strip=True)
            if not title:
                h = card.find(["h2", "h3"])
                title = h.get_text(" ", strip=True) if h else href
            out[href] = {
                "title": title,
                "url": "https://latent.space" + href,
                "date": d,
                "author": "",
                "kind": "ainews" if href.startswith("/p/ainews") else "post",
            }
            found += 1
        if oldest is None or oldest < since:
            break
    return sorted(out.values(), key=lambda x: x["date"], reverse=True)


# ---------------------------------------------------------------- Tom Tunguz
def list_tunguz_archive(session: PoliteSession, since: datetime) -> list[dict]:
    """tomtunguz.com/archive/ lists every post with a <time datetime> on one page."""
    r = session.get("https://tomtunguz.com/archive/")
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    out = []
    for li in soup.select("li.archive-item"):
        t, a = li.find("time"), li.find("a", href=True)
        if not (t and a):
            continue
        d = parse_iso(t.get("datetime"))
        if d and d >= since:
            out.append({"title": a.get_text(" ", strip=True), "url": a["href"],
                        "date": d, "author": "Tomasz Tunguz", "kind": "post"})
    return out


# ---------------------------------------------------------------- Simon Willison
_MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def simonwillison_month_counts(session: PoliteSession, since: datetime,
                               until: datetime) -> Counter:
    """Sum the per-type counts printed at the top of each /YYYY/Mon/ archive page."""
    totals: Counter = Counter()
    y, m = since.year, since.month
    while (y, m) <= (until.year, until.month):
        r = session.get(f"https://simonwillison.net/{y}/{_MONTHS[m - 1]}/")
        if r.status_code == 200:
            text = BeautifulSoup(r.text, "html.parser").get_text(" ")
            head = re.search(r"(\d+) posts:(.{0,300})", text, re.S)
            if head:
                totals["posts"] += int(head.group(1))
                for n, kind in re.findall(r"(\d+)\s+([a-z]+)", head.group(2)):
                    totals[kind.rstrip("s")] += int(n)
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return totals


__all__ = [
    "list_feed", "list_substack_archive", "list_latentspace_archive",
    "list_tunguz_archive", "simonwillison_month_counts",
    "looks_paywalled", "html_to_text", "parse_iso", "RobotsDisallowed",
]
