---
title: Course feedback collection form
pillar: educational-operations
event_type: course
audience: faculty
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: feedback, form
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Generate a course feedback form with quantitative and qualitative items balanced for completion rate and signal quality.

## When to use it

At the end of a course block (mid-course and end-of-course), when you want actionable feedback rather than vague satisfaction scores.

## The prompt

```
Generate a course feedback form for [course name]. Audience: [learners — number, level].

The form should:

1. Take **under 5 minutes** to complete. Hard cap.
2. Mix structured (numeric/Likert) and unstructured (free text) items, but bias toward structured to keep completion high.
3. Yield **actionable** results — every item should map to a decision I could make for the next iteration.

Sections:

1. **Course-level Likerts** (3-4 items): pacing, difficulty, value relative to time invested.
2. **Module-level rapid rating** (1 item per module): grade each module on usefulness 1-5.
3. **Open free text** (2 items only):
   - 'One thing that should change about this course before next iteration.'
   - 'One thing that should NOT change.'
4. **Demographics** (2-3 items, all optional): role, prior experience with the topic, anything you actually need for stratifying results.
5. **Optional self-report on learning** (1 item): how much they think they learned, with a calibration note ('We'll compare this to pre/post assessment results').

For each item, include the question, the response format, and a one-sentence rationale ('I'll use this to decide whether to drop Module X next year').
```

## Expected output

A 5-minute form with item-by-item rationale. Should produce data you can actually act on.

## Common failure modes

- Form is too long; completion rate drops below 50% and you have selection bias.
- Free text questions are too open; results are unanalyzable.
- 'How satisfied were you' generic items that don't inform any decision.

## Required human verification

- Pilot with 2-3 learners and time them.
- Confirm each item maps to a specific decision.
- Plan how you'll analyze free text responses before sending the survey — otherwise the data won't get used.
