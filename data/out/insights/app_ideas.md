# App ideas: easy to prototype, useful or fun, worth sharing

*63 ideas mined from the findings by five passes (needs, hacks, new powers, culture, makers). Scores are Sonnet's 1-5 estimates; ranking = ease + shareable + the better of fun/useful + half the other. Each idea links the findings that sparked it.*

## Patterns

- Many ideas are near-duplicates, especially slop detection and voice preservation, which shows how strongly 'AI sounds generic' dominated the commentary; pick one best version rather than building several.
- The highest-scoring items pair a text-in, result-out flow with a shareable verdict such as a score, a receipt or a profile, which suits a 30-60 second demo and a LinkedIn or X post.
- Culture-argument ideas like bubble, Jevons and AGI debates turn jargon-heavy discourse into play, and they are timely hooks for a professional audience.
- Ideas that mostly repackage what a chatbot already does, such as handoff briefs and prompt interviews, only stand out through distinct packaging or personality, so keep the format sharp.
- The 3-4 week builds, such as game arenas, font generators and dataset makers, are poor first picks for a non-engineer; the weekend text-and-API apps give faster feedback.

## Start here

1. **Slop-o-Meter**: Paste any text and get a funny, highlighted 'slop score' with named tells like em-dash abuse, rule of three, and 'not X but Y' antithesis. *(A paste-and-score slop meter with highlighted tells is a weekend build, takes seconds to demo, and everyone wants to run their own post or a rival's through it.)*
2. **Argue Me Out of It**: A three-round debate game where AI steelmans the case against your idea and tracks every point you concede. *(A three-round debate where AI argues against your idea and counts your concessions is a weekend build, has a built-in scoreboard to screenshot, and works with any idea or opinion.)*
3. **Bubble or Not? Swipe Court**: A Tinder-style swipe game where you rule on real AI-bubble headlines and see which camp (Zitron, Smith, Marcus) you actually agree with. *(A swipe court on real AI-bubble headlines is fast to build, naturally ends in a shareable 'which camp are you' result, and rides a hot cultural argument.)*
4. **Voice Fingerprint**: Turn your past writing into a portable voice guide, then test whether any AI draft sounds like you. *(Building a voice fingerprint from your own writing and testing AI drafts against it speaks to the reader's own LinkedIn audience, and the before/after demo is strong.)*
5. **Side Project Graveyard**: A cemetery-themed board for all the half-built AI side projects you started, with a prompt to resurrect, merge or bury each. *(A cemetery board for abandoned side projects is a weekend build with instant humor that resonates with every vibe coder, and it makes a great personal story post.)*
6. **Do I Actually Get This?**: Paste anything AI wrote for you (memo, formula, script) and get a quick quiz to prove you understand it before you send it. *(A quiz to prove you understand what AI wrote for you before you send it is quick to build, solves a real professional worry, and has a fun pass/fail moment on screen.)*
7. **AGI Argument Referee**: Paste an AGI hot take and a referee bot identifies the debate move (moving goalposts, scaling-is-all, vibes-as-evidence) and calls it with a whistle. *(A referee bot that blows a whistle on AGI hot-take moves like goalpost-moving makes a funny, highly shareable 30-second demo and is easy to build.)*
8. **Jevons or Doom? Dev Job Slider**: A playful simulation where you adjust 'cost of software' and 'demand elasticity' sliders and watch the number of engineering jobs rise or crash. *(A Jevons-or-doom slider simulation is a weekend build with live-moving visuals that turn a heated job-market debate into something people can play with.)*
9. **Jira Horror**: Paste your boring work tasks and get them turned into a spooky audio-drama with an eerie narrator. *(Turning boring work tasks into a spooky audio drama is a pure delight demo that a corporate audience will share, and it takes a weekend with text-to-speech.)*
10. **Who Pays for the Free Tier?**: A satirical 'cost receipt' that shows what your free AI chat really costs the provider, and what you'd pay if subsidies ended. *(A satirical cost receipt for your free AI chat is quick to build, looks great as a screenshot, and puts a sharp point on the subsidy debate.)*
11. **Me.md**: A 5-minute interview that builds the personal context file you can paste into every AI tool you use. *(A five-minute interview that produces a portable personal context file is useful for any AI user, quick to build, and easy to show start to finish.)*

## All ideas

### Slop-o-Meter

**Paste any text and get a funny, highlighted 'slop score' with named tells like em-dash abuse, rule of three, and 'not X but Y' antithesis.**

*a weekend · fun 5 · useful 4 · ease 5 · shareable 5 · sparked by a common frustration · culture pass*

- **For:** LinkedIn posters, marketers, students and editors worried their writing reads as AI.
- **Why now:** Writers feel pressure to avoid AI tells and end up with contorted prose. A transparent, playful detector that shows pattern counts (not a pass/fail judgment) is wanted and shareable. ([The Algorithmic Bridge, 2026-04-21](https://www.thealgorithmicbridge.com/p/how-the-ai-writing-panic-is-making)) ([One Useful Thing, 2026-06-04](https://www.oneusefulthing.org/p/co-existence-and-the-end-of-co-intelligence)) ([Don't Worry About the Vase, 2025-11-17](https://thezvi.substack.com/p/on-writing-2)) ([Hacker News — Ask HN, 2026-11-04](https://news.ycombinator.com/item?id=50366117)) ([Bluesky, 2026-06-17](https://bsky.app/profile/gergely.pragmaticengineer.com/post/3mohzeauhjk22)) ([The Algorithmic Bridge, 2026-05-13](https://www.thealgorithmicbridge.com/p/how-this-small-startup-achieved-a)) ([The Algorithmic Bridge, 2026-08-12](https://www.thealgorithmicbridge.com/p/on-substack-pangram-partnership-its)) ([Bluesky, 2026-03-30](https://bsky.app/profile/bcmerchant.bsky.social/post/3micghrux7k2d)) ([The Algorithmic Bridge, 2026-05-13](https://www.thealgorithmicbridge.com/p/how-this-small-startup-achieved-a)) ([The Algorithmic Bridge, 2026-06-09](https://www.thealgorithmicbridge.com/p/nine-things-about-claude-mythos-5))
- **How it works:** User pastes text; rule-based detection highlights em dashes, triads, antithesis, stock phrases and gives a score with a cheeky verdict ('Certified Delve Enthusiast'). Optional AI call suggests a plainer rewrite of the worst sentence.
- **Build:** Single-page web app with regex/heuristics in JS, optional LLM call for rewrite. Hardest part: tuning heuristics so scores feel fair and not too noisy.
- **Demo moment:** Pasting a famous LinkedIn post and watching it light up like a Christmas tree with a 94% slop score.
- **Post hook:** I built a slop detector and ran my own old posts through it. Humbling. Try yours.
- **Risks:** Heuristic detectors give false positives; frame it as 'tells' not 'proof of AI'.

### Argue Me Out of It

**A three-round debate game where AI steelmans the case against your idea and tracks every point you concede.**

*a weekend · fun 5 · useful 4 · ease 5 · shareable 5 · sparked by a hack people use · hacks pass*

- **For:** Founders, managers and writers about to commit to a decision or hot take.
- **Why now:** People write custom instructions to make AI push back instead of agreeing, and use it as a sparring partner. A structured game makes the hack a one-click experience. ([Don't Worry About the Vase, 2026-04-08](https://thezvi.substack.com/p/ai-163-mythos-quest)) ([The Algorithmic Bridge, 2026-03-23](https://www.thealgorithmicbridge.com/p/the-one-thing-i-use-ai-for-that-actually)) ([Hacker News — Ask HN, 2026-03-19](https://news.ycombinator.com/item?id=47433702)) ([Bluesky, 2026-10-10](https://bsky.app/profile/mikecaulfield.bsky.social/post/3mxijogbzqc26)) ([Import AI, 2026-05-18](https://importai.substack.com/p/import-ai-457-ai-stuxnet-cursed-muon)) ([Bluesky, 2026-09-02](https://bsky.app/profile/anildash.com/post/3muk3dpvqcc2c)) ([Don't Worry About the Vase, 2026-06-04](https://thezvi.substack.com/p/ai-171-false-flag)) ([Lenny's Newsletter, 2026-09-29](https://www.lennysnewsletter.com/p/all-of-the-lenny-and-friends-summit)) ([Simon Willison's Weblog, 2026-07-21](https://simonwillison.net/2026/Jul/21/cat-and-thariq/)) ([Hacker News — Ask HN, 2026-02-26](https://news.ycombinator.com/item?id=47160641))
- **How it works:** The user enters a belief or plan and rates their confidence. The AI delivers its strongest counterargument, the user responds, and it goes three rounds. A scorecard shows conceded points, unanswered objections and a before/after confidence delta.
- **Build:** Chat-style web app with a system prompt for steelmanning and structured JSON scoring per round. Hardest part is keeping the pushback sharp but not hostile.
- **Demo moment:** The confidence slider drops from 90 to 60 after the AI finds the one objection the user could not answer.
- **Post hook:** I asked AI to disagree with my strategy for 3 rounds. It won 2 of them.
- **Risks:** Generic chatbots can be told to do this; the value is in the scoring and format.

### Bubble or Not? Swipe Court

**A Tinder-style swipe game where you rule on real AI-bubble headlines and see which camp (Zitron, Smith, Marcus) you actually agree with.**

*a weekend · fun 5 · useful 3 · ease 5 · shareable 5 · sparked by a cultural moment · culture pass*

- **For:** Curious professionals, investors-by-accident, anyone whose group chat argues about whether AI is a bubble.
- **Why now:** The bubble argument is everywhere and polarized, with smart people disagreeing on the same revenue facts. A game that makes you commit to positions is more engaging than another take. ([Marcus on AI, 2026-06-26](https://garymarcus.substack.com/p/the-month-generative-ai-lost-its)) ([Bluesky, 2026-10-20](https://bsky.app/profile/edzitron.com/post/3myd2tohovq2v)) ([Hacker News — Ask HN, 2026-11-04](https://news.ycombinator.com/item?id=50362700)) ([Don't Worry About the Vase, 2026-04-23](https://thezvi.substack.com/p/ai-165-in-our-image))
- **How it works:** User swipes 15 cards, each a paraphrased claim (revenue growth, circular deals, dot-com comparison, bailout odds) with agree/disagree/unsure. At the end they get a shareable 'bubble personality' card showing which commentator they align with and how their view compares with others.
- **Build:** Next.js or plain React, static JSON of cards, simple scoring matrix, share image via html-to-image. Hardest part is writing fair, balanced cards that don't misrepresent the named people; use archetypes instead of real names if needed.
- **Demo moment:** Swiping through cards fast, then the reveal of a result card like 'You are 70% Ed Zitron, 30% Noah Smith'.
- **Post hook:** I built a 2-minute quiz that tells you what kind of AI-bubble believer you are. I turned out to be a 'Circular Deal Skeptic.' What are you?
- **Risks:** Misattributing positions to real people; keep them as archetypes. Facts go stale quickly.

### Voice Fingerprint

**Turn your past writing into a portable voice guide, then test whether any AI draft sounds like you.**

*1-2 weeks · fun 4 · useful 4 · ease 4 · shareable 5 · sparked by a hack people use · hacks pass*

- **For:** LinkedIn and newsletter writers who want AI help without sounding like AI.
- **Why now:** People hand-craft voice skill files and style guides, and critics question whether they work. A tool that builds the guide and also tests it would settle the argument. ([Bluesky, 2026-04-21](https://bsky.app/profile/edzitron.com/post/3mjy2n37vi22v)) ([Ben's Bites, 2026-03-24](https://www.bensbites.com/p/agents-should-interview-you)) ([Exponential View, 2026-03-05](https://www.exponentialview.co/p/how-i-think)) ([Don't Worry About the Vase, 2026-03-11](https://thezvi.substack.com/p/gpt-54-is-a-substantial-upgrade)) ([Exponential View, 2026-03-13](https://www.exponentialview.co/p/the-lantern-and-the-flame)) ([Ben's Bites, 2026-02-12](https://www.bensbites.com/p/something-big-is-happening)) ([Don't Worry About the Vase, 2025-11-17](https://thezvi.substack.com/p/on-writing-2)) ([The Algorithmic Bridge, 2026-04-21](https://www.thealgorithmicbridge.com/p/how-the-ai-writing-panic-is-making)) ([One Useful Thing, 2026-06-04](https://www.oneusefulthing.org/p/co-existence-and-the-end-of-co-intelligence)) ([The Algorithmic Bridge, 2026-06-09](https://www.thealgorithmicbridge.com/p/nine-things-about-claude-mythos-5)) ([Don't Worry About the Vase, 2026-02-10](https://thezvi.substack.com/p/claude-opus-46-system-card-part-2))
- **How it works:** The user pastes 5-10 samples of their writing. The app produces a one-page voice guide (rhythm, pet phrases, taboo words, examples) to paste into any AI tool. A 'sounds like me?' tester scores a new draft and highlights the lines that break the voice.
- **Build:** Simple web app with an LLM API for analysis and scoring, with copy and download of the guide as markdown. Hardest part is a scoring method that is not just flattery.
- **Demo moment:** A generic AI paragraph gets a 41% voice match with offending phrases highlighted. After applying the guide, it rewrites to 88%.
- **Post hook:** I built a lie detector for 'does this sound like me?' Here's my score on my last 5 posts.
- **Risks:** Scoring is subjective; writing samples are personal data.

### Side Project Graveyard

**A cemetery-themed board for all the half-built AI side projects you started, with a prompt to resurrect, merge or bury each.**

*a weekend · fun 5 · useful 3 · ease 5 · shareable 5 · sparked by a common frustration · needs pass*

- **For:** Vibe coders and tinkerers who start many things in an hour and finish none
- **Why now:** Agents let people spin up many projects that get abandoned and fragment attention; a playful ritual of triage makes it manageable. ([Simon Willison's Weblog, 2026-05-31](https://simonwillison.net/2026/May/31/the-solution-might-be-cancelling-my-ai-subscription/)) ([Latent Space, 2026-10-02](https://latent.space/p/rlm/)) ([Hacker News — Ask HN, 2026-03-24](https://news.ycombinator.com/item?id=47511075))
- **How it works:** User adds projects (name, one line, last touched). Each gets a tombstone; the app asks 3 questions and recommends resurrect, merge, or bury with an epitaph. A weekly 'pick one' nudge keeps focus on a single project.
- **Build:** Mobile-friendly React app with localStorage, an LLM for epitaphs and triage advice. Hardest part: keeping it fun, not another to-do list.
- **Demo moment:** Tombstones rise on screen as a user buries a project with a funny auto-written epitaph.
- **Post hook:** I had 23 abandoned AI side projects. I built a graveyard for them. 4 got resurrected.
- **Risks:** Niche audience; risk of a one-time use.

### Do I Actually Get This?

**Paste anything AI wrote for you (memo, formula, script) and get a quick quiz to prove you understand it before you send it.**

*a weekend · fun 4 · useful 4 · ease 5 · shareable 4 · sparked by a cultural moment · hacks pass*

- **For:** Professionals who use AI-written content or spreadsheets and must defend them in meetings.
- **Why now:** There is growing worry that people lose understanding of AI-produced work, and developers keep checking output step by step to keep their grip. A quiz turns passive acceptance into active comprehension. ([AINews (smol.ai), 2026-01-14](https://news.smol.ai/issues/26-01-14-not-much/)) ([Hacker News — Ask HN, 2026-10-19](https://news.ycombinator.com/item?id=50151036)) ([Marcus on AI, 2026-04-27](https://garymarcus.substack.com/p/dario-amodei-hype-ai-safety-and-the)) ([Bluesky, 2026-08-19](https://bsky.app/profile/charity.wtf/post/3mtgw45ee222b))
- **How it works:** The user pastes the AI output and the context. The app generates five questions of rising difficulty, such as 'Why does this formula use absolute references?' and 'What would a skeptical VP challenge?'. After answering, the user gets a comprehension score and a short explainer on the gaps.
- **Build:** Web app with LLM question generation and grading, plus shareable score cards. Hardest part is questions that test understanding rather than recall.
- **Demo moment:** A pasted Excel formula yields a quiz and a 3/5 score, and the explainer fills the gaps.
- **Post hook:** AI wrote it, but could you defend it in the meeting? I built a 2-minute test.
- **Risks:** Quiz quality varies; the user can ignore it.

### AGI Argument Referee

**Paste an AGI hot take and a referee bot identifies the debate move (moving goalposts, scaling-is-all, vibes-as-evidence) and calls it with a whistle.**

*a weekend · fun 5 · useful 3 · ease 4 · shareable 5 · sparked by a cultural moment · culture pass*

- **For:** People who follow AI arguments online and want a laugh and a clearer view.
- **Why now:** Scaling vs world models vs 'LLMs aren't enough' debates recycle the same rhetorical moves. A playful referee that names them teaches critical reading. ([Marcus on AI, 2026-03-14](https://garymarcus.substack.com/p/breaking-expensive-new-evidence-that)) ([Bluesky, 2026-09-12](https://bsky.app/profile/hardmaru.bsky.social/post/3mvdg3pillk22)) ([AINews (smol.ai), 2026-01-08](https://news.smol.ai/issues/26-01-08-not-much/)) ([Marcus on AI, 2026-09-09](https://garymarcus.substack.com/p/the-case-for-boycotting-generative))
- **How it works:** User pastes a tweet or paragraph. An LLM returns a penalty card (e.g., 'Goalpost shift, 5 yards'), the strongest point made, and the missing evidence. A replay-style commentary adds humor.
- **Build:** Simple web page with a structured LLM prompt returning JSON, sports-style UI. Hardest part: keeping outputs consistent and fair across both sides.
- **Demo moment:** Pasting a spicy tweet and a referee card slams down: 'Flag: appeal to the next model release'.
- **Post hook:** I built a referee for AI arguments. It flagged both Gary Marcus and his critics. Paste your favorite take.
- **Risks:** Can appear biased; prompt for even-handedness and show reasoning.

### Jevons or Doom? Dev Job Slider

**A playful simulation where you adjust 'cost of software' and 'demand elasticity' sliders and watch the number of engineering jobs rise or crash.**

*a weekend · fun 4 · useful 4 · ease 5 · shareable 4 · sparked by a cultural moment · culture pass*

- **For:** Non-engineers and engineers wanting to understand the Jevons paradox argument.
- **Why now:** The Jevons paradox is invoked constantly in the engineering-jobs debate yet rarely explained. A toy model makes the logic intuitive. ([AI as Normal Technology, 2026-07-13](https://www.normaltech.ai/p/what-will-be-left-for-us-to-work)) ([Simon Willison's Weblog, 2026-01-08](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/)) ([AINews (smol.ai), 2026-03-06](https://news.smol.ai/issues/26-03-06-not-much/)) ([Bluesky, 2026-05-27](https://bsky.app/profile/caseynewton.bsky.social/post/3mms7tkwgp222))
- **How it works:** User moves two sliders (AI productivity gain, how much new demand cheaper software creates). A bar chart of jobs animates with a plain-language caption ('Demand outran productivity: more devs'). Presets for 'Optimist', 'Pessimist', 'Agents automate everything'.
- **Build:** Single page React with a simple formula and Chart.js. Hardest part: choosing a model that's simple but not misleading.
- **Demo moment:** Dragging the elasticity slider past a threshold and watching jobs flip from falling to booming.
- **Post hook:** The 'Jevons paradox will save software jobs' argument is just one slider. Here's the slider.
- **Risks:** Toy model could be read as prediction; label clearly as illustrative.

### Jira Horror

**Paste your boring work tasks and get them turned into a spooky audio-drama with an eerie narrator.**

*a weekend · fun 5 · useful 2 · ease 5 · shareable 5 · sparked by a cultural moment · powers pass*

- **For:** Office workers, PMs and anyone who enjoys workplace humor
- **Why now:** Someone turned real Jira tickets into horror-game audiologs, showing that mundane work artifacts become funny when reframed as narrative. TTS is now good enough to deliver it. ([Bluesky, 2026-10-30](https://bsky.app/profile/emollick.bsky.social/post/3mz2nfm6wts2m)) ([AINews (smol.ai), 2026-10-31](https://latent.space/p/ainews-google-admits-ai-mode-hurts-search-revenue-15-500b-drop-worst-since-2004-ipo-ai-bear-market-c/))
- **How it works:** User pastes 5-10 task titles or a standup note and picks a genre (horror, noir, nature documentary). The LLM writes short log entries and a TTS voice reads them over a looping ambient track. Result plays as a shareable audio card.
- **Build:** Simple web page, LLM for scripting, a TTS API such as ElevenLabs or OpenAI TTS, and a looped royalty-free ambient track. Hardest part is tone: the script must stay funny, not just creepy, and must avoid leaking confidential info.
- **Demo moment:** Paste 'Q3 roadmap sync moved again' and hear a whispering narrator describe the meeting that would not end.
- **Post hook:** I turned my sprint backlog into a horror podcast.
- **Risks:** Users may paste confidential tickets; add a warning and offer a sample mode.

### Who Pays for the Free Tier?

**A satirical 'cost receipt' that shows what your free AI chat really costs the provider, and what you'd pay if subsidies ended.**

*a weekend · fun 4 · useful 3 · ease 5 · shareable 5 · sparked by a cultural moment · culture pass*

- **For:** General public who assume AI is free and don't know about subsidized pricing.
- **Why now:** Subsidized inference and fragile economics are a core worry. A receipt format makes the abstract concrete and personal. ([Latent Space, 2026-06-12](https://latent.space/p/loopcraft/)) ([AINews (smol.ai), 2026-05-01](https://news.smol.ai/issues/26-05-01-not-much/)) ([Hacker News — Ask HN, 2026-02-16](https://news.ycombinator.com/item?id=47034849)) ([Tomasz Tunguz, 2026-06-07](https://tomtunguz.com/inflation-deflation-ai/))
- **How it works:** User enters their usual weekly AI use (chats, images, code help). The app prints a funny itemized receipt showing the 'true cost' vs 'what you paid' with stylized assumptions, plus a 'if prices normalize' total.
- **Build:** Static React with adjustable assumptions and a receipt-styled share image. Hardest part: choosing defensible, clearly-labeled assumptions.
- **Demo moment:** The receipt prints out line by line ending with 'You owe: $47/month (you paid $0)'.
- **Post hook:** I made my AI receipt. My 'free' ChatGPT habit would cost me $47 a month at unsubsidized prices. What's yours?
- **Risks:** Numbers are estimates; present as illustrative and let users edit assumptions.

### Me.md

**A 5-minute interview that builds the personal context file you can paste into every AI tool you use.**

*a weekend · fun 3 · useful 4 · ease 5 · shareable 4 · sparked by a hack people use · hacks pass*

- **For:** Everyday professionals tired of re-explaining their role, preferences and projects to each chatbot.
- **Why now:** Engineers keep AGENTS.md and TRAVEL.md-style context files so agents know them. Non-engineers have no easy way to create the equivalent. ([Ben's Bites, 2026-07-02](https://www.bensbites.com/p/fable-is-back)) ([Hacker News — Ask HN, 2025-11-17](https://news.ycombinator.com/item?id=45950934)) ([Hacker News — Ask HN, 2026-05-16](https://news.ycombinator.com/item?id=48160604)) ([Latent Space, 2026-09-29](https://latent.space/p/thariq/))
- **How it works:** A friendly chat asks adaptive questions about role, communication style, current projects, tools and pet peeves. It outputs a structured Me.md with sections such as Work, Writing, Travel and Never Do. The user copies it into custom instructions or downloads it as a file.
- **Build:** Chat UI with an LLM that asks one question at a time and fills a JSON schema, then renders markdown. Hardest part is keeping the interview short while collecting useful detail.
- **Demo moment:** After five questions, a clean one-page 'user manual for working with me' appears and is pasted into ChatGPT to show the answer quality change.
- **Post hook:** Every AI chat starts with you as a stranger. I built a 5-minute fix.
- **Risks:** ChatGPT memory partially overlaps; privacy concerns around personal details.

### AI Pricing Bingo

**A live bingo card of recurring AI industry tropes (price cut, 'this changes everything', silent plan change, bubble tweet) you mark as news happens.**

*a weekend · fun 5 · useful 2 · ease 5 · shareable 5 · sparked by a cultural moment · culture pass*

- **For:** AI-news-fatigued professionals and the LinkedIn crowd who enjoy gentle self-mockery.
- **Why now:** Vendor pricing changes via tweets, hype cycles, and bubble arguments recur predictably. Bingo turns fatigue into humor and encourages sharing. ([Simon Willison's Weblog, 2026-04-22](https://simonwillison.net/2026/Apr/22/claude-code-confusion/)) ([Bluesky, 2026-04-21](https://bsky.app/profile/simonwillison.net/post/3mk24tklb522i)) ([Tomasz Tunguz, 2026-08-04](https://tomtunguz.com/what-if-gpu-prices-double/)) ([Marcus on AI, 2026-06-26](https://garymarcus.substack.com/p/the-month-generative-ai-lost-its))
- **How it works:** Users get a randomized 5x5 card of squares such as 'Price cut announced via tweet' or 'Someone compares it to dot-com'. They tap squares during a week; completing a line triggers confetti and a shareable card. Friends can compare cards.
- **Build:** Static React app with local storage and a share image. Hardest part: writing a funny, evergreen set of squares.
- **Demo moment:** Tapping a square while scrolling feeds and the BINGO confetti triggers.
- **Post hook:** I made AI Twitter Bingo. I got a full row before lunch. Post your card.
- **Risks:** Humor may be hit or miss; keep it affectionate not mean.

### Human or Slop? The Guessing Game

**Show two paragraphs, one written by a human author and one by AI, and guess which; see how your streak compares to others.**

*1-2 weeks · fun 5 · useful 3 · ease 4 · shareable 5 · sparked by a cultural moment · culture pass*

- **For:** General public, writers, teachers, curious LinkedIn crowd.
- **Why now:** Everyone claims they can spot AI prose, and the tells argument is hot. A head-to-head game tests that confidence and teaches the tells. ([The Algorithmic Bridge, 2026-04-21](https://www.thealgorithmicbridge.com/p/how-the-ai-writing-panic-is-making)) ([One Useful Thing, 2026-06-04](https://www.oneusefulthing.org/p/co-existence-and-the-end-of-co-intelligence)) ([Don't Worry About the Vase, 2025-11-17](https://thezvi.substack.com/p/on-writing-2))
- **How it works:** Each round shows two passages on the same prompt; user picks the AI one, then gets a reveal explaining the tells. Final screen: accuracy, 'detector rank', and a share card.
- **Build:** Static web app with curated passage pairs (public-domain human text plus pre-generated AI text). Hardest part: curating good pairs and avoiding copyright problems.
- **Demo moment:** Confidently choosing wrong, then the reveal highlighting the AI tells.
- **Post hook:** I got 6 out of 10 on spotting AI writing. Most people think they'd get 9. Take the test.
- **Risks:** Content curation effort; results could discourage if too hard.

### Ask Me First

**Before you send a prompt, an AI interviews you with the questions that matter and builds the final prompt.**

*a weekend · fun 3 · useful 4 · ease 5 · shareable 4 · sparked by a hack people use · hacks pass*

- **For:** Non-technical AI users whose results suffer from vague requests.
- **Why now:** Planning workflows and ask-user-question elicitation surface requirements before the agent starts. The same trick helps any professional prompt. ([Latent Space, 2026-09-29](https://latent.space/p/thariq/)) ([Hacker News — Ask HN, 2026-01-20](https://news.ycombinator.com/item?id=46691243)) ([Ben's Bites, 2026-10-27](https://www.bensbites.com/p/is-anthropic-the-best-business-in)) ([AINews (smol.ai), 2026-04-24](https://news.smol.ai/issues/26-04-24-deepseek-v4/))
- **How it works:** The user types a rough request. The app asks 3-6 multiple-choice clarifying questions tailored to it, such as audience, length and what to avoid. It assembles a structured prompt, previews it and sends it to the model alongside a before/after comparison.
- **Build:** Web app with a two-step LLM chain: question generator, then prompt assembler. Hardest part is questions that are specific, not generic.
- **Demo moment:** A vague 'write a project update' request becomes a sharp prompt after four taps, and the side-by-side outputs differ sharply.
- **Post hook:** The best prompt trick: make the AI interview you first.
- **Risks:** Chat assistants can already ask questions when told to; the packaging must be faster.

### Boss & Interns

**Watch a smart AI break your goal into pieces and hand them to cheaper AI interns, with the bill shown live.**

*1-2 weeks · fun 5 · useful 3 · ease 3 · shareable 5 · sparked by a new AI capability · hacks pass*

- **For:** Curious professionals who hear about 'agent orchestration' and want to see it work.
- **Why now:** The planner plus cheap executor pattern is everywhere in agent circles. It is abstract, so a visual explainer that actually does a task would help people grasp it. ([Don't Worry About the Vase, 2026-07-28](https://thezvi.substack.com/p/claude-opus-5-is-highly-capable-but)) ([Bluesky, 2026-07-04](https://bsky.app/profile/emollick.bsky.social/post/3mps4xss2uc2t)) ([AINews (smol.ai), 2026-07-09](https://news.smol.ai/issues/26-07-09-gpt-56/)) ([Ben's Bites, 2026-09-24](https://www.bensbites.com/p/back-to-claude))
- **How it works:** The user enters a goal like 'plan a 3-day offsite'. The boss model produces a task list, and intern models run each task in parallel as animated cards. The boss reviews and assembles the result while a cost meter compares against a single big-model run.
- **Build:** React page with parallel API calls to one strong and one cheap model, with streaming cards. Hardest part is task decomposition reliability and clean assembly.
- **Demo moment:** Six intern cards light up at once, finish in seconds, and the boss merges them into a polished plan with '73% cheaper' on screen.
- **Post hook:** This is what an AI 'agent team' actually looks like, and why it's cheaper.
- **Risks:** Cost savings claims depend on current prices; output may not beat a single model.

### Chat Escape Pod

**Turn a messy long AI conversation into a clean, portable 'brain transfer' brief you can paste into any other chatbot.**

*a weekend · fun 3 · useful 5 · ease 4 · shareable 4 · sparked by a hack people use · needs pass*

- **For:** Anyone whose long chats died, hit limits, or who is switching AI providers
- **Why now:** Memory and history are locked into vendors, and people already hack around with summaries and re-uploaded PDFs. A purpose-built hand-off packaging is the product. ([Hacker News — Ask HN, 2026-11-02](https://news.ycombinator.com/item?id=50336034)) ([Ben's Bites, 2026-08-21](https://www.bensbites.com/p/how-i-built-this)) ([AINews (smol.ai), 2025-12-24](https://news.smol.ai/issues/25-12-24-nvidia-groq/)) ([AINews (smol.ai), 2026-08-31](https://news.smol.ai/issues/26-08-31-not-much/)) ([Ben's Bites, 2026-04-16](https://www.bensbites.com/p/my-cheatsheet-for-a-clean-context)) ([Don't Worry About the Vase, 2026-03-11](https://thezvi.substack.com/p/gpt-54-is-a-substantial-upgrade)) ([AINews (smol.ai), 2026-10-24](https://latent.space/p/ainews-kimi-31/))
- **How it works:** User pastes or uploads an exported chat. The app extracts goals, decisions, open questions, preferences and style, and outputs a compact brief with a 'paste this into Claude/ChatGPT/Gemini' button. Optionally keeps a local library of briefs.
- **Build:** Web app with file upload (JSON/txt), LLM summarization with a fixed template, localStorage for the library. Hardest part: handling very long transcripts via chunking.
- **Demo moment:** Drop in a 200-page chat export and get a one-page brief that works instantly in a new chatbot.
- **Post hook:** My ChatGPT history is a hostage situation. I built an escape pod.
- **Risks:** Export formats vary by vendor and change; privacy concerns about uploading chats.

### Make It A LOT More Fun

**Paste in any boring thing, such as a chore list, a quiz, or a meeting agenda, and get a gamified version that is playable in the browser.**

*1-2 weeks · fun 5 · useful 3 · ease 3 · shareable 5 · sparked by a new AI capability · makers pass*

- **For:** Teachers, team leads and parents who want to make dull material engaging
- **Why now:** Simon found that telling Claude to make a game 'a LOT more fun' markedly improved the design, and vibe-coded games have become genuinely fun. The prompt trick becomes a product when packaged with a fun-dial. ([Simon Willison's Weblog, 2026-10-28](https://simonwillison.net/2026/Oct/28/vibe-game-development/)) ([Ben's Bites, 2026-10-29](https://www.bensbites.com/p/ai-is-overwhelming-and-im-doing-it)) ([Simon Willison's Weblog, 2026-10-28](https://simonwillison.net/2026/Oct/28/vibe-game-development/))
- **How it works:** User pastes content and picks a fun-dial level from 1 to 5. The app generates a single-file HTML mini-game and then re-runs a 'make it a LOT more fun' pass. User plays it instantly and gets a share link.
- **Build:** Next.js or plain HTML, LLM API generating a single HTML file, rendered in a sandboxed iframe. Hardest part is reliably valid, safe output; use a template skeleton and validate before showing.
- **Demo moment:** Press the fun-dial from 1 to 5 and watch the same compliance training quiz become a chaotic boss battle.
- **Post hook:** One sentence made my AI games dramatically better. So I built a dial for it.
- **Risks:** Generic output and sandboxing issues; API cost per generation.

### Model Gallery Arena

**Give one weird creative prompt to several AI models and see their outputs side by side in a shareable grid.**

*1-2 weeks · fun 5 · useful 3 · ease 3 · shareable 5 · sparked by something someone built · makers pass*

- **For:** AI-curious professionals who want to judge models for themselves
- **Why now:** Simon's pelican-on-bicycle grid and Mollick's Harbor Town benchmark show personal weird benchmarks are beloved and sticky, but each is a one-off built by experts. ([Simon Willison's Weblog, 2026-10-26](https://simonwillison.net/2026/Oct/26/gpt-61-terra/)) ([Bluesky, 2026-07-16](https://bsky.app/profile/emollick.bsky.social/post/3mqryjkgzjc2q)) ([Bluesky, 2026-07-20](https://bsky.app/profile/emollick.bsky.social/post/3mr44tng2ak2f))
- **How it works:** User picks a quirky challenge such as 'draw a pelican on a bicycle' or 'a procedurally generated harbor town'. The app sends it to multiple models using the user's keys or a demo budget. Results render in a grid with voting and a share image.
- **Build:** Web app with API calls to several providers via OpenRouter; render SVG or HTML outputs in sandboxed iframes. Hardest part is safely rendering generated code and managing cost.
- **Demo moment:** Eight tiny bicycles appear in a grid, each wildly different, and you tap your favourite.
- **Post hook:** Forget benchmarks. I made a gallery to compare AI models on pelicans.
- **Risks:** API costs; the quality of the challenge library matters.

### Review Debt Meter

**A daily budget for how much AI-generated work you can honestly review, with a meter that fills as you paste.**

*a weekend · fun 4 · useful 3 · ease 5 · shareable 4 · sparked by a cultural moment · hacks pass*

- **For:** Managers and analysts who let AI produce more than they can check.
- **Why now:** Some developers cap daily agent output to what they can realistically review, while human review is the bottleneck everywhere. A playful meter makes the discipline visible. ([Simon Willison's Weblog, 2026-03-25](https://simonwillison.net/2026/Mar/25/thoughts-on-slowing-the-fuck-down/)) ([Ben's Bites, 2026-03-10](https://www.bensbites.com/p/just-use-gpt-54-xhigh)) ([Latent Space, 2026-10-21](https://latent.space/p/claude-mods/)) ([Hacker News — Ask HN, 2026-08-08](https://news.ycombinator.com/item?id=49227024))
- **How it works:** The user sets a daily review capacity in pages or minutes. Each time they paste AI output, the app estimates review time and adds it to the meter, with stages from 'fine' to 'rubber stamping'. A weekly recap shows unreviewed output.
- **Build:** Client-side web app or Chrome extension with local storage and a simple reading-time heuristic plus an optional LLM risk rating. Hardest part is making the estimate feel meaningful.
- **Demo moment:** The gauge climbs into the red as three AI reports are pasted, and a banner says 'You are now rubber-stamping.'
- **Post hook:** AI can write faster than you can read. I built a speedometer for it.
- **Risks:** Relies on user discipline; novelty may wear off.

### Scene Spinner

**Upload a short video clip of a room or object and get a spinnable 3D web scene you can embed.**

*1-2 weeks · fun 5 · useful 3 · ease 3 · shareable 5 · sparked by a new AI capability · powers pass*

- **For:** Real estate hobbyists, Etsy sellers, parents and travelers who want 3D memories
- **Why now:** Mollick showed video clips becoming interactive three.js scenes in a few prompts, so a simple wrapper could bring that to everyone. ([Bluesky, 2026-11-10](https://bsky.app/profile/emollick.bsky.social/post/3mzxw7q2jgs2r)) ([Simon Willison's Weblog, 2026-09-28](https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/)) ([AINews (smol.ai), 2026-11-07](https://latent.space/p/ainews-anthropic-ipo-whither-now/))
- **How it works:** User uploads a 10-second clip. The app extracts frames, a vision LLM writes a stylized three.js scene approximating layout and objects, and it renders in a viewer with orbit controls. A share link and embed code are provided.
- **Build:** Frame extraction in browser, multimodal LLM generating three.js code, sandboxed iframe preview. Hardest part is making scenes look consistent rather than random; lean into a low-poly diorama style.
- **Demo moment:** A shaky living room video becomes a tiny low-poly diorama you can rotate.
- **Post hook:** I turned a 10-second video of my desk into a 3D diorama.
- **Risks:** Output is approximate not photoreal; set expectations with the diorama framing.

### Unstick Me

**When your AI chat goes in circles, paste it and get the diagnosis plus three reset moves.**

*a weekend · fun 3 · useful 4 · ease 5 · shareable 4 · sparked by a common frustration · hacks pass*

- **For:** Anyone who has watched a chatbot repeat the same wrong answer for 20 minutes.
- **Why now:** Agent users unstick churning loops by switching models, lowering reasoning effort or giving one nudge. The routine is learnable but not obvious to newcomers. ([Don't Worry About the Vase, 2026-05-08](https://thezvi.substack.com/p/claude-code-codex-and-agentic-coding-f54)) ([Latent Space, 2026-07-03](https://latent.space/p/aiewf-daily-dispatch-locomotives/)) ([AINews (smol.ai), 2026-05-08](https://news.smol.ai/issues/26-05-08-not-much/)) ([Simon Willison's Weblog, 2026-04-30](https://simonwillison.net/2026/Apr/30/codex-goals/))
- **How it works:** The user pastes the stuck conversation. The app identifies the pattern (repeating itself, conflicting constraints, missing info, task too big) and suggests three moves, such as splitting the task or restating the goal, each with a ready-to-paste prompt. A 'try again in another model' link is included.
- **Build:** Simple web app with an LLM diagnosing against a fixed list of loop patterns. Hardest part is writing a good taxonomy and reset prompts.
- **Demo moment:** A frustrating circular chat is diagnosed as 'contradictory constraints', and the suggested reset prompt fixes it on the first try.
- **Post hook:** The 4 reasons your AI keeps looping and the one-line fix for each.
- **Risks:** Diagnoses can be wrong; generic advice might be enough.

### Voice Memo Remix

**Hum or ramble an idea into your phone and get back a produced track in a chosen genre.**

*1-2 weeks · fun 5 · useful 3 · ease 3 · shareable 5 · sparked by a new AI capability · powers pass*

- **For:** Hobbyist musicians, creators and curious non-musicians
- **Why now:** Suno-style models can now turn rough voice memos into full productions, and hobbyist communities already share this music. ([Understanding AI, 2026-10-19](https://www.understandingai.org/p/ai-is-ushering-in-an-age-personal)) ([Understanding AI, 2026-10-19](https://www.understandingai.org/p/ai-is-ushering-in-an-age-personal)) ([Hacker News — Ask HN, 2026-10-05](https://news.ycombinator.com/item?id=49972125))
- **How it works:** User records or uploads a 20-second hum. They pick a genre card (lo-fi, polka, synthwave) and the app submits the audio to a music-generation API. It returns before and after players for side-by-side sharing.
- **Build:** Mobile-friendly web page with MediaRecorder, a music generation API with audio-to-audio support, and a split-screen share page. Hardest part is API availability and licensing; fall back to a text-conditioned model if audio input is unavailable.
- **Demo moment:** Play a clumsy kitchen hum, then the same melody as a polished synthwave track.
- **Post hook:** My off-key shower humming, remixed in 5 genres.
- **Risks:** Music API access may be restricted or costly; copyright of outputs is murky.

### Beep Hunter

**Turn the phones and laptops in your house into a team that finds the mystery chirp from a smoke detector or appliance.**

*1-2 weeks · fun 4 · useful 4 · ease 3 · shareable 5 · sparked by something someone built · makers pass*

- **For:** Homeowners and renters annoyed by an intermittent beep they cannot locate
- **Why now:** Simon Willison vibe-coded a multi-device acoustic triangulation system to find a beep. It is a delightful, relatable problem that most people never solve, and the maker version is developer-only. ([Simon Willison's Weblog, 2026-11-09](https://simonwillison.net/2026/Nov/9/mysterious-beeps/)) ([Bluesky, 2026-10-20](https://bsky.app/profile/simonwillison.net/post/3mydffvspjs2x))
- **How it works:** Open the page on every device you have and join a room with a short code. Each device listens through its mic and timestamps the beep. The host page shows a heat-map of which device heard it first, so you walk toward the loudest or earliest one.
- **Build:** Static web app with Web Audio API and a tiny WebSocket or Firebase relay for rooms. Hardest part is clock sync across devices, so use loudness comparison instead of precise timing for v1.
- **Demo moment:** A beep sounds, three phones on the table light up in order, and an arrow points to the cupboard where the chirping device is.
- **Post hook:** I turned my junk drawer of old phones into a beep-finding detective squad.
- **Risks:** Mic permission friction and echo make accuracy fuzzy; frame it as a hot-or-cold game rather than precision.

### Brain Gym

**Daily 5-minute 'think first, then compare to AI' drills that keep your own reasoning sharp.**

*1-2 weeks · fun 4 · useful 4 · ease 4 · shareable 4 · sparked by a cultural moment · needs pass*

- **For:** Professionals worried about outsourcing their thinking to AI
- **Why now:** Cognitive offloading and skill atrophy are widely worried about, but current remedies are vague (go handwrite). A game structure makes deliberate practice easy. ([The Algorithmic Bridge, 2026-10-21](https://www.thealgorithmicbridge.com/p/put-some-brain-in-your-thinking)) ([Marcus on AI, 2026-10-24](https://garymarcus.substack.com/p/will-generative-ai-do-more-harm-than)) ([Hacker News — Ask HN, 2026-03-15](https://news.ycombinator.com/item?id=47388646))
- **How it works:** The app gives a daily work-style puzzle (e.g. summarize this memo, spot the flaw). The user answers first, then the AI reveals its answer and scores the gap on structure and insight. A streak and a 'your thinking vs AI' chart build over time.
- **Build:** Mobile-friendly web app, LLM generates the scenario and grades the user answer against a rubric, simple streaks in localStorage. Hardest part: fair grading and fresh daily content.
- **Demo moment:** The reveal: your answer next to the AI's, with a 'you caught what it missed' badge.
- **Post hook:** I'm building a gym for the muscle AI is quietly weakening: your own thinking.
- **Risks:** Retention depends on a daily habit; grading subjectivity.

### Coding Agent Feelings Wheel

**A mood-check quiz for people who work alongside AI tools (relief, loss, FOMO, busier-than-ever) that returns a shareable 'AI work feelings' profile.**

*a weekend · fun 4 · useful 2 · ease 5 · shareable 4 · sparked by a cultural moment · culture pass*

- **For:** Knowledge workers and developers feeling mixed emotions about AI coding agents and automation.
- **Why now:** Programmers describe both real loss of puzzle-solving and relief at drudgery, and others say agents make them busier. People want language for ambivalence. ([Simon Willison's Weblog, 2026-10-19](https://simonwillison.net/2026/Oct/19/my-obituary-for-programming/)) ([Bluesky, 2026-01-19](https://bsky.app/profile/benjedwards.com/post/3mcrswsei2k2j)) ([Ben's Bites, 2026-09-29](https://www.bensbites.com/p/sonnet-55-is-worth-a-try)) ([Hacker News — Ask HN, 2026-01-20](https://news.ycombinator.com/item?id=46691243))
- **How it works:** User answers 8 quick, humorous scenario questions ('The agent fixed the bug in 3 minutes. You feel...'). They get a profile such as 'Reluctant Supervisor' or 'Drudgery Liberated' plus a short reflective blurb and a matching meme card.
- **Build:** Static quiz in React with a scoring matrix and share image generator. Hardest part: writing sharp, funny, recognizable questions and profiles.
- **Demo moment:** The profile reveal card, with a relatable caption like 'You supervise 4 agents and miss writing loops'.
- **Post hook:** AI coding agents: relief or grief? I made a quiz to find out which one you are. I got 'Reluctant Supervisor.'
- **Risks:** Narrow audience if too developer-centric; frame for any AI-assisted work.

### Feed Dial

**A browser extension that adds a slider to your feed to dim posts that read as generic AI filler.**

*1-2 weeks · fun 4 · useful 4 · ease 3 · shareable 5 · sparked by people asked for it · needs pass*

- **For:** People who scroll LinkedIn, X, Reddit and Substack and are tired of slop
- **Why now:** There are direct requests for a cross-platform extension that flags AI content, and for user-configured feeds instead of algorithmic ones. ([The Algorithmic Bridge, 2026-05-13](https://www.thealgorithmicbridge.com/p/how-this-small-startup-achieved-a)) ([Bluesky, 2026-06-17](https://bsky.app/profile/gergely.pragmaticengineer.com/post/3mohzeauhjk22)) ([Hacker News — Ask HN, 2026-04-25](https://news.ycombinator.com/item?id=47902507)) ([Ben's Bites, 2026-11-03](https://www.bensbites.com/p/if-you-feel-behind-right-now-dont)) ([Don't Worry About the Vase, 2026-11-05](https://thezvi.substack.com/p/ai-193-progress-may-dramatically)) ([Don't Worry About the Vase, 2026-10-29](https://thezvi.substack.com/p/ai-192-anthropic-is-going-public))
- **How it works:** User installs the extension and sets a 'slop tolerance' slider. Posts matching tells get blurred with a 'peek' button and a reason chip. Stats at the week's end show how much of your feed was dimmed.
- **Build:** Chrome extension (Manifest V3) with content scripts, a heuristic scorer first, optional LLM call for ambiguous posts. Hardest part: site DOM selectors that change often; start with only LinkedIn.
- **Demo moment:** Slide the dial up and a LinkedIn feed visibly blurs out half of its posts live.
- **Post hook:** I gave my LinkedIn feed a slop dial. Here's what % of my feed disappeared.
- **Risks:** Brittle selectors, accuracy concerns, API cost per post; use local heuristics by default.

### Menu Pics

**Snap a restaurant menu and see picture cards for every dish as a swipeable gallery.**

*1-2 weeks · fun 4 · useful 4 · ease 4 · shareable 4 · sparked by something someone built · makers pass*

- **For:** Travellers and diners facing menus in unfamiliar cuisines or languages
- **Why now:** A developer vibe-coded a menu food-picture tool, but Karpathy noted Gemini and ChatGPT do it with one prompt. The packaging, a fast mobile flow with a shareable result, would have to be the point. ([Don't Worry About the Vase, 2026-05-07](https://thezvi.substack.com/p/ai-167-the-prior-restraint-era-begins))
- **How it works:** Take a menu photo. The app extracts dishes, translates them and generates or fetches images. Swipe through cards, mark favourites, and share the shortlist with the table.
- **Build:** Mobile-friendly web app with a vision LLM and image generation or search. Hardest part is image accuracy and speed; show placeholders while loading.
- **Demo moment:** Photograph a Japanese menu and watch dish cards pop in with photos and a 'vegetarian?' tag.
- **Post hook:** Never order blind again: menu photo in, food photos out.
- **Risks:** Big chatbots do this already; differentiation depends on the UX and group-sharing feature.

### NPC Dinner Party

**A mobile-friendly mini-game where you host a dinner for AI characters with secret agendas and try to keep everyone happy.**

*1-2 weeks · fun 5 · useful 2 · ease 3 · shareable 5 · sparked by a new AI capability · needs pass*

- **For:** Casual gamers and anyone who likes social deduction and roleplay
- **Why now:** Intelligent NPCs with lightweight state machines plus occasional model calls make worlds compelling, and playful roleplay is popular. ([Latent Space, 2026-09-21](https://latent.space/p/jev/)) ([AINews (smol.ai), 2026-10-08](https://latent.space/p/ainews-not-much-happened-today-60f/)) ([Simon Willison's Weblog, 2026-10-28](https://simonwillison.net/2026/Oct/28/vibe-game-development/))
- **How it works:** Each round the user picks a conversation topic or seating change. Five characters with hidden moods and goals react via a small state machine, with an LLM writing only the dialogue. After three rounds a reveal shows who wanted what and a score.
- **Build:** Next.js with a JSON state machine for moods and LLM calls for lines; shareable result card. Hardest part: balancing so the game is winnable and keeping API cost low with short prompts.
- **Demo moment:** The final reveal: each guest's secret goal flips on screen with a funny quote about your hosting.
- **Post hook:** I made an AI dinner party where every guest has a secret. I lost in round 2.
- **Risks:** Content-safety handling for roleplay; API cost per play.

### Sketch2App Pocket

**Snap a photo of a napkin sketch or notebook page and get a clickable mobile web prototype with a shareable link.**

*1-2 weeks · fun 4 · useful 4 · ease 3 · shareable 5 · sparked by a new AI capability · powers pass*

- **For:** PMs, founders, teachers and hobbyists who sketch ideas on paper but can't code
- **Why now:** Vision models can now read handwriting and sketches well enough that a student's design notebook became a live app, and non-engineers want that shortcut. ([Latent Space, 2026-11-08](https://latent.space/p/cs146s/)) ([Don't Worry About the Vase, 2026-09-26](https://thezvi.substack.com/p/claude-opus-55-should-raise-your))
- **How it works:** User uploads a photo of a sketch or handwritten notes. The app asks 2-3 clarifying questions, then generates a single-file HTML prototype and shows it in a phone frame. One tap gives a shareable link.
- **Build:** Next.js or plain HTML page, vision-capable LLM API to return one HTML file, rendered in a sandboxed iframe, hosted on Netlify. Hardest part is getting reliable, consistent output from messy handwriting and keeping prototypes inside the iframe sandbox.
- **Demo moment:** Hold up a paper sketch to the camera and 20 seconds later tap through the working version on a phone.
- **Post hook:** I drew an app on a napkin and it was clickable 20 seconds later.
- **Risks:** General tools like Claude artifacts already take screenshots; the value is the sketch-first, phone-frame, shareable packaging.

### Three Takes

**Describe a page, flyer or landing page once and get three genuinely different designs to compare, then merge the best parts.**

*1-2 weeks · fun 4 · useful 4 · ease 3 · shareable 5 · sparked by a hack people use · hacks pass*

- **For:** Small business owners, side-project makers and consultants who need a presentable page without design skills.
- **Why now:** Builders force agents to produce three variants and screenshot them because one pass is never good enough. Merging picked parts is the same trick design skills use. ([Ben's Bites, 2026-08-28](https://www.bensbites.com/p/how-i-built-this-21f)) ([Latent Space, 2026-07-28](https://latent.space/p/chatgpt-work/)) ([AINews (smol.ai), 2026-01-16](https://news.smol.ai/issues/26-01-16-chatgpt-ads/)) ([Don't Worry About the Vase, 2026-07-20](https://thezvi.substack.com/p/on-kimi-k3-its-capabilities-and-related))
- **How it works:** The user describes the page and picks a vibe. The app generates three divergent HTML designs side by side. The user ticks parts they like (hero from A, colors from C) and a merge pass produces the final version for download.
- **Build:** Web app where an LLM returns self-contained HTML rendered in iframes. Hardest part is making the three variants truly different rather than recolors.
- **Demo moment:** Three wildly different pages appear side by side, two clicks merge them into a fourth that looks better than all three.
- **Post hook:** AI designs look generic because you only ask once. Ask three times and merge.
- **Risks:** Output quality varies; the rendering needs sandboxing.

### Borges Room

**Pick a classic short story or poem and walk through a 3D interpretation generated just for it.**

*1-2 weeks · fun 5 · useful 3 · ease 3 · shareable 4 · sparked by a cultural moment · powers pass*

- **For:** Book lovers, students and teachers
- **Why now:** Frontier models can now create creative 3D interpretations of literary texts, and interactive game-like explainers get strong engagement. ([Bluesky, 2026-10-18](https://bsky.app/profile/emollick.bsky.social/post/3my4wwt7wdk2t)) ([Bluesky, 2026-10-14](https://bsky.app/profile/emollick.bsky.social/post/3mxsfdbntvs2o)) ([Simon Willison's Weblog, 2026-09-28](https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/))
- **How it works:** User picks from public-domain stories or pastes a short passage. The LLM generates a three.js scene with lighting, objects and a short on-screen caption. User explores with arrow keys and shares a link.
- **Build:** Static page with LLM generating three.js code, sandboxed iframe, a curated public-domain library. Hardest part is repair loops when generated code throws errors.
- **Demo moment:** Choose 'The Raven' and wander into a dark chamber with a bust above a door.
- **Post hook:** Literature class, but you can walk around inside the story.
- **Risks:** Quality varies; curate and cache the best scenes.

### Claim Check Sheet

**Paste an AI answer and get a clear checklist of its claims, each with a verdict and a source link you can click.**

*1-2 weeks · fun 3 · useful 5 · ease 3 · shareable 4 · sparked by people asked for it · needs pass*

- **For:** Students, analysts and writers verifying AI-generated research
- **Why now:** Fact checks by models over-hedge on tiny details, and people want extracted facts with source links before trusting output. ([AINews (smol.ai), 2025-12-22](https://news.smol.ai/issues/25-12-22-not-much/)) ([Hamel Husain, 2026-09-18](https://hamel.dev/blog/posts/evals-faq/)) ([Bluesky, 2026-05-24](https://bsky.app/profile/emollick.bsky.social/post/3mmkordl2vs2z)) ([Don't Worry About the Vase, 2026-07-02](https://thezvi.substack.com/p/ai-175-the-fable-continues)) ([Bluesky, 2026-03-06](https://bsky.app/profile/simonwillison.net/post/3mgfrg4gtxc2n)) ([Hacker News — Ask HN, 2026-08-08](https://news.ycombinator.com/item?id=49227024)) ([Hamel Husain, 2026-03-26](https://hamel.dev/blog/posts/revenge/))
- **How it works:** User pastes AI text. The app splits it into atomic claims, searches the web for each, and returns a table of verdict (supported, contradicted, unclear), quote and link. The top three riskiest claims are pinned first.
- **Build:** Web app, LLM for claim extraction, a search API (Brave/Tavily) for evidence, table UI. Hardest part: forcing clear verdicts with exact quotes and not fake links.
- **Demo moment:** A pasted report instantly turns into a red/yellow/green claim table with 2 hallucinated stats exposed.
- **Post hook:** I fact-checked ChatGPT's market report with another AI. Two of eleven stats were made up.
- **Risks:** Search quality limits verdicts; user may over-trust the checker.

### Handwriting to Font in a Minute

**Upload a photo of your handwriting sample and download an installable font of it.**

*3-4 weeks · fun 5 · useful 3 · ease 2 · shareable 5 · sparked by something someone built · makers pass*

- **For:** Creatives, teachers, wedding planners and anyone who wants their own font
- **Why now:** A developer built a Claude Code skill that turns handwriting photos into TTF fonts with a deterministic potrace pipeline. It is a delightful personal artefact, but locked behind a developer tool. ([AINews (smol.ai), 2026-07-24](https://news.smol.ai/issues/26-07-24-opus-5/))
- **How it works:** User prints a template sheet, writes the characters, and uploads a photo. The app segments glyphs, vectorises them and builds a font file. The user previews typing in their own hand and downloads it.
- **Build:** Python backend with potrace and fonttools on a small host, simple upload frontend. Hardest part is robust glyph segmentation from phone photos; use a template with alignment markers.
- **Demo moment:** Type a sentence into a box and it appears in your own handwriting, then install it in Google Docs.
- **Post hook:** I turned my terrible handwriting into a font. It took 60 seconds.
- **Risks:** Segmentation errors and font-licensing edge cases; server processing needed.

### Instruction Diet

**Paste your custom instructions and have an AI flag the lines that are stale, contradictory or hurting results.**

*a weekend · fun 3 · useful 4 · ease 4 · shareable 4 · sparked by a hack people use · hacks pass*

- **For:** Heavy ChatGPT and Claude users with long custom instructions or system prompts.
- **Why now:** Developers now prune their instruction files because newer models do worse when over-constrained by old hand-holding. The same bloat exists in everyday custom instructions. ([Ahead of AI, 2026-09-09](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and)) ([Hacker News — Ask HN, 2025-11-17](https://news.ycombinator.com/item?id=45950934)) ([AINews (smol.ai), 2026-08-24](https://news.smol.ai/issues/26-08-28-not-much/)) ([Don't Worry About the Vase, 2026-02-12](https://thezvi.substack.com/p/ai-155-welcome-to-recursive-self))
- **How it works:** The user pastes their instructions. The app marks each line as keep, trim or cut with a reason, and runs the same test prompt with the old and the slimmed version side by side. The user picks the winner and copies the new version.
- **Build:** Web app with an LLM critic and parallel runs for A/B comparison. Hardest part is a fair comparison that does not just favor the shorter output.
- **Demo moment:** A 900-word instruction block shrinks to 200 words and the answer to the test prompt is better.
- **Post hook:** Your AI instructions are probably making it worse. I tested mine.
- **Risks:** A/B judgments are subjective; niche audience.

### Is It Circular?

**An interactive map where you click AI companies and see the money loops between chipmakers, clouds and labs, explained in plain English.**

*1-2 weeks · fun 4 · useful 3 · ease 3 · shareable 5 · sparked by a cultural moment · needs pass*

- **For:** Curious professionals, investors-at-large and LinkedIn readers trying to understand AI deal fragility
- **Why now:** Circular financing and heavy leverage are a hot argument but hard to read; a visual explainer makes it graspable. ([Bluesky, 2026-11-12](https://bsky.app/profile/edzitron.com/post/3n24x2quc5c2v)) ([Marcus on AI, 2026-07-27](https://garymarcus.substack.com/p/circular-financing-aint-what-it-used)) ([Tomasz Tunguz, 2026-09-04](https://tomtunguz.com/the-4-trillion-dollar-ai-data-center-debt-wave/)) ([The Algorithmic Bridge, 2026-05-29](https://www.thealgorithmicbridge.com/p/the-charts-the-ai-industry-doesnt))
- **How it works:** User sees a node graph of companies with arrows labeled by deal type and amount. Clicking a loop plays a 20-second animated 'follow the dollar' story and cites the source. A 'circularity meter' totals the loop sizes.
- **Build:** React with D3 or react-force-graph and a hand-curated JSON of deals with citations. Hardest part: data accuracy and avoiding financial-advice framing; cite everything and label it educational.
- **Demo moment:** Press 'follow the dollar' and watch a coin travel in a loop from the chipmaker to the lab and back.
- **Post hook:** Where does the money in AI actually go? I mapped the loops. It's a circle.
- **Risks:** Factual errors damage credibility; deals change fast; not financial advice.

### Old Models Time Machine

**Type one prompt and see how it would have looked across a decade of image AI, from DeepDream to today.**

*1-2 weeks · fun 4 · useful 3 · ease 3 · shareable 5 · sparked by a cultural moment · powers pass*

- **For:** General public curious about how fast AI progressed, and LinkedIn audiences
- **Why now:** The Old Models Foundation shows that historic image models are a fascinating comparison, and a side-by-side timeline makes AI progress tangible. ([Import AI, 2026-09-28](https://importai.substack.com/p/import-ai-474-platonic-mindspace)) ([Bluesky, 2026-10-20](https://bsky.app/profile/emollick.bsky.social/post/3mydlag277k2c)) ([Bluesky, 2026-10-23](https://bsky.app/profile/antirez.bsky.social/post/3myjth3kl5m2o))
- **How it works:** User enters a prompt and sees a timeline slider of outputs from successive years. Dragging the slider morphs between eras. A share image shows the 2015 and 2026 versions side by side.
- **Build:** Static site with pre-generated sample galleries for common prompts, plus a live call to a current image API for the modern end. Hardest part is sourcing authentic old-model outputs; use a style-emulation approach and label it honestly.
- **Demo moment:** Drag the slider and the otter on a plane goes from swirly nightmare to photoreal.
- **Post hook:** The same prompt, ten years of AI image progress.
- **Risks:** Authenticity of old-style outputs; label clearly as emulations.

### One Post, Five Places

**Paste a draft once and get platform-ready versions for LinkedIn, X, newsletter and blog, each in your voice.**

*1-2 weeks · fun 3 · useful 4 · ease 4 · shareable 4 · sparked by something someone built · hacks pass*

- **For:** Creators and professionals who post the same idea across several channels.
- **Why now:** Bloggers vibe-code extensions and script chains for crossposting, formatting and link-fixing because no tool handles it. The workflow is clear and repeatable. ([Don't Worry About the Vase, 2025-11-17](https://thezvi.substack.com/p/on-writing-2)) ([Bluesky, 2025-11-19](https://bsky.app/profile/simonwillison.net/post/3m5zb43m4mc23)) ([Hacker News — Ask HN, 2026-03-19](https://news.ycombinator.com/item?id=47436526)) ([Ben's Bites, 2026-03-24](https://www.bensbites.com/p/agents-should-interview-you))
- **How it works:** The user pastes a draft and optionally a voice guide. The app produces a LinkedIn post, an X thread, a newsletter version with table of contents and a blog version. Each has editable previews and copy buttons, and a character counter for X.
- **Build:** Web app with an LLM and per-platform templates, plus an optional Chrome extension for pulling text from the page. Hardest part is making each version genuinely native, not just truncated.
- **Demo moment:** One paragraph becomes five formatted posts side by side, and the X thread breaks at natural points.
- **Post hook:** I write once and publish five times. Here's the tool that does the reformatting.
- **Risks:** Platform formatting rules change; multi-format generators are common.

### Plain-Picture Explainer

**Paste anything dense and get a one-screen interactive diagram or animation explaining it in plain English.**

*1-2 weeks · fun 3 · useful 4 · ease 4 · shareable 4 · sparked by a hack people use · powers pass*

- **For:** Professionals who read contracts, reports and technical memos
- **Why now:** People ask LLMs for HTML, diagrams, plain English and explainer videos to understand outputs, and tools that generate custom visuals on demand are rising. ([Ben's Bites, 2026-10-06](https://www.bensbites.com/p/thoughts-from-san-francisco)) ([Ben's Bites, 2026-10-29](https://www.bensbites.com/p/ai-is-overwhelming-and-im-doing-it)) ([Bluesky, 2026-10-15](https://bsky.app/profile/hardmaru.bsky.social/post/3mxwc4blhr22t))
- **How it works:** User pastes text or a PDF page. The LLM chooses a visual form such as flow, timeline or comparison and generates a self-contained interactive HTML explainer. User can click nodes to expand details.
- **Build:** Single page with LLM generating HTML/SVG, sandboxed preview. Hardest part is reliably choosing the right visual type and avoiding misleading simplifications.
- **Demo moment:** A dense policy paragraph becomes a clickable flowchart in seconds.
- **Post hook:** I stopped reading walls of text. I read pictures instead.
- **Risks:** Chat tools can do HTML artifacts; the differentiator is fixed visual templates and one-click share. Do not present as legal advice.

### Source Material Dungeon

**Drop in any document, such as your employee handbook, and an AI game master builds a text adventure from it.**

*1-2 weeks · fun 5 · useful 3 · ease 3 · shareable 4 · sparked by people asked for it · powers pass*

- **For:** Gamers, teachers and trainers
- **Why now:** People asked for a game master agent that builds a campaign from supplied source material, and vibe-coded games are now genuinely fun. ([Hacker News — Ask HN, 2026-10-20](https://news.ycombinator.com/item?id=50159886)) ([Ben's Bites, 2026-10-29](https://www.bensbites.com/p/ai-is-overwhelming-and-im-doing-it)) ([Don't Worry About the Vase, 2026-09-26](https://thezvi.substack.com/p/claude-opus-55-should-raise-your))
- **How it works:** User pastes text or a URL. The LLM extracts characters, locations and rules and starts a campaign with choices. A small state panel tracks inventory and health, and the end screen is a shareable recap card.
- **Build:** Web chat UI with an LLM and structured JSON state per turn, plus optional image per scene. Hardest part is keeping state consistent and stories finishing within about 15 turns.
- **Demo moment:** Paste a quarterly earnings memo and be attacked by The Dreaded Deferred Revenue.
- **Post hook:** I turned our compliance training into a dungeon crawl.
- **Risks:** Long-context drift; limit campaign length.

### Which Plan Do I Actually Need?

**Describe your AI habits in plain English and get a plain-language comparison of which chatbot plan fits, including the limit traps.**

*1-2 weeks · fun 3 · useful 4 · ease 4 · shareable 4 · sparked by a common frustration · needs pass*

- **For:** Professionals confused by ChatGPT, Claude and Gemini tier names and usage caps
- **Why now:** Plan names map poorly across vendors and usage limits are poorly documented, so people burn through caps or overpay. ([Simon Willison's Weblog, 2026-01-16](https://simonwillison.net/2026/Jan/16/chatgpt-ads/)) ([One Useful Thing, 2026-07-23](https://www.oneusefulthing.org/p/an-opinionated-guide-to-which-ai-b22)) ([AINews (smol.ai), 2026-05-04](https://news.smol.ai/issues/26-05-20-not-much/)) ([Don't Worry About the Vase, 2026-10-01](https://thezvi.substack.com/p/ai-188-gemini-dot-argon))
- **How it works:** User answers 5 quick questions (how many long chats a day, files, agents, images). The app maps the answers to a hand-curated plan table and shows a verdict, a 'you'll hit the cap by Wednesday' warning, and a cheaper alternative.
- **Build:** Static JSON of plans maintained by hand, simple React quiz, an LLM only for the explanation text. Hardest part: keeping plan data current; show a 'last verified' date and a community-correction link.
- **Demo moment:** Answer 5 questions and see a shockingly specific 'You'll run out of Claude Pro on day 3' result.
- **Post hook:** AI plan names are a mess. I built a 60-second quiz that tells you what to actually pay for.
- **Risks:** Plan data goes stale quickly; need a visible freshness stamp.

### Will My Job Survive? Argument Mixer

**Pick your job tasks and an economic 'worldview' (Jevons optimist, structural displacement, macro-only), and see three different futures for the same role.**

*1-2 weeks · fun 3 · useful 4 · ease 4 · shareable 4 · sparked by a cultural moment · culture pass*

- **For:** Everyday professionals anxious about AI and jobs who are tired of one-sided takes.
- **Why now:** The jobs debate is unresolved and the camps disagree on mechanism, not just outcome. Showing the same job under each worldview reveals the assumptions. ([Hacker News — Ask HN, 2026-10-09](https://news.ycombinator.com/item?id=50020096)) ([Don't Worry About the Vase, 2026-10-01](https://thezvi.substack.com/p/ai-188-gemini-dot-argon)) ([Bluesky, 2026-02-11](https://bsky.app/profile/bcmerchant.bsky.social/post/3mem2m5gotk26)) ([The Algorithmic Bridge, 2026-11-05](https://www.thealgorithmicbridge.com/p/the-ai-industry-thinks-it-has-a-pr))
- **How it works:** User enters their role and ticks 6-8 typical tasks. They toggle between worldview 'lenses' and an AI writes a short, plainly-labeled scenario narrative per lens. A summary card shows what you would need to believe for each.
- **Build:** Next.js with LLM API, structured prompts per worldview, share card. Hardest part: keeping outputs clearly framed as scenarios rather than predictions.
- **Demo moment:** Flipping the lens toggle and the same job's future flips from 'role expands' to 'role vanishes'.
- **Post hook:** Three smart camps, one job, three totally different futures. I built a tool that shows what you'd have to believe for each.
- **Risks:** Anxiety-inducing outputs; add a disclaimer and a 'what you can do' section. Not career advice.

### Make Me a Mini Tool

**A search-or-build page for tiny single-purpose utilities, such as a GeoJSON viewer, a token counter or a photo renamer, built on demand and saved to a shelf.**

*3-4 weeks · fun 4 · useful 5 · ease 2 · shareable 4 · sparked by a hack people use · makers pass*

- **For:** Non-technical professionals who face small one-off chores that no app quite fits
- **Why now:** Simon builds quick tools when finding an existing one is slower, such as a GeoJSON-to-PNG renderer, plus token counters and log renderers. Non-developers have these chores too but lack the habit. ([Bluesky, 2026-08-31](https://bsky.app/profile/simonwillison.net#week-2026-W36)) ([Simon Willison's Weblog, 2026-05-28](https://simonwillison.net/2026/May/28/claude-opus-4-8/)) ([Simon Willison's Weblog, 2026-06-30](https://simonwillison.net/2026/Jun/30/claude-sonnet-5/))
- **How it works:** User describes the chore, for example 'rename these files by date'. The app generates a self-contained in-browser tool that runs locally on their files. They can save it to a personal shelf or share a link.
- **Build:** Web app with an LLM generating single-file HTML tools in a sandboxed iframe with no network access. Hardest part is making the tools work reliably on first try; add auto-test and retry.
- **Demo moment:** Describe a chore, drag in a folder of files, and watch the tool do it in seconds.
- **Post hook:** I never download random utilities anymore. I just ask for the exact tool.
- **Risks:** Overlaps with chatbot artifacts; value rests on the shelf and local-only safety.

### Notes to Wiki

**Drop in a messy pile of notes and get a linked, Obsidian-ready personal wiki back as a zip.**

*1-2 weeks · fun 4 · useful 4 · ease 3 · shareable 4 · sparked by a hack people use · hacks pass*

- **For:** Knowledge workers who hoard notes and want a second brain without setting it up.
- **Why now:** Karpathy-style LLM wikis and personal knowledge bases built by agents are trending, but each takes technical setup. Packaging the transformation makes it accessible. ([Ben's Bites, 2026-04-14](https://www.bensbites.com/p/big-lab-leaks)) ([Hacker News — Ask HN, 2026-05-16](https://news.ycombinator.com/item?id=48160604)) ([Bluesky, 2026-09-03](https://bsky.app/profile/emollick.bsky.social/post/3munds3sxrc2n)) ([AINews (smol.ai), 2026-04-13](https://news.smol.ai/issues/26-04-13-not-much/))
- **How it works:** The user uploads text or markdown files, or pastes notes. The app groups them into topics, writes linked pages with summaries and backlinks, and builds an index. The result downloads as a zip of markdown files to open in Obsidian.
- **Build:** Web app with chunked LLM processing and in-browser zip creation. Hardest part is cost and consistency across many files, so cap input to about 50 notes.
- **Demo moment:** A chaotic folder of 40 notes becomes a graph view of linked pages in Obsidian.
- **Post hook:** I turned 5 years of messy notes into a linked wiki in 4 minutes.
- **Risks:** Privacy of personal notes; hallucinated links or merged facts.

### Page Feedback Block

**Click anywhere on any web page or draft to leave comments, then copy them all as one clean block to paste into an AI chat.**

*a weekend · fun 2 · useful 4 · ease 5 · shareable 3 · sparked by a common frustration · makers pass*

- **For:** Anyone iterating on AI-generated pages, docs or designs
- **Why now:** Ben built a tool to comment on and delete copy while building, then copy all feedback in one block. Iterating with AI by typing scattered feedback is a common frustration. ([Ben's Bites, 2026-06-04](https://www.bensbites.com/p/build-tools-to-build-more))
- **How it works:** Paste or load a draft and click on text to attach comments or strike it. A panel gathers them into a structured instruction. One click copies it to the clipboard for any chatbot.
- **Build:** Browser extension or single-page app with text selection and annotation. Hardest part is anchoring comments to selections robustly.
- **Demo moment:** Click four sentences, type quick notes, press Copy, and paste a perfectly structured revision brief.
- **Post hook:** The best prompt is a pile of sticky notes. So I built that.
- **Risks:** Small, simple concept that may feel narrow.

### Procedural Painter

**Describe a painting and watch code paint it stroke by stroke on a canvas, with a replay you can export as a video.**

*1-2 weeks · fun 4 · useful 2 · ease 3 · shareable 5 · sparked by a hack people use · powers pass*

- **For:** Art-curious people and anyone tired of samey AI image looks
- **Why now:** Generative art built as programs driving a paint engine, not image models, is a distinct aesthetic, and animated stroke replays are inherently watchable. ([AINews (smol.ai), 2026-11-10](https://latent.space/p/ainews-fable-5-2-retakes-world-1-llm-spot-as-ant-ipo-roadshow-begins/)) ([Simon Willison's Weblog, 2026-10-20](https://simonwillison.net/2026/Oct/20/battledrones/))
- **How it works:** User types a mood or scene. The LLM writes a small p5.js or canvas program using brush strokes and palettes, and it runs live as a painting-in-progress. User exports an MP4 or GIF timelapse.
- **Build:** p5.js, LLM generating the program, MediaRecorder for canvas capture. Hardest part is prompting for painterly quality and avoiding clip-art outputs.
- **Demo moment:** A sunset gets painted stroke by stroke in a 20-second timelapse.
- **Post hook:** No image model here: the AI wrote code that paints.
- **Risks:** Output may look primitive; curate styles such as impressionist dots.

### Voice Library Audiobook

**Turn any article or your own writing into a short audiobook read in your own cloned voice or a family member's.**

*1-2 weeks · fun 4 · useful 4 · ease 3 · shareable 4 · sparked by a new AI capability · powers pass*

- **For:** Parents, writers, and anyone with a long reading list
- **Why now:** Locally run voice cloning has been used to produce custom audiobooks, and cloning can be chained onto existing TTS cheaply. ([Hacker News — Ask HN, 2026-10-05](https://news.ycombinator.com/item?id=49972125)) ([AINews (smol.ai), 2026-10-31](https://latent.space/p/ainews-google-admits-ai-mode-hurts-search-revenue-15-500b-drop-worst-since-2004-ipo-ai-bear-market-c/)) ([Ben's Bites, 2026-09-24](https://www.bensbites.com/p/back-to-claude))
- **How it works:** User records 30 seconds of a voice sample with consent, pastes text, and chooses delivery styles. The app produces an MP3 and a podcast-style RSS link.
- **Build:** Web app with a hosted voice cloning TTS API, text chunking, and audio stitching. Hardest part is consent and abuse prevention for voice cloning, plus chunk consistency.
- **Demo moment:** Paste a bedtime story and hear it read in grandma's recorded voice.
- **Post hook:** I made my own articles into audiobooks narrated by me.
- **Risks:** Voice cloning misuse; require a live read-aloud verification phrase.

### Commodity or Castle? Moat Builder

**A tiny strategy game where you run an AI lab and choose between racing on model quality, price cuts, or moving up the stack, while rivals commoditize you.**

*3-4 weeks · fun 5 · useful 3 · ease 2 · shareable 4 · sparked by a cultural moment · culture pass*

- **For:** MBAs, product people and business-curious readers who like case-study games.
- **Why now:** The commoditization debate is a classic strategy question (moat vs commodity trap) with live market evidence. A game lets players feel the margin squeeze. ([Latent Space, 2026-10-22](https://latent.space/p/modal-d/)) ([Tomasz Tunguz, 2026-09-23](https://tomtunguz.com/the-most-important-market-in-ai-is-the-middle/)) ([AI as Normal Technology, 2026-07-09](https://www.normaltech.ai/p/up-the-stack-how-ais-escape-from)) ([Marcus on AI, 2026-09-09](https://garymarcus.substack.com/p/the-case-for-boycotting-generative))
- **How it works:** Over 8 quarterly turns, players pick actions (train a bigger model, cut price, launch a product, sign enterprise deals). Rival labs respond and margins/market share update. The end screen assigns a strategy archetype and a shareable scorecard.
- **Build:** React with a small rules engine, no backend; optional LLM for quarterly news flavor text. Hardest part: balancing the game so that multiple strategies are viable.
- **Demo moment:** A quarter where you cut price 80% and the market-share bar leaps while the margin bar collapses.
- **Post hook:** I built a game where you run an AI lab. 9 of 10 friends went bankrupt trying to race on price. Can you build a moat?
- **Risks:** Game balancing takes iteration; keep scope to 8 turns and 4 actions.

### Human Receipt

**A writing tool that records your drafting process and produces a verifiable 'written by a human' receipt page.**

*1-2 weeks · fun 3 · useful 4 · ease 3 · shareable 4 · sparked by a common frustration · needs pass*

- **For:** Independent writers, students and Substack authors who need to prove their work is their own
- **Why now:** Writers have trouble proving authorship, and detectors alone are unreliable. Process evidence (typing timeline, revisions) is a more convincing artifact. ([The Algorithmic Bridge, 2026-08-12](https://www.thealgorithmicbridge.com/p/on-substack-pangram-partnership-its)) ([Hacker News — Ask HN, 2026-10-27](https://news.ycombinator.com/item?id=50265376)) ([Bluesky, 2026-06-17](https://bsky.app/profile/gergely.pragmaticengineer.com/post/3mohzeauhjk22))
- **How it works:** User writes in a distraction-free editor that logs revision history and paste events. When finished, it generates a public receipt link showing a timeline, % typed vs pasted, and an optional AI-assistance disclosure.
- **Build:** React editor (TipTap) plus Supabase for event logs and a read-only share page. Hardest part: making the receipt credible without overclaiming; show the data, don't claim proof.
- **Demo moment:** A time-lapse replay of an essay being written, appearing on a receipt page with a QR code.
- **Post hook:** Nobody believes you wrote it yourself anymore. So I made a receipt.
- **Risks:** Can be gamed by retyping AI text; privacy of the draft history.

### Penny Router

**Type any task and see which AI model and effort level it deserves, then run it there and see what you saved.**

*1-2 weeks · fun 3 · useful 4 · ease 3 · shareable 4 · sparked by a hack people use · hacks pass*

- **For:** Professionals who pay for AI subscriptions or APIs and burn through limits on easy tasks.
- **Why now:** Power users manually route work between cheap and strong models and tune thinking levels per task to stay inside limits. Nobody has packaged that judgment for non-engineers. ([Hacker News — Ask HN, 2026-03-29](https://news.ycombinator.com/item?id=47559293)) ([AINews (smol.ai), 2026-07-08](https://news.smol.ai/issues/26-07-08-grok-45/)) ([Ben's Bites, 2026-07-14](https://www.bensbites.com/p/how-to-use-gpt-56)) ([Latent Space, 2026-09-05](https://latent.space/p/grok-bot/))
- **How it works:** The user pastes a task. A small cheap model rates difficulty, stakes and needed reasoning. The app picks a tier (fast, balanced or deep), runs it, and shows a receipt such as 'Used the cheap model, saved about 80% versus always using the top model'. A override button reruns on the strong model.
- **Build:** Next.js or single-page app calling the OpenRouter API with 3 model tiers and a classifier prompt. Hardest part is making the difficulty classifier feel trustworthy and the cost math accurate.
- **Demo moment:** Three tasks go in: a typo fix, a market analysis and a trivia question. Each is routed differently and a running 'saved $' counter ticks up.
- **Post hook:** I stopped using the biggest AI model for everything. Here's the 30-second router I built and what it saved me.
- **Risks:** Misrouting hard tasks to weak models; model names and prices change often.

### Search Without the Summary

**A browser extension that hides AI Overviews on search pages and shows a ticker of how many publisher clicks that summary likely cost.**

*1-2 weeks · fun 3 · useful 4 · ease 3 · shareable 4 · sparked by a common frustration · culture pass*

- **For:** People annoyed by AI summaries and bloggers or readers who care about publishers.
- **Why now:** AI Overviews cut publisher traffic and sometimes make false claims, while the web fills with SEO slop. Users want control and a playful way to see the effect. ([Bluesky, 2025-11-17](https://bsky.app/profile/caseynewton.bsky.social/post/3m5tnb4enwc2g)) ([AINews (smol.ai), 2026-10-31](https://latent.space/p/ainews-google-admits-ai-mode-hurts-search-revenue-15-500b-drop-worst-since-2004-ipo-ai-bear-market-c/)) ([Don't Worry About the Vase, 2026-06-11](https://thezvi.substack.com/p/ai-172-the-first-fable)) ([Hacker News — Ask HN, 2026-05-22](https://news.ycombinator.com/item?id=48235223))
- **How it works:** The extension collapses the AI summary box by default, replaces it with a 'Summary hidden, 7 sources below' banner, and keeps a tally of summaries dodged. Users can click to reveal and a weekly 'clicks returned to publishers' card is shareable.
- **Build:** Chrome extension (Manifest V3) with a content script and CSS selectors, local storage for counts. Hardest part: selectors breaking when Google changes markup.
- **Demo moment:** Searching a question and watching the AI box fold away, with the counter incrementing.
- **Post hook:** I hid Google's AI summaries for a week and sent 143 clicks back to real publishers. Here's the extension.
- **Risks:** Selector fragility; the 'clicks returned' number is an estimate and must be labeled so.

### Soundtrack by Code

**Open a web page or doc and get a live-generated ambient soundtrack that reacts to what you do, from calm typing to rushed deadlines.**

*1-2 weeks · fun 4 · useful 3 · ease 3 · shareable 4 · sparked by a hack people use · powers pass*

- **For:** Remote workers, students, game fans
- **Why now:** Soundtracks generated through code instead of audio files, intensifying with action, show music can be adaptive and free. ([Simon Willison's Weblog, 2026-10-20](https://simonwillison.net/2026/Oct/20/battledrones/)) ([Don't Worry About the Vase, 2026-09-26](https://thezvi.substack.com/p/claude-opus-55-should-raise-your))
- **How it works:** User picks a vibe and the page runs a Web Audio synthesizer whose tempo and layers shift with typing speed or a timer. A slider shows the system adding layers as intensity rises.
- **Build:** Web Audio API or Tone.js with an LLM that writes the generator code per vibe. Hardest part is making it sound pleasant rather than noisy.
- **Demo moment:** Type faster and watch drums and bass layers kick in.
- **Post hook:** My focus music reacts to how fast I type.
- **Risks:** Music quality is subjective; offer 3-4 polished presets.

### Parent Playlist Rescue

**A guided checker and migrator that helps parents lock down kid-unfriendly features and move playlists between music services.**

*1-2 weeks · fun 2 · useful 4 · ease 4 · shareable 3 · sparked by a common frustration · makers pass*

- **For:** Parents of young kids using streaming apps
- **Why now:** Parents disable Spotify's video feature or transfer playlists with scripts and cheap tools. The hack exists, but only as scattered tips and vibe-coded scripts. ([Don't Worry About the Vase, 2026-07-08](https://thezvi.substack.com/p/childhood-and-education-20-phones))
- **How it works:** Parent picks a service and sees a step-by-step settings checklist with screenshots. Optionally they paste a playlist link and the app builds a matching list for another service. A final 'kid-safe' score shows what is still open.
- **Build:** Static guide site with checklist state plus playlist-matching via public APIs. Hardest part is API approvals, so make the checklist the core and the migration optional via CSV exports.
- **Demo moment:** A progress ring fills as each setting is toggled, ending with a green 'ready for the back seat' badge.
- **Post hook:** One tiny setting changed what my kid sees on Spotify. I made a checklist for the rest.
- **Risks:** Settings change often; API restrictions from streaming services.

### Personal Canvas

**A drag-and-drop home page of widgets, such as todos, bookmarks and notes, that you describe in plain English.**

*3-4 weeks · fun 4 · useful 4 · ease 2 · shareable 4 · sparked by something someone built · makers pass*

- **For:** Professionals who want a custom dashboard without a Notion rabbit hole
- **Why now:** Ben Tossell built a visual all-in-one dashboard and a personal canvas of widgets, and users build custom TV launchers. People want personal software shaped to them but not the code. ([Ben's Bites, 2026-10-20](https://www.bensbites.com/p/how-i-built-my-everything-app)) ([Ben's Bites, 2026-07-30](https://www.bensbites.com/p/1-billion-chatgpt-users)) ([AINews (smol.ai), 2026-10-23](https://latent.space/p/ainews-black-october/))
- **How it works:** User types 'add a widget that shows my top 3 priorities and a countdown to launch'. The AI generates the widget on a canvas that they can drag around. Data is stored locally and the layout is shareable as a template.
- **Build:** React with a widget sandbox iframe, LLM generating widget HTML and localStorage. Hardest part is safe sandboxing and stable widget editing.
- **Demo moment:** Describe a widget in a sentence and it appears on the canvas, working, in 5 seconds.
- **Post hook:** I stopped searching for the right dashboard app and just describe widgets.
- **Risks:** Widget quality varies; competes with Notion and similar tools.

### Pocket Arena

**Two phones in the same room battle in a mini browser game with no accounts, joined by a code or a sound.**

*3-4 weeks · fun 5 · useful 2 · ease 2 · shareable 4 · sparked by something someone built · makers pass*

- **For:** Friends, families and classrooms who want instant local multiplayer
- **Why now:** Makers built browser RTS games with device-to-device multiplayer over an audio link and use WebSocket relays for multiplayer. Nobody has packaged zero-setup party games for non-developers. ([Bluesky, 2026-10-20](https://bsky.app/profile/simonwillison.net/post/3mydffvspjs2x)) ([Simon Willison's Weblog, 2026-10-28](https://simonwillison.net/2026/Oct/28/vibe-game-development/)) ([Simon Willison's Weblog, 2026-10-28](https://simonwillison.net/2026/Oct/28/vibe-game-development/))
- **How it works:** Host picks a game template such as tug of war, reaction duel or word race. Friends join by scanning a QR code. The AI customises the theme, such as 'office edition', and the game starts.
- **Build:** Static site plus a small WebSocket relay on Cloudflare Workers; LLM only for themes and content. Hardest part is real-time sync, so keep the games turn-based or tap-based.
- **Demo moment:** Scan a QR code on a second phone and both screens instantly turn into a head-to-head duel.
- **Post hook:** I vibe-coded a multiplayer party game in an afternoon. Here is how the relay works.
- **Risks:** Real-time networking bugs; scope creep into too many games.

### Weekend Dataset Maker

**Describe a niche collection you wish existed, and the app builds a browsable, shareable dataset page from public sources.**

*3-4 weeks · fun 4 · useful 4 · ease 2 · shareable 4 · sparked by something someone built · makers pass*

- **For:** Journalists, analysts, hobbyists and consultants who want a custom list or map
- **Why now:** Makers built a film-discovery dataset, a map of lighthouses, and a dataset of open LLM mentions across 500K papers in a weekend. Non-coders want these artefacts but not the scripting. ([Bluesky, 2026-09-19](https://bsky.app/profile/mikecaulfield.bsky.social/post/3mvve5ezh522v)) ([Bluesky, 2026-03-09](https://bsky.app/profile/emollick.bsky.social/post/3mgmeeq3tv22x)) ([Bluesky, 2026-08-24](https://bsky.app/profile/natolambert.bsky.social/post/3mttl2tpb4g2g))
- **How it works:** User types a topic like 'every lighthouse you can visit in Maine'. The app searches the web, extracts structured rows, and shows an editable table plus a map or card view. User exports CSV or shares a public page.
- **Build:** Web app using LLM with web search tool, a table UI and Leaflet maps. Hardest part is accuracy and source citations, so show a source link per row and flag low-confidence entries.
- **Demo moment:** Type one sentence and watch rows fill in live with pins appearing on a map.
- **Post hook:** I built a dataset that did not exist, in 5 minutes, from one sentence.
- **Risks:** Hallucinated rows and scraping limits; needs clear sourcing.

### Cap Clock

**A tiny dashboard where you log how fast you burn your AI chat limits and it predicts when you'll hit the wall.**

*1-2 weeks · fun 3 · useful 3 · ease 4 · shareable 3 · sparked by a common frustration · needs pass*

- **For:** Heavy chatbot users on $20 plans who get cut off mid-project
- **Why now:** Users get limits hit after minutes and no vendor shows a clear meter, so people rely on trial and error. ([AINews (smol.ai), 2026-05-04](https://news.smol.ai/issues/26-05-20-not-much/)) ([AINews (smol.ai), 2026-10-31](https://latent.space/p/ainews-google-admits-ai-mode-hurts-search-revenue-15-500b-drop-worst-since-2004-ipo-ai-bear-market-c/)) ([One Useful Thing, 2026-07-23](https://www.oneusefulthing.org/p/an-opinionated-guide-to-which-ai-b22))
- **How it works:** User taps 'I got capped' with the app, plan, and approximate time of day. Over time the app shows patterns ('You cap Gemini after ~25 messages') and suggests a fallback tool for the rest of the day. Anonymous aggregates show community-reported caps by plan.
- **Build:** Mobile-friendly web app, Supabase for logs, simple charts. Hardest part: cold-start data; seed with the user's own logs and make it valuable solo.
- **Demo moment:** A countdown ring that says 'cap in ~42 minutes at your current pace' with a switch-to-backup suggestion.
- **Post hook:** Nobody tells you how fast you're burning your AI limit. So I made a clock.
- **Risks:** Manual logging is a friction; crowdsourced data may be noisy.

### Handoff Slides

**Paste a list of URLs or notes and get a clean full-screen deck that you control from your phone.**

*1-2 weeks · fun 3 · useful 4 · ease 3 · shareable 3 · sparked by something someone built · makers pass*

- **For:** Speakers, teachers and anyone giving quick talks who hates slide tooling
- **Why now:** Simon built a custom presentation app that turns a list of URLs into slides remote-controlled from his phone, and Nathan Lambert built a markdown-native slides tool. A web version for non-developers is missing. ([Bluesky, 2026-02-25](https://bsky.app/profile/simonwillison.net/post/3mfp5dhg24c2r)) ([Bluesky, 2026-10-19](https://bsky.app/profile/natolambert.bsky.social/post/3mya62iykzy2l)) ([Bluesky, 2026-03-20](https://bsky.app/profile/natolambert.bsky.social/post/3mhipiintlc2v))
- **How it works:** User pastes links or markdown. The app builds slides with screenshots and AI-written talking points. A QR code opens a phone remote with notes and next/prev buttons.
- **Build:** Web app with markdown to slides, screenshot API, and a WebSocket remote. Hardest part is reliable URL screenshots and cross-device sync.
- **Demo moment:** Scan the QR code, swipe on your phone, and the laptop deck changes with your notes visible on the phone.
- **Post hook:** I stopped making slides. I paste links and present from my phone.
- **Risks:** Competes with existing deck tools; screenshot rights and quality.

### Offline Pocket Oracle

**A fully in-browser decision helper that weighs your options using a small local model, with nothing leaving your device.**

*1-2 weeks · fun 3 · useful 3 · ease 3 · shareable 4 · sparked by a new AI capability · powers pass*

- **For:** Privacy-minded professionals and anyone facing small daily decisions
- **Why now:** There is demand for fast, cheap in-browser decision models, and local models in the browser are now practical. ([AINews (smol.ai), 2026-11-07](https://latent.space/p/ainews-anthropic-ipo-whither-now/)) ([Ben's Bites, 2026-10-20](https://www.bensbites.com/p/how-i-built-my-everything-app)) ([AINews (smol.ai), 2026-10-28](https://latent.space/p/ainews-anthropic-ends-coding-interviews-hunger-beats-tenure/))
- **How it works:** User types a choice such as two job offers or dinner options and sets what matters. A WebGPU local model scores each option and shows probability bars with a short reasoning line. A 'privacy: nothing sent' badge stays visible.
- **Build:** WebLLM or Transformers.js in a static page with a small model. Hardest part is model download size, load time and getting stable numeric scoring.
- **Demo moment:** Turn on airplane mode and it still ranks your options.
- **Post hook:** An AI decision helper that works in airplane mode.
- **Risks:** Small model quality and WebGPU support vary; frame it as a thinking aid.

### Open vs Closed Race Track

**A little racing game where a closed-model car leads by months and an open-weight car keeps catching up; tweak the 'gap' and watch the race.**

*1-2 weeks · fun 4 · useful 3 · ease 3 · shareable 3 · sparked by a cultural moment · culture pass*

- **For:** Curious non-technical readers who've heard 'open models are six months behind' but don't get why it matters.
- **Why now:** The open-closed gap is a recurring, quantified debate (4-6 months, widening vs converging). A race metaphor makes the stakes tangible. ([Interconnects, 2026-09-11](https://www.interconnects.ai/p/open-source-ai-reading-list)) ([Bluesky, 2026-04-20](https://bsky.app/profile/natolambert.bsky.social/post/3mjxa2tmyac2q)) ([Latent Space, 2026-01-23](https://latent.space/p/captaining-imo-gold-deep-think-on/)) ([Don't Worry About the Vase, 2026-07-03](https://thezvi.substack.com/p/fable-6-the-return-of-the-king))
- **How it works:** User picks 'gap dynamics' (converging, constant, widening) and a price lever. The race animates over several 'model release' laps and a caption explains who wins which task categories. Result card summarizes what that world looks like for users.
- **Build:** HTML canvas or simple CSS animation with JS timers. Hardest part: making the metaphor accurate and not just cute.
- **Demo moment:** The open car draws level at the final lap just as the closed car launches a boost.
- **Post hook:** Is open-source AI catching up or falling behind? I made a race where you set the rules and watch.
- **Risks:** Metaphor may oversimplify; keep captions grounded in the debate.

### Token Price Time Machine

**Type a task and see what it would have cost with frontier AI over the past year as prices dropped, rose, or got quietly changed.**

*1-2 weeks · fun 3 · useful 4 · ease 3 · shareable 3 · sparked by a common frustration · culture pass*

- **For:** Curious professionals and AI-budget owners who can't tell whether AI is getting cheaper or pricier.
- **Why now:** Price cuts, hikes, and plan changes are contested and confusing: cheaper models, 80% cuts, rising frontier prices. A simple timeline makes the confusion legible. ([Tomasz Tunguz, 2026-08-04](https://tomtunguz.com/what-if-gpu-prices-double/)) ([Tomasz Tunguz, 2026-06-07](https://tomtunguz.com/inflation-deflation-ai/)) ([AINews (smol.ai), 2026-09-23](https://latent.space/p/ainews-claude-opus-55-the-new-default/)) ([Hacker News — Ask HN, 2026-02-16](https://news.ycombinator.com/item?id=47034849))
- **How it works:** User picks a typical task ('summarize 50-page PDF', 'draft 100 emails') and sees a timeline of what it costs on a budget vs frontier model with annotated events. A toggle shows the 'if subsidies end' scenario.
- **Build:** React with a hand-curated JSON of model prices and events plus Chart.js. Hardest part: keeping price data accurate and sourced; label as approximate.
- **Demo moment:** Selecting a task and watching two lines diverge as an annotated 80% price cut drops one of them.
- **Post hook:** The same AI task cost $4 last year and 12 cents now. Or did it? Here's the time machine.
- **Risks:** Data maintenance burden and accuracy; scope to a few models.

### Vibe Game Jam Arena

**A showcase site where people submit AI-built mini-games and everyone plays and votes in 60-second rounds.**

*3-4 weeks · fun 4 · useful 3 · ease 2 · shareable 4 · sparked by people asked for it · powers pass*

- **For:** Vibe coders, game fans and casual players
- **Why now:** Simon Willison noted that vibe-coded games are now fun but that traditional game jams don't fit, and wants new ways to compare them. ([Simon Willison's Weblog, 2026-10-28](https://simonwillison.net/2026/Oct/28/vibe-game-development/)) ([Ben's Bites, 2026-10-29](https://www.bensbites.com/p/ai-is-overwhelming-and-im-doing-it)) ([Simon Willison's Weblog, 2026-10-20](https://simonwillison.net/2026/Oct/20/battledrones/))
- **How it works:** Creators paste a link or HTML file and a prompt-used note. Players get a random game for 60 seconds, then rate it on fun and originality. A leaderboard and badges show the top builds each week.
- **Build:** Next.js with Supabase for submissions and votes, sandboxed iframes. Hardest part is moderating and sandboxing arbitrary user HTML safely.
- **Demo moment:** Swipe through a feed of tiny games, each playable instantly.
- **Post hook:** A game jam where every entry took under an hour to build.
- **Risks:** Moderation burden and cold start; seed it with your own games.

### What Was I Doing Yesterday

**A browser extension that quietly logs tabs and summarises your day into a recap you can ask questions of.**

*1-2 weeks · fun 3 · useful 4 · ease 3 · shareable 3 · sparked by a common frustration · makers pass*

- **For:** Busy knowledge workers who lose context between days
- **Why now:** A developer built a daemon that logs activity and answers 'what was I doing yesterday'. Non-developers have the same pain with tabs and docs, and local-first logging is attractive. ([Hacker News — Ask HN, 2026-06-08](https://news.ycombinator.com/item?id=48449187)) ([Hacker News — Ask HN, 2026-06-08](https://news.ycombinator.com/item?id=48449187))
- **How it works:** Install the extension, which stores page titles and time spent locally. At end of day it creates a three-bullet recap and an open-loops list. User asks 'where was that pricing page?' and gets the link.
- **Build:** Chrome extension with IndexedDB and an LLM call on titles only, user-supplied key. Hardest part is privacy defaults, so exclude domains and keep everything local.
- **Demo moment:** Ask 'what was that article about pricing I read Tuesday?' and the link pops up instantly.
- **Post hook:** My browser now remembers my week better than I do.
- **Risks:** Privacy sensitivity and extension store review; browser history already exists.

### Text Adventure Skin

**Load a classic text adventure and play it with a friendly GUI that has maps, inventory and optional hints.**

*3-4 weeks · fun 4 · useful 2 · ease 2 · shareable 4 · sparked by something someone built · makers pass*

- **For:** Nostalgic gamers and newcomers who find parsers intimidating
- **Why now:** Users built a Codex interface for the open-sourced A Mind Forever Voyaging, in original or easier form. Interactive fiction has many open classics, and a generic skin would widen the audience. ([Understanding AI, 2026-10-19](https://www.understandingai.org/p/ai-is-ushering-in-an-age-personal)) ([Ben's Bites, 2026-10-29](https://www.bensbites.com/p/ai-is-overwhelming-and-im-doing-it))
- **How it works:** User picks an open-source interactive fiction title from a shelf. The app runs it in a web interpreter and adds clickable verbs, an auto-map and hint levels. An optional AI narrator rewrites the prose in a chosen style.
- **Build:** Web app embedding a Z-machine interpreter such as Parchment with an overlay UI. Hardest part is parsing the game state for maps and inventory.
- **Demo moment:** Click a verb instead of typing and a map draws itself as you walk through rooms.
- **Post hook:** I made a 1980s text adventure playable for people who never touched a parser.
- **Risks:** Licensing of games; only open-source titles.

