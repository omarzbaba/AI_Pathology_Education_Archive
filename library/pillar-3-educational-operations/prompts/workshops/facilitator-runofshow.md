---
title: Day-of facilitator run-of-show
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: operations, run-of-show, contingencies
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Generates the minute-by-minute facilitator run-of-show — the document the lead facilitator holds in their hand all day. Every block has a time range, owner, transition cue, and contingencies for running long, short, or tech failure. Builds in 5-minute buffers because real workshops always run long.

## When to use it

One week before the workshop, after the agenda is finalized but before you've drilled the team on day-of mechanics.

## The prompt

```
You are generating a minute-by-minute facilitator run-of-show. Build in 5-min buffers between blocks. Every transition needs a cue. Every block needs a contingency.

## What I'm planning for

- **Workshop title + date:** [name + date]
- **Times:** [start to end]
- **Venue:** [room layout, AV setup]
- **Agenda:** [paste block names, durations, lead facilitators]
- **Team members + roles:** [lead, support, AV, runners, etc.]
- **Recurring needs:** [coffee breaks every 90-120 min, lunch logistics, restroom locations]

## For each block, produce

- **Time range** (with buffer baked in — assume real start ~5 min later than scheduled)
- **Block name + lead facilitator**
- **One-line content summary**
- **Setup needed** (room arrangement, AV, materials to distribute)
- **Transition cue** — how does the lead hand off to the next block? Exact words help.
- **Contingencies:**
  - If block runs long
  - If block runs short
  - If tech fails

## Required structural blocks

- Registration / check-in / coffee
- Bathroom / coffee breaks every 90-120 min
- Lunch (with re-gathering time)
- Behind-scenes setup time (e.g., "set up station B while plenary runs")
- A 5-min buffer at the end before formal close

## At the end

- **Materials and AV needs by block** (one master list)
- **Roles table:** lead, support, AV, runner — who does what
- **Day-before checklist:** the 5-10 things to confirm by end of day before

## Hard rules

- **5-min buffer between major blocks.** Real workshops run long; build for it.
- **Transition cues are explicit, not assumed.** Awkward silences kill momentum.
- **Every block has contingencies.** Tech fails. People go long. Plan for it.
- **Lunch re-gathering time matters.** "Lunch 12-1" without a 12:55 "find your seats" cue produces a 1:15 actual restart.

## What I will NOT accept

- Schedule packed to 100% with no buffers
- Transition descriptions like "next block begins"
- Missing contingencies
- Lunch without re-gathering
```

## Expected output

A printable run-of-show document with timed blocks, transition cues, contingencies, materials/AV master list, roles table, day-before checklist.

## Required human verification

- Walk through the run-of-show with the lead facilitator and at least one other staff member before the day.
- Verify AV needs with the venue.
- Print multiple copies; the lead carries one and a backup copy is at registration.

## Best model and why

**Claude Sonnet 4.6** — timed scheduling with contingencies is Sonnet's range.
