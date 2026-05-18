---
title: Assignment grading rubric
pillar: educational-operations
event_type: course
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: rubric, grading, assessment
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## The prompt

```
You are generating a grading rubric. Dimensions must be independently assessable. If two dimensions could be confused, merge or rewrite.

## What I'm providing

- **Assignment:** [name + brief description]
- **Course:** [name + audience]
- **Expected length/format:** [pages/slides/video min]
- **Learning objectives assessed:** [from syllabus]
- **Point total:** [if graded numerically]

## What to produce

### 4-6 dimensions

Each capturing what "good" looks like. Independently assessable (don't combine content quality and writing).

### 4 levels per dimension

Exemplary / Proficient / Developing / Needs Substantial Work — each with a behavioral or product descriptor (what would I observe in the artifact?).

### Point weighting

Per dimension, weighted by impact on objectives.

### Feedback prompts

Per dimension, prompts to help graders write specific narrative feedback ("Cite one moment where the student demonstrated X").

### Common pitfalls

Type-specific failure modes the rubric captures.

### Estimated grading time

Per submission, in minutes.

## Hard rules

- **Independently assessable dimensions.**
- **4 levels that genuinely differentiate** — not all positive.
- **Weighting reflects actual importance.**
- **Pitfalls specific to assignment type.**

## What I will NOT accept

- Overlapping dimensions
- All-positive level descriptors
- Generic feedback prompts
```

## Expected output

4-6 dimensions × 4 levels with prompts, pitfalls, time estimate.

## Required human verification

- Grade one sample submission with the rubric, then have a colleague grade independently. Refine where you disagree.
- Verify rubric assesses stated objectives.

## Best model and why

**Claude Opus 4.7** — sharp distinctions between levels reward depth.
