---
title: ACGME / EPA learning objective generation
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: learning-objectives, acgme, epa
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Generate ACGME-milestone-aligned or EPA-mapped learning objectives for a teaching session on a given topic.

## When to use it

When you're designing a new teaching session and need to write objectives that will pass review by your CCC or program leadership.

## The prompt

```
Generate [N] learning objectives for a [duration]-minute teaching session on [topic] for [audience — e.g., 'PGY-2 CP residents in their second month of blood bank'].

Each objective should:

1. Begin with 'By the end of this session, the resident will...' followed by a measurable verb (interpret, distinguish, formulate, justify — NOT 'understand' or 'know').
2. Specify the **condition** under which the behavior occurs (given a case, given a set of lab values, etc.).
3. Specify the **criterion** for success (with what accuracy, citing which guideline, etc.).
4. Map to a specific **ACGME milestone sub-competency** (e.g., 'PC1.3 Interpretation of Diagnostic Studies') or **EPA** (if your program uses EPAs).

After the objectives, identify which milestones are NOT addressed by these objectives — useful context for the program director.
```

## Expected output

N objectives in proper format with explicit condition + behavior + criterion + milestone/EPA mapping, plus a note on milestones not covered.

## Common failure modes

- Objectives use 'understand' or 'know' instead of measurable verbs.
- The milestone mapping is approximate or invented. Verify against your program's actual milestone document.
- Criteria are too vague ('correctly') to be assessed.

## Required human verification

- Verify the milestone or EPA mapping against your program's official document. ACGME milestones are revised periodically; the model may reference an older version.
- Run the objectives by your program director or CCC chair before using them in a formally documented session.
