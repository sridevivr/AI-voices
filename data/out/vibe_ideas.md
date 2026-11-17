# Vibe-codeable app ideas from a year of AI commentary

For a non-engineer building apps (quick wins to ambitious products) with AI coding tools and sharing them on LinkedIn/X. Drawn from 30,139 findings in 1,231 themes; only themes about everyday users, knowledge workers, students, creators and business teams. Generated 2026-11-17. Counts, quotes and links come straight from the findings; the write-ups are Sonnet's.

## What non-developers struggle with

- Non-developers are drowning in AI output: AI-written messages from colleagues, AI slop in feeds, and agent reports too long to review. Condensing and filtering are repeated demands (T141, T263, T037, T429).
- Trust and verification are unsolved. People can't tell whether AI facts are right, whether text is AI-written, or which model actually answered (T079, T105, T202). Checking often costs as much as it saves.
- Paid AI subscriptions are confusing and unstable. Usage caps, plan labels, model lineups and billing changes are opaque, so people want a dashboard, a guide or a comparison (T085, T113, T155, T255).
- Writers and professionals dislike generic AI prose and flattering chatbots. They keep building workarounds like voice skill files, critic-only prompts and anti-sycophancy instructions, and want persistent controls (T038, T089, T133, T169).
- Memory and context are hard to carry across chats, tools and teammates. Users re-explain everything, can't inspect or scrub memory, and can't move it between assistants (T099, T292, T285).
- Non-coders want agents for email, calendar and daily admin but face setup friction, permission worries and a lack of what-is-it-for guidance. Heavy agent use also causes attention fragmentation and burnout (T061, T094, T247, T044).

## Ideas

### 1. Ask-First: Condense AI-Written Messages

**Paste or forward a long email, Slack thread or doc and get the actual ask, decision needed, deadline and what's unsupported, in five lines.**

*Effort: 1-2 weekends · Confidence: high · 120 findings from 11 sources · pain point 62, tool or technique 23, build request 18, workaround 15, tool complaint 2*

- **Problem:** Colleagues send long AI-polished messages that bury the point. Recipients can't tell what is asked or what the sender really thinks, and review becomes the bottleneck.
- **For:** Managers, program managers, and anyone receiving heavy email, proposals or status docs
- **Evidence:** T141 has 34 findings from 9 sources, 14 in the last 90 days, mostly pain points and workarounds such as asking for the original prompt or capping length. T140 (37 findings) shows demand for inbox triage and summarisation, and T263 (31 findings) shows people cannot absorb the volume of AI output.
- **Existing alternatives:** Gmail and Outlook built-in summaries (generic, miss the ask), asking ChatGPT manually (copy-paste, no consistent format), Superhuman AI. None extracts the ask, decision, deadline and unsupported claims in a consistent format, or flags that the text looks padded.
- **MVP:** Web app plus Gmail add-on or Chrome extension. Paste text or click on an email and get a fixed card: The ask, Decision needed, Deadline, Key facts, Things stated without support, Suggested one-line reply. Adds a 'padding score' and tone read. Fuller product adds Slack/Teams threads, doc links, and a team-wide 'send with the ask first' checker for outgoing messages.
- **Build notes:** Next.js on Vercel, an LLM API with structured JSON output, Chrome extension for Gmail, Supabase for auth. Hardest parts: Gmail DOM injection and OAuth review for a Gmail add-on, so start with paste-in and a simple extension. Cost: a few cents per 100 summaries with a small model.
- **Demo hook:** Split screen: a 600-word rambling AI-polished vendor email on the left, a clean 5-line card on the right with the actual ask and deadline highlighted. Takes 10 seconds.
- **Post angle:** "Half the emails in my inbox are AI-written and none of them say what they want. So I built a button that finds the ask." Angle: program manager frustration with AI-polished status updates.
- **Risks:** Gmail and Outlook may add similar summaries natively. Needs a clear differentiator (ask/decision extraction, unsupported-claims flag). Retention depends on a lightweight integration.
- **Themes:** T141 AI-written messages and documents burden recipients; T140 Email clients and agents for inbox triage; T263 Absorbing and reviewing the flood of agent output; T429 AI-generated spam, cold outreach and low-quality submissions

What people said:

> “I have my own Claude. If I'm asking you, i want to know what YOU THINK.” — Charity Majors, Bluesky, 2026-09-14 ([link](https://bsky.app/profile/charity.wtf/post/3mviyfjhktk2i))
>
> “Sometimes I click it. Sometimes I wonder if the person on the other end can tell.” — Tomasz Tunguz, Tomasz Tunguz, 2026-03-08 ([link](https://tomtunguz.com/is-this-tomaszs-agent/))
>
> “Search Gmail by intent, or filter your to-dos.” — Ben's Bites, 2026-09-22 ([link](https://www.bensbites.com/p/what-can-you-build-with-jev))
>
> “It's hard to process so much text from a review that I don't always read it all either.” — Ben Tossell, Ben's Bites, 2026-09-04 ([link](https://www.bensbites.com/p/scraping-107m-rows-of-data-to-build))

### 2. Sloplint

**A linter for your writing: highlights AI tells, explains why, and suggests edits you accept or reject one by one without wholesale rewrites.**

*Effort: 1-2 weekends · Confidence: high · 167 findings from 13 sources · pain point 61, tool or technique 36, tool complaint 24, workaround 21, build request 16, debate 9*

- **Problem:** AI-assisted text has stock phrases, padding and uniform polish that readers spot and discard. Prompting against it fails, and single-pass output lacks iteration.
- **For:** Professionals, bloggers, marketers and job seekers who draft with AI and send or publish it
- **Evidence:** T038 has 67 findings from 12 sources (36 pain points, 16 tool complaints), T430 has 21, T089 has 58 findings, and T281 asks for a tool to remove tells like 'it's not A, it's B'. The workarounds listed (anti-slop prompts, repeated revisions, manual editing) show people want a systematic tool.
- **Existing alternatives:** Pangram (detection, not editing), Havelock.AI and Tropes anti-slop instructions, Every's style guide skill, custom GPTs. Most are prompts or detectors; few give a line-by-line lint with diff-style accept/reject and a personal rule list.
- **MVP:** Paste text, see inline highlights for AI tells (stock phrases, em-dash overuse, 'not X but Y', hedging, rule-of-three, filler openers) with a severity score and a one-click fix suggestion shown as a diff. Fuller product adds a personal voice profile from your past writing, custom banned-phrase rules, and a browser extension for Gmail, LinkedIn and Google Docs.
- **Build notes:** Next.js plus a rule-based regex pass for known tells plus an LLM pass for subtler ones; diff UI using a diff library. Hardest part: keeping false positives low and edits minimal. Cost: pennies per document.
- **Demo hook:** A LinkedIn draft pasted in, 14 highlighted tells with a 'slop score: 82', then accept 6 fixes and the score drops to 19 while the meaning stays the same.
- **Post angle:** "I built a spellchecker for AI slop. Here's what it found in my own LinkedIn posts." Self-deprecating audit angle invites people to paste their own posts.
- **Risks:** Models may stop producing the tells, and chat apps could add self-editing. Detection arms race. Needs a voice-profile feature to stay differentiated.
- **Themes:** T038 Generic AI prose tells and slop; T430 AI prose sounds generic and needs style control; T089 Preserving personal voice when writing and editing with AI; T281 Chatbot personality, tone and style controls

What people said:

> “I don't need to start every response with "Fable sorry I need you to rewrite that"” — Rory Watts, Don't Worry About the Vase, 2026-09-05 ([link](https://thezvi.substack.com/p/claude-mythos-51-and-fable-51-capabilities))
>
> “Those revisions led to more convoluted writing and "Claudespeak" being inserted into the text” — Ethan Mollick, One Useful Thing, 2026-11-09 ([link](https://www.oneusefulthing.org/p/fable-52-and-jagged-agi))
>
> “can one tell AI not to write like ... AI? Is that possible?” — Bender, Hacker News — Ask HN, 2026-05-22 ([link](https://news.ycombinator.com/item?id=48235223))
>
> “removing the "it's not A, it is B" tell would be rather simple and involve a modification of the system prompt” — stuxnet79, Hacker News — Ask HN, 2026-10-29 ([link](https://news.ycombinator.com/item?id=50284849))

### 3. InboxChief: Plain-English Email Triage

**Define your triage rules in plain English and an agent labels, prioritizes and drafts replies in your Gmail with approval before anything is sent.**

*Effort: 3-6 weeks · Confidence: high · 116 findings from 13 sources · build request 36, pain point 35, tool or technique 23, workaround 21, tool complaint 1*

- **Problem:** Inboxes overwhelm people and built-in AI summaries and filters miss important mail. Users want controllable triage and drafts based on their own history.
- **For:** Managers, founders, and professionals with heavy email loads
- **Evidence:** T140 (37 findings, 13 build requests) asks for plain-English rules and personal-context triage. T061 (45 findings, 22 build requests) shows demand for an assistant spanning email, calendar and tasks. T006-style requests like #6229 on school email logistics show non-coders want actioning, not summaries.
- **Existing alternatives:** Superhuman split inboxes, Gmail filters and labels, custom Claude Code CLIs and skills, AI-secretary startups. DIY setups need coding skills, and Gmail's AI misses important items.
- **MVP:** Gmail OAuth, a rules box (e.g. 'anything from my boss or about the launch is urgent; newsletters go to a weekly digest'), a daily triage view with reasons for each ranking, and draft replies saved as Gmail drafts. Fuller product adds calendar awareness, learned rules from corrections, and a weekly 'what you ignored' review.
- **Build notes:** Next.js, Gmail API with restricted-scope OAuth (verification takes time, so launch in test mode with a small allowlist), Supabase, LLM with structured output. Hardest parts: OAuth verification, email privacy, and avoiding mislabeling. Cost: low if you run triage on subject, sender and snippet first.
- **Demo hook:** A 200-unread inbox turns into 7 'needs you today' items with one-line reasons, a 'why' for each, and 3 draft replies ready to review. Rules were typed in one sentence.
- **Post angle:** "I told my inbox my rules in plain English and it finally listened." Angle: a program manager's rules for what counts as urgent.
- **Risks:** Gmail's Gemini and Outlook Copilot are improving. Google's OAuth verification can block a public launch. Trust and privacy concerns for email access.
- **Themes:** T140 Email clients and agents for inbox triage; T061 Personal AI chief of staff and proactive daily assistant; T141 AI-written messages and documents burden recipients

What people said:

> “User-defined skills & rules. Programming in English” — Tomasz Tunguz, Tomasz Tunguz, 2026-05-13 ([link](https://tomtunguz.com/the-disappearance-of-email/))
>
> “I'm trying to train Claude to read the weekly emails from my kids school and reliably summarize them and print a list of action items.” — Charlotte Lee, Don't Worry About the Vase, 2026-02-12 ([link](https://thezvi.substack.com/p/ai-155-welcome-to-recursive-self))
>
> “truly context-aware assistance across email, docs, calendars, contracts, and more” — Latent Space, 2025-12-11 ([link](https://latent.space/p/the-future-of-email-superhuman-cto/))
>
> “you sent me a lengthy email? well, I had the AI read it!” — anildash.com, Bluesky, 2026-09-28 ([link](https://bsky.app/profile/anildash.com/post/3mwm6ykli7s25))

### 4. AI Plan Meter

**One dashboard that tells you how much of your Claude, ChatGPT, Gemini or Perplexity plan you've burned, what it's worth in API dollars, and when you'll hit the cap.**

*Effort: 3-6 weeks · Confidence: medium · 219 findings from 14 sources · pain point 124, tool complaint 45, build request 14, tool or technique 14, debate 13, workaround 8, link shared 1*

- **Problem:** Paying users can't tell how credits, weekly caps and session windows are consumed, and limits change quietly. Plan labels like 5x or 20x don't map to real usage.
- **For:** Heavy AI subscribers, freelancers, small teams and consultants paying for several AI plans
- **Evidence:** T085 (45 findings, 8 sources) and T113 (55 findings) both cover opaque caps, with #143 explicitly requesting an API-equivalent dollar metric. T255 (46 findings) adds expiring credits and billing failures. T181 (35 findings) adds silent price and plan changes.
- **Existing alternatives:** Trial and error, community estimates, outdated support articles, multiple accounts. No cross-provider tracker exists that is simple for non-developers.
- **MVP:** Manual-entry web app (no provider API needed): pick your plans, log or paste usage screenshots/numbers, and see a burn-rate projection, a cutoff warning, a plan-change log, and an 'is my $200 plan worth it' comparison. Fuller product adds a browser extension that reads usage pages, email alerts, vendor pricing-page change monitoring, and a cheapest-adequate-plan recommender.
- **Build notes:** Next.js plus Supabase; start with a manual-entry flow and screenshot parsing via a vision LLM. Hardest parts: no official usage APIs, so a scraping extension is fragile. Pricing-page monitor via scheduled fetch plus diff. Cost: low.
- **Demo hook:** Four plans on one screen with progress bars, a red banner 'You'll hit your Claude weekly cap Thursday 3pm', and a card showing 'you've used $412 of API-equivalent value on a $100 plan'.
- **Post angle:** "My AI subscription limits change every month and nobody tells me. I built a fuel gauge." Relatable for anyone running out of Claude mid-task.
- **Risks:** Providers may add native usage meters, and unofficial scraping can break. Retention requires an active data feed. A narrow audience of heavy users.
- **Themes:** T085 Opaque, shrinking AI subscription usage caps and quotas; T113 Opaque usage caps and plan limits on AI subscriptions; T255 Billing, refund, credit expiry and support failures at AI vendors; T181 Unpredictable AI vendor price, plan and model-access changes; T155 Confusing AI model lineups, modes and tool choice

What people said:

> “disclose subscription limits in a normalized API-budget-equivalent” — AINews (smol.ai), 2026-08-31 ([link](https://news.smol.ai/issues/26-08-31-not-much/))
>
> “The $200 OpenAI subscription plan is cutting weekly usage limits by 50%” — Don't Worry About the Vase, 2026-10-01 ([link](https://thezvi.substack.com/p/ai-188-gemini-dot-argon))
>
> “agents burn through those limits quickly” — Ethan Mollick, One Useful Thing, 2026-07-23 ([link](https://www.oneusefulthing.org/p/an-opinionated-guide-to-which-ai-b22))
>
> “You will have to buy usage credits for using Fable starting tomorrow.” — Ben's Bites, 2026-07-07 ([link](https://www.bensbites.com/p/my-thoughts-on-fable))

### 5. Which AI Should I Use? Task Router and Guide

**Describe the task and get a recommendation of which model and mode to use, why, and what it costs, with a side-by-side comparison of outputs on demand.**

*Effort: 3-6 weeks · Confidence: medium · 201 findings from 12 sources · pain point 101, tool or technique 26, tool complaint 25, debate 19, build request 18, workaround 10, link shared 2*

- **Problem:** Fast-changing products with unclear names, modes and limits make it hard to know which model or tool to use. Users juggle several subscriptions.
- **For:** Non-expert professionals and small teams using several AI tools
- **Evidence:** T155 (38 findings) has explicit build requests like #28605 for a guide telling non-experts which product to use. T202 (30 findings) shows confusion about which model actually answered. T199 (43 findings) shows cost-quality tradeoffs, and T190 (35 findings) shows demand for multi-model front ends.
- **Existing alternatives:** OpenRouter and Inforno (developer-oriented), manual copy-paste comparison, outside explainers. None offers a plain-English recommender for knowledge-work tasks.
- **MVP:** A web app with a task picker (draft a contract, analyze a spreadsheet, write a speech...) that returns a recommended model/mode, a cost estimate and a 'what it's bad at' note from a curated, maintainable table. Add a BYO-key side-by-side compare where one prompt goes to 2-3 models. Fuller product adds a changelog feed when lineups change.
- **Build notes:** Next.js, OpenRouter for BYO-key compare, a hand-curated JSON of model strengths that you update weekly (your edge as curator), Supabase. Hardest part: keeping the guide fresh. Cost: BYO keys means near zero.
- **Demo hook:** Type 'summarize a 90-page contract and flag risks'; the app recommends a model and mode with reasons, then runs the same prompt on three models side by side with cost shown.
- **Post angle:** "There are 14 AI models in my subscriptions and I don't know which to use. So I made a decision tree that updates weekly."
- **Risks:** Content maintenance burden, and rankings go stale. Vendors might simplify naming. Hard to prove accuracy.
- **Themes:** T155 Confusing AI model lineups, modes and tool choice; T202 Silent model swapping and unclear model or effort level; T199 Frontier models cost too much; need routing and price comparison; T190 Multi-model chat front ends with better UX and file handling; T113 Opaque usage caps and plan limits on AI subscriptions

What people said:

> “Keeping up is challenging, even if you are following this stuff closely.” — Ethan Mollick, Bluesky, 2026-07-26 ([link](https://bsky.app/profile/emollick.bsky.social/post/3mrl7ovnk2c2r))
>
> “you can access and compare multiple models in one workspace” — Join_TalkoryAi, Hacker News — Ask HN, 2026-08-13 ([link](https://news.ycombinator.com/item?id=49290713))
>
> “When you select GPT-5.2, what you are really getting is “auto” mode, where the AI decides which model to use, often a less powerful one.” — Ethan Mollick, One Useful Thing, 2026-02-18 ([link](https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the))
>
> “I find that almost entirely useless” — Simon Willison, Simon Willison's Weblog, 2026-08-30 ([link](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/))

### 6. MeetingToDone: Local Meeting Capture and Follow-Through

**A private Mac/web app that transcribes meetings without a bot, extracts decisions and owners, and tracks follow-ups until they're done.**

*Effort: 3-6 weeks · Confidence: medium · 124 findings from 13 sources · tool or technique 54, build request 38, pain point 19, workaround 11, link shared 1, tool complaint 1*

- **Problem:** Users want fast private transcription and meeting follow-ups without cloud bots, but most tools stop at a summary and don't follow up.
- **For:** Program managers, consultants and team leads who run many meetings
- **Evidence:** T215 has 41 findings with 9 build requests, including local-first dictation and meeting capture (#755, #6890) and coaching (#24099). T175 (39 findings) shows demand for private local voice tools. T285 and T233 show decisions and tacit knowledge getting lost.
- **Existing alternatives:** Granola, MacWhisper, Wispr Flow, Otter-style bots. These capture and summarise but rarely track whether decisions and action items actually happen, or give conversation coaching.
- **MVP:** Browser-based recorder or file upload using on-device or API transcription, extract decisions, action items with owners and dates, then a weekly 'what did we say we'd do' list that nudges via email. Fuller product adds calendar integration, Slack follow-up reminders, a meeting-coach metrics view (talk time, interruptions) and a team decision log.
- **Build notes:** Next.js, Whisper-based transcription (an API for the MVP; local later), LLM extraction, Supabase, Google Calendar API. Hardest parts: audio capture of system sound on the web, and speaker labels. Cost: a few cents per meeting hour with API transcription.
- **Demo hook:** Upload a 45-min recording; 60 seconds later: 4 decisions, 7 action items with owners, and a 'last week's items still open' panel.
- **Post angle:** "Meeting notes are not the problem. Nobody follows up. I built the follow-up." Program manager credibility angle.
- **Risks:** A crowded category (Granola, Fireflies, Zoom and Teams native AI). Differentiation depends on follow-through tracking.
- **Themes:** T215 Private local transcription, dictation and meeting capture; T175 Private offline and local voice assistants; T285 Teams lack shared memory and tacit knowledge for agents; T233 Agents need company context and tacit knowledge

What people said:

> “Interrupted founder 6 times in first 10 minutes” — Tomasz Tunguz, Tomasz Tunguz, 2026-01-28 ([link](https://tomtunguz.com/a-coxswain-on-your-shoulder/))
>
> “A Mac app for transcribing multi-hour recordings, with a CLI for agents.” — Ben's Bites, 2026-08-20 ([link](https://www.bensbites.com/p/simple-agents))
>
> “Voice dictation should be free, open source, local first” — AINews (smol.ai), 2026-06-02 ([link](https://news.smol.ai/issues/26-06-02-msft-mai-2/))
>
> “What I really need is something to listen in at meetings for my name, summarize what was asked, and suggest an answer based on the codebase.” — MattGaiser, Hacker News — Ask HN, 2026-01-21 ([link](https://news.ycombinator.com/item?id=46707806))

### 7. Voice Keeper: Your Writing Voice Across Every Assistant

**Learns your writing voice from your past work and gives you a style card, critique and diff-style edits that never rewrite wholesale.**

*Effort: 3-6 weeks · Confidence: medium · 167 findings from 13 sources · pain point 61, tool or technique 36, tool complaint 24, workaround 21, build request 16, debate 9*

- **Problem:** AI editing flattens personal style, hedges claims and changes meaning. Writers want critique and suggestions without wholesale rewrites.
- **For:** Bloggers, LinkedIn creators, consultants, authors and executives who write a lot
- **Evidence:** T089 (58 findings, 28 tool/technique and 12 workarounds) shows people building voice skill files and nightly style-guide updaters. T281 and T430 show demand for portable style layers. #389 asks for a plugin that interviews the user and critiques drafts.
- **Existing alternatives:** Custom GPTs, voice skill files, Kagi proofreading, Grammarly (generic). They require manual setup, and none persistently learns from your edits and flags meaning changes.
- **MVP:** Upload 5-10 past posts, generate a voice profile (tone, sentence length, favorite structures, banned phrases), then critique a draft against it and show proposed edits as accept/reject diffs, flagging any edit that changes meaning. Export the profile as a prompt block for ChatGPT, Claude or Gemini. Fuller product adds learning from accepted edits and a browser extension.
- **Build notes:** Next.js, LLM API, Supabase, diff library. Hardest parts: making the voice profile specific rather than generic, and meaning-change detection. Cost: low.
- **Demo hook:** Before/after of the same draft: a generic ChatGPT rewrite vs. Voice Keeper's three small suggestions, each with a reason and a 'this changes your claim' warning.
- **Post angle:** "ChatGPT edits make me sound like everyone else. I built an editor that keeps me sounding like me." Include the extracted style card of your own writing.
- **Risks:** Chat apps are adding style and memory features. Needs distinct value in the diff and meaning-change checks. Writers can be sensitive about privacy.
- **Themes:** T089 Preserving personal voice when writing and editing with AI; T430 AI prose sounds generic and needs style control; T281 Chatbot personality, tone and style controls; T038 Generic AI prose tells and slop

What people said:

> “A writing plugin that interviews you, critiques drafts and saves what you learn.” — Ben's Bites, 2026-09-08 ([link](https://www.bensbites.com/p/the-first-gpt-6-model))
>
> “have the LLM suggest individual changes” — Drew Breunig, Don't Worry About the Vase, 2026-05-28 ([link](https://thezvi.substack.com/p/ai-170-lack-of-executive-order))
>
> “Each night, the system updates my style guidelines, building a personalized Strunk & White.” — Tomasz Tunguz, Tomasz Tunguz, 2026-09-02 ([link](https://tomtunguz.com/ai-productivity-doesnt-mean-what-i-thought/))
>
> “to never re-write or suggest improvements, and to solely offer critique.” — codingdave, Hacker News — Ask HN, 2026-05-22 ([link](https://news.ycombinator.com/item?id=48235223))

### 8. Straight Talk: Persistent Honesty Layer for Chatbots

**Set how critical, warm and blunt you want AI feedback once, then use it as a front end that applies it to every chat, with a pushback mode that argues the other side.**

*Effort: 1-2 weekends · Confidence: medium · 154 findings from 14 sources · pain point 61, tool complaint 28, tool or technique 20, workaround 19, build request 19, debate 7*

- **Problem:** Chatbots flatter and over-agree, and anti-sycophancy prompts must be re-added each chat. Users have no persistent way to set honest-feedback levels and want real pushback.
- **For:** Founders, managers, job seekers and writers who use AI to evaluate ideas, plans and drafts
- **Evidence:** T133 (42 findings), T169 (42 findings) and T235 (49 findings) together show a repeated pain: sycophancy, and the opposite problem of preachy pushback. #5076 asks for reliable steering of style, #9158 for honest feedback, and #9492 shows the devil's-advocate workaround.
- **Existing alternatives:** Custom instructions, Absolute Mode prompts, steelmanning prompts. These are per-chat, drift over time, and can't be tuned between 'too soft' and 'too hard'.
- **MVP:** Web chat front end with a bring-your-own-key option and sliders for candor, warmth and ambition. One-click modes: Red Team my plan, Steelman the opposite, What would a skeptical investor say, What am I not seeing. Output includes a 'confidence and what would change my mind' footer. Fuller product adds saved personas and past-decision tracking.
- **Build notes:** Next.js, LLM API (BYO key or hosted), system prompts with structured output, Supabase. Hardest part: calibrating critique so it isn't just contrarian; test with real drafts. Cost: modest, passes through to the user's key.
- **Demo hook:** The same business plan evaluated twice: default chatbot says 'Great idea!'; Straight Talk with the candor slider at 8 lists the three reasons it fails, with ranked risks.
- **Post angle:** "Every AI told me my startup idea was great. I built one that disagrees with me." Playful hook with real examples.
- **Risks:** Chat apps are adding tone controls. Weak retention unless modes are used in a workflow. Prompt-only products are easily copied.
- **Themes:** T133 Chatbot sycophancy and need for honest feedback; T169 AI thinking partners that push back; T235 Chatbot pushback, over-caution and over-censorship; T281 Chatbot personality, tone and style controls

What people said:

> “it has yet to be effectively productized but can you imagine how great it would be to be able to steer your LLM responses” — Chelsea Sierra Voss, Don't Worry About the Vase, 2026-10-14 ([link](https://thezvi.substack.com/p/the-safety-culture-at-the-labs-is))
>
> “Users may prefer flattery over honest feedback, quick answers over genuine understanding” — Import AI, 2026-05-18 ([link](https://importai.substack.com/p/import-ai-457-ai-stuxnet-cursed-muon))
>
> “Want to find truth? Go elsewhere.” — Gary Marcus, Marcus on AI, 2026-03-03 ([link](https://garymarcus.substack.com/p/breaking-sycophantic-ai-distorts))
>
> “I play devil's advocate as much as possible.” — apparent, Hacker News — Ask HN, 2026-05-10 ([link](https://news.ycombinator.com/item?id=48088126))

### 9. ProofTrail: Show Your Work Fact-Check for AI Reports

**Paste an AI-written report or draft and get every claim extracted, matched to a source quote, and marked verified, unverified or contradicted.**

*Effort: 3-6 weeks · Confidence: medium · 105 findings from 14 sources · pain point 60, tool or technique 13, tool complaint 12, build request 10, workaround 6, link shared 2, debate 2*

- **Problem:** AI output has fabricated or subtly wrong facts and citations, and checking costs as much as it saves. Users without expertise can't judge quality.
- **For:** Analysts, consultants, writers, students and managers who rely on AI research
- **Evidence:** T079 (52 findings, 12 sources) and T336 (22 findings) show verification pain; #20995 and #12493 are explicit requests for a fact-checker for AI reports. T277 (31 findings) shows demand for source-checking layers.
- **Existing alternatives:** Manual Ctrl-F of quotes, clicking citations, second-model fact checks, Gemini linked citations. All are manual or one-shot.
- **MVP:** Paste text and optionally upload source PDFs or URLs. The app extracts each factual claim, searches the provided sources (and the web) for supporting quotes, and shows a claim table with the quote, link and status. Highlights numbers and citations that cannot be found. Fuller product adds a team review workflow and a browser extension for any chatbot answer.
- **Build notes:** Next.js, LLM with web search tool or a search API, PDF parsing, Supabase. Hardest parts: reliable claim extraction and avoiding false 'verified' marks; always show the quote so the human decides. Cost: moderate per report (many LLM calls).
- **Demo hook:** A 1-page AI market summary turns into a claim table: 14 claims, 9 verified with highlighted quotes, 3 unverifiable, 2 contradicted, with a 'one citation does not exist' red flag.
- **Post angle:** "I caught my AI report inventing a statistic. So I built a tool that makes it show receipts."
- **Risks:** Chat apps' own citation features will improve. The verifier can also be wrong, so over-trust is a risk. Cost per check.
- **Themes:** T079 Verifying AI output and fact-checking claims; T336 Verifying AI output in high-stakes professional work; T277 Media literacy and misleading AI outputs

What people said:

> “A public company even republished an AI-generated report from the platform, mistaking it for professional research” — AINews (smol.ai), 2025-12-22 ([link](https://news.smol.ai/issues/25-12-22-not-much/))
>
> “what i really want as a writer is an automated fact checker and alternative viewpoint giver” — Prakesh, Don't Worry About the Vase, 2026-01-13 ([link](https://thezvi.substack.com/p/claude-coworks))
>
> “show the extracted facts with links to the source material and let doctors correct a fact” — Hamel Husain, 2026-09-18 ([link](https://hamel.dev/blog/posts/evals-faq/))
>
> “The study (and its authors) weren't named, so I can't easily follow up” — Emily M. Bender, Bluesky, 2025-11-26 ([link](https://bsky.app/profile/emilymbender.bsky.social/post/3m6kha4c2tc2f))

### 10. Humanly: Prove You Wrote It

**A writing tool that records your drafting process and issues a shareable 'human-authored' report with an honest AI-assistance breakdown.**

*Effort: 3-6 weeks · Confidence: medium · 114 findings from 13 sources · pain point 68, build request 13, debate 12, tool or technique 11, workaround 6, tool complaint 3, link shared 1*

- **Problem:** Readers and editors can't tell how much of a text is AI-written, and human authors can't prove their work is their own. Detectors give false positives.
- **For:** Writers, students, freelancers, bloggers and creators who get accused of using AI
- **Evidence:** T105 (45 findings), T375 (16 findings) and T417/T418 on education show the problem. #6518 asks for a way to indicate how much of a document was AI-written, #22091 for a way to substantiate manuscripts, and #25359 notes bloggers feel pressure to prove authenticity.
- **Existing alternatives:** Pangram and ZeroGPT (detectors with false positives), end-of-piece disclosures, Google Docs version history. None provides a portable, shareable process record with an AI-assistance label.
- **MVP:** A web editor that logs keystroke/paste events and AI-assist usage, then generates a public verification page with a timeline, paste percentage, and optional AI-assistance disclosure label. Fuller product adds a Google Docs add-on, a badge for blogs, and a classroom mode for teachers.
- **Build notes:** Next.js with a rich text editor (TipTap), event logging in Supabase, a shareable report page. Hardest parts: keeping the report credible, since process logs can be faked. Be honest about this in the pitch. Cost: low.
- **Demo hook:** Write a paragraph live, paste a sentence from ChatGPT, then open the shareable report showing 'typed 91%, pasted 9%, one AI-assisted edit' on a timeline.
- **Post angle:** "AI detectors accused real writers. Instead of guessing, I built a way to show your work."
- **Risks:** Process logs can be gamed, so it only supports honest disclosure. Writers must adopt a new editor. A hard network-effect problem.
- **Themes:** T105 Detecting and disclosing AI authorship; T375 Verifying authenticity of media and human-made work; T165 AI slop eroding trust in search and online spaces; T417 Take-home assignments are undermined by AI cheating

What people said:

> “we find ways to surface interesting qualitative or strategic ideas from Claude, as well as more easily evaluatable technical contributions” — Jack Clark, Import AI, 2026-05-26 ([link](https://importai.substack.com/p/import-ai-458-reckoning-with-the))
>
> “they 'can no longer substantiate' that it was written without utilizing AI” — Don't Worry About the Vase, 2026-08-13 ([link](https://thezvi.substack.com/p/ai-181-astra-goes-cyber-critical))
>
> “In the age of slop, readers test authenticity.” — Tomasz Tunguz, Tomasz Tunguz, 2026-08-03 ([link](https://tomtunguz.com/ai-ghost-writing/))
>
> “If you don't know it's AI, does it matter?” — Alberto Romero, The Algorithmic Bridge, 2025-12-16 ([link](https://www.thealgorithmicbridge.com/p/i-liked-the-essay-then-i-found-out))

### 11. Human Filter: Browser Extension for AI Slop

**A Chrome extension that labels or hides AI-generated posts, comments and clickbait across X, LinkedIn, YouTube and Reddit, with a tunable sensitivity slider.**

*Effort: 3-6 weeks · Confidence: medium · 188 findings from 14 sources · pain point 88, build request 44, tool or technique 25, debate 11, workaround 11, tool complaint 7, link shared 2*

- **Problem:** AI posts, comments and videos flood feeds and forums, and users can't tell or filter machine-written content.
- **For:** Social media, forum and YouTube users, creators and professionals on LinkedIn
- **Evidence:** T037 (67 findings, 25 build requests) includes #8209 asking for a 'percent human' score on accounts and #23371 for a clickbait thumbnail fix. T165 (35 findings), T323 (23 findings) and T429 (18 findings) add related demand.
- **Existing alternatives:** Pangram, hn-ai.org, block lists, channel whitelisting. Fragmented, per-site, and none offers a user-tuned cross-platform label.
- **MVP:** Chrome extension for X and LinkedIn: scans visible posts with a lightweight LLM or detection API, adds a small 'likely AI' badge and an optional collapse toggle, and keeps a local counter ('34% of your feed today'). Fuller product adds YouTube thumbnails and comments, Reddit, and user-specific tuning from feedback.
- **Build notes:** Chrome extension (Manifest V3) with content scripts, a lightweight backend proxy to an LLM or Pangram-style API, local caching. Hardest parts: DOM changes on social sites, false positives, per-post API cost. Cost: can add up, so cache and rate-limit.
- **Demo hook:** A LinkedIn feed with badges appearing on posts live, then a slider hiding the 'likely AI' ones, and a counter: '41% of my feed is AI-written'.
- **Post angle:** "I measured how much of my LinkedIn feed is AI. The number made me close the app." Data-driven hook with a screenshot.
- **Risks:** Detection is unreliable, so false accusations are a risk. Platform DOM changes break the extension. API costs and Chrome Web Store review.
- **Themes:** T037 Filtering AI slop and bot content from feeds; T165 AI slop eroding trust in search and online spaces; T323 Controllable social feeds; T429 AI-generated spam, cold outreach and low-quality submissions; T105 Detecting and disclosing AI authorship

What people said:

> “I’d also like to see automatic ‘percent human’ attached to accounts automatically” — Zvi Mowshowitz, Don't Worry About the Vase, 2026-09-03 ([link](https://thezvi.substack.com/p/ai-184-post-post-mortem))
>
> “a Chrome extension that swaps clickbait thumbnails for real stills from the video.” — Ben Tossell, Ben's Bites, 2026-11-03 ([link](https://www.bensbites.com/p/if-you-feel-behind-right-now-dont))
>
> “Partnering with an AI company to detect AI writing” — Alberto Romero, The Algorithmic Bridge, 2026-10-21 ([link](https://www.thealgorithmicbridge.com/p/put-some-brain-in-your-thinking))
>
> “Another "Hacker News" with less AI and more human-focused hacking news?” — weird_trousers, Hacker News — Ask HN, 2026-07-08 ([link](https://news.ycombinator.com/item?id=48834961))

### 12. Chief of Staff Daily Brief

**A hosted morning brief that reads your calendar, email and tasks, tells you the three things that matter today, and drafts prep for each meeting.**

*Effort: 3-6 weeks · Confidence: high · 198 findings from 15 sources · build request 68, tool or technique 52, pain point 42, workaround 27, tool complaint 4, debate 3, link shared 2*

- **Problem:** People want one assistant across email, calendar, files and tasks that plans their day proactively. Current setups are DIY and siloed.
- **For:** Busy professionals, managers and founders who are not technical
- **Evidence:** T061 has 45 findings, 22 build requests, from 10 sources, including #22252 asking for a customizable Daily Brief and #4147 for task tracking across Gmail and calendar. T031 (68 findings) and T094 (48 findings) show demand for personal agents non-coders can use.
- **Existing alternatives:** Dots, Bond, Daily Brief, ChatGPT scheduled tasks, Claude Cowork and Gmail briefing agents. Many are DIY or lack real customization and follow-through.
- **MVP:** Connect Google Calendar and Gmail (read-only), and each morning email or message a brief: today's meetings with a prep note, replies owed, commitments you made that are due, and a suggested time block. Customizable instructions in plain English. Fuller product adds Notion/Slack, task capture from threads, and an end-of-day review.
- **Build notes:** Next.js, Google APIs with read-only scopes, a scheduled job (Vercel cron), an LLM API, and Resend for email. Hardest parts: Google OAuth verification and keeping briefs short and accurate. Cost: low per user per day.
- **Demo hook:** A screenshot of the 7am brief with 'Top 3', meeting prep for the 10am with the last email thread summarized, and 'You promised X to Priya by Friday'.
- **Post angle:** "I built the chief of staff I couldn't afford. It's an email that arrives at 7am." Program manager angle on prep.
- **Risks:** Crowded category, and Gmail/Gemini, ChatGPT Pulse-style features and Copilot are moving in. Differentiation depends on customization and commitments tracking.
- **Themes:** T061 Personal AI chief of staff and proactive daily assistant; T031 Local-first personal assistants over own data; T094 Agents for non-technical knowledge work; T140 Email clients and agents for inbox triage

What people said:

> “If this is to be any good you need to be able to give it instructions” — Zvi Mowshowitz, Don't Worry About the Vase, 2026-05-22 ([link](https://thezvi.substack.com/p/gemini-35-flash-looks-good-for-how))
>
> “Agents nag me about a document I haven’t signed” — Ben Tossell, Ben's Bites, 2026-10-06 ([link](https://www.bensbites.com/p/thoughts-from-san-francisco))
>
> “partnerships or integrations with systems that expose well-structured personal data” — AINews (smol.ai), 2026-10-23 ([link](https://latent.space/p/ainews-black-october/))
>
> “An AI assistant entry point should be WhatsApp/Telegram and email.” — antirez, Bluesky, 2026-01-30 ([link](https://bsky.app/profile/antirez.bsky.social/post/3mdnampzqck2w))

### 13. Commitment Tracker: Never Drop a Promise

**Scans your sent email and meeting notes for things you promised, and keeps a living list with due dates and gentle nudges.**

*Effort: 3-6 weeks · Confidence: medium · 165 findings from 16 sources · pain point 56, build request 51, tool or technique 29, workaround 22, debate 6, tool complaint 1*

- **Problem:** Prompted tasks and promises are never revisited. People struggle to track task completion across Gmail, calendar and other apps, and agent-driven work fragments attention.
- **For:** Managers, program managers, consultants and account managers
- **Evidence:** #4147 asks for tracking task completion across Gmail and calendar. #11383 and #14829 show prompted tasks never revisited and half-finished work. T044 (64 findings) and T061 (45 findings) show executive-function scaffolding demand, and T140 shows demand for actionable triage.
- **Existing alternatives:** Gmail Nudges, to-do apps, Superhuman reminders, manual notes. None extracts promises from sent mail and chats automatically into a trackable list.
- **MVP:** Gmail read-only connect, scan the last 30 days of sent mail with an LLM to extract 'I will...' commitments, show a list with the recipient, due date and thread link, one-click mark done or snooze, and a Monday digest of open items. Fuller product adds Slack, meeting transcripts, and a team view for managers.
- **Build notes:** Next.js, Gmail API, Supabase, a scheduled job, an LLM with structured extraction. Hardest parts: precision (false commitments annoy users) and OAuth scopes. Cost: low.
- **Demo hook:** Connect Gmail; 20 seconds later, 11 promises you made last month, three overdue and highlighted, each with the original sentence and a 'draft a follow-up' button.
- **Post angle:** "I scanned my sent folder and found 11 promises I'd forgotten. Here's the tool I built so it never happens again."
- **Risks:** Gmail OAuth verification, privacy concerns, extraction errors, and big email clients adding the feature.
- **Themes:** T061 Personal AI chief of staff and proactive daily assistant; T044 Agent-driven work causes burnout and attention fragmentation; T140 Email clients and agents for inbox triage; T285 Teams lack shared memory and tacit knowledge for agents

What people said:

> “I'll prompt a thing and then never look at it.” — swyx, Latent Space, 2026-10-02 ([link](https://latent.space/p/rlm/))
>
> “I start far more than I finish.” — Ben Tossell, Ben's Bites, 2026-10-29 ([link](https://www.bensbites.com/p/ai-is-overwhelming-and-im-doing-it))
>
> “AI as especially helpful for managing focus and organization—acting as external scaffolding for planning, memory, and task follow-through” — Don't Worry About the Vase, 2026-03-26 ([link](https://thezvi.substack.com/p/ai-161-part-1-80000-interviews))
>
> “Make this but open source: https://getcoldturkey.com/” — Cider9986, Hacker News — Ask HN, 2026-10-11 ([link](https://news.ycombinator.com/item?id=50049047))

### 14. One-Click Second Brain

**Drop files, notes, bookmarks and email exports in, with no folders or tags, and ask questions in plain English with source links.**

*Effort: 3-6 weeks · Confidence: medium · 161 findings from 11 sources · tool or technique 51, pain point 38, build request 38, workaround 26, tool complaint 4, link shared 2, debate 2*

- **Problem:** People want years of notes, bookmarks, emails and files searchable by LLMs. Ad hoc setups are fragile and need technical skills.
- **For:** Knowledge workers, researchers and consultants who hoard documents
- **Evidence:** T166 (49 findings) includes #24802 asking for a document store with no tagging or folders, and #25095 for a local second brain. T031 (68 findings) has #28677 asking to find documents and receipts in plain language. T099 and T292 show memory and history management issues.
- **Existing alternatives:** Obsidian with Claude Code, Karpathy-style markdown wikis, custom MCP servers, NotebookLM. They require setup; NotebookLM is source-limited and not a living personal archive.
- **MVP:** A web app with drag-and-drop upload (PDF, docx, text, email export), automatic chunking and embedding, a chat-style Q&A with citations to the original page, and a 'what do I know about X' summary. Fuller product adds a browser bookmark clipper, Gmail/Drive connectors, local-only mode and a weekly 'resurfaced notes' email.
- **Build notes:** Next.js, Supabase with pgvector, an embedding and LLM API, PDF parsing. Hardest parts: document parsing quality and privacy trust. Cost: modest storage and embedding costs; limit free tier size.
- **Demo hook:** Drop 40 random PDFs and notes in; ask 'what did the landlord say about the deposit?' and get the answer with a highlighted source page in seconds.
- **Post angle:** "I stopped organizing my files. I just ask them questions." Before/after screenshot of a chaotic downloads folder.
- **Risks:** Crowded: NotebookLM, ChatGPT projects, Notion AI, and Apple/Google desktop search. Privacy concerns about uploading personal files. Needs a clear niche such as receipts or research.
- **Themes:** T166 Personal knowledge bases and second brains for agents; T031 Local-first personal assistants over own data; T099 AI chat memory and history are non-portable and unmanageable

What people said:

> “Drop them in without any tagging/folders, and later search for them in plain English.” — Ben's Bites, 2026-05-28 ([link](https://www.bensbites.com/p/i-signed-up-for-another-saas))
>
> “people are lonely, confused, hungry for connection, frustrated about what they don’t understand, too busy to figure it all out” — anildash.com, Bluesky, 2026-10-15 ([link](https://bsky.app/profile/anildash.com/post/3mxwu2fm5xc2r))
>
> “have it be my complete second brain, running completely privately on my own hardware” — pcf, Hacker News — Ask HN, 2026-11-02 ([link](https://news.ycombinator.com/item?id=50337431))
>
> “assemble a personal knowledge base of research, contacts, ideas, relationships, and tasks over my recent career” — Ethan Mollick, Bluesky, 2026-09-03 ([link](https://bsky.app/profile/emollick.bsky.social/post/3munds3sxrc2n))

### 15. AI Memory Vault

**See, edit, scrub and export everything ChatGPT and Claude remember about you, and move it between assistants in one click.**

*Effort: 3-6 weeks · Confidence: medium · 108 findings from 13 sources · pain point 49, build request 21, tool or technique 20, workaround 11, tool complaint 5, link shared 1, debate 1*

- **Problem:** Context and memory don't carry across chats or providers, and users can't inspect, scrub or organize them. Users re-explain context and fear lock-in.
- **For:** Heavy ChatGPT/Claude users, consultants and anyone switching assistants
- **Evidence:** T099 (44 findings) and T292 (26 findings) include #1436 requesting a scrubbable memory store, #10803 describing the workaround of prompting for a memory export, and #23694 asking for search over past chats. #5603 asks for per-session toggles.
- **Existing alternatives:** Memory-file review, conversation exporters, Anthropic memory import, ChatGPT Projects, forking chats. Manual, scattered, and none provides one editable portable layer.
- **MVP:** Import ChatGPT/Claude data exports (the official zip), parse conversations, extract facts and preferences into an editable list (keep, edit, delete, tag by project), search across all history, and export a portable 'about me' block for any assistant. Fuller product adds a browser extension to inject context, and per-project isolation.
- **Build notes:** Next.js, client-side parsing of export files for privacy, local storage or Supabase, an LLM for extraction. Hardest parts: export format changes and sensitive data handling. Cost: low if parsing is client-side with BYO key.
- **Demo hook:** Drag in a ChatGPT export; 30 seconds later: 'Here are 143 things it knows about you', with bad or outdated ones deleted and a one-click 'move to Claude' prompt generated.
- **Post angle:** "I exported what ChatGPT knows about me. It was weird, wrong, and a bit creepy. So I built a memory editor."
- **Risks:** Vendors keep adding memory controls and import tools. Export formats change. Narrow, one-time-use pattern unless search and sync keep users.
- **Themes:** T099 AI chat memory and history are non-portable and unmanageable; T292 Opaque, uncontrollable and non-portable AI memory; T155 Confusing AI model lineups, modes and tool choice

What people said:

> “there's simply too much of it” — Utah teapot, Don't Worry About the Vase, 2026-10-22 ([link](https://thezvi.substack.com/p/ai-191-the-hackening-begins))
>
> “tell me everything you know about me” — Florian Brand, Interconnects, 2026-10-25 ([link](https://www.interconnects.ai/p/podcast-kimi-k31-pro-the-new-cyber))
>
> “"what did we talk about last week re: [thing]"” — Ben Tossell, Ben's Bites, 2026-08-21 ([link](https://www.bensbites.com/p/how-i-built-this))
>
> “the ability to organize existing chats into projects, not just new ones” — TheNewBing, AINews (smol.ai), 2026-04-07 ([link](https://news.smol.ai/issues/26-04-06-anthropic-mythos/))

### 16. Burnout Brake for AI-Heavy Workdays

**A focus companion that time-boxes AI sessions, queues stray ideas and resurfaces unfinished work so you finish things instead of starting ten more.**

*Effort: 1-2 weekends · Confidence: medium · 141 findings from 15 sources · pain point 60, build request 34, tool or technique 20, workaround 18, debate 9*

- **Problem:** Parallel agents, dopamine loops and endless side projects cause context switching, exhaustion and half-finished work. People struggle to stop and stay focused.
- **For:** Heavy AI users, vibe coders, ADHD professionals and creators
- **Evidence:** T044 (64 findings, 37 pain points) includes #14829 on how easy it is to start and hard to finish, #5332 requesting a discipline aid against abandoned projects, #8206 on AI as executive-function scaffolding, and #12746 on attention tracking. T188 adds a need to know when to stop.
- **Existing alternatives:** Cold Turkey, break-reminder hooks, limiting to 2-4 sessions, ADHD Claude skills. These block sites or remind but don't track unfinished work or help decide what to finish.
- **MVP:** A web/PWA app: list your active projects (max 3 enforced), each with a 'done means' sentence; a 'parking lot' to capture new ideas without starting them; a session timer with stopping-point prompts; and a Friday review showing started vs. finished. Fuller product adds a desktop focus tracker, calendar blocks, and AI nudges that ask 'does this serve your goal?'
- **Build notes:** Next.js PWA, Supabase, light LLM use for prompts. Hardest part: behaviour design rather than code. Cost: very low.
- **Demo hook:** A dashboard with 3 slots for active projects, a parking lot of 14 shiny ideas, and a stats card: 'This month: started 9, finished 2. Pick one to finish.'
- **Post angle:** "AI made it too easy to start things. I have 11 half-built apps. So I built a tool that makes me finish one." Honest, relatable.
- **Risks:** Habit apps have high churn and weak monetization. It overlaps with to-do apps. It needs a distinct 'AI-era' angle.
- **Themes:** T044 Agent-driven work causes burnout and attention fragmentation; T188 Measuring real AI productivity gains; T061 Personal AI chief of staff and proactive daily assistant

What people said:

> “the critical skill to develop here is discipline” — Simon Willison, Simon Willison's Weblog, 2026-05-31 ([link](https://simonwillison.net/2026/May/31/the-solution-might-be-cancelling-my-ai-subscription/))
>
> “Oura for your attention on the desktop” — AINews (smol.ai), 2026-01-08 ([link](https://news.smol.ai/issues/26-01-08-not-much/))
>
> “Engineering leaders went into AI expecting 2-3x productivity gains but are landing closer to 30%.” — Augment Code, Tomasz Tunguz, 2026-07-21 ([link](https://tomtunguz.com/ai-engineering-productivity-anything-but-normal/))
>
> “What is stopping you from not talking to it until the next day?” — kay_o, Hacker News — Ask HN, 2026-08-29 ([link](https://news.ycombinator.com/item?id=49491745))

### 17. Decision Brief Builder for PMs

**Turn customer feedback, interview notes and tickets into a evidence-backed 'should we build this?' brief with counterarguments and a recommendation.**

*Effort: 3-6 weeks · Confidence: medium · 119 findings from 15 sources · pain point 62, tool or technique 26, workaround 10, debate 10, build request 8, tool complaint 2, link shared 1*

- **Problem:** Shipping is cheap, so deciding what to build and proving impact are the bottleneck. Teams struggle to link customer feedback to ideas.
- **For:** Product managers, founders, program managers and indie builders
- **Evidence:** T211 (38 findings) includes #11683 requesting idea generation grounded in user feedback, #22198 on choosing what to build, and #29000 on using an agent to argue product primitives. T169 shows demand for push-back thinking partners.
- **Existing alternatives:** Dovetail, Productboard, ChatGPT prompts and manual synthesis. They summarize feedback but rarely produce a decision memo with the case against and a go/no-go.
- **MVP:** Paste or upload feedback, interview notes and survey responses; the app clusters themes with counts and quotes, scores ideas on impact/effort/evidence strength, argues the best case against, and produces a one-page decision memo. Fuller product adds Intercom/Zendesk/Slack imports and tracking whether shipped features moved the metric.
- **Build notes:** Next.js, LLM with structured outputs, Supabase, PDF export. Hardest parts: quote-faithful clustering and avoiding invented numbers. Cost: moderate for large datasets.
- **Demo hook:** 100 raw feedback lines turn into 5 ranked themes with quotes, a 'build this first' recommendation and a 'what would make this wrong' box, then a shareable one-pager.
- **Post angle:** "Building is cheap now. Knowing what to build isn't. Here's how I made an AI argue with my product ideas." PM-credibility post.
- **Risks:** Competes with research and feedback tools, and with ChatGPT used directly. Value depends on analysis quality and trust.
- **Themes:** T211 Deciding what to build when building is cheap; T169 AI thinking partners that push back; T143 Enterprises cannot measure or demonstrate AI ROI

What people said:

> “bring me new ideas, right? somehow LLMs are just not it.” — Akshay Nathan, Latent Space, 2026-07-28 ([link](https://latent.space/p/chatgpt-work/))
>
> “It’s never been easier to build something nobody wants.” — Lenny Rachitsky, Lenny's Newsletter, 2026-09-29 ([link](https://www.lennysnewsletter.com/p/all-of-the-lenny-and-friends-summit))
>
> “I used one to decide what to build: gather evidence, argue primitives, keep the judgment.” — Kent C. Dodds, Bluesky, 2026-08-11 ([link](https://bsky.app/profile/kentcdodds.com/post/3msswvnqp6z2s))
>
> “choosing what to build in the first place” — Sarah Guo, AINews (smol.ai), 2026-06-10 ([link](https://news.smol.ai/issues/26-06-10-not-much/))

### 18. AI ROI Baseline for Teams

**A lightweight tool where teams log a workflow's before/after time and quality, and get a credible, board-ready AI impact report.**

*Effort: 3-6 weeks · Confidence: medium · 147 findings from 15 sources · pain point 101, debate 25, tool or technique 7, build request 7, workaround 4, link shared 2, tool complaint 1*

- **Problem:** Few companies track an AI impact metric, pilots stay stuck, and productivity claims are unsourced. Boards demand ROI without baselines.
- **For:** AI program leads, managers, consultants and operations leaders
- **Evidence:** T143 (39 findings, 12 sources), T347 (26 findings), T188 (32 findings) and T241 (30 findings) all show ROI measurement pain. #14714 says only about 2% of S&P 500 companies reporting AI impact track a metric, and #29093 asks for tooling to deliver measurable value.
- **Existing alternatives:** Tracking minutes saved per employee in spreadsheets, surveys, and vendor dashboards that count usage, not outcomes. Usage leaderboards get gamed.
- **MVP:** Web app: define a workflow (e.g. weekly report), record the baseline time and quality, then have team members log tasks quickly (Slack slash command or form) with AI vs. non-AI time; produces a dashboard with hours saved, cost saved, confidence level and caveats, plus an exportable one-page ROI summary. Fuller product adds survey modules and manager-ready quarterly reports.
- **Build notes:** Next.js, Supabase, Slack app for logging, charting library, PDF export. Hardest parts: designing measurement that's honest (self-reports bias) and getting teams to log. Cost: low.
- **Demo hook:** A dashboard where a team shows '312 hours saved on reporting, 71% confidence', with a before/after chart and a one-page PDF produced in a click.
- **Post angle:** "Your AI pilot has no baseline. Here's the 10-minute template and tool I built to fix that." Draws on enterprise program-management experience.
- **Risks:** Hard to get consistent logging, and enterprise buyers may want bigger platforms. Self-reported data is weak. B2B sales cycles are slow.
- **Themes:** T143 Enterprises cannot measure or demonstrate AI ROI; T347 Businesses cannot measure ROI and productivity from AI; T188 Measuring real AI productivity gains; T241 Mandated AI usage and token leaderboards get gamed; T373 Teams lack AI enablement and use-case discovery

What people said:

> “only ~2% track a metric for it” — Ben Tossell, Ben's Bites, 2026-10-01 ([link](https://www.bensbites.com/p/openai-devday-2026))
>
> “who want to get AI to deliver *business value* which is... tricky.” — Gergely Orosz, Bluesky, 2026-09-23 ([link](https://bsky.app/profile/gergely.pragmaticengineer.com/post/3mw6loyobrc2e))
>
> “the returns on that investment have yet to materialize as broad productivity gains” — Sayash Kapoor, Rishi Bommasani, Arvind Narayanan, AI as Normal Technology, 2026-11-10 ([link](https://www.normaltech.ai/p/the-missing-quadrant-in-responses))
>
> “you get a lot of projects that don't make sense, which then quietly die” — nitwit005, Hacker News — Ask HN, 2026-08-31 ([link](https://news.ycombinator.com/item?id=49510066))

### 19. AI Adoption Playbook Generator by Role

**Pick a role and your tools and get a ready-to-use pack: five workflows, prompts, a 30-day rollout plan and an adoption tracker for the team.**

*Effort: 1-2 weekends · Confidence: medium · 130 findings from 13 sources · pain point 58, tool or technique 27, build request 22, workaround 13, debate 6, tool complaint 3, link shared 1*

- **Problem:** Employees and leaders don't know what AI can do for their roles. Use stays with a few early adopters, and uneven adoption breeds friction.
- **For:** Team leads, HR/L&D, operations managers and small-business owners
- **Evidence:** T373 (20 findings) includes #20860 asking for role-specific bundles of tools. T247 (24 findings) shows agents are too hard for non-coders to adopt, T094 (48 findings) shows non-technical workers need profession-specific interfaces, and #2743 asks for help recognising AI-solvable problems.
- **Existing alternatives:** Generic prompt libraries, vendor training, consulting workshops. They are not role-specific, and don't help a manager measure adoption.
- **MVP:** A web app: choose a role (e.g. HR coordinator, finance analyst, customer support lead) and the tools in use; it interviews you about your weekly tasks and generates a prioritised list of AI use cases with example prompts, risk notes and a 30-day plan. Team version has shared prompts and a simple adoption check-in. Fuller product adds Slack delivery of weekly tips.
- **Build notes:** Next.js, LLM API, Supabase, templated PDF/Notion export. Hardest parts: quality of role-specific content (curate seeds yourself) and avoiding generic advice. Cost: low.
- **Demo hook:** Choose 'Operations manager'; in a minute get a custom 30-day plan with 5 workflows, the exact prompts, and an expected hours-saved estimate for each.
- **Post angle:** "Most teams don't need a new AI tool. They need someone to show them what to do with it on Monday morning." AI adoption at work angle.
- **Risks:** Content-heavy and easy to commoditize with ChatGPT. Hard to make recurring. Value lies in curation and a team tracker.
- **Themes:** T373 Teams lack AI enablement and use-case discovery; T247 Agents too hard for non-coders to adopt; T094 Agents for non-technical knowledge work; T155 Confusing AI model lineups, modes and tool choice

What people said:

> “laptops given to new employees would have Cowork installed plus a collection of tools specific to each role” — Tomasz Tunguz, Tomasz Tunguz, 2026-01-13 ([link](https://tomtunguz.com/thoughts-on-claude-coworker/))
>
> “life is filled with software-shaped problems that we, non-coders, don’t even notice” — Alberto Romero, The Algorithmic Bridge, 2026-02-07 ([link](https://www.thealgorithmicbridge.com/p/you-spent-your-whole-life-getting))
>
> “Most have absolutely zero clue what's possible.” — Nicolas Bustamante, Don't Worry About the Vase, 2026-10-08 ([link](https://thezvi.substack.com/p/ai-189-new-math))
>
> “allow expert researchers/app developers create AI apps that work for niche use-cases and have domain-appropriate guardrails” — altmanaltman, Hacker News — Ask HN, 2026-02-28 ([link](https://news.ycombinator.com/item?id=47193606))

### 20. Agent Output Reader: Make AI Reports Skimmable

**Paste a long agent or AI report and get a visual one-page brief with decisions to approve, open questions, key numbers and a shareable link.**

*Effort: 1-2 weekends · Confidence: medium · 108 findings from 10 sources · pain point 38, tool or technique 37, build request 18, workaround 11, link shared 3, tool complaint 1*

- **Problem:** AI output volume exceeds human capacity to review, and agent reports and shared artifacts are hard to render and share.
- **For:** People supervising agents, managers receiving long AI deliverables, consultants
- **Evidence:** T263 (31 findings, 9 in last 90 days) includes #22201 on absorption being the bottleneck and #2437 on reviewing large volumes. #11948 requests feedback directly on AI-generated HTML docs, #4570 a reliable service to publish and render shared HTML pages. T141 shows the same load on recipients.
- **Existing alternatives:** Asking for HTML, diagrams or plain English in the original prompt, Gist rendering, visual explainer skills. Each requires prompts or technical steps, and none consolidates decisions for approval.
- **MVP:** Paste markdown or text; produces a clean, shareable web page with a TL;DR, decision list with approve/reject buttons, key numbers as cards, assumptions flagged, and inline comments for feedback that can be exported back as a prompt. Fuller product adds file upload, team commenting and a browser extension.
- **Build notes:** Next.js, LLM for structuring, markdown renderer, Supabase for shareable pages, comment UI. Hardest parts: reliable structure extraction and the comment-to-prompt export. Cost: low.
- **Demo hook:** A 4,000-word agent research dump becomes a 1-page visual brief with a 'Decisions needed (3)' panel and a shareable link in 10 seconds.
- **Post angle:** "AI gave me a 12-page report I'll never read. So I built a reader for AI output."
- **Risks:** Chat apps and Claude artifacts are adding richer rendering. Differentiation depends on decision workflow and sharing.
- **Themes:** T263 Absorbing and reviewing the flood of agent output; T141 AI-written messages and documents burden recipients; T162 Shared workspaces where humans and agents collaborate

What people said:

> “The biggest constraint is honestly people’s understanding and ability to absorb what you’re giving them.” — Nan Yu, Lenny's Newsletter, 2026-09-29 ([link](https://www.lennysnewsletter.com/p/all-of-the-lenny-and-friends-summit))
>
> “used claude artifacts to give feedback about the html design doc directly to the agent” — rickye26, Hacker News — Ask HN, 2026-09-29 ([link](https://news.ycombinator.com/item?id=49901420))
>
> “As of claude-code-transcripts 0.5 the --gist option now publishes to gisthost.github.io instead” — Simon Willison, Simon Willison's Weblog, 2026-01-01 ([link](https://simonwillison.net/2026/Jan/1/gisthost/))
>
> “that process was also lossy, right? Like I gave them just like my interpretation of what ChatGPT Work cooked up.” — Akshay Nathan, Latent Space, 2026-07-28 ([link](https://latent.space/p/chatgpt-work/))

### 21. Deck Doctor: Editable AI Slides With a Content-First Flow

**Start from your outline and numbers, get an editable, on-brand deck in HTML or PPTX with real charts and citations, not image slides.**

*Effort: 3-6 weeks · Confidence: medium · 92 findings from 10 sources · tool or technique 46, pain point 26, build request 11, workaround 5, tool complaint 4*

- **Problem:** Generated slides are image-based, hard to edit, mangle formatting and are too text-heavy. Slide tools are clumsy for technical content.
- **For:** Consultants, managers, program managers, founders and students who build decks
- **Evidence:** T206 (35 findings) includes #5365 on decks defaulting to too much text, #27511 on image-only slides being hard to correct, and #7973 on losing decks in the browser. T224 (39 findings) and T411 (18 findings) add editable charts and diagrams demand.
- **Existing alternatives:** Gamma, NotebookLM slides, Claude Office files, Perplexity asset creation. Outputs are often image-based, generic or hard to edit, and don't enforce a content-first flow.
- **MVP:** Web app: paste an outline or document; the tool asks for the one key message per slide, generates layouts with real native charts and editable text, then exports PPTX (python-pptx or pptxgenjs) or HTML. Includes a 'too much text' checker. Fuller product adds brand templates, citation footers and a spreadsheet-to-chart import.
- **Build notes:** Next.js, an LLM producing a JSON slide spec, pptxgenjs for export, Chart.js for charts. Hardest parts: layout quality and PPTX fidelity. Cost: low.
- **Demo hook:** A messy 3-page memo turns into a 10-slide editable deck with a native chart; click into PowerPoint and edit a bar value to show it's not an image.
- **Post angle:** "AI slides are screenshots. I built one that makes real, editable PowerPoint, and refuses to put 80 words on a slide."
- **Risks:** A very crowded category, with Gamma, Canva and Microsoft Copilot. Needs a narrow wedge such as consulting-style decks or memo-to-deck.
- **Themes:** T206 AI slide and office document generation; T224 Reliable spreadsheet, BI and financial analyst agents; T411 Diagrams, charts and infographics need editable, accurate output

What people said:

> “AI creates technical slide presentations, but by default it will use way too much text” — Don't Worry About the Vase, 2026-11-05 ([link](https://thezvi.substack.com/p/ai-193-progress-may-dramatically))
>
> “An ideal version would use multiple tools together.” — Ethan Mollick, Bluesky, 2025-12-04 ([link](https://bsky.app/profile/emollick.bsky.social/post/3m74zwbltic26))
>
> “if the browser crashes I’ve just lost my entire deck!” — Simon Willison, Simon Willison's Weblog, 2026-02-25 ([link](https://simonwillison.net/2026/Feb/25/present/))
>
> “Codex is for everyone, for any task done with a computer” — Greg, AINews (smol.ai), 2026-04-30 ([link](https://news.smol.ai/issues/26-04-30-not-much/))

### 22. Household Admin Agent for Forms and Paperwork

**Upload a confusing form, letter or school email and get plain-language steps, a pre-filled draft, deadlines and a checklist.**

*Effort: 3-6 weeks · Confidence: medium · 95 findings from 12 sources · build request 34, pain point 25, tool or technique 23, workaround 11, tool complaint 2*

- **Problem:** Forms, permits, reimbursements and routine admin take heavy time and give unclear answers. Digital processes drain executive function, especially for neurodivergent people.
- **For:** Parents, small-business owners, individuals and neurodivergent users dealing with administration
- **Evidence:** T284 (22 findings) includes #6387 asking for an agent that fills government forms and creates invoices, #1810 on clear zoning and permit answers, and #28675 on executive-function drain. T140 includes #6229 on school email logistics, T404 (17 findings) on errand agents, and T304 on bills.
- **Existing alternatives:** Manus autofill, Claude Code with browser control, agent-drafted correction emails. Mostly DIY or generic chat, with no deadline tracking or guided workflow.
- **MVP:** Upload a PDF or photo of a form or letter; get a plain-English explanation, what's required by when, a checklist, a pre-filled draft of answers from a saved profile and a draft reply. Calendar export for deadlines. Fuller product adds a school-email parser, forwarding address ingestion and a family task board.
- **Build notes:** Next.js, vision LLM, PDF form-filling library, Supabase, Google Calendar export. Hardest parts: accuracy on legal-ish forms (add disclaimers), and sensitive data handling. Cost: low.
- **Demo hook:** Photo of a confusing city permit letter becomes a 6-step checklist with the deadline highlighted and a drafted reply email in 15 seconds.
- **Post angle:** "Adult life is mostly forms. I built an AI that reads the letter, tells me what to do, and drafts the reply."
- **Risks:** Accuracy and liability on forms, and generic chatbots can do part of this. Needs trust-building, with careful positioning as 'draft and explain', not legal advice.
- **Themes:** T284 Bureaucratic and personal paperwork automation; T404 Consumer errand and household agents; T140 Email clients and agents for inbox triage; T304 Personal finance, bills and subscription management

What people said:

> “A agent that automatically fills out government forms and creates invoices” — bnchrch, Hacker News — Ask HN, 2026-06-08 ([link](https://news.ycombinator.com/item?id=48449187))
>
> “no one can figure out what it takes to get approved except by trying and finding out” — Zvi Mowshowitz, Don't Worry About the Vase, 2026-05-01 ([link](https://thezvi.substack.com/p/housing-roundup-14-you-cant-build))
>
> “an explosion in digital processes which drain executive function” — karenho.bsky.social, Bluesky, 2026-10-15 ([link](https://bsky.app/profile/anildash.com/post/3mxwe3o7yuc2r))
>
> “It took me two hours to do an order” — Ari Weinstein, Latent Space, 2026-09-30 ([link](https://latent.space/p/devday-2026/))

### 23. Skim: Your Personal AI News Digest

**Tell it what you care about and what to exclude; get a short daily digest from your newsletters, RSS and X lists with no hype.**

*Effort: 1-2 weekends · Confidence: medium · 121 findings from 8 sources · build request 40, pain point 36, tool or technique 26, workaround 10, tool complaint 4, debate 3, link shared 2*

- **Problem:** AI news and product launches are overwhelming and hype-toned. People want curated, filterable digests and ways to follow topics without noise.
- **For:** Professionals and enthusiasts following AI or any fast-moving field
- **Evidence:** T259 (31 findings, 11 in last 90 days) includes #14832 requesting a daily agent that reads subscribed newsletters, #2985 on curated emerging-tech feeds, and #1850 on topic lists. T323 (23 findings) and T037 show demand for user-controlled, filtered feeds, including #10904 for excluding AI posts.
- **Existing alternatives:** news.smol.ai, Gemini scheduled summaries, HN digests, Techpresso, RSS readers. They are fixed-format and rarely user-tunable with exclusions and mood.
- **MVP:** Forward newsletters to a unique email address or add RSS feeds; set topics, exclusions and a hype filter; the app sends a daily digest with 5 items, one-line 'why it matters' and original links. Fuller product adds an X list import, a 'what changed since last week' view and a team digest.
- **Build notes:** Next.js, an inbound email service (Postmark or Resend inbound), RSS parsing, an LLM, scheduled jobs and Supabase. Hardest parts: reliable email parsing and de-duplication. Cost: low per user.
- **Demo hook:** Forward 40 newsletters; next morning's digest shows 5 ranked items with 'skip: hype' labels for the 12 it dropped.
- **Post angle:** "I get 40 newsletters. I read zero. Now I read one email a day, and it's mine."
- **Risks:** Many existing digest products, and low willingness to pay. Differentiation through filtering control and exclusions.
- **Themes:** T259 Keeping up with AI news without noise or hype; T323 Controllable social feeds; T037 Filtering AI slop and bot content from feeds

What people said:

> “build a tool that each day goes through all newsletters I'm subscribed to” — Colossus, Ben's Bites, 2026-10-29 ([link](https://www.bensbites.com/p/ai-is-overwhelming-and-im-doing-it))
>
> “would be nice to have 1 or a few sites with emerging tech” — BtM909, Hacker News — Ask HN, 2026-09-02 ([link](https://news.ycombinator.com/item?id=49535272))
>
> “I'm sure I will have to do that in 2028 for the politics list.” — Zvi Mowshowitz, Don't Worry About the Vase, 2026-07-14 ([link](https://thezvi.substack.com/p/twitter-thoughts-for-you))
>
> “an RSS feed for updates” — AINews (smol.ai), 2026-01-19 ([link](https://news.smol.ai/issues/26-01-19-not-much/))

### 24. Voice Notes to Structured Work

**Speak freely into your phone and get back an email draft, task list or meeting prep, in your own voice and format, never leaving your control.**

*Effort: 1-2 weekends · Confidence: low · 108 findings from 9 sources · tool or technique 49, build request 30, pain point 19, workaround 7, tool complaint 2, link shared 1*

- **Problem:** Users want fast private dictation and voice assistants that actually produce usable outputs in any app. Cloud-only tools raise privacy concerns.
- **For:** Busy professionals, managers and accessibility users who think better out loud
- **Evidence:** T215 (41 findings) and T175 (39 findings) show strong demand for local dictation, with #755 asking for open-source dictation matching Wispr Flow and #2694 for hands-free control. T257 (28 findings) shows voice agents sound unnatural, so output structure matters.
- **Existing alternatives:** Wispr Flow, Spokenly, MacWhisper, Typeless. They transcribe well but mostly insert raw text; few turn a messy ramble into a structured deliverable with templates.
- **MVP:** A PWA with a record button: speak, get transcript, then pick an output template (email, task list, status update, meeting prep, journal) and receive a clean draft in your style, with a copy button. Fuller product adds custom templates, a Slack/Notion send button and a local-first mode.
- **Build notes:** Next.js PWA, browser MediaRecorder, Whisper-style API, LLM templates, Supabase. Hardest parts: mobile browser audio quirks. Cost: a few cents per recording.
- **Demo hook:** A 60-second rambling voice memo on a walk becomes a clean status update email plus 5 action items in the demo.
- **Post angle:** "I think best while walking. So I built the thing that turns my rambling into a status update."
- **Risks:** A crowded category with strong incumbents, and OS dictation is improving. Differentiation depends on templates and workflow outputs.
- **Themes:** T215 Private local transcription, dictation and meeting capture; T175 Private offline and local voice assistants; T257 Voice assistants lack natural turn-taking

What people said:

> “Controlling your Mac with Voice.” — Ben's Bites, 2026-09-22 ([link](https://www.bensbites.com/p/what-can-you-build-with-jev))
>
> “it is much better to use Qwen3-ASR instead of Whisper medium” — antirez, Bluesky, 2026-02-12 ([link](https://bsky.app/profile/antirez.bsky.social/post/3meogdxi4222v))
>
> “more convenient than a phone app” — AINews (smol.ai), 2026-10-30 ([link](https://latent.space/p/ainews-building-aie-code-the-top-coding-agent-conference/))
>
> “Google should add Gemini voice mode into maps to allow open ended conversations” — Olivia Moore, Don't Worry About the Vase, 2026-07-02 ([link](https://thezvi.substack.com/p/ai-175-the-fable-continues))

