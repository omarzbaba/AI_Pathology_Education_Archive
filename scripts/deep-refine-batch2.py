#!/usr/bin/env python3
"""
Deep refinement batch 2:
- 11 remaining Pillar 1 prompts (deeply refined)
- 5 new Pillar 2 prompts (created at exemplar depth)
- 5 highest-value Pillar 2 prompts (deeply refined)

Total: 21 prompts.

Run:
  python3 scripts/deep-refine-batch2.py
"""

from pathlib import Path

def write_prompt(path, fm, body):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("---\n" + "\n".join(f"{k}: {v}" for k, v in fm.items()) + "\n---\n\n" + body)

# ===========================================================================
# PILLAR 1 — REMAINING 11 PROMPTS (deeply refined)
# ===========================================================================

write_prompt(
    "library/pillar-1-self-education/prompts/compare-contrast.md",
    {"title":"Compare and contrast","pillar":"self-education","event_type":"n/a","audience":"resident",
     "difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"differential, entity-comparison","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Produces a focused side-by-side comparison of two entities you confuse, organized around the *discriminating* features that actually separate them — not a comprehensive list of every difference. The output is a table you can put on a flashcard, plus the single best discriminator and the classic trap.

## When to use it

When you've gotten a board-style question wrong because you picked the wrong one of a pair, when you can name both entities but routinely confuse them, or when you want to drill an entity-vs-entity discrimination before sign-out.

**Not for:** comparisons across a whole category (use [Differential by histologic pattern](library.html#/library/pillar-1-self-education/prompts/differential-by-histologic-pattern) instead) or first-time learning of either entity (read about each first).

## The prompt

```
You are helping me sharpen my discrimination between two entities I confuse. The output is a focused comparison, not a comprehensive list of every difference. Discriminating features only.

## What I'm comparing

- **Entity A:** [be specific — e.g., "follicular lymphoma, grade 1-2"]
- **Entity B:** [e.g., "reactive follicular hyperplasia"]
- **My level:** [PGY level + relevant rotation context]
- **What I get wrong:** [optional — the specific way I mistake them, if I know]

## What to produce

### 1. One-sentence orientation

How do these two entities relate to each other in the differential? (Same family but malignant vs reactive? Both subtypes of X? Lookalikes on H&E but resolved by IHC?)

### 2. Discriminating features table

| Feature | Entity A | Entity B |
|---|---|---|

Each row is a feature where they **differ in a clinically meaningful way**. Skip features they share. Aim for 4-8 rows — not more.

### 3. The single best discriminator

If you could ask only ONE question or order ONE test to resolve the differential, what is it? Justify in one sentence.

### 4. The classic trap

The single feature most likely to push a resident toward the WRONG answer, and how to avoid the trap. Be specific about the cognitive error — not "be careful," but "residents often see [feature] and conclude [wrong entity], because they forget that [feature] is also present in [right entity] when [condition]."

### 5. Source any version-dependent features

If a discriminating feature depends on a specific classification version (WHO 5th vs ICC 2022, NCCN year, etc.), state which version explicitly. Discrimination rules drift between editions.

## Hard rules

- Use the discriminating features your subspecialty's reference text actually uses, not generic ones I could guess
- If a "discriminator" depends on a test I can't realistically order in real practice, say so
- If a specific IHC stain is named, name the clone if the discrimination is clone-dependent
- Do not list shared features (waste of space)
- Do not invent discriminators you're not sure about — say so instead

## What I will NOT accept

- A table where most rows describe features both entities share
- A "best discriminator" that's not actually orderable
- A classic trap that's generic ("look carefully")
```

## Expected output

A 4-section comparison: orientation sentence, 4-8 row table, named best discriminator, named trap. Plus version disclosure for any classification-dependent feature.

## Common failure modes

- **Table includes shared features.** Push back: "Cut rows where they're the same."
- **Discriminators that are actually wrong** (mistaken for one another in subtypes). Verify against your subspecialty atlas.
- **Generic trap** ("be careful with morphology"). Push back: "Name the specific feature that misleads."

## Required human verification

- Confirm the discriminating features against your subspecialty's current reference. Models can confuse features between similar entities, especially for rarer diagnoses.
- If a specific stain pattern is named, confirm clone and current convention.
- Pressure-test the "best discriminator" with an attending — is it actually what they'd use?

## Best model and why

**Claude Sonnet 4.6** — structured comparison tables are Sonnet's strength. For comparisons that require sub-edition precision (WHO 5th vs ICC 2022 for hematopoietic neoplasms, for example), use **Opus 4.7** — Sonnet sometimes blurs version-specific discriminators.
""")

write_prompt(
    "library/pillar-1-self-education/prompts/guideline-plain-language.md",
    {"title":"Guideline plain-language translation","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"quick-win","time_to_use":"2-10min","visual":"text-only",
     "tags":"guidelines, plain-language","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

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
""")

write_prompt(
    "library/pillar-1-self-education/prompts/lis-informatics-review.md",
    {"title":"LIS / informatics concept review","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"informatics, lis, standards","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Bridges the vocabulary gap between clinical pathologists and informatics. You name a concept (HL7 segments, FHIR resources, middleware autoverification, LOINC mapping, instrument interfacing); the model gives you the mental model, the working vocabulary, the most common failure mode, and one specific question you can ask in a vendor or IT meeting that distinguishes a substantive answer from a hand-wave.

## When to use it

Before an informatics committee meeting, when evaluating a vendor proposal, when a workflow issue gets escalated to IT, or when you want to participate substantively in a discussion about lab IT infrastructure rather than just listening.

**Not for:** deep informatics certification prep (read a textbook), implementation-specific configuration questions (those need an actual informaticist), or settled questions you can just look up.

## The prompt

```
You are explaining an informatics concept to me — a clinical pathologist who runs a lab but is not a full-time informaticist. The goal is to give me the mental model, the working vocabulary, and the ability to participate meaningfully in a vendor or IT meeting on this topic.

## What I'm asking about

- **Concept:** [e.g., "HL7 v2.5.1 ORU result segment structure", "FHIR Observation resource", "middleware autoverification logic", "LOINC code harmonization across two instruments", "IHE LAW profile"]
- **My existing knowledge:** [what I know already and what's still fuzzy]
- **The specific situation prompting this:** [optional — e.g., "we're evaluating a middleware vendor next week", "our chemistry instrument is throwing OBX-5 errors"]

## What to produce — 5 parts

### 1. The problem this concept solves (2-3 sentences)

Why does this thing exist? What does it make possible that wasn't possible before? Ground it in a concrete lab problem.

### 2. The mental model (2-3 sentences)

An analogy or simplified description that captures the essence. Be careful: the analogy should illuminate, not mislead. If the analogy breaks down at a critical point, name where.

### 3. The working vocabulary (5-7 terms)

The terms I'll hear thrown around in a meeting, each with a one-sentence definition. These are the words I need to follow the conversation — not exhaustive, just the high-frequency ones.

### 4. The most common failure mode in real labs (2-3 sentences)

The thing that breaks. What goes wrong, what it looks like (downtime, wrong results, missed criticals), what the typical root cause is, and what the fix typically involves.

### 5. One question I can ask in a meeting (1 question + brief rationale)

A specific question that, if asked, would distinguish a vendor who knows what they're doing from one who's improvising. Or a question that would clarify a confusion point that's slowing your meeting. The question should be answerable but not trivial — a good vendor will respect that you asked it.

## Hard rules

- **Cite specific standards by name and version** where applicable. "HL7 v2.5.1 OBX-5", "FHIR R4 Observation.code", "LOINC 33747-0". Do not paraphrase the standard.
- **If you're not sure whether a term or concept is current vocabulary**, say so. Informatics terminology changes (HL7 v2 → FHIR; SNOMED-CT version drift).
- **The mental model analogy must be honest about where it breaks.** Cute analogies that mislead are worse than no analogy.
- **The "common failure mode" should be a real-world failure**, not a textbook risk.
- **The "question to ask" must be specific enough to use in a meeting** without further translation.

## What I will NOT accept

- Vocabulary terms that are themselves opaque (defining one informatics term using three others I don't know)
- A "common failure mode" that's generic ("configuration errors happen")
- An analogy that's accurate at the surface but breaks at the point of usefulness
- A vendor question that's so basic any answer would seem fine
```

## Expected output

Five parts in order. Total length 400-600 words. The vendor question is often the most useful part — it gives you a concrete handle for the meeting.

## Common failure modes

- **Model uses informatics jargon while explaining informatics jargon** (recursive opacity). Push back: "Define [term you used] in plain language too."
- **The "most common failure mode" is generic** rather than the actual recurring failure in real labs. Push back for specific.
- **Standard versions misnamed.** Verify against the actual standard.

## Required human verification

- Verify any cited standard, segment name, code, or version against authoritative documentation (HL7.org, hl7.fhir.org, LOINC.org).
- For high-stakes situations (vendor selection, contract review), have an informaticist colleague pressure-test the question you plan to ask before relying on it.
- The mental model is most useful when validated by someone who has actually built or maintained this in production.

## Best model and why

**Claude Opus 4.7** — informatics standards (HL7, FHIR, LOINC) require depth and specificity. Opus cites segment names and resource types more reliably than Sonnet and is more careful about version disclosure. **Avoid GPT models** for this prompt — they confuse HL7 v2 segment names with FHIR resource fields more often than is comfortable.
""")

write_prompt(
    "library/pillar-1-self-education/prompts/anki-flashcards.md",
    {"title":"Anki flashcard generation","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"quick-win","time_to_use":"2-10min","visual":"text-only",
     "tags":"spaced-repetition, anki","verified_models":"TODO",
     "best_model":"Claude Haiku 4.5","last_updated":"2026-05-17"},
    """## What this prompt does

Converts a topic, paper, set of notes, or lecture into Anki-import-ready flashcards in tab-separated format. The prompt enforces *atomic* cards (one fact per card), *specific* questions (not "what is X"), and *verification flags* for any specific value the model isn't certain about.

## When to use it

Within an hour of finishing a dense reading session, while the material is still fresh enough for you to spot misformulated cards quickly. Also useful for converting a lecture's slide deck into review material.

**Not for:** building a comprehensive deck from scratch (this is for incremental additions, not bulk creation), high-stakes question banks (those need editorial review per card), or material you're seeing for the first time (study first, then make cards).

## The prompt

```
You are generating Anki flashcards from source material. Output must be tab-separated, atomic, and specific. If you cannot verify a specific value (cutoff, dose, gene name), flag it [VERIFY] rather than committing to it.

## What I'm converting

- **Source:** [topic name / paper citation / pasted notes / lecture title]
- **Source material:** [paste the content, or describe if it's a known topic]
- **Number of cards:** [e.g., 15 — don't pad; fewer good cards is better than more weak ones]
- **Card style:** [Basic Q/A — default, unless I say cloze]
- **My level:** [PGY level — calibrates how specific the questions should be]

## Output format — tab-separated, one card per line

Each line:
`question[TAB]answer`

## Rules — applied to every card

1. **Atomic.** Each card tests ONE fact or concept. If a card uses "and" or "or" in the answer, split it into two cards.
2. **Specific question framing.** "What is X?" is a weak question. "In a patient with X, what laboratory finding distinguishes A from B?" is strong. Questions should require retrieval, not recognition.
3. **Use actual numbers, names, and details from the source.** If the source doesn't have a specific value and you're filling it in from memory, append [VERIFY] to the answer.
4. **No clozes unless I asked.** Plain Q/A only by default.
5. **Don't pad to reach N cards.** If the material only supports 10 good cards, give me 10.
6. **No card should test two things at once.** "What are the four causes of X?" is weak (forces dump). "Among the four causes of X, which one is associated with [specific feature]?" is strong.

## After the cards, add a brief note

Add one short paragraph noting:
- What you deliberately did NOT make a card for (and why)
- Any [VERIFY]-flagged values I should double-check before adding the deck to active review

## Hard rules

- Tab-separated format, no extra commentary mixed with cards
- Atomic cards always
- [VERIFY] flag on any value you're not certain about
- Source-grounded specificity over generic phrasing

## What I will NOT accept

- "What is X?" style cards as default framing
- Cards that test multiple facts ("List the three reasons for Y")
- Padding with weak cards to reach the requested number
- Confidently stated specific values without verification
```

## Expected output

N tab-separated lines (one card per line) plus a brief note about exclusions and verification flags. Lines should be import-ready: paste into Anki → Import → Text File.

## Common failure modes

- **"What is X" cards.** Push back: "Reframe these as specific retrieval questions."
- **Cards testing multiple facts.** Split them.
- **Confidently made-up specific values.** Add [VERIFY] manually before adding to your deck.

## Required human verification

- Scan every answer with a specific numerical value, drug dose, gene name, or threshold. Verify against the source. The model sometimes invents plausible-looking specifics.
- For cards built from your own notes, double-check that the model preserved your wording rather than rewriting subtly.

## Best model and why

**Claude Haiku 4.5** — flashcard conversion is a fast, structured task. Haiku handles it well at a fraction of the cost. Bump to **Sonnet 4.6** only if the source material is dense (methods-heavy paper, complex algorithm) where atomicity is harder to maintain.
""")

write_prompt(
    "library/pillar-1-self-education/prompts/board-prep-schedule.md",
    {"title":"Board prep schedule","pillar":"self-education","event_type":"n/a","audience":"resident",
     "difficulty":"quick-win","time_to_use":">10min","visual":"text-only",
     "tags":"planning, board-prep","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Generates a personalized board prep schedule that adapts to your actual constraints (weeks remaining, daily hours available, strongest/weakest subspecialties, resources you'll use). Includes mandatory rest days, a rescue week near the exam, and explicit pre-exam-week guidance — features that distinguish a realistic schedule from a hypothetical one.

## When to use it

At the start of dedicated board prep, when re-allocating an existing plan that's not working, or when a life event (illness, rotation change, family) requires re-planning. Best done with honest self-assessment — the schedule is only as good as your input.

**Not for:** replacing experienced mentor advice (talk to recent graduates), schedules that don't account for clinical work continuing alongside prep (state explicitly), or first-time test-takers who need help calibrating ambitions (talk to a colleague first).

## The prompt

```
You are building me a board prep schedule. Be specific about resources, build in rest, and call out tradeoffs honestly. A schedule I can't sustain is worse than no schedule.

## My situation

- **Exam:** [name, date, format]
- **Weeks until exam:** [N]
- **Daily hours I can commit:** [weekdays X hours, weekends Y hours — be honest, not aspirational]
- **Clinical workload during prep:** [continuing rotations / dedicated study time / hybrid — describe]
- **Self-assessment by subspecialty:**
  - **Strong** (can pass at this moment): [list]
  - **Moderate** (would struggle on harder questions): [list]
  - **Weak** (would fail a focused section): [list]
- **Resources I have:** [qbank name, textbook, review course, study group, etc.]
- **Constraints I want you to respect:** [e.g., "I have a wedding week 8", "I can't study after 8pm", "I need at least one full day off per week"]

## Inconsistency check — do this FIRST

If my self-assessment looks internally inconsistent (a topic listed as "Strong" but also as something I want extra time on, or "Weak" topics that aren't in my resources), ASK me to clarify before generating the schedule.

## What to produce

### Week-by-week schedule

For each week:
- Topics covered (more time on weak areas, maintenance on strong areas)
- Daily breakdown: reading hours, qbank hours, review hours
- ONE rest day per week — not optional
- Specific resource mappings ("Tuesday: 2 hrs Robbins chapter 12 + 1 hr USMLE-style qbank on this topic")

### Required structural features

- **Rescue week** 2 weeks before the exam: re-attack the topics still weak after first pass
- **The week before the exam:** zero new material, focused review only
- **The last 48 hours:** explicit instructions (sleep schedule, light review, no caffeine experimentation, where to be the night before)

### Honest tradeoffs

If my hours and weak areas don't allow full coverage:
- Name which topics get less time and why
- Identify the topics that, if cut entirely, would most hurt me
- Suggest the lowest-cost compromise

### A daily/weekly check-in protocol

How will I know mid-week if the schedule is working or not, and what's my decision rule for adjusting?

## Hard rules

- **No 7-day weeks.** Rest is required.
- **No schedules that ignore my stated constraints.** If I said I can't study after 8pm, don't schedule 9pm review.
- **Resource use must be specific.** "Read about X" is not specific; "Read Robbins ch. 12 pp. 423-441" is.
- **Don't promise comprehensive coverage if hours don't support it.** Tradeoff honesty.
- **Last 48 hours guidance is non-negotiable.** Include it.

## What I will NOT accept

- All days look the same (no week-over-week rhythm)
- Resource use vague enough to be wishful
- Pretending I can study comprehensively when I can't
```

## Expected output

A week-by-week schedule with daily breakdown, named rest days, a rescue week, pre-exam-week and 48-hour guidance, honest tradeoffs section, and a mid-cycle check-in protocol. Length varies with weeks; usually 800-1500 words.

## Common failure modes

- **Aspirational hours that don't match what you said.** Push back.
- **Topics all weighted equally despite your gap profile.** Push back: "Give weak topics more time."
- **No rescue week.** Push back.
- **48-hour instructions missing.** Push back.

## Required human verification

- Run the schedule by a colleague who's recently taken the same exam. They'll spot infeasibilities you and the model both miss.
- Adjust at end of week 2 based on actual sustainability. The initial plan is a hypothesis.
- If clinical work continues during prep, talk to your program director about whether the schedule is compatible with your rotation responsibilities.

## Best model and why

**Claude Sonnet 4.6** — week-by-week structured planning with constraints is well within Sonnet's range. **Opus** is overkill unless the situation is unusual (re-take, very compressed time, complex life constraints).
""")

write_prompt(
    "library/pillar-1-self-education/prompts/question-bank-gap-analysis.md",
    {"title":"Question bank gap analysis","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"intermediate","time_to_use":">10min","visual":"text-only",
     "tags":"board-prep, gap-analysis, metacognition","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Takes a list of qbank questions you've missed and identifies the underlying *concept gaps* — not the surface-level facts you didn't know, but the recurring patterns of misunderstanding that explain why those specific questions fooled you. Then ranks the gaps by impact and produces a targeted review plan for the top gap.

The key discipline this prompt enforces: distinguishing a *concept gap* (you don't understand the underlying mechanism) from a *recall failure* (you knew the fact but couldn't retrieve it under time pressure). The interventions for each are different.

## When to use it

After a substantial block of qbank questions (50+) where you've underperformed, especially if you can't immediately see why. Also useful as a periodic check during board prep — gap analysis every 100 questions is more useful than gap analysis at the end.

**Not for:** small samples (5-10 missed questions is noise), questions you missed for non-knowledge reasons (timing, misreading), or as a substitute for talking through specific cases with an attending.

## The prompt

```
You are doing a gap analysis on questions I missed. Your job is to find the UNDERLYING patterns, not just enumerate the facts I didn't know. Distinguish concept gaps from recall failures — the interventions are different.

## What I'm pasting

For each missed question:
`topic — what the question tested — why I missed it (my honest assessment)`

Example:
- `Plasma cell neoplasms — distinguishing MGUS from smoldering MM — I knew the criteria but defaulted to the wrong threshold`
- `Hemostasis — interpreting mixing studies — I didn't understand what the mixing study actually shows mechanistically`

[paste your list, 10-50 entries]

## What to produce

### 1. Cluster the misses into 2-5 concept clusters

A cluster is a recurring *kind* of misunderstanding, not just a topic area. Examples of good cluster names:
- "Confusing inherited vs acquired in coagulation disorders"
- "Cutoff thresholds in plasma cell neoplasms"
- "Mechanism-to-finding inferences in lab medicine"

For each cluster:
- List the missed questions that belong in it
- State the underlying gap in 1-2 sentences
- **Mark whether this cluster is a concept gap or a recall failure** (or mixed)

### 2. Rank the clusters by impact

Which gap, if filled, would resolve the most other questions? Justify the ranking — don't just list.

### 3. Targeted review plan for the TOP cluster

For the highest-priority gap:
- **Specific resources:** which chapter, paper, or video addresses this cluster directly
- **Targeted qbank topic to drill next:** name the qbank subtopic
- **Estimated hours needed:** be honest, not aspirational
- **A check question:** how will I know I've actually closed this gap?

### 4. The "don't worry about it" list

Anything in my misses that's low-yield for the exam and not worth fixing in the time I have. Be specific — name the questions.

### 5. Meta-pattern

After the cluster analysis: is there a single META-pattern across all my misses? (e.g., "I'm faster than I should be on multi-step questions and miss the second step", "I anchor on the first plausible answer", "I'm strong on facts but weak on integration")

## Hard rules

- **Distinguish concept gaps from recall failures explicitly** — different interventions.
- **Cluster names must describe the gap, not just the topic.**
- **The "don't worry about it" list cannot be empty.** Real qbank data always includes some questions not worth re-studying.
- **The targeted review plan must be specific.** "Read more" is not a plan; "Read Henry chapter 38, then drill the qbank 'PCN cutoffs' subtopic for 90 min" is.

## What I will NOT accept

- Topic-name clusters dressed up as concept clusters
- All clusters labeled "high priority"
- Empty "don't worry about it" list
- Aspirational hours that ignore my actual time budget
```

## Expected output

Clusters with concept-vs-recall labels, ranked by impact, with a specific review plan for the top cluster, an honest "don't worry about it" list, and a meta-pattern observation.

## Common failure modes

- **Model treats every miss as equally important.** Push back: "Rank by impact."
- **Cluster names are just topic names.** Push back: "Name the gap, not the topic."
- **Review plan is vague.** Push back for specific resources and hours.
- **No "don't worry about it" list.** Push back: "Be honest — what's low-yield?"

## Required human verification

- Validate cluster boundaries — does the cluster naming match how YOU think about your gaps?
- The "don't worry about it" list should be validated against your program's emphasis and your exam's blueprint.
- Talk through the meta-pattern with a colleague — sometimes the model sees a pattern that's actually noise, or misses a real pattern.

## Best model and why

**Claude Opus 4.7** — pattern recognition across many missed questions is exactly where Opus pulls away from Sonnet. The cluster-naming discipline and the concept-vs-recall distinction reward depth. **Sonnet** works for shorter lists (≤15 questions) where the clustering is more obvious.
""")

write_prompt(
    "library/pillar-1-self-education/prompts/diagnostic-algorithm-walkthrough.md",
    {"title":"Diagnostic algorithm walkthrough","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"algorithm, diagnostic-workup, guidelines","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Walks through a published diagnostic algorithm step by step — not just naming what happens at each decision point but explaining *why* the question is being asked there, what the answer rules in or out, what the common pitfalls are, and which decision point is most clinically consequential to get right.

Algorithms are easy to apply mechanically and hard to apply with judgment. This prompt builds the judgment.

## When to use it

When you're encountering a clinical algorithm for the first time, when you've used one mechanically without really understanding why each branch exists, or the night before sign-out where the algorithm will come up.

**Not for:** algorithm lookup (just look at the published algorithm), real-time clinical application (use the actual algorithm + your attending), or generating new algorithms (different task).

## The prompt

```
You are walking me through a published diagnostic algorithm. Be specific to the published version. Don't generalize to "similar" protocols.

## What I'm asking about

- **Algorithm:** [exact name and version — e.g., "ISTH 2018 overt DIC scoring", "BSH 2023 guideline for warfarin reversal", "2022 ELN AML response criteria"]
- **My level:** [PGY level + relevant context]
- **What prompted this:** [optional — a case, a board question, a teaching session]

## Version disclosure first

State the version of the algorithm you're walking through. If the algorithm has been substantially revised in the last 5 years, note BOTH:
- The version you're describing
- What changed in the revision (and why it matters clinically)

If you're not certain which version is current, say so explicitly.

## What to produce — node by node

For each decision point in the algorithm:

1. **The question or test being asked at this node** (stated precisely)
2. **Why this question is being asked HERE** — what does the answer rule in or rule out at this point in the workflow?
3. **What happens if positive/yes** — next node, immediate management implication
4. **What happens if negative/no** — next node, what's been ruled out
5. **The common pitfall at this decision point** — the specific way residents mis-apply this step (not "be careful," but "residents often forget that this test has a 24-hour turnaround and order it before they're committed to the rest of the algorithm")

After walking through every node:

### The single most clinically consequential decision point

Of all the nodes in this algorithm, which one carries the highest cost of error? Why? What does getting it wrong cause?

### How to avoid those errors

Specific cognitive moves: a verification step, a sanity check, a question to ask before committing.

## Hard rules

- **Be specific to the published version.** If your version is 2024 and I'm using 2018 at my institution, the discrepancy matters.
- **Pitfalls must be specific, observed-from-real-practice.** Not generic.
- **Do not invent algorithm nodes.** If you're uncertain about the exact structure, ask me to paste the algorithm.
- **Source the algorithm name and year.** Society + version + year.
- **Acknowledge uncertainty** about whether the algorithm has been revised since your training data.

## What I will NOT accept

- Walkthrough that could apply to any "similar" algorithm
- Generic pitfalls ("don't forget to check the value")
- Confidently named cutoffs that aren't in the actual algorithm
- No version disclosure
```

## Expected output

Per-node walkthrough (question / why / yes branch / no branch / pitfall) followed by the most-consequential-node analysis. Length scales with number of nodes; typically 400-800 words for a 5-7 step algorithm.

## Common failure modes

- **Two similar algorithms conflated** (ISTH overt vs non-overt DIC criteria, for example). Push back: "Which one are you walking through?"
- **Pitfalls generic** rather than specific. Push back.
- **Invented or misremembered cutoffs.** Verify against the actual algorithm.

## Required human verification

- **Verify the walkthrough against the actual published algorithm.** Society guideline, original paper, institutional protocol — whatever the authoritative source is.
- **Verify the version is current.** Algorithms get revised; the model may reference an older version without flagging.
- **Pressure-test the "most consequential node" with an attending who uses this algorithm regularly.** Their clinical experience reveals which errors actually cause harm vs which are theoretical.

## Best model and why

**Claude Opus 4.7** — multi-step algorithm walkthroughs with specific guideline versions reward Opus's depth. Sonnet works but more often conflates similar protocols.
""")

write_prompt(
    "library/pillar-1-self-education/prompts/forward-case-drill.md",
    {"title":"Forward case drill — diagnosis to expected findings","pillar":"self-education",
     "event_type":"n/a","audience":"resident","difficulty":"intermediate","time_to_use":"2-10min",
     "visual":"text-only","tags":"case-based, drilling, expected-findings","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Reverses the usual study direction: instead of given-findings-name-diagnosis, you name a diagnosis and the model generates the full constellation of findings you would expect, labeled by diagnostic weight (pathognomonic / highly supportive / supportive / non-specific) and including the findings that would RULE THE DIAGNOSIS OUT.

The discipline this builds: distinguishing features that are *truly pathognomonic* from features that are *highly characteristic* — a distinction over-collapsed in most learning resources.

## When to use it

When you're studying a diagnosis you've read about but haven't seen many times. Also useful as the second step in a learning chain after [Concept explanation at level](library.html#/library/pillar-1-self-education/prompts/concept-explanation-at-level) — first understand the entity, then drill the findings.

**Not for:** real case interpretation (different prompt and different stakes), exhaustive textbook coverage (just read the chapter), or first-time learning of the entity (concept explanation first).

## The prompt

```
You are generating the expected-findings constellation for a diagnosis I'm studying. Be strict about labeling pathognomonic features — over-labeling is the most common failure mode here.

## What I'm studying

- **Diagnosis:** [exact entity name — e.g., "follicular lymphoma, grade 1-2", not just "FL"]
- **My level:** [PGY level + relevant rotation context]
- **Why I'm studying it:** [optional — board prep, sign-out, teaching prep]

## What to produce — 5 sections

### 1. Clinical presentation

- Demographics (age range, sex, predisposing factors)
- Common symptoms and presentations
- Typical workup that brings the patient to pathology
- Common comorbidities or associations

### 2. Laboratory findings

- What's elevated, what's low, what's normal-but-tested (with reference ranges)
- Findings that would specifically be ordered for this differential
- Findings that should be normal in this entity (negative findings matter)

### 3. Imaging findings

- Modality typically used
- What's seen, organized by what's diagnostic vs supportive

### 4. Morphologic and histopathologic findings

- Low power: architecture, distribution
- Mid power: cell populations, stromal context
- High power: cellular detail (nuclear features, cytoplasm)
- IHC: typical positive and negative stains, with clone where clone-dependent
- Molecular: characteristic alterations, with source for each

### 5. Findings that RULE THE DIAGNOSIS OUT

This is the most underrated section. What negative findings should make you reconsider? What positive findings would force you to switch to a different diagnosis?

## Labeling — strict rules

For EVERY finding, label it:
- **[Pathognomonic]** — UNIQUE to this diagnosis. If a finding appears in any other entity, it's not pathognomonic. Almost no features are truly pathognomonic.
- **[Highly supportive]** — Strongly suggests this diagnosis but not unique
- **[Supportive]** — Consistent with the diagnosis but also present in others on the differential
- **[Non-specific]** — Common but doesn't help discriminate

Over-labeling pathognomonic findings is the most common failure mode. If in doubt, downgrade.

## Source any specific value

Cutoffs, reference ranges, percentages, classification criteria — cite the source: `[WHO HAEM5]`, `[NCCN v2.2024]`, etc.

## After the constellation

Ask me ONE question: "On a sign-out, which 2-3 findings would you prioritize describing, and why?"

Wait for my answer before discussing.

## Hard rules

- Strict pathognomonic discipline
- Source any specific value
- Include negative findings (Section 5 is non-negotiable)
- IHC clones named where clone-dependent
- No invented features

## What I will NOT accept

- Liberal use of "pathognomonic"
- Section 5 (rule-out findings) omitted
- Specific values without sources
- Cell-by-cell description rather than weighted by diagnostic importance
```

## Expected output

5 sections covering clinical / lab / imaging / morphology / rule-out findings, each finding labeled by diagnostic weight, sourced values, ending with a prioritization question for you.

## Common failure modes

- **Over-use of "pathognomonic."** Push back: "Verify — is this finding actually unique to this entity, or does it appear in [related entity]?"
- **Section 5 (rule-out) is thin or omitted.** Push for it.
- **Missing IHC clone information** where it matters.

## Required human verification

- Verify the pathognomonic labels against your subspecialty's current reference. The model overuses the label.
- Cross-check the morphologic findings against your subspecialty atlas.
- Verify any cited classification version is current.

## Best model and why

**Claude Opus 4.7** — distinguishing pathognomonic from supportive findings requires both medical knowledge depth and discipline about labels. Opus is more careful with this distinction than Sonnet.
""")

write_prompt(
    "library/pillar-1-self-education/prompts/negative-drill.md",
    {"title":"Negative drill — what would change the diagnosis","pillar":"self-education",
     "event_type":"n/a","audience":"resident","difficulty":"advanced","time_to_use":"2-10min",
     "visual":"text-only","tags":"disconfirmation, counterfactual-reasoning","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Trains the habit of *disconfirmation*: take a working diagnosis you're confident in and ask the model to enumerate the findings or test results that would force you to reconsider, ranked by **clinical likelihood** rather than exoticism. The output should surface the boring, common ways you could be wrong — not the zebra alternatives.

This counters the well-documented confirmation bias in diagnostic reasoning: once we have a working diagnosis, we look for evidence that supports it and discount evidence that doesn't.

## When to use it

When you have a working diagnosis you're confident in, especially:
- Before sign-out, when the consequences of being wrong are high
- For diagnoses you've seen rarely and want to stress-test
- During study of a topic where you've gotten over-confident
- Before a tumor board where you'll defend your diagnosis

**Not for:** real-time clinical interpretation (different stakes), academic devil's advocate exercises (this is calibrated to clinical decision-making), or when you don't actually have a working diagnosis yet.

## The prompt

```
I have a working diagnosis. Your job is to stress-test it by enumerating what would force me to reconsider. Rank by CLINICAL LIKELIHOOD — the most likely way I'm wrong is usually a common condition presenting atypically, not a rare zebra.

## The case

- **My working diagnosis:** [exact entity]
- **Clinical context (de-identified):** [age range, sex if relevant, brief presentation, key positive findings — no PHI]
- **My confidence level:** [low / moderate / high — be honest]
- **What I want stress-tested:** [optional — e.g., "I'm worried I anchored on this", "I want to make sure I'm not missing something common"]

## What to produce — 3 tiers + alternative + discriminating test

### Tier 1: Findings that would force COMPLETE RECONSIDERATION

Rule out the working diagnosis entirely. For each:
- The finding
- One sentence: why does this finding contradict the working diagnosis?
- One sentence: what does it suggest instead?

### Tier 2: Findings that would EXPAND the differential

Don't rule out, but suggest a different category of disease is also in play. For each, same structure.

### Tier 3: Findings that are INCONSISTENT BUT DON'T NECESSARILY CHANGE the diagnosis

Worth noting in the report or follow-up, may indicate complication or atypical presentation.

### The single most likely alternative diagnosis

If you're wrong, what is the SINGLE MOST LIKELY alternative — not the most interesting alternative, the most likely? Justify by saying what makes this alternative compete with the working diagnosis on this case's specific features.

### The ONE test to discriminate

If you could order one test to distinguish your working diagnosis from the most likely alternative, what is it? Justify in one sentence.

## Hard rules

- **Rank by clinical likelihood, not by exoticism.** The most likely way I'm wrong is rarely a rare zebra.
- **Don't pad with implausible alternatives** to look comprehensive.
- **The "one test to discriminate" must have meaningful discriminating power** for THIS pair of differentials. Don't suggest a test that's already negative.
- **Acknowledge if the working diagnosis is genuinely well-supported.** If the case is unambiguous, say so — don't manufacture doubt.

## What I will NOT accept

- A list of rare alternatives without a common one
- An "alternative" that's been excluded by basic workup
- A "discriminating test" with low specificity for the pair
- Pretending the case is more ambiguous than it is
```

## Expected output

3 tiers of disconfirming findings + the single most likely alternative + the one discriminating test. Length 400-600 words.

## Common failure modes

- **Exotic alternatives ranked above common ones.** Push back: "What's the COMMON way I could be wrong?"
- **Discriminating test that's not actually discriminating** for this pair.
- **Manufactured doubt** about a well-supported case. Push back if doubt feels strained.

## Required human verification

- This is a thinking exercise; the model's specific suggestions are starting points.
- If a specific test is recommended, verify it's the right test for the discrimination you actually need.
- Talk through the alternative with an attending if the case is genuinely high-stakes.

## Best model and why

**Claude Opus 4.7** — counterfactual reasoning and ranking by clinical likelihood require both medical knowledge depth and judgment about pretest probability. Sonnet tends to surface rarer alternatives first; Opus is better calibrated to common-things-common.
""")

write_prompt(
    "library/pillar-1-self-education/prompts/journal-club-preread.md",
    {"title":"Journal club pre-read prep","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"quick-win","time_to_use":"2-10min","visual":"text-only",
     "tags":"journal-club, preparation, literature","verified_models":"TODO",
     "best_model":"Claude Opus 4.7 with paper attached","last_updated":"2026-05-17"},
    """## What this prompt does

Generates a one-page pre-read for a journal club paper that attendees can actually use to arrive prepared. Includes background context, study summary with specific numbers, named strengths and limitations, and five discussion questions ordered from concrete to contested.

The most important guardrail: if the model doesn't have the actual paper text, it should refuse to produce the pre-read rather than fabricating content. A pre-read with invented numbers is worse than no pre-read.

## When to use it

When you're hosting journal club and want attendees to arrive prepared rather than reading the paper for the first time during the discussion. Also useful as a personal pre-read for any paper you'll be discussing.

**Not for:** generating the full presentation (different scope), as a substitute for actually reading the paper if you'll be presenting, or methods critique (use the [Paper methods critique](library.html#/library/pillar-1-self-education/prompts/paper-methods-critique) prompt for that depth).

## The prompt

```
You are creating a one-page pre-read for a journal club discussion. Quality depends entirely on whether you actually have the paper text. Honesty about that comes first.

## Honesty check — answer first

Do you have access to the full paper text (attached PDF, pasted full text, or otherwise)? Confirm explicitly. If you only have the title, abstract, or citation, STOP and tell me — do not generate a pre-read that invents numbers, methods, or quotes.

## What I'm requesting

- **Paper:** [DOI, citation, attached PDF, or pasted full text]
- **Audience:** [PGY level mix, plus faculty]
- **Discussion format:** [traditional walk-through / structured critique / debate / structured pro-con]
- **My role:** [presenter / discussant / attendee]

## Pre-read structure (one page, ~400-500 words)

### 1. Clinical or scientific context (3-4 sentences)

Why was this question worth asking? State of the field before this paper — what was open, what was contested, what was the gap.

### 2. The study in one paragraph (5-7 sentences)

Population, methods, key results with specific numbers. Neutral framing — not yet interpretive. Use the paper's own language for the design type (RCT, retrospective cohort, etc.).

### 3. What this paper is good at (1-2 specific strengths)

A specific design or analytic strength that strengthens the interpretation. Not "well-written" — something methodologic.

### 4. What this paper is not good at (1-2 specific limitations)

A specific limitation that constrains interpretation. Not "small sample size" if N=5000. Be specific about WHY the limitation matters.

### 5. Five discussion questions, ordered concrete → abstract → contested

- **Q1 (concrete, methods):** A question about a specific design choice or analytic decision. Answer should be in the paper.
- **Q2 (finding-level):** How confident should we be in the headline result given the design?
- **Q3 (generalizability):** Does this apply to our patient population? What about ours specifically would limit applicability?
- **Q4 (practice-change):** Should this change what we do? If yes, in what specific setting and for which patients?
- **Q5 (contested):** A question where reasonable people would genuinely disagree. Should provoke real debate.

### 6. Attendee preparation note (1 sentence)

What attendees should think about before arriving.

## Hard rules

- **Honesty check at the top.** If you don't have the paper, refuse.
- **Specific numbers from the paper, not vague characterizations.** "27% reduction (95% CI 18-35)" not "significant reduction".
- **The contested question must be genuinely contested,** not just dressed-up settled material.
- **Strengths and limitations must be specific** to this paper's design, not generic.
- **No PHI.**

## What I will NOT accept

- A pre-read generated from the title and abstract alone, dressed up as if the model read the paper
- Fabricated specific numbers or quotes
- Discussion questions that have obvious right answers (Q5 included)
- Generic strengths/limitations
```

## Expected output

A 6-section one-page pre-read (~400-500 words). Suitable for sending to attendees a week ahead.

## Common failure modes

- **Pre-read built from title alone.** Honesty check at top is designed to prevent this — verify the model actually has the paper.
- **Contested question that has an obvious answer.** Push back: "That's settled. Find a genuinely contested one."
- **Fabricated numbers.** Verify against the paper.

## Required human verification

- Verify all specific numbers against the paper.
- Pressure-test the contested question with a colleague — if they immediately agree with you, it's not actually contested.
- If the honesty check answer is "I only have the abstract," discard the pre-read and provide the paper text first.

## Best model and why

**Claude Opus 4.7 with PDF attached** for substantive engagement with the paper. **Gemini 2.5 Pro** if the paper is unusually long. Without the actual paper text, every model fabricates — the model choice doesn't save you.
""")

write_prompt(
    "library/pillar-1-self-education/prompts/multimodal-spep-ife.md",
    {"title":"SPEP / IFE trace interpretation walkthrough","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"advanced","time_to_use":"2-10min","visual":"multimodal",
     "tags":"multimodal, spep, ife, paraprotein","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Walks through SPEP or IFE interpretation as a guided drill — you commit at each step before the model reveals what it sees. Builds the regional reading discipline (orient → describe each region → identify abnormality → integrate → interpret) that distinguishes structured pattern recognition from gestalt guessing.

## When to use it

First month of clinical chemistry, when you're trying to build the SPEP/IFE reading reflex. Especially useful when reading a published teaching atlas of traces.

**Not for:** real patient traces (use your scope and your attending), settled cases (look up the answer), or first-time learning of SPEP fractions (read about the regions first).

## Safety

Published teaching atlases, public-domain images, or your legitimately-cleared teaching collection only. No real patient material. See [Guardrails](library.html#/docs/guardrails).

## The prompt

```
You are my SPEP/IFE interpretation drill partner. Strict interaction protocol: quiz me about a region, wait for my answer, confirm or correct, then move to the next region. Do not reveal your full interpretation until I commit.

## What I'm uploading

- **Test type:** [serum protein electrophoresis (SPEP) / urine protein electrophoresis (UPEP) / immunofixation electrophoresis (IFE) / serum free light chains report]
- **Patient context (if known):** [optional, de-identified]
- **Source:** [confirm: teaching atlas / public-domain / cleared collection]

## Strict protocol

### Phase 1: Orient

Confirm what test we're looking at, the cathode and anode orientation, the fractions visible (albumin, alpha-1, alpha-2, beta-1, beta-2, gamma), and the densitometry tracing if present.

### Phase 2: Region-by-region quiz

For each region in order (albumin → alpha-1 → alpha-2 → beta → gamma):

1. **Quiz me:** "What do you observe in the [region]?" Wait for my answer.
2. **Confirm or correct:** If I'm right, brief confirmation. If wrong, name the specific morphologic feature I missed.
3. **Move to the next region** with another quiz prompt.

### Phase 3: Integration

After we've worked through every region, ask me:
- "What is the most striking abnormality on this trace?"
- "Based on the pattern, what's your differential?"
- "What additional testing would you order, and why?"

Wait for my commitment.

### Phase 4: Reveal

ONLY after I commit, give your full interpretation including:
- Pattern type (e.g., monoclonal gammopathy, polyclonal hypergammaglobulinemia, hypogammaglobulinemia, beta-gamma bridging)
- Differential
- Recommended additional testing
- The published diagnosis if you can infer the source

## Hard rules

- One region at a time. Wait for my answer.
- If a finding is ambiguous (borderline M-spike vs polyclonal), say so explicitly — do not commit to one interpretation.
- Do not invent peaks or fractions you don't actually see in the image.
- Do not reveal the diagnosis until I commit.
- If I don't know how to read a region, briefly orient me to what to look for, then re-ask.

## What I will NOT accept

- Revealing the diagnosis before I commit
- Confident overcalls of borderline M-spikes
- Inventing fractions or peaks that aren't in the trace
- Skipping regions because they look normal (normal is a finding worth confirming)
```

## Expected output

A back-and-forth: orient → 5 region quizzes (one at a time) → integration questions → your committed interpretation → model's full interpretation and published answer.

## Common failure modes

- **Model reveals the diagnosis prematurely.** Push back: "Stop. I haven't committed yet."
- **Model commits to a borderline M-spike** without acknowledging ambiguity.
- **Model invents an IFE band that isn't there.** If you can't see what the model is describing, ask it to specify where in the image.

## Required human verification

- Provenance check before uploading.
- Compare against the published key for the teaching case.
- For borderline calls (small M-spikes, equivocal IFE bands), trust the published answer over your or the model's read.

## Best model and why

**Claude Sonnet 4.6** — handles structured visual interpretation (gels, traces) well and respects the quiz-first protocol. **Gemini 2.5 Pro** is comparable; pick whichever you have image-attachment access to.
""")

# ===========================================================================
# PILLAR 2 — 5 NEW PROMPTS + 5 REFINED
# ===========================================================================

# --- NEW P2 #1: Microscopy teaching session design ---
write_prompt(
    "library/pillar-2-teaching/prompts/microscopy-teaching-session.md",
    {"title":"Microscopy teaching session design","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"intermediate","time_to_use":">10min","visual":"text-only",
     "tags":"teaching, microscopy, image-based, session-design","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Designs a microscopy-anchored teaching session built around 6-10 images rather than slides of text. Generates per-image talking points, discussion questions, and the teaching arc that holds the images together — not just a parade of cases.

The key discipline this prompt enforces: the SESSION has a teaching argument, and each image is selected to advance that argument. Image-based teaching is not "here are some cases" — it's a structured progression.

## When to use it

When you've been asked to give an unknown-cases conference, run a multi-headed microscopy session, or build a self-paced image-based learning module. Especially useful when you have an image collection and need to organize it into teaching.

**Not for:** designing a lecture with slides of text (use [Slide outline for a 1-hour lecture](library.html#/library/pillar-2-teaching/prompts/slide-outline-1hr)), generating images (different problem), or teaching that doesn't have microscopy at the center.

## The prompt

```
You are designing an image-anchored microscopy teaching session. The session must have a teaching argument — a thread that connects the images. Don't give me a parade of cases.

## What I'm building

- **Session topic:** [be specific — e.g., "subtypes of follicular lymphoma and their mimics", not just "lymphoma"]
- **Audience:** [PGY level + subspecialty rotation context]
- **Session duration:** [in minutes]
- **Format:** [multi-headed scope / unknown slide quiz / projected images / web-based teaching set]
- **Image collection I have available:** [describe — e.g., "12 cases including 3 FLG1-2, 2 FLG3A, 2 follicular hyperplasia, 1 marginal zone, 4 other lymphomas"]
- **What learners should walk away with:** [the one thing they should be able to DO after — be specific]

## What to produce

### 1. The teaching argument (1 sentence)

What is the THESIS of this session? Not the topic — the argument. Example: "By the end of this session, residents will be able to distinguish FL from its mimics by attending to architectural patterns at low power, not just immunoprofile."

### 2. Image sequence (6-10 images)

For each image:
- **Position in the session** (with timing)
- **What it shows** (one sentence)
- **Why it's in this position** — how does it advance the teaching argument?
- **The teaching beat:** what you'll say or ask at this image (NOT a textbook description — the specific point this image makes in the session)
- **One question to ask the audience** at this image
- **Anticipated wrong answer** and how to use it as a teaching moment

### 3. Image-to-image transitions

Between images, what's the bridge? "This case showed X; the next case shows what happens when X is absent." Transitions are where learning consolidates.

### 4. The reveal moment

Most image-based sessions have a "reveal" — the unexpected case, the trick, the point where the audience's pattern breaks. Identify where it is in your session and what makes it work.

### 5. Closing synthesis

How do you tie the session together at the end? Not "any questions" — the explicit reinforcement of the teaching argument with the specific evidence the images supplied.

## Hard rules

- The session has a teaching argument, stated explicitly
- Each image advances the argument
- Transitions are explicit, not assumed
- The reveal is identified
- Closing synthesis ties back to the opening thesis

## What I will NOT accept

- "Here are some cases" structure without an argument
- Images that are interesting but don't connect
- A closing that's "questions?" rather than synthesis
- Anticipated audience answers that are softball
```

## Expected output

A session plan with explicit argument, 6-10 images with positioning and teaching beats, transitions, reveal, and closing synthesis. Length 600-1000 words.

## Common failure modes

- **No teaching argument** — just a list of cases. Push back: "What's the thesis?"
- **Generic teaching beats** — "describe what you see" repeated 10 times. Push for the specific point each image makes.
- **Reveal feels arbitrary** — happens because the model didn't plan it. Push for a deliberate reveal.

## Required human verification

- Pilot the session structure with a colleague who teaches the same topic. Their feedback on what the audience actually learns matters more than the plan looks.
- Verify image diagnoses against the published key for each case.
- After the first delivery, write down what worked and what didn't. Image-based sessions improve with iteration.

## Best model and why

**Claude Opus 4.7** — structuring a multi-image teaching argument across 6-10 cases requires substantive synthesis. Opus produces tighter teaching arcs than Sonnet. The reveal-moment design also benefits from Opus's narrative judgment.
""")

# --- NEW P2 #2: Sign-out teaching turn ---
write_prompt(
    "library/pillar-2-teaching/prompts/sign-out-teaching-turn.md",
    {"title":"Sign-out teaching turn","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"quick-win","time_to_use":"<2min","visual":"text-only",
     "tags":"teaching, sign-out, capture-the-moment","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Converts a sign-out moment — a case that just came up, a finding that's worth pausing on, a question a resident asked — into a structured 3-5 minute teaching point you can deliver in the flow of the day. The model gives you the framing, the key question, the supporting points, and the wrap-up — calibrated to the seconds you have, not the hour you don't.

This captures what experienced attendings do instinctively but residents don't yet know how to do for themselves.

## When to use it

In the moment, at the scope or at sign-out, when you want to take 3-5 minutes to make a teaching point rather than just signing out the case. Also useful for senior residents who are being trained to teach in sign-out (resident-as-teacher).

**Not for:** designing formal teaching sessions (different scope), long-form explanations (use the concept explanation prompt instead), or replacing the diagnostic work of sign-out.

## The prompt

```
You are helping me turn a sign-out moment into a quick teaching point. Speed matters — I have 3-5 minutes inserted into a busy sign-out, not an hour to prepare a lecture.

## The moment

- **The case or finding I'm at:** [brief — e.g., "atypical mitosis in a parathyroid adenoma, on a resident's sign-out tray"]
- **The resident's level:** [PGY level + subspecialty rotation]
- **The question I want to teach to:** [the specific point this moment surfaces — e.g., "when does an atypical mitosis change the diagnosis vs when is it incidental?"]
- **Time I have:** [3 min / 5 min — be honest]

## What to produce — in this exact structure

### 1. The hook (1 sentence)

The opening line that makes the resident pause and pay attention. Not "let me teach you something" — the specific framing that turns this case into a question worth pursuing.

### 2. The question (1 sentence)

The exact question you'll ask the resident. They should be able to answer in 30-60 seconds.

### 3. The teaching points (2-3 bullets, MAX)

The substantive content. Each bullet:
- A specific point that follows from the question
- Why it matters clinically
- Tied to what you both can see in this case

### 4. The closing pivot (1 sentence)

How you wrap up and return to sign-out — making the teaching feel like a 30-second beat rather than an interruption.

### 5. The follow-up call-back (1 sentence)

A specific question you'll ask the same resident next week to check whether the teaching stuck.

## Hard rules

- **Calibrated to the time available.** A 3-minute teach is structured differently than a 5-minute teach.
- **Specific to THIS case.** Not generic teaching points that could apply to any version of the case.
- **The opening must hook the resident in.** "I want to make a teaching point" is not a hook.
- **The closing must return to sign-out** — don't leave the resident in teaching mode.
- **The follow-up call-back is non-negotiable.** Teaching that's not called back is teaching that's forgotten.

## What I will NOT accept

- A 5-bullet list when 3 is enough
- A generic opening
- Teaching points untethered from what's on the scope
- No follow-up call-back
```

## Expected output

Five lines: hook, question, 2-3 teaching points, closing pivot, follow-up call-back. Total content fits on a sticky note. Total speaking time matches what you said you had.

## Common failure modes

- **Too long.** A 5-minute teaching point becomes a 15-minute lecture. Push back: "Cut it. I have 3 minutes."
- **Generic hook.** Push back: "Make it specific to this case."
- **No follow-up call-back.** Push back: "What do I ask next week to check?"

## Required human verification

- Time yourself once on a real sign-out. The model's "3 minutes" may be optimistic for your speaking pace.
- After the teach, observe whether the resident actually picks up the concept. If they don't, the framing was wrong — adjust for next time.
- The follow-up call-back only works if you actually do it. Schedule a reminder.

## Best model and why

**Claude Sonnet 4.6** — fast, structured outputs at the right granularity. Opus would over-elaborate; Haiku might be too terse.
""")

# --- NEW P2 #3: Tumor board prep coaching ---
write_prompt(
    "library/pillar-2-teaching/prompts/tumor-board-prep-coaching.md",
    {"title":"Tumor board prep coaching","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"intermediate","time_to_use":">10min","visual":"text-only",
     "tags":"tumor-board, coaching, presentation-skills","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Coaches a resident who will present at tumor board. The model interviews them on the case, identifies where their presentation is weakest, and gives them specific drilling on the 2-3 highest-stakes questions board members will ask. This is meta-prompt — the PRESENTER uses it, not the audience.

## When to use it

When you're coaching a resident who will present at tumor board for the first time, or when a senior resident is presenting a complex case where the consequences of a poor presentation are high.

**Not for:** preparing your own tumor board presentation (you should know your own gaps), generating the case packet itself (different prompt), or replacing real practice runs with your team.

## The prompt

```
You are coaching me through preparing to present a case at tumor board. Interview me, find the weak spots in my presentation, and drill the 2-3 highest-stakes questions board members will ask.

## What I'm presenting

- **Case (de-identified):** [paste your case summary — pathology, imaging, history, current question for the board]
- **Tumor board specialty:** [GU MDTB, GI MDTB, breast MDTB, lung MDTB, etc.]
- **Anticipated attendees:** [med onc, rad onc, surgery, radiology, others]
- **The decision the board needs to make:** [the explicit question I'm bringing]
- **My role on the team:** [my level + how long I've been on this service]
- **What I'm nervous about:** [optional — but useful]

## How to coach me — 4 phases

### Phase 1: Walk-through

I'll talk you through my draft presentation. You listen. Don't interrupt unless I ask. Just take note of:
- Where my framing is weakest
- Where I'm using imprecise language
- Where the decision question is unclear or buried
- Where I'm under-prepared for likely follow-up

Ask me to walk through it first before any feedback.

### Phase 2: Targeted feedback

After my walkthrough, give me feedback in this order:
1. **The single most important fix.** What's the one change that would most improve my presentation?
2. **Second and third priorities.** Two more specific improvements, ranked by impact.
3. **What's working well.** Specific strengths, not "great job."

### Phase 3: The 2-3 highest-stakes questions

For my case, anticipate the 2-3 most likely follow-up questions from board members and walk me through how to answer each:
- The question (phrased as the actual board member would ask it)
- The 2-3 sentence response with the supporting data
- The follow-up question that would likely come next
- Any pre-prepared slide or data point I should have queued up

Cover at minimum: one question from the med onc, one from radiology or surgery (whichever is more relevant), and one from a generalist (medical director, board chair).

### Phase 4: The simulation

Now play the role of the most likely tough questioner at MY institution's board (you may need to ask me what they're like). Ask me one question. I'll respond. You'll give me feedback.

Do 2-3 rounds.

## Hard rules

- **Don't lecture me about the case.** This is about the presentation, not the medicine.
- **Be specific in feedback.** "Be more confident" is useless; "When you said 'I think this is high-grade,' say 'this is high-grade' instead" is useful.
- **The simulation is for practice, not assessment.** Push me, but don't grade me.

## What I will NOT accept

- Generic presentation tips
- Feedback that's all positive or all negative
- Anticipated questions that softball the case
- Skipping the simulation
```

## Expected output

A 4-phase coaching conversation: walkthrough → targeted feedback → 2-3 highest-stakes questions with response framing → 2-3 rounds of simulated tough questions.

## Common failure modes

- **Generic feedback** ("be clear, be confident"). Push for specific.
- **Softball anticipated questions.** Push back: "What's the question they'd ask if they wanted to challenge me?"
- **Skipping the simulation.** Make sure you actually do the practice rounds.

## Required human verification

- The model doesn't know your institution's specific board dynamics. Validate the anticipated questions with someone who attends regularly.
- Practice the simulation aloud — speaking is different from reading.
- After the actual board, write down what was asked vs what the model predicted. Use it to calibrate next time.

## Best model and why

**Claude Opus 4.7** — anticipating sophisticated medical questions and providing substantive coaching requires depth. Opus is better at playing the role of a tough questioner than Sonnet.
""")

# --- NEW P2 #4: Subspecialty rotation goals letter ---
write_prompt(
    "library/pillar-2-teaching/prompts/subspecialty-rotation-goals-letter.md",
    {"title":"Sub-specialty rotation goals letter","pillar":"teaching","event_type":"rotation",
     "audience":"resident","difficulty":"quick-win","time_to_use":"2-10min","visual":"text-only",
     "tags":"rotation, goal-setting, communication","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Drafts the "here's what I'd like to get out of this rotation" letter or email that a resident sends to their incoming rotation director a week or two before the rotation starts. Signals intent, sets expectations, and gives the rotation director something to plan around. The letter is short (under 200 words) but does real work.

This is an under-used communication move — most residents arrive on day 1 with no advance signal of what they want from the rotation. The letter changes that.

## When to use it

1-2 weeks before a rotation starts, when you want to arrive with a clear sense of what you're hoping to get out of it. Especially valuable for elective rotations and sub-specialty rotations where the attending has discretion about what to teach.

**Not for:** rotations where you've been assigned a strict curriculum (less leverage), as a substitute for an in-person orientation conversation, or for rotations where you don't actually have a clear sense of what you want.

## The prompt

```
You are drafting a short letter or email I will send to my incoming rotation director. Goal: signal intent, set realistic expectations, give them something to plan around. Tone: warm, specific, professional. Length: under 200 words.

## What I'm telling them

- **Rotation:** [name and dates]
- **My level:** [PGY level + subspecialty trajectory if relevant]
- **What I'd like to get out of this rotation:** [the 2-3 specific goals — e.g., "I'm going into hematopathology and want maximum exposure to flow cytometry interpretation"]
- **What I've already done that's relevant:** [optional — courses, prior rotations, projects]
- **What I'm flexible about / would defer to your judgment on:** [showing I'm not over-prescriptive]
- **Specific asks (if any):** [optional — e.g., "if possible, I'd love to attend at least one molecular sign-out"]
- **The rotation director's name and how I should address them:** [name + Dr./first name based on their preference]

## Letter structure (under 200 words)

1. **Greeting + acknowledgment of the upcoming rotation** (1 sentence)
2. **A short statement of who I am and why I'm excited about this rotation** (2-3 sentences) — specific, not gushing
3. **The 2-3 specific goals**, framed as "I'd be most grateful for opportunities to..." (3-4 sentences)
4. **A line acknowledging your flexibility** ("happy to defer to your judgment on what's possible given the case mix")
5. **A specific offer** (something I can bring — preparation, a topic I can present, willingness to come in early for sign-out)
6. **Close** (looking forward to learning, formal sign-off)

## Hard rules

- Under 200 words. Hard cap.
- Specific goals, not "I want to learn a lot"
- Tone that's confident without being entitled
- An offer of something I bring, not just a list of asks
- No empty intensifiers ("excited", "thrilled", "honored" — pick one and use sparingly)

## What I will NOT accept

- A letter over 200 words
- Generic goals
- All asks, no offers
- Tone that's either obsequious or presumptuous
```

## Expected output

A short, structured letter or email under 200 words. Should read like a thoughtful resident wrote it in 5 minutes, not like AI generated it.

## Common failure modes

- **Over-length.** Push back: "Cut it to 180 words."
- **Generic goals.** Push back: "What specifically?"
- **No offer.** Push back: "What do I bring?"

## Required human verification

- Read aloud — does it sound like you? If not, rewrite.
- Check the rotation director's preferred mode of address (some prefer first name, some Dr.).
- Send 1-2 weeks ahead, not 1-2 days. The point is to give them time to plan.

## Best model and why

**Claude Sonnet 4.6** — short professional correspondence is Sonnet's strength. Opus would over-elaborate; Haiku might miss the tone calibration.
""")

# --- NEW P2 #5: Difficult feedback conversation prep ---
write_prompt(
    "library/pillar-2-teaching/prompts/difficult-feedback-conversation-prep.md",
    {"title":"Difficult feedback conversation prep","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"advanced","time_to_use":">10min","visual":"text-only",
     "tags":"feedback, hard-conversation, professionalism","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Preps you for a feedback conversation that's harder than usual — a struggling resident, a professionalism concern, performance below expectations, or a conversation where you need to escalate to formal documentation. Generates an opening, a structure for the conversation, anticipated reactions, and the wording you'll need when the resident pushes back or becomes emotional.

This is the prompt you use when the conversation matters most and you don't want to wing it.

## When to use it

Before a feedback conversation where the stakes are high — a remediation plan, a professionalism concern, a discussion of board failure, or any conversation where you anticipate it will be hard. Use early enough to actually prep, not the day of.

**Not for:** routine end-of-rotation feedback (use [Resident feedback note drafting](library.html#/library/pillar-2-teaching/prompts/resident-feedback-note)), conversations that should be handled by your program director or DIO (escalate first), or situations involving safety concerns (those have specific institutional protocols).

## The prompt

```
You are helping me prepare for a difficult feedback conversation. The stakes matter, and I want to have my framing, evidence, and response patterns ready before I'm in the room. Help me think this through carefully.

## What I'm preparing for

- **Context:** [brief — e.g., "PGY-2 resident on second rotation in CP, struggling with autonomy and showing professionalism concerns around timeliness"]
- **The specific concern(s):** [the behaviors or patterns that prompted the conversation]
- **The evidence I have:** [specific observations, dates, comparable comparators if relevant]
- **What outcome I want:** [shared understanding / specific behavioral change / formal documentation / referral to program director]
- **My relationship with the resident:** [length, prior conversations, level of trust]
- **The setting:** [my office / a private room at sign-out / formal meeting with PD present]
- **My time budget:** [how long is the conversation]

## What to produce — 6 sections

### 1. The opening (3-4 sentences, verbatim)

Exactly what you'd say to open. The opening sets the entire conversation. Should:
- Establish that this is a serious conversation, not a passing comment
- Frame the conversation as constructive (toward a goal) not punitive
- Invite the resident to engage rather than defend

### 2. The evidence presentation

How to walk through specific observations without:
- Reading from a list (which feels prosecutorial)
- Being vague (which feels unfair)

Structure: pattern → specific examples → impact. Verbatim suggestion for one example walk-through.

### 3. The pause

After your evidence, give the resident space. The script:
- What to say to invite them to respond
- How long to wait (silence is OK)
- What to do if they don't say anything

### 4. Anticipated reactions and responses

For each likely reaction (denial, deflection, agreement, anger, tears, silence), give me:
- One sentence describing the reaction
- What to say in response — verbatim, calibrated to keep the conversation moving toward the desired outcome

Cover at minimum: denial, deflection ("I was busy"), agreement-without-change ("you're right, I'll try harder"), emotional response, escalation toward you (anger).

### 5. The agreement and next steps

How to close the conversation with:
- A shared understanding of what was discussed
- A specific, observable commitment from the resident
- A timeline for follow-up
- Who else needs to know (program director, CCC) and what gets documented

### 6. What I document afterward

The note I should write in the resident's file — what's appropriate, what isn't, how to keep it factual and concise.

## Hard rules

- **Verbatim suggestions where stakes are highest** (opening, response to emotional reactions, closing commitment).
- **Specific, not generic.** Generic feedback advice doesn't help in hard conversations.
- **The opening cannot be punitive or prosecutorial.** It also cannot be so soft that the seriousness of the issue is lost.
- **Anticipate the reactions I'm most likely to face given my context.** Don't give me a generic list.
- **Acknowledge that some situations require escalation.** If based on what I described this should involve the PD or DIO first, tell me.

## What I will NOT accept

- Generic feedback advice
- An opening that's all warm-and-fuzzy or all evaluative
- Anticipated reactions that don't match what I'm likely to face
- Closing without a specific commitment and timeline
```

## Expected output

Six sections covering the conversation arc. The opening and anticipated-reactions sections are the highest-stakes parts. Length 600-1000 words.

## Common failure modes

- **Generic feedback frameworks** (SBI, COIN, etc.) without specificity to your situation. Push back for specifics.
- **Soft opening** that fails to signal seriousness. Push back if the opening reads as casual.
- **Anticipated reactions that don't match the resident's actual likely response.** Push back if the reactions feel off.

## Required human verification

- **If the situation involves potential safety concerns, professionalism violations that may have institutional reporting requirements, or anything that could escalate to disciplinary action, consult your program director or your institution's relevant office BEFORE the conversation.** This prompt does not replace institutional process.
- **Run the opening by a trusted colleague.** Especially if you anticipate the conversation being especially hard, get a second read on the framing.
- **Practice the opening aloud.** Spoken delivery is different from written, and the opening matters most.

## Best model and why

**Claude Opus 4.7** — high-stakes conversational prep requires nuance, anticipation of reactions, and verbatim language calibrated to specific situations. Opus is materially better than Sonnet at this.
""")

# --- REFINED P2 #1: ACGME / EPA learning objectives ---
write_prompt(
    "library/pillar-2-teaching/prompts/acgme-epa-objectives.md",
    {"title":"ACGME / EPA learning objective generation","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"learning-objectives, acgme, epa, assessment","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Generates learning objectives in the format your CCC and program leadership expect: measurable verbs, conditions, criteria, and an explicit map to a specific ACGME milestone sub-competency or EPA. Also identifies the milestones your objectives do NOT address — useful context for program leadership.

## When to use it

Designing a new teaching session that needs documented objectives, updating a rotation block whose objectives are stale, or preparing materials for a program review where milestone alignment will be scrutinized.

**Not for:** general lesson planning (use slide outline prompt), session design that doesn't need formal milestone mapping, or replacing your program director's review of formal documentation.

## The prompt

```
You are generating learning objectives for a formal pathology training context. Format must be the one CCCs expect: measurable verb + condition + criterion + milestone or EPA mapping.

## What I'm generating objectives for

- **Session or rotation:** [name + duration]
- **Audience:** [exact PGY level + subspecialty rotation context — e.g., "PGY-2 CP residents in their second month of blood bank"]
- **Number of objectives:** [usually 3-7]
- **My program uses:** [ACGME milestones / EPAs / both — name which]
- **The milestone document version I'm working from:** [name + year — e.g., "Pathology Milestones 2.0, 2020 revision"]
- **Topic or content:** [what the session/rotation covers]

## What to produce

For each objective:

```
By the end of this [session / rotation], the [PGY-level] resident will:
[measurable verb] [the specific behavior] [under what conditions] [to what criterion of success], mapping to [milestone sub-competency code or EPA number].
```

### Verb requirements

Use measurable verbs only: interpret, distinguish, formulate, justify, generate, calculate, apply, compare, prioritize, recommend.

NEVER use: understand, know, learn, appreciate, be aware of, recognize (alone), grasp, become familiar with.

### Condition requirements

Each objective must specify the condition under which the behavior occurs:
- "Given a set of lab values..."
- "Given a clinical case..."
- "Given an IHC panel..."
- "In a multidisciplinary sign-out..."

### Criterion requirements

Each objective must specify the criterion for success:
- "With accuracy verified against the [current guideline]"
- "Citing the appropriate WHO classification"
- "Independently, without attending intervention"

### Milestone mapping

Map each objective to a specific milestone sub-competency code (e.g., PC1.3) or EPA. Cite the version of the milestone document you're working from.

### After the objectives

Identify which milestones are NOT addressed by these objectives. Useful context for the CCC and PD — flags whether this session/rotation is over- or under-allocated against the milestone framework.

## Hard rules

- **Measurable verbs only.** No "understand" or "know."
- **Condition and criterion are required for every objective.** Don't omit them to make objectives shorter.
- **Cite the milestone document version.** Milestones get revised; don't refer to outdated codes without flagging.
- **If you're not sure whether a milestone code is current, ASK** rather than guess.
- **The "milestones not addressed" section is non-optional.** It's the most useful part for leadership.

## What I will NOT accept

- Objectives using "understand," "know," or similar non-measurable verbs
- Missing conditions or criteria
- Invented milestone codes
- Verb mismatch with PGY level (PGY-1 objectives requiring "justify" or "formulate" at expert level)
```

## Expected output

3-7 objectives in the required format, plus a list of milestones not addressed. Length depends on number of objectives; typically 300-600 words.

## Common failure modes

- **Non-measurable verbs slipping in.** Push back.
- **Conditions and criteria omitted.** Push back.
- **Invented or outdated milestone codes.** Verify against your current document.

## Required human verification

- Verify every milestone code against your program's current document. ACGME milestones are revised periodically.
- Run objectives by your program director or CCC chair before using in any formally documented context.
- For CME-accredited sessions, additional formatting may be required by your CME office.

## Best model and why

**Claude Sonnet 4.6** — structured objective generation is Sonnet's strength. Verify milestone codes regardless of model; no model is reliably current on milestone documents that have been revised after its training cutoff.
""")

# --- REFINED P2 #2: Bloom's taxonomy MCQ generation ---
write_prompt(
    "library/pillar-2-teaching/prompts/blooms-mcq.md",
    {"title":"Bloom's taxonomy MCQ generation","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"mcq, assessment, blooms, cognitive-level","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Generates MCQs at specified Bloom's taxonomy levels — Application, Analysis, Evaluation — with rationales calibrated to the cognitive task each question tests. Avoids the default failure mode of disguising Recall as Application by adding a clinical vignette to a recall question.

## When to use it

When building formative or summative assessment items that test reasoning rather than memorization. Especially useful when designing assessments that need to demonstrate cognitive level discrimination (CCC documentation, milestone-aligned exams).

**Not for:** quick review questions (use [MCQ generation with rationales](library.html#/library/pillar-1-self-education/prompts/mcq-generation-with-rationales)), questions for board exam prep where you want a mix that matches real board distribution, or formal assessment items that need psychometric validation.

## The prompt

```
You are generating MCQs across Bloom's taxonomy levels. Discipline test: a question that can be answered by retrieving a memorized fact is Recall, regardless of how clinical-looking the vignette is. Be honest about cognitive level.

## What I'm generating

- **Topic:** [be specific]
- **Audience level:** [PGY level + subspecialty rotation context]
- **Number of questions:** [N]
- **Distribution across Bloom's levels:**
  - **Application:** [X%] — use knowledge in a new situation (typical clinical vignette)
  - **Analysis:** [Y%] — distinguish, compare, organize (requires breaking down a complex case)
  - **Evaluation:** [Z%] — justify a decision based on criteria (requires choosing among multiple acceptable approaches)

Avoid Remember/Understand level questions — they don't test what residents actually need.

## For each question, produce

```
Question N (Bloom's level: [Application / Analysis / Evaluation]):

[Vignette — clinical or laboratory context]

A. [Choice]
B. [Choice]
C. [Choice]
D. [Choice]
E. [Choice]

---

ANSWER: [Letter]

LEVEL JUSTIFICATION: [Name the specific cognitive task this question requires. What does the resident have to DO to answer this — not just remember, but DO?]

RATIONALES:
A. [Why correct OR what cognitive shortcut leads to this wrong answer]
B. [Same]
C. [Same]
D. [Same]
E. [Same]

TEACHING POINT (1 sentence): The cognitive skill this question is assessing.
```

## Hard rules — the discipline tests

- **Discipline test #1: Can a resident answer this by retrieving a memorized fact?** If yes, it's Recall, not Application. Mark it as Recall and offer to escalate.
- **Discipline test #2: For Application, does the resident need to apply the concept in a NEW situation,** not just identify which textbook entity matches the vignette? If they're matching, it's still Recall.
- **Discipline test #3: For Analysis, must the resident BREAK DOWN a complex scenario** into discriminating components? If they're just identifying the right answer, it's Application or below.
- **Discipline test #4: For Evaluation, must the resident JUSTIFY a choice among multiple defensible options?** If there's only one right answer with the rest being clearly wrong, it's not Evaluation.
- **Source any specific value cited** in the question or rationales.
- **Distractors must be plausible** — represent real cognitive errors, not throwaways.

## What I will NOT accept

- "Application" questions that are recall dressed in a vignette
- Distractors that are obviously wrong
- "Evaluation" questions with one right answer and four obviously wrong ones
- Level justifications that are vague ("requires higher-order thinking")
```

## Expected output

N questions with verified Bloom's level, level justification, full rationales, and teaching point. Typically 300-450 words per question.

## Common failure modes

- **Recall mislabeled as Application.** The dominant failure mode. Push back: "A resident who memorized [fact] could answer this without applying anything. This is Recall."
- **Evaluation questions with one obvious answer.** Push back: "All five answers should be defensible to some degree. What's wrong with each that makes the chosen one best?"
- **Generic level justifications.** Push back: "Name the specific cognitive task."

## Required human verification

- Verify the correct answer against an authoritative source.
- Pressure-test the Bloom's level: would a memorizer answer it correctly without reasoning? If yes, the level is over-stated.
- Have a colleague who teaches this topic review the question and the level designation before formal use.

## Best model and why

**Claude Opus 4.7** — Bloom's level calibration is genuinely difficult; Sonnet often mis-labels questions. Opus is more disciplined about identifying when a clinical vignette is just dressing for a recall question.
""")

# --- REFINED P2 #3: Case vignette at PGY level ---
write_prompt(
    "library/pillar-2-teaching/prompts/case-vignette-pgy.md",
    {"title":"Case vignette at PGY level","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"vignette, case-based, level-calibration","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Generates a case vignette calibrated to a specific PGY level, with the right complexity, the right amount of clinical context, and demographics that reflect actual epidemiology rather than the textbook-archetype default. Also generates the intended diagnosis, the 2-3 most likely wrong answers at this level (with WHY each is appealing), and a discussion question.

The harder discipline this prompt enforces: vignettes should vary patient demographics across cases. A series of 20 vignettes all about middle-aged white men teaches residents to anchor on that archetype.

## When to use it

Designing case-based teaching, board-style question writing, or building a case bank for resident education. Especially useful when you want a specific cognitive challenge (e.g., "ambiguous lab data integration") rather than just a topic.

**Not for:** real case presentations (use the tumor board prompt instead), case-based assessment that needs psychometric validation, or first-time learning of an entity (use concept explanation first).

## The prompt

```
You are generating a case vignette for teaching. Calibration to PGY level is the entire point — the wrong calibration teaches nothing or frustrates the resident.

## What I'm requesting

- **Topic / diagnosis being taught:** [specific entity, not category]
- **Target audience:** [PGY level + rotation context]
- **Specific cognitive challenge:** [optional — e.g., "ambiguous initial labs", "atypical demographic", "discordant findings"]
- **Constraints:** [SI units, specific terminology, anything else]

## Level calibration guidance — apply explicitly

- **PGY-1:** classic presentation, one main differential to resolve, all relevant data given, no significant red herrings, no atypical demographics.
- **PGY-2:** typical presentation with a complicating factor (comorbidity that obscures the picture, a 'positive' test result that's actually a red herring, atypical demographic for the diagnosis).
- **PGY-3:** atypical presentation, ambiguous lab/imaging data, must integrate multiple discordant findings, decision under uncertainty.
- **PGY-4 / Fellow:** rare entity OR atypical presentation of common entity, requires judgment calls under significant uncertainty, considers cost/risk of further workup.

## What to produce

### The vignette

- **Length:** 4-7 sentences
- **Demographics:** include detail relevant to the differential. **Do NOT default to middle-aged white male.** Reflect the actual epidemiology of the condition; vary across cases when building a series.
- **Data:** include what the resident needs to reason from, no more
- **Ending:** stop at the point where the resident must commit to an interpretation or next step

### The intended diagnosis

State it explicitly.

### The 2-3 most likely wrong answers at this level

For each wrong answer:
- The wrong diagnosis
- WHY a resident at this level would pick it (the specific cognitive error or anchor)
- What in the vignette should have ruled it out

### Discussion question

One question to ask after the resident commits to their interpretation. Should require them to defend or critique their reasoning, not just restate it.

## Hard rules

- **PGY-1 vignettes do not have red herrings.** They're not "easy"; they're calibrated.
- **PGY-3 and Fellow vignettes must have genuine ambiguity.** Not just a longer vignette.
- **Demographics reflect the disease's actual epidemiology.** If the condition is more common in older Black men, that's the demographic to use, not a generic 50-year-old white man.
- **The wrong-answer analysis is the highest-value part.** Generic "they're wrong because the right answer is X" is unacceptable.
- **No PHI.** Vignettes are fictional or sufficiently genericized.

## What I will NOT accept

- A "PGY-3" vignette where the answer is obvious
- Demographics defaulted to textbook archetype
- Wrong-answer analysis that doesn't name the specific cognitive error
- A discussion question that's just "what would you do next?"
```

## Expected output

The vignette + intended diagnosis + 2-3 wrong-answer analysis + discussion question. Length depends on case; typically 400-600 words total.

## Common failure modes

- **Calibration miss** — "PGY-3" vignette that's PGY-1 difficulty. Push back.
- **Textbook demographics by default.** Push back: "Vary the demographic."
- **Generic wrong-answer analysis.** Push back: "What's the SPECIFIC cognitive error?"

## Required human verification

- Pressure-test the vignette against a resident at the target level before using in a session — is the difficulty actually right?
- Check demographics across a series — over 10-20 vignettes, is the distribution defensible?
- Verify clinical details (drug doses, lab cutoffs, classification version) against current source.

## Best model and why

**Claude Opus 4.7** — calibrating difficulty to PGY level, varying demographics intelligently, and generating substantive wrong-answer analyses all reward depth. Sonnet vignettes tend toward "classic presentation" regardless of stated level.
""")

# --- REFINED P2 #4: CCC narrative comment drafting ---
write_prompt(
    "library/pillar-2-teaching/prompts/ccc-narrative-comment.md",
    {"title":"CCC narrative comment drafting","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"ccc, narrative, milestone-evidence, high-stakes","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Converts your bullet observations into a CCC narrative comment that defensibly maps evidence to milestone level. Strict discipline about not inflating beyond the evidence you provided — if your evidence supports level 3 but you've assigned level 4, the prompt flags the inconsistency before drafting.

CCC narratives are read by external reviewers (ACGME visits, fellowship directors reviewing applicants) cold, without context. The narrative must make sense alone.

## When to use it

Writing CCC narratives at semi-annual reviews. Especially valuable for residents you know well but for whom you don't have well-organized notes — the prompt forces evidence-to-claim mapping that you might gloss over otherwise.

**Not for:** routine end-of-rotation feedback (use [Resident feedback note drafting](library.html#/library/pillar-2-teaching/prompts/resident-feedback-note)), evaluations that go directly to the resident (different audience), or replacing your CCC chair's review.

## The prompt

```
You are drafting a CCC narrative comment that must defensibly map evidence to milestone level. Be conservative about inflation. If my evidence doesn't support my assigned level, flag the inconsistency BEFORE drafting.

## What I'm providing

- **Resident initial + PGY:** [e.g., "Resident JD, PGY-3"]
- **Milestone sub-competency:** [e.g., "PC1.3 Interpretation of Diagnostic Studies"]
- **Milestone level I'm assigning:** [e.g., "Level 3 / Level 4 in transition"]
- **Trajectory:** [progressed / plateaued / regressed since last review]
- **Evidence / observations from this review period:**
  [paste bullets — specific behaviors I observed, with case context where useful]
- **Comparison to peers (optional):** [where this resident sits relative to PGY-3 cohort]

## Inconsistency check FIRST

Before drafting, evaluate whether my evidence actually supports my assigned level. If the evidence describes Level 3 behaviors and I've assigned Level 4, OR if the evidence describes Level 4 behaviors and I've assigned Level 3, STOP and tell me. Don't draft until we resolve the inconsistency.

## Narrative structure (4 sentences total)

1. **Level + trajectory sentence:** "Resident JD demonstrates Level [N] performance for [milestone], having [progressed from / maintained / partially regressed from] the prior review."

2. **2-3 sentences of behavioral evidence:** Specific behaviors I observed. Each behavior tied to a case or context (anonymized). Avoid generic language like "demonstrates competence" — use the actual behaviors.

3. **Next milestone behavior sentence:** What is the resident approaching or working toward at the next level? Specific.

4. **Forward-looking expectation sentence:** A specific expectation for the next 6 months.

## Tone and audience

The narrative will be read by an external reviewer (ACGME visit, fellowship director reviewing this resident's application later) cold, without context. It must:
- Make sense as a standalone paragraph
- Use the resident initial + PGY format consistently
- Be factual and evidence-based, not effusive
- Be defensible if challenged

## Hard rules

- **Do NOT inflate beyond evidence.** If evidence supports Level 3, don't draft Level 4.
- **Every behavioral claim must trace to a bullet I provided.** If you can't trace it, you're inventing.
- **Use specific behaviors, not generic praise.** "Demonstrated independent interpretation of routine cases with appropriate escalation of complex cases" is good; "demonstrated competence" is not.
- **Match the trajectory language to the evidence.** "Progressed" requires evidence of progression.

## What I will NOT accept

- Narrative that goes beyond my evidence
- Generic competence statements
- Inflated language ("exceptional," "outstanding") without behavioral evidence
- Trajectory claims without evidence
```

## Expected output

A 4-sentence narrative comment defensibly mapping evidence to milestone level, with forward-looking expectation. Length ~80-120 words.

## Common failure modes

- **Inflation.** The model wants to be generous; resist it.
- **Generic praise.** Push back: "What specifically did the resident do?"
- **Trajectory claims without evidence.** Push back.

## Required human verification

- Re-read against your bullets — every claim should trace to one.
- Have a colleague on the CCC read for consistency with their style.
- Verify the milestone level descriptors against your program's current milestone document — these get revised.

## Best model and why

**Claude Opus 4.7** — tight evidence-to-claim mapping and defensible level assignment reward Opus's depth. Sonnet narratives tend toward generic competence language; Opus is more disciplined about specificity.
""")

# --- REFINED P2 #5: OSCE station drafting ---
write_prompt(
    "library/pillar-2-teaching/prompts/osce-station.md",
    {"title":"OSCE station drafting","pillar":"teaching","event_type":"n/a","audience":"faculty",
     "difficulty":"advanced","time_to_use":">10min","visual":"text-only",
     "tags":"osce, assessment, simulation","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Drafts a complete OSCE station: examinee instructions, simulated-other-party script that handles real conversational variation, expected examinee actions ranked by importance, a behaviorally-anchored scoring rubric, and a "red flag" list of actions that should trigger remediation review.

OSCEs are easy to design badly. The two failure modes: (1) the script is rigid and breaks when the examinee asks an unexpected question, (2) the rubric is too vague for two raters to score the same examinee the same way.

## When to use it

Designing summative or formative OSCE assessment, especially for stations that test communication or reasoning rather than knowledge. Also useful as a teaching tool — running a formative OSCE with a coaching debrief.

**Not for:** assessment without pilot testing (OSCEs need calibration), high-stakes credentialing stations without psychometric review, or replacing your program's standard OSCE design process.

## The prompt

```
You are drafting a complete OSCE station. The script must handle conversational variation; the rubric must enable two raters to score the same examinee the same way.

## What I'm building

- **Target audience:** [e.g., "CP residents at end-of-year assessment", "first-year fellows"]
- **Scenario:** [e.g., "critical value notification to a covering physician at 2am", "frozen section consultation with a surgeon in the OR", "handover to inpatient team after a complex case"]
- **Station length:** [in minutes — typically 7-10]
- **Number of raters:** [single rater / two raters scoring independently]
- **Pass / fail or graded:** [which]

## What to produce — 5 parts

### Part 1: Examinee instructions

What the examinee reads/hears before walking in. Should include:
- The scenario context (1-2 sentences)
- What they're expected to do
- Time limit
- Any props or materials available
- A clear stopping condition (when do they know they're done?)

### Part 2: Simulated other party script

The simulated patient, clinician, or other party. Should include:
- Opening line (what they say first)
- Responses to the 4-5 most likely examinee openers — each with the words they'd actually say
- Information they hold back unless directly asked
- How they respond to a non-empathetic examinee vs an empathetic one
- A "if asked about X" reference for tangential topics
- A wind-down trigger that helps end the station gracefully

### Part 3: Expected examinee actions

Organized as:
- **MUST DO** (failure to do these = critical fail)
- **SHOULD DO** (full credit)
- **OPTIONAL** (above-and-beyond)

For each action, name the specific behavior. Not "communicate effectively" — "explicitly state the patient identifier and the critical value within the first 30 seconds of the call."

### Part 4: Scoring rubric

5-7 dimensions, each with:
- Dimension name
- **Behavioral anchors at 4 levels:** Novice / Developing / Competent / Proficient
- The specific observable behavior at each level

Dimensions should cover: communication, content accuracy, prioritization, professionalism. Each dimension should be independently rateable.

### Part 5: Red flag list

Actions that, if performed, should trigger remediation review:
- Patient safety issues
- Professionalism violations
- Egregious communication failures

Be specific — these are the actions that get reported up, so they need to be unambiguous.

## Hard rules

- **The script must handle conversational variation.** A rigid script that only works if the examinee asks specific questions is broken.
- **Rubric anchors must be behaviorally specific.** "Demonstrates good communication" is not an anchor; "explicitly summarizes the situation, asks for read-back, and confirms next steps before ending the call" is.
- **Inter-rater reliability is the test.** If two raters can read the rubric and rate the same examinee differently, the anchors aren't specific enough.
- **The red flag list is for unambiguous actions only.** "Behaved unprofessionally" is not a red flag; "made a comment about the patient's appearance" might be.

## What I will NOT accept

- A rigid script that breaks under conversational variation
- Vague rubric anchors ("shows competence")
- Red flag items that require subjective judgment
- Expected actions that aren't observable
```

## Expected output

5 parts: examinee instructions, simulated party script with conversational variation, ranked expected actions, behaviorally-anchored 5-7 dimension rubric, red flag list. Length 800-1500 words for a typical 7-10 minute station.

## Common failure modes

- **Script too rigid.** Push back: "Add responses for [common variations]."
- **Vague rubric anchors.** Push back: "Name the specific observable behavior at each level."
- **Red flag list with subjective items.** Push back: "These need to be unambiguous."

## Required human verification

- **Pilot the station** with a faculty member playing the examinee role before formal use.
- **Have a second rater score a video of the pilot independently.** If inter-rater agreement is low, the rubric needs more anchoring.
- **Verify clinical content** (drug doses, lab cutoffs, procedural steps) against current practice.
- **For high-stakes use,** consider psychometric review of the station before deployment.

## Best model and why

**Claude Opus 4.7** — multi-part OSCE artifacts (script, rubric, red-flag list) need internal consistency that Opus holds together better than Sonnet. The conversational-variation handling in the script also benefits from Opus's depth.
""")

# ===========================================================================
# Done
# ===========================================================================

print("Wrote/updated 21 prompts:")
print("  P1 remaining (11 deeply refined):")
print("    compare-contrast, guideline-plain-language, lis-informatics-review,")
print("    anki-flashcards, board-prep-schedule, question-bank-gap-analysis,")
print("    diagnostic-algorithm-walkthrough, forward-case-drill, negative-drill,")
print("    journal-club-preread, multimodal-spep-ife")
print("  P2 new (5):")
print("    microscopy-teaching-session, sign-out-teaching-turn,")
print("    tumor-board-prep-coaching, subspecialty-rotation-goals-letter,")
print("    difficult-feedback-conversation-prep")
print("  P2 refined (5):")
print("    acgme-epa-objectives, blooms-mcq, case-vignette-pgy,")
print("    ccc-narrative-comment, osce-station")
