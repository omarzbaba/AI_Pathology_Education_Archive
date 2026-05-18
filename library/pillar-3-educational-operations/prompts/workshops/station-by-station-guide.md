---
title: Station-by-station facilitator guide
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: station-guide, parallel-documents,rotating-stations
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Generates per-station facilitator guides for a rotating-station workshop. Each station gets its own consistent-format guide: objectives, materials, setup, minute-by-minute script, reset instructions, what attendees walk away with, common questions, and an optional deepening activity for early finishers.

The discipline this enforces: each station's minute-by-minute should account for ~90% of the time allocation, leaving 10% as buffer.

## When to use it

2 weeks before a station-based workshop. Each station owner gets their own guide.

## The prompt

```
You are generating per-station facilitator guides. Consistent format across stations so facilitators can find what they need fast. Each station's script accounts for ~90% of time allocation; 10% is buffer.

## What I'm planning

- **Workshop title + date:** [name + date]
- **Stations:** [list each with topic and lead facilitator]
- **Time per station rotation:** [minutes per rotation]
- **Number of rotations:** [how many groups cycle through]
- **Attendee group size per rotation:** [how many at each station at once]

## For EACH station, produce this consistent structure

### Header
- Station name + lead facilitator + topic
- Time allocation per rotation

### Learning objectives (2-3, in "will be able to" language)

### Materials list
Everything the station owner needs: paperwork, samples, AV, models, props.

### Setup instructions
What to do before the first group arrives. Specific.

### Minute-by-minute script for ONE rotation
- Opening (greeting, frame, ground rules) — 1-2 min
- Content blocks — bulk of time
- Active engagement / hands-on / case discussion
- Closing wrap — last 2-3 min

Must add to ~90% of time allocation, leaving 10% buffer.

### Reset instructions
What to do between rotations (re-stocking, cleanup, repositioning).

### What attendee walks away with
The specific artifact, demonstrated skill, or question they can now answer.

### Common attendee questions
3-5 likely questions and the prepared answer for each.

### If you have extra time
An optional deepening activity for groups who finish early.

## Hard rules

- **Consistent format across all stations.** Facilitators reference different stations during setup; they need to find sections fast.
- **Time budget verified.** Script + buffer = total time. Verify.
- **Walk-away is specific** — not "they'll have learned about X" but "they'll have made a labeled diagram", "they'll be able to interpret a normal vs abnormal trace at first glance", etc.

## What I will NOT accept

- Inconsistent format across stations
- Scripts that exceed time allocation
- Vague walk-away
```

## Expected output

One guide per station, consistent format. 1-2 pages each. Print-ready.

## Required human verification

- Run through one station's guide as the facilitator with a stopwatch. Adjust.
- Each station's lead reads and edits their own guide before the day.

## Best model and why

**Claude Sonnet 4.6** — parallel structured documents are Sonnet's strength.
