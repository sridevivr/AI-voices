# AI commentary trends, Nov 2025 → Nov 2026

*What rose and what fell across 26,923 findings from 19 sources. Every number here is reproducible: `python -m src.insights trends` writes [`trends.json`](trends.json). The interpretation is mine (Claude). Companion reports: [`state_of_ai_2026.md`](state_of_ai_2026.md) and [`tools_guide.md`](tools_guide.md).*

## How to read this

- **Early** = Nov 2025–Feb 2026, **late** = Jul–Oct 2026. Every figure is a count **per 1,000 findings** in that period, so a month with more articles doesn't automatically look busier.
- **The source mix shifted a lot.** AINews fell from 45% to 24% of findings, while Zvi and Latent Space grew. So the pooled numbers can move just because a different publication wrote more.
- **The safeguard:** for each row I also checked the six biggest sources (AINews, Zvi, Hacker News, Latent Space, Simon Willison, Ben's Bites) **one at a time**. A row is marked **rising** or **falling** only if the pooled change is at least 15% *and* at least four of the six move the same way with at most one disagreeing. Otherwise it's "mixed" (moved overall, but the sources disagree) or "flat".
- **Mentions of a product spike when it launches.** The monthly table at the end shows the shape, which is often more telling than the early-versus-late comparison.

## The five shifts that pass the test

1. **From building with AI to controlling it.** Safety and governance nearly doubled (68 → 128 per 1k), and security mentions rose 2.5× (16 → 41), both confirmed within almost every big source. "Cyber" went from almost absent to a steady topic from June onwards. The worry moved from "the AI makes things up" to "the AI can act, so what if it acts wrongly, or is attacked?"
2. **Hallucination fell out of the conversation** (13.4 → 5.1, falling in five of six sources), and so did sycophancy after a burst in November 2025 (3.8 → 1.3). Either models improved, or people stopped expecting otherwise. Probably both.
3. **Agents everywhere.** "Agent" or "agentic" now appears in 27% of findings (from 18%). Talk shifted towards agents that run in the background (+50%), agents that use a computer or browser (×2.2, rising in all six sources), and monitoring and cost tracking for them (observability ×1.4).
4. **Coding-tool chatter cooled, but coding didn't.** The coding agents domain fell from 13% to 10% of findings and devtools fell too, while people kept using these tools. Debating which coding tool to use gave way to discussing how to run agents well. Claude Code mentions **peaked in spring** (around 60–70 per 1k from February to April) and were back above 30 by October, so its "falling" label reflects a peak passing, not abandonment.
5. **Some once-hot topics faded:** RAG and retrieval (11 → 6), AI image generation (19 → 8), AI hardware and compute (27 → 15), healthcare (6 → 3), education (9 → 7), and context-window limits (10 → 7), as models' memory grew.

**Rising but mixed** (likely real, not confirmed by enough sources): open-weight and local models (16 → 34, three sources up and none down), evals (25 → 48), regulation and policy talk, Chinese models, cost and tokens, and debate findings overall.

**Not trending:** jobs and layoffs (flat at about 11 per 1k all year), memory, voice, prompt injection, and pricing and rate limits. These were constant background concerns, not waves.

## Hype cycles: launches and spikes

- **OpenClaw (Feb 2026):** a viral personal AI agent that spiked to 30 per 1k in February, together with a wave of security warnings ([Marcus on AI, 2026-02-01](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere)), then faded to almost nothing by summer. It's the clearest example this year of a viral consumer agent burning out over trust.
- **Fable 5 (Jun 2026):** Anthropic's top model arrived to complaints about over-cautious safety filters refusing ordinary biology and engineering questions ([AINews (smol.ai), 2026-06-09](https://news.smol.ai/issues/26-06-09-anthropic-claude-fable-5/)), then settled as a steady topic.
- **Gemini (Nov 2025):** 85 per 1k in launch month, from a run of Gemini launches and integrations (Deep Research in Gmail and Drive, the CLI, API features), then a decline to around 10 or below from June. In this builder-heavy dataset, Gemini drew attention at launches but not much day-to-day discussion.
- **Skills (from Dec 2025):** agent "skills", meaning reusable instruction packs, went from 5 to 40 per 1k by March, and stayed high. That's a durable change in how people customise AI, not a spike.
- **Robotics (Sep–Oct 2026):** rose to 21–28 per 1k, almost all from two sources (Latent Space and Understanding AI interviews and reporting on robot models). It's worth watching, but the sources are narrow.

## Domains

| | Findings | Early (per 1k) | Late (per 1k) | Change | Big sources ↑ / ↓ | Verdict |
|---|---|---|---|---|---|---|
| safety & governance | 2,487 | 68.2 | 128.0 | ×1.87 | 4 / 0 | **rising** |
| evals & testing | 2,296 | 72.6 | 102.8 | ×1.41 | 3 / 3 | mixed |
| observability & cost | 1,102 | 32.5 | 45.5 | ×1.39 | 5 / 1 | **rising** |
| agents & orchestration | 2,558 | 84.2 | 102.2 | ×1.21 | 4 / 0 | **rising** |
| enterprise adoption | 891 | 25.9 | 31.0 | ×1.2 | 2 / 2 | mixed |
| local & open models | 1,340 | 42.5 | 48.6 | ×1.14 | 5 / 1 | flat |
| research & capabilities | 1,378 | 53.4 | 58.4 | ×1.09 | 2 / 3 | flat |
| jobs & careers | 336 | 11.2 | 11.6 | ×1.04 | 1 / 5 | flat |
| productivity & knowledge work | 1,514 | 53.9 | 54.5 | ×1.01 | 2 / 2 | flat |
| business & markets | 1,093 | 40.5 | 37.7 | ×0.93 | 2 / 3 | flat |
| other | 247 | 9.2 | 8.3 | ×0.91 | 2 / 3 | flat |
| inference & infra | 1,517 | 60.9 | 54.7 | ×0.9 | 2 / 1 | flat |
| education & learning | 377 | 14.8 | 12.4 | ×0.85 | 0 / 5 | **falling** |
| creative & media | 766 | 34.5 | 28.9 | ×0.84 | 2 / 1 | mixed |
| data & pipelines | 514 | 22.0 | 17.8 | ×0.81 | 2 / 4 | mixed |
| coding agents | 3,331 | 128.9 | 100.4 | ×0.78 | 0 / 4 | **falling** |
| model training & fine-tuning | 1,005 | 46.4 | 36.0 | ×0.78 | 4 / 1 | mixed |
| consumer apps | 1,343 | 66.5 | 42.0 | ×0.64 | 2 / 3 | mixed |
| devtools & IDEs | 1,915 | 88.3 | 54.5 | ×0.62 | 1 / 3 | mixed |
| RAG & retrieval | 371 | 16.2 | 9.5 | ×0.6 | 1 / 4 | **falling** |
| hardware & compute | 542 | 27.4 | 15.3 | ×0.57 | 0 / 4 | **falling** |

## Finding types

| | Findings | Early (per 1k) | Late (per 1k) | Change | Big sources ↑ / ↓ | Verdict |
|---|---|---|---|---|---|---|
| debate | 2,265 | 71.8 | 91.9 | ×1.28 | 2 / 0 | mixed |
| workaround | 1,929 | 64.5 | 75.8 | ×1.17 | 4 / 1 | **rising** |
| build_request | 3,262 | 116.4 | 131.5 | ×1.13 | 2 / 0 | flat |
| link_shared | 292 | 10.3 | 10.7 | ×1.03 | 2 / 1 | flat |
| pain_point | 10,181 | 389.1 | 382.5 | ×0.98 | 2 / 0 | flat |
| tool_or_technique | 7,681 | 291.7 | 266.3 | ×0.91 | 0 / 4 | flat |
| tool_complaint | 1,313 | 56.1 | 41.3 | ×0.74 | 2 / 2 | mixed |

## Terms (mentioned in 50+ findings)

Matched by keyword in each finding's summary and quote, so they're approximate. For example, "Claude" also matches "Claude Code", and "image" matches some non-generation uses.

| | Findings | Early (per 1k) | Late (per 1k) | Change | Big sources ↑ / ↓ | Verdict |
|---|---|---|---|---|---|---|
| Fable | 244 | 0.0 | 15.5 | ×32.03 | 6 / 0 | **rising** |
| cyber | 212 | 2.1 | 16.2 | ×6.51 | 5 / 0 | **rising** |
| robotics | 258 | 5.0 | 17.2 | ×3.23 | 4 / 1 | **rising** |
| security | 785 | 16.2 | 40.6 | ×2.46 | 5 / 1 | **rising** |
| sandbox | 445 | 10.0 | 23.6 | ×2.29 | 3 / 3 | mixed |
| computer use/browser agents | 113 | 2.4 | 5.9 | ×2.23 | 6 / 0 | **rising** |
| local/open weights | 697 | 15.8 | 34.1 | ×2.12 | 3 / 0 | mixed |
| evals | 958 | 25.3 | 48.1 | ×1.88 | 3 / 3 | mixed |
| regulation/policy | 300 | 8.5 | 14.4 | ×1.66 | 3 / 3 | mixed |
| background/async agents | 231 | 5.6 | 8.6 | ×1.5 | 5 / 1 | **rising** |
| agents/agentic | 6,525 | 183.1 | 271.9 | ×1.48 | 4 / 0 | **rising** |
| AGI/superintelligence | 138 | 4.7 | 7.1 | ×1.48 | 5 / 1 | **rising** |
| AGENTS.md/CLAUDE.md | 124 | 3.0 | 4.6 | ×1.46 | 4 / 2 | mixed |
| Chinese models | 181 | 5.7 | 8.1 | ×1.38 | 3 / 3 | mixed |
| slop | 115 | 3.6 | 5.0 | ×1.33 | 3 / 3 | mixed |
| vibe coding | 179 | 6.0 | 7.1 | ×1.17 | 2 / 3 | mixed |
| subagents/parallel agents | 332 | 11.4 | 13.4 | ×1.17 | 4 / 2 | mixed |
| Skills (agent) | 615 | 18.6 | 21.0 | ×1.12 | 2 / 2 | flat |
| Codex | 571 | 16.6 | 18.1 | ×1.09 | 4 / 2 | flat |
| Qwen | 507 | 15.9 | 16.9 | ×1.06 | 4 / 1 | flat |
| DeepSeek | 236 | 8.8 | 9.2 | ×1.05 | 3 / 2 | flat |
| voice | 268 | 8.8 | 8.8 | ×1.0 | 4 / 0 | flat |
| jobs/layoffs | 318 | 11.5 | 11.3 | ×0.98 | 3 / 3 | flat |
| memory | 663 | 23.9 | 23.1 | ×0.97 | 2 / 1 | flat |
| prompt injection | 115 | 4.9 | 4.6 | ×0.95 | 3 / 2 | flat |
| pricing/rate limits | 656 | 23.9 | 21.7 | ×0.91 | 3 / 1 | flat |
| GitHub Copilot | 84 | 2.8 | 2.1 | ×0.8 | 2 / 3 | mixed |
| education/students | 229 | 9.2 | 7.1 | ×0.78 | 0 / 6 | **falling** |
| context window/compaction | 231 | 10.3 | 7.0 | ×0.69 | 1 / 5 | **falling** |
| GPUs/Nvidia | 792 | 37.3 | 25.6 | ×0.69 | 4 / 1 | mixed |
| ChatGPT | 386 | 19.2 | 12.7 | ×0.67 | 3 / 2 | mixed |
| Kimi | 268 | 15.0 | 9.9 | ×0.67 | 3 / 3 | mixed |
| MCP | 435 | 22.4 | 13.6 | ×0.62 | 2 / 4 | mixed |
| Claude Code | 1,107 | 42.6 | 25.2 | ×0.6 | 1 / 5 | **falling** |
| RAG | 250 | 11.2 | 6.4 | ×0.59 | 0 / 4 | **falling** |
| healthcare | 209 | 6.2 | 3.3 | ×0.57 | 0 / 5 | **falling** |
| fine-tuning | 340 | 17.7 | 9.7 | ×0.56 | 3 / 2 | mixed |
| image generation | 353 | 19.1 | 8.2 | ×0.44 | 1 / 4 | **falling** |
| sycophancy | 70 | 3.8 | 1.3 | ×0.42 | 1 / 4 | **falling** |
| hallucination | 230 | 13.4 | 5.1 | ×0.4 | 1 / 5 | **falling** |
| ads | 88 | 5.3 | 1.7 | ×0.37 | 0 / 4 | **falling** |
| OpenClaw | 159 | 7.9 | 1.7 | ×0.26 | 1 / 5 | **falling** |
| OpenRouter | 218 | 16.4 | 3.8 | ×0.25 | 3 / 1 | mixed |
| Cursor | 408 | 27.4 | 6.3 | ×0.24 | 1 / 4 | **falling** |
| Ollama/LM Studio | 214 | 13.3 | 2.6 | ×0.22 | 3 / 1 | mixed |
| Gemini | 643 | 44.5 | 8.1 | ×0.19 | 0 / 6 | **falling** |
| Perplexity | 168 | 13.8 | 1.4 | ×0.13 | 1 / 3 | mixed |
| Nano Banana | 61 | 5.6 | 0.0 | ×0.08 | 0 / 6 | **falling** |
| Manus | 85 | 8.4 | 0.0 | ×0.06 | 0 / 2 | mixed |

## Monthly shape of key terms (per 1,000 findings)

Note: Nov 2025 and Nov 2026 are partial months.

| per 1k findings | 25/11 | 25/12 | 26/01 | 26/02 | 26/03 | 26/04 | 26/05 | 26/06 | 26/07 | 26/08 | 26/09 | 26/10 | 26/11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Claude Code | 21 | 34 | 52 | 57 | 62 | 72 | 50 | 39 | 30 | 25 | 16 | 31 | 37 |
| Codex | 10 | 10 | 12 | 36 | 29 | 40 | 29 | 24 | 30 | 16 | 11 | 15 | 12 |
| Cursor | 38 | 29 | 34 | 8 | 15 | 11 | 8 | 9 | 8 | 10 | 3 | 6 | 3 |
| Gemini | 86 | 48 | 33 | 23 | 19 | 15 | 28 | 8 | 12 | 7 | 5 | 9 | 9 |
| Skills (agent) | 5 | 18 | 20 | 27 | 40 | 28 | 28 | 23 | 29 | 28 | 18 | 10 | 23 |
| MCP | 22 | 27 | 27 | 10 | 13 | 7 | 14 | 11 | 13 | 14 | 17 | 10 | 19 |
| OpenClaw | 0 | 0 | 4 | 30 | 16 | 9 | 4 | 3 | 2 | 3 | 1 | 1 | 0 |
| Fable | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 48 | 33 | 9 | 17 | 2 | 19 |
| security | 14 | 13 | 12 | 29 | 15 | 48 | 29 | 39 | 39 | 41 | 43 | 40 | 26 |
| sandbox | 6 | 6 | 14 | 13 | 13 | 9 | 29 | 22 | 26 | 26 | 18 | 25 | 5 |
| local/open weights | 12 | 13 | 15 | 23 | 24 | 26 | 28 | 38 | 49 | 37 | 21 | 30 | 28 |
| robotics | 5 | 5 | 4 | 5 | 9 | 11 | 3 | 8 | 6 | 12 | 21 | 28 | 2 |
| evals | 31 | 18 | 23 | 33 | 31 | 36 | 35 | 38 | 45 | 46 | 65 | 34 | 31 |
| hallucination | 19 | 14 | 11 | 12 | 8 | 8 | 3 | 8 | 8 | 4 | 5 | 4 | 2 |
| sycophancy | 8 | 3 | 2 | 4 | 5 | 1 | 2 | 2 | 2 | 0 | 1 | 2 | 0 |
| image generation | 31 | 26 | 14 | 8 | 8 | 18 | 8 | 12 | 10 | 8 | 10 | 4 | 5 |

## What this means for posting

- **Trust, control and security are the rising topics.** Posts and apps that answer "how do I let AI do things without regretting it?" ride the strongest current.
- **"Which AI tool is best?" posts are yesterday's conversation.** "How I actually run my AI workflow" is today's.
- **Hype cycles are short.** OpenClaw rose and fell within weeks. Build on durable concerns (cost, trust, voice, keeping up), not on this month's launch.
