---
title: Resident-as-teacher scaffolding
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: rat, teaching-skills
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Scaffold a resident-as-teacher session: how would you teach this topic to a junior resident, what are the common misconceptions, what is the one slide you would build.

## When to use it

When a senior resident is asked to give a teaching session and needs a structured way to think about teaching, not just content delivery.

## The prompt

```
I'm a [PGY level] resident asked to give a [duration]-minute teaching session on [topic] to [audience — e.g., 'incoming PGY-1s in their first week of CP'].

Help me think through this as a teaching exercise, not just a content delivery exercise.

1. **What is the ONE concept I most want them to walk away with?** State it in one sentence.
2. **What are the 2-3 common misconceptions** about this topic that I should anticipate and address?
3. **If I had only ONE slide, what would it show?** Describe the visual or text in detail.
4. **What is the simplest exercise** I could do in the session that would let me see whether they understood the one concept?
5. **What's the question I should NOT try to answer in this session** — the related topic that would be a different talk?
6. **How will I know if the session went well?** Give me 2-3 observable indicators during or right after the session.
```

## Expected output

The six answers in order, with the 'one concept' and the 'one slide' being the centerpieces. The exercise should be doable in the time you have.

## Common failure modes

- The 'one concept' is too broad to fit in one sentence.
- The misconceptions are generic.
- The 'one slide' is bullet points rather than something genuinely teachable.

## Required human verification

- Run the 'one concept' by a colleague at the target level: does it land?
- The misconceptions list is most useful when validated by an attending who has taught this topic — they know which misconceptions are real.
- The 'observable indicators' should be specific enough that you can actually check them after the session.
