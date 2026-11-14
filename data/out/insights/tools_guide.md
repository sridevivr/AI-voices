# The AI toolkit people actually used: a practical guide by job to be done

*A year of commentary, sorted into what to reach for when you want to organize knowledge, write, learn, delegate, create media, or build an app without being an engineer.*

*Period: 2025-11-11 to 2026-11-10 · 26,923 findings from 19 sources · generated 2026-11-14 by `python -m src.insights write`. Numbers and tables come from code; prose is Sonnet's; every link is a finding the text cites.*

## Key points

- For everyday work, the most repeated habit is giving AI your own material, such as local markdown notes, an Obsidian vault, or exported messages, so it answers from your context. ([Tomasz Tunguz, 2026-05-29](https://tomtunguz.com/the-pi-agent-skill-distillation/)) ([Hacker News — Ask HN, 2026-05-16](https://news.ycombinator.com/item?id=48160604)) ([Don't Worry About the Vase, 2026-08-27](https://thezvi.substack.com/p/ai-183-pre-post-mortem))
- To avoid flattery, people ask for honesty, set several expert personas to debate, or have a second model stress-test the idea. ([The Algorithmic Bridge, 2026-01-15](https://www.thealgorithmicbridge.com/p/learn-to-use-ai-competently-in-1)) ([Don't Worry About the Vase, 2026-05-28](https://thezvi.substack.com/p/ai-170-lack-of-executive-order)) ([Hacker News — Ask HN, 2026-05-10](https://news.ycombinator.com/item?id=48088126))
- To keep your voice in writing, split structure from prose and ask AI for a list of suggested changes to audit, rather than letting it rewrite. ([Exponential View, 2026-02-20](https://www.exponentialview.co/p/entering-the-trillion-agent-economy)) ([Don't Worry About the Vase, 2026-05-14](https://thezvi.substack.com/p/ai-168-not-leading-the-future)) ([Tomasz Tunguz, 2026-09-02](https://tomtunguz.com/ai-productivity-doesnt-mean-what-i-thought/))
- Agent workspaces such as Claude Cowork bring coding-agent style help to non-technical tasks, for example a phone-requested morning briefing from calendar, email and chat. ([AINews (smol.ai), 2026-01-12](https://news.smol.ai/issues/26-01-12-gemini-apple/)) ([One Useful Thing, 2026-03-31](https://www.oneusefulthing.org/p/claude-dispatch-and-the-power-of)) ([Ben's Bites, 2026-03-10](https://www.bensbites.com/p/just-use-gpt-54-xhigh))
- Among the tools named in building findings, Claude, Claude Code and Codex dominate the mention counts, and non-coders report building personal and family apps with them. ([Don't Worry About the Vase, 2026-02-12](https://thezvi.substack.com/p/ai-155-welcome-to-recursive-self)) ([Simon Willison's Weblog, 2026-08-21](https://simonwillison.net/2026/Aug/21/stop-making-tuis/))
- The build techniques that recur: plan before coding, keep instruction files short, have a different model check the work, and keep memory in plain files you can read. ([Simon Willison's Weblog, 2026-04-23](https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/)) ([Ben's Bites, 2026-02-24](https://www.bensbites.com/p/gemini-tops-benchmarks-again)) ([AINews (smol.ai), 2026-03-16](https://news.smol.ai/issues/26-03-16-not-much/)) ([Hacker News — Ask HN, 2026-11-04](https://news.ycombinator.com/item?id=50366117))
- Routing work across models by cost and task is a common workaround for limits and price, not just an engineer's hobby. ([Hacker News — Ask HN, 2026-03-29](https://news.ycombinator.com/item?id=47559293)) ([Ben's Bites, 2026-07-14](https://www.bensbites.com/p/how-to-use-gpt-56)) ([AINews (smol.ai), 2026-07-09](https://news.smol.ai/issues/26-07-09-gpt-56/))

## How to read this guide

This guide is grouped by the job you are trying to get done. Part 1 covers everyday and business use. Part 2 covers building apps with AI as a non-engineer, with tools first and then numbered techniques. The findings come from newsletters, blogs and Hacker News threads, so many examples come from technical writers. I have kept those that a non-specialist can copy.

Mention counts show which names came up most in tool and technique findings: Claude (1,275), Claude Code (677), Codex (336), Opus (265), MCP (252), Gemini (234) and Cursor (164). Counts show talk, not quality, and they do not tell you what is best for you.

## Part 1, Job: make your own notes and documents usable by AI

The most concrete pattern is a local folder of plain markdown files that an agent can search. Tomasz Tunguz keeps a markdown knowledge base (QMD) of workflow playbooks, and his agent searches it before answering procedural questions. ([Tomasz Tunguz, 2026-05-29](https://tomtunguz.com/the-pi-agent-skill-distillation/))

Another version is an Obsidian vault of debugged, reusable patterns that agents consult when starting a new project, in place of one large instruction file. Zvi Mowshowitz described exporting iMessage history into searchable Markdown or Obsidian files so AI can use personal message data. One Reddit user ran a local Qwen-3.5 model over a decade of personal documents to get a queryable knowledge base. ([Hacker News — Ask HN, 2026-05-16](https://news.ycombinator.com/item?id=48160604)) ([Don't Worry About the Vase, 2026-08-27](https://thezvi.substack.com/p/ai-183-pre-post-mortem)) ([AINews (smol.ai), 2026-04-13](https://news.smol.ai/issues/26-04-13-not-much/))

## Part 1, Job: learn something quickly

The learning findings share one idea: stay active. One user has an LLM generate code, reviews it closely, and questions it until they understand it. Another outlines the problem first, asks for best practices, then asks for pros and cons of each option for their situation. ([Hacker News — Ask HN, 2026-08-10](https://news.ycombinator.com/item?id=49246873)) ([Hacker News — Ask HN, 2026-08-10](https://news.ycombinator.com/item?id=49246873))

Two other tactics: Alberto Romero describes compressing learning into a structured one-day curriculum with exercises. Some users have an LLM write flawed arguments so they can practice spotting and rebutting them. ([The Algorithmic Bridge, 2026-01-15](https://www.thealgorithmicbridge.com/p/learn-to-use-ai-competently-in-1)) ([Don't Worry About the Vase, 2026-03-12](https://thezvi.substack.com/p/ai-159-see-you-in-court))

## Part 1, Job: keep up with AI news

Keeping up is itself a pain point in the findings, and people respond with filters. One Hacker News user recommends the curated digest news.smol.ai. Ben Tossell routes all saved items into one filtered feed with keep.md to feed a newsletter. Zvi Mowshowitz uses a Chrome extension to merge follow lists into a single 'All' list. ([Hacker News — Ask HN, 2026-06-16](https://news.ycombinator.com/item?id=48559049)) ([Ben's Bites, 2026-03-19](https://www.bensbites.com/p/what-makes-a-good-agentsmd)) ([Don't Worry About the Vase, 2026-07-14](https://thezvi.substack.com/p/twitter-thoughts-for-you))

A more elaborate approach comes from Azeem Azhar's analyst, who built synthetic personas modeled on named thinkers to scan hundreds of weekly items through their lenses. Treat that as an idea to borrow, not a setup to copy. ([Exponential View, 2026-03-13](https://www.exponentialview.co/p/the-lantern-and-the-flame))

## Part 1, Job: get pushback instead of flattery

Sycophancy, the habit of AI agreeing with you, is a recurring complaint. Alberto Romero uses AI as a thought partner that generates options and objections, asks for honesty over friendliness, and prefers Claude and Gemini for this. Another approach has an AI play several expert personas that debate a question, so you read the debate and form your own view. ([The Algorithmic Bridge, 2026-01-15](https://www.thealgorithmicbridge.com/p/learn-to-use-ai-competently-in-1)) ([Don't Worry About the Vase, 2026-05-28](https://thezvi.substack.com/p/ai-170-lack-of-executive-order))

You can also use more than one model. One user brainstorms in Claude, asks other LLMs to stress-test the idea, and feeds the results back into Claude. A writer in Azeem Azhar's circle uses an argument engine trained on his past writing to flag weaknesses such as claims asserted without evidence. A small tip from Akshay Nathan: retry tasks the models could not handle three or six months ago. ([Hacker News — Ask HN, 2026-05-10](https://news.ycombinator.com/item?id=48088126)) ([Exponential View, 2026-03-13](https://www.exponentialview.co/p/the-lantern-and-the-flame)) ([Latent Space, 2026-07-28](https://latent.space/p/chatgpt-work/))

## Part 1, Job: write without losing your voice

Generic AI prose is the largest complaint theme in this group, and the workarounds are about control. Do not ask the AI to 'correct' your writing. Ask it for a list of errors or suggested changes and audit it, or revise section by section. Another approach is to separate steps: build an outline first, then the prose. ([Don't Worry About the Vase, 2026-05-14](https://thezvi.substack.com/p/ai-168-not-leading-the-future)) ([Exponential View, 2026-02-20](https://www.exponentialview.co/p/entering-the-trillion-agent-economy))

Tomasz Tunguz runs a nightly system that updates his style guidelines from his own edits. Some users run Kagi's proofread feature to polish posts and important emails without generating the content. Romero suggests adding deliberately spiky or personal phrasing to avoid AI's balanced hedging. ([Tomasz Tunguz, 2026-09-02](https://tomtunguz.com/ai-productivity-doesnt-mean-what-i-thought/)) ([Hacker News — Ask HN, 2026-05-22](https://news.ycombinator.com/item?id=48235223)) ([The Algorithmic Bridge, 2025-12-03](https://www.thealgorithmicbridge.com/p/10-signs-of-ai-writing-that-99-of))

## Part 1, Job: delegate everyday knowledge work and automate across apps

Claude Cowork brings Claude Code-style efficiency to non-technical tasks. Ethan Mollick used Cowork with Dispatch to ask an agent from a phone to prepare a morning briefing from calendars, email and online channels. Another report describes Claude Code as a chief of staff running operations for a consultancy. ([AINews (smol.ai), 2026-01-12](https://news.smol.ai/issues/26-01-12-gemini-apple/)) ([One Useful Thing, 2026-03-31](https://www.oneusefulthing.org/p/claude-dispatch-and-the-power-of)) ([Ben's Bites, 2026-03-10](https://www.bensbites.com/p/just-use-gpt-54-xhigh))

Know the limits: Zvi Mowshowitz relays a user's report that Claude connectors manage Google products better than Google's own integrations, but that no AI they tried could properly edit Google Docs, especially creating comments. ([Don't Worry About the Vase, 2026-07-16](https://thezvi.substack.com/p/ai-177-part-1-tip-of-the-iceberg))

For cross-app automation, Google Workspace Studio builds automations that connect non-Google apps and add AI steps using only prompts. Smaller examples exist too: a personal cashflow tool built with AI that imports bank CSVs and projects recurring expenses, and Jack Clark's reusable Claude skill that mines his newsletter archive. ([Ben's Bites, 2025-12-04](https://www.bensbites.com/p/anthropic-makes-its-first-acquisition)) ([Hacker News — Ask HN, 2026-10-20](https://news.ycombinator.com/item?id=50159886)) ([Import AI, 2026-05-26](https://importai.substack.com/p/import-ai-458-reckoning-with-the))

## Part 1, Job: read what agents produce

Agents produce more than you can read, so people change the format. Ask for a throwaway HTML page instead of building a dashboard. Have the AI write design and explainer documents in HTML rather than markdown. Simon Willison asks Claude for HTML with SVG diagrams, interactive widgets and in-page navigation. ([Ben's Bites, 2026-06-30](https://www.bensbites.com/p/gpt-56-is-here-but)) ([Hacker News — Ask HN, 2026-09-29](https://news.ycombinator.com/item?id=49901420)) ([Simon Willison's Weblog, 2026-05-08](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/))

## Part 1, Job: make design, voice and video

For design, one workflow has GPT-5.5 create UI mockups with gpt-image-2 and then implement them. Ethan Mollick used an image model to render readable text for slides, product mockups and example websites. Anthropic's Dianne Na Penn is quoted saying Opus 4.7 has strong visual design taste, supporting Claude Design. ([Don't Worry About the Vase, 2026-04-28](https://thezvi.substack.com/p/gpt-55-capabilities-and-reactions)) ([One Useful Thing, 2026-04-23](https://www.oneusefulthing.org/p/sign-of-the-future-gpt-55)) ([Simon Willison's Weblog, 2026-05-06](https://simonwillison.net/2026/May/6/code-w-claude-2026/))

For voice, Simon Willison describes director's-notes prompts with audio profile, scene, style, pace and accent sections to steer Gemini 3.1 Flash TTS. For a local option, a Hacker News user ran Qwen3 TTS voice cloning with a reference clip and text to produce a custom audiobook. ([Simon Willison's Weblog, 2026-04-15](https://simonwillison.net/2026/Apr/15/gemini-31-flash-tts/)) ([Hacker News — Ask HN, 2026-10-05](https://news.ycombinator.com/item?id=49972125))

For video, editors use AI to remove silences and transcribe audio. Ben Tossell points to Kino, a tool for editing video with agents. Mollick notes Gemini Omni can see and edit video directly, unlike video AIs that only generate clips. ([Understanding AI, 2025-11-19](https://www.understandingai.org/p/an-ai-tsunami-is-coming-for-hollywood)) ([Ben's Bites, 2026-11-03](https://www.bensbites.com/p/if-you-feel-behind-right-now-dont)) ([One Useful Thing, 2026-07-23](https://www.oneusefulthing.org/p/an-opinionated-guide-to-which-ai-b22))

## Part 1, Job: hire in an AI-assisted world

If you hire, the findings favor tests that assume AI use. Some interviewers give a deliberately vague requirements document, have an AI generate code, and ask the candidate to critique and fix it. Sierra is piloting interviews where candidates improve a codebase with coding agents. David Singleton describes having engineers build short projects end-to-end with an agent of their choice and judging how they direct it. ([Hacker News — Ask HN, 2026-04-10](https://news.ycombinator.com/item?id=47722081)) ([Ben's Bites, 2026-04-23](https://www.bensbites.com/p/chatgpts-nano-banana)) ([Latent Space, 2026-03-20](https://latent.space/p/dreamer/))

## Part 2, The tools

The names that dominate the building findings are Claude Code (677 mentions), Codex (336) and Cursor (164). Others include OpenCode (60), OpenRouter (73) for reaching many models, Replit (16), Windsurf (16), v0 (22), Lovable (6) and Bolt (4). Mentions of the app builders are far fewer than mentions of the coding agents.

On the non-coder side, one report has users building small family tools with Claude Code without coding knowledge. Thomas Ptacek suggests agents make a native GUI cheap, so small personal tools need not stop at a command line. Nathan Lambert uses Opus- and Codex-based agents as general implementation aids for complex knowledge work, not just code. ([Don't Worry About the Vase, 2026-02-12](https://thezvi.substack.com/p/ai-155-welcome-to-recursive-self)) ([Simon Willison's Weblog, 2026-08-21](https://simonwillison.net/2026/Aug/21/stop-making-tuis/)) ([Interconnects, 2026-06-01](https://www.interconnects.ai/p/open-and-closed-models-are-on-different))

Preferences differ. Ben Tossell reports using Droid and Pi rather than Replit Agent for building agents, as a more reliable personal workflow. The input has no verdict on which tool is winning, so choose by trying a small project. ([Ben's Bites, 2026-03-21](https://www.bensbites.com/p/bens-builds-2))

## Part 2, Techniques that make builds work

**1. Plan before you build.** Simon Willison writes a plan.md in the repo and iterates on it with Claude Code before implementation, asking for small commits to keep vibe-coded projects reviewable. Another approach is interview-style specs, where the agent asks clarifying questions first, for example with a /grill-me command. ([Simon Willison's Weblog, 2026-04-23](https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/)) ([Hacker News — Ask HN, 2026-10-19](https://news.ycombinator.com/item?id=50151036))

**2. Use one model to plan and another to build.** Nathan Lambert uses GPT 5 Pro for planning and Claude Code with Opus 4.5 for implementation, passing information back to GPT 5 Pro when stuck. ([Interconnects, 2026-01-21](https://www.interconnects.ai/p/get-good-at-agents))

**3. Keep instruction files short.** Claude Code checks for AGENTS.md by default when no CLAUDE.md is present, so instructions carry across tools. But elaborate files may hurt: Ben Tossell reports people trimming them, and Sebastian Raschka says developers prune or regenerate AGENTS.md and SKILL.md files because older hand-holding over-constrains newer models. ([Don't Worry About the Vase, 2026-09-24](https://thezvi.substack.com/p/ai-187-coming-into-play)) ([Ben's Bites, 2026-02-24](https://www.bensbites.com/p/gemini-tops-benchmarks-again)) ([Ahead of AI, 2026-09-09](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and))

**4. Have a different model check the work.** One dual-agent setup uses one model to write code and a separate model to review it, to avoid self-validating test gaming. Tomasz Tunguz recommends layering a reviewer agent, tests and production observability instead of one gate. ([AINews (smol.ai), 2026-03-16](https://news.smol.ai/issues/26-03-16-not-much/)) ([Tomasz Tunguz, 2026-09-24](https://tomtunguz.com/thinking-in-systems/))

**5. Check the visible result, not only the code.** swyx has a visual play-test skill that catches design issues reading code would miss. For ports, Andreas Kling required byte-for-byte identical output against the trusted original. ([Latent Space, 2026-09-30](https://latent.space/p/devday-2026/)) ([Simon Willison's Weblog, 2026-02-23](https://simonwillison.net/2026/Feb/23/ladybird-adopts-rust/))

**6. Route tasks by cost and difficulty.** One user keeps per-project instruction files that send simple work to cheaper models and hard work to stronger ones. Others pin subagents to cheaper models under a coordinator. Ben Tossell describes picking different GPT-5.6 models and thinking levels per task to manage limits. ([Hacker News — Ask HN, 2026-03-29](https://news.ycombinator.com/item?id=47559293)) ([AINews (smol.ai), 2026-07-09](https://news.smol.ai/issues/26-07-09-gpt-56/)) ([Ben's Bites, 2026-07-14](https://www.bensbites.com/p/how-to-use-gpt-56))

**7. Keep memory in files you can read.** One Hacker News user keeps LOG.md, HANDOFF.md and DECISIONS.md under version control. Ben Tossell syncs every agent memory to a Google Doc so he can inspect it. A shared agents.md plus a humans.md progress log lets you switch models or harnesses mid-project. ([Hacker News — Ask HN, 2026-11-04](https://news.ycombinator.com/item?id=50366117)) ([Ben's Bites, 2026-10-06](https://www.bensbites.com/p/thoughts-from-san-francisco)) ([Hacker News — Ask HN, 2026-06-17](https://news.ycombinator.com/item?id=48565600))

**8. Build a small test set from real examples.** Teams sample production inputs and outputs into a spreadsheet and label them. Another builds eval questions by mining real support emails. Eval-driven development measures every agent change against a fixed set, like TDD for agents. ([Eugene Yan, 2025-11-23](https://eugeneyan.com//writing/product-evals/)) ([Hacker News — Ask HN, 2026-03-10](https://news.ycombinator.com/item?id=47319587)) ([AINews (smol.ai), 2026-11-10](https://latent.space/p/ainews-fable-5-2-retakes-world-1-llm-spot-as-ant-ipo-roadshow-begins/))

**9. Run agent code in a sandbox.** Simon Willison's datasette-agent-sprites plugin runs code in a Fly Sprites persistent sandbox. One user prototypes with Podman and gVisor, planning to swap in Firecracker for stronger isolation. In a survey Tomasz Tunguz cites, Cloudflare hosts agent sandboxes for 62% of teams writing code with agents. ([Simon Willison's Weblog, 2026-05-21](https://simonwillison.net/2026/May/21/datasette-agent/)) ([Hacker News — Ask HN, 2026-01-01](https://news.ycombinator.com/item?id=46450931)) ([Tomasz Tunguz, 2026-10-13](https://tomtunguz.com/ai-in-practice-survey-2026/))

**10. Read the traces.** Hamel Husain notes teams build custom trace viewers to make reading and annotating LLM traces easier. In another Tunguz survey, teams analyze agent performance with BI tools (56%), coding agents (48%), observability tools (41%) and spreadsheets (30%), so no dedicated category has won. ([Hamel Husain, 2026-03-26](https://hamel.dev/blog/posts/revenge/)) ([Tomasz Tunguz, 2026-10-13](https://tomtunguz.com/ai-in-practice-survey-2026/))

## Table: most-mentioned tools

Mentions in tool/technique/workaround findings. The sources lean toward builders; read as "what this crowd recommends", not market share.

| Tool | Mentions |
|---|---|
| Claude | 1,275 |
| Claude Code | 677 |
| Codex | 336 |
| Opus | 265 |
| MCP | 252 |
| Gemini | 234 |
| Cursor | 164 |
| Qwen | 161 |
| Llama | 155 |
| ChatGPT | 124 |
| GPT-5 | 122 |
| GLM | 117 |
| Kimi | 113 |
| DeepSeek | 110 |
| Ollama | 86 |
| Gemma | 80 |
| OpenRouter | 73 |
| Fable | 69 |
| OpenCode | 60 |
| Slack | 60 |
| Sonnet | 54 |
| AGENTS.md | 51 |
| CLAUDE.md | 51 |
| Datasette | 47 |
| LM Studio | 45 |
| Cowork | 41 |
| Perplexity | 40 |
| Docker | 30 |
| Copilot | 28 |
| Nano Banana | 28 |
| Cline | 24 |
| v0 | 22 |
| Playwright | 22 |
| Notion | 20 |
| Deep Research | 20 |
| Obsidian | 19 |
| Excel | 19 |
| Gmail | 19 |
| ElevenLabs | 18 |
| Replit | 16 |
| Windsurf | 16 |
| Figma | 15 |
| NotebookLM | 12 |
| Whisper | 11 |
| Suno | 8 |
| n8n | 7 |
| Lovable | 6 |
| Conductor | 6 |
| Zapier | 5 |
| Veo | 5 |
| Bolt | 4 |
| Sora | 4 |
| Remotion | 4 |
| Claude Design | 4 |
| Granola | 3 |
| Gamma | 3 |
| Artifacts | 3 |

