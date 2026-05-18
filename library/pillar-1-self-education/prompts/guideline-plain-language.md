---
title: Guideline plain-language translation
pillar: self-education
event_type: n/a
audience: resident
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: guidelines, plain-language
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Translates published guideline recommendations into plain language at a target reading level while **preserving every qualifier, conditional, and strength-of-recommendation grade exactly**. The output is suitable for briefing a non-specialist colleague, preparing a patient handout, or summarizing for a tumor board.

The hardest part of guideline translation is *not* simplifying the vocabulary — it's resisting the temptation to collapse "consider X in selected patients with Y" into "do X for Y." This prompt enforces preservation.

## When to use it

When you need to brief a non-specialist (an internist, a patient, a new resident) on a guideline you know well. Also useful before tumor board where you'll need to summarize a recommendation succinctly without distortion.

**Not for:** generating your own guideline interpretation (use the underlying evidence), translating clinical decisions (this is for educational/communication framing only), or anything that would be used for direct patient care decisions without your verification.

## The prompt

```
You are translating guideline recommendations into plain language. Your job is to preserve meaning — every qualifier, conditional, and recommendation grade — while making the language accessible. Translation is not simplification; conditional language stays conditional.

## What I'm pasting

- **Source guideline (name, version, year):** [e.g., "NCCN Acute Myeloid Leukemia v2.2024"]
- **Specific recommendations to translate:** [paste the verbatim recommendation text]
- **Target audience:** [e.g., "first-year medical student", "practicing internist", "patient at 8th-grade reading level"]
- **Use case:** [briefing, handout, tumor board summary, etc.]

## For each recommendation, produce

1. **Plain-language statement in ONE sentence.** Use vocabulary appropriate to the target audience. If a technical term is unavoidable, define it inline.
2. **Preserved grade and evidence quality.** Include the original strength of recommendation (Strong / Conditional / etc.) and quality of evidence (High / Moderate / Low / Very Low). DO NOT smooth these over.
3. **Preserved qualifiers verbatim or as close as possible.** "In selected patients", "when available", "if feasible", "consider", "may be appropriate" — these all stay. Do not collapse conditional language into directives.
4. **One-sentence "why this matters" line.** What changes about practice based on this recommendation? Frame this from the perspective of the target audience.

## Hard rules

- **No collapsing conditionals.** "Consider X" never becomes "Do X". "May be appropriate" never becomes "Is appropriate".
- **No strengthening or weakening.** A conditional recommendation stays conditional in the translation.
- **Preserve population restrictions.** "In patients with Y" cannot become "All patients".
- **Inline term translations must be accurate.** "MGUS — a small abnormal antibody in the blood that doesn't yet require treatment" is OK. "MGUS — early cancer" is wrong (changes meaning).
- **If you're uncertain about the meaning of a specific phrase in the original,** flag it `[VERIFY]` rather than guessing.

## What I will NOT accept

- Translations that change the strength of the recommendation
- Inline term definitions that introduce inaccuracy
- "Why this matters" lines that add editorial content the guideline didn't say
- Loss of population restrictions ("in patients with renal impairment")
```

## Expected output

Per recommendation: one-sentence plain translation, preserved grade + evidence quality, preserved qualifiers, one "why this matters" line. Length depends on number of recommendations.

## Common failure modes

- **Model strengthens or weakens during translation.** This is the #1 failure mode. Always cross-check against the original.
- **Inline term translation distorts the term** (e.g., translating MGUS as "cancer").
- **"Why this matters" line adds claims the guideline didn't make.** Push back: "Cite where in the guideline that 'why' comes from."

## Required human verification

- Cross-check every translated recommendation against the original guideline text — particularly the strength of recommendation and conditional language.
- Verify inline term translations against an authoritative source for the target reading level.
- If using for a patient handout or formal document, have a colleague verify before distribution.

## Best model and why

**Claude Sonnet 4.6** — preserves conditional language better than smaller models or competitors. **Avoid GPT-4o** for this prompt; it tends to flatten qualifiers into directives, which is the failure mode that matters most here.
