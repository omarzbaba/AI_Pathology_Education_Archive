---
title: Pillar I — Self-Education
last_updated: 2026-05-17
---

## Using AI to learn pathology

Pillar I is the most personal of the three. These prompts are designed for *you* — the resident reviewing for boards, the fellow drilling subspecialty differentials, the faculty member catching up on a paper, the program director trying to understand a topic before teaching it. The library here treats AI as a tutor and study partner, not as a source of truth.

A few principles run through every prompt in this pillar:

- **Calibrate before you drill.** Tell the model your level (PGY-2 hematopathology rotation, second pass through immunoassays, etc.) and what you already know. The same question asked cold gets a generic answer; the same question asked with calibration gets one tuned to your gap.
- **Chain in one session.** Most of these prompts are designed to be used in sequence — explain a concept, then deepen it, then drill it. The same conversation thread keeps the model's mental model of you intact.
- **Verify before you trust.** Every prompt in this pillar ends with a *Required human verification* section that names specifically what you must check before treating the output as correct.

<div class="flagship">
<p class="flagship__eyebrow">Start here &middot; Flagship worked example</p>
<h2 class="flagship__title">Three weeks to close your weakest topic</h2>
<p class="flagship__premise">A PGY-2 has three weeks to the in-service exam and keeps reversing CLL/SLL and mantle cell lymphoma under time pressure. Follow the complete self-study loop she ran &mdash; eight prompts from this pillar, in sequence, including the model error she caught and why it mattered.</p>
<ul class="flagship__meta">
<li>Hematopathology</li>
<li>PGY-2</li>
<li>8 prompts chained</li>
<li>~4 h over 3 weeks</li>
</ul>
<ol class="arc">
<li>Name the gap</li>
<li>Schedule it</li>
<li>Concept at level</li>
<li>Discriminators</li>
<li>Self-quiz</li>
<li>Reverse drill</li>
<li>Generate &amp; audit items</li>
<li>Bank what survived</li>
</ol>
<p><a class="btn" href="library.html#/library/pillar-1-self-education/examples/three-weeks-cd5-lpd">Walk through the example &rarr;</a></p>
</div>

## Prompt index

### Concept work

- [Concept explanation at level](library.html#/library/pillar-1-self-education/prompts/concept-explanation-at-level)
- [Compare and contrast](library.html#/library/pillar-1-self-education/prompts/compare-contrast)
- [Guideline plain-language translation](library.html#/library/pillar-1-self-education/prompts/guideline-plain-language)
- [LIS / informatics concept review](library.html#/library/pillar-1-self-education/prompts/lis-informatics-review)

### Self-quizzing

- [Self-quiz one at a time](library.html#/library/pillar-1-self-education/prompts/self-quiz-one-at-a-time)
- [MCQ generation with rationales](library.html#/library/pillar-1-self-education/prompts/mcq-generation-with-rationales)
- [Anki flashcard generation](library.html#/library/pillar-1-self-education/prompts/anki-flashcards)
- [Board prep schedule](library.html#/library/pillar-1-self-education/prompts/board-prep-schedule)
- [Question bank gap analysis](library.html#/library/pillar-1-self-education/prompts/question-bank-gap-analysis)

### Case-based drilling

- [Diagnostic algorithm walkthrough](library.html#/library/pillar-1-self-education/prompts/diagnostic-algorithm-walkthrough)
- [Reverse case drill (findings → Dx)](library.html#/library/pillar-1-self-education/prompts/reverse-case-drill)
- [Forward case drill (Dx → expected findings)](library.html#/library/pillar-1-self-education/prompts/forward-case-drill)
- [Negative drill (what would change the Dx)](library.html#/library/pillar-1-self-education/prompts/negative-drill)
- [Differential by histologic pattern](library.html#/library/pillar-1-self-education/prompts/differential-by-histologic-pattern)
- [Frozen section thinking-out-loud drill](library.html#/library/pillar-1-self-education/prompts/frozen-section-thinking-aloud)

### Reading the literature

- [Paper summarization](library.html#/library/pillar-1-self-education/prompts/paper-summarization)
- [Paper methods critique](library.html#/library/pillar-1-self-education/prompts/paper-methods-critique)
- [Journal club pre-read prep](library.html#/library/pillar-1-self-education/prompts/journal-club-preread)

### Multimodal & lab

- [Photomicrograph description practice](library.html#/library/pillar-1-self-education/prompts/multimodal-photomicrograph)
- [SPEP / IFE trace interpretation walkthrough](library.html#/library/pillar-1-self-education/prompts/multimodal-spep-ife)
- [IHC stain interpretation walkthrough](library.html#/library/pillar-1-self-education/prompts/ihc-stain-interpretation)
- [Blood smear systematic review walkthrough](library.html#/library/pillar-1-self-education/prompts/blood-smear-systematic-review)

### Molecular & CP workflow

- [Molecular result interpretation drill](library.html#/library/pillar-1-self-education/prompts/molecular-result-interpretation)
- [Critical value workflow drill](library.html#/library/pillar-1-self-education/prompts/critical-value-workflow)

### Source-grounded AI (NotebookLM & Claude Projects)

*Use AI grounded in your own source materials — board prep notebooks, sign-out preview corpora, journal club libraries — instead of generic chat. Different setup, different prompts, different failure modes.*

**Read first (now under [How-to](library.html#/docs/how-to/index)):**
- [Choose your tool — NotebookLM vs Claude Projects vs generic chat](library.html#/docs/how-to/notebooklm-vs-claude-projects)
- [Source curation principles for AI notebooks](library.html#/docs/how-to/curate-sources)
- [Verify your AI notebook is actually grounded](library.html#/docs/how-to/verify-grounding)
- [Privacy and copyright for source-grounded AI](library.html#/docs/how-to/privacy-and-copyright)

**Setup guides for specific use cases:**
- [Build a board prep notebook](library.html#/library/pillar-1-self-education/prompts/sg-board-prep-notebook)
- [Build a sign-out preview notebook](library.html#/library/pillar-1-self-education/prompts/sg-signout-notebook)
- [Build a journal club notebook](library.html#/library/pillar-1-self-education/prompts/sg-journal-club-notebook)

**Prompt templates (source-grounded versions):**
- [Source-grounded concept explanation](library.html#/library/pillar-1-self-education/prompts/sg-concept-explanation-sourced)
- [Source-grounded self-quiz](library.html#/library/pillar-1-self-education/prompts/sg-self-quiz-sourced)
- [Source-grounded MCQ generation](library.html#/library/pillar-1-self-education/prompts/sg-mcq-generation-sourced)
- [Knowledge gap discovery from sources](library.html#/library/pillar-1-self-education/prompts/sg-knowledge-gap-discovery)
- [Source-grounded paper critique against your corpus](library.html#/library/pillar-1-self-education/prompts/sg-paper-critique-against-corpus)
- [Cross-source comparison drill](library.html#/library/pillar-1-self-education/prompts/sg-cross-source-comparison)

### Worked examples

- [**Flagship** — Three weeks to close your weakest topic](library.html#/library/pillar-1-self-education/examples/three-weeks-cd5-lpd)
- [Self-quizzing through SPEP interpretation](library.html#/library/pillar-1-self-education/examples/spep-self-quiz)
