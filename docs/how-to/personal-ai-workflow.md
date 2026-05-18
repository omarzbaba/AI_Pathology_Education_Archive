---
title: Building your personal AI workflow — making it a routine, not an experiment
last_updated: 2026-05-18
difficulty: intermediate
category: practice
---

You have the skills. You can write a good prompt, read the response critically, work in sessions, switch models when needed. So why does AI still feel like an experiment that happens occasionally, rather than a working part of your week?

Because skills don't make a workflow. A workflow is the *integration* — where AI lives in your daily and weekly rhythm, what triggers you to open it, what you'd never use it for, and how it compounds value over time instead of feeling like extra work.

This guide is about building that integration. The audience is a pathologist who has done the literacy tutorials and now wants AI to actually change how they work — not just be a thing they're "trying."

---

## Part 1 — Why integration is the hard part

The literacy tutorials in this section teach the technical skills. They're necessary. But here's the trap most pathologists fall into:

> "I learned how to use AI. I use it sometimes. But it still feels like extra work — like a thing I have to remember to do instead of something built into how I work."

If that's you, the missing layer is workflow design. Skills are about *capability*; workflow is about *trigger*. You can know how to write a good prompt and still not write one this week because nothing in your week prompted you to.

The pathologists who get sustained value from AI have answered three questions:

1. **What are the recurring moments in my week where AI would help?**
2. **What's the friction that's keeping me from using it in those moments?**
3. **What habits or rituals would lower that friction?**

This guide walks you through each.

---

## Part 2 — Audit your week first

Before designing where AI fits, name the recurring moments where it *could* fit. A working audit:

Spend 10 minutes thinking through a typical week and write down everything you do recurringly that involves either (a) producing some text or (b) learning something. Be concrete. Don't write "sign-out"; write "Monday morning sign-out prep — I look at the case list the night before and read up on entities I'm rusty on."

A representative list for a typical academic CP attending might look like:

- Sunday evening: review next week's CP case mix, look up anything unfamiliar
- Monday morning: chair morning report; need a teaching point for the case du jour
- Mid-week: prep for a lecture I'm giving Friday
- Weekly: review and sign off on resident notes / case reports
- Bi-weekly: journal club preparation
- Monthly: tumor board prep where I'm presenting one case
- Quarterly: course material updates for the residents' CP curriculum
- Annually: APD-related curriculum and rotation planning

This is your *map*. Each item is a candidate for AI integration. Don't decide yet which ones — just see them.

Pathologists who skip this step end up using AI for one-off tasks that don't compound (e.g., occasionally drafting a hard email) and missing the high-leverage recurring patterns (e.g., weekly journal club prep that would benefit massively from a Project-backed workflow).

---

## Part 3 — Pick three triggers, not ten

The temptation after the audit is to plan AI integration for everything on your list. Don't. Pick three triggers — one weekly, one daily-ish, one as-needed. Three is enough to build habits without overload.

**A weekly trigger** is a recurring task that happens on a predictable cadence — Friday lecture prep, Monday case review, Sunday journal scan. These are the highest-leverage AI integrations because the same workflow runs repeatedly and you can refine it.

**A daily-ish trigger** is something that happens multiple times a week but on demand — drafting feedback notes for residents, helping you think through a hard case, writing a quick email that's harder than it should be. These are smaller individual wins but they add up.

**An as-needed trigger** is something that fires when a specific situation arises — when you're asked to write a letter of recommendation, when you're preparing for a tumor board where you're presenting, when you have to draft a manuscript section. These are infrequent but high-value when they hit.

A worked example for a typical academic CP attending:

- **Weekly:** Friday lecture prep. Every Friday afternoon I block 90 minutes for AI-assisted lecture work — outline generation, speaker notes, audience polls, MCQ drafting.
- **Daily-ish:** Resident feedback note drafting. Whenever I sign off on a case where I want to give the resident structured feedback, I draft with AI assistance before editing.
- **As-needed:** Letter of recommendation. When asked to write a LOR, I follow the [Disclosure and authorship](library.html#/docs/how-to/disclosure-and-authorship) tutorial's recommended pattern: AI for brainstorming, my own voice for the writing.

Three triggers is enough. Resist the urge to add a fourth until you've maintained these three for a month.

---

## Part 4 — Lower the friction at each trigger

A trigger fires; you should be doing the AI-assisted version within 30 seconds. If there's more friction than that, you'll skip it and revert to the old way.

Friction sources to remove:

### Bookmark the right starting point

For each trigger, identify the specific page or tool you want to open and bookmark it. Not "claude.ai" — bookmark the *specific Claude Project* you've set up for that workflow.

- Weekly journal club prep → bookmark the Claude Project that has your year's journal club papers pre-loaded
- Friday lecture prep → bookmark a NotebookLM notebook with your reference textbook chapters for the current rotation
- Resident feedback drafting → bookmark a Claude conversation template (or use a saved prompt)

The bookmark eliminates the "where do I start?" friction.

### Pre-draft your starting prompt

For recurring workflows, write a starting prompt template once and save it where you can paste it quickly. A simple notes app entry, a Notion page, a TextExpander snippet. Whatever you'll actually use.

Example saved prompt for resident feedback drafting:

> Act as a senior pathology attending writing a structured feedback note for a resident I'm supervising on [rotation]. The resident is a PGY-[X]. I observed them [specific behavior]. Help me draft a feedback note that:
>
> 1. Names one specific strength I observed
> 2. Names one specific area for improvement
> 3. Suggests a concrete next step the resident can take this week
> 4. Is calibrated to PGY-[X] expectations (not generic, not condescending)
> 5. Is 150-200 words
>
> Ask me clarifying questions before drafting.

Paste this template, fill in the brackets, send. 30 seconds from trigger to working session. No friction, no decision fatigue.

### Build small reusable Projects rather than one giant one

A single "Pathology" Claude Project loaded with 50 source documents is unwieldy. Better: 4-6 small, focused Projects.

- "Journal club 2025–2026" — current year's selected papers
- "Heme path board prep" — board-relevant references
- "CP teaching reference" — the textbooks I assign residents
- "Letters of recommendation context" — anonymized examples of what I've written before, in my voice

Each Project is small enough to keep curated. Each is fast to open and start working in. Together they cover most of your recurring needs.

The [Source curation principles](library.html#/docs/how-to/curate-sources) tutorial covers what belongs in each notebook.

---

## Part 5 — A worked weekly rhythm

To make this concrete, here's what a fully-integrated weekly rhythm might look like for an academic CP attending:

**Sunday evening (20 minutes):**
- Open your "Sign-out prep" Claude Project, loaded with this week's signed-out cases (your own notes, not patient material).
- Prompt: "Quiz me on the entities I'm likely to encounter this week based on the rotation. Three short questions per entity, mixed difficulty."
- Drill for 15 minutes. Note any entities where you struggled.
- For the weak spots, switch to NotebookLM with your reference chapters loaded. Drill the same entities against the source material.

**Monday morning (15 minutes):**
- For morning report's case du jour, open a fresh Claude conversation.
- Prompt: "Help me design a 5-minute teaching turn around this case [paste case summary, de-identified]. One teaching point, two discussion questions, the common misread to call out."
- Use the structure as your morning report scaffold.

**Wednesday (30 minutes):**
- Mid-week journal scan. Open your "Journal club 2025–2026" Project.
- Add this week's two or three new papers to the corpus.
- Prompt: "Critique the methodology of [paper title]. What would a strong PGY-3 catch about the design?"
- Read the critique, then read the paper, then discuss with yourself: where did the AI miss, where did it help.

**Friday afternoon (90 minutes):**
- Lecture prep. Open a fresh Claude conversation.
- Paste your saved lecture-prep prompt with this week's topic filled in.
- Iterate: outline → critique → fill section 1 → critique → fill section 2 → etc.
- Generate speaker notes, audience polls, two practice MCQs.
- Export as Markdown, paste into your slide tool.

**As-needed throughout the week:**
- Resident feedback notes: paste saved prompt, 5 minutes per note.
- Hard email: AI to draft, my own voice to revise.
- LOR: AI for brainstorm, my own voice for the writing.

Total weekly AI time: ~3 hours. Total weekly value: incalculable, because it's not just "the lecture is better" — it's "the lecture is better AND I learned something AND the residents got cleaner feedback AND I'm not as fried Friday afternoon."

---

## Part 6 — What NOT to integrate

A short list of things that look like AI workflow opportunities but actually aren't:

**Don't integrate clinical decision-making.** AI does not belong in the pathway from slide to diagnosis. You can use it to *teach* about the diagnosis after the fact, but not to make the call. Same goes for ordering tests, signing out reports, calling critical values.

**Don't integrate anything involving real patient data.** This is just the [Privacy and copyright](library.html#/docs/how-to/privacy-and-copyright) rule restated, but in the workflow context: don't build a routine that requires you to paste patient material into AI. If your weekly workflow includes "summarize this patient's chart," redesign it.

**Don't integrate things where AI saves you 30 seconds but adds 5 minutes of overhead.** If you're spending more time prompting and editing than you would just doing the task, the integration is wrong. Some tasks are genuinely faster the old way.

**Don't integrate one-off creative work.** A toast for a colleague's retirement, a personal letter, a hand-written note. AI assistance here is technically possible and aesthetically wrong. Some writing should come from you, period.

---

## Part 7 — Maintaining the workflow

The first month of a new AI workflow is the fragile part. Two things make it stick:

### Calendar block, don't aspire

If your Friday afternoon AI lecture prep is "something I'll do when I have time," it won't happen. If it's a recurring calendar block (90 minutes, Friday 1:00 PM, blocked as Lecture Prep with no other meetings allowed), it will. Treat it like a clinic block — fixed, defended, not negotiable.

### Track the win, not the activity

After each session, write one line in a notes file: *what did I get out of this 90 minutes that I wouldn't have gotten otherwise?* If you can't articulate the win for three sessions in a row, redesign the integration. If you can articulate it consistently, you've found your rhythm.

The track-the-win habit prevents the silent decay where you keep doing the workflow but it's no longer producing value. Discovery happens in the noticing, not in the doing.

---

## Part 8 — When to refactor

After 6–8 weeks of a stable workflow, do a brief refactor:

- Which integrations earned their place? Keep, possibly expand.
- Which integrations technically happen but produce thin value? Either redesign the prompt / Project, or drop.
- Which moments in your week still feel like "I should be using AI here but I keep not"? That's a candidate for a fourth trigger.

The workflow is not static. It evolves with your role, your rotations, your residents, the model landscape. Quarterly refactor keeps it living.

---

## Part 9 — Practical checklist

For your first month of intentional AI workflow:

- [ ] I audited my week and named the recurring text/learning moments
- [ ] I picked exactly three triggers (one weekly, one daily-ish, one as-needed) — no more
- [ ] I bookmarked the specific tool / Project for each trigger
- [ ] I wrote a saved starting prompt for each recurring task
- [ ] I calendar-blocked the recurring sessions (not "when I have time")
- [ ] I'm tracking one-line win-notes after each session
- [ ] I refactor every 6–8 weeks based on what's earning its place

If you can do this for a month, AI stops being an experiment in your work and starts being part of how you work. That's the durable outcome — not "I tried AI today" but "I'm a measurably more effective educator because of how AI is integrated into my week."
