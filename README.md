# AI Voices Digest

Mines AI commentary (newsletters, blogs, Ask HN) for app ideas. First run: a 12-month
historical backfill. Later: the same pipeline, run daily.

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
# Put ANTHROPIC_API_KEY=... in .env (git-ignored). Only the extract/synthesize steps read it.
```

## Pipeline (each step is its own script)

| Step | Script | Output |
|---|---|---|
| 1. Verify sources | `python -m src.verify_sources` | `data/out/source_verification.{md,json}`, `data/out/hn_candidates.json` |
| 2. Fetch | `python -m src.fetch` *(next)* | `data/raw/<source>/<date>_<slug>.json` |
| 3–6. Extract (Haiku, Batches API) | `python -m src.extract` *(next)* | `data/batches/`, `data/out/findings.csv` |
| 7. Synthesize (Sonnet) | `python -m src.synthesize` *(next)* | `data/out/opportunities.md`, `themes.json` |

Modules: `src/config.py` (source registry, keyword filters), `src/http_client.py`
(polite fetching: UA, per-host rate limit, robots.txt, retries), `src/feeds.py`
(RSS/Atom, Substack archive API, site-specific archives), `src/hn.py` (Algolia Ask HN).
