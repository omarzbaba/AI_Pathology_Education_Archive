---
title: IRB protocol for QI or educational research
pillar: educational-operations
event_type: course
audience: faculty
difficulty: advanced
time_to_use: >10min
visual: text-only
tags: irb, qi, educational-research, regulatory
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Drafts a starting IRB protocol for an educational intervention or quality improvement study — the type most pathology educators do. Walks through whether it's QI or research, the appropriate level of IRB review (exempt / expedited / full board), the required protocol elements, and the data/consent language.

The hardest decision this prompt clarifies: **is your project QI or research?** The classification determines everything else.

## When to use it

When planning an educational study (e.g., effectiveness of a new curriculum), a QI project (e.g., reducing critical-value response time), or a scholarship project that will be published. Best done early in project design, before data collection starts.

**Not for:** clinical research with patient subjects (different category — work with your IRB directly), studies involving identifiable patient data (different framework), or as a substitute for actual IRB review (this generates a starting protocol, not a finished submission).

## The prompt

```
You are helping me draft a starting IRB protocol for an educational or QI project. The first thing to settle is whether this is QI or research. The classification changes everything that follows.

## What I'm planning

- **Project name:** [brief]
- **Project description:** [what I'm doing and why]
- **Setting:** [pathology residency / fellowship / faculty development / multi-institutional]
- **Subjects:** [residents / faculty / patients / specimens / records]
- **Data I'll collect:** [pre/post test scores, survey responses, observed behaviors, retrospective chart review, etc.]
- **Will results be published or presented externally?** [yes / no / unsure]
- **Institutional IRB:** [name + general framework — whether they use OHRP Common Rule]

## STEP 1: QI vs Research classification

Walk me through this decision explicitly. Key questions per OHRP guidance:

1. Is the intent to develop or contribute to **generalizable knowledge** (research) vs improve a specific local process (QI)?
2. Will findings be **published or presented externally** in a way intended to inform practice beyond this institution?
3. Is there **randomization or control** that wouldn't otherwise occur?
4. Is there **deviation from accepted practice** to test a hypothesis?

Based on my answers, classify as:
- **QI only** — may not require IRB review at all, but often requires departmental QI committee review
- **QI with planned dissemination** — may require IRB review; some institutions have a "QI with publication intent" pathway
- **Research** — requires IRB review

If you're uncertain, recommend I consult my institutional IRB before designing the rest.

## STEP 2: If research — IRB review level

Walk through likely classification:
- **Exempt** — most educational research with no/minimal risk: surveys, educational tests, observational of normal educational practices
- **Expedited** — research involving minor risk: retrospective record review with PHI, prospective educational intervention
- **Full board** — vulnerable populations, more than minimal risk

For my project specifically, recommend a likely level with rationale.

## STEP 3: Protocol elements

For the appropriate review level, draft each required section:

1. **Specific aims** (1-2 sentences each, measurable)
2. **Background and significance** (~1 paragraph)
3. **Study design and methods** (specific to my project)
4. **Subjects** (inclusion/exclusion, recruitment, sample size with justification)
5. **Data collection** (what, how, by whom)
6. **Data security and confidentiality** (where data lives, who has access, retention plan)
7. **Risks** (specific to subject type — residents have different risks than patients)
8. **Benefits** (to subjects, to the field — be honest)
9. **Consent** (consent form text OR rationale for waiver of consent)
10. **Dissemination plan** (publication, presentation, internal report)

## STEP 4: Common pitfalls for educational research

Flag the 2-3 most common reasons educational research protocols get returned for revision at your IRB.

## Hard rules

- **Be honest about classification.** If a project crosses into research, say so.
- **Recommend consultation with the institutional IRB early** for ambiguous cases.
- **Do NOT generate fake IRB-approved language.** This is a STARTING draft for me to review with my IRB.
- **Acknowledge that institutional policies vary.** What's exempt at one institution may require expedited review at another.

## What I will NOT accept

- A protocol that confidently states the review level without acknowledging institutional variation
- Generic protocol language that doesn't engage with my specific project
- Skipping the QI vs research decision step
- Claims about IRB approval pathways without sourcing
```

## Expected output

A QI/research classification recommendation + IRB review level recommendation + 10-section starting protocol + common pitfalls. Length 1000-1500 words.

## Common failure modes

- **Confidently mis-classifies QI as research** or vice versa. Push back: "Walk through the criteria explicitly."
- **Generic protocol language.** Push for specificity to your project.
- **Skips institutional variation acknowledgment.** Push back.

## Required human verification

- **Consult your IRB.** This prompt generates a starting draft, not an approval. Your IRB's specific requirements may differ.
- **For research that might involve protected health information, consult your privacy officer.** HIPAA implications are project-specific.
- **For multi-institutional projects, all involved IRBs may need to approve.** Don't assume reciprocity.

## Best model and why

**Claude Opus 4.7** — IRB protocol drafting requires depth and regulatory awareness. Opus is more careful about acknowledging uncertainty and institutional variation than Sonnet.
