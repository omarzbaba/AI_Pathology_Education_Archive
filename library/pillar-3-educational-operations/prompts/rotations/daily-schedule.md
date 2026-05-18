---
title: Daily schedule template
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: schedule, daily-template, protected-time
verified_models: TODO
best_model: Claude Haiku 4.5
last_updated: 2026-05-18
---

## What this prompt does

Generates a typical-day schedule template for a rotation with required blocks (sign-out, didactics, case review, protected reading) and explicit acknowledgment of when protected reading time is unrealistic given the rotation's workload.

The discipline this enforces: protected reading time is ≥60 contiguous minutes. If the rotation doesn't allow it, name the trade-off explicitly rather than scheduling 30-minute fragments.

## When to use it

When you're standardizing a rotation's day, or when residents complain the day feels chaotic.

## The prompt

```
You are generating a typical-day rotation schedule. Protected reading time is ≥60 contiguous minutes — if workload doesn't allow it, name the trade-off explicitly.

## What I'm building

- **Rotation:** [name]
- **PGY level:** [target]
- **Typical workload:** [case volume, on-call expectations, special services]
- **Sign-out convention:** [morning sign-out / end-of-day / both]
- **Required didactics or conferences:** [days and times these occur]
- **Lunch convention:** [time + duration]

## What to produce

### Timed schedule, arrival to departure

| Time range | Activity | Lead | Notes |

Required blocks:
- Arrival / chart review or prep
- Sign-out
- Didactics or conferences (specify days)
- Case review or workup blocks
- **Protected reading time** (≥60 contiguous min)
- Lunch
- End-of-day wrap-up

### Notes section

- Days when template doesn't apply (call days, conference days, etc.)
- Common ways the schedule slips and what to do
- Who to tell if you'll be off the schedule (late, leaving early)

### If protected reading time is mathematically infeasible

State this honestly. Name the trade-off — what would have to give to create 60 contiguous protected minutes?

## Hard rules

- **Protected reading ≥60 contiguous minutes.** If not feasible, say so.
- **Specific times, not "morning."**
- **Slip-handling protocol included.**

## What I will NOT accept

- Schedule that pretends protected time exists when it doesn't
- Vague time ranges
- Missing slip-handling
```

## Expected output

A timed template + notes section + honest trade-off statement if protected reading is infeasible.

## Required human verification

- Validate against recent rotators — does the template match real days?
- Confirm with attendings that they expect residents available during the blocks shown.

## Best model and why

**Claude Haiku 4.5** — template generation.
