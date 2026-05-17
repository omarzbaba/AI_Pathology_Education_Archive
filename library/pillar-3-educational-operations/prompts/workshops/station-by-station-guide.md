---
title: Station-by-station facilitator guide
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: operations, station-guide
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generate per-station facilitator guides for a rotating-station workshop, including learning objectives, materials, timing, and assessment per station.

## When to use it

2 weeks before a station-based workshop. Each station owner gets their own guide.

## The prompt

```
Generate a per-station facilitator guide for a rotating-station workshop. Each station gets its own guide.

Stations: [list each station with its topic and lead facilitator]
Time per station: [minutes per rotation]
Number of rotations: [how many groups will cycle through each station]

For EACH station, produce:

1. **Station header:** name, lead facilitator, topic, time allocation.
2. **Learning objectives** (2-3, in 'will be able to' language).
3. **Materials list:** everything the station owner needs (paperwork, samples, AV, models).
4. **Setup instructions:** what to do before the first group arrives.
5. **Minute-by-minute script for one rotation:** opening, content blocks, closing. Should fit in the time allocation with 2-3 min buffer.
6. **What to do between rotations:** reset instructions.
7. **What an attendee should walk away with** (the artifact, the demonstrated skill, the question they can now answer).
8. **Common attendee questions and the prepared answer.**
9. **If you have extra time:** an optional deepening activity.

Format consistently across all stations so facilitators can quickly find what they need.

**Important — refinement:** Each station's minute-by-minute should account for ~90% of the time allocation, leaving 10% as buffer for transitions and unexpected questions. Stations packed to 100% run over.
```

## Expected output

One guide per station, each in the same format. Total length: 1-2 pages per station.

## Common failure modes

- Objectives aren't actually achievable in the time allocated.
- Minute-by-minute timing doesn't include reset time between rotations.
- No accommodation for early-finisher groups.

## Required human verification

- Run through one station's guide as if you were the facilitator, with a stopwatch. Adjust timing.
- Have each station's actual lead read and edit their own guide before the day.

## Best model and why

**Claude Sonnet 4.6** — Parallel structured documents (one per station, same format) is exactly Sonnet's strength.
