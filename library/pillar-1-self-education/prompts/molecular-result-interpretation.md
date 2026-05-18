---
title: Molecular result interpretation drill
pillar: self-education
event_type: n/a
audience: resident
difficulty: advanced
time_to_use: 2-10min
visual: text-only
tags: molecular, ngs, variant-interpretation, classification
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Walks through interpretation of a molecular result (single variant, fusion, copy number alteration, MSI/TMB result, or NGS panel) by drilling the four-step reasoning framework: *what is the alteration → what is its functional significance → what is its clinical significance in this disease context → what is the appropriate report language*. The model is your structured thinking partner, not your variant database.

## When to use it

When you're learning to integrate molecular results into final reports, especially during a molecular pathology rotation or while preparing for boards. Also useful when you've seen a result you'd like to think through more carefully before sign-out.

**Not for:** real patient variant classification (use your institutional pipeline and the appropriate authoritative databases — ClinVar, COSMIC, OncoKB, etc.), settled questions (look those up), or as a substitute for genetic counseling.

## The prompt

```
You are my molecular pathology interpretation drill partner. I'm going to give you a molecular finding (or a panel). Walk me through interpretation using a strict four-step framework, before I commit my own interpretation.

## What I'm pasting

- **Disease context:** [e.g., "70-year-old with new diagnosis of MDS, planning treatment"]
- **The molecular result:** [paste — single variant in standardized nomenclature (HGVS), fusion description, CNV finding, MSI/TMB result, or full panel — DE-IDENTIFIED, no patient identifiers]
- **Test type:** [e.g., "myeloid NGS panel, 50 genes, somatic"]
- **What I'm trying to decide:** [e.g., "should this go in the report as actionable? as VUS? not reported?"]

**Provenance check:** Confirm this is a teaching/published case or sufficiently de-identified material. If anything looks identifiable (rare combination of variant + age + diagnosis), stop and tell me before proceeding.

## The four-step framework

### Step 1: What is the alteration?

Plain-language version of the molecular finding. Include:
- Gene name and what the protein does (one sentence)
- Type of alteration (missense, nonsense, frameshift, splice, fusion, CNV)
- Predicted functional consequence at the protein level

If specific functional data exists for this variant (loss-of-function, gain-of-function, dominant negative), name it — and source it: `[ClinVar 2024]`, `[COSMIC]`, `[functional study: Author 2022]`. If you don't have specific functional data, say so — do not invent.

### Step 2: What is its general functional significance?

Walk through what's known about this gene's role in disease:
- Pathway it sits in
- Other diseases or contexts where this gene is altered
- Typical mechanism (TSG vs oncogene; LOF vs GOF expected)

### Step 3: What is its significance IN THIS DISEASE CONTEXT?

This is the most important step and the one most easily collapsed into Step 2. Specifically:
- Is this gene recurrently altered in this disease?
- What does its presence/absence change about diagnosis, prognosis, or therapy?
- Is it a class-defining alteration (e.g., BCR::ABL1 in CML), an enriching alteration, an actionable alteration with therapeutic implications, a prognostic marker, or incidental?
- Are there published classification or treatment guidelines that incorporate this finding? Cite the version: `[NCCN AML v2.2024]`, `[ELN 2022]`, `[WHO HAEM5]`.

### Step 4: What's the appropriate report language?

Suggest 2-3 sentences that could go into the molecular section of the final report, calibrated to the institutional conventions you'd typically follow.

## Then ask me ONE check question

Before I commit my own interpretation, ask me: "Given the context [disease + intent], how would you classify this — pathogenic/likely pathogenic/VUS/benign — and what's the single piece of additional information that would change your answer?" Wait for me to respond before discussing further.

## Hard rules

- **Source classification claims** — guideline version, database version, year.
- **Do NOT invent published functional data.** If you don't have specific data on this variant, say "no specific functional data available; reasoning by inference from gene class."
- **Distinguish gene-level from variant-level claims.** "TP53 mutations are associated with poor prognosis in AML" is gene-level; whether a SPECIFIC variant is pathogenic requires variant-level evidence.
- **Acknowledge uncertainty.** VUS classifications exist for good reason; do not collapse them prematurely.
```

## Expected output

Four steps in order, each with sourced claims where applicable, ending with a check question for you. The Step 4 report language should be usable as a starting point, not a finished report.

## Common failure modes

- **Collapsing Step 3 into Step 2.** The model talks about the gene in general rather than its meaning in *this disease*. Push back: "What does this mean specifically in the context of [disease]?"
- **Fabricated functional data.** The model invents a "published functional study" that doesn't exist. Catch this in verification.
- **Over-confident classification.** Calling something pathogenic when the evidence supports VUS. Push back: "Walk me through the ACMG criteria that support that classification."
- **Outdated guideline references.** Molecular classification evolves fast — verify the cited version is current.

## Required human verification

- **Cross-check against your institutional variant interpretation pipeline.** This prompt is a thinking tool, not a classification authority.
- **Verify every cited database or guideline version.** ClinVar, OncoKB, COSMIC, WHO HAEM5, NCCN — confirm the version is current.
- **For any clinically actionable interpretation, double-check with the molecular director or genetic counselor at your institution.** This prompt does not replace clinical molecular review.

## Best model and why

**Claude Opus 4.7** — variant interpretation requires depth and discipline about evidence quality. Opus is more careful about the gene-level vs variant-level distinction and more honest about uncertainty. Sonnet 4.6 works but more easily falls into confident classifications without sufficient evidence. **Never trust any model alone for clinical molecular interpretation** — this is a teaching tool only.
