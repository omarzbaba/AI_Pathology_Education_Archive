---
title: Paper summarization
pillar: self-education
event_type: n/a
audience: resident
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: literature, summarization, triage
verified_models: TODO
best_model: Gemini 2.5 Pro
last_updated: 2026-05-17
---

## What this prompt does

Generates a structured paper summary covering question / design / headline finding / most important limitation / would-this-change-practice / attending Q&A prep — in that order, no skipping. The output is a triage tool: read the full paper, scan it, or skip it.

The dominant failure mode is **summarizing from the title and abstract alone** when the model doesn't actually have the paper. This prompt makes that failure mode hard to commit by requiring an explicit honesty check at the top.

## When to use it

When a paper lands in your inbox or shows up in a journal club packet and you have 10 minutes to decide whether to read it. Also useful as the *first* step before journal club presentation: generate the summary, identify what you can't answer, then go read those specific sections of the paper.

**Not for:** in-depth methodology critique (use the [Paper methods critique](library.html#/library/pillar-1-self-education/prompts/paper-methods-critique) prompt), generating discussion questions (use the [Journal club discussion questions](library.html#/library/pillar-2-teaching/prompts/journal-club-discussion-q) prompt), or as a substitute for actually reading the paper before citing it.

## The prompt

```
You are summarizing a paper for me. Before you produce anything, you must honestly answer a question about what you actually have access to.

## Honesty check — answer first

Do you have access to the full text of this paper, or only the title and abstract (or only the title)? Say so explicitly. If you only have the title or abstract, STOP and tell me — do not summarize. A hallucinated summary is more damaging than no summary.

If I've attached a PDF or pasted the full text, confirm you can read it. If I've given you only a citation, ask whether I want you to proceed with title/abstract only or to wait for me to provide the text.

## What I'm requesting

- **Paper:** [DOI, citation, attached PDF, or pasted full text]
- **My background on this topic:** [e.g., "PGY-3, this is for journal club next week; I've read the related guideline but not other papers in this area"]
- **My time budget:** [e.g., "I have 10 minutes; will read more only if your summary makes the case"]

## The six-part summary (in this order, no skipping)

### 1. The question (1 sentence)

What gap in the literature does this paper address? Not "what did they study" — what was the open question this paper was designed to answer?

### 2. The design (2-3 sentences)

Study type, population, comparison or control, key methods. Be specific enough that I could critique the design without reading the paper. Name the study type with the standard terminology (RCT, retrospective cohort, prospective cohort, case-control, diagnostic accuracy, systematic review, meta-analysis, prediction model, etc.).

### 3. The headline finding (1-2 sentences)

The main result. Include the effect size and statistical precision (95% CI or p-value), not just direction. If the result is a difference, give absolute numbers — not just relative risk reduction.

### 4. The most important limitation (1-2 sentences)

The single limitation that most constrains the generalizability or interpretation of the finding. Not a list of limitations — the most important one. Be specific about HOW it constrains interpretation, not just that it exists.

### 5. Would this change practice? (1-2 sentences)

A specific answer:
- **Yes, in [specific setting]:** [what changes and for which patients]
- **No, because:** [the specific gap that would need to be filled first]
- **Not yet, but if [X] confirms:** [what would tip it over]

Avoid "more research is needed" — that's true of everything.

### 6. Three questions I should be prepared to answer

If my attending asks me about this paper, what are the three questions most likely to come up? For each, give me 1-2 sentences of prepared answer.

## Hard rules

- **The honesty check is non-negotiable.** Do not summarize a paper you don't have.
- **Effect sizes must be specific.** "Significant reduction" is not enough; give the number.
- **The limitation must be the MOST important one, not the easiest to name.** Small sample size is easy to name and often not the most important.
- **The "would this change practice" answer must commit.** "It might, depending on circumstances" is a non-answer.
- **The three attending questions must be specific to THIS paper, not generic.** "What were the limitations?" is generic. "Why did the authors choose a 30-day mortality endpoint when the disease usually progresses over years?" is specific.

## What I will NOT accept

- A summary built from the title or abstract alone, dressed up as if you read the full paper
- Vague effect sizes ("significant")
- A list of limitations instead of the most important one
- Generic attending questions
- Citation that doesn't exactly match the paper (verify before producing the summary)
```

## Expected output

The six-part summary in the order above. Total length scales with the paper's substance — usually 300-450 words. Should be readable in 90 seconds.

## Common failure modes

- **Summary fabricated from the title.** This is the dominant failure mode and the most damaging. The honesty check at the top is designed to make this hard to commit; verify the model actually has the paper before trusting the summary.
- **Effect sizes given as direction only ("improved", "reduced") without numbers.** Push back for the number.
- **"More research is needed" non-answers in Step 5.** Push for a commit.
- **Generic limitation** like "small sample size" when N is 5,000. Push for the specific constraint.

## Required human verification

- **Verify the headline finding** against the actual paper. The model frequently misremembers numbers from papers it has "seen."
- **Verify the limitation is real and is actually the most important one.** A junior reviewer would catch obvious limitations; the model's value is in surfacing the subtle one, but it's also where the model is most likely to be wrong.
- **Verify the three attending questions are answerable** from the paper before relying on them in journal club.
- **If the honesty check answer is "I only have the abstract", DISCARD the summary entirely and provide the paper text.**

## Best model and why

**Gemini 2.5 Pro** with the PDF attached — best long-context handling of full-text PDFs as of mid-2026, which is the entire ball game for paper summarization. **Claude Opus 4.7** with PDF attached is a comparable alternative. Without the paper text, every model fabricates — model choice doesn't save you. Always confirm the model has the text before trusting the summary.
