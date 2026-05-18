---
title: Rotation expectations document
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: expectations, syllabus, milestones
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generates a rotation expectations document mapping objectives to milestones, specifying daily/weekly responsibilities, defining the supervision model, and naming the evaluation criteria. Lives in the rotation handbook.

## The prompt

```
You are generating a rotation expectations document. Every objective must map to a specific milestone sub-competency code. Generic "will demonstrate competence" doesn't help the CCC.

## What I'm providing

- **Rotation:** [name + duration]
- **PGY level:** [target]
- **Service context:** [your institution's service]
- **Milestone document version:** [current]
- **Supervision model:** [autonomy gradient — how it changes start to end of rotation]
- **Evaluation framework:** [rubric or form name]

## What to produce

7 sections:

1. **Rotation overview** (2-3 sentences) — place in curriculum, prerequisites, what it builds toward
2. **Learning objectives** (5-8) — milestone-aligned, "will be able to" language with measurable verbs
3. **Daily responsibilities** — typical day's required activities
4. **Weekly responsibilities** — recurring less than daily
5. **End-of-rotation requirements** — deliverables, assessments
6. **Supervision model** — autonomy level at start, at end, triggers for attending involvement
7. **Evaluation criteria** — framework named, when evaluated

Specify any institutional-specific terms and define on first use.

## Hard rules

- **Every objective maps to a specific milestone sub-competency code.**
- **Measurable verbs only** (no "understand," "know").
- **Supervision gradient explicit.**
- **Verify milestone codes against the current version.**

## What I will NOT accept

- Vague objectives ("will demonstrate competence")
- Missing milestone mapping
- Vague supervision model
```

## Expected output

A 7-section document for the rotation handbook.

## Required human verification

- Verify milestone codes against current document.
- Run by rotation director and a recent rotator.
- Confirm supervision model matches institutional policy.

## Best model and why

**Claude Sonnet 4.6** — structured doc with milestone mapping is Sonnet's range.
