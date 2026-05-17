---
title: Daily schedule template
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: schedule, ops
verified_models: TODO
best_model: Claude Haiku 4.5
last_updated: 2026-05-17
---

## What this prompt does

Generate a daily schedule template for a rotation, with placeholders for sign-out, didactics, case review, and protected reading time.

## When to use it

When you're standardizing a rotation's day or when residents complain the day feels chaotic. The template doesn't constrain — it gives a default that everyone can plan around.

## The prompt

```
Generate a typical-day schedule template for [rotation name], [PGY level] resident.

Format as a timed schedule from arrival to departure, with each block including:

- Time range.
- Activity name.
- Who leads (resident, attending, fellow, tech, group).
- Brief note on what happens in the block.

Required blocks:
- Arrival / chart review or prep.
- Sign-out (morning or end-of-day per service convention — specify).
- Didactics or conferences (state which days these occur).
- Case review or workup blocks.
- **Protected reading time** (this is the block residents say is most often eroded — protect it explicitly).
- Lunch.
- End-of-day wrap-up.

Notes section after the schedule:
- Days when this template doesn't apply (call days, conference days, etc.).
- Common ways the schedule slips and what to do about each.
- Who to tell if you're going to be off the schedule (e.g., late, leaving early).

**Important — refinement:** Protected reading time should be at least 60 contiguous minutes. If the rotation workload makes that infeasible, name the trade-off explicitly rather than silently scheduling 30-minute fragments.
```

## Expected output

A timed template with all required blocks, plus notes on exceptions and slip handling.

## Common failure modes

- Protected reading time is in the schedule but functionally unprotected.
- No accommodation for clinical workload variability.
- Schedule assumes residents start at 7 am if you don't specify.

## Required human verification

- Validate against actual recent rotators — does the template match their real days?
- Confirm with attendings that they expect residents to be available during the blocks the schedule suggests.

## Best model and why

**Claude Haiku 4.5** — Template generation — Haiku is sufficient. The constraints (protected reading, slip handling) come from your prompt, not from model depth.
