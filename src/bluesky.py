"""Bluesky source: public posts from a curated list of AI voices, via the public AppView API.

No login is needed for profiles and author feeds (keyword search requires a login, so we use a curated
account list instead). One raw item = one account's posts for one ISO week, with every post's URL, date
and engagement kept in `posts`, so extracted findings can be linked back to the exact post (see
`post_for_quote`). Only complete weeks are written, so a re-run never freezes a half-finished week.

    python -m src.fetch bluesky             # last 365 days
    python -m src.fetch bluesky --days 14   # recent weeks only (digest)
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone

from .http_client import PoliteSession

API = "https://public.api.bsky.app/xrpc"
SOURCE = {"id": "bluesky", "name": "Bluesky", "voice": "community", "author": ""}

# handle -> (voice, ai_focused). ai_focused accounts keep every post of 6+ words; general accounts keep
# only posts that mention AI (see AI_TERMS). Verified 2026-11-16 with app.bsky.actor.getProfiles; handles
# that turned out to be impostors or empty (e.g. jackclark.bsky.social, paulgraham.bsky.social) were left out.
ACCOUNTS = {
    # builders and practitioners
    "simonwillison.net": ("builders", True), "swyx.io": ("builders", True), "hamel.bsky.social": ("builders", True),
    "eugeneyan.com": ("builders", True), "howard.fm": ("builders", True), "geoffreylitt.com": ("builders", True),
    "maggieappleton.com": ("builders", True), "wattenberger.com": ("builders", True), "charity.wtf": ("builders", False),
    "gergely.pragmaticengineer.com": ("builders", False), "antirez.bsky.social": ("builders", False),
    "kentcdodds.com": ("builders", False), "karpathy.bsky.social": ("builders", True),
    "thomwolf.bsky.social": ("builders", True), "clem.hf.co": ("builders", True), "alexalbert.bsky.social": ("builders", True),
    "chiphuyen.bsky.social": ("builders", True),
    # researchers
    "emollick.bsky.social": ("researchers", True), "natolambert.bsky.social": ("researchers", True),
    "rasbt.bsky.social": ("researchers", True), "garymarcus.bsky.social": ("researchers", True),
    "randomwalker.bsky.social": ("researchers", True), "sayash.bsky.social": ("researchers", True),
    "mmitchell.bsky.social": ("researchers", True), "emilymbender.bsky.social": ("researchers", True),
    "melaniemitchell.bsky.social": ("researchers", True), "yoshuabengio.bsky.social": ("researchers", True),
    "rao2z.bsky.social": ("researchers", True), "hardmaru.bsky.social": ("researchers", True),
    # journalists, writers, commentators
    "binarybits.bsky.social": ("news", True), "benjedwards.com": ("news", False), "caseynewton.bsky.social": ("news", False),
    "bcmerchant.bsky.social": ("news", False), "edzitron.com": ("news", False), "molly.wiki": ("news", False),
    "mikecaulfield.bsky.social": ("news", False), "anildash.com": ("community", False), "hankgreen.bsky.social": ("community", False),
}

AI_TERMS = re.compile(
    r"\bai\b|\ba\.i\.|\bllms?\b|\bgpt|chatgpt|\bclaude\b|\bgemini\b|copilot|\bcursor\b|\bagents?\b|agentic|"
    r"\brag\b|embedding|\bprompts?\b|openai|anthropic|\bmcp\b|vibe.?cod|machine learning|language model|codex|"
    r"\bmodels?\b|chatbot|deepseek|\bqwen|mistral|llama|hugging ?face|neural|generative|genai|midjourney|"
    r"\bsora\b|perplexity|notebooklm|slop|hallucinat|benchmark|\bagi\b|superintelligen|nvidia|\bgpus?\b",
    re.I)
MIN_WORDS = 6


def _post_url(uri: str, handle: str) -> str:
    return f"https://bsky.app/profile/{handle}/post/{uri.rsplit('/', 1)[-1]}"


def _post_text(post: dict) -> str:
    rec = post.get("record") or {}
    text = (rec.get("text") or "").strip()
    emb = post.get("embed") or {}
    ext = emb.get("external") or (emb.get("media") or {}).get("external")
    if ext:
        text += f"\n  (link: {ext.get('title', '').strip()} — {ext.get('uri', '')})"
    rec_emb = emb.get("record") or {}
    quoted = rec_emb.get("record", rec_emb) if isinstance(rec_emb, dict) else {}
    if quoted.get("value", {}).get("text"):
        who = (quoted.get("author") or {}).get("handle", "someone")
        text += f"\n  (quoting @{who}: {quoted['value']['text'].strip()[:400]})"
    return text


def list_posts(s: PoliteSession, handle: str, since: datetime, ai_focused: bool) -> tuple[dict, list[dict]]:
    prof = s.get(f"{API}/app.bsky.actor.getProfile", params={"actor": handle}).json()
    posts, cursor = [], None
    while True:
        params = {"actor": handle, "limit": 100, "filter": "posts_and_author_threads"}
        if cursor:
            params["cursor"] = cursor
        r = s.get(f"{API}/app.bsky.feed.getAuthorFeed", params=params)
        r.raise_for_status()
        d = r.json()
        oldest = None
        for item in d.get("feed", []):
            if item.get("reason"):  # a repost of someone else's post
                continue
            p = item["post"]
            if p.get("author", {}).get("handle") != handle:
                continue
            created = datetime.fromisoformat(p["record"]["createdAt"].replace("Z", "+00:00"))
            oldest = created if oldest is None else min(oldest, created)
            if created < since:
                continue
            text = _post_text(p)
            if len(text.split()) < MIN_WORDS or (not ai_focused and not AI_TERMS.search(text)):
                continue
            posts.append({"url": _post_url(p["uri"], handle), "date": created.isoformat(), "text": text,
                          "likes": p.get("likeCount", 0), "replies": p.get("replyCount", 0),
                          "reposts": p.get("repostCount", 0)})
        cursor = d.get("cursor")
        # Pinned posts can be old, so stop only when a whole page is older than the window.
        if not cursor or not d.get("feed") or (oldest and oldest < since and len(d["feed"]) < 100) or \
                (oldest and oldest < since - timedelta(days=7)):
            break
    return prof, sorted(posts, key=lambda p: p["date"])


def fetch(writer, since: datetime):
    """Write one item per account per complete ISO week. `writer` is fetch.Writer('bluesky')."""
    s = PoliteSession()
    this_monday = (datetime.now(timezone.utc) - timedelta(days=datetime.now(timezone.utc).weekday())).replace(
        hour=0, minute=0, second=0, microsecond=0)
    for handle, (voice, ai_focused) in ACCOUNTS.items():
        try:
            prof, posts = list_posts(s, handle, since, ai_focused)
        except Exception as e:
            writer.failed += 1
            print(f"  ! bluesky {handle}: {e!r}"[:200], file=sys.stderr)
            continue
        name = prof.get("displayName") or handle
        weeks = defaultdict(list)
        for p in posts:
            d = datetime.fromisoformat(p["date"])
            weeks[(d - timedelta(days=d.weekday())).date()].append(p)
        for monday, wp in sorted(weeks.items()):
            start = datetime(monday.year, monday.month, monday.day, tzinfo=timezone.utc)
            if start >= this_monday:  # week not finished yet
                continue
            url = f"https://bsky.app/profile/{handle}#week-{monday:%G-W%V}"
            if writer.exists(start, url):
                continue
            lines = [f"Bluesky posts by {name} (@{handle}), week of {monday}", ""]
            for p in wp:
                lines.append(f"[{p['date'][:10]} · {p['likes']} likes · {p['replies']} replies] {p['text']}")
                lines.append("")
            writer.write(date=start, url=url, title=f"{name} on Bluesky, week of {monday}", text="\n".join(lines),
                         author=name, kind="bluesky_week", handle=handle, voice_override=voice, posts=wp)
        print(f"  bluesky {handle}: {len(posts)} posts in window", file=sys.stderr, flush=True)
    return writer


_norm = lambda s: re.sub(r"\W+", " ", s.lower()).strip()


def post_for_quote(item: dict, quote: str) -> dict | None:
    """The post in a bluesky_week item whose text contains the finding's quote (None if not found)."""
    q = _norm(quote)
    if not q:
        return None
    for p in item.get("posts") or []:
        if q in _norm(p["text"]):
            return p
    return None
