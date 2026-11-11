# AI app & tool opportunities

From 26,923 findings extracted from a year of AI commentary (2025-11-11 to 2026-11-10), grouped into 785 themes. Generated 2026-11-11. Counts, quotes and links below come straight from the findings; the write-ups are Sonnet's.

## Cross-cutting observations

- Trust and control over agents dominate demand: sandboxing, permissions, identity, prompt injection and monitoring themes (T002, T005, T009, T011, T021, T022, T029, T049, T054) are high-scoring and repeat across 8-13 sources, but are fragmented across overlapping products.
- Cost and quota opacity is a daily pain: per-token prices mislead, subscription caps shift silently, and agent spend can't be attributed (T016, T023, T036, T044, T076). Users currently juggle subscriptions and manual tracking.
- The bottleneck has moved from generating code to verifying and comprehending it: review, debt, lost mental models and verification all show up (T017, T039, T032, T055, T062), mostly as pain points with few shipped answers.
- Memory, context and portability are unsolved: agents forget across sessions, compaction is lossy, and harnesses and models are vendor-locked, so people hand-maintain markdown files (T003, T013, T045, T012, T031).
- Evaluation is distrusted at every level: public benchmarks, LLM judges, harness variance and eval awareness all undermine results, while app teams find building their own evals hard (T018, T030, T046, T085, T014).
- Many highest-scoring themes are lab-facing or policy-facing (auditing, CoT monitoring, jailbreak scoring). They are hard for a small team to sell, so practical developer and prosumer tools are the better bets.

## Opportunities

### 1. AgentJail: cross-platform coding-agent sandbox with scoped permissions

**One-command sandbox that lets coding agents run in YOLO mode safely, with project-scoped mounts, egress control, credential proxying and rollback.**

*Confidence: high · 411 findings from 14 sources · pain point 189, tool or technique 95, build request 61, workaround 40, tool complaint 14, debate 12*

- **Problem:** Agents with broad shell and filesystem access delete files, wipe databases and leak secrets. Permission prompts are exhausting, so users approve everything. Existing sandboxes are fragmented and hard to set up.
- **Who:** Developers and small teams running Claude Code, Codex, Cursor and similar agents locally or on VPSs.
- **Evidence:** Three overlapping themes (T021: 86 findings, 13 build requests; T022: 96 findings, 10 build requests, 19 workarounds; T011: 118 findings) show repeated demand. Requests include 'OAuth for syscalls' scoped permissions, a sandboxed mode that skips prompts except for dangerous actions, and disposable-but-persistent dev environments. T021/T022 are lower in the last 90 days (0 and 6), so urgency may have plateaued while the problem remains.
- **Existing alternatives:** Docker/Podman, bubblewrap, firejail, sandbox-exec/Seatbelt, Agent Safehouse, Yolobox, smolvm/Era microVMs, Deno Sandbox, nono sandbox, Claude Code auto mode classifier, E2B, Daytona.
- **Gap:** Existing options are DIY, platform-specific and need security expertise. None combine deterministic permission policy, credential proxying, network egress rules and snapshot rollback in a one-command UX across macOS and Linux that works with any agent harness.
- **MVP:** A CLI wrapping any agent command in a container/microVM or Seatbelt profile, with a YAML policy (mounted paths, allowed domains, command deny list), a credential-injecting proxy so secrets never enter the sandbox, and git-snapshot rollback. Ship presets for Claude Code, Codex and Cursor CLI.
- **Why now:** YOLO mode and long unattended agent runs became normal, and incidents involving deleted files and wiped databases are widely discussed. Labs ship only model-side classifiers, which users find insufficient.
- **Risks:** Claude Code, Codex and OS vendors may ship native sandboxing. Many open-source competitors exist, so monetizing beyond open-source goodwill is hard. Isolation guarantees carry reputational risk if escapes occur.
- **Themes:** T021 Coding agents need sandboxing and scoped permissions; T022 Sandboxing coding agents to prevent destructive actions; T011 Sandboxes and runtime isolation for agent code; T002 Agents escape evaluation sandboxes and coordinate covertly

What people said:

> “spin up a sandbox in, you know, 100 millisecond, run a few commands and then like shut it down and like snapshot it” — Erik Bernhardsson, Latent Space, 2026-10-22 ([link](https://latent.space/p/modal-d/))
>
> “Can you clean my C: drive?” — AINews (smol.ai), 2026-10-08 ([link](https://latent.space/p/ainews-claude-haiku-55-better-than/))
>
> “We need to continue to figure out how to build better sandboxes and monitoring tools.” — Sam Altman, Don't Worry About the Vase, 2026-10-02 ([link](https://thezvi.substack.com/p/the-ai-preference-cascade-reaches))
>
> “The code in the packages appeared to be LLM-authored.” — Simon Willison, Simon Willison's Weblog, 2026-09-12 ([link](https://simonwillison.net/2026/Sep/12/openai-agents-rubygems/))
>
> “a slow uptake in the necessary hardening of our cyber infrastructure around the world” — Nathan Lambert, Interconnects, 2026-09-10 ([link](https://www.interconnects.ai/p/one-resignation-turned-the-embers))

### 2. AgentLedger: cost attribution, budgets and kill switch for agent spend

**A gateway and tracer that attributes LLM spend per agent, task and workflow step, forecasts it, and cuts off runaway agents.**

*Confidence: high · 250 findings from 13 sources · pain point 134, tool or technique 50, build request 36, tool complaint 13, workaround 13, debate 3, link shared 1*

- **Problem:** One user action can trigger many LLM calls via retries, loops and parallel agents, so spend is unpredictable, can't be attributed, and spikes surface only in production.
- **Who:** Teams running coding-agent fleets or multi-agent products, and finance or platform owners watching token spend.
- **Evidence:** T044 (56 findings, 8 build requests, 40 pain points, 8 sources) has explicit requests: tracking and forecasting spend for parallel runs costing tens of millions of tokens, and a tool that cuts off a runaway agent. T023 (68 findings, 35 in last 90 days) and T054 add guardrails that cap or halt cost anomalies.
- **Existing alternatives:** ccusage, Cloudflare AI Gateway budgets, thin tagging proxies, LangSmith, Langfuse, token-counting tools.
- **Gap:** Current tools report cost after the fact or per provider. They don't attribute spend to an agent, task or workflow step across providers, and don't enforce hard budgets or halt loops in real time.
- **MVP:** An OpenAI/Anthropic-compatible proxy that tags requests via headers or session IDs, rolls up cost per agent, task and user, and offers per-session budgets, retry-ratio alerts and an automatic kill switch. Include a Slack alert and a simple dashboard.
- **Why now:** Parallel and background agents became mainstream in 2026, making runaway spend a real operational risk, and teams increasingly route across many models.
- **Risks:** Observability vendors (LangSmith, Langfuse, Cloudflare) can add budgets. Gateway-in-path adds latency and trust concerns. Differentiation depends on enforcement and attribution quality.
- **Themes:** T044 Agent cost attribution, estimation and budget forecasting; T023 Cost per task is hidden behind per-token prices; T054 Permission scoping and policy gates for agent actions; T035 Agent trace viewers and observability tooling

What people said:

> “the plan yields about $15,000/month of Opus 5.5 but only about $3,000 of Fable 5.2” — theo, AINews (smol.ai), 2026-11-10 ([link](https://latent.space/p/ainews-fable-5-2-retakes-world-1-llm-spot-as-ant-ipo-roadshow-begins/))
>
> “A transcript of the agent’s final reply would miss most of what Steve Kelling and Nishant Ranka are evaluating.” — Steve Kelling, Latent Space, 2026-11-09 ([link](https://latent.space/p/handshake/))
>
> “Reservations are free and can be canceled later” — Zvi Mowshowitz, Don't Worry About the Vase, 2026-11-03 ([link](https://thezvi.substack.com/p/openai-updates-its-model-spec))
>
> “Five frontier models now sit within five points of each other in terms of intelligence, but their cost per unit differs by 3.8x.” — Tomasz Tunguz, Tomasz Tunguz, 2026-10-13 ([link](https://tomtunguz.com/intelligence-per-dollar-2026/))
>
> “My Claude Token Counter tool shows that the same long prompt uses around 1.25x as many tokens” — Simon Willison, Simon Willison's Weblog, 2026-10-07 ([link](https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/))

### 3. QuotaWatch: subscription usage and model transparency tracker

**A cross-provider tracker that normalizes usage caps, shows remaining quota, which model actually answered, and alerts on silent limit changes.**

*Confidence: medium · 361 findings from 12 sources · pain point 199, tool complaint 70, debate 28, tool or technique 28, build request 26, workaround 9, link shared 1*

- **Problem:** Paid subscribers to Claude, ChatGPT, Gemini, Perplexity and coding agents hit opaque and shifting caps, silent model swaps and misleading multipliers like '5x'/'20x', so value per subscription is unpredictable.
- **Who:** Heavy individual users and developers on Claude Code, Cursor, Codex and chat subscriptions, plus students.
- **Evidence:** T016 (91 findings, 8 sources, 60 pain points, 14 tool complaints), T036 (81 findings, 22 tool complaints), T076 (57 findings) and T053 all describe the problem. Specific asks include disclosing limits in API-budget terms, a way to opt out of silent model experiments, and a tool to use subscription quotas programmatically. Recency is mixed (T016 16, T036 6, T076 21 findings in last 90 days).
- **Existing alternatives:** ccusage, manual refresh and tracking, juggling multiple subscriptions, switching providers, Artificial Analysis charts for prices.
- **Gap:** No neutral tool normalizes quotas across plans, detects model downgrades, or warns before exhaustion. Providers have no incentive to be transparent.
- **MVP:** A browser extension plus local CLI that reads usage from the Claude Code, Codex and Cursor logs and web usage pages, shows remaining quota and burn rate, logs which model responded, and alerts when limits appear to change. Add an API-equivalent cost estimate per plan.
- **Why now:** Providers tightened and restructured caps repeatedly in 2026 (e.g., weekly limit cuts, new top tiers), driving visible user backlash.
- **Risks:** Depends on scraping unstable UIs and undocumented endpoints; providers may add native dashboards or block the access. Consumer willingness to pay is low, so keep the free tier cheap and consider affiliate or team features.
- **Themes:** T016 Opaque subscription limits and silent model swaps; T036 Usage limits and model costs drain agent budgets; T076 Opaque AI subscription usage caps and missing mid-tier plans; T023 Cost per task is hidden behind per-token prices; T053 Expensive frontier models push users toward cost-aware routing

What people said:

> “the plan yields about $15,000/month of Opus 5.5 but only about $3,000 of Fable 5.2” — theo, AINews (smol.ai), 2026-11-10 ([link](https://latent.space/p/ainews-fable-5-2-retakes-world-1-llm-spot-as-ant-ipo-roadshow-begins/))
>
> “Five frontier models now sit within five points of each other in terms of intelligence, but their cost per unit differs by 3.8x.” — Tomasz Tunguz, Tomasz Tunguz, 2026-10-13 ([link](https://tomtunguz.com/intelligence-per-dollar-2026/))
>
> “My Claude Token Counter tool shows that the same long prompt uses around 1.25x as many tokens” — Simon Willison, Simon Willison's Weblog, 2026-10-07 ([link](https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/))
>
> “Anthropic indefinitely rolls back disallowing programmatic use” — Don't Worry About the Vase, 2026-06-18 ([link](https://thezvi.substack.com/p/ai-173-ai-pauses))
>
> “but it uses 6x the normal amount of usage” — Ben Tossell, Ben's Bites, 2026-10-01 ([link](https://www.bensbites.com/p/openai-devday-2026))

### 4. Cost-per-task model evaluator and router

**Benchmark your own prompts across models and effort levels on cost, latency and quality, then route each task to the cheapest adequate model.**

*Confidence: high · 512 findings from 15 sources · tool or technique 176, pain point 156, workaround 59, build request 43, debate 39, tool complaint 38, link shared 1*

- **Problem:** Per-token prices mislead because reasoning models burn more tokens and tokenizers differ. Teams struggle to pick the cheapest adequate model, and subagents inherit premium models by default.
- **Who:** Developers and startups with meaningful LLM spend and agent builders running multi-model stacks.
- **Evidence:** Routing and cost themes recur: T008 (133 findings, 17 build requests, 23 workarounds), T023 (68 findings, 35 in last 90 days), T053, T078, T072 and T031. Requests include a router that picks effort from request and remaining budget, a tool reporting cost per task and intelligence per dollar, and per-task token burn tracking across effort settings.
- **Existing alternatives:** OpenRouter, Factory Router, Cursor Router, Sakana Fugu, Artificial Analysis charts, prompt caching, Cloudflare AI Gateway.
- **Gap:** Routers exist but are generic and opaque. Nobody offers an easy bake-off on your own prompts that outputs a cost-quality frontier and then drives routing rules from it, with per-subagent model settings and failover.
- **MVP:** Upload 20-100 real prompts or a trace sample, run across chosen models and effort tiers, grade with a calibrated judge or user rubric, and output a cost/latency/quality table. Then export a routing config or an OpenAI-compatible proxy that applies it.
- **Why now:** Many models sit close on the pareto frontier at very different prices, and effort/thinking settings added a new axis users must tune by hand.
- **Risks:** OpenRouter and the labs may add smart routing. Aggregator margins are being squeezed (T078). Quality grading is hard. Evaluation is a one-off use unless routing is sticky.
- **Themes:** T008 Model routing and cost-aware delegation; T023 Cost per task is hidden behind per-token prices; T053 Expensive frontier models push users toward cost-aware routing; T078 Cost-optimizing model routing and cheaper inference; T072 Choosing, combining and switching models by task; T031 Frontier model churn, deprecations and vendor lock-in; T067 Subagent fan-out and delegation patterns

What people said:

> “the plan yields about $15,000/month of Opus 5.5 but only about $3,000 of Fable 5.2” — theo, AINews (smol.ai), 2026-11-10 ([link](https://latent.space/p/ainews-fable-5-2-retakes-world-1-llm-spot-as-ant-ipo-roadshow-begins/))
>
> “do they have routing built in?” — sid1992, Hacker News — Ask HN, 2026-11-01 ([link](https://news.ycombinator.com/item?id=50325635))
>
> “You can do like best of N as a type of like multi-agent strategy.” — Katelyn Lesse, Latent Space, 2026-10-27 ([link](https://latent.space/p/opus55/))
>
> “Five frontier models now sit within five points of each other in terms of intelligence, but their cost per unit differs by 3.8x.” — Tomasz Tunguz, Tomasz Tunguz, 2026-10-13 ([link](https://tomtunguz.com/intelligence-per-dollar-2026/))
>
> “My Claude Token Counter tool shows that the same long prompt uses around 1.25x as many tokens” — Simon Willison, Simon Willison's Weblog, 2026-10-07 ([link](https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/))

### 5. Portable agent memory layer (open, inspectable, cross-agent)

**A vendor-neutral memory store that extracts, dedupes, prunes and serves memories to any coding or personal agent, with a UI to see and edit them.**

*Confidence: high · 357 findings from 16 sources · pain point 145, tool or technique 110, build request 53, workaround 40, debate 6, tool complaint 3*

- **Problem:** Agents forget across sessions; hand-maintained AGENTS.md/MEMORY.md files go stale or bloat. Vendor memory is locked in, noisy, and invisible to users.
- **Who:** Developers using several coding agents across repos, plus power users of personal agents.
- **Evidence:** T003 (139 findings, 12 sources, 27 build requests, 47 pain points) and T045 (65 findings, 23 workarounds) plus T013 and T049. Requests: editable visible memory, shared persistent memory for multiplayer agents, memory that records why changes were rejected, and automatic briefing of new sessions. T003 has only 43 findings in last 90 days, so demand is steady but not surging.
- **Existing alternatives:** AGENTS.md/MEMORY.md, Claude-Mem, Letta Code, Cline memory banks, Mimir, MemMachine, Hyperspell, Supermemory, Honcho, Cognition's open memory format.
- **Gap:** Most are tied to one harness or are developer-API products with no user-facing inspection. Self-auditing (pruning conflicting or stale items), scoping per repo/team and portability across Claude Code, Codex and Cursor are weak.
- **MVP:** A local MCP server backed by a git-tracked markdown+SQLite store. It captures learnings from session transcripts, dedupes and consolidates nightly, flags stale or conflicting entries, serves relevant memories on session start, and offers a simple web UI to browse and edit. Support Claude Code, Codex and Cursor via MCP/hooks.
- **Why now:** Memory features are shipping inside vendor products (lock-in worry), and Cognition open-sourced a git/markdown memory format, which signals a de facto standard may emerge.
- **Risks:** Labs are building native memory and will ship it by default. Crowded space with many startups. Quality of automatic extraction is hard to prove, and standards may fragment further.
- **Themes:** T003 Portable, persistent, editable agent memory; T045 Agents lose context and memory across sessions; T013 Context loss and compaction in long agent sessions; T049 Agent identity, permissions and governance

What people said:

> “Where does it look to find out why the team rejected this same change six months ago?” — Mihail Eric, Latent Space, 2026-11-08 ([link](https://latent.space/p/cs146s/))
>
> “I would absolutely not allow agents to authorize any transactions until I could verify the status and nature of those agents.” — Zvi Mowshowitz, Don't Worry About the Vase, 2026-10-23 ([link](https://thezvi.substack.com/p/the-hackening))
>
> “open-sourcing the git- and markdown-backed format as Agent Memory Repo” — AINews (smol.ai), 2026-10-06 ([link](https://latent.space/p/ainews-reflection-beam-501b-a23b/))
>
> “you don’t see by default what these agents remember about you, or what context they have” — Ben Tossell, Ben's Bites, 2026-09-15 ([link](https://www.bensbites.com/p/good-luck-slowing-this-down))
>
> “any LLM system that uses compaction needs to both preserve the pre-compacted text” — Simon Willison, Simon Willison's Weblog, 2026-09-12 ([link](https://simonwillison.net/2026/Sep/12/astra-running-routes/))

### 6. ReviewLens: risk-aware review of agent-written PRs

**Groups and explains large agent diffs, flags risky changes and architectural drift, and supports auto-approval thresholds for low-risk changes.**

*Confidence: medium · 375 findings from 11 sources · pain point 188, tool or technique 90, workaround 42, build request 28, debate 15, tool complaint 11, link shared 1*

- **Problem:** Agents generate PRs faster than humans can review. Large diffs, long PR descriptions and noisy AI review comments cause fatigue, rubber-stamping and anxiety.
- **Who:** Engineering teams and reviewers handling agent-written code.
- **Evidence:** T017 (102 findings, 38 in last 90 days, 55 pain points) and T039 (78 findings, 32 pain points, 12 build requests), plus T032 and T055. Requests: tools to understand agent diffs well enough to review, graph-based codebase understanding with specs, stacked diffs and merge queues, and better PR context.
- **Existing alternatives:** CodeRabbit, Copilot reviewer, Cursor Bugbot, Devin Review, Claude Code /review, Kilo, Rovo, SonarQube, pr.video, pyor.review.
- **Gap:** Current tools add more comments rather than lowering reviewer burden. Few group diffs by intent, run the code, surface the decisions a human must make, or calibrate risk to approve safe changes automatically.
- **MVP:** A GitHub app that, for each PR, clusters changes by intent, produces a short decision-first summary (what changed, what decisions need human judgment, what was tested), scores risk by touched areas (auth, schema, deps), and posts a checklist. Start with summaries and risk labels, then add repo-convention checks.
- **Why now:** Review has become the new bottleneck as agent usage scaled, and vendors (Devin Review, Bugbot) are validating the category.
- **Risks:** This is the most crowded category here: GitHub, Cursor, Cognition and CodeRabbit are all in it. A small team needs a sharp angle (e.g., risk-gated auto-approval or conventions fit) or niche focus. Trust in false positives is hard to earn.
- **Themes:** T017 Reviewing AI-generated code and PRs is the bottleneck; T039 Human review can't keep up with AI-generated PRs; T032 Agent code fails to fit codebases and piles up debt; T055 Losing comprehension and skill with AI-written code; T062 Verifying AI-written code without human review

What people said:

> “When code review becomes the bottleneck” — Latent Space, 2026-11-08 ([link](https://latent.space/p/one_million_ai_engineer_special_how_stanford_teaches_ai-native_engineering_mihail_eric_monaco/))
>
> “if you have a setup that gives you memory, specs and a graph-based understanding (that part is key)” — hey-hey, Hacker News — Ask HN, 2026-10-02 ([link](https://news.ycombinator.com/item?id=49934037))
>
> “Command Center as a code review layer for AI diffs” — earlysignalsvc, AINews (smol.ai), 2026-07-28 ([link](https://news.smol.ai/issues/26-07-28-not-much/))
>
> “I expect this is where the good old fashioned usability testing comes in.” — Simon Willison, Simon Willison's Weblog, 2026-04-02 ([link](https://simonwillison.net/2026/Apr/2/lennys-podcast/))
>
> “PR descriptions need to carry the context” — Ben Tossell, Ben's Bites, 2026-01-08 ([link](https://www.bensbites.com/p/dr-chatgpt-will-see-you-now))

### 7. Agent firewall: prompt-injection and tool-call policy proxy

**A deterministic proxy between agent and tools that scopes capabilities, scans ingested content, gates risky action combinations, and offers a remote kill switch.**

*Confidence: high · 391 findings from 16 sources · pain point 230, build request 74, tool or technique 44, workaround 25, debate 15, tool complaint 3*

- **Problem:** LLMs can't separate instructions from untrusted data, so injected text hijacks agents. Classifier defenses are bypassable, and teams can't scope, audit or revoke what tools agents invoke.
- **Who:** Teams building or deploying tool-using agents, especially with write access to email, repos, or production systems.
- **Evidence:** T009 (96 findings, 63 pain points), T005 (98 findings, 23 build requests, 11 sources), T054 (50 findings), T041 (49 findings, 32 in last 90 days) and T029. Requests: deterministic symbolic control instead of LLM judgment, a proxy scanning tool calls before execution, hard control layers, and fine-grained permissions with escalation. Only 10% of builders say security tooling delivers the most value today (T009).
- **Existing alternatives:** Runlayer, safeagents proxy, llmtrace firewall, BrowseSafe, Panther event mapping, MCP audit trails, human-in-the-loop approvals, URL allowlisting, auto-mode classifiers.
- **Gap:** Existing offerings are early or classifier-based. A framework-agnostic, deterministic policy layer (taint tracking, action-combination limits like 'read private data + external send') with audit logs and a simple policy language is missing.
- **MVP:** An MCP/HTTP tool-call proxy with YAML policies: per-agent allowlists, taint rules blocking 'untrusted-content then external-write' chains, spend/rate caps, human-approval hooks for specified actions, a full audit log, and a kill switch. Ship with an open injection test suite.
- **Why now:** Agents increasingly hold email, repo and production access, and incidents and papers show classifier defenses are permeable, shifting the conversation toward deterministic controls.
- **Risks:** Labs and platforms (Anthropic, OpenAI, Cloudflare, Runlayer) will build part of this. Security buyers need proof and certifications. Hard to demonstrate efficacy, and false positives frustrate developers.
- **Themes:** T009 Prompt injection hijacks tool-using agents; T005 Agent tool-call governance, identity and oversight; T054 Permission scoping and policy gates for agent actions; T041 Agent deception, collusion and attack risks; T029 Real-time monitoring of internal and deployed AI agents; T068 Human-in-the-loop approval and escalation for agents

What people said:

> “Reservations are free and can be canceled later” — Zvi Mowshowitz, Don't Worry About the Vase, 2026-11-03 ([link](https://thezvi.substack.com/p/openai-updates-its-model-spec))
>
> “a proxy that scans tool calls before they execute” — @yb2698, AINews (smol.ai), 2026-10-31 ([link](https://latent.space/p/ainews-google-admits-ai-mode-hurts-search-revenue-15-500b-drop-worst-since-2004-ipo-ai-bear-market-c/))
>
> “"building the trust layer for the agents."” — Keon Shahab, Latent Space, 2026-10-14 ([link](https://latent.space/p/crossing-the-threshold/))
>
> “Only 10% say security tooling delivers the most value today.” — Tomasz Tunguz, Tomasz Tunguz, 2026-10-13 ([link](https://tomtunguz.com/ai-in-practice-survey-2026/))
>
> “asking criminals to file monthly reports” — Gary Marcus, Marcus on AI, 2026-10-10 ([link](https://garymarcus.substack.com/p/we-must-recall-open-ended-ai-agents))

### 8. Agent trace debugger: summarize, cluster and replay runs

**Trace-first debugging that samples huge agent traces, clusters failures, replays steps and compares runs with linked evidence.**

*Confidence: medium · 284 findings from 15 sources · tool or technique 111, pain point 102, build request 33, workaround 31, tool complaint 4, debate 3*

- **Problem:** Agents fail silently, traces are huge and hard to inspect, and dashboards aren't actionable. Teams can't tell why an agent broke or whether a change helped.
- **Who:** Developers building and debugging production agents.
- **Evidence:** T035 (76 findings, 9 sources, 36 tool_or_technique, 10 build requests), T050 (71 findings, 38 in last 90 days) and T029. Requests include inspecting the full tool-call trace (files read, shell history) rather than grading final replies, bulk export APIs with annotation write-back, and understanding opaque reasoning.
- **Existing alternatives:** LangSmith, Langfuse, Arize Phoenix, Raindrop, claude-devtools, Agentsview, Cloudflare Agent Tracing, Claude OTel traces.
- **Gap:** Existing platforms store traces but make users read them manually. Automatic failure clustering, trace summarization, diffing of runs and trace-to-eval conversion are thin, and bulk export is clumsy.
- **MVP:** A local-first viewer ingesting Claude Code/Codex session logs and OpenTelemetry traces, with LLM-generated per-run summaries, failure clustering across runs, side-by-side run diff, and one-click export of failing traces into eval cases.
- **Why now:** Agent logs from coding harnesses are now readily available and long-horizon runs created trace volumes that manual inspection can't handle.
- **Risks:** Well-funded incumbents (LangSmith, Langfuse, Arize) add features quickly. Open-source local viewers may cap willingness to pay.
- **Themes:** T035 Agent trace viewers and observability tooling; T050 Harness evaluation and self-improving agent loops; T029 Real-time monitoring of internal and deployed AI agents; T025 Long-horizon agents drift and need supervision

What people said:

> “A transcript of the agent’s final reply would miss most of what Steve Kelling and Nishant Ranka are evaluating.” — Steve Kelling, Latent Space, 2026-11-09 ([link](https://latent.space/p/handshake/))
>
> “we're working on making it harder to spin up unmonitored inference” — Marcus Williams, Don't Worry About the Vase, 2026-10-21 ([link](https://thezvi.substack.com/p/misaligned))
>
> “the escalation agent determines whether the breach should have occurred & fixes it or blesses the exception.” — Jeanne DeWitt Grosser, Tomasz Tunguz, 2026-10-06 ([link](https://tomtunguz.com/how-to-automate-inbound/))
>
> “can intercept tool calls before execution” — @noahrshinn, AINews (smol.ai), 2026-09-24 ([link](https://latent.space/p/ainews-meta-connect-2026-muse-glasses/))
>
> “APIs that let you write annotations back efficiently.” — Shreya Shankar, Hamel Husain, 2026-09-18 ([link](https://hamel.dev/blog/posts/evals-faq/))

### 9. Context safeguard for long agent sessions

**A layer that archives raw pre-compaction context, pins critical instructions, checkpoints state and sanitizes summaries so long runs don't drift.**

*Confidence: medium · 395 findings from 17 sources · pain point 163, tool or technique 124, workaround 52, build request 43, debate 7, tool complaint 6*

- **Problem:** Compaction is lossy: it drops instructions and state, summaries can carry injected instructions, and agents repeat mistakes or forget confirm-before-acting rules.
- **Who:** Developers and teams running long coding and general agents.
- **Evidence:** T013 (105 findings, 12 sources, 53 pain points, 36 tool_or_technique) and T025 (86 findings, 13 sources). Requests: preserve pre-compacted text and expose it via tool calls, a consolidation pass saving lasting preferences before wiping the session, and reliable confirm-before-acting after compaction. Only 23 findings in last 90 days.
- **Existing alternatives:** Codex and Claude Code built-in compaction, summarizing state to files and restarting, notes on filesystem, subagent isolation, Ralph loops, RLM-style decomposition.
- **Gap:** Everyone hand-rolls it. No portable tool pins invariant instructions, keeps searchable raw transcripts after compaction, and sanitizes summaries across harnesses.
- **MVP:** A hook/MCP package for Claude Code and Codex that stores full transcripts before compaction, exposes a 'recall' tool to search them, re-injects a pinned instruction block after compaction, and runs a pre-wipe pass saving durable preferences to notes.
- **Why now:** Long-running, unattended agents are now routine, and labs are adding managed compaction, which shows the problem is acknowledged but not fully solved.
- **Risks:** Harness vendors will likely absorb this natively (managed compaction is already shipping). Best merged with the memory product rather than standalone.
- **Themes:** T013 Context loss and compaction in long agent sessions; T003 Portable, persistent, editable agent memory; T045 Agents lose context and memory across sessions; T025 Long-horizon agents drift and need supervision

What people said:

> “Where does it look to find out why the team rejected this same change six months ago?” — Mihail Eric, Latent Space, 2026-11-08 ([link](https://latent.space/p/cs146s/))
>
> “open-sourcing the git- and markdown-backed format as Agent Memory Repo” — AINews (smol.ai), 2026-10-06 ([link](https://latent.space/p/ainews-reflection-beam-501b-a23b/))
>
> “you don’t see by default what these agents remember about you, or what context they have” — Ben Tossell, Ben's Bites, 2026-09-15 ([link](https://www.bensbites.com/p/good-luck-slowing-this-down))
>
> “any LLM system that uses compaction needs to both preserve the pre-compacted text” — Simon Willison, Simon Willison's Weblog, 2026-09-12 ([link](https://simonwillison.net/2026/Sep/12/astra-running-routes/))
>
> “Does Grok Bot or your chat assistant perform this sleep cycle automatically? Not today.” — Tomasz Tunguz, Tomasz Tunguz, 2026-08-24 ([link](https://tomtunguz.com/how-long-should-an-agent-live/))

### 10. EvalStarter: eval datasets from production traces with calibrated judges

**Turn production traces into a balanced eval set, surface likely failures for labeling, and calibrate LLM judges against human labels.**

*Confidence: medium · 339 findings from 17 sources · pain point 155, tool or technique 98, build request 44, debate 18, workaround 15, tool complaint 8, link shared 1*

- **Problem:** App teams lack skill and tooling to build representative evals because real failures are rare and synthetic ones unrealistic. LLM judges are biased and rarely validated.
- **Who:** Application teams building LLM products without dedicated eval engineers.
- **Evidence:** T030 (77 findings, 11 sources, 13 build requests), T085 (48 findings), T018 (79 findings, 12 sources, 11 build requests) and T046. Quotes include 'the skill of building evals is the bottleneck more than the tooling', requests to turn traces and human feedback into evals, and a skills plugin to review eval pipelines. Build requests also cover a personal arena for comparing prompts and models.
- **Existing alternatives:** Promptfoo, Braintrust, Langfuse, Arize Phoenix, DeepEval, Inspect AI, Hamel Husain's eval skills.
- **Gap:** Platforms assume you already know what to evaluate. The data-curation step (sampling traces, active learning, labeling UX) and judge calibration (TPR/TNR, kappa against human labels) are still left to the user.
- **MVP:** Connect a trace source (Langfuse/OpenTelemetry/log files), cluster and sample traces, present a fast binary pass/fail labeling UI, auto-propose judge prompts, report agreement with human labels and bias checks (order swap), and export to Promptfoo/Inspect format.
- **Why now:** Eval-driven development is now accepted best practice, yet commentary repeatedly says skill, not tooling, is the blocker.
- **Risks:** Incumbent eval platforms may add labeling and calibration. Buyers are mostly teams that already pay for an observability platform. Judge quality varies by domain.
- **Themes:** T030 Building eval datasets and custom evals is hard; T085 LLM-as-judge is biased and needs calibration; T018 Public benchmarks don't predict real-world performance; T046 Eval harness and setup variance make results incomparable; T035 Agent trace viewers and observability tooling

What people said:

> “A transcript of the agent’s final reply would miss most of what Steve Kelling and Nishant Ranka are evaluating.” — Steve Kelling, Latent Space, 2026-11-09 ([link](https://latent.space/p/handshake/))
>
> “APIs that let you write annotations back efficiently.” — Shreya Shankar, Hamel Husain, 2026-09-18 ([link](https://hamel.dev/blog/posts/evals-faq/))
>
> “I would urge him to read agidefinition.AI” — Gary Marcus, Marcus on AI, 2026-09-06 ([link](https://garymarcus.substack.com/p/sad-to-see-jensen-huang-claim-that))
>
> “turning traces and human feedback into task specs” — Vtrivedy10, AINews (smol.ai), 2026-08-24 ([link](https://news.smol.ai/issues/26-08-25-not-much/))
>
> “it takes a long time for customers to build really high-quality evals” — Cat Wu, Simon Willison's Weblog, 2026-07-21 ([link](https://simonwillison.net/2026/Jul/21/cat-and-thariq/))

### 11. Provider-neutral agent harness with cross-model review loops

**A thin open harness that works across Claude, Codex, local and open models, with planner/implementer/reviewer roles and escalation when an agent loops.**

*Confidence: medium · 518 findings from 16 sources · tool or technique 242, pain point 116, workaround 66, build request 48, debate 26, tool complaint 18, link shared 2*

- **Problem:** Harnesses are vendor-locked, switching models is painful, and open or local models misuse tools and lose context in harnesses tuned for frontier models.
- **Who:** Developers using multiple coding models, and those wanting local or open-weight agents.
- **Evidence:** T012 (122 findings, 10 sources), T072 (68 findings, 23 workarounds), T070 (67 findings), T031 and T008. Requests: unified interface for switching between Codex, Claude and Cursor, a coding harness for local models with queue management and subagents, easy switching because subscription pricing may change. Developers cut off from API access after an acquisition illustrate dependency risk.
- **Existing alternatives:** OpenCode, Pi, Cline SDK, Crush, Conductor, Hermes, Mistral Vibe, Kimi CLI, OpenHands, Qwen Code, Vercel AI SDK, OpenRouter.
- **Gap:** Many harnesses exist, but they are opinionated or tuned to one model family. Local-model-tuned behaviors (small prompts, tool-use repair, compaction, queueing) and structured cross-model review loops are underdeveloped.
- **MVP:** A wrapper or plugin for an existing open harness (e.g., OpenCode/Pi) adding model profiles with per-model prompt and tool-call fixups, a plan-with-model-A/implement-with-model-B/review-with-model-C workflow, and automatic escalation when loops are detected.
- **Why now:** Open-weight models (Kimi, Qwen) became viable for agentic coding and prices and limits on frontier subscriptions keep shifting.
- **Risks:** Crowded space where the open-source community moves fast, and a differentiated value proposition is hard to hold. Monetization is unclear.
- **Themes:** T012 Provider-agnostic harnesses and unified model interfaces; T072 Choosing, combining and switching models by task; T070 Open-source and local models need better agent harnesses; T031 Frontier model churn, deprecations and vendor lock-in; T067 Subagent fan-out and delegation patterns; T008 Model routing and cost-aware delegation

What people said:

> “do they have routing built in?” — sid1992, Hacker News — Ask HN, 2026-11-01 ([link](https://news.ycombinator.com/item?id=50325635))
>
> “You can do like best of N as a type of like multi-agent strategy.” — Katelyn Lesse, Latent Space, 2026-10-27 ([link](https://latent.space/p/opus55/))
>
> “route each task to the best backend” — @elonmusk, AINews (smol.ai), 2026-10-08 ([link](https://latent.space/p/ainews-claude-haiku-55-better-than/))
>
> “An open-source version of Grok Bot.” — Ben's Bites, 2026-08-20 ([link](https://www.bensbites.com/p/simple-agents))
>
> “a cheap model or router could choose the mode from the request, tool state, and remaining time or token budget” — Sebastian Raschka, Ahead of AI, 2026-07-18 ([link](https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms))

### 12. Parallel-agent control plane

**A harness-agnostic dashboard for status, summaries, notification triage and review queues across many concurrent coding agents.**

*Confidence: medium · 371 findings from 15 sources · pain point 136, tool or technique 110, build request 53, workaround 47, debate 20, tool complaint 3, link shared 2*

- **Problem:** Developers running many parallel agents lose track of branches, diffs and status, suffer context-switching and notification overload, and review costs rival doing the work.
- **Who:** Developers running parallel Claude Code, Codex or Cursor sessions on one or more repos.
- **Evidence:** T010 (108 findings, 12 sources, 18 build requests, 15 workarounds), with T043 (59 findings) covering the burnout from juggling agents and T033 background agents. Requests include a window manager for concurrent sessions with notifications based on hooks and PR status, a calendar view of scheduled agent runs, and tools for supervising many concurrent agents.
- **Existing alternatives:** Emdash, Vibe Kanban, Conductor, Superset, tmux/worktrees, Claude Agent Teams, Warp Oz.
- **Gap:** Existing tools are tied to one workflow or are early. Notification triage ('what needs me now'), unified review queue and summary of long sessions across harnesses remain weak.
- **MVP:** A local app that hooks into Claude Code/Codex session events and git worktrees, shows a kanban/status list per agent with one-line summaries, color-coded 'needs input / done / failed' states, desktop notifications for only the important ones, and a review queue linking diffs.
- **Why now:** Parallel agents became mainstream practice and Claude Agent Teams and similar features increased concurrency, but only 26 of its findings are in last 90 days, so interest may be plateauing as vendors ship their own UIs.
- **Risks:** Vendors (Anthropic, OpenAI, Cursor, Warp) are shipping native multi-agent UIs, and many open-source entrants exist. Likely a free or tiny-market product.
- **Themes:** T010 Dashboards for supervising many parallel agents; T043 Burnout, overload and addiction from parallel AI agents; T033 Scheduled, always-on and background agents; T025 Long-horizon agents drift and need supervision; T068 Human-in-the-loop approval and escalation for agents

What people said:

> “Background agents and Stripe’s Minions” — Latent Space, 2026-11-08 ([link](https://latent.space/p/one_million_ai_engineer_special_how_stanford_teaches_ai-native_engineering_mihail_eric_monaco/))
>
> “I had it build a window manager with notifications and color coding based on session hooks and git issue/PR status.” — PippaSedai, Hacker News — Ask HN, 2026-10-30 ([link](https://news.ycombinator.com/item?id=50301479))
>
> “write code and run multi-day experiments, hundreds at a time” — @mirendil, AINews (smol.ai), 2026-10-29 ([link](https://latent.space/p/ainews-gemini-4-carbon/))
>
> “I think up next I’ll add a calendar view where I can see the automations my agents run…” — Ben Tossell, Ben's Bites, 2026-10-20 ([link](https://www.bensbites.com/p/how-i-built-my-everything-app))
>
> “Voice agents have to reach humans over someone's network” — Tomasz Tunguz, Tomasz Tunguz, 2026-08-11 ([link](https://tomtunguz.com/a-winner-in-every-category/))

### 13. Writing voice guardian: critique-only editor that strips AI tells

**An editing layer that learns your voice, critiques rather than rewrites, enforces density rules and flags AI tics and padding.**

*Confidence: medium · 295 findings from 14 sources · pain point 149, tool complaint 42, workaround 32, build request 30, tool or technique 29, debate 13*

- **Problem:** AI prose is bland, padded and formulaic, with recognizable tics. Writers burn effort rewriting and fighting style via prompts, and custom instructions don't stick.
- **Who:** Writers, editors, newsletter authors and professionals drafting with LLMs.
- **Evidence:** T015 (93 findings, 9 sources, 15 tool complaints, 15 workarounds), T019 (85 findings, 24 tool complaints), T066 (45 findings) and T024. Requests: a plugin that interviews the writer and critiques drafts, models that check their own style constraints, humanizing tools, and removing the 'it's not A, it's B' tell. T019 has just 6 findings in last 90 days.
- **Existing alternatives:** Strict system prompts, style guides, second-agent graders, Kagi proofread, ChatGPT/Claude instead of Grammarly, Pangram for detection.
- **Gap:** People rebuild style linters ad hoc. A persistent, personal style profile with a deterministic tell-detector and critique-only mode across models isn't a ready product.
- **MVP:** A web app or browser/Obsidian plugin: paste a draft, get a critique listing AI tells (configurable patterns), padding and density scores, and suggestions tied to a voice profile built from the user's past writing. No automatic rewriting by default, plus an export as a reusable style-guide prompt.
- **Why now:** Writers increasingly use LLMs for drafts and see 'AI slop' backlash in communities, making style enforcement a visible pain.
- **Risks:** Labs improve tone and add style controls; Grammarly-style incumbents can add features. Writers' willingness to pay is modest, and pattern lists go stale as models change.
- **Themes:** T015 AI writing is generic, bloated and loses personal voice; T019 Chatbot tone, sycophancy and style control; T066 AI-padded messages and docs flood recipients; T024 Filtering AI slop from feeds, search and forums

What people said:

> “removing the "it's not A, it is B" tell would be rather simple and involve a modification of the system prompt” — stuxnet79, Hacker News — Ask HN, 2026-10-29 ([link](https://news.ycombinator.com/item?id=50284849))
>
> “it has yet to be effectively productized but can you imagine how great it would be to be able to steer your LLM responses” — Chelsea Sierra Voss, Don't Worry About the Vase, 2026-10-14 ([link](https://thezvi.substack.com/p/the-safety-culture-at-the-labs-is))
>
> “A writing plugin that interviews you, critiques drafts and saves what you learn.” — Ben's Bites, 2026-09-08 ([link](https://www.bensbites.com/p/the-first-gpt-6-model))
>
> “Too much AI & the piece loses its musicality to a clanker’s monotonous internal tune.” — Tomasz Tunguz, Tomasz Tunguz, 2026-08-03 ([link](https://tomtunguz.com/ai-ghost-writing/))
>
> “If Substack supports a feature like “only users with a paid subscription somewhere on the platform can engage,” I’d implement it.” — Nathan Lambert, Interconnects, 2026-06-17 ([link](https://www.interconnects.ai/p/state-of-the-blog-mid-2026))

### 14. Hosted always-on agents with schedules and event triggers

**Cloud runtime that runs recurring and event-triggered agent jobs when your laptop is closed, with chat or Slack delivery and safe defaults.**

*Confidence: medium · 271 findings from 14 sources · tool or technique 105, build request 68, pain point 61, workaround 25, link shared 6, tool complaint 4, debate 2*

- **Problem:** Scheduled agent tasks stop when laptops close. Teams want cloud-hosted proactive agents running on schedules or events, and non-technical users find personal agents hard to host.
- **Who:** Individuals, small teams and developers with recurring agent work (briefings, triage, maintenance).
- **Evidence:** T033 (71 findings, 17 build requests, 27 in last 90 days), T038 (71 findings), T069 (39 findings, 15 build requests) and T060 (44 findings, 15 build requests). Requests: infrastructure for background coding agents like Stripe's Minions, tools to automate recurring agent work, background agent products on open and closed models, and agents that track tasks across Gmail and calendar.
- **Existing alternatives:** Claude Code Routines, Devin scheduling, cron jobs, heartbeat loops, Sentry-triggered agents, OpenClaw on Mac minis, Hermes Agent, Zo Computer, Tasklet, Notion Custom Agents.
- **Gap:** Scheduling features are tied to one vendor, while DIY setups require servers and configuration. A model-agnostic, safe-by-default runtime with integrations and a simple UI isn't mature.
- **MVP:** Pick one narrow job, such as a daily email/newsletter/calendar chief-of-staff brief or a PR/issue triage agent, running on a schedule with bring-your-own-key, OAuth connectors, per-run logs and an approval step before any write action.
- **Why now:** Personal agents like OpenClaw showed demand but also setup pain, and vendors only recently added routines and scheduling.
- **Risks:** Anthropic, OpenAI, Notion and Microsoft are all moving in this direction. Retention for personal agents is weak (T069), and security exposure from broad OAuth access is significant. Needs a narrow wedge.
- **Themes:** T033 Scheduled, always-on and background agents; T038 Personal agents are hard to set up and manage; T069 Personal agent setup and always-on assistants; T060 Proactive agents for tasks and life admin; T077 Filtering information feeds and AI news overload

What people said:

> “build prototypes for workers to better navigate constantly-evolving AI capabilities” — Sayash Kapoor, Rishi Bommasani, Arvind Narayanan, AI as Normal Technology, 2026-11-10 ([link](https://www.normaltech.ai/p/the-missing-quadrant-in-responses))
>
> “Background agents and Stripe’s Minions” — Latent Space, 2026-11-08 ([link](https://latent.space/p/one_million_ai_engineer_special_how_stanford_teaches_ai-native_engineering_mihail_eric_monaco/))
>
> “write code and run multi-day experiments, hundreds at a time” — @mirendil, AINews (smol.ai), 2026-10-29 ([link](https://latent.space/p/ainews-gemini-4-carbon/))
>
> “build a tool that each day goes through all newsletters I'm subscribed to” — Colossus, Ben's Bites, 2026-10-29 ([link](https://www.bensbites.com/p/ai-is-overwhelming-and-im-doing-it))
>
> “get me my domain back from this cruddy website” — Nathan Lambert, Interconnects, 2026-10-25 ([link](https://www.interconnects.ai/p/podcast-kimi-k31-pro-the-new-cyber))

### 15. Open-weight-friendly cyber defense stack

**Verified-defender access and self-hostable security tooling so incident responders aren't blocked by frontier-model refusals.**

*Confidence: low · 267 findings from 14 sources · pain point 144, tool or technique 39, build request 33, tool complaint 18, workaround 14, debate 14, link shared 5*

- **Problem:** Hosted frontier models refuse forensics, incident response and code hardening, pushing defenders to self-hosted open models. Access policies for dual-use are contested.
- **Who:** Security defenders, incident responders, SOC teams and security researchers.
- **Evidence:** T006 (112 findings, 12 workarounds, 9 tool complaints, 10 sources). Requests: gated access for vetted professionals, tools letting defenders use strong models, and inference-layer transparency during incidents. T007 (105 findings, 47 in last 90 days) shows defenders also facing a flood of AI-found vulnerabilities.
- **Existing alternatives:** Self-hosted GLM and fine-tuned open models, trusted-access programs with ID verification, Project Glasswing, exemption applications, Claude Security, Codex Security.
- **Gap:** Trusted-access programs are lab-controlled and slow, while self-hosting requires expertise. Few packaged defender-focused model stacks with prompts, evaluation and refusal-tuning exist.
- **MVP:** An open-source packaged stack (inference server, tuned open model config, forensic/IR prompt library and tool integrations for logs and pcap) plus a benchmark of refusal rates on defender tasks against hosted models.
- **Why now:** Labs introduced cyber safeguards and trusted-access programs, while open models reached capability parity for many defensive tasks.
- **Risks:** Security buyers need credibility and procurement support. Labs are expanding verified programs, shrinking the gap. Dual-use liability concerns.
- **Themes:** T006 Cyber safeguards block legitimate defenders; T007 AI-found vulnerabilities outpace triage and patching; T057 Safety filters over-refuse and block legitimate use

What people said:

> “948 Linux privilege escalation vulnerabilities” — AINews (smol.ai), 2026-11-06 ([link](https://latent.space/p/ainews-inkling-2-small-17a-594b-trained-in-68-hours-on-12t-tokens-beating-muse-spark/))
>
> “buying enough compute, & converting it into enough defensive tokens” — Tomasz Tunguz, Tomasz Tunguz, 2026-11-06 ([link](https://tomtunguz.com/a-90-dollar-key-into-your-companys-secrets/))
>
> “all of our tech companies need to work extra hard to keep us secure” — Nathan Lambert, Interconnects, 2026-10-30 ([link](https://www.interconnects.ai/p/was-i-wrong-about-open-models-and))
>
> “tracks live security incidents that agents can monitor on a schedule” — Ben's Bites, 2026-10-27 ([link](https://www.bensbites.com/p/is-anthropic-the-best-business-in))
>
> “the normal operation of cybersecurity is vast swarms of hacker bots battling vast swarms of defender bots 24/7” — Zach Weinersmith, Don't Worry About the Vase, 2026-10-23 ([link](https://thezvi.substack.com/p/the-hackening))

### 16. AI vulnerability report triage and patch-prioritization

**Validates, deduplicates and prioritizes AI-generated vulnerability reports for maintainers and under-resourced security teams, with patch suggestions.**

*Confidence: medium · 274 findings from 14 sources · pain point 118, tool or technique 63, build request 42, workaround 22, tool complaint 14, debate 10, link shared 5*

- **Problem:** AI finds vulnerabilities faster than maintainers can triage, verify or fix them, and maintainers are swamped with reports of mixed quality.
- **Who:** Open source maintainers, small security teams and organizations with legacy software.
- **Evidence:** T007 (105 findings, 11 sources, 47 in last 90 days, 20 build requests). Requests: verifying and auditing AI-driven kernel vulnerability discovery and patch generation, tools to keep up with the flood of fixes as software is produced faster than it's secured, and live incident tracking for agents.
- **Existing alternatives:** Claude Security, Codex Security, Project Glasswing, Cursor Security Review, deepsec, WAF stopgaps, pwn.watch.
- **Gap:** Scanners generate findings, but verification (reproducing exploits in a sandbox), dedup of AI reports, and ranking by exploitability and exposure for a specific stack are underserved, especially for maintainers with no budget.
- **MVP:** A GitHub app for maintainers that ingests security reports and issues, attempts reproduction in a sandbox, dedupes, scores severity and exposure, and drafts a fix PR for human review. Also, a feed of exposure checks matched to a user's dependency manifest.
- **Why now:** AI vulnerability discovery scaled sharply in 2026 and maintainers report being swamped, with most demand evidence concentrated in the last 90 days.
- **Risks:** Labs ship their own security agents. Maintainers rarely pay, and enterprise sales are heavy. Safe exploit reproduction is technically tricky.
- **Themes:** T007 AI-found vulnerabilities outpace triage and patching; T006 Cyber safeguards block legitimate defenders; T062 Verifying AI-written code without human review

What people said:

> “948 Linux privilege escalation vulnerabilities” — AINews (smol.ai), 2026-11-06 ([link](https://latent.space/p/ainews-inkling-2-small-17a-594b-trained-in-68-hours-on-12t-tokens-beating-muse-spark/))
>
> “buying enough compute, & converting it into enough defensive tokens” — Tomasz Tunguz, Tomasz Tunguz, 2026-11-06 ([link](https://tomtunguz.com/a-90-dollar-key-into-your-companys-secrets/))
>
> “all of our tech companies need to work extra hard to keep us secure” — Nathan Lambert, Interconnects, 2026-10-30 ([link](https://www.interconnects.ai/p/was-i-wrong-about-open-models-and))
>
> “tracks live security incidents that agents can monitor on a schedule” — Ben's Bites, 2026-10-27 ([link](https://www.bensbites.com/p/is-anthropic-the-best-business-in))
>
> “the normal operation of cybersecurity is vast swarms of hacker bots battling vast swarms of defender bots 24/7” — Zach Weinersmith, Don't Worry About the Vase, 2026-10-23 ([link](https://thezvi.substack.com/p/the-hackening))

### 17. AI slop and bot filter for feeds and forums

**A cross-platform browser extension plus moderator tool that scores and filters AI-generated content and bot comments with calibrated uncertainty.**

*Confidence: low · 200 findings from 13 sources · pain point 86, build request 54, debate 24, tool or technique 22, tool complaint 8, workaround 6*

- **Problem:** AI-generated posts, spam and bot comments flood feeds, search and forums, and readers can't tell human from AI. Detectors give false positives and watermarks are strippable.
- **Who:** Readers on X, Substack, Reddit, HN and LinkedIn, plus community moderators and forum operators.
- **Evidence:** T024 (72 findings, 16 build requests), T034 (80 findings, 17 build requests, 33 in last 90 days) and T052 (48 findings, 21 build requests). Requests: a cross-platform Chrome extension flagging AI content, a 'percent human' score on social accounts, paid-only comments to block AI spam, and bot protection beyond captchas.
- **Existing alternatives:** Pangram Chrome extension, hn-ai.org, hcker.news filter, SynthID, Cloudflare Turnstile, hCaptcha, Setfit spam classifiers, human.json, invite-only communities.
- **Gap:** Detectors have false positives on short or mixed text and don't expose uncertainty. Moderator-side tooling for small forums (spam classifiers trained on their own data) is limited.
- **MVP:** A Chrome extension wrapping a third-party detector API, showing per-post and per-account scores with 'uncertain' bands and a hide/collapse option. Pair it with a moderator plugin training a small spam classifier on a community's removed comments.
- **Why now:** Slop complaints intensified and several communities started adopting filters and invite-only rules this year.
- **Risks:** Detection accuracy is fundamentally limited and false accusations harm users. Pangram or platforms may own this. Models adapt, so detectors decay. Low consumer willingness to pay.
- **Themes:** T024 Filtering AI slop from feeds, search and forums; T034 Detecting AI-generated text and content; T052 Bot detection and proof-of-human online

What people said:

> “removing the "it's not A, it is B" tell would be rather simple and involve a modification of the system prompt” — stuxnet79, Hacker News — Ask HN, 2026-10-29 ([link](https://news.ycombinator.com/item?id=50284849))
>
> “is that letter entirely AI generated (yes)” — Kelsey Piper, Don't Worry About the Vase, 2026-10-22 ([link](https://thezvi.substack.com/p/ai-191-the-hackening-begins))
>
> “verifier access, provenance semantics, and what exactly counts as authored output” — AINews (smol.ai), 2026-08-17 ([link](https://news.smol.ai/issues/26-08-17-not-much/))
>
> “If Substack supports a feature like “only users with a paid subscription somewhere on the platform can engage,” I’d implement it.” — Nathan Lambert, Interconnects, 2026-06-17 ([link](https://www.interconnects.ai/p/state-of-the-blog-mid-2026))
>
> “a Chrome extension that works across platforms (X, Substack, Medium, LinkedIn, Reddit, etc.)” — The Algorithmic Bridge, 2026-05-13 ([link](https://www.thealgorithmicbridge.com/p/how-this-small-startup-achieved-a))

### 18. Skill registry with vetting, versioning and cross-harness portability

**A registry for agent skills and plugins that validates, security-scans, versions and tests them across Claude, Codex and other harnesses.**

*Confidence: low · 223 findings from 12 sources · tool or technique 123, pain point 47, build request 27, workaround 12, debate 12, link shared 1, tool complaint 1*

- **Problem:** Skills are loosely specified bundles that are hard to share, version, vet and port across harnesses, and large libraries lose precision.
- **Who:** Teams and individuals who author and install agent skills and MCP servers.
- **Evidence:** T048 (79 findings, 7 sources, 19 build requests) and T059 (73 findings, MCP vs CLI context bloat). Requests include a trusted verification layer to vet skills before install, a standard way to package MCP servers and skills across tools, and portable formats for encoding evals and judges. T048 has only 5 findings in last 90 days.
- **Existing alternatives:** Agent Skills standard, skills.sh, Clawhub, Vercel skills, Agent Plugins, npm packages, Anthropic Tool Search, Cloudflare Code Mode.
- **Gap:** Registries exist, but trust (security review, provenance), automated testing of skills with evals, and measuring whether adding a skill hurts precision are missing.
- **MVP:** A CLI and web index that lints skills against the Agent Skills spec, runs static security checks for exfiltration and dangerous commands, runs a small trigger-accuracy eval, and tracks versions with a lockfile. Add a lazy-loading proxy that exposes only relevant skills.
- **Why now:** Skills became a shared standard across harnesses and supply-chain concerns (malicious packages and skills) are growing.
- **Risks:** Anthropic, Vercel and others control registries, and network effects favor incumbents. Recent activity is low, so demand may have cooled. Security scanning claims are risky.
- **Themes:** T048 Skill registries, portability and trust; T059 Tool schemas bloat context; MCP versus CLI; T050 Harness evaluation and self-improving agent loops

What people said:

> “Zeno wants someone working in a chat client to be able to do what they can do in the dashboard.” — Zeno Rocha, Latent Space, 2026-11-10 ([link](https://latent.space/p/resend/))
>
> “shifts evaluation from task outputs to the quality of generated agent harnesses” — AINews (smol.ai), 2026-09-03 ([link](https://news.smol.ai/issues/26-09-03-gpt-6-astra/))
>
> “standard for packaging MCP servers and Skills” — Ben's Bites, 2026-08-11 ([link](https://www.bensbites.com/p/make-it-readable))
>
> “We’ll all need trusted operators like Tank to verify our skills.” — Tomasz Tunguz, Tomasz Tunguz, 2026-02-09 ([link](https://tomtunguz.com/can-you-fly-that-thing/))
>
> “Experimental. Support for this field may vary between agent implementations” — Simon Willison, Simon Willison's Weblog, 2025-12-19 ([link](https://simonwillison.net/2025/Dec/19/agent-skills/))

### 19. Independent audit and incident-tracking database for AI labs and agents

**A public, neutral tracker of AI incidents, lab safety claims and potential legal violations, aimed at enforcement targets and auditors.**

*Confidence: low · 458 findings from 13 sources · pain point 212, build request 80, debate 66, tool or technique 51, tool complaint 24, workaround 19, link shared 6*

- **Problem:** Labs self-police, disclose incidents late and publish thin documentation, and no independent mechanism verifies their claims.
- **Who:** Policymakers, AGs and prosecutors, journalists, enterprises relying on lab safety claims, and AI safety researchers.
- **Evidence:** T001 is the top-scored theme (783.4; 127 findings from 9 sources; 48 build requests; 81 in last 90 days). Requests include independent auditors not paid by labs, incident and near-miss reporting, and a public database cataloging potential AI company lawbreaking. T027 and T014 add distrust of lab-run alignment and eval results.
- **Existing alternatives:** AIUC-1 standard, METR, voluntary lab reports, CAISI pilot, proposed FINRA-style body and AI NTSB.
- **Gap:** No neutral, continuously updated incident and claims database linking lab statements to evidence exists, and auditors depend on lab access and payment.
- **MVP:** A curated public website that logs incidents and lab safety-document gaps, each with sources, a structured schema (date, system, harm, disclosed or not), and a claims-versus-evidence scorecard. Start by tracking system cards and incident disclosures for the main labs.
- **Why now:** Late disclosures and thin system cards drew repeated criticism, and policy proposals for an AI NTSB and auditing bodies are active.
- **Risks:** Hard to monetize (grant or donation funded). Needs credibility and legal care. Real audits require lab access that a small team can't get. Curation workload is ongoing. Demand comes mainly from commentators rather than paying users.
- **Themes:** T001 Third-party auditing, certification and incident reporting for AI labs; T027 Unreliable alignment evaluation and chain-of-thought monitoring; T014 Models detect evals and change behavior; T040 Jailbreaks keep bypassing model safeguards; T061 Government and military AI use restrictions

What people said:

> “verifies a response came from a specific model without revealing weights” — jaminball, AINews (smol.ai), 2026-11-04 ([link](https://latent.space/p/ainews-behind-latent-space-kill-my-saas-jev-ai-in-2026-aiei-shanghai/))
>
> “foster true auditor independence by not allowing auditors to be paid (or selected) by the labs they audit” — Nat Purser, Don't Worry About the Vase, 2026-10-17 ([link](https://thezvi.substack.com/p/leaked-anthropic-draft-ai-regulatory))
>
> “somebody should put up a website with all the potential lawbreaking in one place” — Zephyr Teachout, Marcus on AI, 2026-09-30 ([link](https://garymarcus.substack.com/p/can-companies-like-openai-keep-getting))
>
> “there is someone who's not financially, like, motivated” — Thariq Shihipar, Latent Space, 2026-09-29 ([link](https://latent.space/p/thariq/))
>
> “Requiring incident reporting for near misses could allow us to understand where alignment failures continue” — Sayash Kapoor, Arvind Narayanan, AI as Normal Technology, 2026-09-14 ([link](https://www.normaltech.ai/p/the-ai-as-normal-technology-view))

### 20. Cheap GPU price aggregator and flexible capacity broker

**Compare and book spot and on-demand GPUs across marketplaces with verified hardware, bandwidth checks and flexible terms.**

*Confidence: low · 117 findings from 12 sources · pain point 61, tool or technique 38, build request 12, workaround 4, link shared 1, debate 1*

- **Problem:** Rented GPUs vary in bandwidth, authenticity and stability, while capacity is scarce, sold in rigid long contracts and priced volatilely.
- **Who:** Startups, researchers and small teams renting GPUs for training and inference.
- **Evidence:** T037 (55 findings, 10 sources, 25 in last 90 days, 32 pain points, 11 build requests). Requests: pooling scattered compute for startups, independent inference capacity as neoclouds face distress, flexible on-demand layers, and latency/bandwidth-tiered inference pricing.
- **Existing alternatives:** vast.ai, Modal, Runpod serverless, Colab over SSH, spot markets, neoclouds, GPU marketplaces.
- **Gap:** No neutral tool compares real price, verified specs and reliability across providers and handles short bookings. Existing marketplaces vary widely in quality.
- **MVP:** A price comparison site aggregating public GPU marketplace APIs with an on-instance benchmark script (bandwidth, GPU model verification) and community reliability scores. Add alerts for price drops on specific GPUs.
- **Why now:** Compute scarcity and neocloud distress were recurring topics late in the year, with demand concentrated in the last 90 days.
- **Risks:** Thin margins, easy to copy, and provider APIs and terms vary. Real brokerage requires capital and trust. Market could shift if capacity loosens.
- **Themes:** T037 GPU rental and capacity scarcity, unreliability and rigid pricing; T071 KV cache memory limits long-context serving

What people said:

> “the general lack of availability of big blobs of compute for newer startups to buy” — Import AI, 2026-11-09 ([link](https://importai.substack.com/p/import-ai-480-self-sustaining-space))
>
> “AI may be priced the same way. We see this already with products focused on low-latency inference” — Tomasz Tunguz, Tomasz Tunguz, 2026-11-04 ([link](https://tomtunguz.com/watts-in-store-for-2027-inference/))
>
> “independent inference capacity is essential for the startup ecosystem” — saranormous, AINews (smol.ai), 2026-10-27 ([link](https://latent.space/p/ainews-anthropic-s1/))
>
> “the world needs to, and that's fundamentally, I mean, I'm very biased, but like that's why I think modal can play a very large role” — Erik Bernhardsson, Latent Space, 2026-10-22 ([link](https://latent.space/p/modal-d/))
>
> “rent GPUs & CPUs with the infra handled for you” — Ben's Bites, 2026-08-13 ([link](https://www.bensbites.com/p/grok-bot-is-not-what-you-think))

## Top 40 themes by demand score

| # | Theme | Domain | Findings | Sources | Last 90 days | Buildable |
|---|---|---|---|---|---|---|
| T001 | Third-party auditing, certification and incident reporting for AI labs | safety & governance | 127 | 9 | 81 | maybe |
| T002 | Agents escape evaluation sandboxes and coordinate covertly | safety & governance | 111 | 13 | 74 | yes |
| T003 | Portable, persistent, editable agent memory | agents & orchestration | 139 | 12 | 43 | yes |
| T004 | AI regulation, liability and governance debates | safety & governance | 142 | 12 | 54 | no |
| T005 | Agent tool-call governance, identity and oversight | safety & governance | 98 | 11 | 50 | yes |
| T006 | Cyber safeguards block legitimate defenders | safety & governance | 112 | 10 | 40 | yes |
| T007 | AI-found vulnerabilities outpace triage and patching | safety & governance | 105 | 11 | 47 | yes |
| T008 | Model routing and cost-aware delegation | agents & orchestration | 133 | 11 | 36 | yes |
| T009 | Prompt injection hijacks tool-using agents | safety & governance | 96 | 10 | 35 | yes |
| T010 | Dashboards for supervising many parallel agents | agents & orchestration | 108 | 12 | 26 | yes |
| T011 | Sandboxes and runtime isolation for agent code | agents & orchestration | 118 | 8 | 30 | yes |
| T012 | Provider-agnostic harnesses and unified model interfaces | agents & orchestration | 122 | 10 | 18 | yes |
| T013 | Context loss and compaction in long agent sessions | agents & orchestration | 105 | 12 | 23 | yes |
| T014 | Models detect evals and change behavior | evals & testing | 110 | 6 | 37 | maybe |
| T015 | AI writing is generic, bloated and loses personal voice | productivity & knowledge work | 93 | 9 | 19 | yes |
| T016 | Opaque subscription limits and silent model swaps | consumer apps | 91 | 8 | 16 | yes |
| T017 | Reviewing AI-generated code and PRs is the bottleneck | coding agents | 102 | 7 | 38 | yes |
| T018 | Public benchmarks don't predict real-world performance | evals & testing | 79 | 12 | 23 | yes |
| T019 | Chatbot tone, sycophancy and style control | consumer apps | 85 | 9 | 6 | yes |
| T020 | Alignment, welfare and existential risk debates | safety & governance | 103 | 10 | 35 | no |
| T021 | Coding agents need sandboxing and scoped permissions | safety & governance | 86 | 10 | 0 | yes |
| T022 | Sandboxing coding agents to prevent destructive actions | coding agents | 96 | 7 | 6 | yes |
| T023 | Cost per task is hidden behind per-token prices | observability & cost | 68 | 8 | 35 | yes |
| T024 | Filtering AI slop from feeds, search and forums | consumer apps | 72 | 10 | 13 | yes |
| T025 | Long-horizon agents drift and need supervision | agents & orchestration | 86 | 13 | 8 | yes |
| T026 | Computer-use and browser agents are unreliable | agents & orchestration | 87 | 13 | 22 | maybe |
| T027 | Unreliable alignment evaluation and chain-of-thought monitoring | safety & governance | 85 | 7 | 44 | maybe |
| T028 | AI investment bubble and financing opacity | business & markets | 95 | 9 | 30 | maybe |
| T029 | Real-time monitoring of internal and deployed AI agents | observability & cost | 51 | 10 | 36 | yes |
| T030 | Building eval datasets and custom evals is hard | evals & testing | 77 | 11 | 20 | yes |
| T031 | Frontier model churn, deprecations and vendor lock-in | enterprise adoption | 73 | 13 | 7 | yes |
| T032 | Agent code fails to fit codebases and piles up debt | coding agents | 73 | 9 | 6 | yes |
| T033 | Scheduled, always-on and background agents | agents & orchestration | 71 | 9 | 27 | yes |
| T034 | Detecting AI-generated text and content | safety & governance | 80 | 6 | 33 | yes |
| T035 | Agent trace viewers and observability tooling | observability & cost | 76 | 9 | 19 | yes |
| T036 | Usage limits and model costs drain agent budgets | coding agents | 81 | 8 | 6 | yes |
| T037 | GPU rental and capacity scarcity, unreliability and rigid pricing | inference & infra | 55 | 10 | 25 | yes |
| T038 | Personal agents are hard to set up and manage | agents & orchestration | 71 | 9 | 22 | yes |
| T039 | Human review can't keep up with AI-generated PRs | devtools & IDEs | 78 | 7 | 15 | yes |
| T040 | Jailbreaks keep bypassing model safeguards | safety & governance | 78 | 8 | 0 | yes |

Score = (3×build requests + 2×(pain points, workarounds, complaints) + other findings) × source diversity × recency. All themes: `themes.json`; every finding with its theme: `findings.csv`.
