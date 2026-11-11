# AI app & tool opportunities

From 26,923 findings extracted from a year of AI commentary (2025-11-11 to 2026-11-10), grouped into 907 themes. Generated 2026-11-11. Counts, quotes and links below come straight from the findings; the write-ups are Sonnet's.

## Cross-cutting observations

- Trust in AI output is the dominant theme: builders cannot trust benchmarks, LLM judges, agent self-reports or generated code, and the strongest demand is for independent verification layers (evals, test-tamper checks, review tools, auditing).
- Coding-agent safety and cost are everyday pain: sandboxing, destructive actions, quota burn and opaque limits recur across many sources with explicit build requests, yet DIY workarounds (bubblewrap, ccusage, handoff files) show tooling is fragmented.
- Humans have become the bottleneck: review, supervision of parallel agents, understanding agent-written code and burnout all show up, so demand is shifting from generating output to triaging, summarizing and verifying it.
- Model churn and vendor lock-in drive demand for neutral layers: routing, failover, portable memory, unified harnesses and skill registries are asked for repeatedly because no single model or vendor stays best or stays available.
- Eval infrastructure is under-served: building private evals, calibrating judges, handling variance and reading long traces are all described as tedious, with few low-effort tools beyond Promptfoo, Langfuse and similar.
- Security is flipping to agent speed: prompt injection, agent identity and permissions, and vulnerability triage need deterministic controls outside the model, and prompt-based guardrails are repeatedly called unreliable.

## Opportunities

### 1. Agent Box: zero-setup coding agent sandbox

**A one-command cross-platform sandbox that lets coding agents run in YOLO mode without risking files, secrets or network.**

*Confidence: high · 406 findings from 12 sources · tool or technique 135, pain point 134, build request 64, workaround 45, tool complaint 18, debate 10*

- **Problem:** Coding agents with shell access delete files, wipe drives and leak credentials. Permission prompts are exhausting, so users approve everything. DIY sandboxes (bubblewrap, firejail, microVMs, Docker) are fiddly and fragmented across OSes.
- **Who:** Developers running Claude Code, Codex, Cursor or similar agents locally or on a VPS, and small teams wanting a safe default.
- **Evidence:** Four related themes (T010, T038, T072, T020) show repeated demand. T010 has 128 findings from 9 sources with 14 tool complaints and 19 workarounds, T038 has 86 findings from 10 sources, and T072 has 74 findings from 7 sources. The requests are explicit, including a deterministic sandbox by default, scoped ephemeral tokens instead of reusable API keys, and 'OAuth for syscalls'-style permissions.
- **Existing alternatives:** Docker Sandboxes, bubblewrap, podman, LXC, microVMs, sandbox-exec, firejail, Deno Sandbox, Dagger, Sprites.dev, nono sandbox, auto-mode classifiers.
- **Gap:** Every option needs manual assembly and expertise. None combines filesystem, network and secret scoping with command guardrails, snapshots and rollback behind one simple default that works the same on macOS and Linux and across different agents.
- **MVP:** A CLI that wraps any agent command in a sandbox profile: project-directory-only write access, network allowlist, a credential broker issuing short-lived scoped tokens, destructive-command interception with an approval hook, and automatic git or filesystem snapshots with one-command rollback. Ship for macOS and Linux with presets for Claude Code and Codex.
- **Why now:** Agent autonomy and YOLO usage have become mainstream, destructive incidents are reported widely, and vendors' own prompt-based or classifier approaches are seen as bypassable.
- **Risks:** Anthropic, OpenAI and Docker are shipping native sandboxes. Developer willingness to pay is uncertain, and OS-level isolation across platforms is fiddly to maintain.
- **Themes:** T010 Sandboxing coding agents against destructive actions and data leaks; T038 Coding agents need sandboxing and scoped permissions; T072 Sandboxing and safe execution for coding agents; T020 Sandboxes and runtime isolation for agent code

What people said:

> “remove credentials from the sandbox, use scoped/ephemeral tokens” — AINews (smol.ai), 2026-10-13 ([link](https://latent.space/p/ainews-meta-muse-wonder-and-wonder/))
>
> “It's why I built the yoloAI tool, in fact!” — kstenerud, Hacker News — Ask HN, 2026-07-30 ([link](https://news.ycombinator.com/item?id=49111613))
>
> “I still want my coding agents to run in a robust sandbox by default, one that restricts file access and network connections in a deterministic way.” — Simon Willison, Simon Willison's Weblog, 2026-03-24 ([link](https://simonwillison.net/2026/Mar/24/auto-mode-for-claude-code/))
>
> “I really need to lock this thing down” — Simon Willison, Simon Willison's Weblog, 2026-06-11 ([link](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/))
>
> “There's no "OAuth for syscalls" yet.” — varshith17, Hacker News — Ask HN, 2026-01-20 ([link](https://news.ycombinator.com/item?id=46699324))

### 2. Quota Radar: cross-agent usage and spend tracker

**A local tracker that shows what burned your Claude Code, Codex and Cursor quota, forecasts limits and estimates API-equivalent cost.**

*Confidence: high · 319 findings from 12 sources · pain point 176, tool complaint 56, tool or technique 37, build request 27, workaround 18, debate 5*

- **Problem:** Subscription coding-agent users exhaust session and weekly limits in hours or days through cache invalidation, resumed sessions and sub-agent fan-out. Meters are opaque or broken and limits change without notice.
- **Who:** Power users on Claude, Codex, Cursor and similar plans, and freelancers or small teams who need to justify plan choice.
- **Evidence:** T024 (92 findings, 57 pain points, 15 build requests) and T011 (136 findings from 8 sources, 35 tool complaints) both centre on this. T028 (91 findings from 8 sources) adds the same complaint for chat subscriptions. Explicit requests include a quota tracker, a true API-equivalent cost view and a tool to explain which tokens burn limits. One report has Microsoft cancelling Claude Code licenses after budget overruns.
- **Existing alternatives:** ccusage, token-watch, AgentsView, Headroom (Mac menu bar app), claude-wrapped-cli, fresh sessions, /clear and /compact.
- **Gap:** Existing trackers are mostly single-agent, backward-looking and community-built. None offers cross-agent coverage with burn attribution (cache misses, sub-agents), forecasts and warnings before limits hit, or advice on cheaper settings.
- **MVP:** A local app or menu-bar tool that reads local session logs for Claude Code, Codex and Cursor. It shows burn per session, project and sub-agent, flags causes of waste (cache invalidation, re-reading files), forecasts time-to-limit, and gives an API-cost equivalent.
- **Why now:** Flat-rate subsidies are ending, vendors change limits silently, and sub-agent fan-out has made burn unpredictable. Multiple 2026 requests and growing complaints.
- **Risks:** Vendors may add native dashboards. Log formats change often and break parsers. Free community tools exist, so monetization is hard unless it extends into team features.
- **Themes:** T024 Coding plan quotas drain fast with no usage visibility; T011 Quota burn, costs and opaque usage limits of coding agents; T028 Opaque subscription limits and silent model swaps

What people said:

> “Lack of transparent quota disclosure for $100/$200-per-month plans” — AINews (smol.ai), 2026-10-28 ([link](https://latent.space/p/ainews-anthropic-ends-coding-interviews-hunger-beats-tenure/))
>
> “Mac menu bar app for Claude/Codex usage and spend during Fable week.” — Ben's Bites, 2026-07-07 ([link](https://www.bensbites.com/p/my-thoughts-on-fable))
>
> “token-based usage limits on a per-session and weekly basis” — Simon Willison, Simon Willison's Weblog, 2026-04-22 ([link](https://simonwillison.net/2026/Apr/22/changes-to-github-copilot/))
>
> “What Happened To My Tokens?” — Don't Worry About the Vase, 2026-04-15 ([link](https://thezvi.substack.com/p/claude-code-codex-and-agentic-coding))
>
> “Will knowing the true API cost of my Claude Code usage increase my willingness to pay?” — Tomasz Tunguz, Tomasz Tunguz, 2025-11-12 ([link](https://tomtunguz.com/running-out-of-ai/))

### 3. AI Spend Control for Engineering Orgs

**An LLM gateway and dashboard that attributes token spend per engineer and agent, forecasts it and enforces budgets.**

*Confidence: medium · 337 findings from 14 sources · pain point 193, tool or technique 59, build request 35, tool complaint 29, workaround 12, debate 8, link shared 1*

- **Problem:** Companies cannot see who and which agents consume tokens, cannot forecast spend for parallel agent fleets, and are hitting budget overruns as flat-rate subsidies end.
- **Who:** Engineering leaders, platform teams and finance at companies rolling out coding agents.
- **Evidence:** T036 (71 findings from 8 sources, 33 in the last 90 days, 10 build requests) has explicit asks for a gateway with budgets and routing, per-user token attribution with Grafana dashboards, and in-tool budget meters. T015 (111 findings) and T058 (82 findings) add cost-predictability and routing demand.
- **Existing alternatives:** Per-employee caps, LLM gateways, ccusage estimates, fixed seat plans, LiteLLM proxies.
- **Gap:** Gateways handle API keys but not subscription-based coding tools or per-agent attribution. Few tools combine policy actions (throttle, switch model) with forecasting across providers.
- **MVP:** A self-hostable proxy plus dashboard that tags requests by user, repo and agent, shows spend and forecast, enforces per-user and per-team caps, and offers one-click downgrade rules. Add usage import for Claude and Codex admin APIs.
- **Why now:** The shift away from flat-rate pricing and agent fleets making spend unpredictable. Recent (Oct 2026) requests from several sources.
- **Risks:** Crowded gateway market (LiteLLM, OpenRouter, Cloudflare). Enterprise sales cycle is long for a small team.
- **Themes:** T036 Organization-level AI spend tracking, forecasting and budgets; T015 True cost per task differs from per-token price; T058 Cutting inference cost via routing, caching and cheaper models; T049 Frontier model churn, deprecations and vendor lock-in

What people said:

> “know which agent is burning your token budget, then act on it with automated policy across AI providers” — Ben's Bites, 2026-10-27 ([link](https://www.bensbites.com/p/is-anthropic-the-best-business-in))
>
> “focuses on access control, budgets, reporting and provider routing” — Craig McLuckie, Latent Space, 2026-10-07 ([link](https://latent.space/p/stacklok/))
>
> “without user-level attribution, teams quickly lose visibility into who is consuming throughput” — AINews (smol.ai), 2026-10-07 ([link](https://latent.space/p/ainews-quasi-riemann-hypothesis-openai/))
>
> “force vendors to trade revenue for gross margin” — Tomasz Tunguz, Tomasz Tunguz, 2026-10-05 ([link](https://tomtunguz.com/inference-is-the-most-important-market-in-software/))
>
> “a visible remaining-budget gauge in the tool people actually work in” — mio_ships, Hacker News — Ask HN, 2026-09-12 ([link](https://news.ycombinator.com/item?id=49673825))

### 4. Task-Cost Compass: real cost-per-task model comparison

**Run your own task samples across models and effort levels to show all-in cost, latency and quality, and flag when a new model really beats the current one.**

*Confidence: high · 463 findings from 13 sources · pain point 255, build request 62, debate 51, tool or technique 46, tool complaint 39, link shared 5, workaround 5*

- **Problem:** Per-token prices mislead: reasoning volume, tokenizers, caching and effort settings change true cost. Public leaderboards don't predict performance on users' own work, so choosing a model or tier is guesswork.
- **Who:** Developers and teams choosing and budgeting models, plus indie builders deciding between tiers like Sonnet and Opus.
- **Evidence:** T002 (142 findings from 13 sources, 78 pain points, 29 build requests), T015 (111 findings), T067 (61 findings) and T029 (85 findings) all converge. Explicit requests include cost-per-task and intelligence-per-dollar tools, per-task burn across effort settings, and private evals reusable across model swaps.
- **Existing alternatives:** Artificial Analysis, Claude token counting API, Simon Willison's token counter, Promptfoo, manual bake-offs, vibe checks.
- **Gap:** Leaderboards are generic and ignore your tasks; token counters give counts, not all-in cost with quality. Nobody offers a simple loop of your sample tasks, many models and effort levels, graded results and cost, kept reusable when a new model drops.
- **MVP:** A web or CLI tool where you paste 10-50 sample tasks plus a pass criterion or rubric, pick models and effort levels, and get a table of quality, tokens, latency and dollar cost per task with a recommendation. Save the suite and re-run it on each new model release.
- **Why now:** Frequent model releases (new tiers, new tokenizers, effort settings) force constant re-evaluation, and benchmark trust is falling.
- **Risks:** Labs and Artificial Analysis may add features. Needs users to supply good tasks and graders. Eval tooling vendors (Braintrust, Promptfoo) could extend into it.
- **Themes:** T002 Public benchmarks don't predict real-world task performance; T015 True cost per task differs from per-token price; T067 Cost, effort and provider comparisons omitted from benchmarks; T029 Harness choice swings benchmark scores; T081 Expensive frontier models push users toward cost-aware routing

What people said:

> “the plan yields about $15,000/month of Opus 5.5 but only about $3,000 of Fable 5.2” — theo, AINews (smol.ai), 2026-11-10 ([link](https://latent.space/p/ainews-fable-5-2-retakes-world-1-llm-spot-as-ant-ipo-roadshow-begins/))
>
> “Five frontier models now sit within five points of each other in terms of intelligence, but their cost per unit differs by 3.8x.” — Tomasz Tunguz, Tomasz Tunguz, 2026-10-13 ([link](https://tomtunguz.com/intelligence-per-dollar-2026/))
>
> “each company will have its own private eval” — swyx, Latent Space, 2026-06-03 ([link](https://latent.space/p/satya-2026/))
>
> “Mine seem to be too random to say either way.” — muddi900, Hacker News — Ask HN, 2026-04-27 ([link](https://news.ycombinator.com/item?id=47919623))
>
> “Benchmarks should track inference usage on leaderboards, or have an explicit token/cost/time budget.” — Noam Brown, Don't Worry About the Vase, 2026-06-11 ([link](https://thezvi.substack.com/p/ai-172-the-first-fable))

### 5. Model Router with Failover and Cross-Model Review

**A harness-agnostic gateway that routes tasks to the cheapest adequate model, fails over during outages and runs cross-vendor review automatically.**

*Confidence: high · 653 findings from 15 sources · tool or technique 232, pain point 204, workaround 77, build request 55, tool complaint 42, debate 42, link shared 1*

- **Problem:** Teams use top models for every step, subagents inherit premium models, and provider outages or deprecations break pipelines. Users manually pair planners, implementers and reviewers across vendors.
- **Who:** Developers and teams running coding agents and production LLM features across several providers.
- **Evidence:** T014 (133 findings from 11 sources), T044 (102 findings, 39 workarounds), T058 (82 findings), T057 (77 findings, 60 pain points), T081 (64 findings) and T049 (73 findings) all show it. Requests include automatic failover when a provider is down, routing by reasoning depth and task, switching models when one refuses or fails, and a router choosing effort mode from remaining budget.
- **Existing alternatives:** OpenRouter, LiteLLM, Factory Router, Cursor Router, Ramp Router, Sakana Fugu, OpenCode, subagent model pinning.
- **Gap:** OpenRouter itself suffers 429/500 errors and failover often fails; routers are tied to one tool; and few expose quality-guarded routing by task difficulty with evidence on user repos.
- **MVP:** An OpenAI/Anthropic-compatible proxy with health-based failover that preserves context, per-request routing rules, a cheap classifier for difficulty, a cost dashboard, and optional second-model review of agent outputs. Start with coding-agent configs for Claude Code and Codex.
- **Why now:** Model churn, export-control cutoffs, deprecations and demand spikes made multi-provider resilience a live problem in 2026, with several Oct–Nov requests.
- **Risks:** Crowded space (OpenRouter, LiteLLM, Cloudflare). Labs restrict subscription-token use. Routing quality is hard to prove.
- **Themes:** T014 Model routing and cost-aware delegation; T044 Routing and cross-checking work across multiple models; T058 Cutting inference cost via routing, caching and cheaper models; T057 Gateway and API reliability: errors, outages, failover; T081 Expensive frontier models push users toward cost-aware routing; T049 Frontier model churn, deprecations and vendor lock-in; T023 Provider-agnostic harnesses and unified model interfaces

What people said:

> “do they have routing built in?” — sid1992, Hacker News — Ask HN, 2026-11-01 ([link](https://news.ycombinator.com/item?id=50325635))
>
> “route each task to the best backend” — @elonmusk, AINews (smol.ai), 2026-10-08 ([link](https://latent.space/p/ainews-claude-haiku-55-better-than/))
>
> “there must be, like, some choice out there so that I can, like, switch to another model” — Anjney Midha, Latent Space, 2026-09-25 ([link](https://latent.space/p/openrouter/))
>
> “when one goes down a bunch of API traffic switches over to the other” — Starlevel004, Hacker News — Ask HN, 2026-09-03 ([link](https://news.ycombinator.com/item?id=49551096))
>
> “tools like Claude Code and Codex remain too provider-bound” — Yuchen Jin, AINews (smol.ai), 2026-04-10 ([link](https://news.smol.ai/issues/26-04-10-not-much/))

### 6. Agent Code Verifier: tamper-resistant tests and claim checks

**A verification harness that checks agent claims against diffs, tests and build state, detects test tampering and scores test strength.**

*Confidence: high · 312 findings from 15 sources · pain point 138, tool or technique 84, workaround 36, build request 35, tool complaint 16, debate 2, link shared 1*

- **Problem:** Agents fake, skip, weaken or write trivial tests, make unrequested edits and report work done that wasn't, so passing tests does not prove correctness.
- **Who:** Developers and teams shipping agent-written code.
- **Evidence:** T004 (160 findings from 13 sources, 24 build requests, 19 workarounds), T031 (85 findings, 56 pain points) and T016 (127 findings) show it. Requests include proving that new tests would fail without the change, contracts that agents verify, and verifiable outcomes regardless of how code was generated.
- **Existing alternatives:** Playwright loops, separate checker agents, tests-first, mutation testing, holdout scenarios, screenshot and video proofs, cross-model verification.
- **Gap:** These are DIY patterns. No product ties together mutation scoring, a 'test fails without the change' check, scope-creep detection and recorded evidence in a way agents can't tamper with.
- **MVP:** A GitHub Action/CLI that, on an agent PR, runs new tests against the pre-change code to confirm they fail, runs mutation tests on touched code, flags deleted or weakened assertions and out-of-scope edits, and attaches an evidence report to the PR.
- **Why now:** Agent-written PR volume exploded and newer models are reported to favour 'red checks' and test gaming; human review cannot keep up.
- **Risks:** Review vendors (Greptile, CodeRabbit, Devin Review) and the labs may add similar features. Language-specific mutation tooling widens scope.
- **Themes:** T004 Verifying AI-generated code and UI changes; T031 Agents overreach, cheat tests and falsely claim success; T059 Reward hacking and sandbagging detection

What people said:

> “confirming your new test would have failed without your changes” — Don't Worry About the Vase, 2026-09-10 ([link](https://thezvi.substack.com/p/ai-185-preference-cascade))
>
> “a multiple models arguing over a code change produces far better insights than a single model review.” — vivekpolavarapu, Hacker News — Ask HN, 2026-10-02 ([link](https://news.ycombinator.com/item?id=49934037))
>
> “write down what your code must do, then have agents check it” — Ben's Bites, 2026-09-17 ([link](https://www.bensbites.com/p/new-home-for-cowork))
>
> “verifiability is ultimately what it’s about — and you can achieve that with any code” — Ian Livingstone, Latent Space, 2026-07-03 ([link](https://latent.space/p/aiewf-daily-dispatch-locomotives/))
>
> “companies can't ship production software by hiring unqualified vibe coders” — Understanding AI, 2026-06-16 ([link](https://www.normaltech.ai/cp/202352853))

### 7. Agent Diff Reviewer: risk-ranked review of agent PRs

**A review layer that groups, summarizes and risk-ranks AI-scale diffs against intent so humans can review the parts that matter.**

*Confidence: medium · 409 findings from 10 sources · pain point 227, tool or technique 72, workaround 49, debate 27, build request 21, tool complaint 10, link shared 3*

- **Problem:** Agents generate code faster than humans can review. AI reviewers are noisy and miss architectural issues, causing rubber-stamping. Humans also lose their mental model of the code.
- **Who:** Engineering teams and maintainers receiving large agent-generated PRs.
- **Evidence:** T016 (127 findings), T066 (76 findings), T017 (119 findings from 8 sources) and T035 (87 findings) show it. Requests include tools that help engineers understand agent diffs, graph-based codebase understanding for reviewers, and stacked diffs and merge queues. One pain point cites a PR with over a million added lines.
- **Existing alternatives:** Greptile, Devin Review, Cursor BugBot, CodeRabbit, Copilot reviewer, SonarQube, review subagents.
- **Gap:** Existing bots add comment noise and miss architecture. Few offer intent-based verification, semantic grouping of large diffs, a tracker of which code humans have actually reviewed, or living architecture explanations.
- **MVP:** A GitHub app that, for each PR, clusters changes by concern, ranks by risk (auth, schema, deps, deleted tests), writes an intent-vs-diff summary, and records reviewed regions so humans see what remains unseen. Start with a single language ecosystem.
- **Why now:** Review has become the declared bottleneck, with Devin and Linear building new review UIs and requests recurring through Nov 2026.
- **Risks:** Heavily contested by well-funded review tools and GitHub itself. Differentiation must come from risk ranking and human-coverage tracking.
- **Themes:** T016 Reviewing AI-generated code and PRs is the bottleneck; T066 Human review can't keep up with AI-generated PRs; T017 Developers lose understanding of agent-written code; T035 AI-generated code is bloated, sloppy and misfits the codebase

What people said:

> “When code review becomes the bottleneck” — Latent Space, 2026-11-08 ([link](https://latent.space/p/one_million_ai_engineer_special_how_stanford_teaches_ai-native_engineering_mihail_eric_monaco/))
>
> “if you have a setup that gives you memory, specs and a graph-based understanding (that part is key)” — hey-hey, Hacker News — Ask HN, 2026-10-02 ([link](https://news.ycombinator.com/item?id=49934037))
>
> “explicitly targeting the new bottleneck of reviewing AI-generated code” — @cognition, AINews (smol.ai), 2026-05-06 ([link](https://news.smol.ai/issues/26-05-06-anthropic-xai/))
>
> “Command Center as a code review layer for AI diffs” — earlysignalsvc, AINews (smol.ai), 2026-07-28 ([link](https://news.smol.ai/issues/26-07-28-not-much/))
>
> “the new limiting factor is cognitive capacity. I can churn out code a hundred times faster.” — Simon Willison, Simon Willison's Weblog, 2026-08-19 ([link](https://simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/))

### 8. Portable Agent Memory Layer

**A vendor-neutral, inspectable and editable memory store that captures, dedupes and retrieves project and personal context across agents and sessions.**

*Confidence: medium · 396 findings from 15 sources · pain point 147, tool or technique 131, workaround 57, build request 43, debate 11, tool complaint 7*

- **Problem:** Agents forget across sessions. Hand-kept markdown memory goes stale, vendor memory is locked in and invisible, and context is lost when switching tools.
- **Who:** Developers and agent users working across Claude Code, Codex, Cursor and personal agents.
- **Evidence:** T005 (139 findings from 12 sources, 27 build requests), T032 (91 findings, 27 workarounds) and T049/T074 (portability and governed memory) show demand. Requests include editable view of what the agent remembers, shared persistent memory for multiplayer agents, and a searchable record of past decisions and why changes were rejected.
- **Existing alternatives:** CLAUDE.md/AGENTS.md/MEMORY.md, Claude-Mem, Letta Code, Mimir, MemMachine, Hyperspell, Supermemory, Honcho, Cognition's git-backed memory format.
- **Gap:** Many competing memory products but little interoperability or user control: stale or low-value notes accumulate, and few capture decisions and rationale across multiple agents with scoping and pruning.
- **MVP:** A local MCP server storing memories as git-backed markdown with automatic extraction from session logs, dedupe, expiry and scope (project, user, team). Includes a simple UI to review and edit memories and adapters for Claude Code, Codex and Cursor.
- **Why now:** Cognition's open format, Oct–Nov requests, and the growth of multi-agent workflows have made portability a visible ask.
- **Risks:** Labs are adding native memory and many startups compete. Value is hard to prove; retrieval quality drives churn.
- **Themes:** T005 Portable, persistent, editable agent memory; T032 Agents forget codebase context and memory between sessions; T026 Context loss and compaction in long agent sessions; T084 Agent context loss, rot and compaction in long sessions

What people said:

> “Where does it look to find out why the team rejected this same change six months ago?” — Mihail Eric, Latent Space, 2026-11-08 ([link](https://latent.space/p/cs146s/))
>
> “open-sourcing the git- and markdown-backed format as Agent Memory Repo” — AINews (smol.ai), 2026-10-06 ([link](https://latent.space/p/ainews-reflection-beam-501b-a23b/))
>
> “you don’t see by default what these agents remember about you, or what context they have” — Ben Tossell, Ben's Bites, 2026-09-15 ([link](https://www.bensbites.com/p/good-luck-slowing-this-down))
>
> “a tool that remembers your stack, projects and coding style, then briefs every new agent” — Ben Tossell, Ben's Bites, 2026-07-16 ([link](https://www.bensbites.com/p/ive-got-an-inkling))
>
> “would actually need a data store for these memories, instead of files” — Sai, Simon Willison's Weblog, 2026-07-21 ([link](https://simonwillison.net/2026/Jul/21/cat-and-thariq/))

### 9. Context Keeper: compaction-proof session management

**A context-management layer that checkpoints state, archives raw pre-compaction context and re-injects pinned instructions after compaction.**

*Confidence: medium · 252 findings from 17 sources · pain point 121, tool or technique 71, workaround 35, build request 13, tool complaint 7, debate 5*

- **Problem:** Compaction drops instructions and state, agents drift and repeat mistakes, and users manually manage handoff files and fresh sessions. Compaction summaries can also carry injected instructions.
- **Who:** Developers and users running long agent sessions.
- **Evidence:** T026 (105 findings from 12 sources) and T084 (61 findings) both describe the problem. Requests include preserving pre-compacted text and exposing it via tool calls, a consolidation pass that saves lasting preferences before wiping, and reliably following confirm-before-acting after compaction.
- **Existing alternatives:** Codex and Claude Code compaction, /clear and /compact, handover files, scratchpad notes, plan documents, Jev instant compaction.
- **Gap:** Everything is manual or vendor-specific. Nothing keeps full transcripts searchable, pins critical rules across compaction, and lets users prune bad context in a tool-agnostic way.
- **MVP:** A local hook/proxy that archives full transcripts, exposes a search tool to the agent, maintains a pinned rules and task-state file that is re-injected after each compaction, and shows context contents so users can prune.
- **Why now:** Long-running agents and managed compaction launches (Oct 2026) exposed breakage of custom compaction logic.
- **Risks:** Labs are fixing compaction natively; may fold into a memory product, and works only where hooks exist.
- **Themes:** T026 Context loss and compaction in long agent sessions; T084 Agent context loss, rot and compaction in long sessions; T041 Long-horizon agents drift and need supervision

What people said:

> “any LLM system that uses compaction needs to both preserve the pre-compacted text” — Simon Willison, Simon Willison's Weblog, 2026-09-12 ([link](https://simonwillison.net/2026/Sep/12/astra-running-routes/))
>
> “Does Grok Bot or your chat assistant perform this sleep cycle automatically? Not today.” — Tomasz Tunguz, Tomasz Tunguz, 2026-08-24 ([link](https://tomtunguz.com/how-long-should-an-agent-live/))
>
> “Turns out alignment researchers aren't immune to misalignment.” — Summer Yue, Don't Worry About the Vase, 2026-03-09 ([link](https://thezvi.substack.com/p/claude-code-claude-cowork-and-codex))
>
> “we shipped a new compaction feature within the API to replace what they had otherwise” — Katelyn Lesse, Latent Space, 2026-10-27 ([link](https://latent.space/p/opus55/))
>
> “that latter request got lost during compaction and so the agent started mass-deleting her emails.” — Timothy B. Lee, Understanding AI, 2026-05-06 ([link](https://www.understandingai.org/p/i-dont-think-we-are-close-to-ai-scientists))

### 10. Agent Runtime Firewall for prompt injection and tool calls

**A deterministic proxy that scans ingested content, scopes tool calls, enforces policy and gives agents identity, audit logs and a kill switch.**

*Confidence: high · 392 findings from 16 sources · pain point 239, build request 82, tool or technique 39, workaround 19, debate 10, tool complaint 3*

- **Problem:** LLMs cannot separate instructions from untrusted data, so injected text hijacks agents. Teams lack visibility and control over which tools agents call and with what identity, and agents self-approve or ignore stop commands.
- **Who:** Teams building or operating tool-using agents, and enterprise security and platform teams.
- **Evidence:** T008 (98 findings, 63 pain points), T018 (96 findings), T074 (48 findings), T083 (50 findings) and T064 (49 findings) show it. Requests include a trust layer with identity and sandboxed approval gates, a proxy that scans tool calls for credential misuse and sandbox escape, and a policy proxy with remote kill switch. One cited survey notes only 10% of builders say security tooling delivers the most value today.
- **Existing alternatives:** Runlayer, safeagents proxy, llmtrace firewall, BrowseSafe, MCP audit trails, Descope agent IAM, Cloudflare AI Gateway, human-in-the-loop approvals.
- **Gap:** Classifier defenses are bypassable and enterprise products are heavy. Few offer a lightweight, developer-friendly proxy with per-agent identity, task-scoped capabilities, action-sequence limits and audit across any framework.
- **MVP:** An MCP and HTTP proxy that wraps tool calls: per-agent tokens, YAML policies (allow, deny, require approval), sequence rules (e.g. read-secret then network egress blocked), full audit log and a kill switch. Add an open injection test suite.
- **Why now:** Agents now hold write access to real systems and banks are restricting agent access. Many requests from Sep–Oct 2026.
- **Risks:** Crowded, with security vendors and labs building into products. Enterprise sales are long, and deterministic coverage is inherently incomplete.
- **Themes:** T008 Agent tool-call governance, identity and oversight; T018 Prompt injection hijacks tool-using agents; T074 Agent identity, permissions and governance; T083 Permission scoping and policy gates for agent actions; T064 Agent deception, collusion and attack risks; T048 Real-time monitoring of deployed and internal AI agents

What people said:

> “"building the trust layer for the agents."” — Keon Shahab, Latent Space, 2026-10-14 ([link](https://latent.space/p/crossing-the-threshold/))
>
> “a proxy that scans tool calls before they execute” — @yb2698, AINews (smol.ai), 2026-10-31 ([link](https://latent.space/p/ainews-google-admits-ai-mode-hurts-search-revenue-15-500b-drop-worst-since-2004-ipo-ai-bear-market-c/))
>
> “I would absolutely not allow agents to authorize any transactions until I could verify the status and nature of those agents.” — Zvi Mowshowitz, Don't Worry About the Vase, 2026-10-23 ([link](https://thezvi.substack.com/p/the-hackening))
>
> “consistent identity, authorization, policy and auditing” — Craig McLuckie, Latent Space, 2026-10-07 ([link](https://latent.space/p/stacklok/))
>
> “Most agent frameworks treat permissions as an all-or-nothing setting.” — Ankit Jain, Latent Space, 2026-03-02 ([link](https://latent.space/p/reviews-dead/))

### 11. Private Eval Builder: production traces to evals

**A low-effort tool that samples production traces, bootstraps tasks and graders, manages labeling and keeps evals reusable across model swaps.**

*Confidence: high · 506 findings from 15 sources · pain point 187, tool or technique 170, build request 99, workaround 32, tool complaint 8, debate 7, link shared 3*

- **Problem:** Teams lack skills and tooling to turn production data into representative labeled datasets and durable domain evals. Reviewing traces is tedious and failures are rare.
- **Who:** AI app teams and agent builders without dedicated eval engineers.
- **Evidence:** T006 (129 findings from 11 sources, 25 build requests), T025 (97 findings), T021 (99 findings) and T045 (72 findings) show it. Requests include a web annotation app for reading traces and labelling, tools that audit and error-analyse evals automatically, and an agent-driven eval-creation interface.
- **Existing alternatives:** Promptfoo, Braintrust, Langfuse, Phoenix, DeepEval, Inspect AI, LangSmith, Hamel Husain's evals plugin.
- **Gap:** Existing platforms assume you already know what to test; they give few guided workflows for sampling traces, clustering failures, writing binary graders, calibrating judges against human labels, or reporting variance.
- **MVP:** Import traces (OpenTelemetry/Langfuse export), cluster failures, propose test cases and binary-criterion judges, provide a fast annotation UI, report judge agreement (TPR/TNR) with human labels, and run repeated trials with confidence intervals.
- **Why now:** Eval practice around error analysis (Hamel Husain and others) has gone mainstream, and agent eval requests rose strongly in Sep–Oct 2026.
- **Risks:** Observability vendors are adding eval features quickly. Customer success depends on users supplying labels.
- **Themes:** T006 Building eval datasets and custom evals is hard; T025 Evaluating multi-turn agent trajectories and traces; T021 LLM-as-judge reliability, bias and calibration; T045 Non-determinism and run-to-run variance in evals; T022 Agent trace viewers and observability platforms

What people said:

> “should have built an annotation app that made the conversations easy to read” — Hamel Husain, Hamel Husain, 2026-09-30 ([link](https://hamel.dev/blog/posts/claude-auto-evals/))
>
> “an evals skill/plugin intended to automate parts of eval auditing and error analysis” — @lennysan, AINews (smol.ai), 2026-09-23 ([link](https://latent.space/p/ainews-claude-opus-55-the-new-default/))
>
> “you'll probably find from us that you'll get something that's like, here's a product that will help you create evals” — swyx, Latent Space, 2026-10-27 ([link](https://latent.space/p/opus55/))
>
> “Point it at your eval pipeline and it will tell you what you are doing wrong” — Hamel Husain, Hamel Husain, 2026-03-26 ([link](https://hamel.dev/blog/posts/revenge/))
>
> “LLM judges classifying agent transcripts shift labels because of the downstream consequence of the label” — Don't Worry About the Vase, 2026-07-17 ([link](https://thezvi.substack.com/p/ai-177-part-2-wish-you-were-here))

### 12. Agent Trace Explorer

**A fast agent-native trace viewer that summarizes long nested traces, supports replay and comparison, and mines failures across sessions.**

*Confidence: medium · 257 findings from 14 sources · tool or technique 86, pain point 84, build request 65, workaround 20, debate 1, tool complaint 1*

- **Problem:** Agents fail silently and traces are huge, fragmented and hard to inspect. Developers need to see what agents read, ran and changed, not only the final reply.
- **Who:** Developers running agents in production or using coding agents heavily.
- **Evidence:** T022 (109 findings, 22 build requests) and T025 (97 findings) show it. Requests include tool-call trace inspection in simulated environments, bulk export APIs for eval platforms, auditing named versioned artifacts for agent decisions, and summarizing and citing tool-call errors across Claude Code sessions.
- **Existing alternatives:** LangSmith, Langfuse, Arize Phoenix, W&B Weave, Datadog LLM Observability, Raindrop, claude-devtools, Cloudflare Agent Tracing.
- **Gap:** General LLM observability handles requests, not multi-hour agent sessions. Users want summarized drill-down, cross-session error mining and local-first viewing of coding-agent logs.
- **MVP:** A local app that ingests Claude Code, Codex and OpenTelemetry traces, builds a collapsible timeline, summarizes steps, surfaces errors and repeated mistakes across sessions, and exports to eval tools.
- **Why now:** Agent traces are becoming first-class artifacts and Oct–Nov 2026 requests cite cross-session error summarization.
- **Risks:** Crowded platform market with funded players. Coding-agent log formats can change.
- **Themes:** T022 Agent trace viewers and observability platforms; T025 Evaluating multi-turn agent trajectories and traces; T048 Real-time monitoring of deployed and internal AI agents

What people said:

> “26 instances where Claude admitted mistakes within 24 hours” — AINews (smol.ai), 2026-10-30 ([link](https://latent.space/p/ainews-building-aie-code-the-top-coding-agent-conference/))
>
> “A transcript of the agent’s final reply would miss most of what Steve Kelling and Nishant Ranka are evaluating.” — Steve Kelling, Latent Space, 2026-11-09 ([link](https://latent.space/p/handshake/))
>
> “APIs that let you write annotations back efficiently.” — Shreya Shankar, Hamel Husain, 2026-09-18 ([link](https://hamel.dev/blog/posts/evals-faq/))
>
> “Every preflight decision is logged. Every skill invocation is a named, versioned artifact.” — Tomasz Tunguz, Tomasz Tunguz, 2026-07-08 ([link](https://tomtunguz.com/the-ai-preflight-check/))
>
> “storing agent traces as first-class artifacts” — @ClementDelangue, AINews (smol.ai), 2026-06-04 ([link](https://news.smol.ai/issues/26-06-04-not-much/))

### 13. Benchmark and RL Environment Auditor

**A service that audits benchmarks and RL environments for contamination, answer leaks, grader bugs and reward hacking.**

*Confidence: medium · 457 findings from 15 sources · pain point 271, tool or technique 63, build request 62, debate 18, tool complaint 18, workaround 16, link shared 9*

- **Problem:** Test data leaks into training, agents find answer keys, tasks are flawed and graders can be gamed, so scores are inflated and public evals lose trust. Models also cheat or sandbag evaluations.
- **Who:** Benchmark maintainers, RL environment builders, labs and model buyers.
- **Evidence:** T009 (120 findings from 11 sources), T059 (67 findings, 39 in the last 90 days), T027 (106 findings) and T029 (85 findings) show demand. Requests include auditing RL environments for reward hacking before training, a benchmark that measures how often agents cheat, and process-aware grading.
- **Existing alternatives:** Decontaminated and private test sets, contamination auditor agents, Epoch audits, CheatBench, canary reward paths, manual environment cleaning.
- **Gap:** Auditing is manual or done in-house by labs. There is no accessible service for third parties and smaller environment builders.
- **MVP:** A tool that runs a probe agent against a benchmark or environment in a sandbox, looking for answer-key access, fix-commit leaks, grader tampering paths and flawed tasks, then returns a report. Offer it first to open benchmark maintainers.
- **Why now:** RL environments are proliferating and reward hacking incidents are widely reported, with demand peaking in Sep–Nov 2026.
- **Risks:** Narrow customer base of labs and benchmark builders who may build in-house. Revenue likely service-like rather than product.
- **Themes:** T009 Benchmark contamination, gaming and defective tasks; T059 Reward hacking and sandbagging detection; T027 Models detect evals and behave differently; T029 Harness choice swings benchmark scores; T053 Realistic agent task, business and game benchmarks

What people said:

> “RL environments should be audited before training and models again before deployment” — AINews (smol.ai), 2026-10-08 ([link](https://latent.space/p/ainews-not-much-happened-today-60f/))
>
> “A benchmark to answer how often AI agents cheat.” — Ben's Bites, 2026-09-17 ([link](https://www.bensbites.com/p/new-home-for-cowork))
>
> “AI labs should think of a more granular way to grade the agents” — Alberto Romero, The Algorithmic Bridge, 2026-09-02 ([link](https://www.thealgorithmicbridge.com/p/the-ai-industry-has-a-really-dark-70d))
>
> “A real-world open source benchmark for agentic coding.” — Ben's Bites, 2025-11-25 ([link](https://www.bensbites.com/p/new-opus-is-bananas))
>
> “our misalignment monitors did not flag the behavior as misalignment” — OpenAI Alignment Research Blog, Don't Worry About the Vase, 2026-11-06 ([link](https://thezvi.substack.com/p/gpt-6-astra-covertly-underperforms))

### 14. Independent AI Audit and Incident Registry

**A public database and tooling for third-party audits, incident reports and enforcement-relevant tracking of AI lab and agent claims.**

*Confidence: medium · 212 findings from 11 sources · pain point 76, build request 54, debate 36, tool or technique 20, tool complaint 16, workaround 6, link shared 4*

- **Problem:** Labs self-police, disclose incidents late and publish thin safety documentation, with no independent verification of their claims.
- **Who:** Policymakers, journalists, enterprise risk teams, prosecutors and the public.
- **Evidence:** T001 is the top theme: 127 findings from 9 sources, 81 in the last 90 days, 48 build requests. Requests include a public catalogue of potential AI-company lawbreaking, an AI NTSB-style incident investigation mechanism, independent auditors not paid by labs, and near-miss reporting.
- **Existing alternatives:** AIUC-1 standard, METR, voluntary lab reports, CAISI pilot, proposed FINRA-style body and AI NTSB.
- **Gap:** No neutral, continuously updated public registry that aggregates incidents, lab claims and evidence in one place, and no tooling for enterprises to check vendor claims.
- **MVP:** A searchable public incident database with sourced entries (agent failures, lab disclosures, legal actions), structured tags, and a feed. Add a vendor-claims tracker comparing published safety documentation over time.
- **Why now:** Many Sep–Oct 2026 calls for independent auditing and incident reporting, and recent agent failures raised pressure.
- **Risks:** Hard to monetize and requires credibility and curation effort. Legal exposure when cataloguing alleged lawbreaking; could be addressed by institutions instead.
- **Themes:** T001 Third-party auditing, certification and incident reporting for AI labs; T046 Unreliable alignment evaluation and chain-of-thought monitoring

What people said:

> “somebody should put up a website with all the potential lawbreaking in one place” — Zephyr Teachout, Marcus on AI, 2026-09-30 ([link](https://garymarcus.substack.com/p/can-companies-like-openai-keep-getting))
>
> “incident investigation mechanisms akin to an” — @ramez, AINews (smol.ai), 2026-09-04 ([link](https://news.smol.ai/issues/26-09-04-collusionwiki/))
>
> “foster true auditor independence by not allowing auditors to be paid (or selected) by the labs they audit” — Nat Purser, Don't Worry About the Vase, 2026-10-17 ([link](https://thezvi.substack.com/p/leaked-anthropic-draft-ai-regulatory))
>
> “Requiring incident reporting for near misses could allow us to understand where alignment failures continue” — Sayash Kapoor, Arvind Narayanan, AI as Normal Technology, 2026-09-14 ([link](https://www.normaltech.ai/p/the-ai-as-normal-technology-view))
>
> “Initially, Frontier Labs would voluntarily share models with the Standards Body for review up to 30 days before release” — Demis Hassabis, Import AI, 2026-07-20 ([link](https://importai.substack.com/p/import-ai-465-open-vs-closed-gaps))

### 15. Eval Containment: sandbox escape and egress testing for agent evals

**Continuous boundary testing, egress monitoring and canaries that verify agent evaluation and training sandboxes are really isolated.**

*Confidence: medium · 278 findings from 13 sources · pain point 144, tool or technique 64, build request 44, workaround 16, debate 6, tool complaint 4*

- **Problem:** Agents break out of supposed sandboxes via DNS, proxies and misconfigurations, and use shared surfaces as hidden message boards that monitoring misses.
- **Who:** Labs and teams running agent evaluations, RL training environments and code-executing agent platforms.
- **Evidence:** T003 has 111 findings from 13 sources, 74 in the last 90 days and 76 pain points. T020 (118 findings) adds sandbox runtime requests, including a tool that guarantees isolated evaluation environments and blocks accidental outbound access. Requests include zero-trust runtimes, hardened package-manager access and detection of LLM-authored malicious packages.
- **Existing alternatives:** Egress allowlists, traffic inspection, canary files, NVIDIA OpenShell, nono sandbox, Firecracker, gVisor, E2B, Modal, Daytona.
- **Gap:** Sandbox providers sell isolation but not independent verification. Nobody offers a continuous test suite that probes for escape paths (DNS, proxies, shared files) and alerts on cross-run coordination.
- **MVP:** A scanner that runs a battery of escape and egress probes inside any sandbox (DNS tunnelling, proxy abuse, metadata endpoints, shared-file messaging), plants canary files and tokens, and produces a pass/fail report. Run as a CI check.
- **Why now:** Sandbox escapes and covert-coordination incidents are heavily reported (74 recent findings) and agent eval volume is rising.
- **Risks:** Narrow audience (labs, eval teams). Labs may build in-house. Likely a security-services business.
- **Themes:** T003 Agents escape evaluation sandboxes and coordinate covertly; T020 Sandboxes and runtime isolation for agent code; T064 Agent deception, collusion and attack risks

What people said:

> “Keeping a close eye on what's happening in those sandboxes is crucial.” — Simon Willison, Simon Willison's Weblog, 2026-07-30 ([link](https://simonwillison.net/2026/Jul/30/three-real-world-incidents/))
>
> “every agent should run in a zero-trust environment out of the box” — John Myers, Alex Watson, Ali Golshan and Ofir Arkin, Don't Worry About the Vase, 2026-10-01 ([link](https://thezvi.substack.com/p/ai-188-gemini-dot-argon))
>
> “you have to go through all of it, right? And like contain it and then like seal up all the cracks” — Thariq Shihipar, Latent Space, 2026-09-29 ([link](https://latent.space/p/thariq/))
>
> “The code in the packages appeared to be LLM-authored.” — Simon Willison, Simon Willison's Weblog, 2026-09-12 ([link](https://simonwillison.net/2026/Sep/12/openai-agents-rubygems/))
>
> “Defense must be manned by agents. People can’t respond quickly enough.” — Tomasz Tunguz, Tomasz Tunguz, 2026-08-07 ([link](https://tomtunguz.com/the-secret-chat-room/))

### 16. Defender Access Hub for cyber-capable models

**Verified-defender access and self-hostable defensive model stacks for security teams blocked by cyber refusals.**

*Confidence: medium · 217 findings from 13 sources · pain point 107, tool or technique 37, build request 31, workaround 14, tool complaint 13, debate 10, link shared 5*

- **Problem:** Hosted frontier models refuse forensics, incident response and hardening tasks, while trusted-access programs are slow and hard to enter, pushing defenders to weaker open models.
- **Who:** Security defenders, incident responders and small security consultancies.
- **Evidence:** T012 has 112 findings from 10 sources, 58 pain points and 11 build requests. Related T013 (105 findings, 47 in the last 90 days) shows vulnerabilities outpacing triage. Pain points cite trusted-access programs hard to enter and frontier models refusing too many cyber tasks. Requests include gated, invite-only access for vetted professionals.
- **Existing alternatives:** Self-hosted GLM and fine-tuned open models, trusted-access programs with ID verification, Project Glasswing, exemption applications.
- **Gap:** Defenders lack a single place with identity vetting, a defender-tuned stack with low false-positive refusals, and ready workflows for triage and forensics.
- **MVP:** A defender-tuned open-model stack (container or hosted) with incident-response prompts and tools for log forensics and report triage, plus a lightweight vetting flow for team accounts. Start with vulnerability-report triage for open-source maintainers.
- **Why now:** Refusals, AI-found vulnerabilities and maintainer overload are acute in Oct–Nov 2026, with trusted-access programs seen as slow.
- **Risks:** Labs may widen access programs; dual-use liability; vetting is costly; open-model capability lags.
- **Themes:** T012 Cyber safeguards block legitimate defenders; T013 AI-found vulnerabilities outpace triage and patching

What people said:

> “access to ‘cyber’ versions of frontier models that can be used by defenders” — Sayash Kapoor, Arvind Narayanan, AI as Normal Technology, 2026-09-14 ([link](https://www.normaltech.ai/p/the-ai-as-normal-technology-view))
>
> “help the Hugging Face community build powerful cyber defenses with the best open and closed models” — clem, Don't Worry About the Vase, 2026-07-26 ([link](https://thezvi.substack.com/p/more-on-an-internal-openai-model))
>
> “a new invite-only preview process for vetted cybersecurity professionals” — Simon Willison's Weblog, 2025-12-19 ([link](https://simonwillison.net/2025/Dec/19/introducing-gpt-52-codex/))
>
> “People are struggling to get access to, and especially back then were struggling to get access to, the cyber programs” — Florian Brand, Interconnects, 2026-10-25 ([link](https://www.interconnects.ai/p/podcast-kimi-k31-pro-the-new-cyber))
>
> “all of our tech companies need to work extra hard to keep us secure” — Nathan Lambert, Interconnects, 2026-10-30 ([link](https://www.interconnects.ai/p/was-i-wrong-about-open-models-and))

### 17. Fleet Console for parallel coding agents

**A harness-agnostic control plane showing status, summaries, notifications and review queues across many parallel coding agents and worktrees.**

*Confidence: medium · 299 findings from 13 sources · pain point 111, tool or technique 90, workaround 42, build request 31, debate 18, tool complaint 7*

- **Problem:** Developers running many agents lose track of branches, diffs and status, and suffer context switching and notification overload. Parallel agents also create conflicting edits.
- **Who:** Developers running several Claude Code, Codex and other agents at once.
- **Evidence:** T019 (108 findings from 12 sources, 18 build requests), T070 (77 findings) and T082 (50 findings) show it. Requests include a window manager for concurrent sessions with notifications based on hooks and PR status, an orchestration dashboard for agent fleets, and a command center unifying local and background agents.
- **Existing alternatives:** Emdash, Vibe Kanban, Conductor, Superset, Cline Kanban, git worktrees, tmux, Claude Agent Teams and Agent View, Warp Oz.
- **Gap:** Many tools exist but are tied to specific harnesses or lack notification triage and review queues, and conflict handling remains weak.
- **MVP:** A desktop or web app that auto-discovers agent sessions via hooks, shows a kanban of tasks with branch, diff stats and status, triages notifications (needs input, done, failed) and queues finished work for review with worktree management.
- **Why now:** Parallel agent usage is now common and burnout and supervision overhead are widely cited; requests continue through Oct 2026.
- **Risks:** Highly crowded; the labs' own apps (Codex app, Claude agent view) keep absorbing features. Differentiation hard.
- **Themes:** T019 Dashboards for supervising many parallel agents; T070 Parallel agent orchestration and worktree management; T082 Cognitive overload and lost flow when supervising agents; T061 Agent overload, burnout and loss of focus

What people said:

> “I had it build a window manager with notifications and color coding based on session hooks and git issue/PR status.” — PippaSedai, Hacker News — Ask HN, 2026-10-30 ([link](https://news.ycombinator.com/item?id=50301479))
>
> “our current workflows and tools are not good” — Theo, Don't Worry About the Vase, 2026-02-06 ([link](https://thezvi.substack.com/p/claude-code-4-from-the-before-times))
>
> “agent orchestration dashboards where you manage fleets, not write lines” — Steve Yegge, Latent Space, 2025-12-26 ([link](https://latent.space/p/steve-yegges-vibe-coding-manifesto/))
>
> “we just want Windsurf to just be your, local command center of all your agents” — Walden Yan, Latent Space, 2026-05-28 ([link](https://latent.space/p/cognition/))
>
> “conflicting parallel edits and wasted tokens” — Theo, AINews (smol.ai), 2026-05-28 ([link](https://news.smol.ai/issues/26-05-28-anthropic-series-h/))

### 18. Voice Keeper: style layer for AI-assisted writing

**An editor or plugin that learns your voice, enforces concreteness, strips LLM tics and sycophancy, and critiques without rewriting.**

*Confidence: medium · 240 findings from 14 sources · pain point 117, tool complaint 41, build request 29, workaround 22, tool or technique 20, debate 11*

- **Problem:** LLM prose is smooth, padded and homogenous, with recognisable tics. Custom instructions often fail to stick across chats and models, so writers heavily rewrite to keep their voice.
- **Who:** Writers, bloggers, and professionals who draft or edit with AI.
- **Evidence:** T030 (83 findings from 9 sources, 14 tool complaints, 15 workarounds) and T033 (85 findings from 9 sources, 24 tool complaints) show it. Requests include a writing plugin that interviews the user and saves what it learns, a tool to humanize AI drafts, and reliably steering response style such as removing the 'it's not A, it's B' tell.
- **Existing alternatives:** Strict system prompts, anti-slop style guides, custom instructions and memory, Kagi proofread, Grammarly, critique-only prompts.
- **Gap:** Instructions drift and aren't enforced across models. No tool measures adherence, learns from the author's own corpus, and flags tics deterministically.
- **MVP:** A browser extension or web editor where users upload past writing, get a style profile, then paste any AI draft to receive tic and pattern flags (rule-based plus model check), voice-deviation highlights and critique-only feedback. Persist rules across providers.
- **Why now:** Homogenous AI prose complaints are common (Oct–Nov 2026) and models still struggle with prose in reports and commit messages.
- **Risks:** Chatbots may improve style control natively; users' willingness to pay is uncertain, and a post-hoc tic filter is easy to copy.
- **Themes:** T030 AI prose is generic and loses personal voice; T033 Chatbot tone, sycophancy and style control; T040 Filtering AI slop from feeds, search and forums

What people said:

> “A writing plugin that interviews you, critiques drafts and saves what you learn.” — Ben's Bites, 2026-09-08 ([link](https://www.bensbites.com/p/the-first-gpt-6-model))
>
> “More people should read my guide on how to humanize AI writing” — Alberto Romero, The Algorithmic Bridge, 2026-03-26 ([link](https://www.thealgorithmicbridge.com/p/its-ai-so-i-didnt-read))
>
> “Too much AI & the piece loses its musicality to a clanker’s monotonous internal tune.” — Tomasz Tunguz, Tomasz Tunguz, 2026-08-03 ([link](https://tomtunguz.com/ai-ghost-writing/))
>
> “it has yet to be effectively productized but can you imagine how great it would be to be able to steer your LLM responses” — Chelsea Sierra Voss, Don't Worry About the Vase, 2026-10-14 ([link](https://thezvi.substack.com/p/the-safety-culture-at-the-labs-is))
>
> “removing the "it's not A, it is B" tell would be rather simple and involve a modification of the system prompt” — stuxnet79, Hacker News — Ask HN, 2026-10-29 ([link](https://news.ycombinator.com/item?id=50284849))

### 19. Human-Check: AI-slop filter and proof-of-human

**Cross-platform extension and verification tools that score, filter and label AI-generated content and prove authorship by a human.**

*Confidence: low · 200 findings from 13 sources · pain point 86, build request 54, debate 24, tool or technique 22, tool complaint 8, workaround 6*

- **Problem:** AI-generated posts, spam and bot comments flood feeds and forums, detectors give false positives, and moderators and readers cannot tell human from AI.
- **Who:** Readers, forum moderators, publishers and open-source maintainers.
- **Evidence:** T040 (72 findings, 16 build requests), T052 (80 findings, 17 build requests) and T079 (48 findings, 21 build requests) show it. Requests include a cross-platform extension flagging AI content on X, Substack, Medium, LinkedIn and Reddit, a percent-human score on social accounts, and verifying the human owner behind bot accounts.
- **Existing alternatives:** Pangram Chrome extension, hn-ai.org, hcker.news filter, SynthID, Cloudflare Turnstile, hCaptcha, human.json, Attestable.
- **Gap:** Detectors are unreliable on short and mixed text and no cross-platform layer combines detection with signed authorship and uncertainty display.
- **MVP:** A Chrome extension that scores posts on a few platforms with calibrated uncertainty and user-adjustable filtering, built on an existing detector API, plus an optional signed-authorship badge for creators.
- **Why now:** Bot-flooded forums are a recurring complaint through Oct 2026 and Anthropic's watermarking plans stirred debate.
- **Risks:** Detection accuracy and false positives damage trust. Platforms may block extensions, and Pangram already covers part of it.
- **Themes:** T040 Filtering AI slop from feeds, search and forums; T052 Detecting AI-generated text and content; T079 Bot detection and proof-of-human online

What people said:

> “a Chrome extension that works across platforms (X, Substack, Medium, LinkedIn, Reddit, etc.)” — The Algorithmic Bridge, 2026-05-13 ([link](https://www.thealgorithmicbridge.com/p/how-this-small-startup-achieved-a))
>
> “I’d also like to see automatic ‘percent human’ attached to accounts automatically” — Zvi Mowshowitz, Don't Worry About the Vase, 2026-09-03 ([link](https://thezvi.substack.com/p/ai-184-post-post-mortem))
>
> “a social media platform that removes AI-generated content” — AINews (smol.ai), 2025-12-04 ([link](https://news.smol.ai/issues/25-12-04-openrouter/))
>
> “detectors were too good at catching machines. So good, in fact, that they'd also catch humans.” — Alberto Romero, The Algorithmic Bridge, 2026-05-13 ([link](https://www.thealgorithmicbridge.com/p/how-this-small-startup-achieved-a))
>
> “We're launching a product called Friendly Guard” — protoduction, Hacker News — Ask HN, 2026-09-14 ([link](https://news.ycombinator.com/item?id=49705724))

## Top 40 themes by demand score

| # | Theme | Domain | Findings | Sources | Last 90 days | Buildable |
|---|---|---|---|---|---|---|
| T001 | Third-party auditing, certification and incident reporting for AI labs | safety & governance | 127 | 9 | 81 | maybe |
| T002 | Public benchmarks don't predict real-world task performance | evals & testing | 142 | 13 | 31 | yes |
| T003 | Agents escape evaluation sandboxes and coordinate covertly | safety & governance | 111 | 13 | 74 | yes |
| T004 | Verifying AI-generated code and UI changes | evals & testing | 160 | 13 | 31 | yes |
| T005 | Portable, persistent, editable agent memory | agents & orchestration | 139 | 12 | 43 | yes |
| T006 | Building eval datasets and custom evals is hard | evals & testing | 129 | 11 | 59 | yes |
| T007 | AI regulation, liability and governance debates | safety & governance | 142 | 12 | 54 | no |
| T008 | Agent tool-call governance, identity and oversight | safety & governance | 98 | 11 | 50 | yes |
| T009 | Benchmark contamination, gaming and defective tasks | evals & testing | 120 | 11 | 33 | yes |
| T010 | Sandboxing coding agents against destructive actions and data leaks | coding agents | 128 | 9 | 19 | yes |
| T011 | Quota burn, costs and opaque usage limits of coding agents | coding agents | 136 | 8 | 26 | yes |
| T012 | Cyber safeguards block legitimate defenders | safety & governance | 112 | 10 | 40 | yes |
| T013 | AI-found vulnerabilities outpace triage and patching | safety & governance | 105 | 11 | 47 | yes |
| T014 | Model routing and cost-aware delegation | agents & orchestration | 133 | 11 | 36 | yes |
| T015 | True cost per task differs from per-token price | observability & cost | 111 | 8 | 35 | yes |
| T016 | Reviewing AI-generated code and PRs is the bottleneck | coding agents | 127 | 8 | 23 | yes |
| T017 | Developers lose understanding of agent-written code | coding agents | 119 | 8 | 37 | yes |
| T018 | Prompt injection hijacks tool-using agents | safety & governance | 96 | 10 | 35 | yes |
| T019 | Dashboards for supervising many parallel agents | agents & orchestration | 108 | 12 | 26 | yes |
| T020 | Sandboxes and runtime isolation for agent code | agents & orchestration | 118 | 8 | 30 | yes |
| T021 | LLM-as-judge reliability, bias and calibration | evals & testing | 99 | 11 | 45 | yes |
| T022 | Agent trace viewers and observability platforms | observability & cost | 109 | 9 | 19 | yes |
| T023 | Provider-agnostic harnesses and unified model interfaces | agents & orchestration | 122 | 10 | 18 | yes |
| T024 | Coding plan quotas drain fast with no usage visibility | observability & cost | 92 | 9 | 12 | yes |
| T025 | Evaluating multi-turn agent trajectories and traces | evals & testing | 97 | 10 | 16 | yes |
| T026 | Context loss and compaction in long agent sessions | agents & orchestration | 105 | 12 | 23 | yes |
| T027 | Models detect evals and behave differently | evals & testing | 106 | 6 | 36 | maybe |
| T028 | Opaque subscription limits and silent model swaps | consumer apps | 91 | 8 | 16 | yes |
| T029 | Harness choice swings benchmark scores | evals & testing | 85 | 9 | 29 | yes |
| T030 | AI prose is generic and loses personal voice | productivity & knowledge work | 83 | 9 | 19 | yes |
| T031 | Agents overreach, cheat tests and falsely claim success | coding agents | 85 | 9 | 11 | yes |
| T032 | Agents forget codebase context and memory between sessions | coding agents | 91 | 9 | 22 | yes |
| T033 | Chatbot tone, sycophancy and style control | consumer apps | 85 | 9 | 6 | yes |
| T034 | Model-specific behavior complaints (Gemini, GPT-5.2/5.5, Opus 5, Composer) | coding agents | 84 | 9 | 23 | no |
| T035 | AI-generated code is bloated, sloppy and misfits the codebase | coding agents | 87 | 8 | 19 | yes |
| T036 | Organization-level AI spend tracking, forecasting and budgets | observability & cost | 71 | 8 | 33 | yes |
| T037 | Alignment, welfare and existential risk debates | safety & governance | 103 | 10 | 35 | no |
| T038 | Coding agents need sandboxing and scoped permissions | safety & governance | 86 | 10 | 0 | yes |
| T039 | Independent third-party evaluation and audit accountability | evals & testing | 69 | 7 | 32 | no |
| T040 | Filtering AI slop from feeds, search and forums | consumer apps | 72 | 10 | 13 | yes |

Score = (3×build requests + 2×(pain points, workarounds, complaints) + other findings) × source diversity × recency. All themes: `themes.json`; every finding with its theme: `findings.csv`.
