# AI Voices Digest — project brief for Claude

One-time 12-month backfill that mines AI commentary for app ideas; later the same
pipeline runs as a daily digest. Keep fetch / extract / synthesize as separate scripts.

## Hard rules (from the owner)
- NEVER read, print, cat, or echo `.env` or the API key. Never commit it.
- The API key is ONLY for the pipeline scripts (`src/extract.py`, `src/synthesize.py`).
  It comes from `ANTHROPIC_API_KEY` (set on the "ai-voices" cloud environment) or `.env`.
- Deadline: Anthropic credits expire Nov 16 2026 (UTC); **all batch jobs submitted by Sat Nov 14**.
- Budget ~$40 total. Show a cost estimate and WAIT for OK before any batch over $2.
  If total spend would pass $40, stop and ask. Spend is logged in `data/out/spend.json`.
- No Opus, no web search, unless the owner approves.
- Extraction: `claude-haiku-5-5`, Message Batches, structured outputs, every request
  under 100K input tokens (Haiku price jumps above that), shared instructions first with
  1-hour `cache_control`. Synthesis: `claude-sonnet-5-5`.
- The GitHub repo is PUBLIC: do not commit fetched article text (`data/raw/`, `data/batches/`
  are git-ignored). Outputs in `data/out/` (short quotes + links) are fine.
- Fetch politely: descriptive User-Agent, 1.5 s per host, robots.txt (see `src/http_client.py`).

## Source decisions (made 2026-11-10)
- Skip paid-only Substack posts (only previews are public).
- Simon Willison: long-form entries + commented links only (no quotes/notes).
- Chip Huyen dropped (no posts in 12 months). Eugene Yan kept (5 posts).
- Ask HN: tightened filter (`src/hn.py:is_relevant`): Ask/Tell HN with an AI term in the title → 342 threads
  (mostly on-topic; some general AI-industry chatter). Top 25 comments + 2 replies each.
- AINews moved from news.smol.ai to latent.space in Sep 2026; both are fetched (see `src/fetch.py`).

## Pipeline status / plan
1. Verify sources — DONE (`data/out/source_verification.md`).
2. Fetch — `python -m src.fetch` (≈20 min; resumable; skips existing files).
   Raw data is NOT in git, so a new session must re-run this first.
3. Cost estimate — `python -m src.extract estimate` (free token counting). Show owner, wait for OK.
4–5. Pilot — `python -m src.extract pilot` (20 items: AINews + HN + blogs). Show 10 example
   findings + actual cost; WAIT for owner's OK.
6. Full run — `python -m src.extract submit --est <dollars> --yes` then `python -m src.extract collect`
   (saves raw results immediately, retries failures once), `python -m src.extract export`.
7–8. Synthesis with Sonnet → `data/out/opportunities.md`, `findings.csv`, `themes.json`, `run_log.md`
   (`src/synthesize.py`, not written yet).

The cloud environment "ai-voices" allows exactly the source hosts + hn.algolia.com.
Use `.venv/bin/python` (create with `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`).
