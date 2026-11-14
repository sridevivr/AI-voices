# The ten biggest AI debates of the year, and what each side actually argues

*From who pays when AI causes harm to whether the money behind it is a bubble, here are the arguments that drew the most commentary between November 2025 and November 2026, with the best case on each side and a post angle for each.*

*Period: 2025-11-11 to 2026-11-10 · 26,923 findings from 19 sources · generated 2026-11-14 by `python -m src.insights write`. Numbers and tables come from code; prose is Sonnet's; every link is a finding the text cites.*

## Key points

- The most-debated topic was not capability but accountability: who is liable, and whether rules should target models, compute or applications. No consensus emerged. ([Marcus on AI, 2026-09-17](https://garymarcus.substack.com/p/liability-regulation-and-ais-new)) ([Latent Space, 2026-09-17](https://latent.space/p/recursive/)) ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view))
- Safety arguments split inside the safety world. Disagreements covered whether control efforts help or backfire, whether loss-of-control incidents show a discontinuity or just negligence, and whether the safety and labor camps can ally. ([Don't Worry About the Vase, 2026-09-10](https://thezvi.substack.com/p/ai-185-preference-cascade)) ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view)) ([Understanding AI, 2026-04-06](https://www.understandingai.org/p/bernie-sanders-has-a-plan-to-stop))
- Bubble, commoditization and scaling debates are all versions of one question: does the spending and the valuation match what the technology can defend or deliver? The two sides often cite the same facts, such as cash-rich buyers or similar model performance, and reach opposite conclusions. ([Latent Space, 2026-04-03](https://latent.space/p/pmarca/)) ([Marcus on AI, 2026-02-05](https://garymarcus.substack.com/p/is-the-great-ai-meltdown-imminent)) ([Simon Willison's Weblog, 2026-03-06](https://simonwillison.net/2026/Mar/6/anthropic-and-the-pentagon/)) ([Marcus on AI, 2026-03-14](https://garymarcus.substack.com/p/breaking-expensive-new-evidence-that))
- Several debates are about definitions more than facts: what counts as vibe coding, as open source, as AGI, or as an AI that 'seems conscious'. Whoever sets the definition shapes the argument. ([Simon Willison's Weblog, 2026-04-23](https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/)) ([Interconnects, 2025-11-12](https://www.interconnects.ai/p/inside-a-chinese-frontier-lab-inclusion)) ([AINews (smol.ai), 2026-08-24](https://news.smol.ai/issues/26-08-27-not-much/)) ([Exponential View, 2026-02-05](https://www.exponentialview.co/p/mustafa-suleyman-ai-is-hacking-our))
- Gary Marcus, Zvi Mowshowitz, Nathan Lambert and Simon Willison show up repeatedly as anchors for opposing positions, so a few recurring voices frame much of the discussion. ([Marcus on AI, 2026-09-17](https://garymarcus.substack.com/p/liability-regulation-and-ais-new)) ([Don't Worry About the Vase, 2026-09-28](https://thezvi.substack.com/p/what-also-happened-notonlyhuggingface)) ([Interconnects, 2026-09-11](https://www.interconnects.ai/p/open-source-ai-reading-list)) ([Simon Willison's Weblog, 2026-04-23](https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/))
- The Anthropic-versus-government dispute made an abstract question concrete: can a vendor's contract limit how government uses AI? It was argued in contract and court terms. ([Don't Worry About the Vase, 2026-02-27](https://thezvi.substack.com/p/anthropic-and-the-dow-anthropic-responds)) ([Don't Worry About the Vase, 2026-03-27](https://thezvi.substack.com/p/anthropic-vs-dow-6-the-court-rules)) ([Don't Worry About the Vase, 2026-03-18](https://thezvi.substack.com/p/anthropic-vs-dow-5-motions-filed))

## 1. Who is responsible when AI causes harm, and what exactly should be regulated?

**The question:** If an AI system or agent does damage, who pays, and should rules aim at the model, the chips, or the way it is used? This was the most-debated topic of the year. ([Don't Worry About the Vase, 2026-09-28](https://thezvi.substack.com/p/what-also-happened-notonlyhuggingface)) ([Latent Space, 2026-09-17](https://latent.space/p/recursive/))

**One side, liability is enough:** Gary Marcus describes technolibertarians who say liability for AI harms can substitute for regulation. Marcus disagrees: liability alone is insufficient and new regulation is also needed. Richard Socher makes a related case on what to target. He says strict regulation of compute and GPU usage would be totalitarian and rules should aim at specific applications. ([Marcus on AI, 2026-09-17](https://garymarcus.substack.com/p/liability-regulation-and-ais-new)) ([Latent Space, 2026-09-17](https://latent.space/p/recursive/))

**Other side, more structure is needed:** Some favor regulating model flops. Sayash Kapoor and Arvind Narayanan note that experts disagree on whether to rely on the existing tort system, strict liability, or strengthened negligence law with oversight. Zvi Mowshowitz points to the unsettled question of whether developers or users should bear liability for agent harms, with proposals ranging from civil to criminal responsibility. ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view)) ([Don't Worry About the Vase, 2026-09-28](https://thezvi.substack.com/p/what-also-happened-notonlyhuggingface))

Smaller versions of the fight appeared elsewhere. A Hacker News thread asked whether an automated LLM system should be liable for following malicious instructions embedded in web content. Ben Thompson argued the US should legalize distillation through fair-use law, while labs prohibit it despite having trained on unlicensed data. ([Hacker News — Ask HN, 2026-08-31](https://news.ycombinator.com/item?id=49506998)) ([Simon Willison's Weblog, 2026-07-20](https://simonwillison.net/2026/Jul/20/afraid-of-chinese-models/))

**Why it matters:** Where liability lands decides who builds safeguards, from model makers to the businesses deploying agents. A professional deploying agents at work should know that this is unsettled. ([Don't Worry About the Vase, 2026-09-28](https://thezvi.substack.com/p/what-also-happened-notonlyhuggingface)) ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view))

**Post angle:** 'If your AI agent does something harmful, who is responsible: you, the vendor, or nobody? Experts still disagree.' ([Don't Worry About the Vase, 2026-09-28](https://thezvi.substack.com/p/what-also-happened-notonlyhuggingface))

## 2. Is AI an existential risk, and are safety efforts helping?

**The question:** Is superintelligence a threat to humanity, and do the current ways of managing it work? This was the second most-debated area. ([Don't Worry About the Vase, 2026-03-31](https://thezvi.substack.com/p/movie-review-the-ai-doc)) ([Don't Worry About the Vase, 2026-09-10](https://thezvi.substack.com/p/ai-185-preference-cascade))

**Worried side:** Zvi Mowshowitz summarizes the position that building superintelligence will kill everyone, noting that accelerationists rely mainly on the argument that past technology was good. Nick Bostrom's framing, as reported by Import AI, is whether to pause or slow superintelligence versus launch it sooner given its life-saving potential. ([Don't Worry About the Vase, 2026-03-31](https://thezvi.substack.com/p/movie-review-the-ai-doc)) ([Import AI, 2026-02-16](https://importai.substack.com/p/import-ai-445-timing-superintelligence))

**Disagreement inside safety:** Some argue AI control efforts raise existential risk by distracting from learning from failures and creating adversarial dynamics with AIs. Others say control is needed to limit dangerous escapes. Kapoor and Narayanan note that the safety and cybersecurity communities read recent loss-of-control incidents differently: one sees discontinuity, the other negligence. Richard Socher also questioned whether Anthropic-style constitutions actually align models. ([Don't Worry About the Vase, 2026-09-10](https://thezvi.substack.com/p/ai-185-preference-cascade)) ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view)) ([Latent Space, 2026-09-17](https://latent.space/p/recursive/))

**Consciousness and welfare:** Mustafa Suleyman argues that AI that seems conscious, even if it isn't, risks collective AI psychosis and manipulation of human empathy. Gary Marcus disputes whether an LLM's reports of its own internal states count as evidence. In October, Anthropic's policy against abusive treatment of Claude was read either as precautionary moral concern or as a data-quality measure. ([Exponential View, 2026-02-05](https://www.exponentialview.co/p/mustafa-suleyman-ai-is-hacking-our)) ([Marcus on AI, 2026-03-12](https://garymarcus.substack.com/p/is-the-us-military-actually-afraid)) ([AINews (smol.ai), 2026-10-10](https://latent.space/p/ainews-typesafejev-at-100m-arr-75b/))

**Politics:** Kai Williams noted that safety advocates focused on existential risk and left-leaning labor groups focused on job loss and hype disagree on the threat and on policy, which complicates a unified anti-AI coalition. ([Understanding AI, 2026-04-06](https://www.understandingai.org/p/bernie-sanders-has-a-plan-to-stop))

**Why it matters:** The same word, 'safety', covers very different priorities. Readers should be able to tell which camp a claim comes from. ([Understanding AI, 2026-04-06](https://www.understandingai.org/p/bernie-sanders-has-a-plan-to-stop)) ([Don't Worry About the Vase, 2026-09-10](https://thezvi.substack.com/p/ai-185-preference-cascade))

**Post angle:** 'The AI safety movement isn't one movement: doom researchers, labor groups and security people disagree on what the threat even is.' ([Understanding AI, 2026-04-06](https://www.understandingai.org/p/bernie-sanders-has-a-plan-to-stop)) ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view))

## 3. Is AI spending a bubble?

**The question:** Is the AI infrastructure buildout headed for a telecom-style crash, or is it a real buildout backed by real demand? ([Tomasz Tunguz, 2025-12-03](https://tomtunguz.com/top-10-posts-2025/)) ([Latent Space, 2026-04-03](https://latent.space/p/pmarca/))

**Bubble worriers:** Gary Marcus says circular financing, where a chipmaker funds a customer that buys its chips, is seen by some as a dotcom-style signal, and he argues the collapse risk is underrated. Others argue a bubble could trigger macro collapse via sunk compute costs, though some say the impact would be temporary. ([Marcus on AI, 2026-02-05](https://garymarcus.substack.com/p/is-the-great-ai-meltdown-imminent)) ([AINews (smol.ai), 2025-12-03](https://news.smol.ai/issues/25-12-03-not-much/))

**Boom defenders:** Marc Andreessen's side argues today's buyers are cash-rich incumbents and demand already exists. Tomasz Tunguz reports a similar argument that the cash flows of top customers justify the spend. Zvi Mowshowitz raised the point that revenue could rise if prices were higher and free tiers disappeared. ([Latent Space, 2026-04-03](https://latent.space/p/pmarca/)) ([Tomasz Tunguz, 2025-12-03](https://tomtunguz.com/top-10-posts-2025/)) ([Don't Worry About the Vase, 2026-04-23](https://thezvi.substack.com/p/ai-165-in-our-image))

**Third positions:** Hacker News commenters split over whether the bubble framing is extreme or median, and whether bubble dynamics can coexist with automation of software. Azeem Azhar left 'bubble or boom' as an open question for 2026. Salvatore Sanfilippo's camp argued that AI company finances are irrelevant to the long-run shift in programming. ([Hacker News — Ask HN, 2026-10-09](https://news.ycombinator.com/item?id=50020096)) ([Exponential View, 2026-01-16](https://www.exponentialview.co/p/the-new-moat-in-2026)) ([Simon Willison's Weblog, 2026-01-11](https://simonwillison.net/2026/Jan/11/dont-fall-into-the-anti-ai-hype/))

**Why it matters:** For anyone writing about AI, the debate shows a bubble and a lasting technology shift can both be true, and commentators are arguing about which question matters. ([Hacker News — Ask HN, 2026-10-09](https://news.ycombinator.com/item?id=50020096)) ([Simon Willison's Weblog, 2026-01-11](https://simonwillison.net/2026/Jan/11/dont-fall-into-the-anti-ai-hype/))

**Post angle:** 'Even if AI is a bubble, the 2000 telecom crash didn't end the internet. The real question is who is left holding the bill.' ([Latent Space, 2026-04-03](https://latent.space/p/pmarca/)) ([Tomasz Tunguz, 2025-12-03](https://tomtunguz.com/top-10-posts-2025/))

## 4. Will AI improve itself, and when does AGI arrive?

**The question:** Will AI that builds better AI trigger runaway progress, or will bottlenecks slow it? ([One Useful Thing, 2026-03-12](https://www.oneusefulthing.org/p/the-shape-of-the-thing)) ([Interconnects, 2026-09-10](https://www.interconnects.ai/p/one-resignation-turned-the-embers))

**Takeoff side:** Proponents of recursive self-improvement expect fast takeoff. Zvi Mowshowitz argues that diminishing-returns assumptions miss paradigm shifts. Ramez Naam counters that the current loop is too weak. ([Interconnects, 2026-09-10](https://www.interconnects.ai/p/one-resignation-turned-the-embers)) ([Don't Worry About the Vase, 2026-10-01](https://thezvi.substack.com/p/ai-188-gemini-dot-argon))

**Skeptical side:** Nathan Lambert argues human bottlenecks and jagged capabilities make returns far smaller, which he calls 'lossy self-improvement'. Ethan Mollick frames it as unresolved, with bottlenecks possible in compute, data or research difficulty. Import AI says it remains unclear whether progress comes through paradigm-changing creativity or slow compounding gains. ([Interconnects, 2026-09-10](https://www.interconnects.ai/p/one-resignation-turned-the-embers)) ([One Useful Thing, 2026-03-12](https://www.oneusefulthing.org/p/the-shape-of-the-thing)) ([Import AI, 2026-06-22](https://importai.substack.com/p/import-ai-462-superpersuasion-self))

**Timelines:** Gary Marcus argues 2027 AGI timelines are unrealistic and called the AI 2027 scenario marketing-like speculation. Another thread questions whether AGI claims mean anything without an operational definition, and whether timelines are IPO-driven hype. A related argument: can AI make discoveries in the physical world or only in verifiable domains like math? ([Marcus on AI, 2025-11-21](https://garymarcus.substack.com/p/breaking-the-ai-2027-doomsday-scenario)) ([AINews (smol.ai), 2026-08-24](https://news.smol.ai/issues/26-08-27-not-much/)) ([Latent Space, 2026-10-08](https://latent.space/p/periodic/))

**Why it matters:** Timelines drive investment, policy and career decisions. Without a shared definition of AGI, the predictions can't be compared. ([AINews (smol.ai), 2026-08-24](https://news.smol.ai/issues/26-08-27-not-much/))

**Post angle:** 'Before you trust any AGI date, ask: how is AGI defined, and who benefits from the timeline?' ([AINews (smol.ai), 2026-08-24](https://news.smol.ai/issues/26-08-27-not-much/)) ([Marcus on AI, 2025-11-21](https://garymarcus.substack.com/p/breaking-the-ai-2027-doomsday-scenario))

## 5. Are AI models commodities with no moat?

**The question:** If top models perform similarly, where does a lasting advantage come from? ([Simon Willison's Weblog, 2026-03-06](https://simonwillison.net/2026/Mar/6/anthropic-and-the-pentagon/))

**Commodity case:** Bruce Schneier and Nathan Sanders argue top-tier models are commoditized with similar performance, so branding and perceived trustworthiness differentiate providers. Gary Marcus argues OpenAI's market share is eroding as competitors build similar products. Alberto Romero frames it as whether models are swappable like electricity (Apple's view) or transformative technology that justifies massive capex. ([Simon Willison's Weblog, 2026-03-06](https://simonwillison.net/2026/Mar/6/anthropic-and-the-pentagon/)) ([Marcus on AI, 2026-06-16](https://garymarcus.substack.com/p/openais-lead-is-dwindling-fast)) ([The Algorithmic Bridge, 2026-05-30](https://www.thealgorithmicbridge.com/p/what-apple-knows-about-ai-that-silicon))

**Moat case:** Arguments for defensibility include enterprise contracts, exclusive private models and full-stack platforms. In vertical products like Harvey and OpenEvidence, one side points to proprietary data and specialized UI, while the other says general models will absorb the tasks. Arvind Narayanan asks whether labs can move up the stack into products and services or stay undifferentiated vendors. ([Hacker News — Ask HN, 2026-02-13](https://news.ycombinator.com/item?id=46998801)) ([Latent Space, 2026-10-21](https://latent.space/p/tenex/)) ([AI as Normal Technology, 2026-07-09](https://www.normaltech.ai/p/up-the-stack-how-ais-escape-from))

**Why it matters:** If you build on AI, the question is whether your product survives when the model vendor adds your feature. One thread questioned Graphify's defensibility since its code is free and easy for agents to reproduce. ([AINews (smol.ai), 2026-06-29](https://news.smol.ai/issues/26-06-29-not-much/)) ([Latent Space, 2026-10-21](https://latent.space/p/tenex/))

**Post angle:** 'In a world of near-identical models, what is your moat: data, distribution, trust, or just a head start?' ([Simon Willison's Weblog, 2026-03-06](https://simonwillison.net/2026/Mar/6/anthropic-and-the-pentagon/)) ([Latent Space, 2026-10-21](https://latent.space/p/tenex/))

## 6. Does scaling still work, or are new architectures needed?

**The question:** Can more compute and data get to AGI, or do we need world models and neurosymbolic approaches? ([Marcus on AI, 2026-03-14](https://garymarcus.substack.com/p/breaking-expensive-new-evidence-that)) ([Marcus on AI, 2025-11-27](https://garymarcus.substack.com/p/a-trillion-dollars-is-a-terrible))

**New ideas side:** Gary Marcus argues for world models and neurosymbolic AI. In one thread, Sutskever and Marcus are placed against scaling advocates. Marcus also argued that Anthropic's coding speedups come from harnesses and neurosymbolic tools rather than pure deep learning scaling. ([Marcus on AI, 2026-03-14](https://garymarcus.substack.com/p/breaking-expensive-new-evidence-that)) ([Marcus on AI, 2025-11-27](https://garymarcus.substack.com/p/a-trillion-dollars-is-a-terrible)) ([Marcus on AI, 2026-06-05](https://garymarcus.substack.com/p/no-need-to-panic-about-anthropics))

**Scaling side:** Some point to improved pre-training and post-training delivering gains. Others say compute returns are shifting from pretraining to RL and data generation, while some say scaling is dead. Yi Tay argues progress comes from ideas combining well, not scaling alone. ([Tomasz Tunguz, 2025-12-03](https://tomtunguz.com/top-10-posts-2025/)) ([AINews (smol.ai), 2026-01-06](https://news.smol.ai/issues/26-01-06-xai-series-e/)) ([Latent Space, 2026-01-23](https://latent.space/p/captaining-imo-gold-deep-think-on/))

**Why it matters:** Alberto Romero notes the premise of current generative AI investment is at stake. A plateau also matters for whether consumer hardware could run near-frontier models. ([The Algorithmic Bridge, 2026-03-19](https://www.thealgorithmicbridge.com/p/openais-dead)) ([Hacker News — Ask HN, 2026-02-13](https://news.ycombinator.com/item?id=46998801))

**Post angle:** 'The scaling debate isn't scale versus no scale. It's whether the next gain comes from more compute or from a new idea.' ([Latent Space, 2026-01-23](https://latent.space/p/captaining-imo-gold-deep-think-on/)) ([AINews (smol.ai), 2026-01-06](https://news.smol.ai/issues/26-01-06-xai-series-e/))

## 7. What counts as vibe coding, and how far can AI coding go?

**The question:** Is vibe coding any AI-assisted coding, or only coding where you don't review the output? And can coding agents replace engineers? ([Simon Willison's Weblog, 2026-04-23](https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/)) ([Marcus on AI, 2026-04-27](https://garymarcus.substack.com/p/dario-amodei-hype-ai-safety-and-the))

**Definition fight:** Simon Willison argues vibe coding means using code without review, and a project can be pure vibe coding yet still low-risk. Another view says if you cannot fix the AI-generated code, you are vibe coding. ([Simon Willison's Weblog, 2026-04-23](https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/)) ([AINews (smol.ai), 2026-01-14](https://news.smol.ai/issues/26-01-14-not-much/))

**Replacement fight:** Dario Amodei's claim that agents can replace software engineers who architect and maintain systems was criticized as overhyping autonomous AI. Sebastian Raschka argues expert codebases still win because replicating them takes much effort. Alberto Romero notes it's unresolved whether AI-written code reflects AI capability or hidden human guidance in prompts, judgment and taste. ([Marcus on AI, 2026-04-27](https://garymarcus.substack.com/p/dario-amodei-hype-ai-safety-and-the)) ([Ahead of AI, 2025-12-30](https://magazine.sebastianraschka.com/p/state-of-llms-2025)) ([The Algorithmic Bridge, 2026-01-13](https://www.thealgorithmicbridge.com/p/claude-code-coded-claude-cowork))

**Discipline and tools:** Hamel Husain asked whether AI tools encourage lazy thinking or whether discipline rests with the developer. Developers also split on terminal versus GUI for agents, and on Codex versus Claude Code. ([Hamel Husain, 2026-01-18](https://hamel.dev/blog/posts/ai-stack/)) ([Ben's Bites, 2026-05-09](https://www.bensbites.com/p/bens-builds-3-an-email-app)) ([Hacker News — Ask HN, 2026-05-17](https://news.ycombinator.com/item?id=48166147))

**Why it matters:** For a non-engineer building apps, the definition decides how much risk to assume: reviewing code versus shipping on trust. ([Simon Willison's Weblog, 2026-04-23](https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/)) ([AINews (smol.ai), 2026-01-14](https://news.smol.ai/issues/26-01-14-not-much/))

**Post angle:** 'Vibe coding isn't the same as AI-assisted coding. The dividing line is whether anyone reads the code.' ([Simon Willison's Weblog, 2026-04-23](https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/))

## 8. Are Chinese open models catching up, and will open models keep pace?

**The question:** Is the gap between open and closed models, and between Chinese and US models, closing? ([Interconnects, 2026-09-11](https://www.interconnects.ai/p/open-source-ai-reading-list)) ([Don't Worry About the Vase, 2026-06-29](https://thezvi.substack.com/p/wsj-article-claiming-china-has-matched))

**Gap-persists side:** Nathan Lambert expects American closed labs to pull ahead on capabilities despite strong open-weight results. Yi Tay argues the closed-open gap may be widening because ideas compound over time. Zvi Mowshowitz argues the gap between Chinese open models like GLM-5.2 and top US models is not steadily shrinking. ([Interconnects, 2026-04-15](https://www.interconnects.ai/p/my-bets-on-open-models-mid-2026)) ([Latent Space, 2026-01-23](https://latent.space/p/captaining-imo-gold-deep-think-on/)) ([Don't Worry About the Vase, 2026-06-29](https://thezvi.substack.com/p/wsj-article-claiming-china-has-matched))

**Convergence side:** Data cited by Lambert show a 4-6 month gap between open and closed models. For Kimi K2.6, some call it the best open coding model, while others cite large gaps on reliability and long-horizon tasks. Lambert also asks whether upcoming US open models, such as GPT-OSS, Nemotron, Arcee or Reflection AI, can challenge the Chinese lead in adoption. ([Interconnects, 2026-09-11](https://www.interconnects.ai/p/open-source-ai-reading-list)) ([AINews (smol.ai), 2026-04-21](https://news.smol.ai/issues/26-04-21-image-2/)) ([Interconnects, 2026-01-07](https://www.interconnects.ai/p/8-plots-that-explain-the-state-of))

**Why it matters:** Restricted frontier access could strengthen open-weight models, but open models don't stop malicious use. A Hacker News thread asked whether Chinese labs will restrict access by nationality or expand exports. ([AINews (smol.ai), 2026-06-26](https://news.smol.ai/issues/26-06-26-gpt-56-preview/)) ([Hacker News — Ask HN, 2026-06-13](https://news.ycombinator.com/item?id=48519780))

**Post angle:** 'Open models trail the frontier by months, not years, but  ([Interconnects, 2026-09-11](https://www.interconnects.ai/p/open-source-ai-reading-list))

the real argument is whether that gap holds.' ([Interconnects, 2026-09-11](https://www.interconnects.ai/p/open-source-ai-reading-list)) ([Interconnects, 2026-04-15](https://www.interconnects.ai/p/my-bets-on-open-models-mid-2026))

## 9. Is training on copyrighted work and open code fair?

**The question:** Is AI training fair use, can licenses stop it, and who owns what AI produces? ([Hacker News — Ask HN, 2026-02-13](https://news.ycombinator.com/item?id=47000737)) ([Hacker News — Ask HN, 2026-02-13](https://news.ycombinator.com/item?id=47000737))

**Fair-use side:** One discussion held that training may be fair use, so copyright-based licensing may not apply, and materials must be legally obtained. Another argued that a training-prohibition clause is hard to enforce because training data is inaccessible. ([Hacker News — Ask HN, 2026-02-13](https://news.ycombinator.com/item?id=47000737)) ([Hacker News — Ask HN, 2026-02-13](https://news.ycombinator.com/item?id=47000737))

**Skeptical side:** Gary Marcus criticizes OpenAI for complaining about IP being taken after it trained on artists' and writers' work without permission. Chris Lattner calls whether AI reproducing familiar code structures is learning or copying an open IP question. Simon Willison asks whether code largely produced by an LLM can carry copyright, which depends on human creative control. ([Marcus on AI, 2026-02-13](https://garymarcus.substack.com/p/irony-irony-laced-with-karma-and)) ([Simon Willison's Weblog, 2026-02-22](https://simonwillison.net/2026/Feb/22/ccc/)) ([Simon Willison's Weblog, 2026-01-11](https://simonwillison.net/2026/Jan/11/answers/))

**Definitions again:** The OSI definition and Linux Foundation openness framework disagree on whether open-weights releases count as open source. ([Interconnects, 2025-11-12](https://www.interconnects.ai/p/inside-a-chinese-frontier-lab-inclusion))

**Why it matters:** Anyone publishing AI-built code or content faces unsettled rules about licensing and ownership. ([Simon Willison's Weblog, 2026-01-11](https://simonwillison.net/2026/Jan/11/answers/)) ([Simon Willison's Weblog, 2026-01-11](https://simonwillison.net/2026/Jan/11/answers/))

**Post angle:** 'Who owns code your AI wrote? The answer may depend on how much creative direction you gave it.' ([Simon Willison's Weblog, 2026-01-11](https://simonwillison.net/2026/Jan/11/answers/))

## 10. Can AI vendors limit how governments use their models?

**The question:** Should a company be able to bar uses like mass domestic surveillance or fully autonomous weapons through contract, or should government decide all lawful uses? ([Don't Worry About the Vase, 2026-02-27](https://thezvi.substack.com/p/anthropic-and-the-dow-anthropic-responds)) ([Don't Worry About the Vase, 2026-03-05](https://thezvi.substack.com/p/ai-158-the-department-of-war))

**Vendor side:** Dario Amodei argued for safeguards, and Anthropic refused a Pentagon request for relaxed Claude access, holding to no autonomous weapons and no mass surveillance, which may cost a contract. Gary Marcus reported Anthropic refusing to back down. ([Don't Worry About the Vase, 2026-02-27](https://thezvi.substack.com/p/anthropic-and-the-dow-anthropic-responds)) ([Ben's Bites, 2026-02-26](https://www.bensbites.com/p/claude-has-some-conflicts)) ([Marcus on AI, 2026-02-27](https://garymarcus.substack.com/p/did-trump-just-overplay-his-hand))

**Government side:** The Department of War argued for unrestricted access. Emil Michael's debate was whether Anthropic's redlines are an illegitimate operational veto or ordinary contract terms with force of law. Timothy B. Lee framed it as trusting government promises versus needing contractual or legislative constraints. ([Don't Worry About the Vase, 2026-02-27](https://thezvi.substack.com/p/anthropic-and-the-dow-anthropic-responds)) ([Don't Worry About the Vase, 2026-03-27](https://thezvi.substack.com/p/anthropic-vs-dow-6-the-court-rules)) ([Understanding AI, 2026-03-02](https://www.understandingai.org/p/the-pentagons-bombshell-deal-with))

**Legal question:** Alan Rozenshtein argued a preliminary injunction against the supply chain risk designation could go either way. He also raised whether redlines actually constrain government behavior. ([Don't Worry About the Vase, 2026-03-18](https://thezvi.substack.com/p/anthropic-vs-dow-5-motions-filed)) ([Don't Worry About the Vase, 2026-03-05](https://thezvi.substack.com/p/ai-158-the-department-of-war))

**Why it matters:** The dispute tests whether vendor contracts can function as AI governance. Separately, access limits were debated for a cyber-capable model, where Simon Willison judged the caution justified. ([Don't Worry About the Vase, 2026-02-27](https://thezvi.substack.com/p/anthropic-and-the-dow-anthropic-responds)) ([Simon Willison's Weblog, 2026-04-07](https://simonwillison.net/2026/Apr/7/project-glasswing/))

**Post angle:** 'Can a software contract be an AI safety policy? One company just tried to find out.' ([Don't Worry About the Vase, 2026-02-27](https://thezvi.substack.com/p/anthropic-and-the-dow-anthropic-responds)) ([Don't Worry About the Vase, 2026-03-27](https://thezvi.substack.com/p/anthropic-vs-dow-6-the-court-rules))

