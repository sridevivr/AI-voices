# Vibe-codeable app ideas from a year of AI commentary

For a non-engineer building apps (quick wins to ambitious products) with AI coding tools and sharing them on LinkedIn/X. Drawn from 26,923 findings in 907 themes; only themes about everyday users, knowledge workers, students, creators and business teams. Generated 2026-11-11. Counts, quotes and links come straight from the findings; the write-ups are Sonnet's.

## What non-developers struggle with

- The loudest everyday complaint is that AI output sounds generic. Voice, tone, sycophancy and padded prose show up as separate themes with 83, 85 and 45 findings, all asking for control over how AI writes.
- Subscription opacity is a consumer-scale grievance. Hidden caps, silent model swaps and plan changes appear across 8+ sources, and users are asking for normalized, API-dollar-style usage views.
- The next wave of pain is on the receiving end: colleagues send long AI-written messages and docs, nobody can tell who wrote them, and reviewers carry the cost of verifying output.
- Managers and teams cannot find AI use cases, measure ROI or redesign workflows. Only about 2% of S&P 500 companies that report AI impact track a metric for it, which is a gap a program manager understands well.
- Memory and context are fragmented and locked to each provider. Users want to see, scrub, scope and port what the AI knows about them.
- Non-developers are overwhelmed by constant change and by too many models and modes. They want curated, low-hype guidance and one place to choose a model.

## Ideas

### 1. Voice Keeper

**An editor that learns your writing voice, strips AI tics, and critiques your drafts instead of rewriting them.**

*Effort: 3-6 weeks · Confidence: high · 216 findings from 12 sources · pain point 96, tool complaint 43, tool or technique 32, workaround 21, build request 15, debate 9*

- **Problem:** AI drafts come out smooth, padded and generic, and writers rewrite heavily to keep their own voice. Custom instructions like 'no em dashes' don't stick.
- **For:** Professionals, bloggers, LinkedIn writers, newsletter authors
- **Evidence:** Voice and prose themes dominate: T030 (score 394.7, 83 findings, 9 sources), T033 (85 findings), T272 and T231. Explicit build requests include a writing plugin that interviews the user, critiques drafts and saves what it learns (#389), and a tool to preserve a distinct voice (#25363).
- **Existing alternatives:** Grammarly, ChatGPT/Claude custom instructions, Every's style-guide prompt, anti-slop skills, Havelock.AI. They rewrite rather than critique, and rules don't persist across chats.
- **MVP:** Paste 5 of your past posts and it builds a voice profile. Then paste a draft and get a side-by-side with tic highlights (it's not X, it's Y; 'and honestly?'; em dashes), line-level critique, and a density and concreteness score, with no auto-rewrite by default. The fuller product adds a browser extension, saved style guides per audience, and a multi-pass judge model.
- **Build notes:** Next.js on Vercel, Claude or GPT API, Supabase for profiles. Hardest part is making the voice profile specific (few-shot excerpts plus an extracted rules list) and building a reliable tic detector, which combines regex with an LLM pass. Cost is about 2-5 cents per draft.
- **Demo hook:** Split screen: a ChatGPT draft with 14 highlighted tics next to the same draft after Voice Keeper, with a 'sounds like you' score going from 31 to 84.
- **Post angle:** 'I fed an AI 5 of my LinkedIn posts and it told me exactly where my drafts stop sounding like me.' The angle is that the tool critiques instead of rewriting, and it shows the build.
- **Risks:** ChatGPT and Claude style features may improve. Voice fidelity is subjective, and retention depends on how often people write.
- **Themes:** T030 AI prose is generic and loses personal voice; T033 Chatbot tone, sycophancy and style control; T272 AI prose is generic and loses the author's voice; T231 AI editors lack taste and give poor critique

What people said:

> “A writing plugin that interviews you, critiques drafts and saves what you learn.” — Ben's Bites, 2026-09-08 ([link](https://www.bensbites.com/p/the-first-gpt-6-model))
>
> “Too much AI & the piece loses its musicality to a clanker’s monotonous internal tune.” — Tomasz Tunguz, Tomasz Tunguz, 2026-08-03 ([link](https://tomtunguz.com/ai-ghost-writing/))
>
> “More people should read my guide on how to humanize AI writing” — Alberto Romero, The Algorithmic Bridge, 2026-03-26 ([link](https://www.thealgorithmicbridge.com/p/its-ai-so-i-didnt-read))
>
> “can one tell AI not to write like ... AI? Is that possible?” — Bender, Hacker News — Ask HN, 2026-05-22 ([link](https://news.ycombinator.com/item?id=48235223))

### 2. TL;DR Shield

**Turn any bloated AI-written Slack message, email or doc into the decision, the ask and the deadline.**

*Effort: 1-2 weekends · Confidence: high · 80 findings from 10 sources · pain point 60, workaround 12, tool or technique 5, debate 2, build request 1*

- **Problem:** Colleagues send long AI-padded messages and RFCs that hide the real message, and readers can't tell who wrote them or whether the content is stale.
- **For:** Managers, program managers, cross-functional team members
- **Evidence:** T097 (45 findings, 8 sources, 19 in the last 90 days) describes padded AI messages, with workarounds like length caps, ask-first-line rules and asking for the original prompt. T144 adds that colleagues paste unreviewed AI output (#14103) and reviewers bear the cost.
- **Existing alternatives:** Pasting into ChatGPT to summarize, Slack AI summaries, and manual norms such as the 'Clarity Standard'. They require a manual step and don't extract what the sender wants from you.
- **MVP:** A Chrome extension and web paste box. It returns: what they want from me, by when, the key facts, and what's missing, plus an 'AI-padding' meter. The fuller version is a Slack/Gmail integration that auto-posts a decision-first summary in thread.
- **Build notes:** Chrome extension (Plasmo) plus a small Next.js API using Claude Haiku-class models. Gmail and Slack OAuth is the hardest part, so start with paste and selection. Cost is under 1 cent per message.
- **Demo hook:** A 600-word Slack wall of text collapses into three lines: Ask / Deadline / Missing info, with a 'You can skip 80%' badge.
- **Post angle:** 'Everyone's sending me AI-written essays. So I built a shield.' It's relatable to any manager, and the post invites people to submit their worst messages.
- **Risks:** Slack AI and Gmail Gemini may add summaries natively. The value is in extracting the ask rather than just summarizing, and that needs good prompt design.
- **Themes:** T097 Flood of verbose AI-written messages and docs; T144 Mandated AI usage and low-quality AI output erode trust

What people said:

> “Because of the clodisms, even just like silly, like, I don't know, there's like an M dash in the middle of the thing” — Latent Space, 2026-10-27 ([link](https://latent.space/p/opus55/))
>
> “You must stand behind every idea and every sentence in your docs” — Sophie Alpert, Simon Willison's Weblog, 2026-08-11 ([link](https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/))
>
> “Sometimes I click it. Sometimes I wonder if the person on the other end can tell.” — Tomasz Tunguz, Tomasz Tunguz, 2026-03-08 ([link](https://tomtunguz.com/is-this-tomaszs-agent/))
>
> “people who blindly copy and paste the output of AI systems to their peers” — Niklas Gruhn, Simon Willison's Weblog, 2026-08-03 ([link](https://simonwillison.net/2026/Aug/3/dont-be-a-meat-proxy/))

### 3. Plan Watch

**See what your AI subscriptions really give you: normalized usage limits, plan-change alerts, and which model is answering.**

*Effort: 3-6 weeks · Confidence: medium · 171 findings from 10 sources · pain point 111, tool complaint 30, build request 15, debate 6, tool or technique 6, workaround 3*

- **Problem:** Caps are opaque and shifting, plans change by tweet, and models are silently swapped, so subscribers can't tell what they're getting for their money.
- **For:** Paying subscribers of ChatGPT, Claude, Gemini and Perplexity, students and freelancers
- **Evidence:** T028 (score 419.3, 91 findings, 8 sources), T110 (57 findings) and T247 show repeated complaints. Users want limits expressed as an equivalent API-dollar budget instead of vague multipliers (#143, #5924), and OpenAI cut weekly limits by 50% on its $200 plan (#14351).
- **Existing alternatives:** Manual checking, vendor pricing pages, Reddit threads. Nothing normalizes plans across providers or alerts on changes.
- **MVP:** A comparison dashboard of plans with a normalized value-per-dollar score, a pricing-page diff monitor with email alerts, and a self-reported usage log. The fuller product adds a browser extension that counts messages and detects the model label per chat.
- **Build notes:** Next.js plus Supabase, a scheduled job (Vercel cron) that scrapes pricing pages and diffs them with an LLM summary, and Resend for email. The hard parts are keeping plan data accurate and extension DOM scraping that breaks. Cost is minimal.
- **Demo hook:** A dashboard card: 'Claude Pro cut weekly limits yesterday, which equals $X of API usage. Here are 3 cheaper options.'
- **Post angle:** 'I'm tired of guessing what my $20 AI plan actually gives me, so I built a tracker.' It shows live data and invites people to share the plan changes they've spotted.
- **Risks:** Maintaining plan data is manual or brittle, and vendors may change pages often. Users may only check occasionally, which makes retention hard.
- **Themes:** T028 Opaque subscription limits and silent model swaps; T110 Opaque AI subscription usage caps and missing mid-tier plans; T247 Silent AI plan changes and frontier models pulled to API-only

What people said:

> “disclose subscription limits in a normalized API-budget-equivalent” — AINews (smol.ai), 2026-08-31 ([link](https://news.smol.ai/issues/26-08-31-not-much/))
>
> “rather than vague multipliers” — AINews (smol.ai), 2026-09-01 ([link](https://news.smol.ai/issues/26-09-01-claude-mythos-51/))
>
> “The $200 OpenAI subscription plan is cutting weekly usage limits by 50%” — Don't Worry About the Vase, 2026-10-01 ([link](https://thezvi.substack.com/p/ai-188-gemini-dot-argon))
>
> “The model intelligence and quality is incredibly opaque, and it feels like they sometimes just switch the labels out.” — preommr, Hacker News — Ask HN, 2026-09-24 ([link](https://news.ycombinator.com/item?id=49838409))

### 4. Memory Closet

**Export what ChatGPT or Claude 'knows' about you, clean it, scope it by project and import it anywhere.**

*Effort: 1-2 weekends · Confidence: medium · 64 findings from 8 sources · pain point 36, build request 11, tool or technique 9, workaround 6, tool complaint 1, debate 1*

- **Problem:** AI memory leaks across projects, holds stale facts, can't be edited, and locks users into one provider.
- **For:** Heavy ChatGPT/Claude users, consultants and freelancers with several clients or projects
- **Evidence:** T157 (32 findings) and T162 (32 findings, 12 in the last 90 days) describe memory leakage and lock-in. People ask for portable memory (#4678), a scrubbable store (#1436), and already use a prompt-based memory export to switch assistants (#10803).
- **Existing alternatives:** Anthropic's memory import, ChatGPT Projects, manual export prompts and markdown files. None gives a visual editor with scopes.
- **MVP:** Paste an exported memory dump. The app sorts facts into personal, work and per-project buckets, flags stale or conflicting items, lets you edit them, and exports a clean profile block for ChatGPT, Claude or Gemini. The fuller product adds versioning and a Chrome extension that syncs.
- **Build notes:** Next.js plus Supabase. It's an LLM structuring task with a good card-based UI. The hard part is supporting export formats, so start with paste only. Cost is a few cents per import.
- **Demo hook:** Paste 4,000 words of messy memory and watch it turn into tidy cards, with a red 'stale, left your old job' flag and a one-click export to Claude.
- **Post angle:** 'I exported everything ChatGPT remembers about me and was horrified. Then I built a cleaner.' The privacy hook invites replies.
- **Risks:** Providers may add native memory editing and import. Users need export prompts that keep working.
- **Themes:** T157 Chatbot memory is leaky, stale and uneditable; T162 Portable, scoped AI memory and chat history

What people said:

> “it's worth considering options that work across providers and also backing up each providers built-in memory” — mlapeter, Hacker News — Ask HN, 2026-11-02 ([link](https://news.ycombinator.com/item?id=50336034))
>
> “there's simply too much of it” — Utah teapot, Don't Worry About the Vase, 2026-10-22 ([link](https://thezvi.substack.com/p/ai-191-the-hackening-begins))
>
> “tell me everything you know about me” — Florian Brand, Interconnects, 2026-10-25 ([link](https://www.interconnects.ai/p/podcast-kimi-k31-pro-the-new-cyber))
>
> “Qwen, which literally regurgitates what it knows about me in every response” — AINews (smol.ai), 2026-01-16 ([link](https://news.smol.ai/issues/26-01-16-chatgpt-ads/))

### 5. Red Team My Decision

**A panel of expert personas that pushes back on your plan, with pre-mortems and a calibrated verdict instead of flattery.**

*Effort: 1-2 weekends · Confidence: medium · 124 findings from 12 sources · pain point 48, tool complaint 25, tool or technique 18, workaround 15, build request 11, debate 7*

- **Problem:** Chatbots agree with leading questions and flatter users, and people build prompt hacks to get real pushback before decisions.
- **For:** Managers, founders, PMs preparing proposals and strategy memos
- **Evidence:** T187 (39 findings) shows workarounds such as persona debates (#1517) and cross-checking multiple LLMs (#9489). T033 adds build requests for tools that surface disconfirming evidence (#5126), with 85 findings on sycophancy overall.
- **Existing alternatives:** Custom 'absolute mode' prompts, devil's advocate prompts, manual cross-checks between Claude and ChatGPT. These need prompt skill and give inconsistent pushback.
- **MVP:** Enter a decision or plan. Five personas (CFO, skeptic customer, ops lead, legal, pre-mortem narrator) respond, then a synthesizer gives the top 3 risks, what evidence would change your mind, and a confidence range. The fuller product adds multi-model runs and decision logs with follow-up reviews.
- **Build notes:** Next.js, multiple model APIs run in parallel (Claude, GPT, Gemini) with streaming UI. The hard part is making personas distinct, not generic. Cost is about 5-15 cents per run.
- **Demo hook:** A 20-second clip of a weak product launch plan getting 5 personas arguing, then a synthesizer card: 'Kill this assumption first.'
- **Post angle:** 'ChatGPT told me my idea was brilliant. So I built an AI board that disagrees with me.' The PM angle makes it feel like a pre-mortem as a product.
- **Risks:** Chat apps can run personas on request, so the value must be in the packaged workflow. Users may not return unless a decision log builds habit.
- **Themes:** T187 AI sycophancy: need for a challenging thought partner; T033 Chatbot tone, sycophancy and style control

What people said:

> “be a doctor, a lawyer, a historian, a psychologist, and argue this out with each other” — Ole Lehmann, Don't Worry About the Vase, 2026-05-28 ([link](https://thezvi.substack.com/p/ai-170-lack-of-executive-order))
>
> “I use Claude to brainstorm, then I ask Chatgpt and Gemini to 'stress test' the idea.” — UansaS, Hacker News — Ask HN, 2026-05-10 ([link](https://news.ycombinator.com/item?id=48088126))
>
> “it can hit too softly or too hard if you don’t give precise instructions.” — Alberto Romero, The Algorithmic Bridge, 2026-03-23 ([link](https://www.thealgorithmicbridge.com/p/the-one-thing-i-use-ai-for-that-actually))
>
> “Want to find truth? Go elsewhere.” — Gary Marcus, Marcus on AI, 2026-03-03 ([link](https://garymarcus.substack.com/p/breaking-sycophantic-ai-distorts))

### 6. Inbox Rules in English

**Triage Gmail with plain-English rules and drafts in your voice, with nothing sent without approval.**

*Effort: 2-3 months · Confidence: medium · 29 findings from 5 sources · build request 12, pain point 9, tool or technique 4, workaround 3, tool complaint 1*

- **Problem:** Inboxes of 100+ emails a day are a time sink, built-in AI summaries aren't trusted, and Gmail and Superhuman are limited or bloated.
- **For:** Managers and knowledge workers with heavy email loads
- **Evidence:** T216 (29 findings) has 12 build requests, including plain-English triage rules (#12576), a simple Gmail-first client with split inboxes (#14778), and auto-drafts in the user's voice (#3325).
- **Existing alternatives:** Superhuman, Gmail labels and filters, Gmail's AI features, DIY Claude Code triage. They are either costly or require technical setup.
- **MVP:** Connect Gmail (read-only plus drafts). Write rules like 'anything from my skip-level is urgent' and 'newsletters go to a Friday digest'. See a triaged view with a reason per email, plus draft replies in a voice profile. The fuller product adds receipts forwarding and CRM scoring.
- **Build notes:** Next.js, Gmail API with Google OAuth (the app verification process for sensitive scopes is the hardest and slowest part), Supabase, a cheap LLM for classification. Cost is cents per day per user. Start with a test-user list.
- **Demo hook:** A messy 80-email inbox sorts into 'Needs you today (4)', 'Waiting on others', and 'Digest', each with a one-line reason.
- **Post angle:** 'I told my inbox the rules in English, and it listened.' The hook is a real inbox before and after.
- **Risks:** Gmail's native Gemini features, privacy concerns and OAuth verification make this hard. Trust requires conservative actions.
- **Themes:** T216 Email clients and AI inbox triage that work

What people said:

> “User-defined skills & rules. Programming in English” — Tomasz Tunguz, Tomasz Tunguz, 2026-05-13 ([link](https://tomtunguz.com/the-disappearance-of-email/))
>
> “I wanted a split inbox and rules to organize my emails.” — Ben Tossell, Ben's Bites, 2026-05-09 ([link](https://www.bensbites.com/p/bens-builds-3-an-email-app))
>
> “we can do a more customizable version of this using Claude Code” — Peter Wildeford, Don't Worry About the Vase, 2026-01-15 ([link](https://thezvi.substack.com/p/ai-151-while-claude-coworks))
>
> “auto-drafting replies in your voice, scheduling on your behalf” — Latent Space, 2025-12-11 ([link](https://latent.space/p/the-future-of-email-superhuman-cto/))

### 7. Meeting to Done

**Paste a meeting transcript and get commitments extracted, owners assigned, follow-ups drafted, and chasers scheduled.**

*Effort: 3-6 weeks · Confidence: medium · 60 findings from 9 sources · build request 23, tool or technique 18, pain point 11, workaround 6, debate 2*

- **Problem:** Commitments made in meetings fall through the cracks, and task apps require behavior change rather than capturing work from where it happens.
- **For:** Program managers, team leads, consultants running many meetings
- **Evidence:** T240 (22 findings) includes a request for a self-completing to-do list that turns meeting commitments into tasks (#18817) and notes that conversational capture avoids behavior change (#15373). T137 (38 findings, 19 in the last 90 days) wants an agent that tracks task completion across Gmail and calendar (#4147).
- **Existing alternatives:** Granola, Otter, Fireflies, Notion AI. They summarize but rarely close the loop on follow-through.
- **MVP:** Upload a transcript or paste notes. It outputs an action register (who, what, when, confidence), draft follow-up emails, and a 'dropped ball' checklist. The fuller product adds Calendar and Gmail integration, and nudges when a promise goes quiet.
- **Build notes:** Next.js, Supabase, LLM structured output, Google Calendar and Gmail integrations in later phases. The hardest part is reliable owner and date extraction and avoiding invented tasks. Cost is cents per meeting.
- **Demo hook:** A messy 40-minute transcript becomes a clean action register in 10 seconds, with a click that opens three drafted follow-up emails.
- **Post angle:** 'As a former PM, I know most meeting notes are never read. I built what I wish I'd had.' The angle is about follow-through.
- **Risks:** Meeting-recorder tools are adding action items natively. Differentiation is in follow-up tracking and chasers.
- **Themes:** T240 Agent-native task management and scheduled automations; T137 Personal super-assistant across apps that takes actions

What people said:

> “Sam Altman's number one, ask for an AI app. It's the self-completing to-do list.” — swyx, Latent Space, 2026-03-20 ([link](https://latent.space/p/dreamer/))
>
> “AI as especially helpful for managing focus and organization—acting as external scaffolding for planning, memory, and task follow-through” — Don't Worry About the Vase, 2026-03-26 ([link](https://thezvi.substack.com/p/ai-161-part-1-80000-interviews))
>
> “They all require me to change my behavior. Morpheus doesn’t.” — Rohit Krishnan, Exponential View, 2026-02-20 ([link](https://www.exponentialview.co/p/entering-the-trillion-agent-economy))
>
> “Agents nag me about a document I haven’t signed” — Ben Tossell, Ben's Bites, 2026-10-06 ([link](https://www.bensbites.com/p/thoughts-from-san-francisco))

### 8. AI Use-Case Finder

**Interview a team about its workflows and get a ranked list of AI opportunities with time saved, risk and who should try each first.**

*Effort: 3-6 weeks · Confidence: high · 112 findings from 14 sources · pain point 84, debate 10, tool or technique 9, build request 4, workaround 2, tool complaint 2, link shared 1*

- **Problem:** Companies can't identify concrete AI applications, adoption stays with early adopters, and managers lack use-case discovery and change-management tools.
- **For:** Team managers, transformation leads, small-business owners, consultants
- **Evidence:** T114 (42 findings) shows companies can't identify use cases (#19109), and small companies want outsourced help keeping up (#24210). T127 describes a delegation framework weighing baseline time, success probability and evaluation cost, and T173 shows no measurable ROI (score 133.4).
- **Existing alternatives:** Consultants, internal examples shared in Slack, generic AI-ideas lists. They are costly or not specific to a team's work.
- **MVP:** A guided chat that interviews you about your week and turns it into a task inventory. It scores each task with the delegation framework (time spent, success likelihood, review cost) and outputs a one-page prioritized plan with suggested prompts or tools. The fuller product adds team surveys and a rollout tracker.
- **Build notes:** Next.js, Supabase, structured LLM output, PDF export. The hard part is making recommendations specific and honest about review costs. Cost is about 10-20 cents per session.
- **Demo hook:** Answer 6 questions about a marketing coordinator's week, then see a ranked table: 'Weekly report: save 3h, low risk, start here.'
- **Post angle:** 'My old PM brain meets AI: a free tool that finds where your team should and shouldn't use AI.' It plays on the MBA and PM background.
- **Risks:** Quality depends on interview depth. Without feedback on whether suggestions worked, it risks being a one-time report.
- **Themes:** T114 Organizations can't redesign workflows or scale AI adoption; T127 AI productivity gains limited by review and non-coding bottlenecks; T173 Enterprise AI pilots show no measurable ROI

What people said:

> “they just have to figure out what to do with it” — IAmGraydon, Hacker News — Ask HN, 2026-04-27 ([link](https://news.ycombinator.com/item?id=47928683))
>
> “can’t just hire a team for keeping up with the frontier” — Keshav, Ben's Bites, 2026-10-22 ([link](https://www.bensbites.com/p/claudes-personal-agent))
>
> “How the people, teams of companies, can democratize AI & amplify the most valuable capabilities in an organization.” — Arvind KC, Tomasz Tunguz, 2026-10-28 ([link](https://tomtunguz.com/arvind-kc-office-hours/))
>
> “Engineering leaders went into AI expecting 2-3x productivity gains but are landing closer to 30%.” — Augment Code, Tomasz Tunguz, 2026-07-21 ([link](https://tomtunguz.com/ai-engineering-productivity-anything-but-normal/))

### 9. Signal Brief

**A low-hype daily or weekly digest of the AI news and newsletters you follow, tuned to your job, with 'what this means for you'.**

*Effort: 3-6 weeks · Confidence: medium · 94 findings from 10 sources · tool or technique 29, build request 28, pain point 22, workaround 12, debate 2, link shared 1*

- **Problem:** AI news is hype-driven and overwhelming, independent blogs are hard to follow, and workers can't tell what changes affect them.
- **For:** Knowledge workers, managers and operators tracking AI
- **Evidence:** T069 (56 findings, 9 sources) includes a request for an agent that reads all subscribed newsletters and sends key highlights (#14832), and a curated feed on emerging tech over product announcements (#2985). T137 wants a Daily Brief with real customization (#22252).
- **Existing alternatives:** TLDR, Rundown AI, smol.ai news, RSS readers. They are one-size-fits-all and don't filter by role.
- **MVP:** Forward newsletters or paste RSS feeds, state your role and what you ignore. It emails a weekly 5-item brief with a hype score and a 'try this Monday' action. The fuller product adds page-change monitors and a personal topic memory.
- **Build notes:** Next.js, Resend inbound email parsing, RSS fetchers, an LLM ranking and summary pipeline, Supabase. Cost is about 5-30 cents per user per week. The hard part is email parsing and source dedupe.
- **Demo hook:** Twelve newsletters turn into one 2-minute email with 'ignore this, skim this, act on this' labels.
- **Post angle:** 'I unsubscribed from 12 AI newsletters and built one that only tells me what matters for my job.'
- **Risks:** A crowded category with newsletter fatigue. Distribution is hard, and ChatGPT scheduled tasks could offer a similar service.
- **Themes:** T069 Keeping up with AI news and filtered feeds; T137 Personal super-assistant across apps that takes actions

What people said:

> “build a tool that each day goes through all newsletters I'm subscribed to” — Colossus, Ben's Bites, 2026-10-29 ([link](https://www.bensbites.com/p/ai-is-overwhelming-and-im-doing-it))
>
> “would be nice to have 1 or a few sites with emerging tech” — BtM909, Hacker News — Ask HN, 2026-09-02 ([link](https://news.ycombinator.com/item?id=49535272))
>
> “build prototypes for workers to better navigate constantly-evolving AI capabilities” — Sayash Kapoor, Rishi Bommasani, Arvind Narayanan, AI as Normal Technology, 2026-11-10 ([link](https://www.normaltech.ai/p/the-missing-quadrant-in-responses))
>
> “If this is to be any good you need to be able to give it instructions” — Zvi Mowshowitz, Don't Worry About the Vase, 2026-05-22 ([link](https://thezvi.substack.com/p/gemini-35-flash-looks-good-for-how))

### 10. SOP Interviewer

**Talk through how you do your job and get a clean, maintained SOP that humans and AI agents can both follow.**

*Effort: 3-6 weeks · Confidence: medium · 49 findings from 12 sources · build request 17, pain point 14, tool or technique 8, workaround 6, tool complaint 2, link shared 1, debate 1*

- **Problem:** Know-how lives in people's heads, onboarding relies on apprenticeship, and agents lack context about how the business actually runs.
- **For:** Team leads, ops managers, small-business owners, departing or onboarding employees
- **Evidence:** T307 (17 findings) and T288 (16 findings) show demand for documenting tacit knowledge so new hires ramp faster (#23885) and for a context database of SOPs (#10945). T258 asks for shared company memory instead of re-explaining context (#24180).
- **Existing alternatives:** Scribe, Notion docs, consultants mapping processes. They record clicks but don't ask the questions that surface judgment calls and exceptions.
- **MVP:** A voice or text interviewer that asks follow-ups ('what if the client doesn't reply?', 'who approves?'), then produces an SOP with steps, decision points, exceptions and a checklist. The fuller product adds a shared library, staleness reminders and an agent-ready export.
- **Build notes:** Next.js, Whisper or browser speech-to-text, an LLM for interview flow and structured output, Supabase. The hardest part is interview quality, which needs good prompting. Cost is about 10-30 cents per SOP.
- **Demo hook:** A 2-minute ramble about onboarding a client turns into a polished SOP with an 'exceptions' section nobody had written.
- **Post angle:** 'Every company has a 'ask Sarah' process. I built an AI that interviews Sarah.' It's relatable and plays to the PM's process-mapping skills.
- **Risks:** Chat apps can do a basic version. Differentiation depends on interview quality and keeping SOPs maintained.
- **Themes:** T307 Capturing specs, intent and tacit knowledge for agents; T288 Tacit knowledge and company brain for agents; T258 Company knowledge and shared team context

What people said:

> “Most companies are practically apprenticeships.” — Aaron Levie, Latent Space, 2026-03-05 ([link](https://latent.space/p/box/))
>
> “Sitting alongside retrieval is the context database, the recipe book of how each business actually runs.” — Tomasz Tunguz, Tomasz Tunguz, 2026-05-27 ([link](https://tomtunguz.com/harnessing-ai/))
>
> “Implicit knowledge — knowledge that an agent can’t explain in natural language, code, or other explicit form — won’t survive these handoffs.” — Timothy B. Lee, Understanding AI, 2026-05-06 ([link](https://www.understandingai.org/p/i-dont-think-we-are-close-to-ai-scientists))
>
> “Employees can share skills and company memory instead of re-explaining context in every chat.” — Ben's Bites, 2026-10-15 ([link](https://www.bensbites.com/p/prompt-tips-from-anthropic))

### 11. Pilot Scorecard

**A lightweight way for teams to measure whether an AI pilot is actually saving time, with surveys, minutes-saved logs and a go/no-go summary.**

*Effort: 3-6 weeks · Confidence: medium · 98 findings from 13 sources · pain point 67, debate 18, build request 5, tool or technique 3, workaround 2, tool complaint 2, link shared 1*

- **Problem:** Companies report little measurable return on AI spend, few track any AI metric, and mandates lead to gaming of usage counts.
- **For:** AI program owners, department heads, consultants running pilots
- **Evidence:** T173 (31 findings) says only about 2% of S&P 500 companies that report AI impact track a metric (#14714) and organizations lack a clear accounting of costs and benefits (#19550). T177 and T144 cover spend with no ROI visibility and gamed usage counts.
- **Existing alternatives:** Vendor dashboards, the Ramp AI Index, ad hoc surveys. They measure logins and tokens rather than real workflow time saved.
- **MVP:** Define a workflow and baseline time, send a 30-second weekly pulse to pilot users, and get a dashboard with time saved, quality issues, review time and a verdict (scale, fix, kill). The fuller version adds Slack check-ins and a pilot-to-production tracker.
- **Build notes:** Next.js, Supabase, Slack webhooks, a charting library. It's mostly CRUD and charts. The hardest part is survey design and honest calculations including review time. Cost is near zero.
- **Demo hook:** A dashboard shows 'Claimed 5h/week saved, net 1.8h after review time. Verdict: fix the workflow, then scale.'
- **Post angle:** 'Everyone says AI saves time. Here's a scorecard that tells you whether it really does.' It speaks to PMs and managers.
- **Risks:** A B2B tool with a slow sales cycle. Adoption depends on managers running pilots, so go after consultants and small teams first.
- **Themes:** T173 Enterprise AI pilots show no measurable ROI; T177 Enterprise AI spend lacks ROI visibility; T144 Mandated AI usage and low-quality AI output erode trust

What people said:

> “only ~2% track a metric for it” — Ben Tossell, Ben's Bites, 2026-10-01 ([link](https://www.bensbites.com/p/openai-devday-2026))
>
> “the returns on that investment have yet to materialize as broad productivity gains” — Sayash Kapoor, Rishi Bommasani, Arvind Narayanan, AI as Normal Technology, 2026-11-10 ([link](https://www.normaltech.ai/p/the-missing-quadrant-in-responses))
>
> “you get a lot of projects that don't make sense, which then quietly die” — nitwit005, Hacker News — Ask HN, 2026-08-31 ([link](https://news.ycombinator.com/item?id=49510066))
>
> “Productivity is up for individuals, but she doesn’t seeing proportional gains at the organization level.” — Azeem Azhar, Exponential View, 2026-05-29 ([link](https://www.exponentialview.co/p/live-with-azeem-ai-and-roi))

### 12. Show Your Sources

**Paste an AI report plus its sources and get every claim checked, with exact quotes to Ctrl-F and unsupported claims flagged.**

*Effort: 3-6 weeks · Confidence: medium · 73 findings from 12 sources · pain point 36, tool or technique 14, build request 13, debate 5, tool complaint 3, workaround 2*

- **Problem:** AI output is almost right with fabricated citations, and verification is hard without expertise. Data agents return final numbers with nothing to check.
- **For:** Analysts, researchers, consultants, writers, lawyers
- **Evidence:** T153 (36 findings, 10 sources) shows requests for tools that check whether AI-generated research is accurate (#12493), a fact checker for drafts (#20995), and checkable artifacts (#7288). T368 and T255 add demand for verified numbers and cheap verification.
- **Existing alternatives:** Manual cross-checking, asking another model, Gemini highlighted citations. None audits a given document against its own sources.
- **MVP:** Upload a report and its source PDFs or URLs. It lists each claim with a verdict (supported, partial, unsupported), the exact quote and page, and a flagged number list. The fuller product adds a browser extension and a verification log.
- **Build notes:** Next.js, PDF text extraction, an LLM claim extractor plus quote matching with fuzzy string checks (quotes verified in code, not by the LLM). Hard parts are long documents and avoiding false verification. Cost is about 20-60 cents per report.
- **Demo hook:** A consulting-style AI report with 4 red 'unsupported' flags and 1 invented citation highlighted, with a click-through to the matching source quote.
- **Post angle:** 'I audited an AI-written report and found 4 claims no source supports. So I built the auditor.'
- **Risks:** Verification can give false confidence. Models may improve at citations, and it has to be honest about limits.
- **Themes:** T153 Verifying AI output and research for accuracy; T368 Condensing long documents, filings and papers reliably; T255 Legal AI is hard to verify and trust

What people said:

> “A public company even republished an AI-generated report from the platform, mistaking it for professional research” — AINews (smol.ai), 2025-12-22 ([link](https://news.smol.ai/issues/25-12-22-not-much/))
>
> “what i really want as a writer is an automated fact checker and alternative viewpoint giver” — Prakesh, Don't Worry About the Vase, 2026-01-13 ([link](https://thezvi.substack.com/p/claude-coworks))
>
> “provide the user with checkable artifacts” — Hamel Husain, Hamel Husain, 2026-06-29 ([link](https://hamel.dev/blog/posts/eval-smell/))
>
> “the parts that count still count and one needs to pay attention” — Zvi Mowshowitz, Don't Worry About the Vase, 2026-10-28 ([link](https://thezvi.substack.com/p/anthropic-files-its-s-1))

### 13. Which Model?

**A task-aware picker and side-by-side comparison so non-experts know which AI to use for what, and what it costs.**

*Effort: 1-2 weekends · Confidence: medium · 117 findings from 11 sources · pain point 48, tool or technique 21, tool complaint 20, debate 19, build request 5, workaround 2, link shared 2*

- **Problem:** Models are jagged, modes and plans are confusingly named, and users pay for several subscriptions and cross-check by hand.
- **For:** Everyday multi-chatbot users, students, small teams
- **Evidence:** T361 (17 findings) shows requests for a workspace to compare models in one place (#8019) and notes frontier models are jagged (#3484). T161 notes confusing product modes (#22168) and that one in five users has more than one chatbot app installed (#10750).
- **Existing alternatives:** Poe, Inforno, LMArena, OpenRouter chat UI (reported buggy in T362). They are model-centric rather than task-centric.
- **MVP:** Describe a task and get a recommended model and mode with a reason, then run it side-by-side on 2-3 models with your own API keys, with cost per answer. The fuller product adds saved task recipes and a personal win-rate record.
- **Build notes:** Next.js, OpenRouter for unified API access (user keys), streaming comparison UI. The hardest parts are keeping the recommendations current and key management. Cost is nearly zero with BYO keys.
- **Demo hook:** One prompt, three model answers streaming side by side, then a card: 'Winner for this task: Model B at 1/5 the price.'
- **Post angle:** 'I pay for 3 AI subscriptions and still don't know which to use. So I built a tiebreaker.'
- **Risks:** A crowded space (Poe, OpenRouter, LMArena). Model names and capabilities change quickly, so recommendations need upkeep.
- **Themes:** T361 Choosing and juggling multiple frontier models; T161 Chatbot switching and model confusion; T081 Expensive frontier models push users toward cost-aware routing

What people said:

> “you can access and compare multiple models in one workspace” — Join_TalkoryAi, Hacker News — Ask HN, 2026-08-13 ([link](https://news.ycombinator.com/item?id=49290713))
>
> “Today, it takes a lot of work and fiddling to make sure you’re not missing out on capabilities.” — Nathan Lambert, Interconnects, 2026-01-11 ([link](https://www.interconnects.ai/p/use-multiple-models))
>
> “Which means you only would use it either if you are doing relatively advanced math” — Zvi Mowshowitz, Don't Worry About the Vase, 2025-12-05 ([link](https://thezvi.substack.com/p/deepseek-v32-is-okay-and-cheap-but))
>
> “One in five AI chatbot users now has more than one app installed” — Alberto Romero, The Algorithmic Bridge, 2026-03-04 ([link](https://www.thealgorithmicbridge.com/p/how-many-people-does-it-take-to-kill))

### 14. Human Meter

**A browser extension that estimates how AI-written a LinkedIn or X post is and lets you mute the slop.**

*Effort: 3-6 weeks · Confidence: low · 117 findings from 12 sources · pain point 58, build request 25, tool or technique 19, workaround 9, tool complaint 4, debate 2*

- **Problem:** Feeds and comments are flooded with AI-generated text, and readers can't tell human from AI.
- **For:** Heavy LinkedIn and X readers, creators, recruiters
- **Evidence:** T040 (72 findings, 10 sources) includes explicit requests for a 'percent human' score on social accounts (#8209) and a cross-platform Chrome extension that flags AI content on X, Substack, Medium, LinkedIn and Reddit (#4815). T175 and T344 add interest in detection and provenance.
- **Existing alternatives:** Pangram's Chrome extension, hn-ai.org, manual tells. Coverage is limited and detectors give false positives.
- **MVP:** An extension that adds a small badge to posts based on stylistic tells (triads, 'it's not X, it's Y', em dashes) and an LLM check, with a 'hide posts above 80%' toggle. The fuller version adds an account-level score and a shared community flag list.
- **Build notes:** Chrome extension with a content script, backend LLM scoring with caching, Supabase. Hard parts are DOM changes on LinkedIn and X, and detector accuracy. Cost depends on volume, so cache and only score on visibility.
- **Demo hook:** A LinkedIn feed scrolls by with green and red badges and a 'slop hidden: 14 posts' counter.
- **Post angle:** 'I built a slop detector for LinkedIn. Then I found out how many of my own posts it flagged.' A self-aware hook invites replies.
- **Risks:** Detection is unreliable and false positives can offend people. Platform ToS and DOM scraping, and Pangram already operates here.
- **Themes:** T040 Filtering AI slop from feeds, search and forums; T175 Detecting and disclosing AI-written text; T344 AI writing detection and authorship verification

What people said:

> “I’d also like to see automatic ‘percent human’ attached to accounts automatically” — Zvi Mowshowitz, Don't Worry About the Vase, 2026-09-03 ([link](https://thezvi.substack.com/p/ai-184-post-post-mortem))
>
> “a Chrome extension that works across platforms (X, Substack, Medium, LinkedIn, Reddit, etc.)” — The Algorithmic Bridge, 2026-05-13 ([link](https://www.thealgorithmicbridge.com/p/how-this-small-startup-achieved-a))
>
> “removing the "it's not A, it is B" tell would be rather simple and involve a modification of the system prompt” — stuxnet79, Hacker News — Ask HN, 2026-10-29 ([link](https://news.ycombinator.com/item?id=50284849))
>
> “How will HN make the transition when this happens?” — amichail, Hacker News — Ask HN, 2026-10-27 ([link](https://news.ycombinator.com/item?id=50265376))

### 15. Teach Me Anything

**Give it a topic and it runs a Socratic mini-course with quizzes, spaced repetition and progress tracking.**

*Effort: 3-6 weeks · Confidence: medium · 61 findings from 7 sources · tool or technique 22, pain point 15, workaround 13, debate 6, build request 5*

- **Problem:** People use LLMs as tutors but chat has no curriculum or memory of progress, and AI shortcuts skip the productive struggle.
- **For:** Self-directed adult learners, career switchers, students
- **Evidence:** T238 (44 findings) includes requests for an app where you suggest a subject and it teaches interactively and tests knowledge (#23073), and an AI tutor that tracks spaced-repetition timing (#7640). T309 requests tutoring that pushes students to solve problems rather than giving answers (#10391).
- **Existing alternatives:** ChatGPT study mode, Khanmigo, Anki, NotebookLM, DIY /teach-me prompts. They lack persistent curriculum and spaced review in one place.
- **MVP:** Enter a topic and level to get a 10-lesson outline. Each lesson is a Socratic dialogue with a quiz, and missed items return later via spaced repetition. The fuller version adds source import (papers, videos) and streaks.
- **Build notes:** Next.js, Supabase, LLM with structured lesson state, a simple SM-2 spaced repetition algorithm. The hardest part is keeping lessons accurate and on-level. Cost is about 5-20 cents per lesson.
- **Demo hook:** Type 'teach me options trading', then watch a lesson, a quiz miss, and a 'review tomorrow' card appear.
- **Post angle:** 'I used AI to learn a new skill, but not by asking it for answers. I built a tutor that makes me struggle.'
- **Risks:** The big chat apps are adding learning modes. Retention and content accuracy are real concerns.
- **Themes:** T238 Structured LLM-guided self-learning workflows; T309 AI shortcuts skip the productive struggle in learning

What people said:

> “Socratic method, can be really useful here, i have been planning an app to do exactly that” — rhythmshahriar, Hacker News — Ask HN, 2026-08-10 ([link](https://news.ycombinator.com/item?id=49246873))
>
> “I really want an AI tutor (ai learning harness) that I can give it a topic, it can synthesize information from sources, gauge my level” — taosx, Hacker News — Ask HN, 2026-08-01 ([link](https://news.ycombinator.com/item?id=49138466))
>
> “there would be some hot app that let you suggest a subject” — iknownthing, Hacker News — Ask HN, 2026-06-23 ([link](https://news.ycombinator.com/item?id=48649857))
>
> “Students who were given a personalized sequence of problems by an AI tutor scored 0.15 standard deviations higher” — Ethan Mollick, One Useful Thing, 2026-05-26 ([link](https://www.oneusefulthing.org/p/choosing-to-stay-human))

### 16. AI-Era Interview Kit

**Generate interview exercises and scoring rubrics that test judgment with AI assistants, not memorized answers.**

*Effort: 3-6 weeks · Confidence: low · 40 findings from 4 sources · tool or technique 19, pain point 11, debate 5, workaround 4, build request 1*

- **Problem:** Traditional interviews and take-homes no longer reveal real skill when candidates can use AI, and managers don't know how to assess AI-assisted work.
- **For:** Hiring managers, recruiters, small-business owners, including for non-engineering roles
- **Evidence:** T248 (40 findings, 11 in the last 90 days) shows interviewers piloting AI-native assessments (#4768, #24512) and struggling to verify real ability (#19030), and wanting repeatable low-pressure interviews (#10212).
- **Existing alternatives:** HackerRank-style platforms, ad hoc work trials, Sierra's internal approach. They are engineering-centric and not rubric-driven for everyone else.
- **MVP:** Enter a role and level. It generates a scenario with a flawed AI output to critique, a vague brief to scope, and an 'explain your choices' prompt, plus a 1-5 rubric and follow-up questions. The fuller version adds a candidate-facing session with a scored report.
- **Build notes:** Next.js, Supabase, LLM generation, shareable candidate links. The hard part is rubric quality across roles. Cost is cents per kit.
- **Demo hook:** Enter 'marketing manager', then see an exercise with an AI-written campaign brief containing 3 planted errors, plus a scoring rubric.
- **Post angle:** 'Interviews are broken now that candidates use AI. Here's the kit I'd use as a hiring manager.'
- **Risks:** Hiring tools face a long sales cycle, and quality is hard to prove. Free kit generation is a hook but monetization is unclear.
- **Themes:** T248 Interviewing candidates who use AI assistants

What people said:

> “This month, I laid the traditional coding interview to rest.” — Felix Rieseberg, AINews (smol.ai), 2026-10-28 ([link](https://latent.space/p/ainews-anthropic-ends-coding-interviews-hunger-beats-tenure/))
>
> “debugging/review focused interviews where candidates improve a medium-sized codebase with coding agents.” — Ben's Bites, 2026-04-23 ([link](https://www.bensbites.com/p/chatgpts-nano-banana))
>
> “we'll actually try to build the whole thing with x or cloud code” — David Singleton, Latent Space, 2026-03-20 ([link](https://latent.space/p/dreamer/))
>
> “about 80% of the dev candidates that I interview tell me that they aren't writing much code themselves anymore” — mdwelsh, Hacker News — Ask HN, 2026-09-19 ([link](https://news.ycombinator.com/item?id=49768826))

### 17. Pivot Plan

**Upload your resume and get a concrete 30-60-90 day plan toward adjacent roles that AI is less likely to squeeze, with practice tasks.**

*Effort: 3-6 weeks · Confidence: low · 36 findings from 9 sources · pain point 23, build request 4, debate 3, tool or technique 3, workaround 2, link shared 1*

- **Problem:** Workers fear displacement, can't see comparable alternatives, and juniors lose the learning pipeline as entry-level tasks get automated.
- **For:** Early-career professionals, laid-off knowledge workers, career changers
- **Evidence:** T324 (18 findings) asks for a concrete, actionable adaptation guide rather than platitudes (#23641) and transition counseling (#20303). T286 requests simulated work environments for early-career learning (#14387).
- **Existing alternatives:** Career coaches, LinkedIn Learning, ChatGPT resume advice. They are generic and don't provide hands-on practice.
- **MVP:** Upload a resume and goals. It returns 3 adjacent role paths with a skill gap analysis, a 30-60-90 day plan, and 3 realistic work simulations (e.g. 'write a PRD for this scenario') with AI feedback. The fuller version adds portfolio building and job tracking.
- **Build notes:** Next.js, Supabase, resume parsing, LLM structured plan and feedback. The hard parts are role-market accuracy and avoiding generic advice. Cost is about 10-30 cents per plan.
- **Demo hook:** Upload a resume and watch a roadmap appear: 'Program Manager to AI Operations Lead, 3 skill gaps, week 1 task.'
- **Post angle:** 'I'm an MBA who moved from tech program management into building apps. Here's the tool I wanted for pivoting.'
- **Risks:** A sensitive and crowded category with generic AI advice. Quality of labor-market insight needs care.
- **Themes:** T324 Support for displaced developers and career transitions; T286 Entry-level jobs shrinking and juniors lacking a path to experience

What people said:

> “people really, really need this and, on the other hand, I don’t have a solid answer either” — Alberto Romero, The Algorithmic Bridge, 2026-03-17 ([link](https://www.thealgorithmicbridge.com/p/how-to-survive-the-ai-age-a-concrete))
>
> “Freelance careers/unemployment counsellor for devs.” — andyjohnson0, Hacker News — Ask HN, 2026-10-10 ([link](https://news.ycombinator.com/item?id=50036432))
>
> “I cannot imagine a fit for me at any place yet” — bumicodes, Hacker News — Ask HN, 2026-10-10 ([link](https://news.ycombinator.com/item?id=50036432))
>
> “you create simulative jobs for them” — Alessio Fanelli, Latent Space, 2026-03-17 ([link](https://latent.space/p/felix-anthropic/))

### 18. Good Enough Gate

**A simple guardrail for heavy AI users that sets a session budget, enforces stopping points and decides when output is good enough.**

*Effort: 1-2 weekends · Confidence: low · 64 findings from 9 sources · pain point 32, workaround 9, debate 9, build request 9, tool or technique 5*

- **Problem:** Running agents all day drains energy, erodes work-life boundaries and creates compulsive overuse, with no tool to decide when to stop.
- **For:** Heavy AI users, solo builders, knowledge workers running multiple agents
- **Evidence:** T061 (64 findings, 9 sources) lists workarounds like capping sessions to 2-4 and forced offline time. Requests include tools to decide when AI output is good enough (#23649), a discipline aid against abandoned side projects (#5332), and an 'Oura for attention' (#12746).
- **Existing alternatives:** Cold Turkey, timers, grayscale screens, willpower. None is built for AI workflow overuse.
- **MVP:** A desktop-style web app where you set a goal, a time or task budget and a 'done' definition. It checks in with a short rubric ('does this meet the bar?'), logs sessions and gives an evening wrap-up. The fuller version adds a browser extension for tracking AI tabs and break nudges.
- **Build notes:** Next.js PWA, Supabase, optional Chrome extension for tab time tracking. The hardest part is making it sticky rather than another thing to ignore. Cost is minimal.
- **Demo hook:** A timer hits its limit and a card says: 'You set 'good enough' = 3 bullet summary. You have it. Stop here?'
- **Post angle:** 'AI made me more productive and more exhausted. I built a stop button.' It's honest and relatable.
- **Risks:** Habit tools struggle with retention, and the demo value is lower than in other ideas. It may stay a niche.
- **Themes:** T061 Agent overload, burnout and loss of focus

What people said:

> “knowing when to stop using AI once you find it useful” — Alberto Romero, The Algorithmic Bridge, 2026-03-17 ([link](https://www.thealgorithmicbridge.com/p/how-to-survive-the-ai-age-a-concrete))
>
> “the critical skill to develop here is discipline” — Simon Willison, Simon Willison's Weblog, 2026-05-31 ([link](https://simonwillison.net/2026/May/31/the-solution-might-be-cancelling-my-ai-subscription/))
>
> “I end up just laying there doing the luge while all the ideas swirl around my head when I should be reading + sleeping.” — Ben Tossell, Ben's Bites, 2026-08-25 ([link](https://www.bensbites.com/p/agents-on-your-mobile))
>
> “Oura for your attention on the desktop” — AINews (smol.ai), 2026-01-08 ([link](https://news.smol.ai/issues/26-01-08-not-much/))

