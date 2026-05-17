---
title: Conference schedule and topic rotation
pillar: educational-operations
event_type: conference
audience: faculty
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: schedule, rotation
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generate a quarterly or annual conference schedule with topic rotation across subspecialties and assigned presenters.

## When to use it

Annually when you're planning the conference series for the academic year, or quarterly for shorter cycles.

## The prompt

```
Generate a [quarterly / annual] conference schedule for [conference series name — e.g., 'Tuesday morning CP didactics']. Audience: [target audience and level].

Constraints:
- **Frequency**: [weekly / biweekly]
- **Number of sessions to fill**: [N]
- **Available presenters**: [list of presenters with their subspecialties and rotation availability]
- **Required topic coverage**: [subspecialties or specific topics that must be covered, e.g., RISE prep blocks]
- **Standing items**: [recurring slots — journal club every Nth week, in-service review, etc.]

Produce:

1. A full schedule with date, topic, presenter, and any pre-reading.
2. **Balance check**: distribution of topics across subspecialties. If some subspecialties are over- or under-represented, flag it and suggest adjustments.
3. **Presenter load check**: distribution of sessions per presenter. Avoid overloading any one person.
4. **Buffer sessions**: 1-2 unscheduled or flexible sessions per quarter to accommodate guest speakers, schedule slips, or topic substitutions.
5. **Logistics**: room, AV needs, recording status, attendance tracking.

End with: a draft email template I can use to invite each presenter with their assigned date and topic.

**Important — refinement:** The model can suggest a schedule but YOU must confirm each presenter's availability before publishing. Do not treat suggested presenters as confirmed.
```

## Expected output

A schedule + balance and load checks + buffer sessions + logistics + invitation template.

## Common failure modes

- Schedule is balanced on paper but a single presenter has 3 sessions in a row.
- No buffer sessions, so any schedule change cascades.
- 'Required coverage' items get scheduled but in suboptimal weeks (e.g., RISE prep after the exam).

## Required human verification

- Verify each presenter's availability before publishing.
- Confirm room and AV bookings.
- Validate the topic order against any sequencing constraints (e.g., a topic that's a prerequisite for another).

## Best model and why

**Claude Sonnet 4.6** — Schedule planning with constraints — Sonnet handles this. Confirm presenter availability regardless of what the model suggests.
