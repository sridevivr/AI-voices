# Who Drives the AI Conversation: A Field Guide to the Voices Worth Following

*From Simon Willison's hands-on agent notes to Ed Zitron's compute skepticism, here is who shapes the year's AI commentary, what each person argues, and where a non-engineer can join in.*

*Period: 2025-11-11 to 2026-11-14 · 30,139 findings from 20 sources · generated 2026-11-22 by `python -m src.insights write`. Numbers and tables come from code; prose is Sonnet's; every link is a finding the text cites.*

## Key points

- Start with Simon Willison. He has the most findings (1,829) and writes about coding agents and tooling, which is the vibe-coding territory you work in. ([Simon Willison's Weblog, 2026-11-09](https://simonwillison.net/2026/Nov/9/mysterious-beeps/)) ([Simon Willison's Weblog, 2026-09-10](https://simonwillison.net/2026/Sep/10/shopify-react-native/))
- Add Ben Tossell for practical agent tools and workflows, and Tomasz Tunguz for the business and cost side (token prices, GPU rental rates, how much agent work is plain code). ([Ben's Bites, 2026-11-10](https://www.bensbites.com/p/how-i-got-seduced)) ([Tomasz Tunguz, 2026-10-06](https://tomtunguz.com/how-to-automate-inbound/)) ([Tomasz Tunguz, 2026-11-04](https://tomtunguz.com/watts-in-store-for-2027-inference/))
- For a broad LinkedIn audience, Ethan Mollick and Alberto Romero cover work, writing and creativity, topics that readers outside tech can relate to. ([Bluesky, 2026-09-22](https://bsky.app/profile/emollick.bsky.social/post/3mw3cswdlw226)) ([The Algorithmic Bridge, 2026-10-21](https://www.thealgorithmicbridge.com/p/put-some-brain-in-your-thinking))
- Zvi Mowshowitz, Gary Marcus, Emily Bender and Ed Zitron give you the skeptical and safety-minded side. Their posts are good for replies and counterpoints. ([Don't Worry About the Vase, 2026-10-26](https://thezvi.substack.com/p/gemini-4-argon-the-model-and-safety)) ([Marcus on AI, 2026-10-31](https://garymarcus.substack.com/p/report-from-the-vatican)) ([Bluesky, 2026-10-09](https://bsky.app/profile/emilymbender.bsky.social/post/3mxho5xod3s2k)) ([Bluesky, 2026-11-10](https://bsky.app/profile/edzitron.com/post/3mzy3bn3u5s2i))
- Counts reflect how much each source publishes and quotes, not how influential a person is. Prolific bloggers will rank high, and people who post mostly on Bluesky may be undercounted.

## Start here: the builders

**Simon Willison** (1,829 findings, via his Weblog and Bluesky) focuses on devtools, coding agents and testing. He mostly reports techniques and pain points from his own experiments. One example: giving a coding agent "hearing" by running microphones on several devices and hot-swapping JavaScript over WebSockets. He also flags debates, such as Shopify moving mobile apps from React Native back to separate Swift and Kotlin codebases because agents lower the cost of maintaining two platforms. Follow him for concrete, reproducible examples that you can try and write about. ([Simon Willison's Weblog, 2026-11-09](https://simonwillison.net/2026/Nov/9/mysterious-beeps/)) ([Simon Willison's Weblog, 2026-09-10](https://simonwillison.net/2026/Sep/10/shopify-react-native/))

**Ben Tossell** (713 findings, via Ben's Bites) covers coding agents, orchestration and productivity. His posts recommend specific tools, such as Executor v2 for integrations and UI skills for design work. He also records debates that matter to non-engineers, like whether agent-written "slop" is acceptable if the code works, is secure and performs. This is a good source of tool picks and quotable arguments. ([Ben's Bites, 2026-11-10](https://www.bensbites.com/p/how-i-got-seduced)) ([Ben's Bites, 2026-10-13](https://www.bensbites.com/p/zucks-wonderfull))

**antirez**, **Gergely Orosz** and **Hamel Husain** are smaller voices (216, 202 and 94 findings) with practical views. antirez argues that developers who refuse AI help risk falling behind, and he discusses local inference trade-offs. Orosz asks whether hand-coding is becoming obsolete and shows how to connect Sentry to a coding agent through MCP. Husain writes about evals and how to choose between precision and recall based on business consequences. Reply to them when you have a hands-on experience to compare. ([Bluesky, 2026-11-09](https://bsky.app/profile/antirez.bsky.social/post/3mzukga6eo22b)) ([Bluesky, 2026-09-24](https://bsky.app/profile/gergely.pragmaticengineer.com/post/3mwb3mufsjk2k)) ([Bluesky, 2026-07-22](https://bsky.app/profile/gergely.pragmaticengineer.com/post/3mrabnxvsf22w)) ([Hamel Husain, 2026-10-20](https://hamel.dev/blog/posts/decision-model-evals/))

**swyx** (174 findings, plus 106 shared with Alessio Fanelli, via Latent Space) tracks agents and orchestration. His warning is that teams burn tokens on agent experiments without shipping real products. He also asks whether agent skills should be written by hand or taken from community packs. He is useful if you write about how teams adopt agents. ([Latent Space, 2026-11-08](https://latent.space/p/cs146s/))

## The business and money lens

**Tomasz Tunguz** (833 findings) writes about markets, agents and cost. His data points are easy to cite. Short-term GPU rental rates reportedly jumped from about $3 to $12-13 per hour. In 14 production agent workflows, 65% of nodes were pure code. He also notes a UC Berkeley study finding that harness software can cut the cost of resolving the same task by 71% without losing accuracy. He is a strong source for a program-manager audience that cares about unit economics. ([Tomasz Tunguz, 2026-11-04](https://tomtunguz.com/watts-in-store-for-2027-inference/)) ([Tomasz Tunguz, 2026-10-06](https://tomtunguz.com/how-to-automate-inbound/))

**Ed Zitron** (301 findings, mostly Bluesky) is the main skeptic on AI economics. He cites JPMorgan's estimate of under 0.5% cumulative productivity gain over a decade. He questions whether 190GW of planned AI compute has real demand, and he points out that published GPU price indices diverge from what users report paying. He is worth quoting when you want a counterweight to boom narratives, and worth checking carefully before you repeat his claims. ([Bluesky, 2026-11-10](https://bsky.app/profile/edzitron.com/post/3mzy3bn3u5s2i)) ([Bluesky, 2026-07-31](https://bsky.app/profile/edzitron.com/post/3mrxdzj544k2y)) ([Bluesky, 2026-10-13](https://bsky.app/profile/edzitron.com/post/3mxrguttrcy2r))

## Explainers for a broad professional audience

**Ethan Mollick** (686 findings, One Useful Thing and Bluesky) covers capabilities, creative work and knowledge work. He raises questions such as whether AI peer review should change academic science, and whether craft in fields like coding survives automation, given that augmentation lacks a playbook compared to automation. He also shares small demos, like turning video clips into interactive 3D scenes. His posts translate well to LinkedIn. ([Bluesky, 2026-10-23](https://bsky.app/profile/emollick.bsky.social/post/3myjcs6g7zc2q)) ([Bluesky, 2026-09-22](https://bsky.app/profile/emollick.bsky.social/post/3mw3cswdlw226)) ([Bluesky, 2026-11-10](https://bsky.app/profile/emollick.bsky.social/post/3mzxw7q2jgs2r))

**Alberto Romero** (298 findings, The Algorithmic Bridge) focuses on AI writing. Topics include whether undisclosed AI-assisted writing breaks the reader-writer contract, and estimates that about half of published articles are AI-generated. If you publish on AI, his questions about disclosure apply to you directly. ([The Algorithmic Bridge, 2026-03-26](https://www.thealgorithmicbridge.com/p/its-ai-so-i-didnt-read)) ([The Algorithmic Bridge, 2026-10-21](https://www.thealgorithmicbridge.com/p/put-some-brain-in-your-thinking))

**Mike Caulfield** (116 findings) and **Anil Dash** (97) bring education and culture. Caulfield notes that AI grading of essays needs more than a pasted rubric, and that a Cambridge study found AI matched human grades only about half the time. Dash asks whether everyday people will really build their own apps with AI or whether effort keeps it a niche, a question close to your own vibe coding. ([Bluesky, 2026-09-12](https://bsky.app/profile/mikecaulfield.bsky.social/post/3mvciiiczyc2g)) ([Bluesky, 2026-05-15](https://bsky.app/profile/anildash.com/post/3mlvnc2ytkc2v))

## Safety, governance and the skeptics

**Zvi Mowshowitz** (922 findings, Don't Worry About the Vase) is the detailed tracker of safety and evals. He dissects whether a low misalignment rate shows real alignment or just evaluation awareness, and he describes the layered defenses labs use, such as classifiers, probes and monitors. His posts are long, so mine them for single, quotable distinctions. ([Don't Worry About the Vase, 2026-10-26](https://thezvi.substack.com/p/gemini-4-argon-the-model-and-safety))

**Gary Marcus** (538 findings) and **Emily M. Bender** (179) are the critics. Marcus questions whether an accord's "independent" oversight is truly independent and argues current LLMs are not conscious. Bender disputes claims that Claude can feel pain, saying the burden of proof lies with those making the claim. Expect pushback when you reply, but their arguments help you test your own claims. ([Marcus on AI, 2026-09-29](https://garymarcus.substack.com/p/hot-take-on-a-weak-white-house-accord)) ([Marcus on AI, 2026-10-31](https://garymarcus.substack.com/p/report-from-the-vatican)) ([Bluesky, 2026-10-09](https://bsky.app/profile/emilymbender.bsky.social/post/3mxho5xod3s2k))

**Sayash Kapoor and Arvind Narayanan** (95 findings, AI as Normal Technology) offer a measured view on evaluation and liability. They argue that judging agents means examining entire trajectories, not just final outcomes. They also lay out the open debate over whether AI liability should rely on tort law, strict liability or stronger negligence rules. ([AI as Normal Technology, 2026-10-19](https://www.normaltech.ai/p/new-paper-emerging-trends-in-ai-agent)) ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view))

## Researchers and the open-model world

**Nathan Lambert** (668 findings, Interconnects) covers training and open models. He cites estimates that distillation of American closed models closes only 1-2 months of the gap behind Chinese open models, and he asks whether open models should be restricted after a potential misuse incident. **Sebastian Raschka** (127) is more technical, on verbose reasoning models and calibration. **hardmaru** (71) shares research on multi-agent systems and AI co-scientists. These three are best for staying current on the technical side without reading papers. ([Interconnects, 2026-09-21](https://www.interconnects.ai/p/the-current-balance-of-power-in-open)) ([Interconnects, 2026-09-10](https://www.interconnects.ai/p/one-resignation-turned-the-embers)) ([Ahead of AI, 2026-07-18](https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms)) ([Bluesky, 2026-06-22](https://bsky.app/profile/hardmaru.bsky.social/post/3motv2lwguk22))

## Table: who drives the conversation

| Person | Findings | Mostly about | Via |
|---|---|---|---|
| Simon Willison | 1,829 | devtools & IDEs, coding agents, evals & testing | Simon Willison's Weblog, Bluesky |
| Zvi Mowshowitz | 922 | safety & governance, evals & testing, consumer apps | Don't Worry About the Vase |
| Tomasz Tunguz | 833 | business & markets, agents & orchestration, observability & cost | Tomasz Tunguz, Don't Worry About the Vase |
| Ben Tossell | 713 | coding agents, agents & orchestration, productivity & knowledge work | Ben's Bites |
| Ethan Mollick | 686 | research & capabilities, creative & media, productivity & knowledge work | Bluesky, One Useful Thing |
| Nathan Lambert | 668 | model training & fine-tuning, local & open models, research & capabilities | Interconnects, Bluesky |
| Gary Marcus | 538 | safety & governance, research & capabilities, business & markets | Marcus on AI, Bluesky |
| Ed Zitron | 301 | business & markets, observability & cost, inference & infra | Bluesky |
| Alberto Romero | 298 | productivity & knowledge work, safety & governance, consumer apps | The Algorithmic Bridge |
| antirez | 216 | coding agents, local & open models, inference & infra | Bluesky, Simon Willison's Weblog |
| Gergely Orosz | 202 | coding agents, productivity & knowledge work, devtools & IDEs | Bluesky, Tomasz Tunguz |
| Emily M. Bender | 179 | safety & governance, research & capabilities, consumer apps | Bluesky |
| swyx | 174 | agents & orchestration, coding agents, productivity & knowledge work | Latent Space, AINews (smol.ai) |
| Sebastian Raschka | 127 | inference & infra, model training & fine-tuning, research & capabilities | Ahead of AI, Bluesky |
| Mike Caulfield | 116 | productivity & knowledge work, education & learning, consumer apps | Bluesky |
| swyx & Alessio Fanelli | 106 | research & capabilities, agents & orchestration, evals & testing | Latent Space |
| Anil Dash | 97 | consumer apps, safety & governance, coding agents | Bluesky |
| Sayash Kapoor, Arvind Narayanan | 95 | evals & testing, safety & governance, research & capabilities | AI as Normal Technology |
| Hamel Husain | 94 | evals & testing, coding agents, devtools & IDEs | Hamel Husain, AINews (smol.ai) |
| hardmaru | 71 | research & capabilities, agents & orchestration, model training & fine-tuning | Bluesky |

Counts reflect how much each source publishes and quotes, not influence.

