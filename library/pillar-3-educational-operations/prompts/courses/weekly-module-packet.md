---
title: Weekly module learning packet
pillar: educational-operations
event_type: course
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: module, packet
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generate a weekly module learning packet with required reading, pre-class question prompts, in-class activities, and post-class assessment.

## When to use it

One week before each module is delivered. The packet is what gets sent to learners + the instructor's preparation guide in one.

## The prompt

```
Generate a learning packet for Week [N] of [course name]. Topic: [topic]. Time: [duration of the in-class session].

The packet has two audiences:

**For the learners** (1-2 pages):
- Week topic and learning outcome (the one thing they should be able to do after this week).
- Required reading (1-3 items with full citations and a 1-sentence reading guide).
- 3 pre-class reflection questions to think about while reading.
- Pre-class assignment if any (brief, not a paper).

**For the instructor** (2-3 pages):
- Topic overview and where this week fits in the course arc.
- Suggested in-class agenda with timing.
- Active learning activities (1-2) with materials list.
- Discussion questions for the in-class session (5-7).
- Anticipated misconceptions and how to address them.
- Post-class assessment items (3-5 questions for an online quiz or written response).
- Recommended further reading for learners who want to go deeper.

Be specific about what learners produce. 'Discuss' is not enough — what's the artifact?

**Important — refinement:** Verify every reading citation and confirm institutional library access. If you can't verify, mark with [VERIFY] rather than including unverified citations.
```

## Expected output

A two-audience packet: learner-facing (concise) and instructor-facing (detailed enough to teach the week without further prep).

## Common failure modes

- Learner section is too long; learners skim or skip.
- Instructor section doesn't actually help an instructor who hasn't taught the topic before.
- Pre-class questions are surface-level recall.

## Required human verification

- Verify reading citations and confirm availability through your institution's library.
- Run the instructor section by a colleague who hasn't taught the week — would they be ready?
- Check that the post-class assessment aligns to the stated learning outcome.

## Best model and why

**Claude Sonnet 4.6** — Two-audience structured doc — Sonnet is the right tier. Verify reading citations regardless of model.
