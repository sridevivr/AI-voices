# What shifted in AI talk, and what only spiked

*Safety, security and open models grew fastest over the year, while talk of named tools like Claude Code, Cursor and Gemini faded.*

*Period: 2025-11-11 to 2026-11-14 · 30,139 findings from 20 sources · generated 2026-11-22 by `python -m src.insights write`. Numbers and tables come from code; text is Sonnet's; every link is a finding the text cites.*

## Key points

- **Safety and governance talk grew most, in every big source** Mentions rose from 73.7 to 127.1 per 1k (x1.72), up in all five big sources and down in none. ([Don't Worry About the Vase, 2026-09-30](https://thezvi.substack.com/p/a-morally-binding-white-house-accord))
- **Security and cyber worries jumped** Security mentions rose x2.4 and cyber x10.03 per 1k, both up in six big sources. Cyber requests focus on monitoring and defenders. ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view)) ([Interconnects, 2026-09-10](https://www.interconnects.ai/p/one-resignation-turned-the-embers))
- **Open weights and sandboxing are both rising** Local/open weights rose x1.89 and sandbox x1.99. People want models they can control and agents that stay contained. ([Don't Worry About the Vase, 2026-07-31](https://thezvi.substack.com/p/ai-179-part-2-hearing-the-fire-alarm)) ([Marcus on AI, 2026-02-01](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere))
- **Named tools lost share of attention** Claude Code fell x0.45, Cursor x0.3, Gemini x0.28 and Perplexity x0.17, all with a falling verdict. ([Ben's Bites, 2025-11-25](https://www.bensbites.com/p/new-opus-is-bananas)) ([Don't Worry About the Vase, 2025-11-24](https://thezvi.substack.com/p/gemini-3-pro-is-a-vast-intelligence))
- **Old accuracy worries are fading** Hallucination fell x0.5 and sycophancy x0.51, both with a falling verdict. RAG also fell, x0.57. ([Don't Worry About the Vase, 2025-11-28](https://thezvi.substack.com/p/claude-opus-45-model-card-alignment))
- **Product hype spikes fade fast, with some rebounds** Fable peaked at 49.9 per 1k in June 2026 and dipped to 2.1 by October. OpenClaw peaked at 28.6 in February 2026. ([Bluesky, 2026-06-11](https://bsky.app/profile/simonwillison.net/post/3mnzstv7b5k2x)) ([Bluesky, 2026-02-21](https://bsky.app/profile/simonwillison.net/post/3mfdf5v7bns2b))

## Key moments

- **2025-11**: Gemini talk peaks at 84.5 per 1k ([Don't Worry About the Vase, 2025-11-28](https://thezvi.substack.com/p/claude-opus-45-model-card-alignment)) ([Ben's Bites, 2025-11-25](https://www.bensbites.com/p/new-opus-is-bananas))
- **2025-11**: Cursor talk peaks ([Don't Worry About the Vase, 2025-11-24](https://thezvi.substack.com/p/gemini-3-pro-is-a-vast-intelligence)) ([Tomasz Tunguz, 2025-11-12](https://tomtunguz.com/running-out-of-ai/))
- **2025-11**: Image generation talk peaks ([Don't Worry About the Vase, 2025-11-27](https://thezvi.substack.com/p/ai-144-thanks-for-the-models)) ([Bluesky, 2025-11-21](https://bsky.app/profile/emollick.bsky.social/post/3m65eoydujk2u))
- **2025-12**: OpenRouter requests peak ([AINews (smol.ai), 2025-12-31](https://news.smol.ai/issues/25-12-31-not-much/)) ([Bluesky, 2025-12-05](https://bsky.app/profile/natolambert.bsky.social/post/3m77bcnl5vu2g))
- **2025-12**: Fine-tuning talk peaks ([AINews (smol.ai), 2025-12-24](https://news.smol.ai/issues/25-12-24-nvidia-groq/)) ([Ben's Bites, 2025-12-16](https://www.bensbites.com/p/gpt-5-doesnt-suck-anymore))
- **2026-02**: OpenClaw personal agents spike ([Bluesky, 2026-02-21](https://bsky.app/profile/simonwillison.net/post/3mfdf5v7bns2b)) ([Ben's Bites, 2026-02-24](https://www.bensbites.com/p/gemini-tops-benchmarks-again))
- **2026-05**: Healthcare keyword spike, mostly off-topic ([Marcus on AI, 2026-05-03](https://garymarcus.substack.com/p/have-llms-improved-patient-outcomes)) ([AINews (smol.ai), 2026-05-06](https://news.smol.ai/issues/26-05-06-anthropic-xai/))
- **2026-06**: Fable 5 talk surges ([AINews (smol.ai), 2026-06-30](https://news.smol.ai/issues/26-06-30-sonnet5/)) ([Bluesky, 2026-06-11](https://bsky.app/profile/simonwillison.net/post/3mnzstv7b5k2x))
- **2026-07**: Kimi K3 drives Kimi spike ([AINews (smol.ai), 2026-07-30](https://news.smol.ai/issues/26-07-30-not-much/)) ([Simon Willison's Weblog, 2026-07-27](https://simonwillison.net/2026/Jul/27/kimi-k3/))
- **2026-09**: Cyber risk talk peaks ([Simon Willison's Weblog, 2026-09-27](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/)) ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view))
- **2026-10**: Robotics talk peaks at 25.1 ([Latent Space, 2026-10-13](https://latent.space/p/dyna/)) ([Don't Worry About the Vase, 2026-10-15](https://thezvi.substack.com/p/ai-190-scion-of-the-times))

## Confirmed shifts

*These items moved in the same direction across most big sources, so the change looks real.*

**x1.72** Safety and governance rate, late vs early

- **Safety and governance**: The biggest verified rise: 73.7 to 127.1 mentions per 1k. Findings include calls for internal monitoring of model capabilities and alignment, covering cyber, bio and chemical risks. ([Don't Worry About the Vase, 2026-09-30](https://thezvi.substack.com/p/a-morally-binding-white-house-accord))
- **Security and cyber** (Sayash Kapoor, Arvind Narayanan, Nathan Lambert): Security went from 16.1 to 39.5 per 1k and cyber from 1.2 to 16.9. Requests focus on defenders: better cyber tooling, access to capable models, and hardening infrastructure against AI misuse. ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view)) ([Interconnects, 2026-09-10](https://www.interconnects.ai/p/one-resignation-turned-the-embers))
- **Open weights gain ground**: Local/open weights rose from 17.4 to 33.5 per 1k, up in five big sources. Chinese open models like Kimi K3 are seen as competitive, creating demand for a better American alternative. ([Don't Worry About the Vase, 2026-07-31](https://thezvi.substack.com/p/ai-179-part-2-hearing-the-fire-alarm))
- **Sandboxing agents** (Gary Marcus): Sandbox mentions nearly doubled, from 10.7 to 21.8 per 1k. Gary Marcus asked for a secure permission model that limits personal agents' access to passwords, databases and system files. ([Marcus on AI, 2026-02-01](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere))
- **Named tools fade**: Claude Code fell from 53.5 to 23.9 per 1k, Cursor from 21.5 to 6.0 and Gemini from 31.7 to 8.4. Themes like safety grew while these products shrank. ([Ben's Bites, 2025-11-25](https://www.bensbites.com/p/new-opus-is-bananas)) ([Don't Worry About the Vase, 2025-11-24](https://thezvi.substack.com/p/gemini-3-pro-is-a-vast-intelligence))
- **Accuracy worries fade**: Hallucination fell from 11.2 to 5.4 per 1k and sycophancy from 3.4 to 1.5. RAG also fell, from 10.6 to 5.9. All three carry a falling verdict. ([Don't Worry About the Vase, 2025-11-28](https://thezvi.substack.com/p/claude-opus-45-model-card-alignment))

## Uncertain changes

*Big sources disagreed on these, so treat the direction as unsettled.*

**x2.71** Robotics rate per 1k, late vs early; verdict mixed

- **Evals and testing**: Evals and testing rose from 68.4 to 97.5 per 1k, and the narrower 'evals' term from 24.1 to 45.8. Four big sources rose and two fell, so the verdict is mixed.
- **Coding agents and IDEs**: Coding agents fell from 141.9 to 98.7 per 1k, yet remain the largest domain with 3,718 findings. Devtools and IDEs fell from 80.2 to 52.7. Both verdicts are mixed.
- **Robotics** (Jason Ma): Robotics rose from 5.4 to 15.5 per 1k, peaking at 25.1 in October 2026, but three big sources fell. Jason Ma says robots still need reliable generalization and dexterity before scaling. ([Latent Space, 2026-10-13](https://latent.space/p/dyna/)) ([Don't Worry About the Vase, 2026-10-15](https://thezvi.substack.com/p/ai-190-scion-of-the-times))
- **Regulation and policy**: Regulation/policy rose from 9.0 to 14.7 per 1k, with peaks in June and September 2026. Three big sources rose and two fell, so the verdict is mixed.
- **Chinese models**: Mentions rose from 5.3 to 8.7 per 1k, with a July 2026 peak of 14.3. Three big sources rose and three fell, so the verdict is mixed. ([Don't Worry About the Vase, 2026-07-31](https://thezvi.substack.com/p/ai-179-part-2-hearing-the-fire-alarm))
- **Agents as a term**: Agents/agentic rose from 214.2 to 260.8 per 1k, but most of the climb came by February 2026. Since then it has hovered between about 237 and 285.

## Steady concerns

*These flat items stay large, so they are the background of the conversation, not a trend.*

**x1.02** Pain point rate per 1k, late vs early

- **Pain points dominate**: Pain points are the biggest finding type at 11,236 findings, and their rate barely moved, from 368.7 to 376.2 per 1k. Frustration is the constant.
- **Agents and orchestration**: Agents and orchestration held at 87.1 to 98.0 per 1k with a flat verdict, and 2,724 findings overall. Subagents and parallel agents were flat too, from 12.0 to 12.4.
- **Vibe coding holds steady**: Vibe coding stayed flat, from 6.6 to 7.1 per 1k, with bumps to 10.8 in December 2025 and 11.5 in October 2026. Small but stable.
- **Memory**: Memory moved from 23.6 to 21.5 per 1k with a flat verdict. It stayed mostly between 20 and 30 per 1k each month.
- **Prompt injection**: Prompt injection stayed flat, 4.3 to 4.2 per 1k. One example: attackers can hide instructions in code comments, docs or MCP servers to leak data through Markdown image rendering. ([Simon Willison's Weblog, 2025-11-25](https://simonwillison.net/2025/Nov/25/google-antigravity-exfiltrates-data/))
- **Productivity and knowledge work**: This domain stayed flat, from 60.6 to 57.2 per 1k, across 1,743 findings. Everyday work use is a steady topic, not a fading one.

## Hype spikes

*These topics surged for a month or two, then dropped back toward their usual level.*

**49.9** Fable mentions per 1k in June 2026

- **Fable 5, June 2026** (Simon Willison, Nathan Lambert): Fable talk went from zero before June 2026 to 49.9 per 1k. Findings include builders using it, complaints about a separate usage-credit purchase plus identity verification, and a request for a tool detecting silent provider-side changes. ([AINews (smol.ai), 2026-06-30](https://news.smol.ai/issues/26-06-30-sonnet5/)) ([Bluesky, 2026-06-11](https://bsky.app/profile/simonwillison.net/post/3mnzstv7b5k2x)) ([Simon Willison's Weblog, 2026-06-10](https://simonwillison.net/2026/Jun/10/if-claude-fable-stops-helping-you/))
- **OpenClaw, February 2026** (Andrej Karpathy, Ben Tossell): OpenClaw peaked at 28.6 per 1k. Andrej Karpathy described an emerging category of personal agents on personal hardware, while users reported account bans, leaked reasoning and security worries. ([Bluesky, 2026-02-21](https://bsky.app/profile/simonwillison.net/post/3mfdf5v7bns2b)) ([Ben's Bites, 2026-02-24](https://www.bensbites.com/p/gemini-tops-benchmarks-again)) ([AINews (smol.ai), 2026-02-24](https://news.smol.ai/issues/26-02-24-claude-code/))
- **Kimi K3, July 2026** (Simon Willison, Nathan Lambert): Kimi peaked at 26.5 per 1k. Users wanted to plug it into Claude Code, Chinese open models were seen as competitive, and Simon Willison called its license 'janky'. ([AINews (smol.ai), 2026-07-30](https://news.smol.ai/issues/26-07-30-not-much/)) ([Don't Worry About the Vase, 2026-07-31](https://thezvi.substack.com/p/ai-179-part-2-hearing-the-fire-alarm)) ([Simon Willison's Weblog, 2026-07-27](https://simonwillison.net/2026/Jul/27/kimi-k3/))
- **Gemini and Cursor, November 2025** (Zvi Mowshowitz): Gemini hit 84.5 per 1k and Cursor 34.7. Gemini 3 Pro drew complaints of fabricated answers and duplicate code, while Cursor talk covered its free Composer 1 model. ([Don't Worry About the Vase, 2025-11-28](https://thezvi.substack.com/p/claude-opus-45-model-card-alignment)) ([Ben's Bites, 2025-11-25](https://www.bensbites.com/p/new-opus-is-bananas)) ([Tomasz Tunguz, 2025-11-12](https://tomtunguz.com/running-out-of-ai/))
- **Cyber, September 2026** (Simon Willison, Gary Marcus, Nathan Lambert): Cyber peaked at 20.3 per 1k and stayed high in October. Requests included monitoring inside frontier labs, a benchmark of felony-level cyberattacks, and better tools for defenders. ([Don't Worry About the Vase, 2026-09-30](https://thezvi.substack.com/p/a-morally-binding-white-house-accord)) ([Simon Willison's Weblog, 2026-09-27](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/)) ([Interconnects, 2026-09-10](https://www.interconnects.ai/p/one-resignation-turned-the-embers))
- **Healthcare, May 2026** (Gary Marcus): Healthcare hit 26.7 per 1k, yet most top findings were about other things, such as Claude Code usage indicators. One did ask for clinically validated medical AI tools. ([AINews (smol.ai), 2026-05-06](https://news.smol.ai/issues/26-05-06-anthropic-xai/)) ([Marcus on AI, 2026-05-03](https://garymarcus.substack.com/p/have-llms-improved-patient-outcomes)) ([Hacker News — Ask HN, 2026-05-13](https://news.ycombinator.com/item?id=48122103))

## What this means for you

*Aim your writing and building at the confirmed shifts, and treat spikes with patience.*

**x2.4** Security mentions per 1k, late vs early

- **Write about agent safety**: Safety, security and sandboxing all rose with verdicts you can cite. Plain-language posts on what could go wrong when agents get access to files and accounts match where the conversation is heading. ([Marcus on AI, 2026-02-01](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere)) ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view))
- **Do not tie posts to one tool**: Claude Code, Cursor and Gemini all fell by more than half. Frame advice around lasting jobs, such as reviewing agent output, so it outlasts any one product's moment. ([Don't Worry About the Vase, 2025-11-24](https://thezvi.substack.com/p/gemini-3-pro-is-a-vast-intelligence))
- **Check spikes before reacting**: Fable and OpenClaw spiked then faded, and the healthcare spike was mostly off-topic. Wait for several months and several sources before calling something a shift. ([AINews (smol.ai), 2026-05-06](https://news.smol.ai/issues/26-05-06-anthropic-xai/)) ([Bluesky, 2026-02-21](https://bsky.app/profile/simonwillison.net/post/3mfdf5v7bns2b))

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

