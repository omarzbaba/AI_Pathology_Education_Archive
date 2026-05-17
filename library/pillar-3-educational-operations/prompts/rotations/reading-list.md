---
title: Rotation reading list with rationale
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: reading-list, references
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generate a curated rotation reading list with a one-sentence rationale per item explaining why each reading is on the list.

## When to use it

When the existing reading list is stale, when you're building a new rotation, or when residents tell you the current list is too long.

## The prompt

```
Generate a curated reading list for [rotation name] for [PGY level] residents on a [N]-week rotation.

The list should be:

- **8-15 items.** Resist the urge to include everything; readability and use matter more than comprehensiveness.
- **Grouped by week or by topic** so residents know what to read when.
- **Prioritized**: mark each as Required, Strongly Recommended, or Optional Deep Dive.

For each item:

1. Full citation.
2. **One-sentence rationale**: why this is on the list. What gap does it fill?
3. Approximate reading time.
4. **One question** the resident should be able to answer after reading.

Include a mix of:
- 1-2 foundational textbook chapters.
- 2-3 high-yield review articles (recent).
- 1-2 landmark papers (older, still cited).
- 1-2 current guidelines.
- 1 piece of historical context (an older paper that explains why the field thinks the way it does).

At the end, name the 2 items the resident should read in the first 48 hours.

**Important — refinement:** Verify EVERY citation. Models routinely generate plausible-looking but non-existent paper titles. If you cannot verify a citation, leave it out and recommend I add one I know exists.
```

## Expected output

A prioritized reading list with rationale, time estimate, and check-question for each item.

## Common failure modes

- List is too long; nobody reads it all.
- 'Foundational' chapters are out of date.
- Citations are inaccurate or missing.

## Required human verification

- Verify every citation. Models routinely hallucinate paper titles and authors.
- Check that landmark papers are still considered foundational in current practice.
- Have an attending in the subspecialty review and prune.

## Best model and why

**Claude Opus 4.7** — Curation requires judgment about which papers are landmark vs current. Opus is more careful, but **verify every citation regardless of model** — hallucinated paper titles are common.
