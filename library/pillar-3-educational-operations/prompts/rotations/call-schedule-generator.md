---
title: Call schedule generator with constraints
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: call-schedule, planning, constraints
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generates a fair call schedule respecting constraints (vacations, time-off requests, ACGME work-hour rules, fairness across residents, weekend equity). This is the chief resident task that consumes hours and produces resentment when done poorly.

## When to use it

When you're building the next call cycle — typically a quarterly or semi-annual task. Best done with all constraint information collected upfront.

**Not for:** ad hoc swap requests (use a swap tool), schedules without explicit constraints (the prompt requires them), or replacing your program's institutional scheduling system.

## The prompt

```
You are generating a call schedule that must be fair and constraint-respecting. Show your work — explain the trade-offs you made and where the schedule is tight.

## What I'm providing

- **Time period:** [start date to end date, e.g., "January 1 to March 31, 2027"]
- **Call type:** [pathology call / CP-only call / weekend call / etc.]
- **Residents available:** [list with PGY level for each]
- **Per-resident constraints:**
  - Vacation requests (specific dates)
  - Conference / educational leave
  - Hard "no" dates (interviews, life events)
  - Soft preferences (avoid weekends, prefer back-to-back, etc.)
- **Institutional rules:**
  - ACGME work hour limits applicable
  - Maximum consecutive call days
  - Mandatory rest days
  - Weekend frequency caps
- **Total slots to fill:** [calculate from time period × shifts per day]

## What to produce

### The schedule

A day-by-day table:
| Date | Day | Resident | Notes |

### Fairness check

- Total call days per resident
- Weekend days per resident
- Holiday days per resident (if applicable)
- Variance flag: which residents are over- or under-allocated and by how much

### Constraint compliance check

For each resident, confirm:
- All hard "no" dates respected
- Vacation dates respected
- Work-hour rules not violated
- Maximum consecutive days not exceeded

### Tradeoffs I should know about

- **Where the schedule is tight** (any constraint I came close to violating)
- **Where I had to compromise** (soft preferences I couldn't accommodate, and why)
- **What additional flexibility from a resident would most improve the schedule**

### Swap-friendly notes

For each resident, identify the dates that would be easiest for them to swap with someone if a swap request comes in later.

## Hard rules

- **All hard constraints respected.** No exceptions, no "almost."
- **Work-hour rules not violated.** Flag if my stated constraints are inconsistent with ACGME rules.
- **Fairness calculation must be honest.** If the schedule is unfair to one resident, say so directly.
- **Do not silently relax constraints to make the math work.** Tell me what's blocking and ask for adjustment.

## What I will NOT accept

- A schedule that violates a hard constraint (even one)
- Hidden compromises ("almost equal weekends")
- A schedule generated without flagging the tradeoffs
```

## Expected output

A complete schedule + fairness check + constraint compliance check + tradeoffs + swap-friendly notes.

## Common failure modes

- **Hard constraint violated silently.** Verify every constraint manually before publishing.
- **Fairness math hidden.** Push for explicit per-resident totals.
- **Schedule that "works on average" but is unfair to one resident.** Push back.

## Required human verification

- **Verify every hard constraint against the schedule.** The model can miss things.
- **Verify ACGME work-hour rules** for your specialty and PGY level.
- **Share the draft with affected residents** before finalizing. They will spot issues you and the model missed.
- **Document your fairness methodology** so you can defend the schedule.

## Best model and why

**Claude Opus 4.7** — multi-constraint scheduling with fairness reasoning is hard. Opus produces more honest tradeoff analysis than Sonnet, which tends to silently relax constraints.
