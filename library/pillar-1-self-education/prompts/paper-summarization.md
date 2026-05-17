---
title: Paper summarization
pillar: self-education
event_type: n/a
audience: resident
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: literature, summarization
verified_models: TODO
best_model: Gemini 2.5 Pro
last_updated: 2026-05-17
---

## What this prompt does

Generate a structured summary of a paper covering question, design, findings, limitations, and what would change practice. The structure matters because it forces the model to address all five — not just the conclusion.

## When to use it

When you have a paper to read and only 10 minutes. Use the summary as a triage tool: decide whether to read the full paper, scan key sections, or move on.

## The prompt

```
Summarize this paper for a [PGY level] pathology resident. I have [N] minutes.

Use this structure:

1. **The question** (1 sentence): what gap in the literature does this paper address?
2. **The design** (2-3 sentences): study type, population, comparison, key methods. Be specific enough that I could critique the design without reading the paper.
3. **The headline finding** (1-2 sentences): the main result and its effect size.
4. **The most important limitation** (1-2 sentences): the limitation that most constrains the generalizability of the findings.
5. **Would this change practice?** (1-2 sentences): if yes, in what specific setting; if no, why not.
6. **Three questions** I should be prepared to answer if my attending asks about this paper.

If you don't know the specific paper, tell me — do not summarize from the title alone.

Paper: [paste DOI, citation, or the full text if you have it]

**Important — refinement:** If you do not have direct access to the actual paper text (not just the title or abstract), say so explicitly at the top and refuse to summarize. Hallucinated paper summaries are the most common failure mode for this prompt and the most damaging — never bluff.
```

## Expected output

The six-section summary in the order above. Total length ~250-400 words. The three attending questions should be specific enough that you can prep answers in 10 minutes.

## Common failure modes

- The model summarizes from the title alone when it doesn't have the paper. Push back: 'do you actually have access to the paper text?'
- The 'most important limitation' is generic ('small sample size' when n=2,000). Push back for specific.
- The 'would this change practice?' is non-committal. Push for a specific answer.

## Required human verification

- **Critical:** verify the headline finding and effect size against the actual paper. The model frequently misremembers numbers from papers it has 'seen'.
- If the model invents a citation, that's a hallucination — discard the entire summary.
- Confirm the three attending questions are actually answerable from the paper.

## Best model and why

**Gemini 2.5 Pro** — Best for papers attached as PDFs — Gemini's long-context handling of full-text PDFs is the strongest option. If working from pasted text only, Claude Opus 4.7 is comparable. Avoid models without document attachment if the paper is long.
