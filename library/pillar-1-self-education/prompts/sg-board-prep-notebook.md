---
title: Build a board prep notebook
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: source-grounded, board-prep, notebooklm, claude-projects
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Step-by-step setup for a board prep notebook (NotebookLM or Claude Projects) that becomes your study companion for the months leading up to RISE, ABPath, or in-service exams. The key idea: stop pasting the same source material into every prompt; build a notebook that knows your curriculum and stays grounded in it.

## When to use it

At the start of dedicated board prep (8-16 weeks out), or when you've been pasting the same sources repeatedly and realize a notebook would save time.

**Not for:** quick one-off study (use generic chat), exam prep where the source material is constantly changing (the notebook becomes stale), or when you don't have time to curate sources (curation IS the work).

## The setup — six phases

```
BOARD PREP NOTEBOOK SETUP (NotebookLM or Claude Projects)

## Phase 1: Decide your scope

Pick ONE of these scope patterns:

A. **Full-board notebook** (e.g., one notebook covering CP, one covering AP)
   - Pros: single source of truth, comprehensive
   - Cons: huge corpus, harder to keep focused, slower retrieval

B. **Subspecialty notebooks** (e.g., separate notebooks for heme, chem, blood
   bank, micro)
   - Pros: focused, faster retrieval, easier to update
   - Cons: more setup, switching between notebooks

C. **Topic notebooks** (e.g., separate notebooks for "plasma cell neoplasms",
   "anemia workup", "TMA")
   - Pros: surgically focused on weak topics
   - Cons: many notebooks to manage

RECOMMENDATION: Start with B (subspecialty notebooks). Most board prep is
naturally organized by subspecialty, and it keeps each notebook to a
manageable corpus.

## Phase 2: Curate sources for ONE notebook

For your first notebook (start with your weakest subspecialty):

- **2-4 foundational chapters** from your primary reference (e.g., Henry's,
  Robbins, McPherson)
- **2-3 high-yield review articles** (recent — within last 5 years)
- **1-2 current guidelines** relevant to the subspecialty
- **Your own annotated notes from the rotation** (typed or scanned with OCR)
- **NOT:** old qbank questions verbatim (you want to test against, not
  contaminate the source)
- **NOT:** copyrighted material you don't have legitimate access to
  (see the privacy guide)

Aim for 10-25 documents total. More than 30 dilutes retrieval; fewer than 10
limits coverage.

## Phase 3: Upload and verify grounding

After uploading:

1. Ask a question you KNOW the answer to from the source: "What's the WHO
   classification of [entity X]?"
2. Check the response cites the actual uploaded source (NotebookLM shows
   citations explicitly; Claude Projects you have to ask)
3. Ask a question that's NOT in your source: "What's the latest 2027
   guideline update?" — the model should say "not in my sources" rather
   than confabulating from general knowledge.
4. If the model hallucinates outside the source, the grounding is weak.
   Re-evaluate your tool choice.

## Phase 4: Use it for active retrieval

Don't use the notebook as a search engine. Use it for ACTIVE RETRIEVAL:
- "Quiz me on plasma cell disorders, one question at a time, based ONLY on
  the uploaded sources. Don't reveal the answer until I commit."
- "Generate 5 MCQs based on the uploaded sources, with the source citation
  for each answer."
- "Compare the WHO criteria for X vs Y as described in the uploaded
  sources. Note any discrepancies between sources."

The notebook's value is that the questions and answers are GROUNDED in YOUR
study material, not the model's general knowledge.

## Phase 5: Update the notebook monthly

Board prep evolves. Every month:
- Add 1-2 new high-yield papers as they come out
- Remove sources that turned out to be redundant
- Re-evaluate scope (is the notebook getting too big? too narrow?)

## Phase 6: Plan for end-of-prep

The notebook is a study tool, not a permanent reference. After the exam:
- Save the notebook in archive mode
- Don't delete — useful if you re-take or want to review
- Re-evaluate for fellowship/practice use (different scope)
```

## Expected output

A working notebook you can drill against for weeks of board prep, with sources you trust and grounding you've verified.

## Common failure modes

- **Over-curating the corpus.** Spending 4 hours selecting "perfect" sources before doing any actual studying. The corpus should be good-enough; iterate.
- **Treating the notebook as a search engine.** It's a drill partner. Use it for active retrieval, not passive reading.
- **Forgetting to verify grounding** after uploads. The model may sound authoritative while drifting outside your sources.
- **Mixing copyrighted material you don't have legitimate access to.** Personal study fair-use is murky; institutional uploads can be problematic.

## Required human verification

- **Verify grounding monthly** with a known-answer probe question. Drift happens silently.
- **Cross-check at least one answer per session** against the original source. The model occasionally paraphrases in ways that change meaning.
- **For any answer that surprises you,** open the source and verify directly before incorporating into your mental model.

## Best model and why

For **board prep specifically: NotebookLM is currently the strongest** because its grounding is tighter (refuses to answer outside sources more reliably) and citations are surfaced explicitly. **Claude Projects (Sonnet 4.6 underlying)** is a strong alternative if you want broader reasoning capability alongside grounding. Generic chat with pasted sources works for casual review but loses persistence.
