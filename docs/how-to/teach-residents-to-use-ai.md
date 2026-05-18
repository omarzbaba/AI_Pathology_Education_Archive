---
title: How to teach a resident to use AI well — a faculty / PD guide
last_updated: 2026-05-18
difficulty: intermediate
category: educator
---

Every other tutorial in this section assumes the reader is the AI user. This one is different: it's for the program director, the faculty mentor, the rotation director, the senior who is responsible for the next generation's AI literacy — whether they want to be or not.

Your residents are already using AI. Whether you've taught them to or not. Whether your program has a policy or not. The question is whether they're being taught well, or learning by trial-and-error and peer rumor.

This guide is the practical version of "what to teach, what to evaluate, what bad habits to catch early, and what to scaffold across the residency arc." It assumes you've personally used AI enough to recognize the failure modes (the [What to do when the AI is wrong](library.html#/docs/how-to/what-to-do-when-ai-is-wrong) tutorial is a prerequisite).

---

## Part 1 — The frame: AI literacy is a clinical skill now

Two ways of thinking about AI in residency education are both wrong:

**Wrong frame 1: "AI is a fad. Train the basics; let residents figure AI out on their own."** Residents will figure it out — badly. They'll cite AI in case reports. They'll use it to draft CCC narratives without disclosure. They'll trust threshold values it confidently invents. The cost of letting this self-educate is real, accruing now.

**Wrong frame 2: "AI will replace much of what we teach. Pivot the curriculum toward AI proficiency."** This overcommits to a technology whose specifics will change every quarter. Residents still need to learn pathology — slides, signs, smears, interpretation. AI literacy is additive, not substitutive.

**The right frame:** AI literacy is a *clinical skill* in 2026, comparable to "how to use UpToDate" in 2008. It has its own discipline, its own failure modes, its own ethics. It should be taught with the same seriousness, by faculty who actually use it, integrated into existing rotations rather than carved off into a separate "AI elective." The goal isn't to make residents AI specialists; it's to make them competent users who don't cause harm and who can defend their work.

The rest of this guide is about how to do that across the four-year arc.

---

## Part 2 — The four-year scaffold

A reasonable scaffold for AP/CP residency, adaptable to other lengths. Each year builds on the previous; the meta-skill is the same throughout (verify, take responsibility, disclose) but the depth and context change.

### PGY-1 — Posture and safety

**What to teach:**
- The verify-one-detail discipline (every response gets one specific claim checked against a primary source)
- The hard rules: no patient material, no clinical decisions, no citation of AI as a source
- The posture difference: AI is a tutor, not an oracle; you are responsible for the output
- How to write a basic five-component prompt
- The single-shot vs iteration distinction

**What to require:**
- One short reflection during the first six months: *"Describe one instance where you used AI for learning this rotation. What did you ask? What did you do with the response? What did you verify?"*
- The reflection is graded for *thinking*, not for AI fluency. A resident who says "I noticed the AI gave me a confidently wrong drug name and I caught it because I checked the FDA label" is doing better than one who says "I used AI and it was helpful."

**What to evaluate:**
- Whether they catch AI errors when you spot-check their work (this is the diagnostic question; if they consistently miss the errors, the literacy hasn't taken)

**Resource:** point them at [Your first 30 minutes with an LLM](library.html#/docs/how-to/first-30-minutes) and [How to write a good prompt](library.html#/docs/how-to/how-to-write-a-good-prompt). Read them yourself first.

### PGY-2 — Practical skill and chaining

**What to teach:**
- Chaining prompts within a single conversation (the discipline, not just the mechanics)
- Adapting library prompts to their subspecialty (when they hit one they care about)
- Cross-model verification for important questions
- Recognizing the five failure modes by name
- The difference between AI as study partner (acceptable) and AI as substitute for studying (not)

**What to require:**
- Use of an AI-assisted study technique in their board prep (NotebookLM corpus, source-grounded self-quizzing, etc.) with a one-line description of what they're doing
- A worked example of a "round 1 → round 3" prompt iteration on a topic relevant to their rotation (paste the three prompts and the three responses; comment on what changed and why)

**What to evaluate:**
- Whether they're using AI as a thinking partner or a homework-doer (the diagnostic question)
- Whether their study technique is producing measurable competence on rotation, not just AI-fluent talk

**Resource:** [Chaining prompts in one session](library.html#/docs/how-to/chaining-prompts), [Adapting prompts to your subspecialty](library.html#/docs/how-to/adapt-prompts-to-subspecialty), [What to do when the AI is wrong](library.html#/docs/how-to/what-to-do-when-ai-is-wrong).

### PGY-3 — Productive use and disclosure

**What to teach:**
- AI use in academic work — disclosure norms, journal policy, the misconduct line
- Building a personal AI workflow (the integration step, not just the skill step)
- Using AI to teach (residents teaching residents — they're starting to lead morning report, journal club, etc.)
- Multimodal AI for image-based work, with the framing trap discussion
- Cost and tool selection — when to use which model

**What to require:**
- All academic work (case reports, posters, abstracts) carries an explicit AI disclosure statement, even if the answer is "no AI was used"
- Demonstrate one teaching activity (slide deck, MCQ set, OSCE station) developed with AI assistance, with the workflow documented
- Personal AI workflow audit: name three triggers in their week where AI lives

**What to evaluate:**
- Whether they can defend everything in their AI-assisted work without consulting the AI again (the integrity test)
- Whether their AI-generated teaching material is representative (demographically, presentationally) or defaults to the model's biases
- Whether they're disclosing appropriately — neither over-disclosing trivially nor under-disclosing substantial use

**Resource:** [Disclosure and authorship](library.html#/docs/how-to/disclosure-and-authorship), [Bias in medical AI](library.html#/docs/how-to/bias-in-medical-ai), [Building your personal AI workflow](library.html#/docs/how-to/personal-ai-workflow), [Working with images](library.html#/docs/how-to/working-with-images).

### PGY-4 (and chiefs) — Teaching and leading

**What to teach:**
- How to teach junior residents to use AI (this guide, for them)
- How to set rotation-level norms on AI use as they take on leadership
- How to think about AI in their first faculty / fellowship year — institutional policy, scholarly integrity, model selection at scale
- The deeper antipatterns: AI as cover, AI replacing genuine learning, AI in clinical decision-making

**What to require:**
- Co-lead one teaching session on AI literacy for the PGY-1s coming in (you supervise; they teach)
- Contribute one prompt or tutorial to the program's shared library (this site, your program's internal version, whatever)
- An exit reflection on how AI has changed how they work over the four years, and what they wish they'd learned earlier

**What to evaluate:**
- Whether they can teach the junior residents the discipline (not just the skills) coherently
- Whether they leave residency with a sustainable AI workflow that will compound through their career
- Whether they understand AI well enough to set norms in their next setting (fellowship, faculty, community practice)

**Resource:** this guide, plus all the others.

---

## Part 3 — Bad habits to catch early

Six specific resident behaviors to watch for and correct. Each has a characteristic surface and a deeper failure mode.

### 1. The copy-paste resident

**Surface:** their resident notes, case reports, or teaching materials read fluently but generically. The voice is uniform across topics. The factual claims sometimes don't quite match the case.

**Diagnostic question:** ask them to explain a specific paragraph extempore, without notes. If they can't, the work isn't theirs.

**Correction:** don't shame; recalibrate. "I want to make sure you can defend everything in your work. Walk me through this section." Then teach the [Common mistakes](library.html#/docs/how-to/common-mistakes) tutorial's antipattern 7 explicitly.

### 2. The AI-as-authority resident

**Surface:** they reference AI conclusions as if they were primary sources. "Claude said it's PNH, so I think it's PNH." They don't push back when you disagree with the AI.

**Diagnostic question:** when you offer an alternative interpretation, do they evaluate it on its merits or check it against what AI said?

**Correction:** model the pushback discipline. When they cite AI, ask them where the AI got that, and require them to find the primary source. Make this routine, not punitive.

### 3. The over-discloser

**Surface:** every email, every note, every email has an "AI-assisted, may contain errors" disclaimer. The disclaimers are everywhere and signal nothing.

**Diagnostic question:** can they articulate when disclosure actually matters? Do they understand the difference between scholarly disclosure (substantive) and routine over-labeling (noise)?

**Correction:** walk them through the [Disclosure and authorship](library.html#/docs/how-to/disclosure-and-authorship) tutorial's section 5 — what does and doesn't warrant disclosure. Help them develop a personal policy.

### 4. The under-discloser

**Surface:** their case reports are well-written above their apparent ability. Their CCC narratives sound polished but generic. They don't mention AI use.

**Diagnostic question:** ask them directly about AI use in a specific piece of work. Do they downplay, evade, or own it?

**Correction:** this one is more serious. Set the program's expectation clearly and in writing: substantive AI use must be disclosed, every time. Make it a graded element. Catch it twice and have a longer conversation about scholarly integrity.

### 5. The framing-trap resident (esp. for image work)

**Surface:** they upload images to AI and ask "what is this?" They learn the diagnoses by AI revelation rather than by working through them.

**Diagnostic question:** their interpretive reasoning on real cases is weak relative to their apparent fluency. They name diagnoses confidently but can't articulate the features that drove the call.

**Correction:** introduce the [Working with images](library.html#/docs/how-to/working-with-images) tutorial's framing-trap section explicitly. Sit at the scope with them; require them to articulate features before naming an entity; do it without AI assistance for a period.

### 6. The opt-out resident

**Surface:** they don't use AI at all, often as a stated principle ("I want to learn the real way"). They lag peers on AI-adjacent skills (efficient literature review, teaching prep, drafting).

**Diagnostic question:** is the opt-out informed (they've tried it, they understand its uses and limits, they've made a thoughtful choice) or reflexive (they fear it, or they assume it's cheating)?

**Correction:** for informed opt-outs, respect the choice but require minimum literacy — they need to be able to evaluate AI-assisted work from peers and trainees they'll supervise. For reflexive opt-outs, address the underlying assumption: AI used well isn't cheating; AI used badly is, but the same is true of UpToDate or Google.

---

## Part 4 — Program-level decisions

If you're a program director or rotation director, a few decisions to make explicitly rather than implicitly:

### Policy on AI use in scholarly work

Pick a stance. Common options:

- **Permissive with disclosure**: residents may use AI for scholarly work as long as they disclose substantively. Most ICMJE-aligned position.
- **Permissive for some genres, restricted for others**: AI for posters and educational materials is fine; AI for case reports requires extra scrutiny; AI for original research is restricted.
- **Restrictive**: residents are discouraged from AI-drafting any work they submit for academic credit, with limited exceptions.

There is no right answer here. There is a wrong answer, which is to have no answer. Residents need to know what your program expects.

### Policy on AI in clinical documentation

Specifically: can residents use AI to draft routine reports, sign-out notes, CCC narratives? Different from scholarly work because the clinical record has different stakes.

Most programs currently say: no AI in primary clinical documentation, period. Some allow AI for non-clinical accompanying materials (educational case reports, teaching files derived from cases). Pick a stance, write it down, enforce consistently.

### Policy on AI in evaluations

Faculty using AI to draft resident evaluations is a real, growing pattern. Set the norm. If allowed: disclose. If not allowed: say so.

### A required AI literacy module

Strongly consider a 60-90 minute required session in the orientation week of PGY-1 year. Cover: hard rules, verify-one-detail, prompt basics, disclosure expectations, program policy. Use [How to write a good prompt](library.html#/docs/how-to/how-to-write-a-good-prompt) and [What to do when the AI is wrong](library.html#/docs/how-to/what-to-do-when-ai-is-wrong) as the spine.

This module should be taught by a faculty member who actually uses AI in their work — not delegated to "the tech person" or skipped. It signals that the program takes this seriously.

---

## Part 5 — A small set of program-level habits

Beyond formal policy, six small habits that shape culture:

1. **Faculty model AI use openly.** If you use AI to draft a teaching slide, mention it. If you use it to brainstorm OSCE scenarios, mention it. Residents will copy what they see; show them the responsible version.

2. **Disclose in your own talks.** When you give grand rounds or invited talks that used AI assistance, include a disclosure slide. Normalizes the practice.

3. **Make verification visible.** When you catch AI errors in your own work or in resident work, talk about how you caught them. The skill is in the catching, and residents only see it if you make it visible.

4. **Curate one shared resource.** A Slack channel, a Notion page, a folder of "good prompts our residents have developed." Something concrete that grows over time and that residents contribute to.

5. **Review AI policy annually.** The landscape changes. Your policy from two years ago is probably wrong on a few points now. Annual review with the residents in the room.

6. **Hire faculty who can do this.** As you replace faculty over time, hire with AI literacy as a meaningful criterion, not a nice-to-have. The future faculty cohort that can teach this well is the one you have to build deliberately.

---

## Part 6 — Common questions from PDs

**"Should I require my residents to use AI?"**

No. Require literacy (they can recognize the failure modes, they understand the discipline), not use. Some residents will adopt heavily; some will adopt lightly; both can be excellent pathologists.

**"What if a resident is using AI in a way I think is unethical?"**

Address it like any other professionalism issue. Have the conversation, document it, set expectations for change, follow up. The same playbook you'd use for any other concerning resident behavior.

**"What about residents who don't have personal devices or AI subscriptions?"**

Most major LLMs have free tiers sufficient for educational use. Don't let this be a barrier. If your institution has barriers (e.g., AI tools blocked on institutional networks), that's a separate fight to take to IT and compliance.

**"How do I evaluate AI literacy on the milestone framework?"**

It overlaps with several existing milestones — practice-based learning and improvement, professionalism, interpersonal communication. You don't need a new milestone. You need to ask milestone-relevant questions through an AI lens: *is this resident incorporating new information well? are they practicing ethically? are they communicating honestly?*

**"What if I, as faculty, don't really understand AI well enough to teach this?"**

The fastest way to build the capability is to use it for your own work for a month. Pick one of the workflows in [Building your personal AI workflow](library.html#/docs/how-to/personal-ai-workflow) and do it consistently. You'll be teaching from experience by the end of the month, which is more valuable than teaching from theory.

---

## Part 7 — Practical checklist for the next academic year

If you're starting next academic year with intent to do this well:

- [ ] Read all 16 of this site's How-to tutorials yourself (they're not long; cluster reading across a couple of evenings)
- [ ] Pick one workflow from [Building your personal AI workflow](library.html#/docs/how-to/personal-ai-workflow) and run it for 8 weeks before teaching others
- [ ] Draft your program's written policy on AI use in scholarly and clinical work
- [ ] Schedule a 90-minute required AI literacy module for the PGY-1 orientation
- [ ] Add an AI disclosure line to your resident evaluation forms
- [ ] Identify one piece of resident scholarship per quarter for a faculty-led review specifically about AI use
- [ ] Invite a resident or fellow who's a strong AI user to co-teach with you (peer teaching is high-leverage here)

If you do these seven things across an academic year, your program's AI culture will be substantially ahead of where it is now — and ahead of most peer programs. The residents you train will go to their next role (fellowship, faculty, community practice) as people who use AI well, set norms in their new settings, and don't cause harm with it.

That is the real outcome of this work. Not "our residents use AI." Not even "our residents are competent with AI." But: *our residents go on to be the people who teach others to use AI well, in places we'll never see.*

That's the multiplier effect, and it's the reason this matters.
