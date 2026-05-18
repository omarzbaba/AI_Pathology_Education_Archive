---
title: Resident-as-teacher scaffolding
pillar: teaching
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: resident-as-teacher, scaffolding, teaching-skills
verified_models: TODO
best_model: Claude Sonnet 4.6
last_invariant: 2026-05-17
---

## What this prompt does

Scaffolds a teaching session for a resident who has been asked to teach — typically for the first time. Forces the resident to think about teaching as a deliberate practice (one concept, one slide, one exercise) rather than content delivery.

The single most useful question: "what is the ONE concept you most want them to walk away with?" If it doesn't fit in one sentence, it's too broad.

## When to use it

When you're a senior resident asked to give a teaching session, or when you're an attending coaching a resident through their first teaching attempt. Useful both as preparation and as a coaching conversation guide.

**Not for:** experienced teachers (different scope), prep for high-stakes formal lectures (use the slide outline prompt), or contexts where you're being assessed on teaching skill (different framing).

## The prompt

```
You are scaffolding my preparation for a teaching session. Push me to think about teaching as a deliberate practice, not content delivery. If my answers are vague, push back.

## My context

- **My level:** [PGY level]
- **Session topic:** [what I'm teaching]
- **Audience:** [who and how many — be specific, e.g., "the three incoming PGY-1s in their first week of CP, plus the senior resident who's been with us a year"]
- **Session duration:** [in minutes]
- **Format:** [didactic / case-based / hands-on / interactive — what I have in mind]
- **My teaching experience:** [first time / a few times / regular]

## Walk me through these 6 questions, one at a time

### 1. What is the ONE concept you most want them to walk away with?

State it in one sentence. If you can't fit it in one sentence, it's too broad — push you to narrow.

Pressure-test: can a learner reasonably restate it in 30 seconds at the end of the session? If not, still too broad.

### 2. What are the 2-3 common misconceptions about this topic you should anticipate?

These are the misconceptions that experienced teachers know but you might miss. If your answers are generic ("they might think it's easy"), push for specific cognitive shortcuts learners use.

### 3. If you had only ONE slide, what would it show?

Describe the visual or text in detail. This is the anchor slide — if you had 30 seconds with this audience, what would you put up?

### 4. What is the simplest exercise you could do that would let you see whether they understood the one concept?

Active retrieval or application. Not "ask if they have questions" — an exercise that produces an artifact (a written answer, a verbal commitment, a marked-up image).

### 5. What's the question you should NOT try to answer in this session?

The related topic that would be a different talk. Naming it explicitly prevents scope creep.

### 6. How will you know if the session went well?

Give 2-3 observable indicators during or right after — not "they seemed engaged" but specific behaviors.

## After my answers, give me

- **Your one specific suggestion** for how to make the session land better
- **The one risk** I should anticipate

## Hard rules

- **Walk through questions ONE AT A TIME.** Wait for my answer.
- **Push back if my answer is vague.** Generic answers produce generic sessions.
- **The 'one concept' must fit in 30 seconds.** If not, narrow.
- **Observable indicators must be observable.** "Engagement" is not observable.

## What I will NOT accept

- Walking through all 6 questions at once
- Accepting vague answers without pushback
- Recommendations that aren't specific to my context
```

## Expected output

A back-and-forth scaffolding conversation across 6 questions, ending with the model's specific suggestion and risk callout.

## Common failure modes

- **Model dumps all 6 questions at once.** Push back: "One at a time."
- **Accepting vague answers.** Push back yourself: "I gave a vague answer — push me to be more specific."
- **Generic suggestions at the end.** Push back.

## Required human verification

- Run the 'one concept' by a colleague at the target audience level — does it land?
- Validate the observable indicators are actually observable.

## Best model and why

**Claude Sonnet 4.6** — reflective scaffolding suits Sonnet's pattern of clear, structured outputs.
