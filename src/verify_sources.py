"""Step 1: verify every source and write a table of 12-month item counts.

Usage:  python -m src.verify_sources
Writes: data/out/source_verification.json and data/out/source_verification.md
No API key is used here.
"""
from __future__ import annotations

import json
import sys
import traceback
from collections import Counter

from .config import OUT_DIR, RECENT_DAYS, SOURCES, window_start, now_utc
from .feeds import (RobotsDisallowed, list_feed, list_latentspace_archive,
                    list_substack_archive, list_tunguz_archive, looks_paywalled,
                    simonwillison_month_counts)
from .hn import is_relevant, list_ask_hn
from .http_client import PoliteSession


def _fmt(d):
    return d.strftime("%Y-%m-%d") if d else "—"


def verify_source(sess: PoliteSession, src: dict, since, recent) -> dict:
    row = {"id": src["id"], "name": src["name"], "author": src["author"],
           "voice": src["voice"], "feed": src["feed"], "notes": []}
    entries = list_feed(sess, src["feed"])
    dated = [e for e in entries if e["date"]]
    row["feed_items"] = len(entries)
    row["feed_newest"] = _fmt(max((e["date"] for e in dated), default=None))
    row["feed_oldest"] = _fmt(min((e["date"] for e in dated), default=None))
    row["active_90d"] = any(e["date"] >= recent for e in dated)
    in_window_feed = [e for e in dated if e["date"] >= since]
    pw = sum(looks_paywalled(e["html"]) for e in in_window_feed)
    row["feed_12mo"] = len(in_window_feed)
    row["feed_paywalled_share"] = round(pw / len(in_window_feed), 2) if in_window_feed else None
    feed_covers_window = bool(dated) and min(e["date"] for e in dated) <= since

    # Archive / 12-month count
    if src["id"] == "latentspace":
        posts = list_latentspace_archive(sess, since)
        kinds = Counter(p["kind"] for p in posts)
        row["count_12mo"] = kinds["post"]
        row["archive"] = "public HTML archive (/archive/?page=N)"
        row["notes"].append(
            f"Left Substack. Archive also holds {kinds['ainews']} AINews issues "
            "(counted under AINews); robots.txt disallows /api/.")
        row["_ainews_posts"] = [p for p in posts if p["kind"] == "ainews"]
        row["paid_12mo"] = None
    elif src["platform"] == "substack":
        try:
            posts = list_substack_archive(sess, src["site"], since)
            aud = Counter(p["audience"] for p in posts)
            kinds = Counter(p["kind"] for p in posts)
            row["count_12mo"] = len(posts)
            row["paid_12mo"] = sum(v for k, v in aud.items() if k != "everyone")
            row["archive"] = "Substack archive API (public)"
            if kinds.get("podcast"):
                row["notes"].append(f"{kinds['podcast']} are podcast posts")
        except RobotsDisallowed:
            row["count_12mo"] = row["feed_12mo"]
            row["archive"] = "API disallowed by robots.txt"
            row["paid_12mo"] = None
    elif src["id"] == "tomtunguz":
        row["count_12mo"] = len(list_tunguz_archive(sess, since))
        row["paid_12mo"] = 0
        row["archive"] = "public /archive/ page (all posts, dated)"
        row["notes"].append(f"feed only has {row['feed_items']} recent items")
    elif src["id"] == "simonwillison":
        c = simonwillison_month_counts(sess, since, now_utc())
        row["count_12mo"] = c["entrie"] + c["link"]
        row["paid_12mo"] = 0
        row["archive"] = "public month archives (/YYYY/Mon/)"
        row["notes"].append(
            f"≈{c['posts']} items total: {c['entrie']} long-form entries, {c['link']} links "
            f"with commentary, {c['quote']} quotes, {c['note']} notes; count = entries+links "
            "(month pages since Nov 2025, slight over-count)")
    else:
        row["count_12mo"] = row["feed_12mo"]
        row["paid_12mo"] = 0
        row["archive"] = "feed covers 12 mo" if feed_covers_window else \
            f"feed only back to {row['feed_oldest']}; archive check needed"

    if not row["active_90d"]:
        row["notes"].append(f"STALE: last post {row['feed_newest']}")
    if row.get("feed_paywalled_share") and row["feed_paywalled_share"] >= 0.8 and not row.get("paid_12mo"):
        row["notes"].append("feed has excerpts only; full text is public on the site")
    if row.get("paid_12mo") and row.get("count_12mo"):
        share = row["paid_12mo"] / row["count_12mo"]
        if share >= 0.3:
            row["notes"].append(f"PAYWALL: {share:.0%} of posts are paid-only (preview text only)")
    return row


def verify_ainews(sess: PoliteSession, since, latentspace_row: dict | None) -> dict:
    src = next(s for s in SOURCES if s["id"] == "ainews")
    row = verify_source(sess, src, since, now_utc())
    smol = {e["url"] for e in list_feed(sess, src["feed"]) if e["date"] and e["date"] >= since}
    ls = latentspace_row.get("_ainews_posts", []) if latentspace_row else []
    last_smol = row["feed_newest"]
    ls_after = [p for p in ls if _fmt(p["date"]) > last_smol]
    row["count_12mo"] = len(smol) + len(ls_after)
    row["archive"] = "full history in RSS"
    row["active_90d"] = row["active_90d"] or bool(ls_after)
    row["feed_paywalled_share"] = None  # short RSS items are summaries; full issue is on the page
    row["notes"] = [n for n in row["notes"] if not n.startswith("STALE")]
    row["notes"].append("RSS has summaries only; full issue text (~6-7k words) is on each issue page.")
    row["notes"].append(
        f"news.smol.ai RSS stops {last_smol}; AINews moved to latent.space "
        f"(+{len(ls_after)} issues since). Feed has same-day duplicates to dedupe.")
    row["paid_12mo"] = 0
    return row


def verify_hn(sess: PoliteSession, since) -> dict:
    stories = list_ask_hn(sess, since)
    rel = [s for s in stories if is_relevant(s)]
    (OUT_DIR / "hn_candidates.json").write_text(json.dumps(
        [{**s, "date": s["date"].isoformat()} for s in rel], indent=1))
    return {
        "id": "hn", "name": "Hacker News — Ask HN", "author": "HN community",
        "voice": "community", "feed": "hn.algolia.com/api/v1",
        "feed_items": len(stories), "feed_newest": _fmt(stories[0]["date"]) if stories else "—",
        "feed_oldest": _fmt(stories[-1]["date"]) if stories else "—",
        "active_90d": True, "count_12mo": len(rel), "paid_12mo": 0,
        "feed_paywalled_share": 0, "archive": "Algolia API",
        "comments_in_relevant": sum(s["num_comments"] for s in rel),
        "notes": [f"{len(stories)} Ask HN threads with >=10 comments; "
                  f"{len(rel)} pass the keyword filter"],
    }


def to_markdown(rows: list[dict]) -> str:
    lines = [
        f"# Source verification — {now_utc():%Y-%m-%d %H:%M} UTC",
        "",
        "| Source | Voice | Active (90d) | Newest | Feed items (oldest) | 12-mo items | Paid/preview-only | Archive | Notes |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        paid = "—" if r.get("paid_12mo") is None else str(r["paid_12mo"])
        if r.get("feed_paywalled_share"):
            paid += f" (feed {int(r['feed_paywalled_share'] * 100)}% short)"
        lines.append(
            f"| {r['name']} | {r['voice']} | {'yes' if r['active_90d'] else '**NO**'} | "
            f"{r['feed_newest']} | {r['feed_items']} ({r['feed_oldest']}) | "
            f"**{r['count_12mo']}** | {paid} | {r['archive']} | {'; '.join(r['notes'])} |")
    total = sum(r["count_12mo"] for r in rows)
    lines += ["", f"**Total 12-month items: {total}**"]
    return "\n".join(lines)


def main(only: list[str] | None = None):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sess = PoliteSession()
    since, recent = window_start(), window_start(RECENT_DAYS)
    rows, ls_row = [], None
    ordered = sorted(SOURCES, key=lambda s: s["id"] != "latentspace")  # LS first (feeds AINews)
    for src in ordered:
        if src["id"] == "ainews" or (only and src["id"] not in only):
            continue
        print(f"… {src['id']}", file=sys.stderr, flush=True)
        try:
            row = verify_source(sess, src, since, recent)
        except Exception as e:  # keep going; report the failure in the table
            traceback.print_exc()
            row = {"id": src["id"], "name": src["name"], "voice": src["voice"],
                   "active_90d": False, "feed_newest": "—", "feed_items": 0,
                   "feed_oldest": "—", "count_12mo": 0, "paid_12mo": None,
                   "archive": "ERROR", "notes": [repr(e)[:120]]}
        if src["id"] == "latentspace":
            ls_row = row
        rows.append(row)
    if not only or "ainews" in only:
        print("… ainews", file=sys.stderr, flush=True)
        rows.insert(0, verify_ainews(sess, since, ls_row))
    if not only or "hn" in only:
        print("… hn", file=sys.stderr, flush=True)
        rows.append(verify_hn(sess, since))

    for r in rows:
        r.pop("_ainews_posts", None)
    (OUT_DIR / "source_verification.json").write_text(json.dumps(rows, indent=1, default=str))
    md = to_markdown(rows)
    (OUT_DIR / "source_verification.md").write_text(md)
    print(md)


if __name__ == "__main__":
    main(sys.argv[1:] or None)
