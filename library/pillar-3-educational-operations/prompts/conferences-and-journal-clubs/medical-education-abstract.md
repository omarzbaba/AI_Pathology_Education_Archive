---
title: Conference abstract for medical education research
pillar: educational-operations
event_type: conference
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: abstract, medical-education-research, scholarship
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Drafts a conference abstract for medical education research (AAMC, AMEE, society educational sections). Medical education abstracts follow different conventions than clinical research abstracts — different sections, different evidence standards, different ways of framing innovation.

## When to use it

When submitting to a medical education conference. Best done with your project data in hand and a clear sense of which conference's conventions apply.

**Not for:** clinical research abstracts (different conventions), QI abstracts (different framework), or as a substitute for your IRB-approval status (verify before submitting).

## The prompt

```
You are drafting a medical education conference abstract. Med-ed abstracts have different conventions than clinical research — the framing and evidence standards are specific.

## What I'm submitting

- **Conference:** [name + abstract category if applicable]
- **Word limit:** [check the conference guidelines]
- **Abstract type:** [original research / innovation report / curriculum description / scholarly perspective]
- **Conference's preferred structure:** [check guidelines — usually structured with named sections]

## My project

- **Background / problem:** [the educational gap your project addresses]
- **Setting:** [where this happened — institution, level of learners, scale]
- **Intervention or innovation:** [what you did]
- **Evaluation approach:** [how you measured impact]
- **Results:** [what you found — quantitative + qualitative]
- **Discussion / implications:** [what others can take from this]
- **IRB / ethics status:** [exempt / expedited / approved / not applicable]

## What to produce

### The abstract

In the conference's required structure. Common med-ed structures:

**Research abstract (200-350 words):**
- **Background / Problem**
- **Educational Context** (setting + learners)
- **Innovation / Intervention**
- **Evaluation Methods**
- **Results**
- **Discussion / Significance**

**Innovation report (200-350 words):**
- **Statement of Problem**
- **Approach** (what you did, how it was novel)
- **Outcomes** (what evidence you have it worked)
- **Practical Lessons / Implications**

### Title

3-5 candidate titles. Med-ed titles tend to be longer and more descriptive than clinical research titles. Avoid clever titles that obscure content.

### Keywords

5-7 keywords for indexing.

### A note on what's missing

If your project has gaps (small sample, no comparison group, limited follow-up), name them explicitly and suggest framing that's honest without being self-defeating. Reviewers respect acknowledged limitations.

## Hard rules

- **Match the conference's required structure exactly.** Submissions get rejected for format issues.
- **Word count within limit.** Count it.
- **Specific outcomes, not vague claims.** "Improved learning" is not an outcome; "30% improvement in post-test scores (p<0.05)" is.
- **Honest about limitations.** Don't oversell.
- **IRB status mentioned where applicable** (some conferences require it in the abstract).

## What I will NOT accept

- Abstracts that overrun word limits
- Vague outcomes
- Oversold conclusions
- Generic discussion section that could apply to any project
```

## Expected output

The structured abstract + 3-5 candidate titles + keywords + limitation framing. Total length depends on word limit.

## Common failure modes

- **Word count overrun.** Verify.
- **Vague outcomes.** Push for specific numbers.
- **Conclusion overreach.** Pull back to what the evidence supports.

## Required human verification

- Verify all reported numbers against your actual data.
- Confirm conference's required structure and word limit haven't changed.
- Have a colleague who's served as a med-ed conference reviewer read the draft.
- Verify IRB status language matches your actual approval.

## Best model and why

**Claude Sonnet 4.6** — structured short-form writing with specific conventions is Sonnet's strength.
