---
title: Rotation evaluation rubric
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: advanced
time_to_use: >10min
visual: text-only
tags: evaluation, rubric, milestone-alignment
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generates a milestone-aligned evaluation rubric with behaviorally-anchored level descriptors. The key discipline: anchors describe OBSERVABLE BEHAVIORS, not personality traits, and they GENUINELY DISCRIMINATE between levels (not just sound positive at every level).

## When to use it

When piloting milestone-anchored evaluations or replacing a generic form. Should be reviewed by your CCC before deployment.

## The prompt

```
You are generating a rotation evaluation rubric. Anchors must be observable behaviors and must genuinely discriminate between levels. "Demonstrates competence" at every level is the failure mode.

## What I'm building

- **Rotation:** [name + duration]
- **PGY level:** [target level]
- **Milestone document version:** [your program's current version]
- **Number of dimensions:** [usually 5-7]
- **Rater time budget:** [target — usually 15 min]

## What to produce

### 5-7 dimensions

Each mapped to a milestone sub-competency this rotation is positioned to assess. Mix of knowledge/technical and professional/interpersonal.

### Per-dimension structure

For each dimension:
- Name
- Milestone sub-competency mapping
- **5 levels with behavioral anchors:**

Each anchor must describe an OBSERVABLE BEHAVIOR. Examples:
- BAD: "Demonstrates competence in interpreting routine cases"
- GOOD: "Independently formulates a workup plan for routine cases and seeks supervision appropriately for complex ones; escalation decisions match attending expectations >80% of the time"

- **Narrative comment prompt** to help raters write specific feedback ("Cite one specific case or moment where you observed this dimension")

### Quality controls

- Each dimension independently rateable (no overlap)
- 5 levels genuinely differentiate
- Behavioral anchors, not personality traits
- "Unable to assess" option for each dimension

### Time and observation requirements

- Estimated rater time
- Minimum observations needed to assign each dimension fairly

## Hard rules

- **Observable behaviors only.** "Shows enthusiasm" is not an anchor.
- **Genuine differentiation.** If levels 3, 4, 5 all sound positive in different ways without distinction, the anchors are too soft.
- **Independent dimensions.** "Writing quality" and "organization" overlap; merge or rewrite.
- **"Unable to assess" option non-negotiable.** Otherwise raters default to 3/5 for things they didn't observe.

## What I will NOT accept

- Personality-trait anchors
- Anchors that all sound positive
- Overlapping dimensions
- Missing "unable to assess" option
```

## Expected output

5-7 dimensions, each with 5-level behaviorally-anchored descriptors, narrative prompts, quality controls.

## Common failure modes

- **Anchors that all sound positive.** Push back: "Differentiate."
- **Personality traits.** Push back.
- **Overlapping dimensions.** Push to merge or rewrite.

## Required human verification

- Run by CCC chair before use.
- Pilot with two raters scoring the same resident — check inter-rater agreement.
- Verify milestone mapping is current.

## Best model and why

**Claude Opus 4.7** — behavioral anchors that genuinely discriminate require care. Sonnet anchors tend toward all-positive.
