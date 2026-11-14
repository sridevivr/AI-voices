# Tools & techniques people actually used in 2026

*From 9,610 "tool or technique" and "workaround" findings: things people said they use, recommend, or hack together, not launch announcements. Grouped by job. Links go to the finding behind each example. Companion reports: [`state_of_ai_2026.md`](state_of_ai_2026.md) and [`trends.md`](trends.md).*

## Most-mentioned tools

Counted in tool, technique and workaround findings only. These 19 sources lean towards builders and towards Claude (Simon Willison, Zvi, Latent Space), so read this as "what this crowd recommends", not market share.

| Tool | Mentions | What it is |
|---|---|---|
| Claude (any) | 1,275 | Anthropic's models and apps |
| Claude Code | 677 | AI coding agent: the most-recommended tool in the dataset |
| Codex | 336 | OpenAI's coding agent, often used alongside Claude Code |
| MCP | 252 | The standard for connecting AI to your apps and data |
| Gemini | 234 | Google's models |
| Cursor | 164 | AI code editor (discussed less over the year) |
| Qwen · Kimi · GLM · DeepSeek | 110–161 each | Chinese open models, used for cost and privacy |
| ChatGPT | 124 | Mentioned less as a tool than in news |
| Ollama · LM Studio | 86 · 45 | Run AI models on your own computer |
| OpenRouter | 73 | One account to use many AI models |
| AGENTS.md / CLAUDE.md | 51 each | Instruction files that teach agents your rules |
| Claude Cowork | 41 | Claude agent for non-coding knowledge work |
| Perplexity | 40 | AI search |
| Claude Artifacts | 29 | Small apps made inside a Claude chat |

---

## Part 1: Everyday and business use

### Writing that still sounds like you
The loudest complaint of the year was that AI writing sounds generic. What people do about it:
- **Use AI as a critic, never a rewriter:** "offer critique but never rewrite", so you make every fix yourself [[cite:Using AI only as a critic of drafts]].
- **Build a living style guide:** Tomasz Tunguz runs a nightly job that updates his style guidelines from the edits he makes to AI drafts [[cite:Nightly system that updates personal style guidelines]].
- **Force a readable format:** Ben Tossell's custom instructions force plain technical English in a skimmable layout [[cite:custom instructions to force AI output into ASD-STE100]].
- **Team rule:** spend more time writing a doc than readers will spend reading it (Clay's AI writing policy) [[cite:Clay's AI writing policy]], and "stand behind every idea and sentence" you share [[cite:Sophie Alpert's internal policy requires engineers]].

### A thinking partner that pushes back
Chatbots tend to agree with you. The workarounds:
- **Persona debate:** ask the AI to play several experts who argue it out, then form your own view [[cite:play several expert personas that debate]].
- **Cross-examine two models:** ask Claude and ChatGPT the same question and use their disagreements [[cite:Comparing answers from Claude and ChatGPT on the same problem]].
- **Steelman against yourself** before committing to an idea [[cite:argue against one's own ideas]].

### Your own knowledge base
- **Plain markdown files plus Obsidian** as a personal wiki that AI can read. People export things like iMessage history into searchable notes [[cite:Exporting iMessage history into searchable Markdown]].
- **Connect your own archive to Claude via MCP:** Simon Willison lets Claude search his past blog posts [[cite:Simon Willison uses a datasette-mcp plugin]].
- **Local file search that understands content** (DigUp) [[cite:DigUp is a fully local search tool]].

### Docs, decks and spreadsheets
- **Gamma** cut deck-building "from a half-day job to about ten minutes" [[cite:Gamma reduced presentation building]].
- **Claude** creates and edits Word, Excel and PowerPoint files while keeping their formatting [[cite:generate formatted Word, Excel, and PowerPoint files directly]], and analysed a 12-tab spreadsheet accurately [[cite:Analyzed a 12-tab spreadsheet]].
- **Ask for HTML, diagrams or explainers instead of walls of text** when you need to understand AI output (Karpathy's tip) [[cite:ask LLMs for HTML output, diagrams]].
- **Known gap:** no AI tool properly edits Google Docs, especially adding comments [[cite:no AI they tried can properly edit Google Docs]].

### Agents for knowledge work
- **Claude Cowork** is now on mobile and web as a background agent "teammate" [[cite:Claude Cowork extended to mobile and web]].
- Teams use agents for repetitive reasoning work: contract redlines, marketing retrospectives, data questions [[cite:Agent-based automation of repetitive reasoning tasks]].
- **Interactive mini-sites** are replacing some decks and spreadsheets as work products [[cite:Interactive websites (Sites) are being used]].

### Keeping up without drowning
- **An RSS reader** (NetNewsWire is a favourite) instead of algorithmic feeds [[cite:NetNewsWire, an open-source RSS reader]].
- **Merge your follow lists into one curated list** [[cite:port and combine follow lists]].
- Most people still stitch Hacker News, Google News, LinkedIn and niche outlets together by hand, which is the gap behind "Signal Brief" in `vibe_ideas.md` [[cite:combine Hacker News, Google News, Bing, LinkedIn]].

### Voice, video, design and music
- **Voice:** ElevenLabs for polished voice and ad localisation [[cite:ElevenLabs Ads Engine localises ads]]; Qwen3-TTS to clone your own voice locally, for example for an audiobook [[cite:Qwen3 TTS's voice clone feature]].
- **Video:** edit talks and launch videos with Claude plus ffmpeg and Remotion (transcribe, crop, add slides and animation) [[cite:edit launch and talk videos by transcribing]]; Kino for agent-driven editing [[cite:Kino is a tool for editing video with agents]].
- **Design:** generate mockups with an image model, then have the agent build them [[cite:create UI mockups with gpt-image-2]]; Claude Design for visual work [[cite:Opus 4.7 has strong visual design taste]].
- **Music:** Suno can turn a rough voice memo into a full production in another genre [[cite:Suno's version 4.5 can transform an existing recording]].

### Sales and go-to-market
- **Lightfield:** a CRM where you describe workflows in plain English [[cite:Lightfield is an AI-native CRM]].
- **A full inbound sales function run by one agent** for about $1,000 a year (Tunguz's template) [[cite:Running a full inbound sales function on an agent]].
- **Time outreach to buying signals** such as job changes or LinkedIn updates [[cite:Sales buying-signal detection]].

---

## Part 2: Building with AI (your vibe-coding toolkit)

### What non-coders are building with
**Claude Code** (desktop or terminal), **Claude Cowork**, **Lovable**, **Replit Agent** and **Claude Artifacts** are the tools named in the non-coders theme (69 findings, 15 sources). Typical builds are small tools the person needs themselves:
- A Chrome extension that lets you drag time slots on Google Calendar, because the native interface couldn't [[cite:Building a custom Chrome extension via an agent to drag time slots]].
- A personal cashflow forecaster built from bank CSV exports [[cite:Personal cashflow graph tool built with AI]].
- Native desktop apps for small personal tools, now cheap enough to be worth building [[cite:Building native GUI apps for small personal tools]].

### Techniques that make builds work
1. **Get interviewed before building.** Have the agent ask clarifying questions before it writes code (a "/grill-me" command, or plan mode) [[cite:a /grill-me command]]. Thariq Shihipar (Anthropic) uses question-style elicitation to pull out requirements first [[cite:ask-user-question style elicitation]].
2. **Keep the instruction file short and real.** CLAUDE.md or AGENTS.md should hold your rules and the mistakes to avoid. Claude Code now also reads AGENTS.md, so one file works across tools [[cite:Claude Code now reads AGENTS.md when no CLAUDE.md is present]]. Expect to rewrite it as models change [[cite:Maintaining a Claude.md file of failure modes]].
3. **Use handoff notes instead of long sessions.** Keep small index files any agent can read, and start fresh sessions rather than resuming old ones [[cite:chat-index.md and folder-map.md]]. Some people sync agent memory to a Google Doc to keep it visible [[cite:Syncing every agent memory to a Google Doc]].
4. **Make checks automatic, not polite requests.** Put rules into tests and pre-commit hooks rather than prose instructions [[cite:Enforce machine-checkable agent rules through pre-commit hooks]].
5. **Let the agent see what it built.** Screenshots and in-terminal video for visual QA [[cite:renders screenshots and inline videos in the terminal]]; design kits so the result doesn't look AI-generated [[cite:Hallmark is a rebuilt design skill]]; sketch the app idea visually before building [[cite:Design and visualization tools are used to flesh out an app idea]].
6. **Have a second model review the first.** Claude and Codex reviewing each other is common, and GitHub Copilot now mixes models automatically [[cite:GitHub Copilot Fusion orchestrates Anthropic and OpenAI models]].
7. **Watch costs from day one.** OpenRouter gives one account for many models [[cite:OpenRouter is recommended as a multi-provider model gateway]]. A better harness, meaning the setup around the model, can cut the cost of the same task by 71% [[cite:Harness software around the model can cut the cost]].
8. **Protect your machine.** Run agents in a sandbox or container [[cite:Sandboxing coding agent projects is recommended as a defense]]. Small Claude Code "mods" can block risky commands and blur secrets [[cite:Claude Code mods are small plugins that block risky commands]].
9. **Later: run several agents in parallel.** Power users run many agents at once, with a dashboard to coordinate (Ben Tossell built his own) [[cite:Ben Tossell built a visual all-in-one dashboard]]. It's worth it once single-agent builds feel routine.

### Patterns worth copying for your own posts
- **Build the tool you needed this week**, then post the before and after. That's the dominant pattern in the non-coder theme.
- **Show the workflow, not just the product.** "How I got the agent to interview me first" is as shareable as the app itself.
- **Be honest about failures.** Readers trust posts that show where the agent got it wrong, and verification is the year's top concern.
