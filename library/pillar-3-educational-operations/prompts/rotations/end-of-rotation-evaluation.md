---
title: End-of-rotation evaluation
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: evaluation, end-of-rotation, milestone-aligned
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Generates an end-of-rotation evaluation form aligned to milestones, with numeric ratings, narrative comments per dimension, an overall narrative, a specific commitment for next rotation, and an "unable to assess" gate to prevent defaulting to 3/5 for dimensions the evaluator hasn't observed.

## When to use it

When updating an evaluation form or when residents and attendings both complain the current form doesn't capture what matters.

## The prompt

```
You are generating an end-of-rotation evaluation form. Include an "unable to assess" option for each dimension — otherwise raters default to 3/5 for things they didn't observe. False data is worse than no data.

## What I'm building

- **Rotation:** [name]
- **PGY level:** [target]
- **Evaluation rubric to use:** [paste, or generate using the evaluation-rubric prompt first]
- **Estimated time available for an attending:** [target ≤30 min]

## Form sections

1. **Header**
   - Resident name + rotation + dates + supervising attending(s) + weeks evaluated

2. **Numeric ratings**
   - Each dimension from rubric, rated 1-5 with anchor text visible
   - **"Unable to assess" option for each dimension** — non-negotiable

3. **Narrative comment per dimension**
   - Prompted with: "Describe a specific instance where you observed this resident at this level"

4. **Overall narrative**
   - 1-2 paragraph free text
   - Trajectory, strengths, growth opportunities

5. **Specific commitment for next rotation**
   - 1-2 behavioral targets for resident focus

6. **Quality-of-evaluation gate**
   - "Did you have sufficient observation to evaluate this resident on the dimensions you rated?" yes/no/partial with comment

7. **Resident sign-off**
   - Box for resident acknowledgment of receipt and discussion

## Hard rules

- **"Unable to assess" option on every dimension.** Stops default-to-3 behavior.
- **Narrative prompts are specific** ("describe a specific instance"), not vague.
- **20-30 min completion time** for an attending who knows the resident well.
- **Quality gate prevents inflated ratings** from undersampled observations.

## What I will NOT accept

- Missing "unable to assess" option
- Vague narrative prompts
- Forms that take an hour
- No quality gate
```

## Expected output

A complete evaluation form covering all sections.

## Required human verification

- Pilot with one attending on one resident; iterate based on what's hard to complete.
- Verify milestone alignment.
- Confirm form complies with institutional or ACGME documentation requirements.

## Best model and why

**Claude Sonnet 4.6** — form generation with milestone alignment.
