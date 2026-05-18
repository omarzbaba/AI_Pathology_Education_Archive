---
title: Course syllabus
pillar: educational-operations
event_type: course
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: syllabus, course, policies
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generates a complete course syllabus with weekly schedule, objectives, assessment plan, resources, policies (including an EXPLICIT AI use policy — not silence), and communication norms.

## The prompt

```
You are generating a course syllabus. Every week must have a topic + outcome. AI use policy must be explicit — silence is not a policy.

## What I'm providing

- **Course name:** [name]
- **Duration:** [N weeks]
- **Audience:** [target learners]
- **Meeting time/location:** [if applicable]
- **Format:** [in-person / hybrid / async]
- **Prerequisites:** [if any]
- **My institution's specific requirements:** [CME accreditation, etc.]

## What to produce

8 sections:

1. **Course title, instructor(s), meeting info**
2. **Course description** (3-5 sentences) — scope, prerequisites, place in curriculum
3. **Learning objectives** (4-7) — course-level, "will be able to" with measurable verbs
4. **Weekly schedule** — each week with topic, readings, in-class activity, post-class assignment, outcome
5. **Assessment plan** — formative + summative, weighting if graded
6. **Resources** — required and recommended with full citations
7. **Policies**:
   - Attendance
   - Makeup work
   - Accommodations
   - **AI use policy — explicit, not silence**
   - Academic integrity
8. **Communication norms** — how to reach instructors, response times

For each weekly topic, name ONE outcome demonstrating mastery.

## Hard rules

- **AI use policy explicit.** Specify what's encouraged, what requires disclosure, what's prohibited.
- **Every week has a measurable outcome.**
- **All resources verified.**
- **Match institutional formality** (CME = more formal; didactic series = less).

## What I will NOT accept

- Silent or boilerplate AI use policy
- Weekly topics without outcomes
- Assessment plan disconnected from objectives
```

## Expected output

Complete syllabus, 5-8 pages, ready for curriculum committee review.

## Required human verification

- Verify all resource citations.
- Check institutional policies for AI use match your statement.
- Confirm assessment plan aligns to objectives.

## Best model and why

**Claude Sonnet 4.6** — structured doc with explicit policies. The AI policy is the genuinely new part; spend time refining it.
