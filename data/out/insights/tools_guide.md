# The AI Tools and Habits People Actually Used

*From writing in your own voice to running parallel coding agents, here are the tools and techniques that people reported working, grouped by the job they do.*

*Period: 2025-11-11 to 2026-11-14 · 30,139 findings from 20 sources · generated 2026-11-22 by `python -m src.insights write`. Numbers and tables come from code; text is Sonnet's; every link is a finding the text cites.*

## Key points

- **Claude tools dominate what people name** Claude shows up in 1430 tool findings and Claude Code in 759, ahead of Codex at 379. Gemini and Cursor trail well behind. ([Ben's Bites, 2026-10-29](https://www.bensbites.com/p/ai-is-overwhelming-and-im-doing-it))
- **Everyday value comes from pointing AI at your own material** Emails, notes, messages and past writing become searchable knowledge bases and voice guides that agents can draw on. ([Bluesky, 2026-09-03](https://bsky.app/profile/emollick.bsky.social/post/3munds3sxrc2n)) ([Hacker News — Ask HN, 2026-05-16](https://news.ycombinator.com/item?id=48160604)) ([Exponential View, 2026-03-05](https://www.exponentialview.co/p/how-i-think))
- **Private, local options are now practical** People run local models for coding, transcription and personal search, trading some convenience for privacy and control. ([Ahead of AI, 2026-06-27](https://magazine.sebastianraschka.com/p/using-local-coding-agents)) ([Bluesky, 2025-11-18](https://bsky.app/profile/simonwillison.net/post/3m5wrjexots2i)) ([AINews (smol.ai), 2026-04-13](https://news.smol.ai/issues/26-04-13-not-much/))
- **Agents need checking, so builders add checks** Agents sometimes claim work is done when it is not. Tests written first and agents running their own code catch this. ([Hacker News — Ask HN, 2026-08-08](https://news.ycombinator.com/item?id=49227024)) ([Bluesky, 2026-03-06](https://bsky.app/profile/simonwillison.net/post/3mgfrg4gtxc2n)) ([Don't Worry About the Vase, 2026-07-02](https://thezvi.substack.com/p/ai-175-the-fable-continues))
- **Match the model to the task** Builders send hard work to strong models and easy work to cheaper ones, using routing rules and subagents to control cost. ([Hacker News — Ask HN, 2026-03-29](https://news.ycombinator.com/item?id=47559293)) ([Don't Worry About the Vase, 2026-07-28](https://thezvi.substack.com/p/claude-opus-5-is-highly-capable-but)) ([Bluesky, 2026-07-04](https://bsky.app/profile/emollick.bsky.social/post/3mps4xss2uc2t))

## Write in your own voice

*People keep their voice by feeding AI their own writing and using it as an editor or critic.*

**58** findings on keeping personal voice with AI

- **Voice skill file** (Ed Zitron): Some users write a Claude skill file that captures how they write. Ed Zitron mocked the idea as unnecessary, so treat it as one option, not a must. ([Bluesky, 2026-04-21](https://bsky.app/profile/edzitron.com/post/3mjy2n37vi22v))
- **Outline by hand, AI trained on you** (Azeem Azhar): Azeem Azhar starts from handwritten outlines and uses AI tools trained on a decade of his own writing as his thinking and writing workflow. ([Exponential View, 2026-03-05](https://www.exponentialview.co/p/how-i-think))
- **Second agent grades drafts** (Tomasz Tunguz): A second agent grades drafted posts and checks them against the author's personal writing style before publishing. ([Tomasz Tunguz, 2025-12-05](https://tomtunguz.com/agent-asana-inflection/))
- **Written style guides**: Writing an AI style guide gives the model something concrete to imitate when it drafts in your voice. ([Ben's Bites, 2026-03-24](https://www.bensbites.com/p/agents-should-interview-you))
- **Editing without flattening** (Simon Smith): GPT-5.4 is reported to edit a user's writing while preserving their voice, something earlier models failed at. ([Don't Worry About the Vase, 2026-03-11](https://thezvi.substack.com/p/gpt-54-is-a-substantial-upgrade))

## Build a personal knowledge base

*Turn years of emails, notes and messages into something an agent can search and brief you from.*

**49** findings on personal knowledge bases for agents

- **Agent-built briefings** (Ethan Mollick): One user had an agent assemble a knowledge base from years of emails, writings and calendar data, with twice-daily briefings that cross-reference new emails. ([Bluesky, 2026-09-03](https://bsky.app/profile/emollick.bsky.social/post/3munds3sxrc2n))
- **Obsidian vault of skills** (zambelli): Keep a personal Obsidian vault of debugged, reusable patterns that agents consult when starting projects, instead of one huge instruction file. ([Hacker News — Ask HN, 2026-05-16](https://news.ycombinator.com/item?id=48160604))
- **Local model over your documents** (Unlucky-Message8866): Some users run a local Qwen-3.5 model over a decade of personal documents to make them queryable without sending them out. ([AINews (smol.ai), 2026-04-13](https://news.smol.ai/issues/26-04-13-not-much/))
- **Messages into Markdown** (Zvi Mowshowitz): Exporting iMessage history into searchable Markdown or Obsidian files makes personal message data usable by AI. ([Don't Worry About the Vase, 2026-08-27](https://thezvi.substack.com/p/ai-183-pre-post-mortem))
- **Karpathy-style wikis**: Personal wiki tools inspired by Karpathy's knowledge base idea are being built to organize what you know with LLMs. ([Ben's Bites, 2026-04-14](https://www.bensbites.com/p/big-lab-leaks))

## Capture meetings and dictation

*On-device transcription keeps recordings private and turns meetings into notes and follow-up tasks.*

**41** findings on private transcription and meeting capture

- **MacWhisper** (Simon Willison): MacWhisper, a macOS app that transcribes audio with Whisper or NVIDIA Parakeet, added automatic speaker recognition. ([Bluesky, 2025-11-18](https://bsky.app/profile/simonwillison.net/post/3m5wrjexots2i))
- **On-device for big files**: Transcribing large audio and video files on your own device is described as private and fast. ([Ben's Bites, 2026-10-08](https://www.bensbites.com/p/text-is-so-2023))
- **Meeting notes as data** (Simon Last): Meeting notes feed a custom agent that writes pre-reads and follow-up tasks and @-mentions the people referenced in summaries. ([Latent Space, 2026-04-15](https://latent.space/p/notion/))
- **Voice dictation as default** (Tomasz Tunguz): Dictating with Whisper and WisprFlow, or talking to Gemini Live, is now a normal way to work with AI. ([Tomasz Tunguz, 2025-12-23](https://tomtunguz.com/scoring-2025-predictions/))
- **Swap in a faster model** (antirez): A Telegram bot for transcribing voice messages moved from Whisper medium to Qwen3-ASR for better speed at equal quality. ([Bluesky, 2026-02-12](https://bsky.app/profile/antirez.bsky.social/post/3meogdxi4222v))

## Analyze spreadsheets and research

*Treat AI as a junior analyst whose work you can check, and let agents do the reading at scale.*

**39** findings on spreadsheet and analyst agents

- **Claude for Excel** (Ethan Mollick): Claude for Excel acts like a junior analyst that does spreadsheet work the user can easily check. ([One Useful Thing, 2026-02-18](https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the))
- **Big messy workbooks** (Nabeel S. Qureshi): An AI analyzed a 12-tab spreadsheet accurately, the kind of white-collar analysis work many people do by hand. ([Don't Worry About the Vase, 2026-03-11](https://thezvi.substack.com/p/gpt-54-is-a-substantial-upgrade))
- **AI answer in every cell** (Tomasz Tunguz): Build spreadsheets where each cell is an AI-generated answer, with dozens of tool calls per row, to research lists of companies at scale. ([Tomasz Tunguz, 2026-09-07](https://tomtunguz.com/three-waves-of-ai-consumption/))
- **Research agent army** (Jack Clark): Set several research agents to read papers and compile reports while you hike or sleep. ([Import AI, 2026-01-19](https://importai.substack.com/p/import-ai-441-my-agents-are-working))
- **Apps inside Sheets**: Google Sheets Canvas lets users build apps inside Sheets that stay in sync with the spreadsheet data. ([Ben's Bites, 2026-08-18](https://www.bensbites.com/p/do-you-use-a-personal-agent))

## Delegate daily admin

*Personal agents work best with a simple home base of instructions, memory and a running task list.*

**45** findings on personal chief-of-staff assistants

- **Agent folder with TODOS.md** (Ben Tossell): Ben Tossell keeps a personal agent folder with general instructions, memory and a running TODOS.md file to manage daily tasks. ([Ben's Bites, 2026-04-30](https://www.bensbites.com/p/building-gets-easier))
- **Digital chief of staff** (swyx, Alessio Fanelli): A personal agent handles administration, summarizing, news search and task management. ([Latent Space, 2026-09-05](https://latent.space/p/grok-bot/))
- **Dots for dropped balls**: The Dots agent is used to avoid dropping important balls and to flag high-priority items. ([Don't Worry About the Vase, 2026-10-08](https://thezvi.substack.com/p/ai-189-new-math))
- **Claude Cowork**: Claude Cowork brings Claude Code-style efficiency to non-technical knowledge work tasks. ([AINews (smol.ai), 2026-01-12](https://news.smol.ai/issues/26-01-12-gemini-apple/))
- **Shared skills for colleagues** (Kyle Daigle): Teams share CLI-based skills with non-technical staff so they can work without learning new tools. ([Latent Space, 2026-06-02](https://latent.space/p/github/))

## Pressure-test your thinking

*Ask AI to disagree with you before you commit to an idea.*

**42** findings on AI thinking partners that push back

- **Argue-back instruction** (Kaj Sotala): A custom instruction makes Claude argue against your position with steelmanned counterarguments instead of agreeing first. ([Don't Worry About the Vase, 2026-04-08](https://thezvi.substack.com/p/ai-163-mythos-quest))
- **AI as sparring partner** (Alberto Romero): Have the model argue against your ideas before you commit to them, as practice for critical thinking. ([The Algorithmic Bridge, 2026-03-23](https://www.thealgorithmicbridge.com/p/the-one-thing-i-use-ai-for-that-actually))
- **Ask for the other side** (jimcollinswort1): Ask the LLM for opposing viewpoints, historical analysis and sources to strengthen your thinking. ([Hacker News — Ask HN, 2026-03-19](https://news.ycombinator.com/item?id=47433702))
- **Three versions of an idea** (Ben Tossell): Generate three versions of an idea with your agent to feel out which direction works best. ([Ben's Bites, 2026-09-08](https://www.bensbites.com/p/the-first-gpt-6-model))

## Tools for building with AI

*Claude Code and Codex lead, with local models, routers, worktrees and sandboxes around them.*

**1430** mentions of Claude in tool findings

- **Claude Code and Codex** (Colossus): Coding agents like Claude Code and Codex are used to quickly turn passing ideas into working tools. ([Ben's Bites, 2026-10-29](https://www.bensbites.com/p/ai-is-overwhelming-and-im-doing-it))
- **Ollama with local models** (Sebastian Raschka): Qwen3.6 35B-A3B running locally through Ollama with Qwen Code is described as a practical local coding agent setup. ([Ahead of AI, 2026-06-27](https://magazine.sebastianraschka.com/p/using-local-coding-agents))
- **OpenCode and OpenRouter** (DarthCeltic85): Builders use these to route work across models and vendors by cost and strength, using per-project instruction files. ([Hacker News — Ask HN, 2026-03-29](https://news.ycombinator.com/item?id=47559293))
- **Git worktrees** (cdnsteve): Git worktrees keep parallel agents on the same project from overwriting each other's code. ([Hacker News — Ask HN, 2026-04-16](https://news.ycombinator.com/item?id=47797632))
- **Phone control**: Claude Code Remote Control lets you drive an agent running on a home machine or cloud server from your phone. ([AINews (smol.ai), 2026-07-29](https://news.smol.ai/issues/26-07-29-not-much/))
- **Sandbox runtimes** (Tomasz Tunguz): Sandboxes isolate agent-written code. Cloudflare hosts agent sandboxes for 62% of teams writing code with agents. ([Tomasz Tunguz, 2026-10-13](https://tomtunguz.com/ai-in-practice-survey-2026/))

## Techniques that make builds work

*Plan first, verify everything, keep instructions lean and spend expensive models only where they matter.*

**153** findings on routing tasks across models

- **1. Plan before code** (defatigable): Have the agent analyze the codebase and propose a plan from your spec, iterate on the plan, then implement and review each step. ([Hacker News — Ask HN, 2026-01-20](https://news.ycombinator.com/item?id=46691243))
- **2. Let the agent interview you** (Thariq Shihipar): Use ask-user-question style prompts so the agent pulls out requirements and unknowns before it starts implementing in Claude Code. ([Latent Space, 2026-09-29](https://latent.space/p/thariq/))
- **3. Write failing tests first** (Andrej Karpathy): Writing failing tests and then having agents make them pass guides the agent and lets it verify its own work. ([Ben's Bites, 2026-01-27](https://www.bensbites.com/p/skills-are-taking-over)) ([Hacker News — Ask HN, 2026-08-08](https://news.ycombinator.com/item?id=49227024))
- **4. Make agents run their code** (Simon Willison): Have coding agents manually exercise their own code to catch issues that automated tests miss. ([Bluesky, 2026-03-06](https://bsky.app/profile/simonwillison.net/post/3mgfrg4gtxc2n))
- **5. Keep instruction files lean** (Sebastian Raschka): Developers prune or regenerate AGENTS.md and SKILL.md files, because old hand-holding can make newer models produce worse solutions. ([Ahead of AI, 2026-09-09](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and))
- **6. Route by cost and strength** (DarthCeltic85): Use cheaper models for simple work and stronger ones for hard work, directed by per-project instruction files. ([Hacker News — Ask HN, 2026-03-29](https://news.ycombinator.com/item?id=47559293))
- **7. Planner plus cheaper workers** (Ethan Mollick): Use a smart frontier model as planner that delegates subtasks to cheaper models as needed. ([Bluesky, 2026-07-04](https://bsky.app/profile/emollick.bsky.social/post/3mps4xss2uc2t))
- **8. Isolate parallel agents** (Boris Cherny): Run multiple coding agents on separate git branches to multiply pull request throughput. ([Tomasz Tunguz, 2026-03-10](https://tomtunguz.com/communication-tax-small-orgs/))

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

