# A year of AI commentary: risk and access up, tool-name chatter down

*Across 26,923 findings from 2,209 items (Nov 2025 to Nov 2026), security, cost visibility and open-weight models gained ground, while talk of specific coding tools and chatbots faded.*

*Period: 2025-11-11 to 2026-11-10 · 26,923 findings from 19 sources · generated 2026-11-14 by `python -m src.insights write`. Numbers and tables come from code; prose is Sonnet's; every link is a finding the text cites.*

## Key points

- Safety and governance rose from 71.7 to 128.0 mentions per 1,000 findings (x1.78), up in four big sources and down in none. Security (x2.44) and cyber (x9.38) rose with it. ([One Useful Thing, 2026-02-18](https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the)) ([Simon Willison's Weblog, 2026-02-21](https://simonwillison.net/2026/Feb/21/claws/))
- Observability and cost rose (34.6 to 45.5 per 1k, x1.31). People increasingly ask what AI usage costs and what it actually did. ([AINews (smol.ai), 2026-11-06](https://latent.space/p/ainews-inkling-2-small-17a-594b-trained-in-68-hours-on-12t-tokens-beating-muse-spark/)) ([AINews (smol.ai), 2026-06-30](https://news.smol.ai/issues/26-06-30-sonnet5/))
- Local and open-weight models rose (x1.83, up in five big sources, down in none). Interest is in the category, not in any single tool. ([Marcus on AI, 2026-07-20](https://garymarcus.substack.com/p/china-has-all-but-caught-up-the-us)) ([Don't Worry About the Vase, 2026-07-31](https://thezvi.substack.com/p/ai-179-part-2-hearing-the-fire-alarm)) ([AINews (smol.ai), 2026-07-30](https://news.smol.ai/issues/26-07-30-not-much/))
- Computer use and browser agents (x1.97) and AGI/superintelligence talk (x1.48) both rose, but from small bases.
- Chatter about named coding tools and chatbots fell: devtools and IDEs (x0.65), Claude Code (x0.51), Cursor (x0.29) and Gemini (x0.26) all carry a falling verdict. ([Don't Worry About the Vase, 2025-11-28](https://thezvi.substack.com/p/claude-opus-45-model-card-alignment)) ([Latent Space, 2025-11-18](https://latent.space/p/agent-labs/))
- Older worries cooled: hallucination (x0.47), RAG (x0.57) and education (x0.79) are all falling, with most big sources moving down.

## How to read this

Each topic is measured as mentions per 1,000 findings, comparing December 2025 to March 2026 with July to October 2026. A topic is called rising or falling only when the verdict says so, which depends on how many of the larger sources moved the same way. That matters because the source mix shifted: AINews fell from 40.1% to 23.7% of findings, while Don't Worry About the Vase rose from 12.8% to 19.1% and Latent Space from 6.8% to 13.2%.

The window ends on 10 November 2026, so the last month is partial and its small numbers are noisy. Treat monthly zeros and jumps in November with care.

## Confirmed shifts

**Risk is the biggest move.** Safety and governance went from 71.7 to 128.0 per 1k, up in four big sources and down in none. Within it, security went from 16.4 to 40.6 and cyber from 1.3 to 16.2. Security jumped in April 2026 (48.4) and has held around 39 to 43 every month from June to October. That looks like a new baseline rather than a one-off spike. The OpenClaw episode in February is a good example of the worry: Ethan Mollick called the open-source local agent a serious security risk because it gives an AI broad access to a computer and accounts. ([One Useful Thing, 2026-02-18](https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the)) ([Simon Willison's Weblog, 2026-02-21](https://simonwillison.net/2026/Feb/21/claws/)) ([Marcus on AI, 2026-02-01](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere))

**Cost and visibility came up too.** Observability and cost rose from 34.6 to 45.5 per 1k, up in four big sources and down in one. The findings behind it are practical: a developer asks for a usage-credit purchase on top of a plan to be explained, and agent workflows on OpenRouter lose cached work and pay repeated processing costs. One reading is that once people run agents for real, the questions shift from what the model can do to what it costs and what happened. ([AINews (smol.ai), 2026-06-30](https://news.smol.ai/issues/26-06-30-sonnet5/)) ([AINews (smol.ai), 2026-11-06](https://latent.space/p/ainews-inkling-2-small-17a-594b-trained-in-68-hours-on-12t-tokens-beating-muse-spark/)) ([Simon Willison's Weblog, 2026-06-10](https://simonwillison.net/2026/Jun/10/if-claude-fable-stops-helping-you/))

**Open weights are a rising category.** Local/open weights rose from 18.4 to 34.1 per 1k, up in five big sources and down in none, climbing from 11.7 in November 2025 to 48.9 in July 2026. The July peak coincided with Kimi K3. Gary Marcus argued that free local Chinese models undercut closed US labs, and Zvi Mowshowitz's blog noted demand for a better American open alternative. The picture is category-level, though: Ollama/LM Studio and Chinese models as a group carry mixed verdicts, so the rise is not tied to one tool. ([Marcus on AI, 2026-07-20](https://garymarcus.substack.com/p/china-has-all-but-caught-up-the-us)) ([Don't Worry About the Vase, 2026-07-31](https://thezvi.substack.com/p/ai-179-part-2-hearing-the-fire-alarm)) ([AINews (smol.ai), 2026-07-30](https://news.smol.ai/issues/26-07-30-not-much/))

**Two small risers.** Computer use and browser agents roughly doubled (2.8 to 5.9 per 1k) and were up in six big sources with none down. AGI/superintelligence rose from 4.6 to 7.1, and its monthly path is lumpy, with a September high of 14.9. Both are small numbers, so the direction is more reliable than the size.

**Product names faded.** Devtools and IDEs fell from 84.3 to 54.5 per 1k. Claude Code halved (50.3 to 25.2), peaked in April 2026 at 71.9 and has partly recovered to 30.9 and 37.3 in the last two months. Cursor fell from 23.0 to 6.3, and Gemini from 32.1 to 8.1 after a November 2025 peak of 85.5 around Gemini 3 Pro. Perplexity, OpenClaw and Nano Banana also carry falling verdicts. The broader coding agents domain is only mixed (138.7 to 100.4, down in three big sources, up in none), so coding has not gone away. Commentary seems to have moved from brand-by-brand comparisons to the issues around using the tools. ([Don't Worry About the Vase, 2025-11-28](https://thezvi.substack.com/p/claude-opus-45-model-card-alignment)) ([Ben's Bites, 2025-11-25](https://www.bensbites.com/p/new-opus-is-bananas)) ([Latent Space, 2025-11-18](https://latent.space/p/agent-labs/))

**Older worries cooled.** Hallucination fell from 11.4 to 5.1 per 1k and was down in five big sources. RAG fell from 11.6 to 6.4, and education and learning from 15.8 to 12.4, down in all five big sources. Healthcare is also falling, but its path is distorted by a May 2026 spike (see below).

## Uncertain (mixed) changes

**Evals and testing** grew from 72.1 to 102.8 per 1k, but three big sources went up and three went down, so the verdict is mixed. The narrower term evals nearly doubled (25.7 to 48.1) with the same split. It peaked at 64.9 in September and fell back to 34.2 in October.

**Agents/agentic** is the biggest single term (222.5 to 271.9 per 1k) and its verdict is mixed. The monthly numbers show most of the climb came early, from 101.9 in November 2025 to 286.6 in February 2026, and then a plateau around 250 to 300. Whether that is a ceiling or saturation is not something the data settles.

**Robotics and sandboxes.** Robotics went from 5.7 to 17.2 per 1k and peaked in October at 28.0. The findings are mostly about what is missing: generalization, dexterity, and a debate over whether progress is near-term or the robots are gimmicks. Sandboxing doubled (11.5 to 23.6) but with three big sources up and two down. It overlaps with the agent-permission worry from the OpenClaw period. ([Latent Space, 2026-10-13](https://latent.space/p/dyna/)) ([AINews (smol.ai), 2026-10-15](https://latent.space/p/ainews-modals-1b-arr-16b-series-d/)) ([Don't Worry About the Vase, 2026-10-15](https://thezvi.substack.com/p/ai-190-scion-of-the-times)) ([Marcus on AI, 2026-02-01](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere))

**Other mixed items:** regulation/policy (8.6 to 14.4, with a September high of 21.3), research and capabilities, consumer apps (59.7 to 42.0), hardware and compute (25.9 to 15.3), MCP (20.5 to 13.6) and agent Skills (25.4 to 21.0) all moved but split the big sources. Hold any claims about these loosely.

## Stable background concerns (flat)

The mix of finding types barely moved. Pain points stayed near 375 to 383 per 1k, the largest type at 10,181 findings in total, and build requests stayed roughly level. Complaints about pricing and rate limits (24.7 to 21.7), memory (26.3 to 23.1), prompt injection (4.8 to 4.6), enterprise adoption, jobs and careers, and inference and infrastructure are all flat. Agents and orchestration (x1.13) and vibe coding (6.2 to 7.1) are also flat.

Flat does not mean solved. It means these were steady annoyances all year. The pain of constantly re-evaluating which model is best, described by Tomasz Tunguz in November 2025, is the kind of background load that persists. Prompt injection staying flat while security overall rose suggests the new worry is about agent permissions and access, not that attack type specifically. That is an interpretation, not something the data states directly. ([Tomasz Tunguz, 2025-11-21](https://tomtunguz.com/the-bacon-and-the-skillet-when-ai-market-share-congeals/)) ([Simon Willison's Weblog, 2025-11-25](https://simonwillison.net/2025/Nov/25/google-antigravity-exfiltrates-data/))

## Hype cycles and spikes

**Fable (June 2026, 48.5 per 1k, median 0.0).** The verdict reads rising, but the shape is a burst: 48.5 in June, 33.1 in July, then 8.6 to 16.6 afterwards. The findings are about access and trust. Users objected to Fable 5 needing a separate usage-credit purchase plus identity verification. Ben Tossell noted that model access can be revoked abruptly, and Nathan Lambert said a model going API-only raises the cost of running a writing publication. Simon Willison's blog carried a request for a tool that detects silent provider-side changes to a model's responses. ([AINews (smol.ai), 2026-06-30](https://news.smol.ai/issues/26-06-30-sonnet5/)) ([Ben's Bites, 2026-06-16](https://www.bensbites.com/p/bye-bye-fable)) ([Interconnects, 2026-06-17](https://www.interconnects.ai/p/state-of-the-blog-mid-2026)) ([Simon Willison's Weblog, 2026-06-10](https://simonwillison.net/2026/Jun/10/if-claude-fable-stops-helping-you/))

**OpenClaw (February 2026, 29.7 per 1k, median 2.7).** A security-and-trust episode. Andrej Karpathy was wary of running it, Gary Marcus asked for a permission model that limits access to passwords and system files, and users reported Google accounts banned for running Gemini through it. Mentions fell to 1.7 per 1k late in the year. ([Simon Willison's Weblog, 2026-02-21](https://simonwillison.net/2026/Feb/21/claws/)) ([Marcus on AI, 2026-02-01](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere)) ([Ben's Bites, 2026-02-24](https://www.bensbites.com/p/gemini-tops-benchmarks-again)) ([AINews (smol.ai), 2026-02-24](https://news.smol.ai/issues/26-02-24-claude-code/))

**Gemini (November 2025, 85.5 per 1k).** Gemini 3 launch commentary. Zvi Mowshowitz flagged high evaluation awareness and fabricated answers, and Ben's Bites flagged duplicate code and a 'you're absolutely right' loop in coding models. Attention fell steadily afterward. Cursor had a smaller November peak (37.5), with coverage of its product-first path and its free Composer 1 model. ([Don't Worry About the Vase, 2025-11-28](https://thezvi.substack.com/p/claude-opus-45-model-card-alignment)) ([Ben's Bites, 2025-11-25](https://www.bensbites.com/p/new-opus-is-bananas)) ([Latent Space, 2025-11-18](https://latent.space/p/agent-labs/)) ([Tomasz Tunguz, 2025-11-12](https://tomtunguz.com/running-out-of-ai/))

**Kimi (July 2026, 27.0 per 1k, median 5.2).** The Kimi K3 release. Findings include requests to plug a local K3 into Claude Code, Simon Willison's criticism of its modified MIT license, and the competitive-pressure argument. Its verdict is mixed because it spiked and then dropped, even as the open-weights category kept rising. ([AINews (smol.ai), 2026-07-30](https://news.smol.ai/issues/26-07-30-not-much/)) ([Simon Willison's Weblog, 2026-07-27](https://simonwillison.net/2026/Jul/27/kimi-k3/)) ([Marcus on AI, 2026-07-20](https://garymarcus.substack.com/p/china-has-all-but-caught-up-the-us)) ([Don't Worry About the Vase, 2026-07-31](https://thezvi.substack.com/p/ai-179-part-2-hearing-the-fire-alarm))

**DeepSeek (November 2026, 21.7 per 1k, median 7.1).** Partly a partial-month effect, but the findings concern DeepSeek V4.1 Flash and the cost of OpenRouter's roughly 10-minute provider pinning, which forces repeated KV-cache recomputation. A Hacker News thread asked whether to trust a Claude subscription or switch to open alternatives. Its overall verdict is flat. ([Latent Space, 2026-11-10](https://latent.space/p/naiveai/)) ([AINews (smol.ai), 2026-11-06](https://latent.space/p/ainews-inkling-2-small-17a-594b-trained-in-68-hours-on-12t-tokens-beating-muse-spark/)) ([AINews (smol.ai), 2026-11-05](https://latent.space/p/ainews-it-s-swapping-season/)) ([Hacker News — Ask HN, 2026-11-04](https://news.ycombinator.com/item?id=50366117))

**Smaller peaks.** OpenRouter in December 2025 (25.5) was mostly feature requests such as text-to-speech models and reasoning support. Image generation in November 2025 (31.0) included trust erosion over real versus AI photos. Fine-tuning in December 2025 (24.1) covered tools like Tinker. Robotics peaked in October 2026 (28.0). The healthcare peak in May 2026 (29.1) is partly an artifact: some of its top findings concern clinical trials and medical AI, but others are about Claude Code usage indicators and agent monitoring, so read its drop with caution. ([AINews (smol.ai), 2025-12-31](https://news.smol.ai/issues/25-12-31-not-much/)) ([Don't Worry About the Vase, 2025-11-27](https://thezvi.substack.com/p/ai-144-thanks-for-the-models)) ([Ben's Bites, 2025-12-16](https://www.bensbites.com/p/gpt-5-doesnt-suck-anymore)) ([Hacker News — Ask HN, 2026-05-13](https://news.ycombinator.com/item?id=48122103)) ([AINews (smol.ai), 2026-05-06](https://news.smol.ai/issues/26-05-06-anthropic-xai/))

## What this means for you

Write about the conditions of use, not the leaderboard. The data suggests the audience's attention moved from which tool is best to what could go wrong and what it costs: permissions, security, usage limits, access being revoked. A post explaining how you scoped what an AI agent could touch in your own project would fit where the conversation is heading. ([One Useful Thing, 2026-02-18](https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the)) ([Marcus on AI, 2026-02-01](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere)) ([Ben's Bites, 2026-06-16](https://www.bensbites.com/p/bye-bye-fable))

As a vibe coder, treat model dependence as a risk you manage. Access changes, pricing and silent model changes were recurring complaints, and open-weight models are a growing category as a fallback. Keep your projects portable across at least one other model, and watch your own usage costs. ([AINews (smol.ai), 2026-06-30](https://news.smol.ai/issues/26-06-30-sonnet5/)) ([Simon Willison's Weblog, 2026-06-10](https://simonwillison.net/2026/Jun/10/if-claude-fable-stops-helping-you/)) ([Marcus on AI, 2026-07-20](https://garymarcus.substack.com/p/china-has-all-but-caught-up-the-us))

Be careful with the drop in tool names. Falling mentions of Claude Code or Cursor does not mean fewer people use them. It may mean the novelty wore off, and the source mix changed. Avoid headlines like 'X is dying' and stick to topics with a rising or falling verdict. Treat the mixed items, such as agents, evals and robotics, as open questions you can ask your readers rather than conclusions you can announce.

## Table: domains (2025-12..2026-03 vs 2026-07..2026-10)

| | Findings | Early (per 1k) | Late (per 1k) | Change | Big sources ↑ / ↓ | Verdict |
|---|---|---|---|---|---|---|
| safety & governance | 2,487 | 71.7 | 128.0 | ×1.78 | 4 / 0 | **rising** |
| evals & testing | 2,296 | 72.1 | 102.8 | ×1.42 | 3 / 3 | mixed |
| observability & cost | 1,102 | 34.6 | 45.5 | ×1.31 | 4 / 1 | **rising** |
| research & capabilities | 1,378 | 48.4 | 58.4 | ×1.21 | 3 / 1 | mixed |
| agents & orchestration | 2,558 | 90.5 | 102.2 | ×1.13 | 4 / 0 | flat |
| creative & media | 766 | 27.1 | 28.9 | ×1.06 | 3 / 0 | flat |
| local & open models | 1,340 | 45.6 | 48.6 | ×1.06 | 4 / 1 | flat |
| enterprise adoption | 891 | 29.6 | 31.0 | ×1.05 | 2 / 1 | flat |
| inference & infra | 1,517 | 56.1 | 54.7 | ×0.98 | 2 / 0 | flat |
| data & pipelines | 514 | 18.6 | 17.8 | ×0.96 | 2 / 3 | flat |
| productivity & knowledge work | 1,514 | 58.9 | 54.5 | ×0.93 | 2 / 2 | flat |
| business & markets | 1,093 | 40.8 | 37.7 | ×0.92 | 2 / 3 | flat |
| jobs & careers | 336 | 12.7 | 11.6 | ×0.91 | 1 / 4 | flat |
| model training & fine-tuning | 1,005 | 42.1 | 36.0 | ×0.86 | 4 / 2 | mixed |
| other | 247 | 9.8 | 8.3 | ×0.86 | 2 / 3 | mixed |
| education & learning | 377 | 15.8 | 12.4 | ×0.79 | 0 / 5 | **falling** |
| coding agents | 3,331 | 138.7 | 100.4 | ×0.73 | 0 / 3 | mixed |
| consumer apps | 1,343 | 59.7 | 42.0 | ×0.71 | 2 / 3 | mixed |
| devtools & IDEs | 1,915 | 84.3 | 54.5 | ×0.65 | 1 / 4 | **falling** |
| hardware & compute | 542 | 25.9 | 15.3 | ×0.6 | 2 / 3 | mixed |
| RAG & retrieval | 371 | 17.1 | 9.5 | ×0.57 | 2 / 3 | mixed |

## Table: finding types

| | Findings | Early (per 1k) | Late (per 1k) | Change | Big sources ↑ / ↓ | Verdict |
|---|---|---|---|---|---|---|
| debate | 2,265 | 78.4 | 91.9 | ×1.17 | 2 / 0 | mixed |
| workaround | 1,929 | 66.4 | 75.8 | ×1.14 | 3 / 1 | flat |
| build_request | 3,262 | 118.2 | 131.5 | ×1.11 | 2 / 1 | flat |
| pain_point | 10,181 | 374.6 | 382.5 | ×1.02 | 2 / 0 | flat |
| link_shared | 292 | 10.6 | 10.7 | ×1.01 | 2 / 1 | flat |
| tool_or_technique | 7,681 | 299.4 | 266.3 | ×0.89 | 0 / 3 | flat |
| tool_complaint | 1,313 | 52.5 | 41.3 | ×0.79 | 2 / 2 | mixed |

## Table: terms (50+ findings; keyword matches, approximate)

| | Findings | Early (per 1k) | Late (per 1k) | Change | Big sources ↑ / ↓ | Verdict |
|---|---|---|---|---|---|---|
| Fable | 244 | 0.0 | 15.5 | ×32.03 | 6 / 0 | **rising** |
| cyber | 212 | 1.3 | 16.2 | ×9.38 | 5 / 0 | **rising** |
| robotics | 258 | 5.7 | 17.2 | ×2.84 | 2 / 2 | mixed |
| security | 785 | 16.4 | 40.6 | ×2.44 | 5 / 1 | **rising** |
| sandbox | 445 | 11.5 | 23.6 | ×2.01 | 3 / 2 | mixed |
| computer use/browser agents | 113 | 2.8 | 5.9 | ×1.97 | 6 / 0 | **rising** |
| evals | 958 | 25.7 | 48.1 | ×1.86 | 3 / 3 | mixed |
| local/open weights | 697 | 18.4 | 34.1 | ×1.83 | 5 / 0 | **rising** |
| regulation/policy | 300 | 8.6 | 14.4 | ×1.64 | 2 / 2 | mixed |
| AGI/superintelligence | 138 | 4.6 | 7.1 | ×1.48 | 4 / 1 | **rising** |
| Chinese models | 181 | 5.7 | 8.1 | ×1.37 | 2 / 4 | mixed |
| slop | 115 | 3.8 | 5.0 | ×1.29 | 3 / 3 | mixed |
| background/async agents | 231 | 6.8 | 8.6 | ×1.25 | 4 / 2 | mixed |
| agents/agentic | 6,525 | 222.5 | 271.9 | ×1.22 | 2 / 1 | mixed |
| vibe coding | 179 | 6.2 | 7.1 | ×1.13 | 2 / 3 | flat |
| DeepSeek | 236 | 8.4 | 9.2 | ×1.1 | 4 / 2 | flat |
| AGENTS.md/CLAUDE.md | 124 | 4.1 | 4.6 | ×1.1 | 3 / 2 | flat |
| subagents/parallel agents | 332 | 12.5 | 13.4 | ×1.06 | 4 / 2 | flat |
| prompt injection | 115 | 4.8 | 4.6 | ×0.96 | 4 / 2 | flat |
| Codex | 571 | 20.3 | 18.1 | ×0.89 | 4 / 2 | flat |
| voice | 268 | 9.9 | 8.8 | ×0.89 | 3 / 2 | flat |
| Qwen | 507 | 19.2 | 16.9 | ×0.88 | 4 / 1 | flat |
| memory | 663 | 26.3 | 23.1 | ×0.88 | 2 / 3 | flat |
| pricing/rate limits | 656 | 24.7 | 21.7 | ×0.88 | 3 / 2 | flat |
| jobs/layoffs | 318 | 12.9 | 11.3 | ×0.87 | 2 / 2 | mixed |
| Kimi | 268 | 11.7 | 9.9 | ×0.85 | 3 / 3 | mixed |
| Skills (agent) | 615 | 25.4 | 21.0 | ×0.83 | 0 / 3 | mixed |
| education/students | 229 | 8.9 | 7.1 | ×0.81 | 0 / 6 | **falling** |
| GPUs/Nvidia | 792 | 33.5 | 25.6 | ×0.77 | 3 / 2 | mixed |
| GitHub Copilot | 84 | 3.1 | 2.1 | ×0.74 | 1 / 3 | mixed |
| context window/compaction | 231 | 10.3 | 7.0 | ×0.7 | 1 / 3 | mixed |
| ChatGPT | 386 | 18.9 | 12.7 | ×0.68 | 2 / 3 | mixed |
| MCP | 435 | 20.5 | 13.6 | ×0.67 | 2 / 4 | mixed |
| fine-tuning | 340 | 16.6 | 9.7 | ×0.6 | 1 / 3 | mixed |
| RAG | 250 | 11.6 | 6.4 | ×0.57 | 0 / 4 | **falling** |
| image generation | 353 | 14.7 | 8.2 | ×0.57 | 2 / 4 | mixed |
| healthcare | 209 | 6.6 | 3.3 | ×0.54 | 0 / 4 | **falling** |
| Claude Code | 1,107 | 50.3 | 25.2 | ×0.51 | 0 / 5 | **falling** |
| sycophancy | 70 | 3.4 | 1.3 | ×0.47 | 1 / 3 | mixed |
| hallucination | 230 | 11.4 | 5.1 | ×0.47 | 1 / 5 | **falling** |
| ads | 88 | 4.2 | 1.7 | ×0.45 | 1 / 3 | mixed |
| OpenRouter | 218 | 12.0 | 3.8 | ×0.34 | 4 / 1 | mixed |
| Cursor | 408 | 23.0 | 6.3 | ×0.29 | 1 / 4 | **falling** |
| Gemini | 643 | 32.1 | 8.1 | ×0.26 | 0 / 6 | **falling** |
| Ollama/LM Studio | 214 | 11.5 | 2.6 | ×0.26 | 2 / 1 | mixed |
| OpenClaw | 159 | 11.0 | 1.7 | ×0.19 | 1 / 5 | **falling** |
| Perplexity | 168 | 11.5 | 1.4 | ×0.16 | 1 / 4 | **falling** |
| Nano Banana | 61 | 3.7 | 0.0 | ×0.12 | 0 / 6 | **falling** |
| Manus | 85 | 6.9 | 0.0 | ×0.07 | 0 / 2 | mixed |

## Table: monthly shape (per 1,000 findings)

| | 25/11 | 25/12 | 26/01 | 26/02 | 26/03 | 26/04 | 26/05 | 26/06 | 26/07 | 26/08 | 26/09 | 26/10 | 26/11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fable | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 48 | 33 | 9 | 17 | 2 | 19 |
| cyber | 5 | 1 | 2 | 1 | 1 | 13 | 2 | 10 | 17 | 14 | 20 | 14 | 2 |
| robotics | 5 | 5 | 4 | 5 | 9 | 11 | 3 | 8 | 6 | 12 | 21 | 28 | 2 |
| security | 14 | 13 | 12 | 29 | 15 | 48 | 29 | 39 | 39 | 41 | 43 | 40 | 26 |
| sandbox | 6 | 6 | 14 | 13 | 13 | 9 | 29 | 22 | 26 | 26 | 18 | 25 | 5 |
| evals | 31 | 18 | 23 | 33 | 31 | 36 | 35 | 38 | 45 | 46 | 65 | 34 | 31 |
| local/open weights | 12 | 13 | 15 | 23 | 24 | 26 | 28 | 38 | 49 | 37 | 21 | 30 | 28 |
| regulation/policy | 9 | 9 | 8 | 8 | 10 | 7 | 9 | 18 | 12 | 11 | 21 | 12 | 9 |
| Chinese models | 5 | 9 | 5 | 4 | 5 | 4 | 7 | 11 | 12 | 5 | 10 | 4 | 5 |
| background/async agents | 6 | 5 | 4 | 8 | 12 | 9 | 16 | 13 | 15 | 6 | 5 | 8 | 5 |
| agents/agentic | 102 | 142 | 192 | 287 | 303 | 253 | 298 | 263 | 261 | 295 | 276 | 258 | 281 |
| vibe coding | 4 | 10 | 5 | 4 | 5 | 9 | 8 | 7 | 6 | 5 | 5 | 12 | 3 |
| DeepSeek | 6 | 19 | 5 | 3 | 5 | 13 | 6 | 6 | 10 | 12 | 8 | 7 | 22 |
| subagents/parallel agents | 5 | 6 | 12 | 22 | 12 | 11 | 13 | 14 | 19 | 9 | 11 | 15 | 11 |
| Codex | 10 | 10 | 12 | 36 | 29 | 40 | 29 | 24 | 30 | 16 | 11 | 15 | 12 |
| voice | 10 | 10 | 8 | 8 | 15 | 11 | 16 | 9 | 8 | 9 | 11 | 8 | 9 |
| Qwen | 9 | 19 | 16 | 17 | 26 | 24 | 31 | 14 | 12 | 29 | 13 | 16 | 26 |
| memory | 22 | 22 | 24 | 27 | 34 | 25 | 26 | 23 | 26 | 29 | 17 | 21 | 23 |
| pricing/rate limits | 22 | 25 | 25 | 22 | 26 | 32 | 29 | 24 | 25 | 16 | 19 | 26 | 25 |
| jobs/layoffs | 4 | 12 | 14 | 14 | 12 | 16 | 15 | 9 | 12 | 15 | 8 | 11 | 11 |
| Kimi | 21 | 18 | 12 | 10 | 5 | 6 | 4 | 4 | 27 | 5 | 3 | 5 | 0 |
| Skills (agent) | 5 | 18 | 20 | 27 | 40 | 28 | 28 | 23 | 29 | 28 | 18 | 10 | 23 |
| education/students | 6 | 16 | 9 | 4 | 6 | 4 | 18 | 9 | 9 | 5 | 3 | 11 | 12 |
| GPUs/Nvidia | 42 | 43 | 40 | 23 | 23 | 19 | 24 | 22 | 27 | 33 | 12 | 33 | 54 |
| context window/compaction | 8 | 8 | 13 | 11 | 8 | 8 | 8 | 6 | 5 | 9 | 9 | 5 | 16 |
| ChatGPT | 18 | 21 | 25 | 11 | 16 | 8 | 13 | 7 | 15 | 20 | 8 | 8 | 3 |
| MCP | 22 | 27 | 27 | 10 | 13 | 7 | 14 | 11 | 13 | 14 | 17 | 10 | 19 |
| fine-tuning | 18 | 24 | 19 | 8 | 12 | 13 | 7 | 7 | 8 | 9 | 13 | 9 | 9 |
| RAG | 10 | 9 | 17 | 6 | 12 | 8 | 13 | 7 | 9 | 8 | 4 | 5 | 8 |
| image generation | 31 | 26 | 14 | 8 | 8 | 18 | 8 | 12 | 10 | 8 | 10 | 4 | 5 |
| healthcare | 5 | 6 | 10 | 2 | 7 | 14 | 29 | 10 | 2 | 5 | 3 | 2 | 6 |
| Claude Code | 21 | 34 | 52 | 57 | 62 | 72 | 50 | 39 | 30 | 25 | 16 | 31 | 37 |
| hallucination | 19 | 14 | 11 | 12 | 8 | 8 | 3 | 8 | 8 | 4 | 5 | 4 | 2 |
| OpenRouter | 23 | 26 | 15 | 2 | 1 | 2 | 3 | 3 | 6 | 3 | 5 | 1 | 12 |
| Cursor | 38 | 29 | 34 | 8 | 15 | 11 | 8 | 9 | 8 | 10 | 3 | 6 | 3 |
| Gemini | 86 | 48 | 33 | 23 | 19 | 15 | 28 | 8 | 12 | 7 | 5 | 9 | 9 |
| Ollama/LM Studio | 18 | 14 | 16 | 6 | 8 | 11 | 4 | 5 | 4 | 5 | 0 | 2 | 8 |
| OpenClaw | 0 | 0 | 4 | 30 | 16 | 9 | 4 | 3 | 2 | 3 | 1 | 1 | 0 |
| Perplexity | 16 | 16 | 14 | 9 | 6 | 2 | 3 | 0 | 1 | 1 | 2 | 1 | 0 |

