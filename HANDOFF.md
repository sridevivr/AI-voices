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

## Where things stand (2026-11-22, after the v2 run)
- Data: 30,139 findings from 20 sources (19 newsletters/blogs/HN + 37 curated Bluesky accounts), 1,231 themes.
- Outputs in `data/out/insights/`: five SHORT v2 reports (`state_of_ai.md`, `debates.md`, `trends.md`,
  `tools_guide.md`, `voices.md`; replies in `replies.json`, audited and hand-fixed, see CLAUDE.md item 16),
  `overview.md` ("The numbers"), `app_ideas.md` + `app_ideas.csv` (NOT on the web page by the owner's request),
  and the web page `site/index.html`.
- Web page (private Artifact): https://claude.ai/artifact/LcSyqw1ZZwQFEwWcT7uuuq — version 4 = the v2 reports with
  icons, big numbers, pull quotes, Year in AI strip, heatmap, bubble chart, debate side chips, voices map.
- Spend: $23.87 of the $40 cap (see `data/out/spend.json`); the owner has a $100 promo grant.

## How to audit a fresh `write --yes` (free, here)
1. Every number in the text appears in `insights.prompt_for(pack, name)`; every evidence id is in `_allowed`.
2. Source-agreement wording: the rule uses the SIX biggest sources. Sonnet twice wrote "all five" / "every big
   source" for safety & governance (5 of 6). Check `big_sources_up/down` in pack.json trends.
3. People chips: a chip must be someone who holds the card's view, not someone who mocked or opposed it.
4. Debates: two sides first, "Why it matters" last.
5. Fix by hand in `replies.json`, then `python -m src.insights render` and `site`; record fixes in CLAUDE.md.
6. Look at the page with Playwright (wrap the file in a doctype shell; desktop light 1280px + phone dark 390px;
   click each tab). Republish: Artifact `read` the URL first, then publish `site/index.html` with that `url`.

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
