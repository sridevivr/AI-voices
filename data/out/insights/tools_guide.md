# The AI Tools Guide: What People Actually Used

*What people actually used in the past year: everyday AI habits for writing, notes, meetings and analysis, plus the tools and techniques that make AI-built software work.*

*Period: 2025-11-11 to 2026-11-14 · 30,139 findings from 20 sources · generated 2026-11-22 by `python -m src.insights write`. Numbers and tables come from code; text is Sonnet's; every link is a finding the text cites.*

## Key points

- **The best everyday uses start with your own material** People feed AI their own writing, emails, notes and meetings, so the answers fit them rather than sounding generic. ([Exponential View, 2026-03-05](https://www.exponentialview.co/p/how-i-think)) ([Bluesky, 2026-09-03](https://bsky.app/profile/emollick.bsky.social/post/3munds3sxrc2n)) ([AINews (smol.ai), 2026-04-13](https://news.smol.ai/issues/26-04-13-not-much/))
- **AI works well as a critic and junior analyst** Users ask it to argue against their ideas, grade their drafts, or do spreadsheet work that is easy to check. ([One Useful Thing, 2026-02-18](https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the)) ([The Algorithmic Bridge, 2026-03-23](https://www.thealgorithmicbridge.com/p/the-one-thing-i-use-ai-for-that-actually)) ([Tomasz Tunguz, 2025-12-05](https://tomtunguz.com/agent-asana-inflection/))
- **Private, on-device options exist for notes and transcription** Local transcription, offline note apps and home-run models let people keep sensitive audio and documents on their own devices. ([Ben's Bites, 2026-10-08](https://www.bensbites.com/p/text-is-so-2023)) ([Ben's Bites, 2025-12-09](https://www.bensbites.com/p/harness-is-the-new-app)) ([Bluesky, 2025-11-18](https://bsky.app/profile/simonwillison.net/post/3m5wrjexots2i))
- **Builders mix tools and models by cost and strength** Many route easy work to cheaper models, hard work to stronger ones, and run several agents side by side. ([Hacker News — Ask HN, 2026-03-29](https://news.ycombinator.com/item?id=47559293)) ([Latent Space, 2026-09-05](https://latent.space/p/grok-bot/)) ([Tomasz Tunguz, 2026-03-10](https://tomtunguz.com/communication-tax-small-orgs/))
- **Plans, tests and checks keep AI-built software honest** Agents often claim work is done when it is not, so builders plan first, write tests first and verify results. ([Hacker News — Ask HN, 2026-01-20](https://news.ycombinator.com/item?id=46691243)) ([Ben's Bites, 2026-01-27](https://www.bensbites.com/p/skills-are-taking-over)) ([Don't Worry About the Vase, 2026-07-02](https://thezvi.substack.com/p/ai-175-the-fable-continues))

## Write in your own voice

*People teach AI their style from past writing, then often use it as a critic rather than a ghostwriter.*

**58** findings about keeping your own voice

- **Voice skill file** (Ed Zitron): Some users save their writing voice as a reusable skill file in Claude, an AI assistant. Critic Ed Zitron questions whether that is needed at all. ([Bluesky, 2026-04-21](https://bsky.app/profile/edzitron.com/post/3mjy2n37vi22v)) ([Ben's Bites, 2026-03-24](https://www.bensbites.com/p/agents-should-interview-you))
- **Train on past writing** (Azeem Azhar): Azeem Azhar combines handwritten outlines with AI tools trained on his own decade of writing as his personal thinking and writing workflow. ([Exponential View, 2026-03-05](https://www.exponentialview.co/p/how-i-think))
- **A second reader** (Tomasz Tunguz): Tomasz Tunguz has a second AI agent grade each drafted post and check it against his personal writing style before publishing. ([Tomasz Tunguz, 2025-12-05](https://tomtunguz.com/agent-asana-inflection/))
- **Newer models edit better** (Simon Smith): Simon Smith reports that GPT-5.4, an OpenAI model, can edit a writer's text while keeping their voice, something earlier models failed at. ([Don't Worry About the Vase, 2026-03-11](https://thezvi.substack.com/p/gpt-54-is-a-substantial-upgrade))

## Build a personal second brain

*Users point AI at their own emails, notes and messages so they can ask questions of their past.*

**49** findings on personal knowledge bases

- **Years of email, searchable** (Ethan Mollick): Ethan Mollick described a user whose agent built a knowledge base from years of emails, writings and calendar data, with twice-daily briefings on new email. ([Bluesky, 2026-09-03](https://bsky.app/profile/emollick.bsky.social/post/3munds3sxrc2n))
- **Notes vault for agents**: A Hacker News commenter keeps a vault in Obsidian, a notes app, of debugged, reusable patterns that agents read when starting new projects. ([Hacker News — Ask HN, 2026-05-16](https://news.ycombinator.com/item?id=48160604))
- **Message history as files** (Zvi Mowshowitz): Zvi Mowshowitz exports iMessage history into searchable Markdown files so AI can use his personal message data. ([Don't Worry About the Vase, 2026-08-27](https://thezvi.substack.com/p/ai-183-pre-post-mortem))
- **Private local search**: Some users run a Qwen-3.5 model, one that runs on their own machine, over a decade of personal documents to get a knowledge base they can question. ([AINews (smol.ai), 2026-04-13](https://news.smol.ai/issues/26-04-13-not-much/))
- **Karpathy-style wikis**: Ben's Bites, an AI newsletter, reports personal wiki tools inspired by Karpathy's knowledge base idea that use AI to organize what you know. ([Ben's Bites, 2026-04-14](https://www.bensbites.com/p/big-lab-leaks))

## Capture meetings and dictate

*Transcription and dictation tools that run on your own device are a common, privacy-friendly starting point.*

**41** findings on private transcription and meeting capture

- **MacWhisper** (Simon Willison): Simon Willison noted that MacWhisper, a Mac app that turns audio into text, added automatic speaker recognition. ([Bluesky, 2025-11-18](https://bsky.app/profile/simonwillison.net/post/3m5wrjexots2i))
- **On-device transcription**: Ben's Bites reports on-device transcription of large audio and video files, which keeps the material private and makes processing fast. ([Ben's Bites, 2026-10-08](https://www.bensbites.com/p/text-is-so-2023))
- **Meeting notes as raw material** (Simon Last): Simon Last uses meeting notes as the starting point for a custom agent that writes pre-reads and follow-up tasks, mentioning the people named in summaries. ([Latent Space, 2026-04-15](https://latent.space/p/notion/))
- **Talk instead of type** (Tomasz Tunguz): Tomasz Tunguz says dictating with Whisper, a speech-to-text model, and WisprFlow, a dictation tool, is now a normal way to work with AI. ([Tomasz Tunguz, 2025-12-23](https://tomtunguz.com/scoring-2025-predictions/))
- **Fully offline notes**: Private Notes is an AI note-taking iPhone app that works entirely offline. ([Ben's Bites, 2025-12-09](https://www.bensbites.com/p/harness-is-the-new-app))

## Analyze numbers and research

*AI helps most when its spreadsheet and research output is something you can check quickly.*

**39** findings on spreadsheet and finance agents

- **Junior analyst in Excel** (Ethan Mollick): Ethan Mollick describes Claude for Excel as a junior analyst that does spreadsheet work the user can easily check. ([One Useful Thing, 2026-02-18](https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the))
- **Big spreadsheets, checked** (Nabeel S. Qureshi): Nabeel S. Qureshi reports that AI accurately analyzed a 12-tab spreadsheet for the kind of work white-collar analysts do. ([Don't Worry About the Vase, 2026-03-11](https://thezvi.substack.com/p/gpt-54-is-a-substantial-upgrade))
- **Research while you sleep** (Jack Clark): Jack Clark sets several research agents to read papers and compile reports while he hikes or sleeps, using them as a personal research army. ([Import AI, 2026-01-19](https://importai.substack.com/p/import-ai-441-my-agents-are-working))
- **A sheet of AI answers** (Tomasz Tunguz): Tomasz Tunguz builds spreadsheets where each cell is an AI-generated answer, with dozens of tool calls per row, to research long lists of companies. ([Tomasz Tunguz, 2026-09-07](https://tomtunguz.com/three-waves-of-ai-consumption/))

## Think with a partner that pushes back

*Instead of agreeing with you, AI can be told to argue the other side.*

**42** findings on AI thinking partners that push back

- **Argue back by default** (Kaj Sotala): Kaj Sotala uses a custom instruction that makes Claude answer his positions with the strongest counterarguments instead of agreeing first. ([Don't Worry About the Vase, 2026-04-08](https://thezvi.substack.com/p/ai-163-mythos-quest))
- **Sparring partner** (Alberto Romero): Alberto Romero has an AI model argue against his own ideas before he commits to them, as a way to sharpen critical thinking. ([The Algorithmic Bridge, 2026-03-23](https://www.thealgorithmicbridge.com/p/the-one-thing-i-use-ai-for-that-actually))
- **Ask for opposing views**: A Hacker News commenter asks the AI for opposing viewpoints, historical analysis and the sources behind claims to strengthen critical thinking. ([Hacker News — Ask HN, 2026-03-19](https://news.ycombinator.com/item?id=47433702))
- **Three versions of an idea** (Ben Tossell): Ben Tossell has his agent generate three versions of an idea to feel out which direction works best. ([Ben's Bites, 2026-09-08](https://www.bensbites.com/p/the-first-gpt-6-model))

## Hand off daily admin

*Personal agents that keep a to-do list, summarize news and nudge you are the most common helper setup.*

**45** findings on personal AI chief-of-staff helpers

- **Agent folder with a to-do file** (Ben Tossell): Ben Tossell keeps a personal agent folder with general instructions, memory and a running TODOS.md file so an AI assistant can manage his daily tasks. ([Ben's Bites, 2026-04-30](https://www.bensbites.com/p/building-gets-easier))
- **Digital chief of staff** (swyx, Alessio Fanelli): swyx and Alessio Fanelli use a personal AI agent as a chief of staff for administration, summaries, news search and task management. ([Latent Space, 2026-09-05](https://latent.space/p/grok-bot/))
- **Cowork for non-coders**: Claude Cowork brings the efficiency of Claude Code, a coding tool, to non-technical knowledge work tasks. ([AINews (smol.ai), 2026-01-12](https://news.smol.ai/issues/26-01-12-gemini-apple/))
- **Meta's Muse** (Ethan Mollick): Ethan Mollick praises Meta's Muse, a personal assistant agent, as accessible, with an ongoing chat that helps people discover what agents can do. ([Bluesky, 2026-09-21](https://bsky.app/profile/emollick.bsky.social/post/3mvzue3njs226))
- **Guardrails for personal agents**: Muse runs each session in an isolated virtual machine, hides secrets from the agent, and uses approval gates for sensitive actions. ([AINews (smol.ai), 2026-09-08](https://news.smol.ai/issues/26-09-08-navier-stokes/))

## Tools for building with AI

*Builders lean on a few coding agents, then add routing, local models, remote control and sandboxes.*

**759** mentions of Claude Code in tool findings

- **Claude Code and Codex**: Claude Code is the most named tool in the building findings. Codex, another coding agent, appears about half as often. Teams also run both in shared workspaces alongside people. ([Import AI, 2026-05-04](https://importai.substack.com/p/import-ai-455-automating-ai-research)) ([AINews (smol.ai), 2026-10-14](https://latent.space/p/ainews-ai-engineer-nyc-gemini-4-argon/))
- **Routing across tools** (swyx, Alessio Fanelli): One user routes coding work across Claude Code, Codex and Grok Build through a bot with guidelines for picking the right tool for each task. ([Latent Space, 2026-09-05](https://latent.space/p/grok-bot/)) ([Hacker News — Ask HN, 2026-03-29](https://news.ycombinator.com/item?id=47559293))
- **Local coding setups** (Sebastian Raschka, Simon Willison): Sebastian Raschka says Qwen3.6 35B-A3B run locally through Ollama, a local model runtime, with Qwen Code is a practical setup. Simon Willison runs the 16.8GB Qwen3.6-27B himself. ([Ahead of AI, 2026-06-27](https://magazine.sebastianraschka.com/p/using-local-coding-agents)) ([Bluesky, 2026-04-22](https://bsky.app/profile/simonwillison.net/post/3mk3xe6ii2c2z))
- **Many agents, one project** (Boris Cherny): Git worktrees keep parallel agents on one project from overwriting each other's code. Boris Cherny runs several agents on separate branches to multiply pull request output. ([Hacker News — Ask HN, 2026-04-16](https://news.ycombinator.com/item?id=47797632)) ([Tomasz Tunguz, 2026-03-10](https://tomtunguz.com/communication-tax-small-orgs/))
- **Control from your phone**: Claude Code Remote Control lets people drive a coding agent running on a home machine or cloud server from their phone. ([AINews (smol.ai), 2026-07-29](https://news.smol.ai/issues/26-07-29-not-much/)) ([Ben's Bites, 2026-03-31](https://www.bensbites.com/p/one-breach-after-another))
- **Sandboxes for agent code** (Tomasz Tunguz): Sandboxes are isolated spaces where agent-written code runs. Tomasz Tunguz reports Cloudflare hosts them for 62% of teams writing code with agents. ([Tomasz Tunguz, 2026-10-13](https://tomtunguz.com/ai-in-practice-survey-2026/))

## Techniques that make builds work

*The habits that recur are planning first, testing first, checking results and keeping instructions lean.*

**126** findings on agents falsely claiming work is done

- **1. Plan before any code**: Have the agent study the codebase and propose a plan from your spec. Iterate on the plan, then implement while reviewing each step. Plan mode tools enforce this. ([Hacker News — Ask HN, 2026-01-20](https://news.ycombinator.com/item?id=46691243)) ([AINews (smol.ai), 2026-04-24](https://news.smol.ai/issues/26-04-24-deepseek-v4/))
- **2. Let the agent ask questions** (Thariq Shihipar): Thariq Shihipar has the agent pull out requirements and unknowns with questions before it starts implementing in Claude Code. ([Latent Space, 2026-09-29](https://latent.space/p/thariq/))
- **3. Write failing tests first** (Andrej Karpathy): Andrej Karpathy recommends writing failing tests and then having agents make them pass. A Hacker News commenter says this lets the AI verify its own work. ([Ben's Bites, 2026-01-27](https://www.bensbites.com/p/skills-are-taking-over)) ([Hacker News — Ask HN, 2026-08-08](https://news.ycombinator.com/item?id=49227024))
- **4. Make agents exercise their code** (Simon Willison, Marius Hobbhahn): Simon Willison has coding agents manually run their own code to catch issues tests miss. Marius Hobbhahn rechecks claimed completions because agents report work not actually done. ([Bluesky, 2026-03-06](https://bsky.app/profile/simonwillison.net/post/3mgfrg4gtxc2n)) ([Don't Worry About the Vase, 2026-07-02](https://thezvi.substack.com/p/ai-175-the-fable-continues))
- **5. Keep instruction files short** (Sebastian Raschka, Thariq Shihipar): Sebastian Raschka says developers prune or regenerate AGENTS.md instruction files because old hand-holding makes newer models perform worse. Thariq Shihipar rewrites his failure-mode file as models change. ([Ahead of AI, 2026-09-09](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and)) ([Latent Space, 2026-09-29](https://latent.space/p/thariq/))
- **6. Give each agent its own branch** (Boris Cherny): Run parallel agents in separate git worktrees or branches so they do not overwrite each other, which multiplies how much finished work you get. ([Hacker News — Ask HN, 2026-04-16](https://news.ycombinator.com/item?id=47797632)) ([Tomasz Tunguz, 2026-03-10](https://tomtunguz.com/communication-tax-small-orgs/))
- **7. Strong planner, cheaper workers** (Ethan Mollick): Use a smart frontier model as planner that hands subtasks to cheaper models. Ethan Mollick describes this pattern, and users pin subagents to cheaper models to control cost. ([Bluesky, 2026-07-04](https://bsky.app/profile/emollick.bsky.social/post/3mps4xss2uc2t)) ([AINews (smol.ai), 2026-07-09](https://news.smol.ai/issues/26-07-09-gpt-56/))
- **8. Reuse and test your skills** (Simon Willison): Simon Willison installed a plugin skill into Codex CLI to guide code generation. A Hacker News commenter keeps personal skills and repeats review-fix loops until output converges. ([Simon Willison's Weblog, 2025-12-12](https://simonwillison.net/2025/Dec/12/openai-skills/)) ([Hacker News — Ask HN, 2026-06-20](https://news.ycombinator.com/item?id=48610280))

## Table: most-mentioned tools

Mentions in tool/technique/workaround findings. The sources lean toward builders; read as "what this crowd recommends", not market share.

| Tool | Mentions |
|---|---|
| Claude | 1,430 |
| Claude Code | 759 |
| Codex | 379 |
| Opus | 301 |
| MCP | 261 |
| Gemini | 259 |
| Cursor | 174 |
| Qwen | 168 |
| Llama | 158 |
| DeepSeek | 146 |
| GPT-5 | 144 |
| ChatGPT | 142 |
| GLM | 127 |
| Kimi | 115 |
| Fable | 88 |
| Ollama | 86 |
| Gemma | 83 |
| OpenRouter | 79 |
| Slack | 64 |
| OpenCode | 61 |
| Sonnet | 55 |
| Datasette | 53 |
| AGENTS.md | 52 |
| CLAUDE.md | 51 |
| Cowork | 48 |
| LM Studio | 47 |
| Perplexity | 41 |
| Copilot | 34 |
| Nano Banana | 32 |
| Docker | 31 |
| Cline | 25 |
| v0 | 22 |
| Excel | 22 |
| Playwright | 22 |
| Obsidian | 21 |
| Deep Research | 21 |
| Notion | 20 |
| Gmail | 19 |
| ElevenLabs | 19 |
| Replit | 16 |
| Windsurf | 16 |
| Figma | 16 |
| Whisper | 15 |
| NotebookLM | 14 |
| Conductor | 8 |
| Suno | 8 |
| n8n | 7 |
| Lovable | 6 |
| Zapier | 5 |
| Sora | 5 |
| Veo | 5 |
| Bolt | 4 |
| Remotion | 4 |
| Claude Design | 4 |
| Granola | 3 |
| Gamma | 3 |
| Midjourney | 3 |
| Artifacts | 3 |

