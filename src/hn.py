"""Hacker News "Ask HN" discovery via the Algolia API, with a local keyword filter."""
from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone

from .config import (HN_AI_TERMS, HN_API, HN_MIN_COMMENTS, HN_NEED_TERMS,
                     HN_STRONG_TITLE_TERMS)
from .feeds import html_to_text
from .http_client import PoliteSession

_AI = re.compile("|".join(HN_AI_TERMS), re.I)
_NEED = re.compile("|".join(HN_NEED_TERMS), re.I)
_STRONG = re.compile("|".join(HN_STRONG_TITLE_TERMS), re.I)
_ASK = re.compile(r"\s*(ask|tell) hn", re.I)


def list_ask_hn(session: PoliteSession, since: datetime, until: datetime | None = None,
                min_comments: int = HN_MIN_COMMENTS) -> list[dict]:
    """All Ask HN stories in [since, until) with >= min_comments, newest first.

    Queries in 7-day windows so no window exceeds Algolia's 1000-hit cap.
    """
    until = until or datetime.now(timezone.utc)
    out: dict[str, dict] = {}
    start = since
    while start < until:
        end = min(start + timedelta(days=7), until)
        params = {
            "tags": "ask_hn",
            "hitsPerPage": 1000,
            "numericFilters": f"created_at_i>={int(start.timestamp())},"
                              f"created_at_i<{int(end.timestamp())},"
                              f"num_comments>={min_comments}",
        }
        r = session.get(f"{HN_API}/search_by_date", params=params)
        r.raise_for_status()
        for h in r.json()["hits"]:
            out[h["objectID"]] = {
                "id": h["objectID"],
                "title": h.get("title") or "",
                "text": html_to_text(h.get("story_text") or ""),
                "author": h.get("author") or "",
                "date": datetime.fromtimestamp(h["created_at_i"], tz=timezone.utc),
                "points": h.get("points") or 0,
                "num_comments": h.get("num_comments") or 0,
                "url": f"https://news.ycombinator.com/item?id={h['objectID']}",
            }
        start = end
    return sorted(out.values(), key=lambda x: x["date"], reverse=True)


def is_relevant(story: dict) -> bool:
    title, body = story["title"], story.get("text", "")
    if not _ASK.match(title):
        return False
    if _STRONG.search(title):
        return True
    return bool(_AI.search(title) and (_NEED.search(f"{title}\n{body}") or title.rstrip().endswith("?")))


def fetch_thread(session: PoliteSession, story_id: str) -> dict:
    """Full item tree from Algolia (story + nested comments)."""
    r = session.get(f"{HN_API}/items/{story_id}")
    r.raise_for_status()
    return r.json()
