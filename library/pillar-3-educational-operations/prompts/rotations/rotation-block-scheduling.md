---
title: Rotation block scheduling across an academic year
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: advanced
time_to_use: >10min
visual: text-only
tags: rotation-schedule, annual-planning, constraints
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generates a year-long rotation block schedule respecting required experiences, board prep timing, elective preferences, and constraints (vacation, conference, life events). Different from call scheduling — this is the "which resident is on which rotation each block" annual puzzle.

## When to use it

Annually when planning the next academic year's rotation assignments. Best done after collecting resident preferences and constraints but before the year begins.

**Not for:** call scheduling (different prompt), ad hoc rotation swaps (different process), or programs where rotation assignments follow a strict algorithm without flexibility.

## The prompt

```
You are generating a year-long rotation block schedule. Respect required experiences, board prep timing, and resident constraints. Be honest about tradeoffs.

## What I'm providing

- **Academic year:** [July 2027 - June 2028]
- **Block structure:** [number of blocks, length of each — usually 13 four-week or 12 four-week blocks]
- **Residents:** [list with PGY level for next year]
- **Required rotations per PGY level:**
  - PGY-1: [list with minimum blocks each]
  - PGY-2: [list]
  - PGY-3: [list]
  - PGY-4: [list]
- **Resource constraints:** [maximum residents per rotation per block, e.g., "max 2 on autopsy", "max 1 on molecular"]
- **Resident preferences:**
  - Elective preferences (ranked)
  - Board prep block requests (if applicable)
  - Vacation block requests
  - Hard conflicts (interviews, life events, conferences)
- **Program priorities:** [graduating resident board prep, fellowship interview accommodation, etc.]

## What to produce

### The grid

Block-by-block, resident-by-resident schedule:

| Block | Dates | Resident 1 | Resident 2 | Resident 3 | ... |

### Required-experience compliance check

For each resident, confirm:
- All required rotations completed by end of year (or PGY level)
- Minimum blocks met for each
- Sequencing makes sense (e.g., autopsy before sign-out independence)

### Resource compliance check

For each block, confirm:
- Resource caps not exceeded (max residents per rotation)
- No critical rotations unstaffed

### Preference accommodation summary

Per resident:
- Electives received vs requested
- Vacation blocks granted vs requested
- Board prep timing
- Hard conflicts respected

### Tradeoffs I should know about

- Which residents got less of their preferences and why
- Where I had to make compromises on sequencing
- What additional flexibility would most improve the schedule
- Which residents I'd talk to first about adjustments

### Comparison to fairness baseline

How does this schedule compare to a baseline where preferences were ignored and rotations were assigned alphabetically? Useful to show your CCC the schedule isn't arbitrary.

## Hard rules

- **Required rotations met for every resident.** No exceptions.
- **Resource caps respected.** No exceptions.
- **Hard conflicts respected.** No exceptions.
- **Be honest about preference accommodation.** Don't claim "preferences met" when they weren't.
- **Flag if my stated constraints are mathematically impossible to satisfy** rather than silently relaxing them.

## What I will NOT accept

- A schedule that misses a required rotation for any resident
- A schedule that exceeds resource caps
- Hidden preference compromises
- Schedule generated without flagging tradeoffs
```

## Expected output

Schedule grid + required-experience check + resource check + preference summary + tradeoffs + fairness comparison.

## Common failure modes

- **Required rotation missed silently.** Verify manually.
- **Resource cap exceeded.** Verify.
- **Hidden preference compromises.** Push for explicit comparison.

## Required human verification

- **Verify every required rotation count manually.** The model can miscount.
- **Share the draft with residents** before publishing — they'll spot issues.
- **Verify against ACGME and your program's specific requirements.**
- **Document fairness methodology** for the CCC.

## Best model and why

**Claude Opus 4.7** — multi-constraint annual scheduling with fairness reasoning rewards Opus's depth.
