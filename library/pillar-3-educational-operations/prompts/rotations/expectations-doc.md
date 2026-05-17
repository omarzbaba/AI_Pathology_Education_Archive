---
title: Rotation expectations document
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: expectations, syllabus
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Generate a rotation expectations document with milestone-aligned objectives, daily and weekly responsibilities, and the supervision model.

## When to use it

When you're rolling out a revised rotation or onboarding a new attending who needs to understand what the program expects. Lives in the rotation handbook.

## The prompt

```
Generate a rotation expectations document for [rotation name], [N] weeks in duration, for [PGY level] residents.

Structure:

1. **Rotation overview** (2-3 sentences): the rotation's place in the curriculum, what it builds on, what it builds toward.
2. **Learning objectives** (5-8): milestone-aligned where possible, written in 'will be able to' language with measurable verbs.
3. **Daily responsibilities**: a typical day's required activities (sign-out, case review, didactics).
4. **Weekly responsibilities**: anything that recurs less than daily (journal club, case conference, presentation).
5. **End-of-rotation requirements**: deliverables, assessments, exit interviews.
6. **Supervision model**: what level of autonomy at the start of the rotation, what level at the end, what triggers attending involvement.
7. **Evaluation criteria**: how the resident will be assessed, with the rubric or framework named.

This document should answer 'what is expected of me?' clearly enough that no resident has to guess.

Specify any institutional-specific terms (e.g., 'sign-out', 'preview') and define them on first use.
```

## Expected output

A complete expectations doc covering all seven areas. Suitable for the rotation handbook and onboarding.

## Common failure modes

- Objectives that aren't actually assessable.
- Supervision model that's vague enough to be uninterpretable.
- Daily/weekly responsibilities that don't match the actual rotation flow.

## Required human verification

- Verify objectives map to actual milestones in your program's current document.
- Run by the rotation director and at least one recent rotator before finalizing.
- Confirm the supervision model is consistent with your program's policy and any institutional credentialing rules.
