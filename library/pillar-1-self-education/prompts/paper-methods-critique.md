---
title: Paper methods critique
pillar: self-education
event_type: n/a
audience: resident
difficulty: advanced
time_to_use: 2-10min
visual: text-only
tags: literature, critical-appraisal, methods
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generates a structured methodology critique using the appropriate reporting guideline as the framework (CONSORT for RCTs, STROBE for observational, STARD for diagnostic accuracy, PRISMA for systematic reviews, TRIPOD for prediction models). The output is checklist-style and item-by-item, not impressionistic — which is exactly what reviewers and journal club discussants need.

## When to use it

Preparing for journal club presentation, peer-reviewing a manuscript, writing a critical letter, or studying critical appraisal skills. The structured framework forces engagement with the *design* choices rather than the *result*.

**Not for:** paper summarization (use the dedicated prompt), questions about clinical significance (separate skill), or analyzing your own work without a colleague's review (the model isn't an independent reviewer).

## The prompt

```
You are critiquing the methods section of a paper, item-by-item against the appropriate reporting guideline. Be specific, be honest, and source your critique points to the actual paper text. A vague critique that could apply to any paper is useless.

## Honesty check first

Do you have access to the full methods section of this paper? Confirm explicitly. If you don't have the methods section (or only have the abstract), STOP and tell me — do not critique what you cannot read.

## What I'm requesting

- **Paper:** [DOI, citation, attached PDF, or pasted methods section]
- **Study type:** [one of: RCT, retrospective cohort, prospective cohort, case-control, diagnostic accuracy, systematic review, meta-analysis, prediction model, qualitative study, other (name it)]
- **Reporting guideline framework I want you to use:**
  - RCT → CONSORT 2010 (+ relevant extensions)
  - Observational study → STROBE
  - Diagnostic accuracy → STARD 2015
  - Systematic review/meta-analysis → PRISMA 2020
  - Prediction model → TRIPOD 2024
  - Qualitative → COREQ or SRQR
  - Other → [name the guideline you want me to use]
- **My critique purpose:** [journal club presentation / peer review / personal study / writing a letter]

## What to produce — item-by-item

### Part 1: The checklist

For each major reporting guideline item, mark:
- **Adequate** — the paper addresses this item clearly and completely
- **Partial** — the paper addresses it but with gaps
- **Not addressed** — the paper is silent on this item
- **Not applicable** — the item doesn't apply to this study design (justify)

For each item, quote or paraphrase the relevant text from the paper where applicable. If the paper doesn't address an item, say what would have been needed.

### Part 2: The three most consequential gaps

Beyond the checklist, identify the **3 gaps a peer reviewer would flag**. For each:
- What the gap is
- Why it matters (how it constrains the paper's interpretability)
- What the authors should have done

### Part 3: The single most constraining design choice

Of all the design choices the authors made, identify the ONE that most constrains the paper's interpretability. This is different from "the most criticizable" — it's the choice that, if it had been different, would most have improved the paper. Suggest the specific alternative.

### Part 4: What the authors got right

Critique should not be uniformly negative. Identify 1-2 design choices the authors made that demonstrate methodological care or thoughtfulness. Specific, not generic.

### Part 5: Calibration disclosure

Acknowledge any uncertainty about whether the guideline version you used is current. Reporting guidelines update; if you're not sure whether you're using the latest version (e.g., CONSORT 2025 if released), say so explicitly so I can verify against the current source.

## Hard rules

- **Critique must be specific.** "Sample size could be larger" is not a critique. "Sample size of 47 yields 0.6 power to detect the pre-specified effect size, which the authors do not address" is.
- **Quote or paraphrase from the actual paper** rather than imagining what the methods might have said.
- **Do not invent guideline items.** If you're not sure what the current CONSORT items are, say so.
- **The constraining design choice in Part 3 must be feasible to have done differently.** "They should have done an RCT" is not a useful critique if the topic doesn't permit one.
- **Do not pad with peripheral critique** if the methods are largely sound. A paper with strong methods deserves a critique that says so.

## What I will NOT accept

- Vague critique that could apply to any paper
- Critique fabricated for a paper you don't actually have
- "More research is needed" as a critique
- Critique that ignores Part 4 (what they got right)
```

## Expected output

A checklist with adequacy ratings + the three consequential gaps + the most constraining design choice with alternative + 1-2 strengths + a calibration note about the guideline version. Length: 500-800 words for a typical paper.

## Common failure modes

- **Generic critique** that could apply to any paper. Push back: "Be more specific. What specifically in this paper's methods?"
- **Critique fabricated for a paper the model doesn't have.** The honesty check at top is designed to prevent this, but verify before trusting.
- **Guideline version uncertainty hidden.** If the model isn't sure whether it's using CONSORT 2010 or 2025, push for explicit acknowledgment.
- **All-negative critique** that ignores what the authors did well. Push for Part 4.

## Required human verification

- **Verify the critique against the actual methods section.** Quotes the model attributes to the paper need to be checked.
- **Verify the reporting guideline version is current.** Guidelines update; the model may reference an older version.
- **For a critique you'll present publicly** (journal club, peer review, letter), have a methodologist colleague pressure-test the critique before relying on it. There's no substitute for human review on methodologic critique.

## Best model and why

**Claude Opus 4.7** — methods critique requires applying named reporting guidelines with precision and resisting the temptation to be vaguely negative. Opus is materially more disciplined about specificity and about acknowledging what's done well. **Avoid Sonnet** for high-stakes critique (peer review, public presentation) — it produces critique that sounds plausible but is often generic.
