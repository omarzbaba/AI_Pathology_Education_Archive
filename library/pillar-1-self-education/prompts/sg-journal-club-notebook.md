---
title: Build a journal club notebook
pillar: self-education
event_type: conference
audience: resident
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: source-grounded, journal-club, notebooklm, claude-projects, literature
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-18
---

## What this prompt does

Sets up a journal-club-specific notebook containing the paper you're presenting plus 5-10 related papers, so you can discuss your paper in deep context — citing prior literature, naming contradictions, anticipating questions grounded in the cited work.

## When to use it

When you're presenting at journal club and want to engage the paper at the depth a careful discussant would. Especially valuable for high-stakes presentations (specialty journal club, society meeting, board prep).

**Not for:** casual journal club where the paper is the entire scope, generating the basic summary (use [Paper summarization](library.html#/library/pillar-1-self-education/prompts/paper-summarization) prompt instead), or papers you haven't actually read (the notebook can't substitute for engagement with the primary source).

## The setup

```
JOURNAL CLUB NOTEBOOK SETUP

## Phase 1: Acquire the corpus

1. **The paper itself** (PDF or full text). Confirm you have legitimate access.
2. **The 3-5 most-cited papers from this paper's references.** Look at the
   discussion section — which references do the authors lean on most?
3. **The 2-3 papers that contradict or complicate this paper's findings**
   (search for review articles or recent papers that cite this one critically).
4. **The relevant guideline** that addresses this clinical question
   (NCCN, ASH, society-specific).
5. **Any major prior trial** that this paper builds on or replaces.

Aim for 6-10 documents in the notebook.

## Phase 2: Verify access and provenance

- All papers should be ones you have legitimate access to (institutional
  subscription, open access, your own copies). Do not upload pirated PDFs.
- For institutional protocols or unpublished material, verify upload is OK.

## Phase 3: Initial deep read

Before you ask the notebook anything, read the primary paper yourself.
The notebook is a thinking partner, not a substitute for reading.

## Phase 4: Use the notebook for these specific drills

After your own read, ask the notebook:

1. "Based on the uploaded sources, what's the state of this field BEFORE
   this paper? What was contested, and where did this paper land in that
   debate?"

2. "Where do the uploaded sources DISAGREE with this paper's findings or
   interpretation? Be specific about which source and which point."

3. "What's the most likely critical question someone with [perspective X
   — e.g., 'a hematologist skeptical of this drug class'] would raise
   from the uploaded sources?"

4. "Generate 5 discussion questions for journal club that REQUIRE engaging
   with the broader literature in the notebook, not just the primary paper."

5. "If this paper is wrong about [specific claim], which uploaded source
   would be the strongest counterargument?"

## Phase 5: Pressure-test the notebook's responses

For each notebook response that you'll use in your presentation:
1. Open the cited source
2. Verify the claim is actually in that source as described
3. Check the citation isn't out of context

Notebooks confabulate. Verification is non-optional for journal club.

## Phase 6: Save the notebook for future reference

Even after journal club is over, this notebook becomes useful for:
- Re-presenting if you go to a society meeting
- Citing in a manuscript that touches the same question
- A board-prep reference set on this topic
```

## Expected output

A working notebook you can use to prepare a deep journal club presentation grounded in the actual literature, with verified citations.

## Common failure modes

- **Treating the notebook as a substitute for reading the paper.** It isn't.
- **Confabulated citations.** The model may say "as Smith et al. 2021 demonstrated..." with details that aren't in the actual Smith paper. Verify.
- **Over-relying on the related papers** — the discussion should center the primary paper, not become a literature review.
- **Uploading papers you don't have legitimate access to.** Pirated PDFs in an AI notebook is a copyright and ethics issue.

## Required human verification

- **Verify every citation** the notebook produces before using it in the presentation.
- **Verify the related papers are correctly characterized** — the notebook may misrepresent a paper's argument.
- **Read the primary paper yourself.** Notebook-mediated familiarity is shallow.

## Best model and why

**Claude Opus 4.7 via Claude Projects with the paper PDFs attached** for substantive engagement with literature. **NotebookLM** is a strong alternative when citation linking matters. Generic chat with pasted excerpts works for quick checks but loses the cross-source comparison value.
