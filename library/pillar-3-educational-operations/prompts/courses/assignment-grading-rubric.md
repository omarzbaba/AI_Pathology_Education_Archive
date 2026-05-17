---
title: Assignment grading rubric
pillar: educational-operations
event_type: course
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: rubric, grading
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Generate a rubric for a specific assignment with dimensions, level descriptors, and a scoring guide.

## When to use it

When you're assigning anything more substantive than a quiz and want consistent grading.

## The prompt

```
Generate a grading rubric for the following assignment:

- **Assignment**: [name and brief description]
- **Course**: [course name and audience]
- **Length / format expected**: [pages, slides, video minutes, etc.]
- **Learning objectives this assignment assesses**: [from the syllabus]
- **Point total**: [if graded numerically]

The rubric should have:

1. **4-6 dimensions** that together capture what 'good' looks like for this assignment. Each dimension should be **independently assessable** (don't combine content quality and writing into one row).
2. **4 levels** per dimension: Exemplary, Proficient, Developing, Needs Substantial Work. Each level with a behavioral or product descriptor (what would I observe in the artifact?).
3. **Point values** per dimension (if numeric grading) — weight dimensions according to how much they matter for the objectives.
4. **Feedback prompts** for each dimension to help graders write specific narrative feedback ('Cite one moment where the student demonstrated X').

End with:
- **Common pitfalls** for this assignment type (what students typically get wrong) and how the rubric captures them.
- **Estimated grading time** per submission.
```

## Expected output

A rubric with 4-6 well-defined dimensions, 4 levels each, feedback prompts, pitfalls, and time estimate.

## Common failure modes

- Level descriptors all sound positive — no real differentiation.
- Dimensions overlap and double-count.
- Numeric weighting doesn't reflect what actually matters.

## Required human verification

- Grade one sample submission with the rubric, then have a colleague grade the same one independently. Check for inter-rater agreement; refine where you disagree.
- Verify the rubric assesses the stated learning objectives.
