"""Shared configuration: paths, source registry, constants.

The source registry is reused by the backfill and (later) the daily digest.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RAW_DIR = DATA / "raw"
BATCH_DIR = DATA / "batches"
OUT_DIR = DATA / "out"

USER_AGENT = (
    "AIVoicesDigest/0.1 (personal research backfill of public AI commentary; "
    "+https://github.com/sridevivr/ai-voices)"
)

# Minimum seconds between requests to the same host.
PER_HOST_DELAY = 1.5
REQUEST_TIMEOUT = 30

BACKFILL_DAYS = 365
RECENT_DAYS = 90


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def window_start(days: int = BACKFILL_DAYS) -> datetime:
    return now_utc() - timedelta(days=days)


# voice: builders | researchers | business | news | community
# platform: substack (cursor archive API available) | feed (plain RSS/Atom)
SOURCES: list[dict] = [
    {"id": "ainews", "name": "AINews (smol.ai)", "author": "swyx / smol.ai",
     "site": "https://news.smol.ai", "feed": "https://news.smol.ai/rss.xml",
     "platform": "feed", "voice": "news"},
    {"id": "simonwillison", "name": "Simon Willison's Weblog", "author": "Simon Willison",
     "site": "https://simonwillison.net", "feed": "https://simonwillison.net/atom/everything/",
     "platform": "feed", "voice": "builders"},
    {"id": "latentspace", "name": "Latent Space", "author": "swyx & Alessio Fanelli",
     "site": "https://latent.space", "feed": "https://latent.space/feed",
     "platform": "substack", "voice": "builders"},
    # Chip Huyen dropped: no posts since Jan 2025.
    {"id": "hamel", "name": "Hamel Husain", "author": "Hamel Husain",
     "site": "https://hamel.dev", "feed": "https://hamel.dev/index.xml",
     "platform": "feed", "voice": "builders"},
    {"id": "eugeneyan", "name": "Eugene Yan", "author": "Eugene Yan",
     "site": "https://eugeneyan.com", "feed": "https://eugeneyan.com/rss/",
     "platform": "feed", "voice": "builders"},
    {"id": "interconnects", "name": "Interconnects", "author": "Nathan Lambert",
     "site": "https://www.interconnects.ai", "feed": "https://www.interconnects.ai/feed",
     "platform": "substack", "voice": "researchers"},
    {"id": "raschka", "name": "Ahead of AI", "author": "Sebastian Raschka",
     "site": "https://magazine.sebastianraschka.com", "feed": "https://magazine.sebastianraschka.com/feed",
     "platform": "substack", "voice": "researchers"},
    {"id": "importai", "name": "Import AI", "author": "Jack Clark",
     "site": "https://importai.substack.com", "feed": "https://importai.substack.com/feed",
     "platform": "substack", "voice": "researchers"},
    {"id": "understandingai", "name": "Understanding AI", "author": "Timothy B. Lee",
     "site": "https://www.understandingai.org", "feed": "https://www.understandingai.org/feed",
     "platform": "substack", "voice": "business"},
    {"id": "oneusefulthing", "name": "One Useful Thing", "author": "Ethan Mollick",
     "site": "https://www.oneusefulthing.org", "feed": "https://www.oneusefulthing.org/feed",
     "platform": "substack", "voice": "business"},
    {"id": "exponentialview", "name": "Exponential View", "author": "Azeem Azhar",
     "site": "https://www.exponentialview.co", "feed": "https://www.exponentialview.co/feed",
     "platform": "substack", "voice": "business"},
    {"id": "tomtunguz", "name": "Tomasz Tunguz", "author": "Tomasz Tunguz",
     "site": "https://tomtunguz.com", "feed": "https://tomtunguz.com/index.xml",
     "platform": "feed", "voice": "business"},
    {"id": "lenny", "name": "Lenny's Newsletter", "author": "Lenny Rachitsky",
     "site": "https://www.lennysnewsletter.com", "feed": "https://www.lennysnewsletter.com/feed",
     "platform": "substack", "voice": "business"},
    {"id": "bensbites", "name": "Ben's Bites", "author": "Ben Tossell",
     "site": "https://www.bensbites.com", "feed": "https://www.bensbites.com/feed",
     "platform": "substack", "voice": "builders"},
    {"id": "garymarcus", "name": "Marcus on AI", "author": "Gary Marcus",
     "site": "https://garymarcus.substack.com", "feed": "https://garymarcus.substack.com/feed",
     "platform": "substack", "voice": "researchers"},
    {"id": "normaltech", "name": "AI as Normal Technology", "author": "Arvind Narayanan & Sayash Kapoor",
     "site": "https://www.normaltech.ai", "feed": "https://www.normaltech.ai/feed",
     "platform": "substack", "voice": "researchers"},
    {"id": "zvi", "name": "Don't Worry About the Vase", "author": "Zvi Mowshowitz",
     "site": "https://thezvi.substack.com", "feed": "https://thezvi.substack.com/feed",
     "platform": "substack", "voice": "researchers"},
    {"id": "algobridge", "name": "The Algorithmic Bridge", "author": "Alberto Romero",
     "site": "https://www.thealgorithmicbridge.com", "feed": "https://www.thealgorithmicbridge.com/feed",
     "platform": "substack", "voice": "business"},
]

SOURCES_BY_ID = {s["id"]: s for s in SOURCES}

# --- Hacker News (Algolia) ---------------------------------------------------
HN_API = "https://hn.algolia.com/api/v1"
HN_MIN_COMMENTS = 10  # skip Ask HN threads nobody engaged with

# A thread is kept if it is an Ask/Tell HN post AND either its title matches a strong
# "tool I wish existed" phrase, OR its title mentions AI and (title or text) asks for
# tools/workflows or the title is a question.
HN_AI_TERMS = [
    r"\bai\b", r"\bllms?\b", r"\bgpt", r"chatgpt", r"\bclaude\b", r"\bgemini\b",
    r"copilot", r"\bcursor\b", r"\bagents?\b", r"agentic", r"\brag\b", r"embedding",
    r"\bprompts?\b", r"openai", r"anthropic", r"\bmcp\b", r"vibe.?cod", r"machine learning",
    r"\bml\b", r"language model", r"codex", r"windsurf", r"ollama", r"local model",
]
HN_NEED_TERMS = [
    r"what (do|does|are) (you|your|people|y'?all|hn) use", r"what tools?",
    r"\bhow (do|are) you\b", r"is there (a|an|any) (tool|app|service|way)",
    r"wish (there was|there were|existed|i had)", r"looking for (a|an)",
    r"alternatives? to", r"would (you )?pay for", r"pain ?points?", r"frustrat",
    r"struggl", r"\bannoy", r"workflow", r"\bstack\b", r"recommend",
    r"what('s| is) (missing|broken|hard)", r"anyone (built|building|using)",
    r"\bhate\b", r"doesn'?t work", r"productiv",
]
HN_STRONG_TITLE_TERMS = [
    r"wish (there was|there were|existed|i had)", r"is there (a|an|any) (tool|app|service)",
    r"what (tool|app|software) do you wish", r"would (you )?pay for",
    r"what problems? .* solv", r"what('s| is) a tool",
]
