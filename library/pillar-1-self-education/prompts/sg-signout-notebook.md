---
title: Build a sign-out preview notebook
pillar: self-education
event_type: rotation
audience: resident
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: source-grounded, sign-out, rotation, notebooklm, claude-projects
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Sets up a subspecialty-specific notebook for the rotation you're on right now. Becomes your "preview before sign-out" tool — you load yesterday's cases mentally, the notebook helps you anticipate today's sign-out questions, grounded in the actual literature your service uses.

## When to use it

The first week of a new subspecialty rotation, especially if you'll be on the service for 4+ weeks. Worth the upfront investment because the notebook gets used daily.

**Not for:** short rotations (less than 2 weeks — not worth setup), services where you don't have a clear reference set (build the reference list first), or when your attending uses their own teaching approach that doesn't map to literature.

## The setup

```
SIGN-OUT PREVIEW NOTEBOOK SETUP

## Phase 1: Curate the rotation-specific corpus

For your specific rotation, gather:

- **The 2-3 most-used reference chapters** for this subspecialty (ask the senior
  resident or the fellow — they know what gets pulled at sign-out)
- **Your attendings' published papers** (if relevant to the rotation)
- **Institutional protocols** for the workflows you'll encounter daily
  (with appropriate verification that uploading is OK — see privacy guide)
- **Last year's RISE blueprint topics** for this subspecialty (gives you
  exam-aligned scope)
- **The 3-5 most recent landmark papers** in the subspecialty
- **Your own notes** from didactics and prior rotations

Aim for 8-15 documents. Smaller than a board notebook because your scope is
narrower (one subspecialty for ~4 weeks).

## Phase 2: Add a "what attendings emphasize" companion doc

Create a short doc YOU write that captures:
- "Dr. X always asks about [specific feature] before signing out [case type]"
- "On this service, the workup for [presentation] follows this sequence"
- "The discriminating question for [common differential] is [feature]"

Add this to the notebook. It's the institution-specific layer the public
literature can't supply.

## Phase 3: Daily use pattern

End of each day, before tomorrow:
1. Pull up the notebook
2. Tell it: "Tomorrow I have a [case type] coming up. What should I review
   from the uploaded sources? Give me 3 questions to think about overnight."
3. Read the 1-2 most relevant sections it surfaces
4. Sleep on the questions

Beginning of each day:
1. "Quiz me on yesterday's [topic] in 5 questions, one at a time, from the
   uploaded sources. Don't reveal answers until I commit."
2. 5-10 min before sign-out

## Phase 4: Add to the notebook as you learn

When you encounter a teaching point at sign-out that's not in your corpus,
add it:
- Write a 2-3 sentence note about the teaching point
- Cite the case (de-identified) that illustrated it
- Add the source if your attending mentioned one

This is what makes the notebook valuable over weeks: it accumulates the
specific learning of YOUR rotation, not generic content.

## Phase 5: Archive at end of rotation

Last day of the rotation:
- Add a "what I learned this rotation" summary doc to the notebook
- Save the notebook
- Don't delete — useful when you rotate back, useful for board prep, useful
  if you go into this subspecialty for fellowship
```

## Expected output

A working notebook that becomes your daily preview tool. Should take ~2 hours to set up in week 1; pays off across the remaining weeks of the rotation.

## Common failure modes

- **Spending more time on the notebook than studying** — the notebook is a tool, not the work.
- **Forgetting to add to the notebook** as you learn. Without continuous updates, it stales.
- **Including content you don't have institutional permission to upload.** Read the privacy guide first.
- **Treating the notebook output as authoritative** at sign-out. It's prep; the case is the work.

## Required human verification

- **Verify any uploaded institutional document is OK to upload.** When in doubt, ask your PD or your institutional IT/compliance office.
- **Cross-check the notebook's answers** against the actual source at least once per week. Grounding drift is silent.
- **Your attendings' actual sign-out preferences may differ from the notebook's prediction.** The notebook is a starting hypothesis, not a verdict.

## Best model and why

**Claude Sonnet 4.6 via Claude Projects** for the conversational drill pattern + institutional notes. **NotebookLM** if you want tighter grounding and don't need the conversational flexibility.
