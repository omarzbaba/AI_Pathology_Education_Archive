#!/usr/bin/env python3
"""
Populates the 61 prompt stub files with substantive bodies.
Preserves the YAML frontmatter; replaces the markdown body below it.

After running this once, the prompt bodies are no longer "TODO" stubs.
Dr. Baba can edit any individual file to refine the prompt for his
voice, institutional vocabulary, or subspecialty context.

Run:
  python3 scripts/populate-prompts.py
"""

import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Body template — every prompt has the same seven-section structure
# ---------------------------------------------------------------------------

def body(intent, when, prompt, output, failures, verification):
    return (
        f"## What this prompt does\n\n{intent}\n\n"
        f"## When to use it\n\n{when}\n\n"
        f"## The prompt\n\n```\n{prompt.strip()}\n```\n\n"
        f"## Expected output\n\n{output}\n\n"
        f"## Common failure modes\n\n{failures}\n\n"
        f"## Required human verification\n\n{verification}\n"
    )

# ---------------------------------------------------------------------------
# Pillar 1 — Self-Education (18 prompts)
# ---------------------------------------------------------------------------

P1 = "library/pillar-1-self-education/prompts"

BODIES = {}

BODIES[f"{P1}/concept-explanation-at-level.md"] = body(
    intent="Get an explanation of a pathology concept calibrated to your current level — neither too elementary nor too advanced. The output is an *adapted* explanation, not a generic textbook paragraph.",
    when="When you encounter a concept you half-understand and want a targeted explanation that meets you where you are. Best used as the *first* step in a longer self-quizzing session; the calibration here sets the model's mental model of you for everything that follows.",
    prompt="""I'm a [PGY level] pathology resident on my [N]th rotation in [subspecialty]. I have a [working / weak / strong] understanding of [adjacent concept]. I'm trying to understand [target concept] well enough to [specific goal — e.g., interpret a case in tomorrow's sign-out, write an MCQ for our didactics, answer a co-resident's question].

Explain [target concept] in three layers:

1. The one-sentence version a first-year medical student would understand.
2. The mechanistic explanation a pathology resident at my level should know cold.
3. The nuanced detail that distinguishes someone who has thought hard about this from someone who has just memorized it.

After your explanation, ask me ONE follow-up question to check my understanding before moving on. Do not move on until I answer.""",
    output="Three-layer explanation in plain prose (not bullets) totaling 200-400 words. The third layer should surface a nuance you didn't previously know. The follow-up question at the end should target the most likely misunderstanding for your level.",
    failures="""- The model defaults to the textbook framing and gives you back what you could read in Robbins. Mitigate by being specific about *which* aspect confuses you.
- The model skips the level calibration and explains at one undifferentiated level. Mitigate by re-stating the level after the first response.
- The "nuanced detail" turns out to be a half-remembered fact that's actually wrong. This is the failure mode that matters most for self-education — see verification below.""",
    verification="""- Cross-check the nuanced detail (layer 3) against an authoritative source: the relevant chapter in Robbins, a recent guideline, or a curated review article. The model is most likely to be confidently wrong at the level where you have least ability to catch it.
- If a specific numerical threshold or cutoff is given, verify against the current reference range or guideline."""
)

BODIES[f"{P1}/compare-contrast.md"] = body(
    intent="Generate a side-by-side comparison of two entities that are easy to confuse, focused on the *discriminating* features rather than a comprehensive list of differences.",
    when="When you can name two entities but routinely confuse them, or when you've gotten a board-style question wrong because you picked the wrong one. The output is best when the entities are at the same diagnostic level (e.g., two specific entities, not 'lymphoma vs leukemia').",
    prompt="""Compare and contrast [entity A] and [entity B] for a [PGY level] pathology resident.

Structure your response as:

1. **One-sentence orientation:** how do these two entities relate to each other in the differential? (Same family? Lookalikes? Sequential along a spectrum?)
2. **Discriminating features:** a table with rows for the features that actually distinguish them. Each row should be a feature where the two entities differ in a clinically meaningful way. Skip features they share.
3. **The single best discriminator:** if you could only ask one question or order one test, which one resolves the differential?
4. **The classic trap:** the feature most likely to make a resident pick the wrong answer, and how to avoid it.

Use the discriminating features your textbook actually uses, not generic ones.""",
    output="A short orientation sentence, a 4-8 row table of discriminating features, a named best discriminator with rationale, and one named trap. The table rows should be the features you'd write on a flashcard, not exhaustive.",
    failures="""- The table includes features the two entities share (wasted space).
- The "best discriminator" is something not actually orderable in real practice.
- The "classic trap" is generic ("don't confuse them!") rather than a specific feature.""",
    verification="""- Confirm the discriminating features against your subspecialty's reference text. Models can confuse features between similar entities, especially for rarer diagnoses.
- If a specific stain pattern or molecular finding is named, verify it's the current convention (e.g., WHO classification version)."""
)

BODIES[f"{P1}/self-quiz-one-at-a-time.md"] = body(
    intent="Drill yourself with one question at a time, with the model adapting follow-up questions based on what you got wrong. The interaction structure matters as much as the content.",
    when="When you have 10-30 minutes and want to actively rehearse rather than passively read. Especially valuable the week before an exam, or during a rotation where you want to test your retention of last week's material.",
    prompt="""I'm a [PGY level] resident studying [topic]. I want you to quiz me on this topic.

Ground rules — these are critical:

1. Ask me ONE question at a time. Wait for my answer.
2. After each answer, tell me if I'm right or wrong and explain briefly. If I was partially right, name what I missed.
3. Use my answer to calibrate the next question. If I got it cold, escalate the difficulty. If I struggled, ask a related but slightly easier question that addresses my gap.
4. After 5 questions, give me a one-paragraph synthesis of where I'm strong and where I have a gap.
5. Do NOT lecture between questions. Keep the rhythm tight.

Start with a calibration question that helps you figure out my level on this topic.""",
    output="A back-and-forth conversation. Each model turn = one question + brief feedback on the prior answer (if any). At question 5, a synthesis paragraph identifying your strongest area and biggest gap.",
    failures="""- The model violates the one-question rule and dumps three questions at once. Push back hard: 'One at a time. Wait for my answer before the next question.'
- The model lectures between questions, undermining the drill rhythm. Push back: 'Less explanation, more questions.'
- The synthesis at the end is generic ('keep studying!') rather than specific. Ask: 'Be more specific about my gap — what should I read tonight?'""",
    verification="""- The model's feedback on whether you got it right or wrong is itself fallible. If a question's correct answer surprises you, verify against an authoritative source before incorporating it into your mental model.
- Watch for the model marking you 'partially correct' when you're actually wrong, which builds false confidence."""
)

BODIES[f"{P1}/mcq-generation-with-rationales.md"] = body(
    intent="Generate board-style multiple-choice questions with detailed rationales for all answer choices — both correct and incorrect. The rationales for the distractors are where the learning happens.",
    when="When you've just finished a study block and want active retrieval practice, or when you're building a personal question bank for board prep. Not a substitute for a real qbank, but useful for filling specific gaps.",
    prompt="""Generate [N] USMLE/board-style multiple-choice questions on [topic] calibrated to [PGY level / board level — e.g., RISE, AP/CP boards, ABPath in-service].

For each question:

- The stem must include a clinical or laboratory vignette, not just a knowledge prompt.
- Five answer choices (A-E), with exactly one best answer.
- All distractors must be plausible to someone with partial knowledge — no obvious throwaways.
- After all questions, provide an answer key with a 2-3 sentence rationale for **each** answer choice, including why the wrong ones are wrong. The wrong-answer rationales are the most important part.

Topic depth: assume the resident has read the relevant chapter once but has not drilled the material.""",
    output="N questions in the requested format with full vignettes, five plausible choices each, and complete rationales (right and wrong) for each choice. Rationales should explain not just the fact but the reasoning that connects vignette to answer.",
    failures="""- Distractors are obvious throwaways (one is clearly wrong without thought). Push back: 'Make the distractors more plausible.'
- Wrong-answer rationales are perfunctory ('this is incorrect because the right answer is A'). Push back for substantive explanations.
- Vignettes are generic 'a 50-year-old male presents with' templates that don't add educational value.""",
    verification="""- **Critical:** verify the correct answer against an authoritative source before using the question for study or sharing. AI-generated MCQs routinely have plausible-looking-but-wrong correct answers, especially for nuanced topics.
- Check that the question is not a near-duplicate of a real published board question (rare but possible)."""
)

BODIES[f"{P1}/anki-flashcards.md"] = body(
    intent="Convert a topic, paper, or set of notes into Anki-ready flashcards in a format you can paste directly into Anki's import dialog. The structure matters because Anki rewards atomic, single-concept cards.",
    when="When you've just done dense reading and want to convert it into spaced-repetition material before you forget. Best within an hour of the reading session.",
    prompt="""Convert the following [topic / source: paper title / notes] into Anki flashcards.

Output format: tab-separated values, one card per line. Each line is:

`question[TAB]answer`

Rules:

1. **Atomic cards.** Each card tests ONE fact or concept. If a card has 'and' or 'or' in the answer, split it into two cards.
2. **Specific questions.** 'What is X?' is weak. 'In a patient with X, what laboratory finding distinguishes A from B?' is strong.
3. **No clozes** unless I ask. Plain Q/A only.
4. **Aim for [N] cards.** Don't pad. If the material doesn't justify N cards, give me fewer good ones.
5. Use the actual numbers, names, and details from the source. If you don't know a specific value, leave it blank rather than guessing.

After the cards, add a one-sentence note about anything in the source you decided NOT to make a card for and why.""",
    output="N tab-separated lines, one card per line, plus a brief note on what was deliberately excluded. The cards should be import-ready: paste into Anki → Import → Text File.",
    failures="""- Cards that test 'what is X' without context — useless for retention. Ask for more specific question framings.
- Cards that try to test multiple facts at once. Split them.
- Made-up specific values when the source didn't have them. Verify any specific number, dose, or threshold before incorporating into your deck.""",
    verification="""- Scan the answers for any numerical value, drug dose, gene name, or specific reference range. Verify each against the source or an authoritative reference. The model will sometimes invent plausible-looking specifics."""
)

BODIES[f"{P1}/diagnostic-algorithm-walkthrough.md"] = body(
    intent="Walk through a published diagnostic algorithm step by step, with the model explaining each decision point and the consequences of choosing each branch.",
    when="When you're encountering a clinical algorithm for the first time, or when you've used one mechanically without really understanding why each branch exists. Good for the night before a sign-out where you know an algorithm will come up.",
    prompt="""Walk me through the [name of algorithm — e.g., 'BSH guideline for warfarin reversal', 'ISTH overt DIC scoring', '2022 ELN AML response criteria'] step by step.

For each decision point in the algorithm:

1. State the question or test being asked at this node.
2. Explain *why* this question is being asked here — what does the answer rule in or rule out?
3. Walk through what happens if the answer is yes/positive and what happens if it's no/negative.
4. Name one common pitfall at this decision point — a way residents typically mis-apply this step.

After walking through the full algorithm, end with: the single decision point where errors are most clinically consequential, and how to avoid those errors.

Be specific to the published version of the algorithm; do not generalize to 'similar' protocols.""",
    output="A linear walk-through, one node at a time, with rationale and pitfalls at each. A final synthesis identifying the most consequential decision point. Length: ~400-700 words for a typical 5-7 step algorithm.",
    failures="""- The model conflates two similar algorithms (e.g., ISTH overt vs non-overt DIC criteria) without flagging which it's using.
- The 'common pitfall' is generic ('don't forget to check the value') rather than specific.
- The model substitutes its own simplified logic for the actual published algorithm.""",
    verification="""- **Critical:** verify the algorithm against the actual published source (society guideline, original paper, institutional protocol). The model frequently mis-remembers cutoffs, the order of decision nodes, or which version of an algorithm it's describing.
- If the algorithm has multiple versions (e.g., updated in 2020 and 2024), confirm which version the model is walking through."""
)

BODIES[f"{P1}/reverse-case-drill.md"] = body(
    intent="Give the model a set of findings and ask it to walk you through the differential and final diagnosis — then critique your own approach against the model's. The drill is in your interpretation, not in receiving the answer.",
    when="When you've just signed out a case and want to test whether you'd reach the same conclusion working in reverse from the findings alone. Especially useful for cases where the diagnosis was non-obvious or the differential was wide.",
    prompt="""I'm going to give you a set of findings from a case I just worked. Work the case in reverse: starting from the findings alone, walk through your differential, narrow it systematically, and reach a final diagnosis.

Ground rules:

1. **Do not skip steps.** Even if the answer seems obvious, show your reasoning.
2. **Be explicit about pretest probability.** Name the demographic and clinical context that's shifting your differential.
3. **For each step, name the discriminating finding** that moves you from broad → narrower → narrowest.
4. **End with the single piece of evidence you most wanted that you didn't have**, and what it would have ruled in or out.

After your walkthrough, I'll tell you what I actually concluded and we can compare reasoning paths.

Findings:
[paste the findings — labs, imaging summary, morphology description, clinical context. De-identified, no PHI.]""",
    output="A step-by-step differential walkthrough ending in a final diagnosis and a named 'missing piece of evidence'. The walkthrough should be longer than the findings — that ratio is the point.",
    failures="""- The model jumps to the answer without showing reasoning. Push back: 'walk through the differential explicitly.'
- The model uses information that wasn't in your findings, then claims it was. Watch for this — push back.
- The differential is too narrow because the model anchored on a likely answer. Push back: 'broaden the differential and explain what would shift you to each.'""",
    verification="""- **Never paste identifiable patient information.** Use de-identified findings, published teaching cases, or sufficiently genericized vignettes.
- The model's final diagnosis is fallible. Treat the exercise as a structured comparison of *reasoning paths*, not as a second opinion on the case."""
)

BODIES[f"{P1}/forward-case-drill.md"] = body(
    intent="Name a diagnosis and have the model generate the constellation of findings you would expect to see, then quiz yourself on which findings are pathognomonic vs supportive vs incidental.",
    when="When you're studying a diagnosis you've read about but haven't seen many times. Builds the pattern recognition that comes from case exposure.",
    prompt="""I'm studying [diagnosis] at a [PGY level] level. Generate the constellation of findings I should expect to see, organized as:

1. **Clinical presentation:** demographics, symptoms, onset, common comorbidities.
2. **Laboratory findings:** what's elevated, what's low, what's normal but tested anyway. Include reference ranges.
3. **Imaging findings:** what's seen on the relevant modality.
4. **Morphologic / histopathologic findings:** organized by what's seen at low power → high power → IHC/molecular.
5. **Findings that rule the diagnosis OUT:** the negative findings that should make you reconsider.

For each finding, label it [Pathognomonic / Highly Supportive / Supportive / Common but non-specific].

Then quiz me: ask me which findings I would prioritize on a sign-out and why.""",
    output="A structured constellation with all five sections, every finding labeled by diagnostic weight, and a quiz question at the end about prioritization.",
    failures="""- The model labels too many findings as 'pathognomonic' — a finding is only pathognomonic if it's unique to the diagnosis, which is rare.
- The model includes findings that are actually for a similar but different diagnosis.
- Reference ranges given without source.""",
    verification="""- Verify which findings are truly pathognomonic vs merely supportive. The model overuses 'pathognomonic'.
- Cross-reference the morphologic findings against your subspecialty's atlas or reference text — this is where confident-wrong answers are most likely."""
)

BODIES[f"{P1}/negative-drill.md"] = body(
    intent="Take a settled diagnosis and ask the model to enumerate the findings or test results that would force you to reconsider, ranked by likelihood. Trains the habit of disconfirmation.",
    when="When you have a working diagnosis you're confident in and want to stress-test that confidence. Especially useful for diagnoses you've seen rarely or for cases where the consequences of being wrong are high.",
    prompt="""I have a working diagnosis of [diagnosis] in a patient with [brief clinical context — no PHI]. I want to stress-test this diagnosis.

Generate a ranked list of findings or test results that would force me to reconsider, organized as:

1. **Findings that would force a complete reconsideration** (rule out this diagnosis).
2. **Findings that would expand the differential** (suggest a different category of disease).
3. **Findings that are inconsistent but don't necessarily change the diagnosis** (worth noting, may indicate complication or atypical presentation).

For each finding, give a one-sentence rationale: why does this finding contradict the diagnosis?

Then identify the **single most likely** alternative diagnosis if I'm wrong, and the one test I should order to discriminate between them.""",
    output="A three-tier list of disconfirming findings with rationales, plus a named alternative diagnosis and a discriminating test.",
    failures="""- The list focuses on the rare and exotic alternatives rather than the common ones. Push back: 'what's the most COMMON way I could be wrong?'
- The 'most likely alternative' is something already excluded by basic workup.
- The discriminating test is something with low specificity that won't actually settle the question.""",
    verification="""- This prompt is most useful as a thinking exercise; the model's specific suggestions are starting points, not definitive guidance.
- If a specific test is recommended (e.g., 'order a flow cytometry'), verify the test is the right one for the discrimination you actually need."""
)

BODIES[f"{P1}/board-prep-schedule.md"] = body(
    intent="Generate a personalized board prep schedule based on weeks remaining, daily study hours, and your strongest/weakest subspecialties.",
    when="At the start of board prep, or when you realize the existing plan isn't working and you need to re-allocate. Best when you can be honest with the model about your weak areas.",
    prompt="""I'm preparing for [boards — name and date]. I have [N] weeks until the exam and can realistically commit [X] hours per day on weekdays and [Y] hours per day on weekends.

My self-assessment by subspecialty:
- **Strong:** [list subspecialties where you can pass at this moment]
- **Moderate:** [list where you'd struggle on harder questions]
- **Weak:** [list where you'd fail a focused subspecialty section]

My resources: [qbank, textbook, review course, etc.]

Generate a week-by-week schedule with:

1. Topic allocation per week (more time on weak areas, maintenance on strong areas).
2. Daily breakdown: reading hours, qbank hours, review hours.
3. A rest day every week — not optional.
4. A 'rescue' week 2 weeks before the exam for re-attacking the topics you're still weak in.
5. The week before the exam: zero new material, focused review only.
6. The last 48 hours: explicit instructions (sleep, light review, no caffeine experimentation).

Be specific about resource use, not generic. If you don't have enough info about my resources, ask.""",
    output="A multi-week schedule with daily breakdown, rest days, a rescue week, and explicit pre-exam instructions. The plan should change weekly, not be a flat repeat.",
    failures="""- The schedule is unrealistic for your actual life. Push back with the constraints you didn't share.
- All days look the same — no rhythm. Push back: 'vary the pattern week to week.'
- The model schedules every minute and creates anxiety rather than structure.""",
    verification="""- Run the schedule by a colleague who's recently taken the exam. They will see flaws an AI cannot (e.g., 'no one needs to spend a week on cytogenetics for this exam').
- Adjust based on actual progress in week 2 — the initial plan is a hypothesis, not a contract."""
)

BODIES[f"{P1}/question-bank-gap-analysis.md"] = body(
    intent="Paste a list of question topics you've missed and have the model identify the underlying concept gaps and suggest a targeted review plan.",
    when="After completing a block of qbank questions where you've underperformed. The diagnostic value comes from being honest about which questions you missed and why.",
    prompt="""I've completed [N] qbank questions on [topic / subspecialty / mixed]. Here are the questions I missed, with a brief note on each about why I missed it:

[paste a list, one question per line: 'topic — why I missed it']

Analyze these misses and identify:

1. **The underlying concept gaps** — group the misses into 2-5 concept clusters. A 'gap' is a missing piece of understanding, not 'I didn't know this fact'.
2. **The priority order to address them**, with rationale (which gap, if filled, would resolve the most other questions?).
3. **A specific review plan** for the top gap: which chapter or paper to read, which targeted qbank topic to drill next, an estimate of hours needed.
4. **A 'don't worry about it' list** — anything in my misses that's low-yield for the exam and not worth fixing.""",
    output="2-5 concept clusters with rationale, a priority order, a specific review plan for the top cluster, and a deliberate low-yield list.",
    failures="""- The model treats every miss as equally important. Push back: 'rank the clusters by impact.'
- The 'review plan' is generic ('read more'). Push back: 'name the specific resource and a specific number of hours.'
- The low-yield list is empty. Real qbank performance always includes some questions not worth re-studying — push for an honest list.""",
    verification="""- Cross-check the concept clustering — are these really the right groupings, or is the model finding patterns that don't exist?
- Validate the 'don't worry about it' list against your program's expectations for the exam."""
)

BODIES[f"{P1}/paper-summarization.md"] = body(
    intent="Generate a structured summary of a paper covering question, design, findings, limitations, and what would change practice. The structure matters because it forces the model to address all five — not just the conclusion.",
    when="When you have a paper to read and only 10 minutes. Use the summary as a triage tool: decide whether to read the full paper, scan key sections, or move on.",
    prompt="""Summarize this paper for a [PGY level] pathology resident. I have [N] minutes.

Use this structure:

1. **The question** (1 sentence): what gap in the literature does this paper address?
2. **The design** (2-3 sentences): study type, population, comparison, key methods. Be specific enough that I could critique the design without reading the paper.
3. **The headline finding** (1-2 sentences): the main result and its effect size.
4. **The most important limitation** (1-2 sentences): the limitation that most constrains the generalizability of the findings.
5. **Would this change practice?** (1-2 sentences): if yes, in what specific setting; if no, why not.
6. **Three questions** I should be prepared to answer if my attending asks about this paper.

If you don't know the specific paper, tell me — do not summarize from the title alone.

Paper: [paste DOI, citation, or the full text if you have it]""",
    output="The six-section summary in the order above. Total length ~250-400 words. The three attending questions should be specific enough that you can prep answers in 10 minutes.",
    failures="""- The model summarizes from the title alone when it doesn't have the paper. Push back: 'do you actually have access to the paper text?'
- The 'most important limitation' is generic ('small sample size' when n=2,000). Push back for specific.
- The 'would this change practice?' is non-committal. Push for a specific answer.""",
    verification="""- **Critical:** verify the headline finding and effect size against the actual paper. The model frequently misremembers numbers from papers it has 'seen'.
- If the model invents a citation, that's a hallucination — discard the entire summary.
- Confirm the three attending questions are actually answerable from the paper."""
)

BODIES[f"{P1}/paper-methods-critique.md"] = body(
    intent="Critique a paper's methods section against standard reporting guidelines for the study type (CONSORT for trials, STROBE for observational, PRISMA for reviews, etc.), surfacing missing elements and potential biases.",
    when="When you're presenting a paper at journal club, writing a critical review, or reviewing for a journal. Generates a checklist-style critique that's structured rather than impressionistic.",
    prompt="""Critique the methods section of this paper for a journal club presentation. The paper is a [study type — e.g., retrospective cohort, RCT, diagnostic accuracy study, systematic review].

Use the appropriate reporting guideline as your framework:
- RCT → CONSORT
- Observational study → STROBE
- Diagnostic accuracy → STARD
- Systematic review/meta-analysis → PRISMA
- Prediction model → TRIPOD
- Other → [name the guideline you're using]

Provide:

1. A checklist of the key reporting items expected for this study type.
2. For each item, mark whether the paper addresses it adequately, partially, or not at all. Quote specifically from the methods if needed.
3. The 3 most consequential gaps — the ones a peer reviewer would flag.
4. The 1 design choice that most constrains the paper's interpretability, with a specific suggested alternative.

If I haven't given you the full methods section, ask for it.

Paper methods: [paste methods section or full paper]""",
    output="A structured checklist with adequacy ratings, three named consequential gaps, and one design critique with an alternative. Length: ~400-700 words.",
    failures="""- The critique is generic and could apply to any paper.
- The model invents items not in the actual paper.
- The 'suggested alternative' design isn't actually feasible given the research question.""",
    verification="""- Cross-check the critique against the actual paper. The model will sometimes critique items the paper addresses (just not in the section the model expected).
- If you're presenting this critique at journal club, run it by a faculty member with methods expertise — there's no substitute for human review of methodological critique."""
)

BODIES[f"{P1}/guideline-plain-language.md"] = body(
    intent="Translate a published guideline into plain language at a target reading level, preserving the recommendations and grading.",
    when="When you need to brief a non-pathologist colleague (or yourself, after a long day) on a guideline you've read but not yet internalized. Especially useful before tumor board where you'll need to explain a recommendation.",
    prompt="""Translate the following guideline recommendations into plain language for a [target audience — e.g., 'first-year medical student', 'practicing internist', 'patient at 10th-grade reading level'].

For each recommendation:

1. State the recommendation in one sentence in plain language.
2. Preserve the strength of recommendation (Strong, Conditional, etc.) and the quality of evidence (High, Moderate, Low, Very Low) — these matter and shouldn't be smoothed over.
3. Translate technical terms inline (e.g., 'monoclonal gammopathy of undetermined significance (MGUS) — a small abnormal antibody in the blood that doesn't yet require treatment').
4. Add a one-sentence 'why this matters' line.

Do NOT change the substantive content of the recommendation. If a guideline says 'consider X', do not translate it to 'do X' — preserve the conditional language.

Guideline recommendations: [paste the recommendations]""",
    output="A list of plain-language recommendations, each with grade and evidence quality preserved, with inline term translations and a 'why this matters' line.",
    failures="""- The model strengthens or weakens recommendations during translation. Push back: 'preserve the strength of recommendation exactly.'
- Inline term translations are inaccurate (e.g., translating MGUS as 'cancer').
- 'Why this matters' adds editorial content the guideline didn't actually say.""",
    verification="""- Cross-check the translated recommendations against the original guideline, particularly the strength of recommendation and any conditional language.
- Confirm inline term translations are accurate at the target reading level."""
)

BODIES[f"{P1}/journal-club-preread.md"] = body(
    intent="Generate a one-page pre-read for a journal club paper covering background, key results, and 5 discussion questions. Designed to be sent to attendees the day before.",
    when="When you're hosting journal club and want attendees to arrive prepared rather than reading the paper for the first time during the discussion.",
    prompt="""Create a one-page pre-read for a journal club discussion of this paper. Target audience: [PGY level] pathology residents and faculty.

Structure:

1. **The clinical or scientific context** (3-4 sentences): why this question was worth asking, the state of the field before this paper.
2. **The study in one paragraph** (5-7 sentences): population, methods, key results with numbers. No interpretation yet.
3. **What this paper is good at**: 1-2 specific strengths of the design or analysis.
4. **What this paper is not good at**: 1-2 specific limitations that constrain interpretation.
5. **Five discussion questions**, ordered from concrete (methods, numbers) → abstract (implications, what would change practice). The fifth question should be one where reasonable people disagree.

Keep it to one page. Use specific numbers from the paper, not vague characterizations.

Paper: [paste DOI, citation, or full text]""",
    output="A one-page document (~400-500 words) with the five sections above. The five discussion questions should escalate in abstractness and end with a contested one.",
    failures="""- The model fabricates specific numbers or quotes. If the model doesn't have the paper, it will sometimes guess.
- Discussion questions are leading ('don't you think...?') rather than open.
- The strengths and limitations are generic.""",
    verification="""- Verify all specific numbers (sample sizes, p-values, effect sizes) against the paper.
- Check that the discussion questions are actually answerable from the paper or from background knowledge the attendees should have.
- If the model couldn't access the paper, the pre-read is partly fabricated — discard and try with the paper text pasted in."""
)

BODIES[f"{P1}/lis-informatics-review.md"] = body(
    intent="Get an explanation of LIS, middleware, or informatics concepts at a level useful for clinical pathologists who are not full-time informaticists. Bridges the vocabulary gap that often blocks meaningful conversation with IT.",
    when="When you're attending an informatics committee meeting, evaluating a vendor proposal, or trying to understand why a workflow change is taking longer than expected.",
    prompt="""Explain [informatics concept — e.g., 'HL7 v2.5.1 segment structure', 'middleware autoverification logic', 'LIS-to-EHR interface mapping', 'LOINC code harmonization'] for a clinical pathologist who runs a lab but is not a full-time informaticist.

Structure:

1. **The problem it solves** (2-3 sentences): why this concept exists in the first place.
2. **The mental model** (2-3 sentences): an analogy or simplified diagram (described in words) that captures the essence.
3. **The vocabulary I need to participate in a meeting**: 5-7 terms with one-sentence definitions. These are the words I'll hear thrown around.
4. **The most common failure mode** for this concept in real labs — the thing that breaks and causes downtime or wrong results.
5. **One question I can ask in a vendor or IT meeting that distinguishes a good answer from a hand-wave.**

Avoid jargon I haven't already heard — if you need to use a term, define it inline.""",
    output="The five-section breakdown, total ~300-500 words. The 'one question to ask' should be specific enough that you could actually use it in a meeting.",
    failures="""- The 'mental model' analogy is too cute and loses precision (e.g., 'it's like a post office for lab results').
- The vocabulary section uses terms that are themselves unfamiliar — recursive opacity.
- The 'most common failure mode' is generic ('configuration errors').""",
    verification="""- Verify the technical specifics (e.g., HL7 segment names, LOINC structure) against authoritative documentation. The model sometimes mis-names protocol elements.
- The 'question to ask' is a starting point — have an informatics colleague pressure-test it before relying on it in a high-stakes meeting."""
)

BODIES[f"{P1}/multimodal-photomicrograph.md"] = body(
    intent="Upload a photomicrograph and have the model describe what it sees, then critique your own description against the model's. The drill is your description, not the model's diagnosis.",
    when="When you're building morphologic observation skills and want a structured practice partner. Use published teaching cases or public-domain images — never real patient material.",
    prompt="""I'm uploading a photomicrograph of a [specimen type — e.g., 'H&E-stained kidney biopsy at 40x', 'peripheral blood smear at 100x oil immersion']. This is a published teaching case, not real patient material.

Before I share my own interpretation, please:

1. **Describe what you see** in the image, organized by what's visible at this magnification. Use morphologic descriptors, not diagnostic language ('clusters of cells with hyperchromatic nuclei and high N:C ratio' not 'malignant cells').
2. **Identify the cell type or tissue type** if you can.
3. **Generate a differential** of 3-5 entities based on the visible features.
4. **Name the single most discriminating feature** you'd want to see on additional levels, stains, or higher magnification.

Then ask me ONE question about my interpretation before you reveal what you think the diagnosis is.""",
    output="Structured description → cell/tissue ID → 3-5 entity differential → one discriminating feature → one question to you. The model holds back the diagnosis until you've engaged.",
    failures="""- The model jumps to a diagnosis before describing the morphology. Push back: 'describe first, diagnose later.'
- The model uses diagnostic language disguised as description ('atypical cells').
- The model confidently identifies a finding that isn't actually visible in the image. Watch for this — multimodal AI is improving but still routinely confident-wrong.""",
    verification="""- **Never upload real patient images.** Use published teaching cases, public-domain images, or your legitimately-cleared teaching collection.
- The model's morphologic descriptions are fallible — verify against the published answer for the teaching case before incorporating into your mental model.
- See [Guardrails](library.html#/docs/guardrails) for the full multimodal rules."""
)

BODIES[f"{P1}/multimodal-spep-ife.md"] = body(
    intent="Upload a SPEP or IFE trace and have the model walk through the interpretation, with you predicting each step before the model reveals it.",
    when="During your first month of clinical chemistry, when you've read the chapter but haven't yet built the pattern recognition. Use published teaching traces, not institutional cases.",
    prompt="""I'm uploading a [serum protein electrophoresis / immunofixation electrophoresis] trace. This is a published teaching case.

I want to drill my interpretation, not just see the answer. Use this protocol:

1. **Quiz me first.** Ask me what I observe in [a specific region — e.g., 'the gamma region', 'between the beta-2 and gamma regions'] before you describe it.
2. **After I answer, confirm or correct my observation.** If I'm wrong, name the specific morphologic feature I missed.
3. **Move to the next region** with another question.
4. **After we've worked through the trace**, ask me what additional testing I'd order and why.
5. **Only after I've committed** to my interpretation, give me your full interpretation and the published diagnosis.

Start with the broadest observation: what stands out about this trace compared to a normal one?""",
    output="A back-and-forth conversation, region by region, ending with your committed interpretation and then the model's. The interaction structure (quiz first, reveal later) is the point.",
    failures="""- The model reveals the diagnosis prematurely. Push back: 'don't tell me yet — quiz me first.'
- The model accepts a wrong observation without correcting it. Push back: 'be honest — was my observation correct?'
- The model fabricates features that aren't visible in the trace.""",
    verification="""- **Use published teaching traces or public-domain images only.** No institutional cases, no de-identified real patient material.
- Verify the model's morphologic descriptions and final interpretation against the published answer key for the teaching case.
- See [Guardrails](library.html#/docs/guardrails)."""
)

# ---------------------------------------------------------------------------
# Pillar 2 — Teaching (16 prompts)
# ---------------------------------------------------------------------------

P2 = "library/pillar-2-teaching/prompts"

BODIES[f"{P2}/acgme-epa-objectives.md"] = body(
    intent="Generate ACGME-milestone-aligned or EPA-mapped learning objectives for a teaching session on a given topic.",
    when="When you're designing a new teaching session and need to write objectives that will pass review by your CCC or program leadership.",
    prompt="""Generate [N] learning objectives for a [duration]-minute teaching session on [topic] for [audience — e.g., 'PGY-2 CP residents in their second month of blood bank'].

Each objective should:

1. Begin with 'By the end of this session, the resident will...' followed by a measurable verb (interpret, distinguish, formulate, justify — NOT 'understand' or 'know').
2. Specify the **condition** under which the behavior occurs (given a case, given a set of lab values, etc.).
3. Specify the **criterion** for success (with what accuracy, citing which guideline, etc.).
4. Map to a specific **ACGME milestone sub-competency** (e.g., 'PC1.3 Interpretation of Diagnostic Studies') or **EPA** (if your program uses EPAs).

After the objectives, identify which milestones are NOT addressed by these objectives — useful context for the program director.""",
    output="N objectives in proper format with explicit condition + behavior + criterion + milestone/EPA mapping, plus a note on milestones not covered.",
    failures="""- Objectives use 'understand' or 'know' instead of measurable verbs.
- The milestone mapping is approximate or invented. Verify against your program's actual milestone document.
- Criteria are too vague ('correctly') to be assessed.""",
    verification="""- Verify the milestone or EPA mapping against your program's official document. ACGME milestones are revised periodically; the model may reference an older version.
- Run the objectives by your program director or CCC chair before using them in a formally documented session."""
)

BODIES[f"{P2}/blooms-mcq.md"] = body(
    intent="Generate MCQs at a specified Bloom's level (recall vs application vs analysis) with rationales calibrated to the cognitive task. The Bloom's level matters because most resident MCQs default to recall when application is what residents actually need.",
    when="When you're building assessment items and want to test reasoning, not just memorization.",
    prompt="""Generate [N] multiple-choice questions on [topic] for [PGY level] residents. I want the questions distributed across Bloom's taxonomy levels:

- [X]% at **Application** (use knowledge in a new situation — typical clinical vignette)
- [Y]% at **Analysis** (distinguish, compare, organize — requires breaking down a complex case)
- [Z]% at **Evaluation** (justify a decision based on criteria — requires choosing among multiple acceptable approaches)

Avoid Remember/Understand level questions — they don't test what residents actually need.

For each question:

1. Provide the question and 5 answer choices.
2. Label the Bloom's level.
3. Explain *why* this question is at that level (what cognitive task is required to answer it).
4. Provide rationales for all five choices.

The rationales should explain the *reasoning*, not just state which is right.""",
    output="N questions with Bloom's labels, level justifications, and full rationales. The 'why this level' explanation should make explicit what cognitive task the question tests.",
    failures="""- The model mis-labels Bloom's level (calls a recall question 'application' because it includes a clinical vignette).
- All questions end up at the same actual level despite the requested distribution.
- 'Application' questions test the same fact a 'recall' question would, just dressed up.""",
    verification="""- Verify the correct answer against an authoritative source.
- Pressure-test the Bloom's level: would a resident who has only memorized facts be able to answer this question? If yes, it's not actually application or higher.
- Have a colleague who teaches this topic review the questions before using them in formal assessment."""
)

BODIES[f"{P2}/case-vignette-pgy.md"] = body(
    intent="Generate a case vignette calibrated to a specific PGY level — appropriate complexity, age-appropriate red herrings, the right amount of clinical context.",
    when="When designing case-based teaching and you need a vignette tuned to a specific level. PGY-1 vignettes should be simpler than PGY-3 vignettes in ways that go beyond word count.",
    prompt="""Generate a case vignette for a teaching session targeted at [PGY level] residents on [topic / diagnosis being taught].

Calibration guidance by level:

- **PGY-1:** classic presentation, one main differential to resolve, all relevant data given, no significant red herrings.
- **PGY-2:** more typical presentation with a complicating factor (atypical demographic, comorbidity that obscures the picture, a 'positive' test result that's actually a red herring).
- **PGY-3:** atypical presentation, ambiguous lab/imaging data, must integrate multiple discordant findings.
- **PGY-4 / Fellow:** rare entity or atypical presentation of common entity, requires judgment calls under uncertainty.

The vignette should:

1. Be 4-7 sentences long.
2. Include demographic detail relevant to the differential (don't default to a 50-year-old white male).
3. Include the data the resident needs to reason from, no more.
4. End at the point where the resident must commit to an interpretation or next step.

After the vignette, provide:
- The intended diagnosis.
- The 2-3 most likely wrong answers a resident at this level would give, and why.
- One discussion question to use after the resident commits.""",
    output="The vignette + intended diagnosis + wrong-answer analysis + discussion question. The wrong-answer analysis is the most useful part for teaching.",
    failures="""- The vignette is technically 'PGY-3' but the answer is obvious — calibration miss.
- Demographic defaults to standard textbook archetype.
- The 'wrong answers a resident would give' are improbable rather than the real common errors.""",
    verification="""- Pressure-test the vignette against a resident at the target level before using it in a session — is the difficulty actually right?
- Check that the demographic detail is consistent with the diagnosis's actual epidemiology, not a stereotype.
- No PHI, ever — this is fictional or genericized."""
)

BODIES[f"{P2}/matched-case-pair.md"] = body(
    intent="Generate two cases that share a superficial presentation but resolve to different diagnoses, designed to highlight a specific discriminating feature. The pair structure forces residents to notice the discriminator.",
    when="When teaching a differential where two entities are commonly confused, especially when the discrimination is taught in a textbook but rarely drilled.",
    prompt="""Generate a matched case pair for teaching the discrimination between [entity A] and [entity B] at [PGY level].

The pair should:

1. **Share superficial features** that put both entities in the differential (similar demographics, similar chief complaint, similar initial workup results).
2. **Diverge on the discriminating feature(s)** I want to teach — name those features explicitly.
3. **Be roughly equal in length and information density**, so the difficulty isn't in deciphering one but in noticing the discriminator.

For each case, provide:

- The vignette (4-6 sentences).
- The intended diagnosis.
- The discriminating feature(s) that should resolve it.

After both cases:

- A side-by-side comparison showing which features they share and which differ.
- The 'aha' question to use in teaching: when residents see both side by side, what question crystallizes the discrimination?""",
    output="Two paired vignettes + intended diagnoses + named discriminators + side-by-side comparison + 'aha' question.",
    failures="""- The two cases differ on a feature other than the intended discriminator (confounded teaching).
- One case is obviously harder than the other and residents notice the structural difference rather than the clinical one.
- The 'aha question' is leading rather than illuminating.""",
    verification="""- Verify the discriminating feature is actually the discriminator in current practice (not an outdated criterion).
- Pressure-test with a resident who hasn't been taught the discrimination — do they notice it, or does the pair just feel like 'two cases'?"""
)

BODIES[f"{P2}/osce-station.md"] = body(
    intent="Draft an OSCE station with patient script, stem, expected examinee actions, and a scoring rubric.",
    when="When designing summative or formative OSCE assessment, especially for stations that test communication or reasoning rather than knowledge.",
    prompt="""Draft an OSCE station for [target audience — e.g., 'CP residents at end-of-year assessment'] on [scenario type — e.g., 'critical value notification', 'frozen section consultation', 'handover to inpatient team'].

The station should include:

1. **Station instructions for the examinee** (what they're walking into, what they're expected to do, time limit).
2. **Patient/clinician script** for the simulated other party — what they say in response to common openers, what they hold back unless asked, how they respond to the examinee's communication style.
3. **The expected examinee actions** organized as: must do, should do, optional.
4. **A scoring rubric** with weighted line items — communication, content accuracy, prioritization, professionalism. Each item with behavioral anchors for novice/competent/proficient.
5. **A 'red flag' list** — actions that, if performed, indicate the examinee should be flagged for remediation.

Length: realistic for a 7-10 minute station.""",
    output="A complete station packet ready for use: examinee instructions, script, action checklist, rubric, and red flag criteria.",
    failures="""- The script is too rigid and breaks if the examinee asks unexpected questions.
- The rubric items are vague and can't actually be scored reliably by two raters.
- Red flag list confuses 'made a mistake' with 'is unsafe to practice'.""",
    verification="""- Pilot the station with a faculty member playing the examinee role before using it in formal assessment.
- Have a second rater score a video of the pilot independently — if you don't get agreement, the rubric needs more behavioral anchoring.
- Verify the clinical content (any lab values, drug names, dose adjustments) against current practice."""
)

BODIES[f"{P2}/slide-outline-1hr.md"] = body(
    intent="Generate a slide outline for a 1-hour lecture, including timing, beat structure, and recommended visuals for each slide.",
    when="When you've agreed to give a lecture and need a starting structure before you put a single slide in PowerPoint. Saves the 'staring at empty slides' phase.",
    prompt="""Generate a slide outline for a 1-hour lecture on [topic] for [audience].

Structure:

- **Total slides: 35-45.** Roughly 1 slide per 80-100 seconds. Resist the urge to cram more.
- **Beat structure:** opening hook (1 slide, 2-3 min) → roadmap (1 slide) → 3-4 content beats (8-12 slides each, ~12-15 min each) → synthesis (2-3 slides) → questions (1 slide, 5-10 min).
- **For each slide:** title, 2-3 bullet points of content (not full sentences), and a one-line recommended visual ('photomicrograph of X', 'algorithm flowchart', 'table comparing A and B', 'text only').
- **Mark moments of audience interaction** (poll, question, case to think about) at the transitions between beats.
- **Identify the 2 slides that, if you only had 30 seconds, you'd use.** Those are the slides that anchor the lecture.

After the outline, name the most likely point in the lecture where you'll run out of time, and the 2-3 slides you'd cut to recover.""",
    output="A 35-45 slide outline with titles, brief content, visuals, and interaction beats. Plus the anchor slides and a contingency cut list.",
    failures="""- The outline is text-heavy with no visual diversity — every slide is 'bullet points'.
- The interaction beats are filler rather than substantive.
- The 'anchor slides' aren't actually the most important; they're the ones that came first in the outline.""",
    verification="""- Walk through the outline at presentation pace (~80 seconds per slide). Does the timing work?
- Verify the substantive content for each beat against your subspecialty's reference. The model may sketch beats that turn out to be technically wrong.
- The recommended visuals are starting points; you supply the actual images and verify they're properly licensed."""
)

BODIES[f"{P2}/speaker-notes.md"] = body(
    intent="Generate speaker notes for an existing slide deck by pasting slide titles and bullet points, with the model filling in the connective tissue between bullets.",
    when="When you've made slides but haven't rehearsed yet, and need a script to anchor your first pass through the deck. Best for talks you'll give multiple times — the notes get refined each iteration.",
    prompt="""Generate speaker notes for the following slide deck. The talk is [N] minutes total for [audience].

For each slide, write speaker notes that:

1. Open with a transition sentence connecting from the previous slide.
2. Explain each bullet in 2-3 spoken sentences (more than the slide says, less than a paragraph).
3. Include the one specific example, anecdote, or analogy I should use here. Be concrete — 'the Bethesda case from last week' not 'a recent case'.
4. End with a bridge sentence to the next slide.

If a slide is a visual or a diagram with minimal text, the speaker notes should be longer — that's where I'm explaining what the audience sees.

Mark moments to pause for questions or audience interaction.

Slides:
[paste slide titles + bullet content, one slide per block]""",
    output="Per-slide speaker notes with transitions, expansions, specific examples, and bridges. The notes should be in spoken voice, not written voice — short sentences, no jargon you wouldn't actually say.",
    failures="""- The notes are written voice ('It is important to recognize that...') rather than spoken voice.
- The 'specific example' is generic ('think of a recent case').
- Transition sentences are formulaic ('Moving on to slide X').""",
    verification="""- Verify any clinical content the model adds beyond what was on the slide. The model fills in gaps and sometimes fills them with confident-wrong content.
- Rehearse the notes aloud. Spoken language reveals problems written language hides."""
)

BODIES[f"{P2}/visual-metaphor.md"] = body(
    intent="Generate visual metaphors for an abstract concept, ranked by precision vs accessibility. The point is not to pick the metaphor for you but to surface options you wouldn't have generated alone.",
    when="When you're explaining an abstract concept (gating in flow cytometry, antibody-antigen interactions, deconvolution) and your usual go-to metaphor isn't landing. Brainstorming fuel, not final answer.",
    prompt="""Generate 5-7 visual metaphors for explaining [abstract concept] to [audience].

For each metaphor:

1. The metaphor in one sentence.
2. **What it captures well** — which features of the concept does this metaphor faithfully represent?
3. **Where it breaks down** — the feature of the concept the metaphor distorts or misses.
4. **Precision score** (1-5): how technically accurate is the metaphor when pushed?
5. **Accessibility score** (1-5): how immediately graspable is it for the target audience?

Rank the list by (precision × accessibility), but acknowledge the trade-off — the most accessible metaphors are often the least precise.

End with: which metaphor would you pick if I'm teaching to medical students vs. attendings, and why?""",
    output="5-7 ranked metaphors with strengths, weaknesses, and scores. Plus the differentiated recommendation for different audiences.",
    failures="""- All metaphors are variants of one ('it's like a key in a lock' / 'it's like a key fitting a door').
- Precision scores are inflated — every metaphor is rated 4-5 on precision.
- The 'breaks down' analysis is superficial.""",
    verification="""- Push each metaphor to its breaking point with an expert in your subspecialty. The metaphors that survive expert pushback are the ones to use; those that don't will mislead learners.
- Trust audience feedback over your own assessment — if the metaphor doesn't land in the room, the precision score doesn't matter."""
)

BODIES[f"{P2}/audience-polls.md"] = body(
    intent="Generate audience poll questions at specific moments in a lecture to drive engagement and surface misconceptions. Different from MCQs — polls are designed for live response and discussion, not assessment.",
    when="When you're delivering a 30-60 minute talk and want to break up the lecture rhythm with 2-3 polling moments. Poll questions need different design than test questions.",
    prompt="""Generate [N] audience poll questions for a [duration]-minute lecture on [topic] for [audience].

Each poll should:

1. Be answerable in 30-60 seconds — short stem, ideally 3 answer choices (not 5).
2. **Have a 'wrong' answer that most of the audience will pick**, by design. The polling moment is teaching, not assessment — the value is in the wrong answer being common and the explanation being illuminating.
3. **Map to a specific point in the lecture** where it serves as a transition or a moment of misconception-surfacing.
4. Include a 1-2 sentence note for me on how to use the result: what to say when the audience splits 60/30/10, what to say when they all get it right.

For each poll, provide:

- The question and answer choices.
- The intended placement in the lecture.
- The likely audience distribution.
- The teaching beat that follows.""",
    output="N polls with placement, expected distribution, and follow-up teaching beats. The polls should feel like *teaching moments*, not pop quizzes.",
    failures="""- Polls are designed as assessment, with one obvious right answer — kills engagement.
- The 'common wrong answer' is not actually common — model misjudges audience.
- No suggestion for what to do with the result, so the poll lands flat.""",
    verification="""- Run the poll past a colleague at the target audience level. If they get the 'intended wrong answer' right cold, the poll won't work as designed.
- Verify the correct answer."""
)

BODIES[f"{P2}/video-script.md"] = body(
    intent="Draft a video script and storyboard for a short educational explainer, with shot suggestions and on-screen text cues.",
    when="When you're producing short educational content (2-5 min explainers, social media clips, asynchronous training) and need a script that thinks about visuals, not just dialogue.",
    prompt="""Draft a script for a [duration]-minute educational video on [topic] for [audience].

Format:

- **Two columns:** left = narration; right = visuals/on-screen text/cuts.
- **One row per beat**, with each beat being 5-15 seconds of video.
- **Total length:** target the duration above; flag if the script will overrun.
- **Hook:** the first 5 seconds must give the viewer a reason to keep watching. Stating the topic isn't a hook.
- **Visuals:** 'cut to photomicrograph', 'animated diagram of antibody binding', 'on-screen text: NORMAL RANGE 4.0-11.0 K/uL'. Be specific about what's on screen at each beat.
- **End with a single takeaway** that fits in 5 seconds.

After the script, list:
- The 2-3 shots/assets I'll need to produce or source.
- The 1 sentence the viewer will remember 24 hours later.""",
    output="Two-column script with timed beats, opening hook, specific visuals, and a final takeaway. Plus an asset list and a stated 24-hour-takeaway.",
    failures="""- The 'hook' is just the topic stated declaratively.
- Visuals are placeholders ('relevant image') rather than specific.
- The script is too dense to fit in the stated duration when read at natural pace.""",
    verification="""- Read the script aloud at natural pace and time it. AI-generated scripts almost always overrun.
- Verify any specific clinical content.
- Source visuals from properly licensed material; do not use images without clear permission."""
)

BODIES[f"{P2}/resident-feedback-note.md"] = body(
    intent="Convert bullet-point observations from a rotation into a polished feedback note, preserving specificity while improving readability.",
    when="When you've taken notes during a rotation and need to convert them into a feedback document the resident will actually read and remember.",
    prompt="""Convert these rotation observations into a feedback note for [resident name initial], a [PGY level] who just finished their [N]-week rotation on [service].

Observations (mix of strengths, areas for growth, specific instances):
[paste your bullet notes — specific incidents, recurring patterns, comparative observations]

Format:

1. **Opening orientation** (1-2 sentences): the rotation, the level of trust the resident operates at, the overall arc.
2. **Strengths section:** 2-4 specific strengths, each tied to a behavior or incident I noted. Avoid generic praise.
3. **Growth section:** 2-3 specific growth areas, each tied to a behavior or incident. Use language that's actionable — what would 'better' look like?
4. **One specific behavioral commitment** for the next rotation, framed as a question the resident should ask themselves at each sign-out.
5. **Closing** (1 sentence): a forward-looking statement, not a hollow compliment.

Tone: warm but honest. Specific over generic. Behavioral over personality-based.

Do NOT add observations that aren't in my notes. If something is missing, leave it out rather than padding.""",
    output="A feedback note in five sections that reads like a real attending wrote it — specific, behavioral, actionable. The 'behavioral commitment' question is the most valuable line.",
    failures="""- The model adds praise or critique you didn't write. Watch for this — it dilutes credibility.
- Growth areas are framed as personality traits ('be more confident') rather than behaviors.
- The closing is hollow ('great work, keep it up!').""",
    verification="""- Re-read against your original observations. Anything in the note that's not in your notes is the model speaking, not you. Delete or rewrite.
- Sanity-check the tone with how you'd actually talk to this resident.
- Run formal feedback notes through your institution's required template format if one exists."""
)

BODIES[f"{P2}/ccc-narrative-comment.md"] = body(
    intent="Convert milestone scores and bullet observations into a CCC narrative comment that connects evidence to the assigned milestone level.",
    when="When you're writing CCC narratives at the semi-annual review and need to convert your numeric scores into prose that justifies the rating with evidence.",
    prompt="""Write a CCC narrative comment for [resident initial], PGY-[level], for [milestone sub-competency — e.g., 'PC1.3 Interpretation of Diagnostic Studies'].

My assigned level: [milestone level]
My evidence/observations: [paste bullet observations from this review period that support this level]
Comparison to prior: [stayed the same / progressed / regressed since last review]

Format the narrative:

1. **One sentence stating the level and the trajectory** (progressed, plateaued, etc.).
2. **2-3 sentences of behavioral evidence** for this level — specific behaviors I observed.
3. **One sentence on the next milestone behavior** the resident is approaching or working toward.
4. **One sentence with a forward-looking expectation** for the next 6 months.

Tone: factual, evidence-based, defensible. The narrative should make sense to an external reviewer (PGY-1 ACGME visit) reading the file cold.

Do NOT inflate beyond the evidence I provided. If the evidence supports level 3 but I've inadvertently described level 4 behaviors, flag the inconsistency.""",
    output="A four-sentence narrative tightly mapped to the milestone, with explicit evidence and forward-looking framing.",
    failures="""- The narrative inflates the level beyond the evidence.
- 'Evidence' is generic ('resident demonstrates competence') rather than behavioral.
- The forward-looking expectation is unrealistic given the current level.""",
    verification="""- Read against your bullets — every claim in the narrative should be traceable to a bullet.
- Have a colleague on the CCC read for tone consistency with how they'd write a similar narrative.
- Verify the milestone level descriptors against your program's current milestone document — these get revised periodically."""
)

BODIES[f"{P2}/lor-starting-draft.md"] = body(
    intent="Generate a starting draft for a letter of recommendation. **Heavy editing required** — the model produces structurally plausible but generic prose; the specific anecdotes and judgments must come from you.",
    when="When you've agreed to write a LOR and need to break the blank-page paralysis. Treat the output as scaffolding, not as a letter you'd sign.",
    prompt="""Draft a letter of recommendation for [applicant name and degree(s)] applying to [program type / specific program] starting in [year].

Context I'll provide:
- My relationship to the applicant: [how long you've known them, in what capacity, frequency of interaction]
- My role: [your title, why your voice carries weight for this application]
- Their strengths I want to highlight: [specific traits + the specific anecdotes that demonstrate each]
- What I want the reader to know that's not on the CV: [the differentiator]
- Their areas for growth I want to acknowledge honestly: [optional but recommended for credibility]

Letter structure:

1. Opening: relationship, capacity, and a one-sentence headline of who this person is.
2. Body paragraph(s) — one per strength, each with the specific anecdote that demonstrates it. Replace any placeholders with specifics; do not leave generic.
3. A paragraph that says what distinguishes this applicant from others at their level.
4. Closing: explicit recommendation with appropriate strength, and an offer to discuss further.

**Critical:** the letter MUST be heavily edited by me before sending. The model will produce structurally plausible prose that reads as generic to experienced LOR readers (program directors read hundreds and recognize template language). My job is to inject specificity, my actual voice, and the anecdotes only I would know.""",
    output="A draft letter with placeholders where you'll need to insert specifics. The draft is the skeleton; you supply the flesh.",
    failures="""- The model produces generic praise that sounds like every other LOR.
- The 'distinguishing' paragraph is platitudinous.
- Quoted anecdotes get distorted in translation.""",
    verification="""- **Read every sentence and ask: would I write this exact sentence?** Rewrite the ones where the answer is no — that's most of them.
- Verify the applicant's accomplishments, dates, and dosing of praise.
- LOR readers detect AI-template language. The differentiator is your specific voice and your specific knowledge — that has to come from you, not the model.
- See [Guardrails](library.html#/docs/guardrails) on the structural plausibility failure mode."""
)

BODIES[f"{P2}/journal-club-discussion-q.md"] = body(
    intent="Generate 5 discussion questions for a journal club paper, ranging from methods critique to clinical implications.",
    when="When you're leading journal club and want a question set that escalates from concrete to abstract, ensuring the discussion doesn't stall at 'I liked the paper'.",
    prompt="""Generate 5 discussion questions for a journal club discussion of [paper citation]. The audience is [PGY level] residents and faculty.

Structure the questions to escalate:

1. **A concrete methods question** — what specific design choice or analytic approach should we scrutinize? Answer should be in the paper.
2. **A finding-level question** — how confident should we be in the headline result, given the design? Requires interpretation.
3. **A generalizability question** — does this result apply to our patient population? Requires connecting paper to practice.
4. **A practice-change question** — should this change what we do, and if so, how? Requires judgment.
5. **A contested question** — one that reasonable people would disagree on. Should provoke real debate.

For each question, include:
- The question itself.
- One sentence on what makes it a productive question (what discussion does it open?).
- The 'wrong' response that's most likely to come up early in discussion and how to redirect.""",
    output="5 escalating questions with productivity notes and predicted-wrong-response handling. The fifth question should be genuinely contested.",
    failures="""- All 5 questions are at the same level of abstraction.
- The 'contested question' has an obvious right answer and doesn't actually provoke debate.
- The 'wrong response' is straw-man rather than the real misconception.""",
    verification="""- Verify the methods-level question is answerable from the actual paper.
- Pre-test the contested question with a colleague — if they immediately agree with you, it's not actually contested."""
)

BODIES[f"{P2}/tumor-board-presentation.md"] = body(
    intent="Generate a tumor board case presentation outline given clinical history, imaging, and pathology findings. Tumor board presentations have a specific structure that AI can reliably scaffold.",
    when="When you're presenting a case at tumor board and need a structured outline to follow. Especially useful as a residency teaching tool — junior residents need to learn the structure.",
    prompt="""Generate a tumor board case presentation outline for the following case:

- **Clinical history (de-identified):** [paste, no PHI]
- **Imaging findings:** [paste]
- **Pathology findings:** [paste — gross, microscopic, IHC, molecular as available]
- **Question for the board:** [what decision are you bringing to the multidisciplinary group? — staging, treatment plan, second opinion, etc.]

Outline structure:

1. **One-sentence patient summary** (anonymized): age range, key comorbidity if relevant, presentation.
2. **Imaging summary** in radiologist-friendly framing: what they need to know to interpret the pathology.
3. **Pathology in order:** gross → microscopic → IHC → molecular. Lead with the diagnostic features, not the workup history.
4. **Diagnosis and stage** if available.
5. **The decision point** — what the board is being asked to advise on.
6. **The 2-3 most likely questions** from the board (med onc, rad onc, surg, radiology) and the data points you should have ready.

Length: 3-4 minutes of presentation time. No PHI.""",
    output="A structured outline ready to present, with anticipated questions and data points to have ready.",
    failures="""- Outline includes information that would identify a patient.
- The 'decision point' is buried rather than stated explicitly.
- Anticipated questions miss the actual ones that get asked at your institution's tumor board.""",
    verification="""- **No PHI ever.** Strip names, MRNs, exact ages, dates of service, institutional identifiers.
- Verify the pathology summary against your sign-out — the model may simplify in ways that mislead.
- Run anticipated questions by a colleague who attends your tumor board regularly."""
)

BODIES[f"{P2}/resident-as-teacher.md"] = body(
    intent="Scaffold a resident-as-teacher session: how would you teach this topic to a junior resident, what are the common misconceptions, what is the one slide you would build.",
    when="When a senior resident is asked to give a teaching session and needs a structured way to think about teaching, not just content delivery.",
    prompt="""I'm a [PGY level] resident asked to give a [duration]-minute teaching session on [topic] to [audience — e.g., 'incoming PGY-1s in their first week of CP'].

Help me think through this as a teaching exercise, not just a content delivery exercise.

1. **What is the ONE concept I most want them to walk away with?** State it in one sentence.
2. **What are the 2-3 common misconceptions** about this topic that I should anticipate and address?
3. **If I had only ONE slide, what would it show?** Describe the visual or text in detail.
4. **What is the simplest exercise** I could do in the session that would let me see whether they understood the one concept?
5. **What's the question I should NOT try to answer in this session** — the related topic that would be a different talk?
6. **How will I know if the session went well?** Give me 2-3 observable indicators during or right after the session.""",
    output="The six answers in order, with the 'one concept' and the 'one slide' being the centerpieces. The exercise should be doable in the time you have.",
    failures="""- The 'one concept' is too broad to fit in one sentence.
- The misconceptions are generic.
- The 'one slide' is bullet points rather than something genuinely teachable.""",
    verification="""- Run the 'one concept' by a colleague at the target level: does it land?
- The misconceptions list is most useful when validated by an attending who has taught this topic — they know which misconceptions are real.
- The 'observable indicators' should be specific enough that you can actually check them after the session."""
)

# ---------------------------------------------------------------------------
# Pillar 3 — Educational Operations & Documentation (27 prompts)
# ---------------------------------------------------------------------------

P3 = "library/pillar-3-educational-operations/prompts"

# ---- Workshops (9) ----

BODIES[f"{P3}/workshops/announcement-registration.md"] = body(
    intent="Draft the announcement and registration copy for a workshop, including objectives, audience, prerequisites, and a clear call to action.",
    when="When you've committed to running a workshop and need to publicize it 6-10 weeks out. The copy needs to drive registration without overpromising.",
    prompt="""Write an announcement and registration page for the following workshop:

- **Title:** [workshop title]
- **Audience:** [who it's for, level, prerequisites if any]
- **Date / location / format:** [in-person / hybrid / virtual, dates, venue]
- **Duration:** [hours, breaks, end-of-day plans]
- **Faculty:** [names + roles]
- **What attendees will be able to do after:** [3-5 learning outcomes in 'will be able to' language]
- **Cost / registration cap:** [if any]
- **Registration deadline and link/process:** [exact instructions]

Produce:

1. A 100-word **promotional blurb** suitable for email, Twitter, society newsletters.
2. A **full announcement page** (~300-400 words) with: opening 2-sentence hook, audience and prerequisites, learning outcomes, schedule overview, faculty bios in 1-2 sentences each, logistics, registration call-to-action.
3. A **registration confirmation email** template (~150 words) for attendees who sign up.

Tone: professional, specific, slightly warmer than a journal abstract. Avoid 'cutting-edge', 'revolutionary', and similar empty intensifiers.""",
    output="Three deliverables: blurb, announcement, confirmation email. Each calibrated to its medium.",
    failures="""- Empty intensifiers and corporate-marketing tone ('don't miss this exciting opportunity').
- Vague learning outcomes ('participants will gain insight').
- Confirmation email that doesn't include what attendees actually need to prepare.""",
    verification="""- Check faculty bios with each faculty member before publishing.
- Verify dates, venue, registration link, and any CME credit claims.
- Confirm registration cap is realistic for the venue."""
)

BODIES[f"{P3}/workshops/pre-workshop-survey.md"] = body(
    intent="Design a short pre-workshop survey that captures attendee level, expectations, and content preferences without burning their goodwill.",
    when="3-4 weeks before the workshop, when you want enough data to calibrate content but not so much that response rate craters.",
    prompt="""Design a pre-workshop survey for [workshop title]. Audience: [audience description].

The survey should:

1. Take **under 3 minutes** to complete. Hard cap.
2. Include 5-8 questions total.
3. Capture the data I actually need to calibrate the workshop, not nice-to-haves.

Required data:
- Their baseline familiarity with the topic (single Likert or skill-anchored multiple choice).
- What they're hoping to walk away with (free text, max 1 sentence).
- Their role and PGY/years in practice.
- Any specific topic they want covered (free text, optional).

Format each question with:
- The question itself.
- The response format (single-select, multi-select, Likert 1-5, free text).
- Why the question is in the survey (what decision will I make with the answer?).

End with a one-sentence email template for sending the survey link.""",
    output="A 5-8 question survey with response formats and explicit rationale for each question. Plus an email template.",
    failures="""- Survey is too long; response rate will be poor.
- Questions don't actually inform decisions you'll make.
- Free text fields are too open and produce unanalyzable results.""",
    verification="""- Pilot-test the survey with 2-3 representative attendees and time them. Adjust if it takes more than 3 minutes.
- Map each question to a specific decision you'll make based on the result. If you can't map a question to a decision, cut it."""
)

BODIES[f"{P3}/workshops/facilitator-runofshow.md"] = body(
    intent="Generate a minute-by-minute facilitator run-of-show for a workshop, including transitions, contingencies, and named owners for each block.",
    when="One week before the workshop. The run-of-show is the document the lead facilitator holds in their hand all day.",
    prompt="""Generate a minute-by-minute facilitator run-of-show for [workshop title] on [date], from [start time] to [end time].

Workshop structure: [paste the agenda with block names, durations, lead facilitators]

For each block, the run-of-show should include:

- **Time range** (e.g., 9:15-9:35)
- **Block name and lead facilitator**
- **One-line content summary**
- **Setup needed** (room arrangement, AV, materials to distribute)
- **Transition cue** (how does the lead facilitator hand off to the next block?)
- **Contingencies:** what's the fallback if (a) the block runs long, (b) the block runs short, (c) the tech breaks?

Include explicit blocks for:
- Registration / check-in / coffee
- Bathroom / coffee breaks (every 90-120 min)
- Lunch (with timing for re-gathering)
- Anything the lead facilitator needs to do behind the scenes (e.g., 'set up next station while panel runs')

End with:
- A list of materials and AV needs by block.
- The roles list: who does what (lead, support, AV, runner).""",
    output="A document the lead facilitator can use to run the day without thinking. Should be print-friendly.",
    failures="""- Blocks transition without explicit cues — leads to awkward silences.
- No contingencies for running long/short.
- Lunch timing doesn't account for re-gathering.""",
    verification="""- Walk through the run-of-show with the lead facilitator and at least one other staff member before the day.
- Verify any AV needs with the venue."""
)

BODIES[f"{P3}/workshops/station-by-station-guide.md"] = body(
    intent="Generate per-station facilitator guides for a rotating-station workshop, including learning objectives, materials, timing, and assessment per station.",
    when="2 weeks before a station-based workshop. Each station owner gets their own guide.",
    prompt="""Generate a per-station facilitator guide for a rotating-station workshop. Each station gets its own guide.

Stations: [list each station with its topic and lead facilitator]
Time per station: [minutes per rotation]
Number of rotations: [how many groups will cycle through each station]

For EACH station, produce:

1. **Station header:** name, lead facilitator, topic, time allocation.
2. **Learning objectives** (2-3, in 'will be able to' language).
3. **Materials list:** everything the station owner needs (paperwork, samples, AV, models).
4. **Setup instructions:** what to do before the first group arrives.
5. **Minute-by-minute script for one rotation:** opening, content blocks, closing. Should fit in the time allocation with 2-3 min buffer.
6. **What to do between rotations:** reset instructions.
7. **What an attendee should walk away with** (the artifact, the demonstrated skill, the question they can now answer).
8. **Common attendee questions and the prepared answer.**
9. **If you have extra time:** an optional deepening activity.

Format consistently across all stations so facilitators can quickly find what they need.""",
    output="One guide per station, each in the same format. Total length: 1-2 pages per station.",
    failures="""- Objectives aren't actually achievable in the time allocated.
- Minute-by-minute timing doesn't include reset time between rotations.
- No accommodation for early-finisher groups.""",
    verification="""- Run through one station's guide as if you were the facilitator, with a stopwatch. Adjust timing.
- Have each station's actual lead read and edit their own guide before the day."""
)

BODIES[f"{P3}/workshops/badge-design-spec.md"] = body(
    intent="Draft a specification for printable workshop badges — fields, dimensions, color, accessibility, and print-shop-ready dimensions.",
    when="3-4 weeks before the workshop, when you're ordering supplies and need a spec to send to the print shop or graphic designer.",
    prompt="""Draft a print specification for workshop attendee badges. Workshop: [name and date].

The spec should include:

- **Dimensions:** physical size of the badge (mm or inches), orientation (portrait/landscape), bleed area if printed professionally.
- **Required fields:** what appears on the badge (name in large type, institution in smaller type, role, date or event name, etc.) with the relative font size and position of each.
- **Optional fields:** any conditional content (faculty/attendee/staff color coding, table assignment, dietary marker if used).
- **Color palette:** specific colors with hex codes; reasonable defaults if I don't specify.
- **Font:** legible at distance, with size minimums for accessibility (e.g., name in 24-32pt).
- **Lanyard / holder type:** clip vs lanyard, hole position, paper weight or material.
- **Quantity to order** with at least 10% buffer for last-minute attendees and reprints.

End with a print-shop-ready summary I can paste into an order form.""",
    output="A spec document plus a print-shop summary. Should be unambiguous enough that two designers would produce identical badges.",
    failures="""- Font sizes too small to read from across a room.
- No buffer quantity, so you run out at registration.
- Color choices that don't meet WCAG contrast for the text-on-background.""",
    verification="""- Print one prototype and test legibility from 6 feet.
- Verify the lanyard/holder type matches the badges you're ordering."""
)

BODIES[f"{P3}/workshops/access-card-layout.md"] = body(
    intent="Specify a printable access card layout for workshop attendees with QR code, name, role, and event branding.",
    when="When attendees need a card that grants access to a companion site, a Slack channel, or other workshop resources. Pairs with the badge but is more durable and portable.",
    prompt="""Specify a print layout for an attendee access card for [workshop name].

The card should be **the size of a business card or hotel keycard** (specify exactly) and include:

1. Front of card:
   - Workshop title and date.
   - Attendee name (placeholder for personalization).
   - A QR code linking to [specific URL — e.g., the companion site, a Slack invite, the workshop schedule].
   - Event branding (color, logo if applicable).
2. Back of card:
   - 1-3 line description of what scanning the QR gets the attendee.
   - Any usage instructions (e.g., 'access valid through [date]', 'one-time use').
   - Contact for help.

Include:

- Exact dimensions and bleed area.
- QR code size minimum to ensure scannability (typically 1 inch / 25mm minimum).
- Font sizes for name vs body text.
- File format expected by your print shop (PDF, AI, etc.).

End with a sample of the front and back as ASCII art so I can visualize the layout.""",
    output="Full specification + visualized layout. Should be print-shop-ready.",
    failures="""- QR code too small to scan reliably.
- No fallback instruction if the QR doesn't work (e.g., 'or visit [URL]').
- Layout is busy and the QR is hard to find.""",
    verification="""- Print one prototype and scan the QR with multiple phone types and lighting conditions.
- Verify the URL is correct and resolves to the intended destination."""
)

BODIES[f"{P3}/workshops/certificate-of-completion.md"] = body(
    intent="Draft a certificate of completion template with attestation language, signature blocks, and a layout brief.",
    when="The week before the workshop, so certificates can be printed (or set up for digital delivery) ahead of the closing session.",
    prompt="""Draft a certificate of completion template for [workshop name] on [date], held at [location].

The certificate should include:

1. Standard certificate header: 'Certificate of Completion' or equivalent.
2. **Attestation language**: 'This certifies that [Name] has successfully completed [workshop title] on [date] in [city]', with the workshop's hour count if applicable.
3. **Learning outcomes**: list the workshop's stated objectives (so the certificate documents what the attendee was certified to have completed).
4. **Issuing organization** with logo placeholder.
5. **Signature blocks**: typically 1-2 signers (workshop director, institutional sponsor). Include printed name, title, and signature line.
6. **Authentication elements**: certificate number, QR code linking to a verification page (optional), date of issue.

Layout brief:
- Orientation (landscape recommended for certificates).
- Suggested font (a serif display face for traditional feel; a clean sans-serif for modern).
- Color palette (institutional colors or neutral palette).
- Border style (none, simple line, classical ornament).

Produce both:
1. The plain-text content with placeholders for name and date.
2. A layout brief that a designer could use to produce the visual template.

Avoid CME claims unless I've specified the workshop is CME-accredited.""",
    output="The text content + the visual layout brief. Together they enable production of the certificate.",
    failures="""- Includes CME credit claims without verifying accreditation.
- Attestation language is so generic the certificate is meaningless.
- Learning outcomes section is omitted, reducing the certificate's documentary value.""",
    verification="""- If claiming CME or any continuing education credit, verify accreditation status before including.
- Confirm signers' titles are current.
- Have one printed prototype reviewed for any layout issues at full size."""
)

BODIES[f"{P3}/workshops/post-workshop-thank-you.md"] = body(
    intent="Draft a post-workshop thank-you email to attendees with a link to the companion materials and a feedback request.",
    when="Within 24-48 hours after the workshop ends, while attendees still remember the experience.",
    prompt="""Draft a post-workshop thank-you email to attendees of [workshop name] held on [date].

The email should:

1. **Subject line** (short, specific, recognizable in a busy inbox).
2. **Opening** (1-2 sentences): brief thanks and a specific reference to a moment from the workshop (you'll need to fill this in with the actual moment).
3. **What's available now**: links to the companion materials site, slides, recordings (if any), reading list — be explicit about what each link goes to.
4. **What's coming**: anything you've promised that's still in production (e.g., 'we'll share the post-workshop summary by [date]').
5. **Feedback request**: link to the survey, with a one-sentence explanation of why their feedback matters (this affects response rate). 5 minutes max.
6. **Closing**: a forward-looking invitation (next workshop, contact for follow-up questions).

Tone: warm, specific, professional. Avoid 'we had such a great time' generic thanks.

Length: under 200 words. Attendees skim email; don't waste their attention.""",
    output="A complete email ready to send, with placeholders only for the specific 'moment from the workshop' line.",
    failures="""- Generic 'thanks for attending' tone that signals you didn't actually pay attention.
- Too many links — attendees won't click any.
- Feedback survey buried.""",
    verification="""- Verify all links work before sending.
- The specific 'moment' line has to come from you — the model doesn't know what happened in the room."""
)

BODIES[f"{P3}/workshops/faculty-feedback-summary.md"] = body(
    intent="Convert raw feedback comments into a summary email to faculty, themed by issue and ordered by frequency, with suggested actions.",
    when="1-2 weeks after the workshop, when feedback is in but faculty are still close enough to the event to engage with it.",
    prompt="""Convert the following raw attendee feedback into a faculty debrief email.

Raw feedback: [paste the feedback comments — could be from a survey, exit ticket, or post-event responses]

Structure the debrief:

1. **One-paragraph summary**: overall reception, response rate, top-level themes.
2. **What worked** (themes that came up positively, ordered by frequency, with example quotes — paraphrased to preserve anonymity if needed).
3. **What didn't work** (themes that came up negatively, ordered by frequency, with example quotes).
4. **The signal vs the noise**: which comments represent systemic issues vs one-off complaints. Be honest with faculty about both.
5. **Suggested actions for the next iteration**: 3-5 specific changes, ranked by ease × impact.
6. **A note on response rate and selection bias**: who responded and who didn't, and what that means for interpreting the data.

Tone: data-forward, no defensiveness, no minimization of critical feedback. Faculty trust this kind of debrief when it's honest.""",
    output="A debrief email with all six sections, paraphrased quotes for anonymity, and ranked suggested actions.",
    failures="""- Selective reporting that favors positive feedback.
- Quotes that could identify individual respondents.
- Suggested actions are aspirational rather than operational.""",
    verification="""- Re-read against the raw feedback — confirm you haven't omitted significant negative themes.
- Anonymize all quotes — even paraphrased, check that no quote could be traced to a specific person.
- Run the debrief past one trusted faculty member before sending to the wider group."""
)

# ---- Rotations (8) ----

BODIES[f"{P3}/rotations/orientation-onepager.md"] = body(
    intent="Generate a one-page rotation orientation covering schedule, expectations, key contacts, and what success looks like by day 5.",
    when="Send to incoming residents the week before they start a rotation. The goal is to remove the 'I don't know what I don't know' fog of the first day.",
    prompt="""Generate a one-page orientation document for the [rotation name] rotation. Audience: [PGY level] residents starting the rotation.

The page should fit on one printed page (so be ruthless about what to include). Sections:

1. **Welcome and orientation logistics** (3-4 sentences): when and where to arrive on day 1, who to find, what to bring.
2. **Daily schedule template**: typical Monday-Friday, with sign-out times, didactics, conferences.
3. **Key contacts**: 3-5 people the resident should know (lab director, attending of the week, fellow, charge tech, scheduler). Name, role, how to reach.
4. **Reading for day 1**: 1-3 items, with rationale. Don't pad.
5. **What success looks like by end of week 1**: 3-4 observable indicators that the resident is on track.
6. **What to do if things aren't clear**: explicit escalation path.

Tone: welcoming, concrete, no jargon you wouldn't explain.""",
    output="A one-page document, printable and skimmable, that removes day-1 confusion.",
    failures="""- Tries to fit too much, defeats the one-page constraint.
- 'Key contacts' don't include the people who actually answer questions on day 1.
- Reading list is aspirational rather than essential.""",
    verification="""- Pilot with a recent rotator: would they have wanted this document?
- Verify contact info is current.
- Update each rotation block (don't recycle stale info)."""
)

BODIES[f"{P3}/rotations/expectations-doc.md"] = body(
    intent="Generate a rotation expectations document with milestone-aligned objectives, daily and weekly responsibilities, and the supervision model.",
    when="When you're rolling out a revised rotation or onboarding a new attending who needs to understand what the program expects. Lives in the rotation handbook.",
    prompt="""Generate a rotation expectations document for [rotation name], [N] weeks in duration, for [PGY level] residents.

Structure:

1. **Rotation overview** (2-3 sentences): the rotation's place in the curriculum, what it builds on, what it builds toward.
2. **Learning objectives** (5-8): milestone-aligned where possible, written in 'will be able to' language with measurable verbs.
3. **Daily responsibilities**: a typical day's required activities (sign-out, case review, didactics).
4. **Weekly responsibilities**: anything that recurs less than daily (journal club, case conference, presentation).
5. **End-of-rotation requirements**: deliverables, assessments, exit interviews.
6. **Supervision model**: what level of autonomy at the start of the rotation, what level at the end, what triggers attending involvement.
7. **Evaluation criteria**: how the resident will be assessed, with the rubric or framework named.

This document should answer 'what is expected of me?' clearly enough that no resident has to guess.

Specify any institutional-specific terms (e.g., 'sign-out', 'preview') and define them on first use.""",
    output="A complete expectations doc covering all seven areas. Suitable for the rotation handbook and onboarding.",
    failures="""- Objectives that aren't actually assessable.
- Supervision model that's vague enough to be uninterpretable.
- Daily/weekly responsibilities that don't match the actual rotation flow.""",
    verification="""- Verify objectives map to actual milestones in your program's current document.
- Run by the rotation director and at least one recent rotator before finalizing.
- Confirm the supervision model is consistent with your program's policy and any institutional credentialing rules."""
)

BODIES[f"{P3}/rotations/reading-list.md"] = body(
    intent="Generate a curated rotation reading list with a one-sentence rationale per item explaining why each reading is on the list.",
    when="When the existing reading list is stale, when you're building a new rotation, or when residents tell you the current list is too long.",
    prompt="""Generate a curated reading list for [rotation name] for [PGY level] residents on a [N]-week rotation.

The list should be:

- **8-15 items.** Resist the urge to include everything; readability and use matter more than comprehensiveness.
- **Grouped by week or by topic** so residents know what to read when.
- **Prioritized**: mark each as Required, Strongly Recommended, or Optional Deep Dive.

For each item:

1. Full citation.
2. **One-sentence rationale**: why this is on the list. What gap does it fill?
3. Approximate reading time.
4. **One question** the resident should be able to answer after reading.

Include a mix of:
- 1-2 foundational textbook chapters.
- 2-3 high-yield review articles (recent).
- 1-2 landmark papers (older, still cited).
- 1-2 current guidelines.
- 1 piece of historical context (an older paper that explains why the field thinks the way it does).

At the end, name the 2 items the resident should read in the first 48 hours.""",
    output="A prioritized reading list with rationale, time estimate, and check-question for each item.",
    failures="""- List is too long; nobody reads it all.
- 'Foundational' chapters are out of date.
- Citations are inaccurate or missing.""",
    verification="""- Verify every citation. Models routinely hallucinate paper titles and authors.
- Check that landmark papers are still considered foundational in current practice.
- Have an attending in the subspecialty review and prune."""
)

BODIES[f"{P3}/rotations/daily-schedule.md"] = body(
    intent="Generate a daily schedule template for a rotation, with placeholders for sign-out, didactics, case review, and protected reading time.",
    when="When you're standardizing a rotation's day or when residents complain the day feels chaotic. The template doesn't constrain — it gives a default that everyone can plan around.",
    prompt="""Generate a typical-day schedule template for [rotation name], [PGY level] resident.

Format as a timed schedule from arrival to departure, with each block including:

- Time range.
- Activity name.
- Who leads (resident, attending, fellow, tech, group).
- Brief note on what happens in the block.

Required blocks:
- Arrival / chart review or prep.
- Sign-out (morning or end-of-day per service convention — specify).
- Didactics or conferences (state which days these occur).
- Case review or workup blocks.
- **Protected reading time** (this is the block residents say is most often eroded — protect it explicitly).
- Lunch.
- End-of-day wrap-up.

Notes section after the schedule:
- Days when this template doesn't apply (call days, conference days, etc.).
- Common ways the schedule slips and what to do about each.
- Who to tell if you're going to be off the schedule (e.g., late, leaving early).""",
    output="A timed template with all required blocks, plus notes on exceptions and slip handling.",
    failures="""- Protected reading time is in the schedule but functionally unprotected.
- No accommodation for clinical workload variability.
- Schedule assumes residents start at 7 am if you don't specify.""",
    verification="""- Validate against actual recent rotators — does the template match their real days?
- Confirm with attendings that they expect residents to be available during the blocks the schedule suggests."""
)

BODIES[f"{P3}/rotations/evaluation-rubric.md"] = body(
    intent="Generate a rotation evaluation rubric with milestone-aligned dimensions and behavioral anchors for each level.",
    when="When the existing evaluation form is generic or when you're piloting milestone-anchored evaluations. Should be reviewed by the CCC before use.",
    prompt="""Generate an end-of-rotation evaluation rubric for [rotation name], [PGY level] residents.

The rubric should:

1. Have **5-7 dimensions** mapped to milestone sub-competencies that this rotation is positioned to assess.
2. For each dimension, **5 levels** with behavioral anchors (e.g., level 3 = 'Independently formulates a workup plan for routine cases and seeks supervision appropriately for complex ones').
3. Include both **knowledge/technical dimensions** and **professional/interpersonal dimensions**.
4. Have a **narrative comment field** for each dimension with prompting questions to help raters write meaningful narratives.

Avoid:
- Anchors that describe attitudes ('shows enthusiasm') rather than behaviors.
- Anchors that are mostly about effort ('tries hard') rather than performance.
- A 'meets expectations' middle that nobody can disagree with.

End with:
- Estimated time for an attending to complete the rubric (target: 15 minutes).
- The minimum number of observations required to assign each dimension fairly.""",
    output="A rubric with 5-7 dimensions, 5 leveled behavioral anchors per dimension, narrative prompts, plus time and observation guidance.",
    failures="""- Anchors that all sound positive (no real differentiation between levels 3-5).
- Dimensions overlap and rate the same behavior twice.
- Behavioral anchors aren't actually behaviors.""",
    verification="""- Run the rubric by your CCC chair before use.
- Pilot with two raters scoring the same resident independently. If inter-rater reliability is low, the anchors need refinement.
- Verify milestone mapping against your program's current document."""
)

BODIES[f"{P3}/rotations/mid-rotation-feedback.md"] = body(
    intent="Generate a mid-rotation feedback template that surfaces course-correction opportunities before the end-of-rotation evaluation locks in.",
    when="At the midpoint of any rotation, especially for rotations longer than 2 weeks where there's time to course-correct.",
    prompt="""Generate a mid-rotation feedback template for [rotation name], to be used at the midpoint of the rotation.

The template should structure a 10-15 minute conversation, not a written-only evaluation. Format:

1. **For the resident to think about before the meeting** (3-4 reflective questions): how the rotation is going from their perspective, what they need more or less of, what's surprised them.
2. **For the attending to think about before the meeting** (3-4 observation prompts): specific strengths observed, specific opportunities for growth observed, anything the resident might not know about themselves.
3. **Conversation structure for the meeting** (5 blocks):
   - Resident shares first (2 min).
   - Attending shares (3-4 min).
   - Joint identification of one strength to lean into (2 min).
   - Joint identification of one specific growth area for the second half of the rotation (2 min).
   - Agreement on one observable change by the end of the rotation (2 min).
4. **What gets documented**: just the one strength, one growth area, one commitment. No surprises at the end-of-rotation evaluation.

Tone: collaborative, low-stakes, course-correction oriented.""",
    output="A structured template with prep questions, conversation flow, and minimal documentation requirements.",
    failures="""- Template is too long; meeting overruns and feels like an evaluation.
- Resident reflection prompts are generic.
- Documentation requirements turn a course-correction meeting into a paper exercise.""",
    verification="""- Pilot with a willing attending-resident pair. Time the meeting; adjust if it consistently runs long.
- Check that the documented commitment is observable enough to assess at end-of-rotation."""
)

BODIES[f"{P3}/rotations/end-of-rotation-evaluation.md"] = body(
    intent="Generate an end-of-rotation evaluation form aligned to milestones, with both numeric and narrative sections.",
    when="When you're updating an evaluation form or when residents and attendings both complain the current form doesn't capture what matters.",
    prompt="""Generate an end-of-rotation evaluation form for [rotation name], [PGY level], using the evaluation rubric I've provided (or a new one if I haven't).

The form should include:

1. **Header**: resident name, rotation name, dates, supervising attending(s), number of weeks evaluated.
2. **Numeric ratings**: each dimension from the rubric, rated 1-5 with the anchor text visible.
3. **Narrative comment for each dimension**: prompted with a specific question ('Describe a specific instance where you observed this resident at this level').
4. **Overall narrative**: 1-2 paragraph free text covering the resident's trajectory, strengths, and growth opportunities.
5. **Specific commitment for next rotation**: 1-2 behavioral targets the resident should focus on.
6. **Quality of evaluation gates**: a question to the evaluator about whether they had sufficient observation to evaluate this resident (mitigates the 'I'll just give 4s' default).
7. **Resident sign-off**: a box for the resident to acknowledge they received and discussed the evaluation.

Make the form completable in 20-30 minutes by an attending who knows the resident well.""",
    output="A complete evaluation form ready for use, with numeric and narrative sections and sufficient observation gating.",
    failures="""- Narratives become 'no comments' because the prompts are weak.
- Numeric ratings default to all-fours because the anchors don't distinguish levels.
- The form takes so long that attendings rush it.""",
    verification="""- Pilot with one attending on one resident; iterate the form based on what they say is hard.
- Verify milestone alignment.
- Check that the form complies with any institutional or ACGME documentation requirements."""
)

BODIES[f"{P3}/rotations/resident-to-resident-handoff.md"] = body(
    intent="Generate a resident-to-resident handoff document covering what the incoming resident needs to know in their first week.",
    when="Last day of the rotation, when the outgoing resident has the most context and the lowest motivation to write it down. The template lowers the activation energy.",
    prompt="""Generate a peer-to-peer rotation handoff template for [rotation name]. Audience: the next resident starting this rotation.

The template structures the outgoing resident's tacit knowledge into usable form. Sections:

1. **Welcome and orientation moment**: a 2-3 sentence note from the outgoing resident on what to know on day 1.
2. **What the syllabus doesn't tell you**: 3-5 practical tips that aren't in the formal documents (where to find the on-service charger, who actually approves sign-out late, which attending wants what kind of preview).
3. **Three attendings I worked with the most**: name and a sentence on what each cares about most (e.g., 'Dr. X wants the smear scanned before sign-out, period').
4. **The single most useful resource I found**: the article, textbook, app, or website that made the rotation easier.
5. **The mistake I made early and what I'd do differently**: vulnerable but useful.
6. **The case or moment I learned the most from**: brief, anonymized.
7. **Open offer**: 'I'm happy to answer questions by [contact method] for the first week if you have them'.

Tone: peer-to-peer, slightly informal, honest. This is NOT a formal evaluation document — it's collegial advice.""",
    output="A template the outgoing resident can complete in 20 minutes that gives the incoming resident a week's head start.",
    failures="""- Becomes too formal; outgoing residents don't write candidly.
- Identifies cases with potential to identify patients.
- 'Three attendings' notes are too candid and reflect badly on the attending.""",
    verification="""- Strip patient identifiers from any cases described.
- Be diplomatic about attendings; aim for accurate without being unkind.
- The 'mistake' should be one the outgoing resident is comfortable putting in writing."""
)

# ---- Courses (5) ----

BODIES[f"{P3}/courses/syllabus.md"] = body(
    intent="Generate a course syllabus with weekly topics, learning objectives, assessment plan, and policy language.",
    when="When you're designing a new longitudinal course (residency didactic series, fellowship curriculum, elective course) and need a starting structure.",
    prompt="""Generate a course syllabus for [course name], [N] weeks in length, for [audience].

The syllabus should include:

1. **Course title, instructor(s), meeting time and location.**
2. **Course description** (3-5 sentences): scope, prerequisites if any, where this course fits in the larger curriculum.
3. **Learning objectives** (4-7): course-level objectives in 'will be able to' language.
4. **Weekly schedule**: each week with topic, readings, in-class activity, post-class assignment if any. Be specific.
5. **Assessment plan**: how learners are evaluated (formative and summative components, weighting if graded).
6. **Required and recommended resources** with full citations.
7. **Policies**: attendance, makeup work, accommodations, AI use, academic integrity. Address each explicitly.
8. **Communication norms**: how to contact instructors, expected response times.

For each weekly topic, name **one outcome** the learner should be able to demonstrate after that week.

Match the level of formality your institution expects (CME-accredited course = more formal; residency didactic series = less).""",
    output="A complete syllabus organized by section. Length: 5-8 pages. Should pass review by the relevant curriculum committee.",
    failures="""- Weekly topics that aren't actually achievable in one session.
- AI use policy that's either absent or boilerplate; both are problematic.
- Assessment plan that doesn't align with the stated objectives.""",
    verification="""- Verify required resources are in print and accessible.
- Check institutional policies on AI use and assessment — your statement should match.
- Run the weekly schedule by anyone who taught the course previously."""
)

BODIES[f"{P3}/courses/weekly-module-packet.md"] = body(
    intent="Generate a weekly module learning packet with required reading, pre-class question prompts, in-class activities, and post-class assessment.",
    when="One week before each module is delivered. The packet is what gets sent to learners + the instructor's preparation guide in one.",
    prompt="""Generate a learning packet for Week [N] of [course name]. Topic: [topic]. Time: [duration of the in-class session].

The packet has two audiences:

**For the learners** (1-2 pages):
- Week topic and learning outcome (the one thing they should be able to do after this week).
- Required reading (1-3 items with full citations and a 1-sentence reading guide).
- 3 pre-class reflection questions to think about while reading.
- Pre-class assignment if any (brief, not a paper).

**For the instructor** (2-3 pages):
- Topic overview and where this week fits in the course arc.
- Suggested in-class agenda with timing.
- Active learning activities (1-2) with materials list.
- Discussion questions for the in-class session (5-7).
- Anticipated misconceptions and how to address them.
- Post-class assessment items (3-5 questions for an online quiz or written response).
- Recommended further reading for learners who want to go deeper.

Be specific about what learners produce. 'Discuss' is not enough — what's the artifact?""",
    output="A two-audience packet: learner-facing (concise) and instructor-facing (detailed enough to teach the week without further prep).",
    failures="""- Learner section is too long; learners skim or skip.
- Instructor section doesn't actually help an instructor who hasn't taught the topic before.
- Pre-class questions are surface-level recall.""",
    verification="""- Verify reading citations and confirm availability through your institution's library.
- Run the instructor section by a colleague who hasn't taught the week — would they be ready?
- Check that the post-class assessment aligns to the stated learning outcome."""
)

BODIES[f"{P3}/courses/assignment-grading-rubric.md"] = body(
    intent="Generate a rubric for a specific assignment with dimensions, level descriptors, and a scoring guide.",
    when="When you're assigning anything more substantive than a quiz and want consistent grading.",
    prompt="""Generate a grading rubric for the following assignment:

- **Assignment**: [name and brief description]
- **Course**: [course name and audience]
- **Length / format expected**: [pages, slides, video minutes, etc.]
- **Learning objectives this assignment assesses**: [from the syllabus]
- **Point total**: [if graded numerically]

The rubric should have:

1. **4-6 dimensions** that together capture what 'good' looks like for this assignment. Each dimension should be **independently assessable** (don't combine content quality and writing into one row).
2. **4 levels** per dimension: Exemplary, Proficient, Developing, Needs Substantial Work. Each level with a behavioral or product descriptor (what would I observe in the artifact?).
3. **Point values** per dimension (if numeric grading) — weight dimensions according to how much they matter for the objectives.
4. **Feedback prompts** for each dimension to help graders write specific narrative feedback ('Cite one moment where the student demonstrated X').

End with:
- **Common pitfalls** for this assignment type (what students typically get wrong) and how the rubric captures them.
- **Estimated grading time** per submission.""",
    output="A rubric with 4-6 well-defined dimensions, 4 levels each, feedback prompts, pitfalls, and time estimate.",
    failures="""- Level descriptors all sound positive — no real differentiation.
- Dimensions overlap and double-count.
- Numeric weighting doesn't reflect what actually matters.""",
    verification="""- Grade one sample submission with the rubric, then have a colleague grade the same one independently. Check for inter-rater agreement; refine where you disagree.
- Verify the rubric assesses the stated learning objectives."""
)

BODIES[f"{P3}/courses/feedback-collection-form.md"] = body(
    intent="Generate a course feedback form with quantitative and qualitative items balanced for completion rate and signal quality.",
    when="At the end of a course block (mid-course and end-of-course), when you want actionable feedback rather than vague satisfaction scores.",
    prompt="""Generate a course feedback form for [course name]. Audience: [learners — number, level].

The form should:

1. Take **under 5 minutes** to complete. Hard cap.
2. Mix structured (numeric/Likert) and unstructured (free text) items, but bias toward structured to keep completion high.
3. Yield **actionable** results — every item should map to a decision I could make for the next iteration.

Sections:

1. **Course-level Likerts** (3-4 items): pacing, difficulty, value relative to time invested.
2. **Module-level rapid rating** (1 item per module): grade each module on usefulness 1-5.
3. **Open free text** (2 items only):
   - 'One thing that should change about this course before next iteration.'
   - 'One thing that should NOT change.'
4. **Demographics** (2-3 items, all optional): role, prior experience with the topic, anything you actually need for stratifying results.
5. **Optional self-report on learning** (1 item): how much they think they learned, with a calibration note ('We'll compare this to pre/post assessment results').

For each item, include the question, the response format, and a one-sentence rationale ('I'll use this to decide whether to drop Module X next year').""",
    output="A 5-minute form with item-by-item rationale. Should produce data you can actually act on.",
    failures="""- Form is too long; completion rate drops below 50% and you have selection bias.
- Free text questions are too open; results are unanalyzable.
- 'How satisfied were you' generic items that don't inform any decision.""",
    verification="""- Pilot with 2-3 learners and time them.
- Confirm each item maps to a specific decision.
- Plan how you'll analyze free text responses before sending the survey — otherwise the data won't get used."""
)

BODIES[f"{P3}/courses/course-postmortem.md"] = body(
    intent="Generate a course post-mortem template covering what worked, what didn't, what changed mid-course, and what to do differently next time.",
    when="Within 2-4 weeks of course completion, when feedback is in but instructors still remember the course. Don't postpone — institutional memory decays fast.",
    prompt="""Generate a post-mortem template for [course name], [course duration] in [term/year], taught by [instructors].

The template should structure a 45-60 minute meeting AND produce a documented artifact for the curriculum file. Sections:

1. **Pre-meeting work** for each instructor (10 min each):
   - Review feedback data.
   - Note 2-3 things that worked.
   - Note 2-3 things that didn't.
   - Note any change made mid-course and how it landed.

2. **Meeting structure** (45-60 min):
   - Quick round: each instructor's top 'worked' and top 'didn't work' (10 min).
   - Discussion of patterns: what came up multiple times? (15 min).
   - Mid-course changes review: keep, revert, or refine? (10 min).
   - Decisions for next iteration: 3-5 specific changes, ranked by ease × impact (15 min).
   - Documentation owner and timeline (5 min).

3. **Artifact to produce after the meeting**:
   - Summary of what worked and what didn't (3-4 bullets each).
   - Mid-course changes log (kept, reverted, or refined).
   - Action list for next iteration (specific, owned, dated).
   - Any structural issues to escalate to the curriculum committee.

Tone: honest, learning-oriented, no defensiveness.""",
    output="A meeting structure + an artifact template. Lightweight enough to actually happen.",
    failures="""- Meeting runs over and becomes a venting session rather than a decision-making one.
- Action list is aspirational rather than specific.
- No assigned owner means changes don't get made.""",
    verification="""- Each action item should have a named owner and a date.
- The artifact should be reviewable by anyone who didn't attend the meeting.
- Schedule the meeting before the course ends; don't wait until 'when there's time'."""
)

# ---- Conferences & Journal Clubs (5) ----

BODIES[f"{P3}/conferences-and-journal-clubs/journal-club-packet.md"] = body(
    intent="Generate a journal club packet with paper summary, background context, key results, methodologic critique, and discussion questions.",
    when="One week before journal club, when you're the lead and want to send pre-reading to attendees that ensures real discussion.",
    prompt="""Generate a journal club packet for the following paper:

- **Paper**: [full citation]
- **Audience**: [PGY level, mix of residents and faculty]
- **Discussion format**: [traditional, debate, structured critique, etc.]

The packet should include:

1. **One-paragraph background**: the state of the field before this paper. What question made this paper worth doing?
2. **The study summary**: design, population, key results with numbers. Neutral framing, not yet interpretive.
3. **Methodologic critique** (using the appropriate reporting guideline framework — see the [Paper methods critique prompt](library.html#/library/pillar-1-self-education/prompts/paper-methods-critique)):
   - 2 specific strengths of the methods.
   - 2-3 specific limitations.
4. **The 'so what'**: what could this paper change about practice? What barriers exist to that change?
5. **5 discussion questions** ordered from concrete to contested:
   - Methods or numbers question.
   - Generalizability question.
   - Comparison-to-prior-literature question.
   - Practice-change question.
   - A genuinely contested question.
6. **Attendee preparation note**: what they should think about before arriving.

Length: 2-3 pages. No PHI.""",
    output="A complete packet ready to send to attendees a week before journal club.",
    failures="""- Critique is generic.
- Discussion questions are leading rather than open.
- Background context misses the paper's intellectual lineage.""",
    verification="""- Verify all numbers against the actual paper.
- Pre-test the contested question with a colleague.
- Confirm citations are accurate."""
)

BODIES[f"{P3}/conferences-and-journal-clubs/tumor-board-case-packet.md"] = body(
    intent="Generate a tumor board case packet with history, imaging summary, pathology findings, treatment options, and discussion questions.",
    when="When you're preparing cases for an upcoming tumor board. The packet structure ensures the cases get presented consistently.",
    prompt="""Generate a tumor board case packet template for [tumor board name — e.g., 'GU multidisciplinary tumor board']. The template should support presentation of [N] cases per session.

For each case in the packet:

1. **De-identified header**: case number, demographic envelope (age range, sex if relevant to pathology), referring specialty, date case was discussed.
2. **Brief clinical history** (2-3 sentences): presentation, key comorbidities, prior workup. No PHI.
3. **Imaging summary**: modality, key findings, formal radiology read summary.
4. **Pathology summary**: gross findings, microscopic findings, IHC results, molecular results. Organized by what's diagnostically discriminating.
5. **Current diagnosis and stage** (if applicable).
6. **The question for the board**: explicit, single decision being asked of the multidisciplinary group.
7. **Treatment options under consideration**: 2-3 alternatives with rationale for each.
8. **Anticipated discussion points**: 2-3 things you expect the board to weigh in on.
9. **Outcome decision** (filled in after the discussion).

Plus a packet header with date, attendees, and any standing references (e.g., institutional treatment protocols).

The packet should be PHI-free and suitable for retention as part of the case file.""",
    output="A template for the packet header + a per-case template. Together they support consistent case presentation.",
    failures="""- Templates that allow PHI to creep in.
- The 'question for the board' is unclear, leading to unfocused discussion.
- No outcome field — board decisions don't get documented.""",
    verification="""- **Verify no PHI** in any case packet before circulating.
- Confirm the 'outcome decision' field is filled in for every case (administrative discipline matters).
- Match the packet format to institutional retention requirements."""
)

BODIES[f"{P3}/conferences-and-journal-clubs/grand-rounds-speaker-prep.md"] = body(
    intent="Generate a grand rounds speaker prep document with audience profile, expected questions, recommended visuals, and timing breakdown.",
    when="2-3 weeks before grand rounds, when you've accepted the invitation and need to start preparing. Skips the 'where do I even start' phase.",
    prompt="""I'm giving grand rounds on [topic] at [institution] on [date]. The talk is [duration] minutes plus Q&A. The audience is [mix — usually attendings, fellows, residents, sometimes med students or outside guests].

Help me prepare. Generate:

1. **Audience profile**: who's likely in the room, what they know about the topic coming in, what they want to walk away with.
2. **Talk structure** (high-level): opening hook (which approach — a case? a statistic? a contrarian framing?), 3-4 content beats, synthesis. Estimated timing for each.
3. **Recommended visuals**: 2-3 specific visuals that will land in this audience (a graph, a side-by-side comparison, a clinical photo) — describe what each would show.
4. **5 questions** I should be ready for:
   - 2 from a content expert (the attending in the audience who knows the topic best).
   - 2 from a generalist (the medical director or chief who wants the high-level take).
   - 1 from a trainee (the resident who wants the practical takeaway).
5. **What to NOT do**: 2-3 framings, opening lines, or rhetorical moves that will misfire with this audience at this institution.
6. **A 'walking away' line**: the one sentence the audience should remember 24 hours later.""",
    output="A prep document I can use to structure my preparation, not a script. Includes audience-specific Q&A prep.",
    failures="""- 'Audience profile' is generic.
- 'What not to do' is empty or platitudinous.
- The walking-away line is too long or too vague.""",
    verification="""- Run the audience profile by a colleague at the host institution if you can — they'll know specifics you don't.
- The walking-away line should be testable: would the audience be able to repeat it tomorrow?"""
)

BODIES[f"{P3}/conferences-and-journal-clubs/conference-schedule.md"] = body(
    intent="Generate a quarterly or annual conference schedule with topic rotation across subspecialties and assigned presenters.",
    when="Annually when you're planning the conference series for the academic year, or quarterly for shorter cycles.",
    prompt="""Generate a [quarterly / annual] conference schedule for [conference series name — e.g., 'Tuesday morning CP didactics']. Audience: [target audience and level].

Constraints:
- **Frequency**: [weekly / biweekly]
- **Number of sessions to fill**: [N]
- **Available presenters**: [list of presenters with their subspecialties and rotation availability]
- **Required topic coverage**: [subspecialties or specific topics that must be covered, e.g., RISE prep blocks]
- **Standing items**: [recurring slots — journal club every Nth week, in-service review, etc.]

Produce:

1. A full schedule with date, topic, presenter, and any pre-reading.
2. **Balance check**: distribution of topics across subspecialties. If some subspecialties are over- or under-represented, flag it and suggest adjustments.
3. **Presenter load check**: distribution of sessions per presenter. Avoid overloading any one person.
4. **Buffer sessions**: 1-2 unscheduled or flexible sessions per quarter to accommodate guest speakers, schedule slips, or topic substitutions.
5. **Logistics**: room, AV needs, recording status, attendance tracking.

End with: a draft email template I can use to invite each presenter with their assigned date and topic.""",
    output="A schedule + balance and load checks + buffer sessions + logistics + invitation template.",
    failures="""- Schedule is balanced on paper but a single presenter has 3 sessions in a row.
- No buffer sessions, so any schedule change cascades.
- 'Required coverage' items get scheduled but in suboptimal weeks (e.g., RISE prep after the exam).""",
    verification="""- Verify each presenter's availability before publishing.
- Confirm room and AV bookings.
- Validate the topic order against any sequencing constraints (e.g., a topic that's a prerequisite for another)."""
)

BODIES[f"{P3}/conferences-and-journal-clubs/qa-prep-doc.md"] = body(
    intent="Generate a Q&A preparation document anticipating audience questions and providing concise, evidence-backed responses.",
    when="The day before any presentation where the Q&A is high-stakes — board meeting, departmental presentation, conference talk, grant defense.",
    prompt="""Help me prepare for the Q&A portion of [presentation title], on [date]. The audience is [audience description].

Generate a Q&A prep document organized as:

1. **The 5-10 questions most likely to come up**, ranked by likelihood. For each:
   - The question (phrased as I'd actually hear it).
   - The questioner's likely angle (technical objection, clinical concern, scope question, etc.).
   - A 2-3 sentence response, evidence-backed.
   - The follow-up question I should anticipate.
   - Any pre-prepared data, citation, or slide I should have ready.

2. **The 2 hardest questions**: the ones I'd dread getting. Spend more time on these. Acknowledge if I genuinely don't have a good answer; suggest how to respond honestly while preserving credibility.

3. **The 1 question I cannot answer**: if there's a question with no good answer (e.g., results not yet available), draft a response that doesn't dodge but acknowledges the gap.

4. **Time management**: how long to spend per answer to leave time for multiple questions. What to do if Q&A runs short or long.

5. **Body and voice**: where to look, how to handle hostile questioners, how to redirect off-topic questions.

End with: the one question I should hope someone asks, because it lets me make my strongest point.""",
    output="A prep document I can study the night before. Length: 3-5 pages. Should reduce surprise during actual Q&A.",
    failures="""- The 'hardest questions' are softball.
- 'I cannot answer' responses dodge rather than acknowledge.
- Time management guidance is generic.""",
    verification="""- Have a colleague pose the anticipated questions to you and rate your responses. The questions you flail on need more prep.
- Verify any data, citations, or numbers you plan to reference.
- The 'one question I hope someone asks' should actually be a question someone might ask, not a planted one that would be obvious."""
)

# ---------------------------------------------------------------------------
# Apply: read each stub file, preserve frontmatter, replace body
# ---------------------------------------------------------------------------

def apply_body(path, new_body):
    p = Path(path)
    if not p.exists():
        print(f"MISSING: {path}")
        return False
    text = p.read_text()
    # Split on the second '---' delimiter (end of frontmatter)
    if not text.startswith("---"):
        print(f"NO FRONTMATTER: {path}")
        return False
    # Find the end of the frontmatter block
    end = text.find("\n---", 4)
    if end < 0:
        print(f"BAD FRONTMATTER: {path}")
        return False
    frontmatter = text[: end + 4]
    p.write_text(frontmatter + "\n\n" + new_body)
    return True

count = 0
missing = 0
for path, content in BODIES.items():
    if apply_body(path, content):
        count += 1
    else:
        missing += 1

print(f"Populated {count} prompt bodies. Missing: {missing}.")
