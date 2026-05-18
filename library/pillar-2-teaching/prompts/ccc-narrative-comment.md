---
title: CCC narrative comment drafting
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: ccc, narrative, milestone-evidence, high-stakes
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Converts your bullet observations into a CCC narrative comment that defensibly maps evidence to milestone level. Strict discipline about not inflating beyond the evidence you provided — if your evidence supports level 3 but you've assigned level 4, the prompt flags the inconsistency before drafting.

CCC narratives are read by external reviewers (ACGME visits, fellowship directors reviewing applicants) cold, without context. The narrative must make sense alone.

## When to use it

Writing CCC narratives at semi-annual reviews. Especially valuable for residents you know well but for whom you don't have well-organized notes — the prompt forces evidence-to-claim mapping that you might gloss over otherwise.

**Not for:** routine end-of-rotation feedback (use [Resident feedback note drafting](library.html#/library/pillar-2-teaching/prompts/resident-feedback-note)), evaluations that go directly to the resident (different audience), or replacing your CCC chair's review.

## The prompt

```
You are drafting a CCC narrative comment that must defensibly map evidence to milestone level. Be conservative about inflation. If my evidence doesn't support my assigned level, flag the inconsistency BEFORE drafting.

## What I'm providing

- **Resident initial + PGY:** [e.g., "Resident JD, PGY-3"]
- **Milestone sub-competency:** [e.g., "PC1.3 Interpretation of Diagnostic Studies"]
- **Milestone level I'm assigning:** [e.g., "Level 3 / Level 4 in transition"]
- **Trajectory:** [progressed / plateaued / regressed since last review]
- **Evidence / observations from this review period:**
  [paste bullets — specific behaviors I observed, with case context where useful]
- **Comparison to peers (optional):** [where this resident sits relative to PGY-3 cohort]

## Inconsistency check FIRST

Before drafting, evaluate whether my evidence actually supports my assigned level. If the evidence describes Level 3 behaviors and I've assigned Level 4, OR if the evidence describes Level 4 behaviors and I've assigned Level 3, STOP and tell me. Don't draft until we resolve the inconsistency.

## Narrative structure (4 sentences total)

1. **Level + trajectory sentence:** "Resident JD demonstrates Level [N] performance for [milestone], having [progressed from / maintained / partially regressed from] the prior review."

2. **2-3 sentences of behavioral evidence:** Specific behaviors I observed. Each behavior tied to a case or context (anonymized). Avoid generic language like "demonstrates competence" — use the actual behaviors.

3. **Next milestone behavior sentence:** What is the resident approaching or working toward at the next level? Specific.

4. **Forward-looking expectation sentence:** A specific expectation for the next 6 months.

## Tone and audience

The narrative will be read by an external reviewer (ACGME visit, fellowship director reviewing this resident's application later) cold, without context. It must:
- Make sense as a standalone paragraph
- Use the resident initial + PGY format consistently
- Be factual and evidence-based, not effusive
- Be defensible if challenged

## Hard rules

- **Do NOT inflate beyond evidence.** If evidence supports Level 3, don't draft Level 4.
- **Every behavioral claim must trace to a bullet I provided.** If you can't trace it, you're inventing.
- **Use specific behaviors, not generic praise.** "Demonstrated independent interpretation of routine cases with appropriate escalation of complex cases" is good; "demonstrated competence" is not.
- **Match the trajectory language to the evidence.** "Progressed" requires evidence of progression.

## What I will NOT accept

- Narrative that goes beyond my evidence
- Generic competence statements
- Inflated language ("exceptional," "outstanding") without behavioral evidence
- Trajectory claims without evidence
```

## Expected output

A 4-sentence narrative comment defensibly mapping evidence to milestone level, with forward-looking expectation. Length ~80-120 words.

## Common failure modes

- **Inflation.** The model wants to be generous; resist it.
- **Generic praise.** Push back: "What specifically did the resident do?"
- **Trajectory claims without evidence.** Push back.

## Required human verification

- Re-read against your bullets — every claim should trace to one.
- Have a colleague on the CCC read for consistency with their style.
- Verify the milestone level descriptors against your program's current milestone document — these get revised.

## Best model and why

**Claude Opus 4.7** — tight evidence-to-claim mapping and defensible level assignment reward Opus's depth. Sonnet narratives tend toward generic competence language; Opus is more disciplined about specificity.
