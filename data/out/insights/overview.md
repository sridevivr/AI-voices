# Quick look: 2025-11-11 to 2026-11-10

*Generated 2026-11-14 by `python -m src.insights build`; every number is computed from `findings.csv` / `themes.json`. No model wrote this page.*

**26,923 findings** from 2,209 articles/threads by 19 sources; 97.8% of quotes verified word-for-word.

| Type | Findings |
|---|---|
| pain point | 10,181 |
| tool or technique | 7,681 |
| build request | 3,262 |
| debate | 2,265 |
| workaround | 1,929 |
| tool complaint | 1,313 |
| link shared | 292 |

## Biggest debates

- **AI regulation, liability and governance debates**: 70 debate findings of 142, 12 sources. e.g. Technolibertarians argue liability for AI harms should substitute for regulation, while Marcus argues liability alone is insufficient and new regulation is also needed. ([Marcus on AI, 2026-09-17](https://garymarcus.substack.com/p/liability-regulation-and-ais-new))
- **Alignment, welfare and existential risk debates**: 60 debate findings of 103, 10 sources. e.g. Some argue AI control efforts increase existential risk by distracting from learning from failures and by creating adversarial dynamics with AIs, while others see control as necessary to limit dangerous escapes. ([Don't Worry About the Vase, 2026-09-10](https://thezvi.substack.com/p/ai-185-preference-cascade))
- **AI investment bubble and financing opacity**: 49 debate findings of 95, 9 sources. e.g. Circular financing deals, where a chipmaker funds a customer that buys its own chips, are seen by some as a dotcom-style bubble signal and by others as normal dealmaking; Marcus argues the risk of collapse is underrated. ([Marcus on AI, 2026-02-05](https://garymarcus.substack.com/p/is-the-great-ai-meltdown-imminent))
- **AGI, timelines and recursive self-improvement debates**: 49 debate findings of 67, 12 sources. e.g. Researchers disagree on whether current AI self-improvement loops are close to a recursive intelligence explosion, with Ramez Naam arguing the loop is too weak and Zvi arguing diminishing returns assumptions miss paradigm shifts. ([Don't Worry About the Vase, 2026-10-01](https://thezvi.substack.com/p/ai-188-gemini-dot-argon))
- **LLM commoditization and weak moats**: 35 debate findings of 55, 9 sources. e.g. Graphify's defensibility is questioned since its code is free and easy for agents to reproduce, risking commoditization by model vendors like Anthropic. ([AINews (smol.ai), 2026-06-29](https://news.smol.ai/issues/26-06-29-not-much/))
- **Scaling versus new architectures, world models and neurosymbolic AI**: 34 debate findings of 83, 7 sources. e.g. Whether scaling compute and data is sufficient for AGI versus needing world models and neurosymbolic AI. ([Marcus on AI, 2026-03-14](https://garymarcus.substack.com/p/breaking-expensive-new-evidence-that))
- **Debates on productivity, vibe coding and limits of AI coding**: 30 debate findings of 90, 9 sources. e.g. Whether vibe coding applies whenever AI helps write code, versus only when code is used without review; the author argues a project can be pure vibe coding yet still low-risk. ([Simon Willison's Weblog, 2026-04-23](https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/))
- **Western versus Chinese open models and openness debates**: 29 debate findings of 64, 13 sources. e.g. Whether Chinese open models like GLM-5.2 are closing the capability gap with top US models, with the author arguing the gap is not steadily shrinking. ([Don't Worry About the Vase, 2026-06-29](https://thezvi.substack.com/p/wsj-article-claiming-china-has-matched))
- **Open-source licensing, copyright and AI training**: 26 debate findings of 58, 5 sources. e.g. Discussion that training may be fair use so copyright-based licensing may not apply, and that materials must be legally obtained. ([Hacker News — Ask HN, 2026-02-13](https://news.ycombinator.com/item?id=47000737))
- **Government and military AI use restrictions**: 24 debate findings of 58, 10 sources. e.g. Whether AI companies can trust government promises versus needing contractual or legislative constraints on military AI use. ([Understanding AI, 2026-03-02](https://www.understandingai.org/p/the-pentagons-bombshell-deal-with))

## What practitioners use (themes with the most tool/technique + workaround findings)

*Building with AI:*
- **Model routing and cost-aware delegation**: 133 findings from 11 sources (71 tool/technique, 23 workaround; 94 total). Named: OpenRouter, Factory Router, Sakana Fugu, advisor strategy, subagent model pinning, small classifier routers
- **Verifying AI-generated code and UI changes**: 160 findings from 13 sources (73 tool/technique, 19 workaround; 92 total). Named: Playwright loops, separate checker agents, tests-first, holdout scenarios, digital twins, mutation testing, screenshot and video proofs
- **Routing and cross-checking work across multiple models**: 102 findings from 8 sources (45 tool/technique, 39 workaround; 84 total). Named: Claude plus Codex review loops, Codex plugin in Claude Code, OpenCode/OpenRouter, manual model switching, per-project routing instructions
- **Provider-agnostic harnesses and unified model interfaces**: 122 findings from 10 sources (62 tool/technique, 6 workaround; 68 total). Named: OpenRouter, Responses API spec, Vercel AI SDK, Deep Agents, Flue, Pi, OpenCode, Cline SDK, Hermes
- **Speculative decoding is fiddly and results vary**: 75 findings from 6 sources (61 tool/technique, 4 workaround; 65 total). Named: EAGLE-3, P-EAGLE, DFlash, DSpark in vLLM/SGLang, MTP in llama.cpp, ik_llama.cpp tuning, ngram drafting, GGUF patch scripts
- **Building eval datasets and custom evals is hard**: 129 findings from 11 sources (51 tool/technique, 11 workaround; 62 total). Named: Promptfoo, Braintrust, LangFuse, Phoenix, DeepEval, Inspect AI, production logs as regression sets
- **Plan-first and spec-first workflows with clarifying questions**: 93 findings from 9 sources (42 tool/technique, 19 workaround; 61 total). Named: Plan mode, Kiro specs, OpenSpec, interview skills, plan critique by another model, PRD skills
- **Agents ignore or bloat CLAUDE.md/AGENTS.md instruction files**: 89 findings from 7 sources (36 tool/technique, 25 workaround; 61 total). Named: Mistake logs, hooks forcing rule reads, trimmed files, symlinked AGENTS.md, rules files, pointer files
- **Portable, persistent, editable agent memory**: 139 findings from 12 sources (52 tool/technique, 8 workaround; 60 total). Named: AGENTS.md and MEMORY.md files, Mimir, MemMachine, Hyperspell, Supermemory, Honcho, wiki-style memory, SQLite stores, dreaming consolidation
- **Non-coders using coding agents for personal tools and apps**: 69 findings from 15 sources (50 tool/technique, 9 workaround; 59 total). Named: Claude Cowork, Claude Code desktop, Replit Agent, Lovable, Claude Artifacts, Expo Agent

*Everyday & business:*
- **Personal knowledge bases and local memory for agents**: 52 findings from 7 sources (25 tool/technique, 15 workaround; 40 total). Named: Obsidian with CLI or Web Clipper, Karpathy-style markdown wiki, SyncThing, SQLite FTS5, QMD, PersonalOS, local Mac memory tools, DigUp, iMessage export to Markdown, MCP sync.
- **Structured LLM-guided self-learning workflows**: 44 findings from 4 sources (21 tool/technique, 13 workaround; 34 total). Named: Socratic prompting, /teach-me commands, agent skills, long-running chat threads, Claude-designed curricula, MCP study tools
- **Keeping up with AI news and filtered feeds**: 56 findings from 9 sources (18 tool/technique, 9 workaround; 27 total). Named: TLDR, Rundown AI, news.smol.ai, HN, Lobsters, RSS readers, NetNewsWire, Parallel Monitor, keep.md, Scouts by Yutori, page-change monitors, Chrome extension merging X lists.
- **AI sycophancy: need for a challenging thought partner**: 39 findings from 7 sources (16 tool/technique, 11 workaround; 27 total). Named: Custom 'Absolute Mode' instructions, adversarial and steelman prompts, devil's advocate prompts, cross-checking Claude and ChatGPT, expert persona debates, rubber ducking.
- **Controllable, multilingual and local TTS with voice cloning**: 45 findings from 6 sources (23 tool/technique, 3 workaround; 26 total). Named: Qwen3-TTS, Chatterbox, VibeVoice, Fish Audio, Kokoro, Cartesia, Gemini TTS audio tags, Hume Voice Conversion
- **AI prose is generic and loses personal voice**: 83 findings from 9 sources (8 tool/technique, 15 workaround; 23 total). Named: Strict system prompts, anti-slop memory and style guides, critique-only prompts, nightly style guides, applying edits one at a time, hand editing, Kagi proofread, using ChatGPT/Claude instead of Grammarly.
- **Agent workspaces for non-technical knowledge workers**: 46 findings from 8 sources (18 tool/technique, 5 workaround; 23 total). Named: Claude Cowork, Openwork, Dispatch, Interpreter, Claude Code as chief of staff, Codex for non-code work, background agents making PRs from Slack.
- **AI design tools and design-to-code canvases**: 41 findings from 8 sources (23 tool/technique, 0 workaround; 23 total). Named: Magic Patterns, Penpot, Google Stitch, Figma AI, Claude Design, Magic Path, Refero DESIGN.md, Hallmark skill, Spline Agent Mode
- **Interviewing candidates who use AI assistants**: 40 findings from 4 sources (19 tool/technique, 4 workaround; 23 total). Named: Vague-spec tasks with AI code critique, code review exercises with planted bugs, paid work trials, explaining AI-built code, agent-based build projects, stating AI policy upfront.
- **Prompt-based cross-app workflow automation and mini-apps**: 29 findings from 7 sources (11 tool/technique, 9 workaround; 20 total). Named: Google Workspace Studio, Anthropic MCP gateway, Slack as agent UI, Zapier, Claude Skills recording, Google Sheets Canvas, vibe-coded internal tools.

**Most-mentioned tools** (in tool/technique/workaround findings): Claude 1,275, Claude Code 677, Codex 336, Opus 265, MCP 252, Gemini 234, Cursor 164, Qwen 161, Llama 155, ChatGPT 124, GPT-5 122, GLM 117, Kimi 113, DeepSeek 110, Ollama 86

## Who drives the conversation

| Person | Findings | Mostly about | Via |
|---|---|---|---|
| Simon Willison | 1,552 | devtools & IDEs, coding agents, safety & governance | Simon Willison's Weblog, Don't Worry About the Vase |
| Zvi Mowshowitz | 922 | safety & governance, evals & testing, consumer apps | Don't Worry About the Vase |
| Tomasz Tunguz | 833 | business & markets, agents & orchestration, observability & cost | Tomasz Tunguz, Don't Worry About the Vase |
| Ben Tossell | 713 | coding agents, agents & orchestration, productivity & knowledge work | Ben's Bites |
| Gary Marcus | 529 | safety & governance, research & capabilities, business & markets | Marcus on AI, Don't Worry About the Vase |
| Nathan Lambert | 442 | model training & fine-tuning, local & open models, research & capabilities | Interconnects, Don't Worry About the Vase |
| Alberto Romero | 298 | productivity & knowledge work, safety & governance, consumer apps | The Algorithmic Bridge |
| Ethan Mollick | 185 | agents & orchestration, productivity & knowledge work, evals & testing | One Useful Thing, Don't Worry About the Vase |
| swyx | 174 | agents & orchestration, coding agents, productivity & knowledge work | Latent Space, AINews (smol.ai) |
| Sebastian Raschka | 119 | inference & infra, model training & fine-tuning, local & open models | Ahead of AI |
| swyx & Alessio Fanelli | 106 | research & capabilities, agents & orchestration, evals & testing | Latent Space |
| Sayash Kapoor, Arvind Narayanan | 95 | evals & testing, safety & governance, research & capabilities | AI as Normal Technology |
| Hamel Husain | 94 | evals & testing, coding agents, devtools & IDEs | Hamel Husain, AINews (smol.ai) |
| Jack Clark | 69 | research & capabilities, safety & governance, evals & testing | Import AI, The Algorithmic Bridge |
| Anthropic | 62 | safety & governance, evals & testing, coding agents | Don't Worry About the Vase, Understanding AI |
| omarsar0 | 58 | agents & orchestration, RAG & retrieval, inference & infra | AINews (smol.ai), Latent Space |
| Timothy B. Lee | 56 | safety & governance, research & capabilities, business & markets | Understanding AI, Don't Worry About the Vase |
| Arvind Narayanan | 49 | research & capabilities, evals & testing, agents & orchestration | AI as Normal Technology, Don't Worry About the Vase |
| Eugene Yan | 48 | evals & testing, agents & orchestration, coding agents | Eugene Yan |
| Dean W. Ball | 47 | safety & governance, evals & testing, enterprise adoption | Don't Worry About the Vase |

## Trends (2025-12..2026-03 vs 2026-07..2026-10, per 1,000 findings)

**Rising** (≥15% change and ≥4 of the 6 biggest sources agree): safety & governance 71.7→128.0; observability & cost 34.6→45.5; Fable 0.0→15.5; cyber 1.3→16.2; security 16.4→40.6; computer use/browser agents 2.8→5.9; local/open weights 18.4→34.1; AGI/superintelligence 4.6→7.1

**Falling** (≥15% change and ≥4 of the 6 biggest sources agree): education & learning 15.8→12.4; devtools & IDEs 84.3→54.5; education/students 8.9→7.1; RAG 11.6→6.4; healthcare 6.6→3.3; Claude Code 50.3→25.2; hallucination 11.4→5.1; Cursor 23.0→6.3; Gemini 32.1→8.1; OpenClaw 11.0→1.7; Perplexity 11.5→1.4; Nano Banana 3.7→0.0

**Spikes** (one month far above usual): Fable in 2026-06 (48.5 vs median 0.0); OpenClaw in 2026-02 (29.7 vs median 2.7); OpenRouter in 2025-12 (25.5 vs median 3.4); Gemini in 2025-11 (85.5 vs median 15.0); Kimi in 2026-07 (27.0 vs median 5.2); healthcare in 2026-05 (29.1 vs median 6.2); Cursor in 2025-11 (37.5 vs median 8.6); robotics in 2026-10 (28.0 vs median 6.5); DeepSeek in 2026-11 (21.7 vs median 7.1); image generation in 2025-11 (31.0 vs median 10.2); fine-tuning in 2025-12 (24.1 vs median 9.3)

