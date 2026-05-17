---
title: Board prep schedule
pillar: self-education
event_type: n/a
audience: resident
difficulty: quick-win
time_to_use: >10min
visual: text-only
tags: planning, board-prep
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Generate a personalized board prep schedule based on weeks remaining, daily study hours, and your strongest/weakest subspecialties.

## When to use it

At the start of board prep, or when you realize the existing plan isn't working and you need to re-allocate. Best when you can be honest with the model about your weak areas.

## The prompt

```
I'm preparing for [boards — name and date]. I have [N] weeks until the exam and can realistically commit [X] hours per day on weekdays and [Y] hours per day on weekends.

My self-assessment by subspecialty:
- **Strong:** [list subspecialties where you can pass at this moment]
- **Moderate:** [list where you'd struggle on harder questions]
- **Weak:** [list where you'd fail a focused subspecialty section]

My resources: [qbank, textbook, review course, etc.]

Generate a week-by-week schedule with:

1. Topic allocation per week (more time on weak areas, maintenance on strong areas).
2. Daily breakdown: reading hours, qbank hours, review hours.
3. A rest day every week — not optional.
4. A 'rescue' week 2 weeks before the exam for re-attacking the topics you're still weak in.
5. The week before the exam: zero new material, focused review only.
6. The last 48 hours: explicit instructions (sleep, light review, no caffeine experimentation).

Be specific about resource use, not generic. If you don't have enough info about my resources, ask.
```

## Expected output

A multi-week schedule with daily breakdown, rest days, a rescue week, and explicit pre-exam instructions. The plan should change weekly, not be a flat repeat.

## Common failure modes

- The schedule is unrealistic for your actual life. Push back with the constraints you didn't share.
- All days look the same — no rhythm. Push back: 'vary the pattern week to week.'
- The model schedules every minute and creates anxiety rather than structure.

## Required human verification

- Run the schedule by a colleague who's recently taken the exam. They will see flaws an AI cannot (e.g., 'no one needs to spend a week on cytogenetics for this exam').
- Adjust based on actual progress in week 2 — the initial plan is a hypothesis, not a contract.
