---
title: Conference schedule and topic rotation
pillar: educational-operations
event_type: conference
audience: faculty
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: schedule, topic-rotation, presenter-balance
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Generates a quarterly or annual conference schedule with topic rotation across subspecialties, balanced presenter loads, required-topic coverage, and buffer sessions. Includes a draft invitation email template.

## When to use it

Annually when planning the academic year's conference series, or quarterly for shorter cycles.

## The prompt

```
You are generating a conference schedule. Balance topics across subspecialties, balance presenter loads, include buffer sessions, and confirm with each presenter before publishing.

## What I'm building

- **Conference series name:** [e.g., "Tuesday morning CP didactics"]
- **Audience:** [target + level]
- **Frequency:** [weekly / biweekly]
- **Number of sessions to fill:** [N]
- **Available presenters:** [list with subspecialties and rotation availability]
- **Required topic coverage:** [subspecialties or specific topics that must be covered, e.g., RISE prep blocks]
- **Standing items:** [recurring slots — journal club every Nth week, in-service review, etc.]

## What to produce

### Full schedule
Date, topic, presenter, any pre-reading.

### Balance check
- Distribution of topics across subspecialties
- Flag if some subspecialties are over- or under-represented; suggest adjustments

### Presenter load check
- Distribution of sessions per presenter
- Flag if any presenter is overloaded (>X sessions in Y weeks)

### Buffer sessions
- 1-2 unscheduled or flexible sessions per quarter for guest speakers, schedule slips, or topic substitutions

### Logistics
- Room, AV needs, recording status, attendance tracking

### Invitation email template
Draft email I can use to invite each presenter with their assigned date and topic.

## Hard rules

- **Verify presenter availability before publishing.** Model can suggest; you must confirm.
- **Buffer sessions are non-optional.**
- **Sequencing constraints respected** (e.g., RISE prep BEFORE the exam, not after).

## What I will NOT accept

- Schedule that assumes presenters are available without verification
- No buffer sessions
- Required-coverage topics scheduled at suboptimal times
```

## Expected output

Schedule + balance check + presenter load check + buffer + logistics + invitation template.

## Required human verification

- **Verify each presenter's availability before publishing.**
- Confirm room and AV bookings.
- Validate sequencing against constraints.

## Best model and why

**Claude Sonnet 4.6** — schedule planning with constraints.
