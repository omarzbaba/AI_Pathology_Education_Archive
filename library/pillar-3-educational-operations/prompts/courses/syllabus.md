---
title: Course syllabus
pillar: educational-operations
event_type: course
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: syllabus, course
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generate a course syllabus with weekly topics, learning objectives, assessment plan, and policy language.

## When to use it

When you're designing a new longitudinal course (residency didactic series, fellowship curriculum, elective course) and need a starting structure.

## The prompt

```
Generate a course syllabus for [course name], [N] weeks in length, for [audience].

The syllabus should include:

1. **Course title, instructor(s), meeting time and location.**
2. **Course description** (3-5 sentences): scope, prerequisites if any, where this course fits in the larger curriculum.
3. **Learning objectives** (4-7): course-level objectives in 'will be able to' language.
4. **Weekly schedule**: each week with topic, readings, in-class activity, post-class assignment if any. Be specific.
5. **Assessment plan**: how learners are evaluated (formative and summative components, weighting if graded).
6. **Required and recommended resources** with full citations.
7. **Policies**: attendance, makeup work, accommodations, AI use, academic integrity. Address each explicitly.
8. **Communication norms**: how to contact instructors, expected response times.

For each weekly topic, name **one outcome** the learner should be able to demonstrate after that week.

Match the level of formality your institution expects (CME-accredited course = more formal; residency didactic series = less).

**Important — refinement:** Include an explicit AI use policy. The default should not be silence; it should specify which uses are encouraged (e.g., drafting, brainstorming), which require disclosure, and which are prohibited (e.g., submitting AI output as own work for graded assignments).
```

## Expected output

A complete syllabus organized by section. Length: 5-8 pages. Should pass review by the relevant curriculum committee.

## Common failure modes

- Weekly topics that aren't actually achievable in one session.
- AI use policy that's either absent or boilerplate; both are problematic.
- Assessment plan that doesn't align with the stated objectives.

## Required human verification

- Verify required resources are in print and accessible.
- Check institutional policies on AI use and assessment — your statement should match.
- Run the weekly schedule by anyone who taught the course previously.

## Best model and why

**Claude Sonnet 4.6** — Structured doc with explicit policies (AI use, integrity) — Sonnet handles this. The AI use policy is the genuinely new part; spend time refining it.
