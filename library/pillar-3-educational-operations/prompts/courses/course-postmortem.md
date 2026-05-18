---
title: Course post-mortem document
pillar: educational-operations
event_type: course
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: postmortem, retrospective, action-items
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Generates a course post-mortem template that structures a 45-60 minute meeting AND produces a documented artifact for the curriculum file. The discipline: action items must have named owners and dates. Aspirational changes without ownership are not action items.

## When to use it

Within 2-4 weeks of course completion, when feedback is in but instructors still remember.

## The prompt

```
You are generating a course post-mortem template. Action items must have named owners and dates. Without that, the items are aspirations.

## What I'm planning

- **Course name + duration + term/year:** [name + when]
- **Instructors involved:** [names + roles]
- **Available data:** [feedback summary, assessment results, attendance]

## Three deliverables

### 1. Pre-meeting work (10 min per instructor)
- Review feedback data
- Note 2-3 things that worked
- Note 2-3 things that didn't
- Note any change made mid-course and how it landed

### 2. Meeting structure (45-60 min)
- **Quick round** (10 min): each instructor's top "worked" and top "didn't work"
- **Discussion of patterns** (15 min): what came up multiple times?
- **Mid-course changes review** (10 min): keep, revert, or refine?
- **Decisions for next iteration** (15 min): 3-5 specific changes, ranked by ease × impact
- **Documentation owner + timeline** (5 min)

### 3. Artifact to produce after the meeting
- Summary of what worked / didn't (3-4 bullets each)
- Mid-course changes log
- **Action list with named owner and date for each item**
- Structural issues to escalate to curriculum committee

## Tone

Honest, learning-oriented, no defensiveness.

## Hard rules

- **Every action item has owner + date.** No exceptions.
- **Schedule meeting before course ends.** Don't wait for "when there's time."
- **Artifact reviewable by anyone who didn't attend.**

## What I will NOT accept

- Action items without ownership
- Vague "we should improve" statements
- Meeting structure that becomes a venting session
```

## Expected output

Meeting structure + artifact template. Lightweight enough to actually happen.

## Required human verification

- Each action item should have a named owner and date.
- Schedule the meeting before the course ends.

## Best model and why

**Claude Sonnet 4.6** — meeting structure + artifact template.
