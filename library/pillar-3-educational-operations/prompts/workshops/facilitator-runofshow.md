---
title: Day-of facilitator run-of-show
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: operations, run-of-show
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generate a minute-by-minute facilitator run-of-show for a workshop, including transitions, contingencies, and named owners for each block.

## When to use it

One week before the workshop. The run-of-show is the document the lead facilitator holds in their hand all day.

## The prompt

```
Generate a minute-by-minute facilitator run-of-show for [workshop title] on [date], from [start time] to [end time].

Workshop structure: [paste the agenda with block names, durations, lead facilitators]

For each block, the run-of-show should include:

- **Time range** (e.g., 9:15-9:35)
- **Block name and lead facilitator**
- **One-line content summary**
- **Setup needed** (room arrangement, AV, materials to distribute)
- **Transition cue** (how does the lead facilitator hand off to the next block?)
- **Contingencies:** what's the fallback if (a) the block runs long, (b) the block runs short, (c) the tech breaks?

Include explicit blocks for:
- Registration / check-in / coffee
- Bathroom / coffee breaks (every 90-120 min)
- Lunch (with timing for re-gathering)
- Anything the lead facilitator needs to do behind the scenes (e.g., 'set up next station while panel runs')

End with:
- A list of materials and AV needs by block.
- The roles list: who does what (lead, support, AV, runner).

**Important — refinement:** Build in 5-minute buffers between blocks. Real workshops always run long; the run-of-show should plan for this rather than assume perfect timing.
```

## Expected output

A document the lead facilitator can use to run the day without thinking. Should be print-friendly.

## Common failure modes

- Blocks transition without explicit cues — leads to awkward silences.
- No contingencies for running long/short.
- Lunch timing doesn't account for re-gathering.

## Required human verification

- Walk through the run-of-show with the lead facilitator and at least one other staff member before the day.
- Verify any AV needs with the venue.

## Best model and why

**Claude Sonnet 4.6** — Timed scheduling with contingencies — Sonnet handles this reliably. Verify the timing math regardless of model.
