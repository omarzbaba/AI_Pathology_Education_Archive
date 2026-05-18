---
title: Course feedback collection form
pillar: educational-operations
event_type: course
audience: faculty
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: feedback, survey, completion-rate
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Generates a course feedback form designed to actually be completed (under 5 minutes, bias toward structured items) and to actually inform decisions (every item maps to a specific change you'd make for the next iteration).

The discipline: if you can't name the decision an item would inform, cut it.

## The prompt

```
You are designing a course feedback form. Under 5 minutes, bias toward structured items, every item must map to a decision I'll make.

## What I'm building

- **Course name:** [name]
- **Audience:** [learners, count, level]
- **Format:** [in-person / online / hybrid]
- **Decisions I might make for next iteration:** [list — drop modules, adjust difficulty, change format, etc.]

## Form structure

### 1. Course-level Likerts (3-4 items)
Pacing, difficulty, value relative to time invested.

### 2. Module-level rapid rating (1 item per module)
Grade each module on usefulness 1-5.

### 3. Open free text (2 items MAX)
- "One thing that should change about this course before next iteration"
- "One thing that should NOT change"

### 4. Demographics (2-3 optional items)
Role, prior experience with topic, anything you actually need for stratifying.

### 5. Optional self-report on learning (1 item)
How much they think they learned, with calibration note ("we'll compare to pre/post assessment results")

### For each item:
- The question text
- Response format (single-select, Likert, free text)
- **The decision I'll make based on the answer** (the test — if you can't name a decision, cut)

## Hard rules

- **Under 5 minutes.** Hard cap.
- **Every item maps to a decision.** Cut items that don't.
- **At most 2 free-text fields.**
- **No "what would you change about the course" generic question** — too open.

## What I will NOT accept

- Form over 5 minutes
- Items without decision mapping
- More than 2 free-text fields
```

## Expected output

A 5-min form with per-item rationale + completion-time estimate.

## Required human verification

- Pilot with 2-3 learners and time.
- Plan how you'll analyze free-text responses before sending.

## Best model and why

**Claude Sonnet 4.6** — survey design.
