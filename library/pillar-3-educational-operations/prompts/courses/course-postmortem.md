---
title: Course post-mortem document
pillar: educational-operations
event_type: course
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: postmortem, retrospective
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generate a course post-mortem template covering what worked, what didn't, what changed mid-course, and what to do differently next time.

## When to use it

Within 2-4 weeks of course completion, when feedback is in but instructors still remember the course. Don't postpone — institutional memory decays fast.

## The prompt

```
Generate a post-mortem template for [course name], [course duration] in [term/year], taught by [instructors].

The template should structure a 45-60 minute meeting AND produce a documented artifact for the curriculum file. Sections:

1. **Pre-meeting work** for each instructor (10 min each):
   - Review feedback data.
   - Note 2-3 things that worked.
   - Note 2-3 things that didn't.
   - Note any change made mid-course and how it landed.

2. **Meeting structure** (45-60 min):
   - Quick round: each instructor's top 'worked' and top 'didn't work' (10 min).
   - Discussion of patterns: what came up multiple times? (15 min).
   - Mid-course changes review: keep, revert, or refine? (10 min).
   - Decisions for next iteration: 3-5 specific changes, ranked by ease × impact (15 min).
   - Documentation owner and timeline (5 min).

3. **Artifact to produce after the meeting**:
   - Summary of what worked and what didn't (3-4 bullets each).
   - Mid-course changes log (kept, reverted, or refined).
   - Action list for next iteration (specific, owned, dated).
   - Any structural issues to escalate to the curriculum committee.

Tone: honest, learning-oriented, no defensiveness.

**Important — refinement:** Action items must have named owners and dates. Items without an owner are aspirations, not actions. If an item has no clear owner, flag it for me to assign or cut.
```

## Expected output

A meeting structure + an artifact template. Lightweight enough to actually happen.

## Common failure modes

- Meeting runs over and becomes a venting session rather than a decision-making one.
- Action list is aspirational rather than specific.
- No assigned owner means changes don't get made.

## Required human verification

- Each action item should have a named owner and a date.
- The artifact should be reviewable by anyone who didn't attend the meeting.
- Schedule the meeting before the course ends; don't wait until 'when there's time'.

## Best model and why

**Claude Sonnet 4.6** — Meeting structure + artifact template — Sonnet is sufficient. The 'named owners and dates' discipline is on you, not the model.
