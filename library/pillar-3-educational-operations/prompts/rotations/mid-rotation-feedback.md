---
title: Mid-rotation feedback template
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: feedback, mid-rotation, course-correction
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Generates a mid-rotation feedback template that surfaces course-correction opportunities before the end-of-rotation evaluation locks in. Structures a 10-15 minute conversation (not a paper exercise) with reflection prompts for both resident and attending, conversation flow, and minimal documentation.

The discipline this enforces: the meeting must fit in 15 minutes. Mid-rotation feedback that becomes a 30-minute conversation gets cancelled by the third occurrence.

## When to use it

At the midpoint of any rotation, especially for rotations longer than 2 weeks.

## The prompt

```
You are generating a mid-rotation feedback template. It must fit in 15 minutes max. The point is course-correction, not formal evaluation.

## What I'm building

- **Rotation:** [name + duration]
- **Format:** [in-person / virtual]
- **Who's involved:** [resident + which attending(s)]

## What to produce

### Pre-meeting work for the resident (3-4 reflection questions)

How the rotation is going from their perspective, what they need more or less of, what's surprised them.

### Pre-meeting work for the attending (3-4 observation prompts)

Specific strengths observed, specific opportunities for growth, anything the resident might not know about themselves.

### Conversation structure (5 blocks, 15 min total)

- **Resident shares first** (2 min)
- **Attending shares** (3-4 min)
- **Joint identification of one strength to lean into** (2 min)
- **Joint identification of one specific growth area for the second half** (2 min)
- **Agreement on one observable change by end of rotation** (2 min)

### What gets documented

ONLY: one strength, one growth area, one commitment. No surprises at end-of-rotation evaluation.

## Tone

Collaborative, low-stakes, course-correction oriented. Not evaluative.

## Hard rules

- **15-minute meeting cap.** If template requires longer, cut sections.
- **Documentation is minimal** — three things, period.
- **The commitment must be observable** for end-of-rotation assessment.

## What I will NOT accept

- Template that produces a 30-minute meeting
- Documentation that turns this into an early formal evaluation
- Vague commitments
```

## Expected output

Pre-meeting prep questions for both parties + conversation flow + minimal documentation requirements.

## Required human verification

- Pilot with a willing attending-resident pair. Time the meeting; adjust.
- Check that the documented commitment is observable enough to assess at end-of-rotation.

## Best model and why

**Claude Sonnet 4.6** — meeting template structure.
