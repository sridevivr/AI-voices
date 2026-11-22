# Handoff: AI Voices Digest — continue from "short reports + visuals"

You are continuing the AI Voices Digest project on branch `claude/tender-euler-8h2rjb` (repo sridevivr/ai-voices,
public). Read `CLAUDE.md` first: it has the hard rules (never read `.env`/the API key; API steps run only on the
owner's Mac, the owner pastes output back; show a cost estimate and wait for OK before anything over $2; $40 budget
cap in `src/extract.py` BUDGET_TOTAL, ask before raising it; no Opus, no web search; repo is public, never commit
`data/raw/` or `data/batches/`) and the full pipeline history (items 1–16).

## Who the owner is and what they want
An MBA, ex-program manager at a large enterprise software company, non-engineer who vibe-codes apps and posts on
LinkedIn/X. Plain, direct explanations; exact commands in separate ```bash blocks; say what each step costs and what
its outcome is. They care about readability of the outputs, not internals.

## Where things stand (2026-11-22)
- Data: 30,139 findings from 20 sources (19 newsletters/blogs/HN + 37 curated Bluesky accounts), 1,231 themes.
- Outputs in `data/out/insights/`: reports (`state_of_ai.md`, `debates.md`, `trends.md`, `tools_guide.md`,
  `voices.md`), `overview.md` ("The numbers"), `app_ideas.md` + `app_ideas.csv` (63 ideas, 11 start-here; NOT on the
  web page by the owner's request), and the web page `site/index.html`.
- Web page (private Artifact): https://claude.ai/artifact/LcSyqw1ZZwQFEwWcT7uuuq — tabs State of AI, Debates, Trends,
  Tools, Voices. Currently version 3 (card layout of the OLD long reports).
- Spend: about $23.24 of the $40 cap (see `data/out/spend.json`); the owner has a $100 promo grant.

## What was just built (committed, f2bfb6e) — not yet run for real
- `src/insights.py`: v2 short report schema (key_points {headline, detail}; sections {heading, takeaway, stat_value,
  stat_label, cards[{label, text ≤45 words, people, evidence_ids}], post_angle}; moments[]; voice_positions[]), hard
  word limits in WRITER, rewritten REPORTS tasks, `validate()` (drops stats whose numbers aren't in the prompt,
  people not in the prompt, unknown voices, invalid months; reports over-long text into `_notes`), `render_report_v2`
  for Markdown, and `theme_growth` added to `build`.
- `src/site.py`: v2 renderers (used when a reply's sections have `cards`; old replies fall back to v1 renderers):
  topic icons, section headers with big numbers, one verified pull quote per section (no repeats), "Year in AI"
  strip (moments; fallback = spike terms), attention heatmap (per-row min–max shading), big-vs-growing bubble chart
  (collision-free labels, scrolls sideways on phones), debate side chips, voices map (5×5 grid).
- Tested here with converted fake replies and injected errors: every check fired; no overflow or JS errors at
  1280px light and 390px dark.

## The owner is running these on their Mac (may already be done; ask for the output if not pasted)
1. `git pull`  2. `.venv/bin/python -m src.insights build` (free)
3. `.venv/bin/python -m src.insights write --yes` (~$0.74; prints any validation notes)
4. `.venv/bin/python -m src.insights site`  5. `git add data/out && git commit -m "Short reports + visuals" && git push`

## Your next steps
1. `git pull origin claude/tender-euler-8h2rjb`, confirm `data/out/insights/replies.json` replies are v2 (sections
   have `cards`) and read each reply's `_notes`.
2. Audit every report (free, here): (a) every number in the text appears in that report's prompt
   (`insights.prompt_for(pack, name)`), (b) every evidence id is in the reply's `_allowed`, (c) people chips and
   voice positions look plausible against the cited findings, (d) word counts: card text ≤45, takeaway ≤20, total
   per report ~500–800 words, (e) spot-check a few cards against their cited findings. Fix small wording errors in
   `replies.json` by hand (record it in CLAUDE.md, as done once before), then `python -m src.insights render` and
   `python -m src.insights site` (both free).
3. Look at the real page once (Playwright: wrap the file in a doctype/head/body shell; Chromium is preinstalled),
   desktop light + phone dark, all five tabs; check charts, pull quotes, no overflow.
4. Republish to the SAME artifact: in a new session you must first `Artifact` action `read` with the URL above, then
   publish `data/out/insights/site/index.html` with `url` set to that URL (no `icon`). Tell the owner it stays private
   until they share it.
5. Commit and push any fixes; update CLAUDE.md (item 16 status).
6. Report back briefly: what changed, any fixes made, spend total.

## Possible next work (only if the owner asks)
- Build plan + launch post for one app idea from `app_ideas.md` (start-here list).
- Weekly digest: `fetch` recent items (incl. `fetch bluesky --days 14`), `extract`, `insights build --since/--until`.
- Note: `src/synthesize.py vibe` and the opportunities report are older dev-oriented outputs; app ideas supersede them.

## Gotchas
- The cloud session cannot call the Anthropic API (key withheld); never try. Network allows the source hosts,
  hn.algolia.com and public.api.bsky.app only.
- `insights build` rewrites pack.json, but replies keep their own `_allowed` evidence, so re-rendering is safe.
- `redo`, `write`, `ideas`, `vibe` are dry runs without `--yes`; never run paid steps yourself (you can't anyway).
- Use `.venv/bin/python`; create it with `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`.
