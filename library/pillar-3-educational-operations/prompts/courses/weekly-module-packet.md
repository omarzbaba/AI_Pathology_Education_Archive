---
title: Weekly module learning packet
pillar: educational-operations
event_type: course
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: module, packet, two-audience
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Generates a weekly module learning packet that serves TWO audiences: a learner-facing version (concise, 1-2 pages, focused on what to do) and an instructor-facing version (detailed, 2-3 pages, focused on how to teach). Includes pre-class prep, in-class agenda, active learning activities, anticipated misconceptions, post-class assessment, and further reading.

## When to use it

One week before each module is delivered. The packet IS the prep — drafted with the instructor in mind so they can teach the week without further prep.

## The prompt

```
You are generating a weekly module learning packet for TWO audiences: learners (concise) and instructors (detailed). Verify reading citations regardless of audience.

## What I'm providing

- **Course name:** [name]
- **Week number + topic:** [N + topic]
- **In-class session duration:** [minutes]
- **Course arc context:** [how this week fits relative to prior and future weeks]
- **Audience:** [target learners]

## TWO deliverables

### A. For learners (1-2 pages)

- **Week topic + learning outcome** (the ONE thing they should be able to do after this week)
- **Required reading** (1-3 items with full verified citations + 1-sentence reading guide per item)
- **3 pre-class reflection questions** to consider while reading
- **Pre-class assignment** if any (brief — not a paper)

### B. For instructors (2-3 pages)

- **Topic overview + place in course arc**
- **Suggested in-class agenda with timing**
- **Active learning activities (1-2)** with materials list
- **Discussion questions for in-class** (5-7)
- **Anticipated misconceptions and how to address each**
- **Post-class assessment items (3-5 questions)** — for online quiz or written response
- **Recommended further reading** for learners who want depth

## Hard rules

- **Verify reading citations** — fabricated paper titles are common.
- **Specify what learners produce** — "discuss" isn't enough; name the artifact.
- **Instructor section is sufficient for a colleague who hasn't taught the week** to teach it.

## What I will NOT accept

- Unverified citations
- Vague "discuss this" without an artifact
- Instructor section that requires additional prep to be usable
```

## Expected output

A two-audience packet: learner-facing concise + instructor-facing detailed.

## Required human verification

- Verify reading citations and confirm institutional library access.
- Run instructor section by a colleague who hasn't taught the week — would they be ready?

## Best model and why

**Claude Sonnet 4.6** — two-audience structured doc.
