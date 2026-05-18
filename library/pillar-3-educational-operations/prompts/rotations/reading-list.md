---
title: Rotation reading list with rationale
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: reading-list, curation, references
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-18
---

## What this prompt does

Generates a curated rotation reading list (8-15 items) with a one-sentence rationale per item, prioritized as Required / Strongly Recommended / Optional Deep Dive. The hardest discipline: **verify every citation**. Models routinely hallucinate plausible-looking paper titles.

## When to use it

When the existing reading list is stale, when building a new rotation, or when residents tell you the current list is too long to actually read.

## The prompt

```
You are generating a rotation reading list. VERIFY EVERY CITATION. If you cannot verify a citation, leave it out and recommend I add one I know exists. Plausible-looking but fabricated paper titles are common.

## What I'm building

- **Rotation:** [name + duration]
- **PGY level:** [target]
- **Subspecialty focus:** [be specific]
- **My time budget for residents reading per week:** [be honest about what fits]

## What to produce

### 8-15 items, NOT MORE

Resist comprehensiveness. Readability and actual use matter more than coverage.

### Group by week or topic

Residents need to know what to read when, not just what's relevant.

### Prioritize each item

- **Required** — must read
- **Strongly Recommended** — read if you have time
- **Optional Deep Dive** — for residents who want more

### Mix of types

- 1-2 foundational textbook chapters
- 2-3 high-yield review articles (recent)
- 1-2 landmark papers (older, still cited)
- 1-2 current guidelines
- 1 piece of historical context (older paper explaining why the field thinks as it does)

### Per item

- Full citation (verified)
- One-sentence rationale (why on the list — what gap does it fill?)
- Approximate reading time
- One question the resident should be able to answer after reading

### Bonus

The 2 items the resident should read in the first 48 hours.

## Hard rules

- **VERIFY EVERY CITATION.** Real titles, real authors, real journals, real years.
- **Mark `[VERIFY]` for any citation you're not certain of** — better to flag than fabricate.
- **8-15 items, not more.** Cut if you exceed.
- **Reading times are realistic.** 30-page review is 60-90 min, not 20.

## What I will NOT accept

- Fabricated citations
- More than 15 items
- Aspirational reading times
- Generic rationales ("important to know")
```

## Expected output

A prioritized list grouped by week/topic, with citations, rationales, times, check-questions, plus first-48-hour highlights.

## Required human verification

- **VERIFY EVERY CITATION.** Search PubMed for each paper title. Confirm authors and year match.
- Have an attending in the subspecialty review and prune.
- Update annually as new key papers emerge.

## Best model and why

**Claude Opus 4.7** — curation requires judgment about landmark vs current. But VERIFY citations regardless of model — hallucinated paper titles are common across all models.
