---
title: Promotion / portfolio teaching narrative
pillar: educational-operations
event_type: course
audience: faculty
difficulty: advanced
time_to_use: >10min
visual: text-only
tags: promotion, portfolio, teaching-narrative, high-stakes
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Drafts the "teaching and education" narrative section of a faculty promotion portfolio. This is the high-stakes annual writing that committee members read to evaluate teaching contributions for promotion to associate or full professor.

The hardest discipline: this is a NARRATIVE, not a list. The narrative connects teaching activities to a coherent identity as an educator — the committee is evaluating whether you ARE an educator, not whether you've done teaching activities.

## When to use it

When preparing your promotion portfolio (annual update or formal promotion year). Best done with your CV in hand, your teaching evaluations available, and ideally with a mentor reviewing the draft.

**Not for:** writing your CV (different format), short bios (different scope), or as a substitute for working with your institution's faculty affairs office on portfolio requirements.

## The prompt

```
You are drafting the "teaching and education" narrative for my promotion portfolio. This is a high-stakes narrative — the committee reads it to evaluate whether I am an EDUCATOR, not whether I've done teaching activities.

## Critical first step

Before drafting, ask me at least 4 questions to elicit specific anecdotes and a coherent educator identity. Do NOT start writing the narrative until you have substantive answers. Generic teaching prose without specific anecdotes is the most common failure mode for promotion narratives.

## What I'll provide

- **Promotion target:** [associate professor / full professor / clinician-educator track / other]
- **My institution's framework:** [educator portfolio required / narrative only / mixed]
- **Time period covered:** [years]
- **Teaching activities to draw from:**
  - **Formal courses or rotations taught:** [list with role and dates]
  - **Mentorship:** [residents, fellows, faculty I've mentored]
  - **Curriculum development:** [what I created or substantially revised]
  - **Educational scholarship:** [publications, presentations, grants]
  - **Educational leadership:** [course director, program director, education committee roles]
- **Teaching evaluations / outcomes data:** [what's available]
- **My institution's word limit:** [if specified]

## The 4+ questions you must ask before drafting

1. **The identity question:** "If a committee member could describe your contribution as an educator in one sentence after reading the narrative, what would that sentence be? Don't tell me what you DO — tell me what you ARE in this domain."

2. **The anecdote question:** "Give me one specific moment in the past 3 years that captures what you bring to teaching. A specific learner, a specific course design decision, a specific moment of impact. Details I can use to ground a paragraph."

3. **The evolution question:** "How have you grown as an educator since your last review? What can you do now that you couldn't 3 years ago?"

4. **The differentiation question:** "What distinguishes your teaching contribution from a colleague at your rank who is also doing teaching? Be honest — committees read many portfolios."

If my answers are generic, push back for specifics before drafting.

## Narrative structure (typically 800-1500 words depending on institutional norms)

### Opening (1 paragraph)
The identity statement — what kind of educator you are. Anchored in a specific scope (e.g., "I have built my educational contribution around teaching diagnostic reasoning to early-stage CP residents through structured case-based instruction"). Not a list of activities; an identity claim.

### Teaching practice (2-3 paragraphs)
- What you teach, to whom, in what formats
- Anchored in one or two SPECIFIC examples from the anecdotes I gave
- Tie to outcomes (learner feedback, performance data) where available

### Curriculum and innovation (1-2 paragraphs)
- What you've built or substantially redesigned
- The specific need it addressed
- Evidence it worked

### Mentorship (1 paragraph)
- Specific mentees and where they are now (de-identified if appropriate)
- Your approach to mentoring as a deliberate practice, not just an activity

### Educational scholarship (1 paragraph if applicable)
- Publications, presentations, grants
- The thread connecting them — what's the educational question you're pursuing?

### Leadership and field contribution (1 paragraph if applicable)
- Roles within the institution and externally
- How your work influences practice beyond your institution

### Forward statement (1 paragraph)
- Where you're going in the next 3-5 years
- Specific, not aspirational

## Hard rules

- **Identity first, activities second.** A list of activities without identity reads as a CV.
- **Specific anecdotes ground every claim.** Generic competence statements are the failure mode.
- **Outcomes where available.** Evaluations, learner performance, dissemination — quantify where you can.
- **Honest about scope.** Promotion committees recognize inflated claims. Stay honest about your level of contribution.
- **Forward statement is specific.** "I plan to continue contributing to medical education" is the worst version; "I plan to develop and validate a structured assessment tool for diagnostic reasoning in CP, partnering with [colleague/group]" is the right version.

## What I will NOT accept

- A list of activities masquerading as a narrative
- Generic anecdotes ("I work hard with my residents")
- Outcomes claimed without evidence
- A forward statement that's actually a wish list
```

## Expected output

The 4+ questions in the first response; the structured narrative (~800-1500 words depending on institutional norms) in the second response after you provide answers.

## Common failure modes

- **Activity-list instead of identity.** Push back: "What's the identity?"
- **Generic anecdotes.** Push back for specific learners, specific moments.
- **Quantified outcomes claimed without evidence.** Verify.

## Required human verification

- **Run by a mentor at your institution** — they know what your specific promotion committee weighs.
- **Verify all dates, titles, and outcomes** against your CV before submitting.
- **Check institutional word limit and format requirements** — these vary considerably.
- **If you're being considered for a track requiring specific evidence (clinician-educator track, etc.), confirm the narrative addresses the required dimensions.**

## Best model and why

**Claude Opus 4.7** — high-stakes narrative writing with identity-level claims requires depth. Sonnet produces more generic prose; Opus is materially better at the identity-vs-activity distinction.
