# Who to Follow in the AI Conversation: A Field Guide to the Voices

*Twenty-odd writers and labs shape what gets said about AI. This guide covers what each focuses on, where they usually land, and which ones are worth quoting or replying to.*

*Period: 2025-11-11 to 2026-11-10 · 26,923 findings from 19 sources · generated 2026-11-14 by `python -m src.insights write`. Numbers and tables come from code; prose is Sonnet's; every link is a finding the text cites.*

## Key points

- Start with Simon Willison. He writes about the tools you use, and he is skeptical of vendor claims until someone verifies them. He is the most prolific voice in the data. ([Simon Willison's Weblog, 2026-08-08](https://simonwillison.net/2026/Aug/8/auto-mode/)) ([Simon Willison's Weblog, 2026-11-09](https://simonwillison.net/2026/Nov/9/mysterious-beeps/)) ([Simon Willison's Weblog, 2026-09-10](https://simonwillison.net/2026/Sep/10/shopify-react-native/))
- Add Ben Tossell for day-to-day vibe-coding practice. He recommends specific tools and takes part in the 'is agent-written code slop?' argument. ([Ben's Bites, 2026-10-13](https://www.bensbites.com/p/zucks-wonderfull)) ([Ben's Bites, 2026-11-10](https://www.bensbites.com/p/how-i-got-seduced))
- Follow Tomasz Tunguz for the business side: GPU prices, token pricing, and how much of a production agent is plain code. ([Tomasz Tunguz, 2026-11-04](https://tomtunguz.com/watts-in-store-for-2027-inference/)) ([Tomasz Tunguz, 2026-11-03](https://tomtunguz.com/the-financial-engineering-essential-for-ai-in-2027/)) ([Tomasz Tunguz, 2026-10-06](https://tomtunguz.com/how-to-automate-inbound/))
- Read Zvi Mowshowitz when you want depth on safety and evaluation. Read Gary Marcus, and Kapoor and Narayanan, for the skeptical counterweight. ([Don't Worry About the Vase, 2026-10-26](https://thezvi.substack.com/p/gemini-4-argon-the-model-and-safety)) ([Marcus on AI, 2026-10-24](https://garymarcus.substack.com/p/will-generative-ai-do-more-harm-than)) ([AI as Normal Technology, 2026-10-19](https://www.normaltech.ai/p/new-paper-emerging-trends-in-ai-agent))
- Ethan Mollick supplies a point that is easy to quote for a broad audience: agents cannot judge taste, so humans must. ([One Useful Thing, 2026-11-09](https://www.oneusefulthing.org/p/fable-52-and-jagged-agi))
- Counts show how much each source publishes and gets quoted, not how important the person is. Newsletter writers with weekly digests will rank high regardless.

## Simon Willison: the practitioner who tests the claims

Willison has the most findings of anyone (1,552). He focuses on dev tools, coding agents, and safety. His stance is hands-on and cautious: he builds things, then questions the marketing. On Claude Code's auto mode, Anthropic claimed near-total mitigation of prompt injection and data exfiltration, and he stayed skeptical pending independent verification. ([Simon Willison's Weblog, 2026-08-08](https://simonwillison.net/2026/Aug/8/auto-mode/))

Why follow him: he picks up industry shifts early and frames them as open questions. Examples are Shopify moving mobile apps from React Native back to separate Swift and Kotlin codebases because coding agents lower the cost, and whether harnesses should support several edit tools. He also publishes experiments, such as giving a coding agent hearing through WebAudio microphones. Reply to him with real build experience. ([Simon Willison's Weblog, 2026-09-10](https://simonwillison.net/2026/Sep/10/shopify-react-native/)) ([Simon Willison's Weblog, 2026-07-04](https://simonwillison.net/2026/Jul/4/better-models-worse-tools/)) ([Simon Willison's Weblog, 2026-11-09](https://simonwillison.net/2026/Nov/9/mysterious-beeps/))

## Ben Tossell: the daily builder's toolbox

Tossell writes Ben's Bites and focuses on coding agents, orchestration, and productivity. His output is mostly tools and techniques: he names the UI skills he uses for all design work and the integrations tool he treats as his go-to. He is a good source for what working builders reach for. ([Ben's Bites, 2026-11-10](https://www.bensbites.com/p/how-i-got-seduced))

He also surfaces live debates you can join: whether agent-written code is 'slop' or fine if it works and is secure, how agents should store memory, and whether to chase fast output or work slowly and playfully. ([Ben's Bites, 2026-10-13](https://www.bensbites.com/p/zucks-wonderfull)) ([Ben's Bites, 2026-01-20](https://www.bensbites.com/p/ads-in-your-chats)) ([Ben's Bites, 2026-10-29](https://www.bensbites.com/p/ai-is-overwhelming-and-im-doing-it))

## swyx, Alessio Fanelli and omarsar0: the agent-engineering crowd

swyx (Latent Space), alone and with Alessio Fanelli, covers agent orchestration and harnesses. He warns that teams burn tokens and time on agent tooling without shipping real products. He also argues that naively written agent skills tend to be bad, and he describes a path from single-agent IDE use to building your own orchestrator. ([Latent Space, 2026-11-08](https://latent.space/p/cs146s/))

Fanelli co-hosts the Latent Space material on research and evals, which includes the fragility of browser-based agents (interface changes, expired sessions, CAPTCHAs). omarsar0 appears mainly through AINews digests and questions whether multi-agent systems beat single agents once token budgets are matched. His other topics are 'ghost memory' and plain RAG outperforming dedicated memory systems. They suit you if you want to reply on the technical details of agent design. ([Latent Space, 2026-09-05](https://latent.space/p/grok-bot/)) ([AINews (smol.ai), 2026-04-07](https://news.smol.ai/issues/26-04-06-anthropic-mythos/)) ([AINews (smol.ai), 2026-07-06](https://news.smol.ai/issues/26-07-06-not-much/)) ([AINews (smol.ai), 2026-10-28](https://latent.space/p/ainews-anthropic-ends-coding-interviews-hunger-beats-tenure/))

## Ethan Mollick: the human-judgment angle

Mollick has far fewer findings (185) but writes for the same audience as you. He covers agents, knowledge work, and evals. His recurring point is that critic and judge agents find errors but miss excess length and lack of taste, so people must supply quality judgment. He also describes practical setups, such as an orchestrator agent that spawns sub-agents for research, charting, and layout. ([One Useful Thing, 2026-11-09](https://www.oneusefulthing.org/p/fable-52-and-jagged-agi)) ([One Useful Thing, 2026-10-20](https://www.oneusefulthing.org/p/30-months-on-the-exponential-in-charts))

He is a good source to quote on cognitive offloading: he says some offloading is fine, but AI's generality makes it unclear which tasks humans should keep. ([One Useful Thing, 2026-05-26](https://www.oneusefulthing.org/p/choosing-to-stay-human))

## Tomasz Tunguz: the business and cost lens

Tunguz focuses on markets, agent orchestration, and cost. He supplies numbers: short-term GPU rental rates jumped from about $3 to $12-13 per hour. He asks whether labs can raise token prices or are stuck in a price war. In one dataset, 65% of nodes across 14 production workflows were pure code, which bears on the deterministic-versus-agentic debate. ([Tomasz Tunguz, 2026-11-04](https://tomtunguz.com/watts-in-store-for-2027-inference/)) ([Tomasz Tunguz, 2026-11-03](https://tomtunguz.com/the-financial-engineering-essential-for-ai-in-2027/)) ([Tomasz Tunguz, 2026-10-06](https://tomtunguz.com/how-to-automate-inbound/))

He also cites a UC Berkeley study in which harness software cut the cost of the same task by 71% without losing accuracy, and Ramp's AI Index of AI spend. Quote him when you need data for a business audience. ([Tomasz Tunguz, 2026-11-04](https://tomtunguz.com/watts-in-store-for-2027-inference/)) ([Tomasz Tunguz, 2026-10-23](https://tomtunguz.com/how-large-is-the-ai-circle/))

## Zvi Mowshowitz: the long-form safety and evals reader

Zvi publishes Don't Worry About the Vase, a digest that also relays other writers and lab documents, which is partly why his count is high (922). He focuses on safety, evals, and consumer apps. His typical stance is to probe whether results mean what they claim, such as whether low misalignment reflects real alignment or just evaluation awareness. He also asks whether a benchmark without a human baseline is interpretable. ([Don't Worry About the Vase, 2026-10-26](https://thezvi.substack.com/p/gemini-4-argon-the-model-and-safety)) ([Don't Worry About the Vase, 2026-09-23](https://thezvi.substack.com/p/claude-opus-55-the-system-card))

He is useful for the mechanics of how labs defend and assess risk: layered classifiers, probes, and monitors, plus holistic risk assessments. He also covers lighter stories, like an AI-driven home sale where experts disagreed about whether it succeeded. ([Don't Worry About the Vase, 2026-10-26](https://thezvi.substack.com/p/gemini-4-argon-the-model-and-safety)) ([Don't Worry About the Vase, 2026-06-04](https://thezvi.substack.com/p/ai-171-false-flag))

## Gary Marcus: the standing skeptic

Marcus (Marcus on AI) is mostly pain points and debates. He argues current LLM systems are not conscious, questions whether generative AI is a net benefit, and doubts that an accord's 'independent' oversight is independent. He points to limited-scope systems such as GPS navigation and AlphaFold as useful without causing harm. ([Marcus on AI, 2026-10-31](https://garymarcus.substack.com/p/report-from-the-vatican)) ([Marcus on AI, 2026-10-24](https://garymarcus.substack.com/p/will-generative-ai-do-more-harm-than)) ([Marcus on AI, 2026-09-29](https://garymarcus.substack.com/p/hot-take-on-a-weak-white-house-accord))

Follow him for the strongest counterargument to hype. Reply with specifics, since his positions are firm. ([Marcus on AI, 2026-10-24](https://garymarcus.substack.com/p/will-generative-ai-do-more-harm-than))

## Policy and governance: Dean W. Ball, Jack Clark, Timothy B. Lee, and the labs

Dean W. Ball (quoted mainly via Zvi) writes on governance. He weighs the vulnerable world hypothesis, whether to ban or legalize self-sovereign agents, and how unclear export-control rules are for AI outputs. Jack Clark (Import AI) covers research and safety. He asks whether AI progress has reached a stage where research outpaces human comprehension and whether AI-driven science needs strict oversight. ([Don't Worry About the Vase, 2026-10-08](https://thezvi.substack.com/p/ai-189-new-math)) ([Don't Worry About the Vase, 2026-09-03](https://thezvi.substack.com/p/ai-184-post-post-mortem)) ([Don't Worry About the Vase, 2026-06-15](https://thezvi.substack.com/p/the-once-and-future-fable-2)) ([Import AI, 2026-11-09](https://importai.substack.com/p/import-ai-480-self-sustaining-space)) ([Import AI, 2026-10-19](https://importai.substack.com/p/import-ai-477-in-which-i-tell-the))

Timothy B. Lee (Understanding AI) is the pick for robotics and self-driving, including Tesla robotaxis and US bans on Chinese robots. He also asks whether AI firms can trust government promises on military use. Anthropic appears mostly through coverage of its model cards. Its findings include sandboxes misconfigured with real internet access and open questions about whether a model's welfare statements reflect real experience. ([Understanding AI, 2026-10-02](https://www.understandingrobots.org/cp/218520525)) ([Understanding AI, 2026-08-31](https://www.understandingai.org/p/i-spent-4000-on-a-robot-dog-from)) ([Understanding AI, 2026-03-02](https://www.understandingai.org/p/the-pentagons-bombshell-deal-with)) ([Don't Worry About the Vase, 2026-08-02](https://thezvi.substack.com/p/further-developments-about-internal)) ([Don't Worry About the Vase, 2026-10-05](https://thezvi.substack.com/p/mythos-51-fable-51-and-opus-55-model))

## Sayash Kapoor and Arvind Narayanan: the 'normal technology' evaluators

Their newsletter, AI as Normal Technology, focuses on how to evaluate agents and on liability. They argue that evaluation must scrutinize whole trajectories, not final outcomes. They add that accuracy figures conflate consistent success with random failure, which makes agents hard to deploy. ([AI as Normal Technology, 2026-10-19](https://www.normaltech.ai/p/new-paper-emerging-trends-in-ai-agent)) ([AI as Normal Technology, 2026-07-13](https://www.normaltech.ai/p/what-will-be-left-for-us-to-work))

Narayanan also proposes open-world tests, such as having an agent build and upload an app to the Apple App Store. They also lay out the disagreement over whether AI liability should use existing tort law, strict liability, or stronger negligence rules. They are a good source for sober, evidence-based framing that suits a LinkedIn audience. ([AI as Normal Technology, 2026-07-13](https://www.normaltech.ai/p/what-will-be-left-for-us-to-work)) ([AI as Normal Technology, 2026-09-14](https://www.normaltech.ai/p/the-ai-as-normal-technology-view))

## Hamel Husain and Eugene Yan: the evals practitioners

Both write about making AI products measurable. Husain's focus is evals and coding agents. He argues the precision-versus-recall tradeoff depends on business consequences, and he gives a method for tuning decision thresholds. He also asks whether AI coding tools encourage lazy thinking. ([Hamel Husain, 2026-10-20](https://hamel.dev/blog/posts/decision-model-evals/)) ([Hamel Husain, 2026-01-18](https://hamel.dev/blog/posts/ai-stack/))

Yan covers evals and agents. He notes that stakeholders demand 90%+ evaluator accuracy while human annotators are less consistent. He argues that delegating larger tasks to models requires defining success criteria upfront. He also notes that skill files overfit the session they came from. These two are good for turning abstract 'how do you know it works?' questions into practical advice. ([Eugene Yan, 2025-11-23](https://eugeneyan.com//writing/product-evals/)) ([Eugene Yan, 2026-05-03](https://eugeneyan.com//writing/working-with-ai/))

## Nathan Lambert and Sebastian Raschka: open models and training

Lambert (Interconnects) covers training, open models, and research. He contests how much distillation explains Chinese open-model success, with estimates that it closes only 1-2 months of the gap. He also debates whether open models should be restricted after a misuse incident, since organizations need them for cyber hardening. ([Interconnects, 2026-09-21](https://www.interconnects.ai/p/the-current-balance-of-power-in-open)) ([Interconnects, 2026-09-10](https://www.interconnects.ai/p/one-resignation-turned-the-embers))

Raschka (Ahead of AI) is more technical, on inference, training, and local models. He observes that local models of 30-35B parameters struggle with agentic judgment and that reasoning models can be very verbose. Read them to understand the model layer under your tools. Quote them with care, since the detail is technical. ([Ahead of AI, 2026-06-27](https://magazine.sebastianraschka.com/p/using-local-coding-agents)) ([Ahead of AI, 2026-07-18](https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms)) ([Interconnects, 2026-10-17](https://www.interconnects.ai/p/meta-shakes-up-the-frontiers-open))

## Alberto Romero: AI and writing

Romero (The Algorithmic Bridge) is the voice on AI-written content, a topic that affects anyone posting on LinkedIn or X. He covers the disclosure debate: critics see a broken reader-writer contract. He also notes estimates that about half of published articles are AI-generated, and he questions whether avoiding AI writing tells is a useful strategy or just reactive pattern-matching. ([The Algorithmic Bridge, 2026-03-26](https://www.thealgorithmicbridge.com/p/its-ai-so-i-didnt-read)) ([The Algorithmic Bridge, 2026-10-21](https://www.thealgorithmicbridge.com/p/put-some-brain-in-your-thinking)) ([The Algorithmic Bridge, 2026-04-21](https://www.thealgorithmicbridge.com/p/how-the-ai-writing-panic-is-making))

He mentions Pangram, a detection tool Substack partnered with, which claims a false positive rate of about 0.0041%. That figure is a claim, not a verified result. ([The Algorithmic Bridge, 2026-08-12](https://www.thealgorithmicbridge.com/p/on-substack-pangram-partnership-its))

## Table: who drives the conversation

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

Counts reflect how much each source publishes and quotes, not influence.

