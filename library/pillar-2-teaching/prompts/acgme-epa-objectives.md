---
title: ACGME / EPA learning objective generation
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: learning-objectives, acgme, epa, assessment
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generates learning objectives in the format your CCC and program leadership expect: measurable verbs, conditions, criteria, and an explicit map to a specific ACGME milestone sub-competency or EPA. Also identifies the milestones your objectives do NOT address — useful context for program leadership.

## When to use it

Designing a new teaching session that needs documented objectives, updating a rotation block whose objectives are stale, or preparing materials for a program review where milestone alignment will be scrutinized.

**Not for:** general lesson planning (use slide outline prompt), session design that doesn't need formal milestone mapping, or replacing your program director's review of formal documentation.

## The prompt

```
You are generating learning objectives for a formal pathology training context. Format must be the one CCCs expect: measurable verb + condition + criterion + milestone or EPA mapping.

## What I'm generating objectives for

- **Session or rotation:** [name + duration]
- **Audience:** [exact PGY level + subspecialty rotation context — e.g., "PGY-2 CP residents in their second month of blood bank"]
- **Number of objectives:** [usually 3-7]
- **My program uses:** [ACGME milestones / EPAs / both — name which]
- **The milestone document version I'm working from:** [name + year — e.g., "Pathology Milestones 2.0, 2020 revision"]
- **Topic or content:** [what the session/rotation covers]

## What to produce

For each objective:

```
By the end of this [session / rotation], the [PGY-level] resident will:
[measurable verb] [the specific behavior] [under what conditions] [to what criterion of success], mapping to [milestone sub-competency code or EPA number].
```

### Verb requirements

Use measurable verbs only: interpret, distinguish, formulate, justify, generate, calculate, apply, compare, prioritize, recommend.

NEVER use: understand, know, learn, appreciate, be aware of, recognize (alone), grasp, become familiar with.

### Condition requirements

Each objective must specify the condition under which the behavior occurs:
- "Given a set of lab values..."
- "Given a clinical case..."
- "Given an IHC panel..."
- "In a multidisciplinary sign-out..."

### Criterion requirements

Each objective must specify the criterion for success:
- "With accuracy verified against the [current guideline]"
- "Citing the appropriate WHO classification"
- "Independently, without attending intervention"

### Milestone mapping

Map each objective to a specific milestone sub-competency code (e.g., PC1.3) or EPA. Cite the version of the milestone document you're working from.

### After the objectives

Identify which milestones are NOT addressed by these objectives. Useful context for the CCC and PD — flags whether this session/rotation is over- or under-allocated against the milestone framework.

## Hard rules

- **Measurable verbs only.** No "understand" or "know."
- **Condition and criterion are required for every objective.** Don't omit them to make objectives shorter.
- **Cite the milestone document version.** Milestones get revised; don't refer to outdated codes without flagging.
- **If you're not sure whether a milestone code is current, ASK** rather than guess.
- **The "milestones not addressed" section is non-optional.** It's the most useful part for leadership.

## What I will NOT accept

- Objectives using "understand," "know," or similar non-measurable verbs
- Missing conditions or criteria
- Invented milestone codes
- Verb mismatch with PGY level (PGY-1 objectives requiring "justify" or "formulate" at expert level)
```

## Expected output

3-7 objectives in the required format, plus a list of milestones not addressed. Length depends on number of objectives; typically 300-600 words.

## Common failure modes

- **Non-measurable verbs slipping in.** Push back.
- **Conditions and criteria omitted.** Push back.
- **Invented or outdated milestone codes.** Verify against your current document.

## Required human verification

- Verify every milestone code against your program's current document. ACGME milestones are revised periodically.
- Run objectives by your program director or CCC chair before using in any formally documented context.
- For CME-accredited sessions, additional formatting may be required by your CME office.

## Best model and why

**Claude Sonnet 4.6** — structured objective generation is Sonnet's strength. Verify milestone codes regardless of model; no model is reliably current on milestone documents that have been revised after its training cutoff.
