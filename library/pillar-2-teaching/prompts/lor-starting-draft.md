---
title: Letter of recommendation starting draft
pillar: teaching
event_type: n/a
audience: faculty
difficulty: advanced
time_to_use: >10min
visual: text-only
tags: lor, narrative, high-stakes
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Produces a structured *scaffold* for a letter of recommendation — never a finished letter. The model holds the bones (paragraph structure, transition logic, closing strength) while you supply the entire substance (specific anecdotes, specific judgments, specific knowledge of this applicant that only you have).

The prompt is deliberately designed to **make the model ask before writing**, not write first and ask later. This is the single most important behavioral change because the dominant failure mode for AI-assisted LORs is generic prose that experienced reviewers immediately recognize as templated.

## When to use it

When you have agreed to write a strong letter and need to break blank-page paralysis. Use only when you have **substantive knowledge** of the applicant — at least 6 months of direct observation, or a comparable depth of interaction.

**Do NOT use** for an applicant you barely know (decline the request instead), for a letter that needs to be in your "real voice" with no AI involvement (some institutions and applicants prefer this), or as a shortcut when you don't have time to do the anecdote-gathering and editing work the prompt requires. AI-assisted LORs that skip those steps are a disservice to the applicant.

## Read this before using

Letters of recommendation are the highest-stakes writing in academic medicine. Three principles govern this prompt:

1. **The model can hold structure. Only you can supply substance.** Reviewers detect template language across hundreds of letters; the differentiator is your specific anecdotes and judgments.
2. **The model must ask, not assume.** This prompt enforces a question-first flow.
3. **Read every sentence aloud before sending.** If a sentence isn't one you would write, rewrite it.

## The prompt

```
You are helping me draft a letter of recommendation for a pathology applicant. Read the entire prompt before responding. Your job is to be a structural scaffold for prose I will substantially rewrite — not to produce a finished letter.

## Critical workflow — do not skip

Before writing ANY of the letter body, you must:

1. Confirm you understand the workflow described below.
2. Ask me **at least 4 specific questions** to elicit specific anecdotes about this applicant. Do not draft body paragraphs until I have given you concrete answers — moments I observed, with enough detail that a reader would know the letter could only have been written by me. If my answers are generic, push back and ask for more specific examples before continuing.

## Context I will provide

- **Applicant name, degree(s), and what they're applying for:** [e.g., "Jane Smith, MD, applying to hematopathology fellowship at [program name], start year 2027"]
- **My relationship to the applicant:** [how long I've known them, in what capacity, frequency of interaction]
- **My role:** [my title, why my voice carries weight for this particular application]
- **The strength of the letter requested:** [strong / very strong / "exceptional" — say plainly which]
- **Areas I want to highlight:** [the 2-3 attributes that should anchor the letter]
- **What I want the reader to know that's NOT on the CV:** [the differentiator]
- **Honest growth areas I want to acknowledge:** [optional — including a thoughtful growth area increases credibility]
- **Word count target / institutional norms:** [e.g., one page, two pages, sub-specialty fellowship norms]

## The 4+ questions you must ask before writing

For EACH attribute I want to highlight, ask me one variation of:
- "Give me one specific moment — a case, a conversation, a decision — where you observed [attribute]. I need details: what was the case, what did the applicant actually say or do, what would a less-skilled trainee have done instead?"

Plus at least one of:
- "What is the most differentiating thing about this applicant — something true of them but not of most strong residents at their stage?"
- "If a program director called you in two weeks and said 'tell me one thing that wasn't in the letter,' what would you say?"

Wait for my answers. If my answers are generic ('she's a hard worker'), push back: 'That description fits many residents. Give me a specific moment.'

## Letter structure — produce ONLY after you have my anecdotes

1. **Opening paragraph (3-4 sentences).** State my relationship, capacity, and a one-sentence headline of who this applicant is in my judgment. The headline should be a claim a reader could disagree with — not 'she is excellent' but something specific like 'she is the strongest first-pass histologic eye I have seen in five years of training residents on this service.'

2. **Body paragraph 1 (one of the highlighted attributes).** Open with a one-sentence claim, then ground it in one specific anecdote from what I gave you, told with the texture only I would know. End by naming what the anecdote demonstrates about the applicant.

3. **Body paragraph 2 (second attribute).** Same structure as paragraph 1, different anecdote.

4. **Optional body paragraph 3 (third attribute or honest growth area).** Same structure. If I provided a growth area, frame it as evidence the applicant is self-aware and improving — not as a weakness disclosure.

5. **Distinguishing paragraph (2-3 sentences).** What sets this applicant apart from other strong candidates at their stage. Use the answer I gave to the differentiating-thing question.

6. **Closing paragraph (2-3 sentences).** Explicit recommendation at the requested strength level, the rank-versus-cohort framing if appropriate ('top 10%', 'best resident I have worked with in N years', etc.), and an explicit offer to discuss the candidate further with my email or phone.

## Hard rules

- **Do not invent anecdotes, dates, case details, or accomplishments.** If a paragraph would require an anecdote I have not given you, write `[INSERT ANECDOTE: <what kind of anecdote belongs here>]` and move on.
- **Do not use template phrases.** Specifically avoid: "It is my pleasure to write this letter," "without hesitation," "a true asset to your program," "this letter is in support of," "I am writing to recommend." These flag the letter as templated in the first sentence.
- **Do not soften my requested strength.** If I asked for "very strong," the letter must read as very strong; do not hedge.
- **Do not pad to reach a length.** A tight one-page letter is better than a padded two-page one.
- **Match the institution's tone norms** based on the field I provided. Sub-specialty fellowship letters have different conventions than residency letters; CP fellowship reads differently than AP fellowship.

## What to produce in your FIRST response (before you have my anecdotes)

Only the 4+ questions, plus a one-sentence confirmation of the workflow. Nothing else. No partial draft. No opening paragraph.

## What to produce in your SECOND response (after my anecdotes)

The full structured draft, with `[INSERT ANECDOTE: ...]` placeholders only where I have not given you what's needed.
```

## Expected output

**First model response:** four or more questions designed to extract specific anecdotes, plus a one-sentence confirmation of the workflow. No draft text. If the model produces a draft on the first response, stop and remind it of the workflow.

**Second model response (after you provide anecdotes):** a structured draft (~400-600 words for a one-page letter) with all six structural sections, anecdotes grounded in your actual answers, no template language, and `[INSERT ANECDOTE: ...]` placeholders only where you have not yet provided enough detail.

## Common failure modes

- **The model drafts a generic letter on the first response without asking for anecdotes.** This is the #1 failure mode. Push back firmly: "Stop. Discard that draft. Ask the questions first."
- **The model accepts generic anecdotes** ('she's a hard worker') and writes around them instead of pushing back. If this happens, push back yourself: "That's not specific enough. Ask me again."
- **The opening sentence uses templated phrasing** ("It is my pleasure to write..."). Reject and rewrite — reviewers reading hundreds of letters spot this in the first sentence.
- **The strength of recommendation is hedged below what you asked for.** Re-state your requested strength and push back.
- **The model invents an anecdote.** Catch this on review — every anecdote in the final letter must trace to something you actually told it.

## Required human verification

- **Read every sentence aloud and ask: would I write this exact sentence?** Rewrite the ones where the answer is no — that should be most of them. The model's job is to give you a scaffold to rewrite, not a letter to sign.
- **Verify factual claims.** The applicant's accomplishments, dates of training, project titles, publications — confirm each against the CV.
- **Pressure-test the differentiation.** Show the closing paragraph to a colleague who doesn't know the applicant: would they understand what makes this person specifically distinctive, or could the closing apply to many strong candidates?
- **Check the strength calibration.** Re-read the letter as a program director who has never met you would. Does it convey the strength you intended, or does it read as lukewarm?
- **See [Guardrails](library.html#/docs/guardrails)** for more on the structural plausibility failure mode that's specifically lethal in LOR contexts.

## A note on AI disclosure in LORs

Different institutions have different norms about disclosing AI assistance in writing LORs. Some explicitly require disclosure if AI was used in drafting; others consider AI-assisted drafting acceptable if the substance and judgment are the author's. Check the relevant institution's policy before using AI assistance for a formal LOR — and consider whether disclosure is appropriate even if not required.

## Best model and why

**Claude Opus 4.7** — LOR readers detect template language with high reliability across hundreds of letters per cycle. Opus produces less formulaic prose than Sonnet and is more disciplined about waiting for anecdotes before drafting. That said: the *structural plausibility* problem applies to every model — the differentiator is always your specific anecdotes and judgment, not the model's prose. Use Opus, edit aggressively. If you find yourself sending the model's draft with only light edits, the letter is not yet ready.
