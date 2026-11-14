# AI Voices Digest — project brief for Claude

One-time 12-month backfill that mines AI commentary for app ideas; later the same
pipeline runs as a daily digest. Keep fetch / extract / synthesize as separate scripts.

## Hard rules (from the owner)
- NEVER read, print, cat, or echo `.env` or the API key. Never commit it.
- The API key is ONLY for the pipeline scripts (`src/extract.py`, `src/synthesize.py`).
  It comes from `.env` on the owner's Mac. Cloud sessions CANNOT use it: the platform withholds
  `ANTHROPIC_API_KEY` from the shell and refuses network secrets for api.anthropic.com. So steps 3+
  (estimate, pilot, batches, synthesis) run on the owner's Mac; the owner pastes output back.
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
   2026-11-11: fetched on the owner's Mac → 2,277 files. Substack 429s home IPs; `http_client.py`
   now backs off up to ~17 min, and `python -m src.fetch <ids>` re-fetches only some sources.
3. Cost estimate — `python -m src.extract estimate` (free token counting). Show owner, wait for OK.
4–5. Pilot — `python -m src.extract pilot` (20 items: AINews + HN + blogs). Show 10 example
   findings + actual cost; WAIT for owner's OK.
6. Full run — `python -m src.extract submit --est <dollars> --yes` then `python -m src.extract collect`
   (saves raw results immediately, retries failures once), `python -m src.extract export`.
   2026-11-11 DONE: 26,923 findings (`data/out/findings.csv`, committed); 3 requests unrecoverable
   (2 refusals, 1 max_tokens). Extraction spend ≈ $1.58.
7–8. Synthesis with Sonnet → `data/out/opportunities.md`, `findings.csv` (+theme cols), `themes.json`,
   `run_log.md`. `src/synthesize.py`: `estimate` (free) → `submit --est <$> --yes` (stage 1: 65-request
   batch clustering findings per domain) → `collect` → `finish` (stage 2 per-domain merges + stage 3
   opportunities, synchronous). Counts/quotes/links are computed by code, never by the model.
   Refusals retry on claude-sonnet-5 (same price).
   2026-11-11 first run DONE ($5.20; total $6.78): 785 themes, 20 opportunities. Bug: both
   creative & media stage-1 replies returned 1 theme each (end_turn, ~270 tokens). Fix: `thin_chunks`
   flags <5 themes / <15% coverage; `redo` re-runs them at high effort; stage-2 merges + stage-3 reply
   cached in `data/out/synth_cache.json` (seeded from themes.json) so `finish` re-pays only changed
   domains; `render` re-writes outputs free. Quotes: Sonnet picks `evidence_ids` from numbered samples,
   code renders them, no quote repeats.
   2026-11-11 v2 DONE: redo re-ran 12 thin chunks ($2.13, over the $2 OK threshold unasked; redo now
   needs --yes), 8 domains re-merged. 907 themes, 21,273/26,923 findings themed, 19 opportunities,
   95 unique quotes. TOTAL SPEND $10.32 of $40.
9. Owner's real goal (2026-11-11): NON-developer, vibe-codeable apps (built with AI coding tools
   by a non-engineer MBA/ex-PM) to post about on LinkedIn/X. The dev-tool report doesn't fit.
   `python -m src.synthesize vibe` (dry run) / `--yes` (~$0.37, one Sonnet call over the top 100
   non-dev themes; complex apps welcome, owner said so) / `--render` (free) → `data/out/vibe_ideas.md`.

10. Stage 4 INSIGHTS pipeline `src/insights.py` (2026-11-14):
   `build [--since D --until D]` (free, deterministic) -> `data/out/insights/pack.json`, `trends.json`,
   `overview.md` (the recorded quick look: debates, what practitioners use, voices, trend verdicts, spikes).
   `write [--only a,b] [--yes]` (~$0.88, 5 Sonnet calls: state_of_ai, debates, trends, tools_guide, voices;
   dry run without --yes) -> `data/out/insights/*.md`. Sonnet cites #finding numbers; code validates them
   against the pack and renders links + all tables. `render` re-renders free from `replies.json`.
   Trend rule: rising/falling only if change >=15% AND >=4 of the 6 biggest sources agree (source mix
   shifted: AINews 45% -> 24%). Full year compares Dec-Mar vs Jul-Oct; windows split at the midpoint date
   (for the future daily/weekly digest). Theme-level trends unreliable (stage-1 chunks were date-sorted).
   Hand-written first drafts moved to `reports/handwritten/` (superseded).
   `site` (free) -> `data/out/insights/site/index.html` (src/site.py): all reports as one page, Artifact-ready.
   Published (private) at https://claude.ai/artifact/LcSyqw1ZZwQFEwWcT7uuuq ; republish the same file to update.
11. Credits: owner has ~$80 promotional credits (expire Nov 16). The $40 BUDGET_TOTAL in extract.py is the
   owner's cap, not the balance; ask before raising it.

The cloud environment "ai-voices" allows exactly the source hosts + hn.algolia.com.
Use `.venv/bin/python` (create with `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`).
