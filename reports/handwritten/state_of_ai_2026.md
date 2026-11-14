# State of AI 2026: what a year of AI commentary says

*Based on 26,923 findings extracted from 2,230 articles, newsletters and Hacker News threads by 19 sources, 11 Nov 2025 to 10 Nov 2026. Counts are computed from the data. The interpretation is mine (Claude), and the links go to the source behind each example. Companion reports: [`trends.md`](trends.md) (what rose and fell) and [`tools_guide.md`](tools_guide.md) (what people actually use).*

## The year in six lines

1. **The conversation moved from "which AI tool should I use" to "how do I trust what AI does".** Safety and governance nearly doubled as a share of the commentary (6.8% to 12.8%), security talk rose about 2.5×, and agent monitoring and cost tracking grew. Talk about coding tools, AI hardware and retrieval (RAG) shrank.
2. **Agents became the default topic.** Words like "agent" or "agentic" appear in about 27% of findings by late 2026, up from 18%. The problems people describe are now about running agents: memory, permissions, cost and supervising several at once.
3. **"Hallucination" nearly disappeared as a complaint**, from 13 to 5 mentions per 1,000 findings. The frustrations that replaced it are quieter: AI writing that sounds generic, chatbots that flatter you, and colleagues sending you padded AI text.
4. **The arguing got louder.** Debate findings rose from 7% to 9% of the total (overall; the big sources don't all agree on this), and workarounds, people hacking around tools that fall short, rose consistently. Regulation, the AI bubble, AGI timelines and whether AI models have any moat dominated.
5. **Open and local models went from hobby to strategy.** Mentions of open-weight and local models roughly doubled (three of the six biggest sources show the rise on their own, none show a fall), driven by Chinese labs (Qwen, Kimi, DeepSeek, GLM) and by people wanting control over cost and data.
6. **Non-coders building their own tools is a real and growing story.** "Non-coders using coding agents for personal tools" is one of the most multi-source themes in the dataset (69 findings from 15 sources), and it's your story.

## What people argued about

These are the themes with the most "debate" findings, meaning places where informed people publicly disagreed. Each one is a ready-made topic for a post that takes a side.

**1. Who should regulate AI, and how much?** (70 debate findings, 12 sources)
The fight shifted from "should we regulate?" to "who gets to?". Federal preemption of state laws versus letting states act ([Don't Worry About the Vase, 2025-11-20](https://thezvi.substack.com/p/ai-143-everything-everywhere-all)); whether government should vet frontier models before release (prior restraint) ([Don't Worry About the Vase, 2026-05-07](https://thezvi.substack.com/p/ai-167-the-prior-restraint-era-begins)); and whether a voluntary 30-day review is reasonable or a licensing regime in disguise ([Don't Worry About the Vase, 2026-06-03](https://thezvi.substack.com/p/trump-signs-executive-order-for-ai)). Main voices: Zvi Mowshowitz, Dean W. Ball, Gary Marcus, Nathan Calvin.

**2. Is AI conscious, and should we pause?** (60)
Mustafa Suleyman warned that AI which merely *seems* conscious can manipulate human empathy ([Exponential View, 2026-02-05](https://www.exponentialview.co/p/mustafa-suleyman-ai-is-hacking-our)). Gary Marcus and others questioned whether a model's self-reports of feelings mean anything ([Marcus on AI, 2026-03-12](https://garymarcus.substack.com/p/is-the-us-military-actually-afraid)). Separately, people disputed whether labs should pause or keep racing when competitors won't stop ([Don't Worry About the Vase, 2026-04-01](https://thezvi.substack.com/p/anthropic-responsible-scaling-policy)).

**3. Is AI a bubble?** (49)
Skeptics point to spending levels, circular deals and leverage. Others argue the customers' cash flows justify the build-out ([Don't Worry About the Vase, 2025-11-27](https://thezvi.substack.com/p/ai-144-thanks-for-the-models)) ([Tomasz Tunguz, 2025-12-03](https://tomtunguz.com/top-10-posts-2025/)). Tomasz Tunguz is the best data-driven voice here.

**4. How close is AGI?** (49)
Gary Marcus calls 2027 timelines marketing ([Marcus on AI, 2025-11-21](https://garymarcus.substack.com/p/breaking-the-ai-2027-doomsday-scenario)). Terence Tao argues today's AI is "clever, not intelligent" ([AINews (smol.ai), 2025-12-16](https://news.smol.ai/issues/25-12-16-gpt-image-15/)). Researchers disagree on whether AI doing AI research means a sudden jump or a smooth curve ([Latent Space, 2026-02-27](https://latent.space/p/metr/)).

**5. Does anyone have a moat?** (35)
Top models now perform similarly, so the argument is whether winners come from sticky integrations and distribution ([Tomasz Tunguz, 2025-11-21](https://tomtunguz.com/the-bacon-and-the-skillet-when-ai-market-share-congeals/)), whether "wrapper" startups survive as general models absorb them ([Latent Space, 2026-03-17](https://latent.space/p/felix-anthropic/)), and whether an app built quickly with AI has any moat at all ([Hacker News — Ask HN, 2026-01-29](https://news.ycombinator.com/item?id=46807308)). This one matters directly for anyone vibe-coding products.

**6. Is vibe coding real productivity?** (30)
Skeptics say AI writes toy code. Experienced programmers increasingly say it now writes most of their output ([Simon Willison's Weblog, 2026-01-08](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/)). Others report only 10–20% gains ([Hacker News — Ask HN, 2026-01-09](https://news.ycombinator.com/item?id=46548947)), and Alberto Romero asks how much of "AI-written" work is really hidden human judgment ([The Algorithmic Bridge, 2026-01-13](https://www.thealgorithmicbridge.com/p/claude-code-coded-claude-cowork)).

**7. Are Chinese open models winning?** (29)
Whether China now leads open-weight AI ([AINews (smol.ai), 2026-03-24](https://news.smol.ai/issues/26-03-24-not-much/)), and whether open models can keep pace with closed frontier labs at all ([Interconnects, 2026-04-15](https://www.interconnects.ai/p/my-bets-on-open-models-mid-2026)). Nathan Lambert (Interconnects) is the go-to voice.

**8. Copyright and "license washing."** (26)
Can an AI rewrite of open-source code shed its license? The chardet relicensing fight became the test case ([Simon Willison's Weblog, 2026-03-05](https://simonwillison.net/2026/Mar/5/chardet/)). There was also pushback on AI labs complaining about others copying them ([Marcus on AI, 2026-02-13](https://garymarcus.substack.com/p/irony-irony-laced-with-karma-and)).

**Also contested:** military use of AI, after Anthropic refused a Pentagon request ([Ben's Bites, 2026-02-26](https://www.bensbites.com/p/claude-has-some-conflicts)); whether benchmarks mean anything anymore ([Interconnects, 2026-06-22](https://www.interconnects.ai/p/glm-52-is-the-step-change-for-open)); and whether AI prices are about to rise ([Simon Willison's Weblog, 2026-05-19](https://simonwillison.net/2026/May/19/gemini-35-flash/)).

## What people struggled with

Pain points are the largest category: 10,181 findings, 38% of everything.

**Builders and developers** (detail in `opportunities.md`):
- Agents doing damage: deleting files, leaking secrets, running unsupervised. Sandboxing and permissions are the most-requested fix.
- Cost and quotas: unpredictable token spend, subscription limits that change without notice, silent model swaps.
- Verification: AI writes code faster than people can review it.
- Memory: agents forget everything between sessions, and people hand-maintain notes files to compensate.

**Everyday users and knowledge workers** (detail in `vibe_ideas.md`):
- **AI writing sounds generic** (83 findings): people rewrite AI drafts to get their voice back.
- **Chatbots flatter instead of challenge** (85 findings on tone and sycophancy): people build "devil's advocate" prompts and cross-check models.
- **AI slop in feeds and forums** (72 findings, 16 explicit requests for filters).
- **Colleagues sending AI-padded messages** (45 findings): long, polished, and empty.
- **Subscriptions are opaque** (91 findings): hidden caps, plan changes and model swaps.
- **Keeping up is exhausting** (56 findings): too much news, too much hype.
- **Organizations can't find use cases or show ROI** (42 + 31 findings): this is where a program manager's skills are scarce and valuable.

## What people actually used

The short version (full guide in [`tools_guide.md`](tools_guide.md)):
- **Claude Code** is by far the most-recommended tool in the dataset: 677 mentions in "tool or technique" findings, against Codex at 336 and Cursor at 164. Part of that lead reflects sources that write mostly about Claude (Simon Willison, Zvi, Latent Space), but the gap is large.
- **Agent "skills" and instruction files (AGENTS.md / CLAUDE.md)** became the standard way to teach AI your preferences, rising from almost nothing in late 2025.
- **Cross-checking models** (Claude plus Codex or ChatGPT reviewing each other) is a common habit for both code and thinking.
- **Open models through OpenRouter or Ollama** (Qwen, Kimi, GLM, DeepSeek) for cost and privacy.
- **For non-coders:** Claude Cowork, Lovable, Replit and Claude Artifacts for building personal tools; Gamma for decks; Claude for Excel and Office files.

## Who drives the conversation

Ranked by findings attributed to them. Counts partly reflect how much each of our 19 sources publishes, and Zvi quotes many of the others.

| Person | Findings | Known for | Why follow, for you |
|---|---|---|---|
| Simon Willison | 1,552 | Hands-on experiments with every new model and tool; coined "prompt injection" | The most reliable "what actually works" voice; great to quote and reply to |
| Zvi Mowshowitz | 922 | Huge weekly roundups; safety and policy | Where the debates surface first |
| Tomasz Tunguz | 833 | Data on AI business, pricing and spend | Business and MBA angles, with charts |
| Ben Tossell (Ben's Bites) | 713 | Building with agents as a non-traditional builder | **Closest to your path**: an operator who builds with AI and shares it |
| Gary Marcus | 529 | The leading skeptic | Useful counterpoint for balanced posts |
| Nathan Lambert | 442 | Open models and training (Interconnects) | The open versus closed and China debates |
| Alberto Romero | 298 | AI and writing, culture | The "AI makes everything sound the same" conversation |
| Ethan Mollick | 185 | AI at work and in organizations (Wharton) | **Your LinkedIn audience's favourite**: AI adoption at work |
| swyx & Alessio Fanelli | 280 | Latent Space: AI engineering interviews | Where builder trends start |
| Sayash Kapoor & Arvind Narayanan | 144 | "AI as Normal Technology": evidence over hype | Measured, research-backed takes |
| Hamel Husain | 94 | Evals: how to measure whether AI works | The practical "how do we know it's good" voice |
| Dean W. Ball | 47 | AI policy | The policy side of the regulation debate |

## What this means for you

You want to build things with AI and talk about it on LinkedIn and X. This year's data points to five angles where demand is real and your background is an advantage:

1. **"I'm not a developer, and I built this."** Non-coders building their own tools is a growing, multi-source story (69 findings from 15 sources), and builders with a business background are rare in that conversation. Document the builds honestly, including where AI failed.
2. **Trust is the theme of the year.** Every app you build can carry a trust feature: shows its sources, asks before acting, critiques instead of rewriting. That's both what people want and a strong post angle.
3. **The workplace side is under-served.** Most commentary is by and for engineers. Use-case discovery, ROI, AI-padded communication and meeting follow-through are pain points with few builders and a program manager's natural vocabulary.
4. **Take sides in the debates.** "Is vibe coding real productivity?" and "does anything built with AI have a moat?" are live questions you can answer from experience.
5. **Write like a human.** Generic AI prose is the loudest everyday complaint in the data. Posts that sound like you will stand out, and the tools that help with that (see `vibe_ideas.md` #1) are a product opportunity too.

## How this was made, and its limits

- **Pipeline:** articles were fetched politely from 19 sources. Claude Haiku 5.5 extracted structured findings (type, summary, verbatim quote of under 25 words, who, domain); 98% of the quotes were verified word-for-word against the source text. Claude Sonnet 5.5 then grouped them into 907 themes. Total API cost was about $10.62.
- **Coverage bias:** these 19 sources skew towards builders, AI insiders and the safety community. Mainstream business press, non-English sources, TikTok and YouTube are not included. Paid Substack posts were skipped.
- **Counts are attention, not truth.** A theme with many findings is one people wrote about a lot, not necessarily one most people experience.
- **The source mix changed over the year:** AINews fell from 45% to 24% of findings. Trend claims therefore require agreement within most of the six biggest sources (see `trends.md`).
