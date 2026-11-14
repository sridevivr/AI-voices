"""Free, deterministic insight tables from data/out/findings.csv (no API calls).

Usage:
    python -m src.insights trends                 # data/out/trends.json + printed tables
    python -m src.insights cite <draft.md> <out.md>   # replace [[cite:text]] markers with source links

Trends compare Nov 2025-Feb 2026 ("early") with Jul-Oct 2026 ("late"), per 1,000 findings. Because
the source mix changed a lot over the year (AINews fell from 45% to 24% of findings), each row also
counts how many of the six biggest sources show the same change on their own; only changes most of
them agree on should be called trends.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict

from .config import OUT_DIR

EARLY = {"2025-11", "2025-12", "2026-01", "2026-02"}
LATE = {"2026-07", "2026-08", "2026-09", "2026-10"}
BIG = ["AINews (smol.ai)", "Don't Worry About the Vase", "Hacker News — Ask HN", "Latent Space",
       "Simon Willison's Weblog", "Ben's Bites"]

TERMS = {
    # products
    "ChatGPT": r"\bchatgpt\b", "Claude Code": r"claude code", "Codex": r"\bcodex\b",
    "Cursor": r"\bcursor\b", "Gemini": r"\bgemini\b", "GitHub Copilot": r"\bcopilot\b",
    "Lovable": r"\blovable\b", "Perplexity": r"\bperplexity\b", "NotebookLM": r"notebooklm",
    "DeepSeek": r"deepseek", "Qwen": r"\bqwen", "Kimi": r"\bkimi\b", "OpenClaw": r"openclaw|clawdbot|moltbot",
    "Manus": r"\bmanus\b", "Ollama/LM Studio": r"ollama|lm studio", "OpenRouter": r"openrouter",
    "Nano Banana": r"nano banana", "ElevenLabs": r"elevenlabs", "Fable": r"\bfable\b",
    # concepts
    "MCP": r"\bmcp\b", "Skills (agent)": r"\bskills?\b", "AGENTS.md/CLAUDE.md": r"agents\.md|claude\.md",
    "vibe coding": r"vibe.?cod", "agents/agentic": r"\bagents?\b|agentic",
    "subagents/parallel agents": r"sub-?agents?|parallel agents|multiple agents|agent teams?",
    "background/async agents": r"background agents?|async agents?|cloud agents?|long-running",
    "context window/compaction": r"compaction|context window|context rot", "memory": r"\bmemory\b",
    "prompt injection": r"prompt injection", "sandbox": r"sandbox", "evals": r"\bevals?\b|evaluation",
    "RAG": r"\brag\b|retrieval", "fine-tuning": r"fine-?tun",
    "computer use/browser agents": r"computer use|browser agent|computer-use", "voice": r"\bvoice\b|speech",
    "image generation": r"image generation|image model|\bimage\b", "robotics": r"robot|humanoid|embodied",
    "local/open weights": r"open.?weight|open.?source model|local model|run locally",
    "Chinese models": r"chinese|china", "sycophancy": r"sycophan", "slop": r"\bslop\b",
    "hallucination": r"hallucinat", "AGI/superintelligence": r"\bagi\b|superintelligen",
    "regulation/policy": r"regulat|legislat|policy|executive order|eu ai act",
    "jobs/layoffs": r"\bjobs?\b|layoff|unemploy|hiring",
    "pricing/rate limits": r"rate limit|usage limit|pricing|subscription|quota",
    "security": r"security|vulnerab|exploit", "cyber": r"\bcyber", "education/students": r"student|teacher|school|education",
    "healthcare": r"health|medical|doctor|clinic", "ads": r"\bads\b|advertis", "GPUs/Nvidia": r"\bgpus?\b|nvidia",
}


def load() -> list[dict]:
    with (OUT_DIR / "findings.csv").open(newline="") as f:
        return list(csv.DictReader(f))


def text(r: dict) -> str:
    return f"{r['summary']} {r['short_quote']}"


def trends(rows: list[dict]) -> dict:
    period = lambda r: "e" if r["date"][:7] in EARLY else "l" if r["date"][:7] in LATE else None
    tot, tot_src, per_month = Counter(), defaultdict(Counter), Counter(r["date"][:7] for r in rows)
    for r in rows:
        p = period(r)
        if p:
            tot[p] += 1
            tot_src[r["source"]][p] += 1

    def table(match, keys):
        out = []
        for k in keys:
            hits = [r for r in rows if match(r, k)]
            cnt, cs = Counter(), defaultdict(Counter)
            for r in hits:
                p = period(r)
                if p:
                    cnt[p] += 1
                    cs[r["source"]][p] += 1
            up = down = 0
            for s in BIG:
                e = cs[s]["e"] / max(tot_src[s]["e"], 1)
                l = cs[s]["l"] / max(tot_src[s]["l"], 1)
                up += l > e * 1.15
                down += l < e / 1.15
            months = Counter(r["date"][:7] for r in hits)
            e1k, l1k = 1000 * cnt["e"] / tot["e"], 1000 * cnt["l"] / tot["l"]
            out.append({"key": k, "findings": len(hits), "early_per_1k": round(e1k, 1),
                        "late_per_1k": round(l1k, 1), "ratio": round((l1k + 0.5) / (e1k + 0.5), 2),
                        "big_sources_up": up, "big_sources_down": down,
                        "monthly_per_1k": {m: round(1000 * months[m] / per_month[m], 1)
                                           for m in sorted(per_month)}})
        return sorted(out, key=lambda x: -x["ratio"])

    rx = {k: re.compile(v, re.I) for k, v in TERMS.items()}
    return {
        "method": __doc__.split("\n\n")[1].strip(),
        "sources_per_period": {s: dict(c) for s, c in tot_src.items()},
        "domains": table(lambda r, k: r["domain"] == k, sorted({r["domain"] for r in rows})),
        "types": table(lambda r, k: r["type"] == k, sorted({r["type"] for r in rows})),
        "terms": table(lambda r, k: bool(rx[k].search(text(r))), list(TERMS)),
    }


def cite(draft: str, out: str, rows: list[dict]):
    """[[cite:some exact text]] -> (Source, date, link) for the one finding whose summary or quote
    contains that text. Fails loudly if none or several match, so no link is guessed."""
    md = open(draft).read()
    errors = []

    def repl(m):
        needle = m.group(1).lower()
        hits = [r for r in rows if needle in text(r).lower()]
        urls = {r["url"] for r in hits}
        if len(urls) != 1:
            errors.append(f"{len(urls)} matches for: {m.group(1)}")
            return m.group(0)
        r = hits[0]
        return f"([{r['source']}, {r['date']}]({r['url']}))"

    md = re.sub(r"\[\[cite:(.+?)\]\]", repl, md)
    if errors:
        sys.exit("Unresolved citations:\n  " + "\n  ".join(errors))
    open(out, "w").write(md)
    print(f"wrote {out}")


def main():
    rows = load()
    if sys.argv[1:2] == ["trends"]:
        t = trends(rows)
        (OUT_DIR / "trends.json").write_text(json.dumps(t, indent=1, ensure_ascii=False))
        for name in ("domains", "types", "terms"):
            print(f"== {name} (per 1k findings, early -> late, big sources up/down) ==")
            for x in t[name]:
                print(f"{x['key']:28} {x['findings']:5} {x['early_per_1k']:6.1f} -> {x['late_per_1k']:6.1f}"
                      f"  x{x['ratio']:<5} up {x['big_sources_up']} / down {x['big_sources_down']}")
    elif sys.argv[1:2] == ["cite"]:
        cite(sys.argv[2], sys.argv[3], rows)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
