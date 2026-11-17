# A year of AI commentary: safety and open models rose, product-name talk faded

*Comparing December 2025 to March 2026 against July to October 2026, a few topics moved clearly. Many others only look like movement because of a spike or a change in which sources are in the mix.*

*Period: 2025-11-11 to 2026-11-14 · 30,139 findings from 20 sources · generated 2026-11-17 by `python -m src.insights write`. Numbers and tables come from code; prose is Sonnet's; every link is a finding the text cites.*

## Key points

- Safety and governance is the clearest rise. Mentions went from 73.7 to 127.1 per 1,000 findings (x1.72), and all five big sources moved up. Security (16.1 to 39.5), cyber (1.2 to 16.9) and sandbox (10.7 to 21.8) rose with it. ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view)) ([Interconnects, 2026-09-10](https://www.interconnects.ai/p/one-resignation-turned-the-embers)) ([Marcus on AI, 2026-02-01](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere))
- Open-weight and Chinese-lab models gained attention. Local/open weights rose from 17.4 to 33.5 per 1,000 and DeepSeek from 8.3 to 10.2, both with a rising verdict. Kimi and Qwen are not rising overall. ([Don't Worry About the Vase, 2026-07-31](https://thezvi.substack.com/p/ai-179-part-2-hearing-the-fire-alarm)) ([AINews (smol.ai), 2026-07-30](https://news.smol.ai/issues/26-07-30-not-much/))
- Agents that work on their own are growing from a small base. Background/async agents went from 6.1 to 8.2 per 1,000 and computer-use/browser agents from 2.7 to 5.4, both rising. ([Bluesky, 2026-02-21](https://bsky.app/profile/simonwillison.net/post/3mfdf5v7bns2b)) ([Latent Space, 2026-05-28](https://latent.space/p/cognition/))
- Named consumer and coding products are being talked about less. Claude Code fell from 53.5 to 23.9, Cursor from 21.5 to 6.0, Gemini from 31.7 to 8.4, and Perplexity, OpenClaw and Nano Banana fell too. The consumer apps domain fell from 62.9 to 45.3. ([Don't Worry About the Vase, 2025-11-24](https://thezvi.substack.com/p/gemini-3-pro-is-a-vast-intelligence)) ([Simon Willison's Weblog, 2025-11-26](https://simonwillison.net/2025/Nov/26/data-renegades-podcast/)) ([Bluesky, 2026-02-21](https://bsky.app/profile/simonwillison.net/post/3mfdf5v7bns2b))
- Old complaints about model quality are fading. Hallucination fell from 11.2 to 5.4, sycophancy from 3.4 to 1.5, RAG from 10.6 to 5.9 and context window/compaction from 9.5 to 6.2, each with a falling verdict. ([Don't Worry About the Vase, 2025-11-28](https://thezvi.substack.com/p/claude-opus-45-model-card-alignment)) ([Ben's Bites, 2025-11-25](https://www.bensbites.com/p/new-opus-is-bananas))
- Fable, a new model name first seen in June 2026, went from 0 to 16.3 per 1,000, a rising verdict. Its coverage centred on pricing, identity verification and access limits. ([AINews (smol.ai), 2026-06-30](https://news.smol.ai/issues/26-06-30-sonnet5/)) ([Don't Worry About the Vase, 2026-06-25](https://thezvi.substack.com/p/ai-174-youre-it))

## How to read this

Each topic is measured as mentions per 1,000 findings, comparing December 2025 to March 2026 with July to October 2026. The verdict is "rising" or "falling" only when the big sources mostly agree on the direction. Otherwise it is "mixed" or "flat".

The source mix shifted during the year. AINews (smol.ai) fell from 36.0% to 21.1% of findings, while Don't Worry About the Vase rose from 11.5% to 17.0% and Latent Space from 6.1% to 11.7%. A raw change in share can therefore partly reflect who was being read. That is why this report leans on the verdicts rather than the ratios alone. Also, November 2026 is a partial month, ending on the 14th.

## Confirmed shifts

**Safety and security moved from side topic to a core theme.** Safety and governance had the only rising verdict among the broad domains. Security, cyber and sandbox, three specific terms, each rose in at least four of the big sources. The cyber requests were practical: defenders need better tools and access to capable models, and critical infrastructure needs faster hardening. Simon Willison asked for a benchmark tracking felony-level cyberattacks by AI labs. ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view)) ([Interconnects, 2026-09-10](https://www.interconnects.ai/p/one-resignation-turned-the-embers)) ([Simon Willison's Weblog, 2026-09-27](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/))

**Sandboxing is a worry about autonomy.** In February, Gary Marcus asked for a secure permission model that limits what personal agents can reach, such as passwords, databases and system files. As agents act on their own, the question is shifting from "is the answer right?" to "what can this thing touch?" ([Marcus on AI, 2026-02-01](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere))

**Open weights and Chinese labs.** Local/open weights rose in five of the big sources, and DeepSeek rose too. Kimi and Qwen are not trending up over the whole period, but they draw attention when a release lands. Zvi Mowshowitz's source notes that Chinese open-weight models are seen as competitive and create demand for a better American open alternative. ([Don't Worry About the Vase, 2026-07-31](https://thezvi.substack.com/p/ai-179-part-2-hearing-the-fire-alarm)) ([AINews (smol.ai), 2026-07-30](https://news.smol.ai/issues/26-07-30-not-much/))

**Agents run longer without supervision.** Background/async agents and computer-use agents both rose. Cole Murray's request for a way to monitor background agent sessions across a team, including open PRs and merge rates, shows the operational problem this creates. The rates are still small (8.2 and 5.4 per 1,000), so this is early growth, not a mainstream shift. ([Latent Space, 2026-05-28](https://latent.space/p/cognition/)) ([Bluesky, 2026-02-21](https://bsky.app/profile/simonwillison.net/post/3mfdf5v7bns2b))

**Product names are fading, and old complaints with them.** Claude Code, Cursor, Gemini, Perplexity, OpenClaw, NotebookLM and Nano Banana all have falling verdicts. Hallucination, sycophancy, RAG, context window/compaction and ads also fell. The late-2025 Gemini and Cursor talk was heavily about launches and bugs. One example is Gemini 3 Pro fabricating answers it did not know, and another is Antigravity producing compiler errors. ([Don't Worry About the Vase, 2025-11-28](https://thezvi.substack.com/p/claude-opus-45-model-card-alignment)) ([Don't Worry About the Vase, 2025-11-24](https://thezvi.substack.com/p/gemini-3-pro-is-a-vast-intelligence)) ([Ben's Bites, 2025-11-25](https://www.bensbites.com/p/new-opus-is-bananas))

## Uncertain (mixed) changes

Evals and testing rose from 68.4 to 97.5 per 1,000 (x1.42), but four big sources rose and two fell, so it is not confirmed. The term "evals" peaked at 60.5 in September 2026 and dropped to 32.8 the next month. Observability and cost (x1.28) and research and capabilities (x1.16) are similarly unsettled.

Coding agents fell from 141.9 to 98.7 per 1,000, and devtools and IDEs from 80.2 to 52.7. Neither is marked falling because the verdict is mixed. It is more cautious to say attention has cooled from a very high base than to say the field is shrinking. The agents/agentic term itself rose from 214.2 to 260.8 (mixed), mostly because it climbed from 99.7 in November 2025 to about 270 by February 2026 and then held.

Other mixed items: regulation/policy (9.0 to 14.7), Chinese models as a group (5.3 to 8.7), slop (4.2 to 6.3) and robotics (5.4 to 15.5, with 3 big sources down). Mixed items on the way down include MCP (19.1 to 12.8), Skills (24.7 to 19.9), ChatGPT (20.5 to 13.2), fine-tuning (15.2 to 8.9), hardware and compute (24.9 to 16.2), the RAG & retrieval domain (15.7 to 8.9) and image generation (15.5 to 7.9). Treat these as uncertain. ([Don't Worry About the Vase, 2026-10-15](https://thezvi.substack.com/p/ai-190-scion-of-the-times))

## Stable background concerns (flat)

Most of the field did not move. Agents & orchestration stayed near 87 to 98 per 1,000, with a flat verdict. Enterprise adoption, inference and infrastructure, business and markets, productivity, creative, jobs and careers, and education were also flat. Jobs/layoffs (13.4 to 11.4) and education/students (10.1 to 9.1) moved only slightly.

The kinds of finding were stable too. Pain points were 368.7 versus 376.2 per 1,000 and build requests 115.3 versus 126.9, both flat. Prompt injection stayed at about 4 per 1,000, vibe coding went from 6.6 to 7.1, and memory and AGENTS.md/CLAUDE.md barely changed. People are still asking for the same things.

## Hype cycles and spikes

**Fable (June 2026, 49.9 per 1,000).** The term did not exist before June. The findings are about access: users objected to Fable 5 needing a separate usage-credit purchase on top of existing plans plus identity verification. A research thread said restrictions on closed frontier models limit autoresearch tasks. Simon Willison built a Datasette API explorer with Fable 5 and GPT-5.5. ([AINews (smol.ai), 2026-06-30](https://news.smol.ai/issues/26-06-30-sonnet5/)) ([Don't Worry About the Vase, 2026-06-25](https://thezvi.substack.com/p/ai-174-youre-it)) ([Bluesky, 2026-06-11](https://bsky.app/profile/simonwillison.net/post/3mnzstv7b5k2x))

**OpenClaw (February 2026, 28.6).** The spike was driven by Andrej Karpathy describing a category of personal agent systems ('Claws') running on personal hardware. Most of the follow-up was trouble: Google accounts banned for running Gemini 3.1 Pro through OpenClaw, Claude Max leaking internal reasoning into live chats, and wariness over security and trust. Its verdict is falling. ([Bluesky, 2026-02-21](https://bsky.app/profile/simonwillison.net/post/3mfdf5v7bns2b)) ([Ben's Bites, 2026-02-24](https://www.bensbites.com/p/gemini-tops-benchmarks-again)) ([AINews (smol.ai), 2026-02-24](https://news.smol.ai/issues/26-02-24-claude-code/)) ([Simon Willison's Weblog, 2026-02-21](https://simonwillison.net/2026/Feb/21/claws/))

**Gemini and Cursor (November 2025).** Gemini peaked at 84.5 and Cursor at 34.7, around the Gemini 3 Pro launch. The findings are a mix of projects (a whale-spotting camera using Gemini) and complaints (a 'you're absolutely right' loop when fixing bugs, and fabricated answers). Cursor's peak included Composer 1 as a free fallback model and Latent Space's account of its product-first approach. ([Simon Willison's Weblog, 2025-11-26](https://simonwillison.net/2025/Nov/26/data-renegades-podcast/)) ([Ben's Bites, 2025-11-25](https://www.bensbites.com/p/new-opus-is-bananas)) ([Don't Worry About the Vase, 2025-11-28](https://thezvi.substack.com/p/claude-opus-45-model-card-alignment)) ([Tomasz Tunguz, 2025-11-12](https://tomtunguz.com/running-out-of-ai/)) ([Latent Space, 2025-11-18](https://latent.space/p/agent-labs/))

**OpenRouter (December 2025, 23.5).** This was mostly feature requests: reasoning on the /v1/messages endpoint, text-to-speech models, and a free Olmo 3 32B Think for testing. ([AINews (smol.ai), 2025-12-31](https://news.smol.ai/issues/25-12-31-not-much/)) ([AINews (smol.ai), 2025-12-30](https://news.smol.ai/issues/25-12-30-not-much/)) ([Bluesky, 2025-12-05](https://bsky.app/profile/natolambert.bsky.social/post/3m77bcnl5vu2g))

**Kimi (July 2026, 26.5).** It followed the Kimi K3 release. Simon Willison called its license a 'janky' modified MIT license with commercial restrictions. Users wanted to plug a local K3 into Claude Code. Kimi's overall verdict is flat. ([Simon Willison's Weblog, 2026-07-27](https://simonwillison.net/2026/Jul/27/kimi-k3/)) ([AINews (smol.ai), 2026-07-30](https://news.smol.ai/issues/26-07-30-not-much/)) ([Bluesky, 2026-07-28](https://bsky.app/profile/natolambert.bsky.social/post/3mrocfwtq6e2g))

**Cyber (September 2026, 20.3) and robotics (October 2026, 25.1).** Cyber's peak is consistent with its rising verdict. Robotics is the less certain one. It peaked on talks about generalization and dexterity, and on a debate over whether humanoids are gimmicks, but three big sources were down. ([Don't Worry About the Vase, 2026-09-30](https://thezvi.substack.com/p/a-morally-binding-white-house-accord)) ([Marcus on AI, 2026-09-23](https://garymarcus.substack.com/p/dear-president-trump-heres-a-deal)) ([Latent Space, 2026-10-13](https://latent.space/p/dyna/)) ([Don't Worry About the Vase, 2026-10-15](https://thezvi.substack.com/p/ai-190-scion-of-the-times))

**Healthcare (May 2026, 26.7).** Treat this one with caution. Only some of the top findings concern medicine, such as a request for clinically validated medical AI tools and one for clinical-trial recruitment search. Others are about agent monitoring or Claude Code usage. It may reflect how findings were tagged more than a real surge. ([Marcus on AI, 2026-05-03](https://garymarcus.substack.com/p/have-llms-improved-patient-outcomes)) ([Hacker News — Ask HN, 2026-05-13](https://news.ycombinator.com/item?id=48122103)) ([Latent Space, 2026-05-28](https://latent.space/p/cognition/)) ([AINews (smol.ai), 2026-05-06](https://news.smol.ai/issues/26-05-06-anthropic-xai/))

## What this means for you

For LinkedIn and X posts, the confirmed shifts are the safest ground: security, sandboxing, cyber, open-weight models and agents running in the background. A post about what an agent should be allowed to touch speaks to a growing worry. It will also hold up longer than a post about last month's model launch, because product-name attention rose and fell quickly. ([Marcus on AI, 2026-02-01](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere)) ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view))

For your own builds, the flat pain points are the stable problems: cost, rate limits and trust. Pricing and rate limits sit at about 20 per 1,000 with a mixed verdict. The Fable findings show a typical pattern in which a model arrives with strong interest and then people complain about credits, verification and access. Plan for the tool you rely on changing terms. ([AINews (smol.ai), 2026-06-30](https://news.smol.ai/issues/26-06-30-sonnet5/)) ([Ben's Bites, 2026-02-24](https://www.bensbites.com/p/gemini-tops-benchmarks-again))

Be careful of the "falling" stories. Claude Code and Cursor fell as names, but the coding agents domain is mixed rather than collapsing, and the source mix changed. "Less talked about" does not mean "less used." Also avoid reading too much into the mixed items (evals, robotics, regulation) until more sources agree.

## Table: domains (2025-12..2026-03 vs 2026-07..2026-10)

| | Findings | Early (per 1k) | Late (per 1k) | Change | Big sources ↑ / ↓ | Verdict |
|---|---|---|---|---|---|---|
| safety & governance | 2,825 | 73.7 | 127.1 | ×1.72 | 5 / 0 | **rising** |
| evals & testing | 2,451 | 68.4 | 97.5 | ×1.42 | 4 / 2 | mixed |
| observability & cost | 1,219 | 33.8 | 43.6 | ×1.28 | 3 / 1 | mixed |
| research & capabilities | 1,662 | 53.3 | 62.1 | ×1.16 | 3 / 0 | mixed |
| agents & orchestration | 2,724 | 87.1 | 98.0 | ×1.12 | 3 / 0 | flat |
| local & open models | 1,508 | 44.4 | 49.2 | ×1.11 | 4 / 1 | flat |
| creative & media | 908 | 29.6 | 30.7 | ×1.04 | 3 / 0 | flat |
| enterprise adoption | 1,005 | 30.1 | 31.3 | ×1.04 | 2 / 1 | flat |
| inference & infra | 1,641 | 53.1 | 52.9 | ×1.0 | 3 / 0 | flat |
| business & markets | 1,315 | 42.5 | 41.8 | ×0.98 | 2 / 3 | flat |
| other | 309 | 10.2 | 9.8 | ×0.96 | 3 / 3 | flat |
| data & pipelines | 545 | 17.5 | 16.4 | ×0.94 | 2 / 3 | flat |
| productivity & knowledge work | 1,743 | 60.6 | 57.2 | ×0.94 | 1 / 2 | flat |
| jobs & careers | 388 | 13.2 | 12.1 | ×0.92 | 1 / 4 | flat |
| education & learning | 485 | 17.0 | 14.9 | ×0.88 | 1 / 4 | flat |
| model training & fine-tuning | 1,060 | 39.9 | 33.6 | ×0.84 | 3 / 3 | mixed |
| consumer apps | 1,603 | 62.9 | 45.3 | ×0.72 | 1 / 4 | **falling** |
| coding agents | 3,718 | 141.9 | 98.7 | ×0.7 | 0 / 3 | mixed |
| devtools & IDEs | 2,044 | 80.2 | 52.7 | ×0.66 | 1 / 3 | mixed |
| hardware & compute | 601 | 24.9 | 16.2 | ×0.66 | 2 / 3 | mixed |
| RAG & retrieval | 385 | 15.7 | 8.9 | ×0.58 | 3 / 2 | mixed |

## Table: finding types

| | Findings | Early (per 1k) | Late (per 1k) | Change | Big sources ↑ / ↓ | Verdict |
|---|---|---|---|---|---|---|
| debate | 2,826 | 87.6 | 101.8 | ×1.16 | 1 / 0 | mixed |
| workaround | 2,118 | 66.4 | 74.2 | ×1.12 | 2 / 1 | flat |
| build_request | 3,558 | 115.3 | 126.9 | ×1.1 | 1 / 1 | flat |
| pain_point | 11,236 | 368.7 | 376.2 | ×1.02 | 1 / 0 | flat |
| link_shared | 496 | 17.0 | 15.4 | ×0.91 | 2 / 2 | flat |
| tool_or_technique | 8,333 | 289.5 | 260.5 | ×0.9 | 0 / 2 | flat |
| tool_complaint | 1,572 | 55.4 | 45.0 | ×0.82 | 1 / 2 | mixed |

## Table: terms (50+ findings; keyword matches, approximate)

| | Findings | Early (per 1k) | Late (per 1k) | Change | Big sources ↑ / ↓ | Verdict |
|---|---|---|---|---|---|---|
| Fable | 284 | 0.0 | 16.3 | ×33.63 | 6 / 0 | **rising** |
| cyber | 248 | 1.2 | 16.9 | ×10.03 | 6 / 0 | **rising** |
| robotics | 263 | 5.4 | 15.5 | ×2.71 | 2 / 3 | mixed |
| security | 867 | 16.1 | 39.5 | ×2.4 | 6 / 0 | **rising** |
| sandbox | 465 | 10.7 | 21.8 | ×1.99 | 4 / 1 | **rising** |
| local/open weights | 767 | 17.4 | 33.5 | ×1.89 | 5 / 0 | **rising** |
| evals | 1,011 | 24.1 | 45.8 | ×1.88 | 4 / 2 | mixed |
| computer use/browser agents | 116 | 2.7 | 5.4 | ×1.86 | 5 / 1 | **rising** |
| regulation/policy | 351 | 9.0 | 14.7 | ×1.6 | 3 / 2 | mixed |
| Chinese models | 212 | 5.3 | 8.7 | ×1.59 | 3 / 3 | mixed |
| slop | 162 | 4.2 | 6.3 | ×1.46 | 4 / 2 | mixed |
| background/async agents | 238 | 6.1 | 8.2 | ×1.32 | 5 / 1 | **rising** |
| AGI/superintelligence | 153 | 5.0 | 6.5 | ×1.27 | 4 / 1 | **rising** |
| agents/agentic | 6,974 | 214.2 | 260.8 | ×1.22 | 3 / 1 | mixed |
| DeepSeek | 286 | 8.3 | 10.2 | ×1.21 | 5 / 1 | **rising** |
| AGENTS.md/CLAUDE.md | 127 | 3.7 | 4.3 | ×1.14 | 3 / 2 | flat |
| vibe coding | 200 | 6.6 | 7.1 | ×1.07 | 2 / 3 | flat |
| subagents/parallel agents | 345 | 12.0 | 12.4 | ×1.04 | 4 / 2 | flat |
| prompt injection | 121 | 4.3 | 4.2 | ×0.97 | 5 / 1 | flat |
| Kimi | 284 | 10.9 | 9.9 | ×0.91 | 4 / 2 | flat |
| memory | 681 | 23.6 | 21.5 | ×0.91 | 2 / 3 | flat |
| education/students | 293 | 10.1 | 9.1 | ×0.9 | 1 / 5 | flat |
| Codex | 639 | 21.2 | 18.6 | ×0.88 | 3 / 3 | flat |
| voice | 301 | 9.9 | 8.6 | ×0.88 | 2 / 3 | flat |
| Qwen | 529 | 18.2 | 15.7 | ×0.87 | 4 / 2 | mixed |
| jobs/layoffs | 362 | 13.4 | 11.4 | ×0.86 | 1 / 3 | mixed |
| pricing/rate limits | 727 | 24.2 | 19.9 | ×0.83 | 2 / 3 | mixed |
| GPUs/Nvidia | 881 | 32.2 | 26.2 | ×0.82 | 3 / 2 | mixed |
| Skills (agent) | 660 | 24.7 | 19.9 | ×0.81 | 0 / 3 | mixed |
| MCP | 457 | 19.1 | 12.8 | ×0.68 | 2 / 3 | mixed |
| GitHub Copilot | 112 | 3.5 | 2.2 | ×0.67 | 1 / 3 | mixed |
| context window/compaction | 236 | 9.5 | 6.2 | ×0.67 | 1 / 4 | **falling** |
| ChatGPT | 467 | 20.5 | 13.2 | ×0.65 | 2 / 4 | mixed |
| healthcare | 242 | 6.7 | 4.0 | ×0.62 | 1 / 3 | mixed |
| fine-tuning | 351 | 15.2 | 8.9 | ×0.6 | 1 / 3 | mixed |
| RAG | 256 | 10.6 | 5.9 | ×0.57 | 0 / 4 | **falling** |
| image generation | 402 | 15.5 | 7.9 | ×0.52 | 2 / 4 | mixed |
| sycophancy | 82 | 3.4 | 1.5 | ×0.51 | 1 / 4 | **falling** |
| hallucination | 262 | 11.2 | 5.4 | ×0.5 | 0 / 6 | **falling** |
| Claude Code | 1,237 | 53.5 | 23.9 | ×0.45 | 0 / 5 | **falling** |
| ads | 114 | 5.0 | 2.0 | ×0.45 | 1 / 4 | **falling** |
| OpenRouter | 227 | 11.0 | 3.7 | ×0.36 | 4 / 1 | mixed |
| Cursor | 423 | 21.5 | 6.0 | ×0.3 | 1 / 5 | **falling** |
| Ollama/LM Studio | 218 | 10.3 | 2.6 | ×0.29 | 3 / 1 | mixed |
| Gemini | 714 | 31.7 | 8.4 | ×0.28 | 0 / 6 | **falling** |
| OpenClaw | 179 | 11.0 | 1.6 | ×0.18 | 1 / 5 | **falling** |
| Perplexity | 170 | 10.5 | 1.4 | ×0.17 | 0 / 4 | **falling** |
| Nano Banana | 70 | 3.7 | 0.0 | ×0.12 | 0 / 6 | **falling** |
| Manus | 88 | 6.4 | 0.0 | ×0.07 | 0 / 2 | mixed |

## Table: monthly shape (per 1,000 findings)

| | 25/11 | 25/12 | 26/01 | 26/02 | 26/03 | 26/04 | 26/05 | 26/06 | 26/07 | 26/08 | 26/09 | 26/10 | 26/11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fable | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 50 | 38 | 8 | 16 | 2 | 18 |
| cyber | 5 | 1 | 2 | 1 | 1 | 14 | 4 | 9 | 18 | 14 | 20 | 14 | 1 |
| robotics | 5 | 5 | 4 | 5 | 8 | 10 | 2 | 7 | 6 | 11 | 19 | 25 | 1 |
| security | 15 | 13 | 11 | 28 | 14 | 51 | 27 | 37 | 37 | 39 | 42 | 40 | 26 |
| sandbox | 5 | 6 | 13 | 11 | 13 | 10 | 25 | 22 | 24 | 24 | 16 | 23 | 4 |
| local/open weights | 12 | 12 | 14 | 22 | 24 | 29 | 26 | 38 | 48 | 35 | 21 | 31 | 24 |
| evals | 30 | 17 | 22 | 31 | 29 | 32 | 33 | 35 | 44 | 44 | 60 | 33 | 30 |
| regulation/policy | 9 | 8 | 8 | 10 | 11 | 9 | 10 | 19 | 14 | 11 | 21 | 13 | 10 |
| Chinese models | 4 | 8 | 4 | 4 | 5 | 6 | 7 | 12 | 14 | 6 | 9 | 5 | 7 |
| slop | 7 | 3 | 3 | 4 | 7 | 2 | 9 | 6 | 6 | 9 | 6 | 5 | 4 |
| background/async agents | 5 | 4 | 4 | 7 | 10 | 8 | 14 | 12 | 14 | 6 | 6 | 7 | 5 |
| AGI/superintelligence | 6 | 6 | 2 | 7 | 6 | 5 | 2 | 3 | 6 | 5 | 13 | 1 | 1 |
| agents/agentic | 100 | 133 | 194 | 272 | 284 | 237 | 276 | 246 | 247 | 277 | 272 | 248 | 260 |
| DeepSeek | 6 | 20 | 4 | 3 | 5 | 13 | 10 | 7 | 11 | 13 | 9 | 8 | 19 |
| vibe coding | 3 | 11 | 6 | 4 | 5 | 8 | 8 | 6 | 5 | 6 | 5 | 12 | 3 |
| subagents/parallel agents | 4 | 5 | 12 | 21 | 11 | 10 | 12 | 12 | 17 | 8 | 10 | 14 | 10 |
| Kimi | 20 | 17 | 12 | 9 | 4 | 6 | 4 | 4 | 26 | 4 | 2 | 6 | 0 |
| memory | 21 | 20 | 22 | 23 | 30 | 24 | 25 | 22 | 26 | 26 | 15 | 20 | 20 |
| education/students | 6 | 15 | 8 | 7 | 9 | 5 | 18 | 10 | 10 | 9 | 5 | 12 | 12 |
| Codex | 10 | 11 | 14 | 37 | 29 | 37 | 26 | 22 | 30 | 19 | 11 | 15 | 14 |
| voice | 11 | 10 | 8 | 10 | 13 | 12 | 14 | 10 | 7 | 9 | 11 | 7 | 10 |
| Qwen | 9 | 18 | 15 | 17 | 24 | 23 | 28 | 13 | 10 | 27 | 12 | 15 | 24 |
| jobs/layoffs | 4 | 12 | 14 | 14 | 13 | 16 | 15 | 8 | 13 | 13 | 9 | 11 | 12 |
| pricing/rate limits | 20 | 23 | 24 | 23 | 27 | 36 | 30 | 26 | 23 | 15 | 18 | 23 | 26 |
| GPUs/Nvidia | 46 | 43 | 38 | 22 | 22 | 18 | 26 | 22 | 27 | 32 | 14 | 33 | 52 |
| Skills (agent) | 5 | 18 | 20 | 27 | 38 | 27 | 26 | 22 | 26 | 26 | 18 | 10 | 20 |
| MCP | 22 | 26 | 25 | 10 | 12 | 7 | 12 | 10 | 13 | 13 | 16 | 10 | 20 |
| context window/compaction | 8 | 8 | 12 | 10 | 8 | 8 | 8 | 5 | 4 | 8 | 8 | 5 | 14 |
| ChatGPT | 20 | 23 | 26 | 13 | 18 | 10 | 15 | 7 | 15 | 21 | 9 | 9 | 3 |
| healthcare | 5 | 6 | 10 | 4 | 7 | 13 | 27 | 12 | 2 | 7 | 4 | 3 | 8 |
| fine-tuning | 17 | 22 | 18 | 8 | 12 | 12 | 6 | 6 | 7 | 8 | 12 | 8 | 8 |
| RAG | 10 | 8 | 16 | 6 | 11 | 8 | 11 | 6 | 8 | 7 | 4 | 4 | 7 |
| image generation | 33 | 26 | 15 | 10 | 8 | 19 | 8 | 11 | 10 | 7 | 10 | 5 | 4 |
| hallucination | 19 | 14 | 11 | 12 | 7 | 9 | 4 | 8 | 8 | 3 | 5 | 5 | 3 |
| Claude Code | 21 | 35 | 57 | 62 | 63 | 68 | 45 | 38 | 29 | 23 | 15 | 29 | 34 |
| OpenRouter | 21 | 24 | 14 | 2 | 1 | 2 | 4 | 3 | 5 | 4 | 5 | 1 | 12 |
| Cursor | 35 | 26 | 32 | 9 | 15 | 10 | 7 | 8 | 7 | 9 | 3 | 5 | 3 |
| Ollama/LM Studio | 16 | 13 | 14 | 5 | 7 | 10 | 4 | 5 | 3 | 6 | 0 | 2 | 7 |
| Gemini | 84 | 46 | 33 | 23 | 20 | 17 | 26 | 8 | 12 | 8 | 5 | 9 | 11 |
| OpenClaw | 0 | 0 | 4 | 29 | 16 | 10 | 5 | 3 | 2 | 2 | 2 | 1 | 0 |
| Perplexity | 15 | 15 | 13 | 8 | 5 | 2 | 3 | 0 | 2 | 1 | 2 | 1 | 0 |

