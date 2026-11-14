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
- **Use AI as a critic, never a rewriter:** "offer critique but never rewrite", so you make every fix yourself ([Hacker News — Ask HN, 2026-05-22](https://news.ycombinator.com/item?id=48235223)).
- **Build a living style guide:** Tomasz Tunguz runs a nightly job that updates his style guidelines from the edits he makes to AI drafts ([Tomasz Tunguz, 2026-09-02](https://tomtunguz.com/ai-productivity-doesnt-mean-what-i-thought/)).
- **Force a readable format:** Ben Tossell's custom instructions force plain technical English in a skimmable layout ([Ben's Bites, 2026-08-11](https://www.bensbites.com/p/make-it-readable)).
- **Team rule:** spend more time writing a doc than readers will spend reading it (Clay's AI writing policy) ([Ben's Bites, 2026-09-29](https://www.bensbites.com/p/sonnet-55-is-worth-a-try)), and "stand behind every idea and sentence" you share ([Simon Willison's Weblog, 2026-08-11](https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/)).

### A thinking partner that pushes back
Chatbots tend to agree with you. The workarounds:
- **Persona debate:** ask the AI to play several experts who argue it out, then form your own view ([Don't Worry About the Vase, 2026-05-28](https://thezvi.substack.com/p/ai-170-lack-of-executive-order)).
- **Cross-examine two models:** ask Claude and ChatGPT the same question and use their disagreements ([Hacker News — Ask HN, 2026-06-05](https://news.ycombinator.com/item?id=48413629)).
- **Steelman against yourself** before committing to an idea ([The Algorithmic Bridge, 2026-03-23](https://www.thealgorithmicbridge.com/p/the-one-thing-i-use-ai-for-that-actually)).

### Your own knowledge base
- **Plain markdown files plus Obsidian** as a personal wiki that AI can read. People export things like iMessage history into searchable notes ([Don't Worry About the Vase, 2026-08-27](https://thezvi.substack.com/p/ai-183-pre-post-mortem)).
- **Connect your own archive to Claude via MCP:** Simon Willison lets Claude search his past blog posts ([Simon Willison's Weblog, 2026-10-22](https://simonwillison.net/2026/Oct/22/donating-agent-skills/)).
- **Local file search that understands content** (DigUp) ([Ben's Bites, 2026-10-15](https://www.bensbites.com/p/prompt-tips-from-anthropic)).

### Docs, decks and spreadsheets
- **Gamma** cut deck-building "from a half-day job to about ten minutes" ([Hacker News — Ask HN, 2026-04-05](https://news.ycombinator.com/item?id=47651140)).
- **Claude** creates and edits Word, Excel and PowerPoint files while keeping their formatting ([AINews (smol.ai), 2026-04-20](https://news.smol.ai/issues/26-04-20-not-much/)), and analysed a 12-tab spreadsheet accurately ([Don't Worry About the Vase, 2026-03-11](https://thezvi.substack.com/p/gpt-54-is-a-substantial-upgrade)).
- **Ask for HTML, diagrams or explainers instead of walls of text** when you need to understand AI output (Karpathy's tip) ([Ben's Bites, 2026-10-06](https://www.bensbites.com/p/thoughts-from-san-francisco)).
- **Known gap:** no AI tool properly edits Google Docs, especially adding comments ([Don't Worry About the Vase, 2026-07-16](https://thezvi.substack.com/p/ai-177-part-1-tip-of-the-iceberg)).

### Agents for knowledge work
- **Claude Cowork** is now on mobile and web as a background agent "teammate" ([AINews (smol.ai), 2026-07-07](https://news.smol.ai/issues/26-07-07-not-much/)).
- Teams use agents for repetitive reasoning work: contract redlines, marketing retrospectives, data questions ([Latent Space, 2026-07-03](https://latent.space/p/vercel-agents-new-software/)).
- **Interactive mini-sites** are replacing some decks and spreadsheets as work products ([Latent Space, 2026-07-28](https://latent.space/p/chatgpt-work/)).

### Keeping up without drowning
- **An RSS reader** (NetNewsWire is a favourite) instead of algorithmic feeds ([Simon Willison's Weblog, 2026-06-17](https://simonwillison.net/2026/Jun/17/netnewswire-status/)).
- **Merge your follow lists into one curated list** ([Don't Worry About the Vase, 2026-07-14](https://thezvi.substack.com/p/twitter-thoughts-for-you)).
- Most people still stitch Hacker News, Google News, LinkedIn and niche outlets together by hand, which is the gap behind "Signal Brief" in `vibe_ideas.md` ([Hacker News — Ask HN, 2026-09-02](https://news.ycombinator.com/item?id=49535272)).

### Voice, video, design and music
- **Voice:** ElevenLabs for polished voice and ad localisation ([Ben's Bites, 2026-06-23](https://www.bensbites.com/p/record-a-skill)); Qwen3-TTS to clone your own voice locally, for example for an audiobook ([Hacker News — Ask HN, 2026-10-05](https://news.ycombinator.com/item?id=49972125)).
- **Video:** edit talks and launch videos with Claude plus ffmpeg and Remotion (transcribe, crop, add slides and animation) ([Simon Willison's Weblog, 2026-07-21](https://simonwillison.net/2026/Jul/21/cat-and-thariq/)); Kino for agent-driven editing ([Ben's Bites, 2026-11-03](https://www.bensbites.com/p/if-you-feel-behind-right-now-dont)).
- **Design:** generate mockups with an image model, then have the agent build them ([Don't Worry About the Vase, 2026-04-28](https://thezvi.substack.com/p/gpt-55-capabilities-and-reactions)); Claude Design for visual work ([Simon Willison's Weblog, 2026-05-06](https://simonwillison.net/2026/May/6/code-w-claude-2026/)).
- **Music:** Suno can turn a rough voice memo into a full production in another genre ([Understanding AI, 2026-10-19](https://www.understandingai.org/p/ai-is-ushering-in-an-age-personal)).

### Sales and go-to-market
- **Lightfield:** a CRM where you describe workflows in plain English ([Ben's Bites, 2026-05-05](https://www.bensbites.com/p/codex-is-gaining-steam)).
- **A full inbound sales function run by one agent** for about $1,000 a year (Tunguz's template) ([Tomasz Tunguz, 2026-10-06](https://tomtunguz.com/how-to-automate-inbound/)).
- **Time outreach to buying signals** such as job changes or LinkedIn updates ([Latent Space, 2026-11-08](https://latent.space/p/cs146s/)).

---

## Part 2: Building with AI (your vibe-coding toolkit)

### What non-coders are building with
**Claude Code** (desktop or terminal), **Claude Cowork**, **Lovable**, **Replit Agent** and **Claude Artifacts** are the tools named in the non-coders theme (69 findings, 15 sources). Typical builds are small tools the person needs themselves:
- A Chrome extension that lets you drag time slots on Google Calendar, because the native interface couldn't ([Ben's Bites, 2026-08-07](https://www.bensbites.com/p/bens-session)).
- A personal cashflow forecaster built from bank CSV exports ([Hacker News — Ask HN, 2026-10-20](https://news.ycombinator.com/item?id=50159886)).
- Native desktop apps for small personal tools, now cheap enough to be worth building ([Simon Willison's Weblog, 2026-08-21](https://simonwillison.net/2026/Aug/21/stop-making-tuis/)).

### Techniques that make builds work
1. **Get interviewed before building.** Have the agent ask clarifying questions before it writes code (a "/grill-me" command, or plan mode) ([Hacker News — Ask HN, 2026-10-19](https://news.ycombinator.com/item?id=50151036)). Thariq Shihipar (Anthropic) uses question-style elicitation to pull out requirements first ([Latent Space, 2026-09-29](https://latent.space/p/thariq/)).
2. **Keep the instruction file short and real.** CLAUDE.md or AGENTS.md should hold your rules and the mistakes to avoid. Claude Code now also reads AGENTS.md, so one file works across tools ([AINews (smol.ai), 2026-09-19](https://latent.space/p/ainews-here-are-6-clones-of-jev-in/)). Expect to rewrite it as models change ([Latent Space, 2026-09-29](https://latent.space/p/thariq/)).
3. **Use handoff notes instead of long sessions.** Keep small index files any agent can read, and start fresh sessions rather than resuming old ones ([Ben's Bites, 2026-10-15](https://www.bensbites.com/p/prompt-tips-from-anthropic)). Some people sync agent memory to a Google Doc to keep it visible ([Ben's Bites, 2026-10-06](https://www.bensbites.com/p/thoughts-from-san-francisco)).
4. **Make checks automatic, not polite requests.** Put rules into tests and pre-commit hooks rather than prose instructions ([AINews (smol.ai), 2026-11-10](https://latent.space/p/ainews-fable-5-2-retakes-world-1-llm-spot-as-ant-ipo-roadshow-begins/)).
5. **Let the agent see what it built.** Screenshots and in-terminal video for visual QA ([AINews (smol.ai), 2026-10-13](https://latent.space/p/ainews-meta-muse-wonder-and-wonder/)); design kits so the result doesn't look AI-generated ([Ben's Bites, 2026-10-27](https://www.bensbites.com/p/is-anthropic-the-best-business-in)); sketch the app idea visually before building ([Hacker News — Ask HN, 2026-11-02](https://news.ycombinator.com/item?id=50334078)).
6. **Have a second model review the first.** Claude and Codex reviewing each other is common, and GitHub Copilot now mixes models automatically ([AINews (smol.ai), 2026-10-29](https://latent.space/p/ainews-gemini-4-carbon/)).
7. **Watch costs from day one.** OpenRouter gives one account for many models ([Hacker News — Ask HN, 2026-11-01](https://news.ycombinator.com/item?id=50325635)). A better harness, meaning the setup around the model, can cut the cost of the same task by 71% ([Tomasz Tunguz, 2026-11-04](https://tomtunguz.com/watts-in-store-for-2027-inference/)).
8. **Protect your machine.** Run agents in a sandbox or container ([Hacker News — Ask HN, 2026-08-31](https://news.ycombinator.com/item?id=49506998)). Small Claude Code "mods" can block risky commands and blur secrets ([Ben's Bites, 2026-10-06](https://www.bensbites.com/p/thoughts-from-san-francisco)).
9. **Later: run several agents in parallel.** Power users run many agents at once, with a dashboard to coordinate (Ben Tossell built his own) ([Ben's Bites, 2026-10-20](https://www.bensbites.com/p/how-i-built-my-everything-app)). It's worth it once single-agent builds feel routine.

### Patterns worth copying for your own posts
- **Build the tool you needed this week**, then post the before and after. That's the dominant pattern in the non-coder theme.
- **Show the workflow, not just the product.** "How I got the agent to interview me first" is as shareable as the app itself.
- **Be honest about failures.** Readers trust posts that show where the agent got it wrong, and verification is the year's top concern.
