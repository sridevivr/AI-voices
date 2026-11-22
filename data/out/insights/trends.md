# What changed in AI talk this year

*Safety, security and open models gained ground, while complaints about made-up answers and big brand names cooled, based on how often topics appeared in a year of AI commentary.*

*Period: 2025-11-11 to 2026-11-14 · 30,139 findings from 20 sources · generated 2026-11-22 by `python -m src.insights write`. Numbers and tables come from code; text is Sonnet's; every link is a finding the text cites.*

## Key points

- **Safety and governance talk grew the most** It now fills about 1 in 8 findings, up from about 1 in 14. All five big sources covered it more.
- **Cyber and security mentions surged** Cyber threats came up about ten times as often, and security more than doubled. Findings ask for ways to measure AI cyberattacks and protect systems. ([Simon Willison's Weblog, 2026-09-27](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/)) ([Interconnects, 2026-09-10](https://www.interconnects.ai/p/one-resignation-turned-the-embers))
- **Open-weight models gained ground** Open-weight models, which anyone can download and run, came up nearly twice as often, and DeepSeek, an AI model maker, rose too.
- **Agents running on their own got more attention** Sandboxes, locked-off spaces where agents run, nearly doubled in mentions. Browser-controlling agents and background agents also rose. ([Marcus on AI, 2026-02-01](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere))
- **Complaints about made-up answers fell by half** Hallucination, AI stating false things, fell by about half, and none of the big sources wrote more about it.
- **Big product names lost attention** Gemini, Google's AI model, and the coding tools Cursor and Claude Code fell sharply from their early share. This measures attention, not use.

## Key moments

- **2025-11**: Gemini 3 Pro complaints and projects ([Don't Worry About the Vase, 2025-11-28](https://thezvi.substack.com/p/claude-opus-45-model-card-alignment)) ([Ben's Bites, 2025-11-25](https://www.bensbites.com/p/new-opus-is-bananas))
- **2025-11**: Cursor and other coding tools in focus ([Latent Space, 2025-11-18](https://latent.space/p/agent-labs/)) ([Tomasz Tunguz, 2025-11-12](https://tomtunguz.com/running-out-of-ai/))
- **2025-11**: Image tools and trust in photos ([Don't Worry About the Vase, 2025-11-27](https://thezvi.substack.com/p/ai-144-thanks-for-the-models)) ([Bluesky, 2025-11-21](https://bsky.app/profile/emollick.bsky.social/post/3m65eoydujk2u))
- **2025-12**: OpenRouter requests for reasoning and speech models ([AINews (smol.ai), 2025-12-31](https://news.smol.ai/issues/25-12-31-not-much/)) ([Simon Willison's Weblog, 2025-12-01](https://simonwillison.net/2025/Dec/1/deepseek-v32/))
- **2025-12**: Fine-tuning tools and tricks ([Latent Space, 2025-12-18](https://latent.space/p/sam-3-the-eyes-for-ai-nikhila-and/)) ([Ben's Bites, 2025-12-16](https://www.bensbites.com/p/gpt-5-doesnt-suck-anymore))
- **2026-02**: OpenClaw personal agents and security worries ([Bluesky, 2026-02-21](https://bsky.app/profile/simonwillison.net/post/3mfdf5v7bns2b)) ([Simon Willison's Weblog, 2026-02-21](https://simonwillison.net/2026/Feb/21/claws/))
- **2026-05**: Health spike, mostly agent-tool requests ([Hacker News — Ask HN, 2026-05-13](https://news.ycombinator.com/item?id=48122103)) ([Marcus on AI, 2026-05-03](https://garymarcus.substack.com/p/have-llms-improved-patient-outcomes))
- **2026-06**: Fable 5 appears, with credit complaints ([AINews (smol.ai), 2026-06-30](https://news.smol.ai/issues/26-06-30-sonnet5/)) ([Bluesky, 2026-06-11](https://bsky.app/profile/simonwillison.net/post/3mnzstv7b5k2x))
- **2026-07**: Kimi K3 open model and license row ([Simon Willison's Weblog, 2026-07-27](https://simonwillison.net/2026/Jul/27/kimi-k3/)) ([Don't Worry About the Vase, 2026-07-31](https://thezvi.substack.com/p/ai-179-part-2-hearing-the-fire-alarm))
- **2026-09**: Cyber risk and defense requests ([Simon Willison's Weblog, 2026-09-27](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/)) ([Interconnects, 2026-09-10](https://www.interconnects.ai/p/one-resignation-turned-the-embers))
- **2026-10**: Robotics generalization needs and job fears ([Latent Space, 2026-10-13](https://latent.space/p/dyna/)) ([Don't Worry About the Vase, 2026-10-15](https://thezvi.substack.com/p/ai-190-scion-of-the-times))

## Confirmed shifts

*Several topics clearly moved: safety and security rose, while talk of made-up answers and big brand names fell.*

**x10.03** Cyber mentions, late period versus early period

- **Safety and governance up**: Safety and governance, covering AI rules and risk, now makes up about 1 in 8 findings, up from about 1 in 14. All five big sources covered it more, and it rose more than any other broad topic.
- **Cyber and security surge** (Simon Willison, Nathan Lambert): Mentions of cyber threats grew about tenfold, and security more than doubled. Findings ask for a benchmark of AI cyberattacks and for tools to harden critical systems. ([Simon Willison's Weblog, 2026-09-27](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/)) ([Interconnects, 2026-09-10](https://www.interconnects.ai/p/one-resignation-turned-the-embers))
- **Open models gain ground**: Talk of open-weight models, which anyone can download and run, nearly doubled, and DeepSeek, an AI model maker, also rose. Five big sources covered open weights more, and none covered them less.
- **Agents working on their own** (Gary Marcus): Sandboxes, locked-off spaces where agents run, nearly doubled in mentions. Browser-controlling agents and background agents also rose. Writers want firm limits on what personal agents can touch. ([Marcus on AI, 2026-02-01](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere))
- **Made-up answers fade**: Complaints about hallucination, AI stating false things, fell by about half, and sycophancy, a model over-agreeing, also fell. No big source wrote more about either.
- **Big brands cool off**: Gemini, Google's AI model, fell to about a quarter of its early level, and Claude Code, a coding tool, fell by more than half. Cursor, another coding tool, fell too. This tracks attention, not use.

## Uncertain changes

*These topics moved, but the big sources disagree, so treat the direction as unconfirmed.*

**x2.71** Robotics mentions, late period versus early period

- **Evals and testing**: Evals, tests that measure how well AI works, grew by about 40% overall. Four big sources wrote more and two wrote less, so the direction is uncertain.
- **Robotics jumps, then drops** (Jason Ma, Timothy B. Lee): Robotics mentions more than doubled, driven by a burst in October. Two big sources rose and three fell. Findings ask for robots that handle new situations and for realistic simulated training data. ([Latent Space, 2026-10-13](https://latent.space/p/dyna/)) ([Understanding AI, 2026-10-01](https://www.understandingrobots.org/cp/218401852))
- **Regulation and policy**: Mentions of regulation and policy rose by about 60%, with peaks in June and September. Big sources split, three up and two down, so the change is uncertain.
- **Coding tools slipped**: Coding agents, AI that writes software, fell by about 30%, and developer tools by about a third. The verdict is still mixed, and coding agents remain among the largest topics.
- **The word 'agent' spreads**: 'Agent' and 'agentic' appear in about 1 in 4 findings, up from about 1 in 5. Most of that rise happened by March 2026, and the verdict is mixed.
- **Chinese models**: Talk of Chinese models rose by about 60% and peaked in July. Big sources split three to three, so it is too early to call a lasting trend.

## Steady concerns

*These topics barely changed, yet they fill a large share of what people write about.*

**11236** findings flagged as pain points, about 1 in 3

- **Pain points stay on top**: Pain points, meaning things that do not work or cost too much, are about 1 in 3 findings. Their share was flat from the early period to the late one.
- **Tips and techniques**: Tools and techniques, shared how-tos, still make up about 1 in 4 findings. They slipped slightly, but the verdict is flat.
- **Steady appetite for new builds**: Requests for things someone wants built are about 1 in 8 findings. That share is flat, a steady demand for new tools.
- **Agents and orchestration**: Agent tools, and the setups that coordinate them, are about 1 in 10 findings. The share stayed flat through the year.
- **Everyday knowledge work**: AI for everyday knowledge work is about 1 in 17 findings, slightly lower but flat by the verdict. It stays one of the larger topics.
- **Prompt injection persists**: Prompt injection, hiding instructions to trick an AI, is a small but steady worry at roughly 1 in 240 findings. Its share is flat.

## Hype spikes

*Short bursts of attention around single names, like Fable or OpenClaw, often faded within a few months.*

**x33.63** Fable growth, late versus early period, starting from zero

- **Fable 5, June 2026** (Simon Willison): Fable 5, an AI model, appeared from nothing in June. Findings include complaints that it needs a separate usage-credit purchase plus identity verification, and a builder using it to make a demo tool. ([AINews (smol.ai), 2026-06-30](https://news.smol.ai/issues/26-06-30-sonnet5/)) ([Bluesky, 2026-06-11](https://bsky.app/profile/simonwillison.net/post/3mnzstv7b5k2x))
- **OpenClaw, February 2026** (Andrej Karpathy, Ben Tossell, Gary Marcus): OpenClaw, a personal AI assistant that runs on your own computer, peaked in February. Findings cover security worries, Google accounts banned for running Gemini through it, and a new category of 'Claws' like it. ([Bluesky, 2026-02-21](https://bsky.app/profile/simonwillison.net/post/3mfdf5v7bns2b)) ([Ben's Bites, 2026-02-24](https://www.bensbites.com/p/gemini-tops-benchmarks-again)) ([Simon Willison's Weblog, 2026-02-21](https://simonwillison.net/2026/Feb/21/claws/))
- **Gemini, November 2025** (Simon Willison, Zvi Mowshowitz, Keshav): Gemini peaked in November 2025. Findings mix a whale-spotting camera project with complaints that Gemini 3 Pro makes up answers and gets stuck in a 'you're absolutely right' loop when fixing bugs. ([Simon Willison's Weblog, 2025-11-26](https://simonwillison.net/2025/Nov/26/data-renegades-podcast/)) ([Don't Worry About the Vase, 2025-11-28](https://thezvi.substack.com/p/claude-opus-45-model-card-alignment)) ([Ben's Bites, 2025-11-25](https://www.bensbites.com/p/new-opus-is-bananas))
- **Kimi K3, July 2026** (Simon Willison): Kimi K3, an open-weight Chinese model, drew a burst of attention in July. Findings include criticism of its license, which adds commercial limits, and calls for a stronger American open alternative. ([Simon Willison's Weblog, 2026-07-27](https://simonwillison.net/2026/Jul/27/kimi-k3/)) ([Don't Worry About the Vase, 2026-07-31](https://thezvi.substack.com/p/ai-179-part-2-hearing-the-fire-alarm))
- **Cyber risk, September 2026** (Simon Willison, Nathan Lambert): Cyber peaked in September but has stayed high since July, so it looks more like a real shift than a spike. Findings are mostly requests for a benchmark of AI cyberattacks and better defenses. ([Simon Willison's Weblog, 2026-09-27](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/)) ([Interconnects, 2026-09-10](https://www.interconnects.ai/p/one-resignation-turned-the-embers)) ([Don't Worry About the Vase, 2026-09-30](https://thezvi.substack.com/p/a-morally-binding-white-house-accord))
- **Robotics, October 2026** (Jason Ma, Timothy B. Lee): Robotics peaked in October. Findings ask for robots that handle new situations and for realistic simulated training data, while a debate asks whether near-term progress is real or humanoid robots are gimmicks. ([Latent Space, 2026-10-13](https://latent.space/p/dyna/)) ([Understanding AI, 2026-10-01](https://www.understandingrobots.org/cp/218401852)) ([Don't Worry About the Vase, 2026-10-15](https://thezvi.substack.com/p/ai-190-scion-of-the-times))

## What this means for you

*Expect more safety questions, hold brand choices loosely, and read spikes as attention, not adoption.*

- **Ask about security early**: Security and safety are the fastest-growing concerns in the commentary. When you try a new AI tool at work, ask what data it can reach and how it is kept in bounds.
- **Do not bet on one brand**: Attention to named products swung a lot, with Gemini, Cursor and OpenClaw all falling after their peaks. Pick tools for the job and be ready to switch.
- **Discount hype, trust steady themes**: Spikes like Kimi K3 faded within a month, while pain points stayed about 1 in 3 findings. Judge AI news by whether the problem it addresses keeps coming up.

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

