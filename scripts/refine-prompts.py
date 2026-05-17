#!/usr/bin/env python3
"""
Refines the 61 prompt files:
1. Adds a `best_model` field to each frontmatter (with brief rationale in body).
2. Appends one concrete refinement to each prompt's code block — a guard,
   constraint, or sharpening that addresses an observed failure mode.
3. Adds a "## Best model and why" section to the body.

Run:
  python3 scripts/refine-prompts.py
"""

import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Per-prompt refinements: (slug-path, refinement-line-appended-to-prompt-code)
# ---------------------------------------------------------------------------

REFINEMENTS = {
    # Pillar 1 — Self-Education
    "library/pillar-1-self-education/prompts/concept-explanation-at-level.md":
        "If any claim in any layer references a specific cutoff, drug name, gene, dose, or guideline year, source it explicitly (e.g., '2024 NCCN, version 2'). If you can't source a specific number, mark it [VERIFY] rather than stating it as fact.",
    "library/pillar-1-self-education/prompts/compare-contrast.md":
        "If a discriminating feature depends on a specific classification version (e.g., WHO 5th edition vs. ICC 2022), state which version you're using. Discrimination rules drift between editions.",
    "library/pillar-1-self-education/prompts/guideline-plain-language.md":
        "Preserve every qualifier in the original guideline ('in selected patients', 'when available', 'if feasible'). Do not collapse conditional language into directives.",
    "library/pillar-1-self-education/prompts/lis-informatics-review.md":
        "Cite the specific standard (HL7 segment name, LOINC code, FHIR resource, IHE profile) where applicable rather than paraphrasing it. If you're unsure whether a term is current vocabulary in this domain, say so.",
    "library/pillar-1-self-education/prompts/self-quiz-one-at-a-time.md":
        "If I correct you on a fact during the drill, stop and acknowledge the correction explicitly before moving on. Do not continue as if it didn't happen.",
    "library/pillar-1-self-education/prompts/mcq-generation-with-rationales.md":
        "Do NOT reproduce or closely paraphrase real published board questions (RISE, ABPath in-service, etc.). Generate original questions only. If the topic is so narrow that you cannot safely generate originals without overlapping existing questions, tell me.",
    "library/pillar-1-self-education/prompts/anki-flashcards.md":
        "Mark any answer where you are uncertain about a specific value, gene name, or threshold with `[VERIFY]` at the end. Better to flag uncertainty than ship a wrong card into spaced repetition.",
    "library/pillar-1-self-education/prompts/board-prep-schedule.md":
        "If my self-assessment looks internally inconsistent (e.g., I list a topic as 'Strong' but also list it as something I want extra time on), ask me to clarify before generating the schedule.",
    "library/pillar-1-self-education/prompts/question-bank-gap-analysis.md":
        "Distinguish between a genuine concept gap (I don't understand the underlying mechanism) and a recall failure (I knew the fact but couldn't retrieve it under time pressure). The interventions for each are different — say which one each cluster is.",
    "library/pillar-1-self-education/prompts/diagnostic-algorithm-walkthrough.md":
        "State which version of the algorithm you're walking through (year, society, edition). If the algorithm has been substantially revised in the last 5 years, note both the version you're describing and what changed.",
    "library/pillar-1-self-education/prompts/reverse-case-drill.md":
        "Critical reminder: the findings I paste must be **de-identified** with NO patient identifiers — no name, MRN, accession number, exact date of service, exact age, institutional identifiers, or rare-finding combinations sufficient for re-identification. If you see anything that looks identifiable in what I paste, stop and tell me before proceeding.",
    "library/pillar-1-self-education/prompts/forward-case-drill.md":
        "Be strict about the 'pathognomonic' label. A finding is only pathognomonic if it is unique to this diagnosis. If a finding appears in >1 diagnosis, it's at most 'highly supportive'. Over-labeling pathognomonic findings is the most common error in this kind of teaching summary.",
    "library/pillar-1-self-education/prompts/negative-drill.md":
        "Rank disconfirming findings by clinical likelihood, not by exoticism. The most likely way I'm wrong is usually a common condition presenting atypically, not a rare zebra. Surface the boring alternatives, not just the interesting ones.",
    "library/pillar-1-self-education/prompts/paper-summarization.md":
        "If you do not have direct access to the actual paper text (not just the title or abstract), say so explicitly at the top and refuse to summarize. Hallucinated paper summaries are the most common failure mode for this prompt and the most damaging — never bluff.",
    "library/pillar-1-self-education/prompts/paper-methods-critique.md":
        "If your critique relies on conventions you're not sure are current (e.g., 'this should follow CONSORT 2010 vs. the 2025 extension'), state your uncertainty about the convention version. Methodology guidelines update; don't critique against an outdated framework.",
    "library/pillar-1-self-education/prompts/journal-club-preread.md":
        "If you don't have the full paper text, say so and refuse to fabricate specific results, sample sizes, p-values, or quotes. A pre-read with invented numbers is worse than no pre-read.",
    "library/pillar-1-self-education/prompts/multimodal-photomicrograph.md":
        "STOP before responding: confirm the image is a published teaching case or public-domain image, NOT real patient material. If I haven't stated the source, ask. Multimodal AI is improving but still confidently wrong on subtle morphology — describe what's actually visible at the magnification, do not invent features you can't see.",
    "library/pillar-1-self-education/prompts/multimodal-spep-ife.md":
        "STOP before responding: confirm the trace is from a published teaching case or public-domain source, NOT institutional patient material. If unclear, ask. Describe only features visible in the trace; do not invent peaks or fractions you can't actually see.",

    # Pillar 2 — Teaching
    "library/pillar-2-teaching/prompts/acgme-epa-objectives.md":
        "Verify the milestone codes against the current Pathology Milestone document (ACGME publishes revisions periodically). If you're not sure which version is current, ask me to provide the milestone document or note which version you're referencing.",
    "library/pillar-2-teaching/prompts/blooms-mcq.md":
        "After each MCQ, justify the Bloom's level by naming the specific cognitive task required to reach the answer. If a question can be answered by retrieving a memorized fact alone — regardless of how clinical-looking the vignette is — it's Remember/Recall, not Application.",
    "library/pillar-2-teaching/prompts/case-vignette-pgy.md":
        "Vary patient demographics across cases. Do not default to middle-aged white male unless I specify. The demographic should reflect the actual epidemiology of the condition, not the textbook archetype.",
    "library/pillar-2-teaching/prompts/matched-case-pair.md":
        "Before writing, confirm with me what specific discriminating feature should resolve the pair. Do not assume — ask one clarifying question if it's not obvious from my framing.",
    "library/pillar-2-teaching/prompts/osce-station.md":
        "The patient/clinician script should handle the 3-4 most likely examinee openers. If I don't tell you what those openers are, ask before drafting the script.",
    "library/pillar-2-teaching/prompts/slide-outline-1hr.md":
        "After the outline, sum the suggested timing for each block and confirm it fits 60 minutes including the Q&A. If the total exceeds 60 min, name which blocks I should compress and by how much.",
    "library/pillar-2-teaching/prompts/speaker-notes.md":
        "Notes should be in spoken voice. If a sentence reads like written prose ('It is important to recognize that...'), rewrite it for the ear ('Here's what to notice...'). Aloud-test as you write.",
    "library/pillar-2-teaching/prompts/visual-metaphor.md":
        "Be honest about precision: do not inflate precision scores. A metaphor that breaks down when pushed against an expert deserves a precision of 2, not 4. The trade-off is the point.",
    "library/pillar-2-teaching/prompts/audience-polls.md":
        "Avoid polls where the correct answer is obvious to anyone awake. The polling moment fails — and engagement craters — if everyone gets it right immediately. The 'wrong' answer must be plausibly attractive.",
    "library/pillar-2-teaching/prompts/video-script.md":
        "Read the script aloud at conversational pace (~150 words/minute). If it overruns the target duration, cut narration first; do not cut visuals or beats.",
    "library/pillar-2-teaching/prompts/resident-feedback-note.md":
        "Every claim in the note must be traceable to an observation I gave you. Do not extrapolate to praise the resident didn't earn or growth areas I didn't flag. If you find yourself padding to reach the target length, leave it short.",
    "library/pillar-2-teaching/prompts/ccc-narrative-comment.md":
        "Do NOT inflate the level beyond the evidence I provided. If you notice my evidence does not actually support my assigned level, stop and tell me before drafting. An inflated CCC narrative is worse than no narrative.",
    "library/pillar-2-teaching/prompts/lor-starting-draft.md":
        "Critical change to the flow: before drafting ANY of the letter body, ask me for at least 4 SPECIFIC anecdotes about this applicant — moments I observed, with enough detail that a reader would know this person could only have come from my pen. Do NOT begin the body paragraphs until you have those anecdotes. Generic LOR prose without specific anecdotes is the most common failure mode and the easiest one to detect from the reader's side.",
    "library/pillar-2-teaching/prompts/journal-club-discussion-q.md":
        "Pressure-test question 5 (the contested one): if it has a clear answer in current literature, it's not actually contested. Replace it with one that reasonable experts genuinely disagree about.",
    "library/pillar-2-teaching/prompts/tumor-board-presentation.md":
        "Strip ALL patient identifiers before pasting: no name, no MRN, no accession number, no exact age, no exact date of service, no institutional identifiers. If I paste something that looks identifiable, stop and tell me before generating the outline.",
    "library/pillar-2-teaching/prompts/resident-as-teacher.md":
        "Pressure-test the 'ONE concept': can a learner reasonably restate it in 30 seconds at the end of the session? If not, it's too broad — narrow it before continuing.",

    # Pillar 3 — Operations (Workshops)
    "library/pillar-3-educational-operations/prompts/workshops/announcement-registration.md":
        "Avoid empty intensifiers ('cutting-edge', 'revolutionary', 'transformative'). If you use one, replace it with a specific concrete outcome attendees will achieve.",
    "library/pillar-3-educational-operations/prompts/workshops/pre-workshop-survey.md":
        "After generating the survey, estimate the actual completion time at a normal reading pace. If it exceeds 3 minutes, cut a question. Optimize for response rate.",
    "library/pillar-3-educational-operations/prompts/workshops/facilitator-runofshow.md":
        "Build in 5-minute buffers between blocks. Real workshops always run long; the run-of-show should plan for this rather than assume perfect timing.",
    "library/pillar-3-educational-operations/prompts/workshops/station-by-station-guide.md":
        "Each station's minute-by-minute should account for ~90% of the time allocation, leaving 10% as buffer for transitions and unexpected questions. Stations packed to 100% run over.",
    "library/pillar-3-educational-operations/prompts/workshops/badge-design-spec.md":
        "Verify font size meets accessibility minimums: name in ≥24pt for in-person events (legible from across a room). If institutional branding requirements conflict with accessibility, name the conflict explicitly.",
    "library/pillar-3-educational-operations/prompts/workshops/access-card-layout.md":
        "QR code must be ≥25mm square and use error correction level H (30% recovery). Smaller codes or lower error correction levels fail when printed with imperfect ink coverage or scanned in low light.",
    "library/pillar-3-educational-operations/prompts/workshops/certificate-of-completion.md":
        "Do NOT include CME, MOC, or any continuing education credit language unless I have explicitly confirmed the workshop is accredited for that credit. False credit claims are a regulatory issue.",
    "library/pillar-3-educational-operations/prompts/workshops/post-workshop-thank-you.md":
        "If I haven't given you a specific moment from the workshop to reference, leave the placeholder `[INSERT SPECIFIC MOMENT]` rather than inventing one. A fabricated reference signals to attendees that the email is templated.",
    "library/pillar-3-educational-operations/prompts/workshops/faculty-feedback-summary.md":
        "Quote selectively but accurately. If a quote could identify the respondent (small group, distinctive phrasing), paraphrase. Do NOT embellish or smooth out quotes to make them more readable — that erodes faculty trust in the data.",

    # Pillar 3 — Operations (Rotations)
    "library/pillar-3-educational-operations/prompts/rotations/orientation-onepager.md":
        "If you can't fit something on one page, cut it. The one-page constraint is the value — it forces ruthless prioritization of what a day-1 resident actually needs.",
    "library/pillar-3-educational-operations/prompts/rotations/expectations-doc.md":
        "Map every objective to a specific milestone sub-competency code (e.g., 'PC1.3 Interpretation of Diagnostic Studies'). Generic 'will demonstrate competence in X' is not useful for the CCC.",
    "library/pillar-3-educational-operations/prompts/rotations/reading-list.md":
        "Verify EVERY citation. Models routinely generate plausible-looking but non-existent paper titles. If you cannot verify a citation, leave it out and recommend I add one I know exists.",
    "library/pillar-3-educational-operations/prompts/rotations/daily-schedule.md":
        "Protected reading time should be at least 60 contiguous minutes. If the rotation workload makes that infeasible, name the trade-off explicitly rather than silently scheduling 30-minute fragments.",
    "library/pillar-3-educational-operations/prompts/rotations/evaluation-rubric.md":
        "Behavioral anchors must describe observable behaviors, not personality traits. 'Shows enthusiasm' is not a behavior; 'arrives prepared to sign-out with a written preview of complex cases' is.",
    "library/pillar-3-educational-operations/prompts/rotations/mid-rotation-feedback.md":
        "The meeting must fit in 15 minutes maximum. If the template you generate requires longer, cut sections. Mid-rotation feedback that becomes a 30-minute conversation gets cancelled by the third occurrence.",
    "library/pillar-3-educational-operations/prompts/rotations/end-of-rotation-evaluation.md":
        "Include a 'minimum observations' gate at each dimension. An evaluator who has not observed a specific dimension should be able to mark 'unable to assess' rather than defaulting to 3/5. False data is worse than no data.",
    "library/pillar-3-educational-operations/prompts/rotations/resident-to-resident-handoff.md":
        "Strip patient identifiers from any case mentioned. Be diplomatic but honest about attendings — aim for 'Dr. X prefers a written preview before sign-out' rather than personal critique.",

    # Pillar 3 — Operations (Courses)
    "library/pillar-3-educational-operations/prompts/courses/syllabus.md":
        "Include an explicit AI use policy. The default should not be silence; it should specify which uses are encouraged (e.g., drafting, brainstorming), which require disclosure, and which are prohibited (e.g., submitting AI output as own work for graded assignments).",
    "library/pillar-3-educational-operations/prompts/courses/weekly-module-packet.md":
        "Verify every reading citation and confirm institutional library access. If you can't verify, mark with [VERIFY] rather than including unverified citations.",
    "library/pillar-3-educational-operations/prompts/courses/assignment-grading-rubric.md":
        "Each dimension must be independently assessable. If two dimensions could be confused or rated together (e.g., 'writing quality' and 'organization'), merge them or rewrite to make the distinction sharper.",
    "library/pillar-3-educational-operations/prompts/courses/feedback-collection-form.md":
        "Every item must map to a specific decision I would make based on the response. If you can't name the decision for an item, cut the item. Survey length is the enemy of response rate.",
    "library/pillar-3-educational-operations/prompts/courses/course-postmortem.md":
        "Action items must have named owners and dates. Items without an owner are aspirations, not actions. If an item has no clear owner, flag it for me to assign or cut.",

    # Pillar 3 — Operations (Conferences & journal clubs)
    "library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs/journal-club-packet.md":
        "If you don't have the full paper text, say so and refuse to generate the packet. Fabricated background, methods, or numbers in a journal club packet undermine the entire session.",
    "library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs/tumor-board-case-packet.md":
        "STRONG REMINDER: strip ALL patient identifiers from each case. No name, no MRN, no accession number, no exact age (use 'in their 60s'), no exact date of service, no institutional identifiers, no rare-disease-plus-location combinations that enable re-identification. If a case feels like it cannot be sufficiently de-identified, tell me.",
    "library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs/grand-rounds-speaker-prep.md":
        "If you don't know the host institution's culture, ASK me what would be a misfire (e.g., references to specific local politics, recent institutional events, in-jokes) before drafting 'what not to do'. Do not guess about a culture you don't know.",
    "library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs/conference-schedule.md":
        "The model can suggest a schedule but YOU must confirm each presenter's availability before publishing. Do not treat suggested presenters as confirmed.",
    "library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs/qa-prep-doc.md":
        "The 'hardest questions' should be genuinely hard, not softballs disguised as challenges. If you can answer one of your own 'hard' questions easily, escalate the difficulty. The 2 hardest questions are the most valuable part of this document.",
}

# ---------------------------------------------------------------------------
# Model recommendations: (slug-path → (model_name, one-paragraph why))
# ---------------------------------------------------------------------------

MODELS = {
    # Pillar 1 — Self-Education
    "library/pillar-1-self-education/prompts/concept-explanation-at-level.md": (
        "Claude Sonnet 4.6",
        "Sonnet 4.6 handles calibrated, layered explanations reliably without over-elaborating. Use Opus 4.7 if the topic is highly specialized and you want maximum depth at layer 3. Avoid Haiku — it tends to compress all three layers into the same level."
    ),
    "library/pillar-1-self-education/prompts/compare-contrast.md": (
        "Claude Sonnet 4.6",
        "Sonnet renders structured comparison tables cleanly and stays specific about discriminators. For comparisons that require sub-edition precision (e.g., WHO 5th vs ICC), bump to Opus 4.7 — Sonnet sometimes blurs version-specific discriminators."
    ),
    "library/pillar-1-self-education/prompts/guideline-plain-language.md": (
        "Claude Sonnet 4.6",
        "Sonnet preserves conditional language ('consider', 'in selected patients') better than smaller models. Avoid GPT-4o here — it tends to flatten qualifiers into directives."
    ),
    "library/pillar-1-self-education/prompts/lis-informatics-review.md": (
        "Claude Opus 4.7",
        "Informatics standards (HL7, FHIR, LOINC) require depth and specificity. Opus 4.7 cites segment names and resource types more reliably. Sonnet works as a fallback but is more likely to paraphrase the standard rather than name it."
    ),
    "library/pillar-1-self-education/prompts/self-quiz-one-at-a-time.md": (
        "Claude Sonnet 4.6",
        "Sonnet respects the one-question-at-a-time rule and calibrates follow-ups well. Opus is overkill for this back-and-forth pacing; the interaction structure matters more than reasoning depth."
    ),
    "library/pillar-1-self-education/prompts/mcq-generation-with-rationales.md": (
        "Claude Opus 4.7",
        "Generating high-quality distractors with substantive wrong-answer rationales is where Opus pulls away from Sonnet. The rationales for incorrect choices are the highest-yield part of an MCQ; Sonnet rationales tend toward formulaic."
    ),
    "library/pillar-1-self-education/prompts/anki-flashcards.md": (
        "Claude Haiku 4.5",
        "Flashcard conversion is a fast, structured task — Haiku handles it well and at a fraction of the cost. Bump to Sonnet only if the source material is dense (a methods-heavy paper, a complex algorithm)."
    ),
    "library/pillar-1-self-education/prompts/board-prep-schedule.md": (
        "Claude Sonnet 4.6",
        "Sonnet does week-by-week structured planning reliably. Opus is overkill unless your situation is unusual (e.g., a re-take with very limited time and complex constraints)."
    ),
    "library/pillar-1-self-education/prompts/question-bank-gap-analysis.md": (
        "Claude Opus 4.7",
        "Identifying the *underlying* concept gaps (not just surface-level misses) requires pattern recognition across questions. Opus pulls away from Sonnet on this kind of synthesis."
    ),
    "library/pillar-1-self-education/prompts/diagnostic-algorithm-walkthrough.md": (
        "Claude Opus 4.7",
        "Multi-step algorithm walkthroughs with specific guideline versions reward Opus's depth. Sonnet works but is more likely to conflate similar protocols."
    ),
    "library/pillar-1-self-education/prompts/reverse-case-drill.md": (
        "Claude Opus 4.7",
        "Explicit reasoning chains under uncertainty are Opus's strongest use case. Sonnet skips steps; Opus shows the work, which is the point of the drill."
    ),
    "library/pillar-1-self-education/prompts/forward-case-drill.md": (
        "Claude Opus 4.7",
        "Distinguishing pathognomonic from supportive findings requires medical-knowledge depth and discipline about labels. Opus is more careful with these distinctions than Sonnet."
    ),
    "library/pillar-1-self-education/prompts/negative-drill.md": (
        "Claude Opus 4.7",
        "Counterfactual reasoning (what would change the diagnosis) and ranking by *clinical likelihood* rather than exoticism is where Opus's depth helps. Sonnet tends to surface rarer alternatives first."
    ),
    "library/pillar-1-self-education/prompts/paper-summarization.md": (
        "Gemini 2.5 Pro",
        "Best for papers attached as PDFs — Gemini's long-context handling of full-text PDFs is the strongest option. If working from pasted text only, Claude Opus 4.7 is comparable. Avoid models without document attachment if the paper is long."
    ),
    "library/pillar-1-self-education/prompts/paper-methods-critique.md": (
        "Claude Opus 4.7",
        "Methods critique requires applying named reporting guidelines (CONSORT, STROBE) with precision. Opus is more reliable at the specific framework items than Sonnet or GPT models."
    ),
    "library/pillar-1-self-education/prompts/journal-club-preread.md": (
        "Claude Opus 4.7 with paper attached",
        "Pre-read quality depends on actually reading the paper. Use Opus 4.7 with the PDF attached, or Gemini 2.5 Pro for very long papers. Without the paper text, every model fabricates; with it, Opus produces the most defensible pre-read."
    ),
    "library/pillar-1-self-education/prompts/multimodal-photomicrograph.md": (
        "Gemini 2.5 Pro",
        "Gemini currently has the strongest fine-grained image analysis for histopathology images. Claude Sonnet 4.6 multimodal is a viable alternative. Both will confidently hallucinate features — verify everything against the published answer for the teaching case."
    ),
    "library/pillar-1-self-education/prompts/multimodal-spep-ife.md": (
        "Claude Sonnet 4.6",
        "Sonnet handles structured visual interpretation (graphs, gel traces) well and respects the quiz-first protocol. Gemini 2.5 Pro is comparable; pick whichever you have access to with image attachment."
    ),

    # Pillar 2 — Teaching
    "library/pillar-2-teaching/prompts/acgme-epa-objectives.md": (
        "Claude Sonnet 4.6",
        "Sonnet produces well-structured objectives in the required 'will be able to' format with milestone mapping. Verify the milestone codes regardless of model — milestones get revised periodically and no model is reliably current."
    ),
    "library/pillar-2-teaching/prompts/blooms-mcq.md": (
        "Claude Opus 4.7",
        "Bloom's level calibration is genuinely difficult and Sonnet often mis-labels questions. Opus is more disciplined about identifying when a 'clinical vignette' actually only tests recall."
    ),
    "library/pillar-2-teaching/prompts/case-vignette-pgy.md": (
        "Claude Opus 4.7",
        "Calibrating difficulty to PGY level (red herrings, comorbidities, demographic variation) requires depth. Sonnet vignettes tend toward 'classic presentation' regardless of stated level."
    ),
    "library/pillar-2-teaching/prompts/matched-case-pair.md": (
        "Claude Opus 4.7",
        "Parallel construction with a single deliberate difference is harder than it looks. Opus is more disciplined about NOT varying confounding features."
    ),
    "library/pillar-2-teaching/prompts/osce-station.md": (
        "Claude Opus 4.7",
        "Multi-part OSCE artifacts (script, rubric, red-flag list) need internal consistency. Opus holds the parts together better than Sonnet."
    ),
    "library/pillar-2-teaching/prompts/slide-outline-1hr.md": (
        "Claude Sonnet 4.6",
        "Slide outlines are structured planning — Sonnet handles this well. Use Opus only if the topic is unusually complex and you want richer visual suggestions."
    ),
    "library/pillar-2-teaching/prompts/speaker-notes.md": (
        "Claude Sonnet 4.6",
        "Expanding bullets into spoken-voice notes is a workhorse task. Sonnet's voice is more natural for spoken delivery than GPT-4o (which tends toward written register)."
    ),
    "library/pillar-2-teaching/prompts/visual-metaphor.md": (
        "Claude Opus 4.7",
        "Generating *diverse* metaphors (not variations of one) is a creativity task where Opus pulls away. Sonnet tends to converge on similar metaphors."
    ),
    "library/pillar-2-teaching/prompts/audience-polls.md": (
        "Claude Sonnet 4.6",
        "Sonnet produces poll questions with reasonable predicted distributions. The 'plausibly wrong' answer is the discipline test — verify each poll passes that bar regardless of model."
    ),
    "library/pillar-2-teaching/prompts/video-script.md": (
        "Claude Sonnet 4.6",
        "Two-column script with timed beats is a structured creative task — Sonnet handles it well. Aloud-test the script for natural pacing regardless of which model you use."
    ),
    "library/pillar-2-teaching/prompts/resident-feedback-note.md": (
        "Claude Opus 4.7",
        "Voice and nuance matter here. Opus produces feedback that reads more like a thoughtful attending and less like a template, and is more disciplined about not adding observations you didn't provide."
    ),
    "library/pillar-2-teaching/prompts/ccc-narrative-comment.md": (
        "Claude Opus 4.7",
        "CCC narratives need tight evidence-to-claim mapping and defensible level assignment. Opus is more conservative about inflation than Sonnet or GPT models."
    ),
    "library/pillar-2-teaching/prompts/lor-starting-draft.md": (
        "Claude Opus 4.7",
        "LOR readers detect template language. Opus produces less formulaic prose than Sonnet, but the structural plausibility problem applies to all models — the differentiator is your specific anecdotes, not the model's prose."
    ),
    "library/pillar-2-teaching/prompts/journal-club-discussion-q.md": (
        "Claude Sonnet 4.6",
        "Question escalation across abstraction levels is well within Sonnet's range. Pressure-test the 'contested' question regardless of model."
    ),
    "library/pillar-2-teaching/prompts/tumor-board-presentation.md": (
        "Claude Sonnet 4.6",
        "Structured case outlines are Sonnet's wheelhouse. The PHI-stripping discipline is more important than model choice — verify before pasting case material."
    ),
    "library/pillar-2-teaching/prompts/resident-as-teacher.md": (
        "Claude Sonnet 4.6",
        "Reflective scaffolding (one concept, one slide, one exercise) suits Sonnet's pattern of producing clear, structured outputs."
    ),

    # Pillar 3 — Operations
    "library/pillar-3-educational-operations/prompts/workshops/announcement-registration.md": (
        "Claude Sonnet 4.6",
        "Marketing copy that avoids empty intensifiers — Sonnet is reasonably disciplined about this. Add explicit 'no cutting-edge, no revolutionary' instructions to any model."
    ),
    "library/pillar-3-educational-operations/prompts/workshops/pre-workshop-survey.md": (
        "Claude Haiku 4.5",
        "Survey design is a quick structured task. Haiku is fast and sufficient. Bump to Sonnet only if the audience is unusual or you need novel question types."
    ),
    "library/pillar-3-educational-operations/prompts/workshops/facilitator-runofshow.md": (
        "Claude Sonnet 4.6",
        "Timed scheduling with contingencies — Sonnet handles this reliably. Verify the timing math regardless of model."
    ),
    "library/pillar-3-educational-operations/prompts/workshops/station-by-station-guide.md": (
        "Claude Sonnet 4.6",
        "Parallel structured documents (one per station, same format) is exactly Sonnet's strength."
    ),
    "library/pillar-3-educational-operations/prompts/workshops/badge-design-spec.md": (
        "Claude Haiku 4.5",
        "Print specification is fast and structured. Haiku is sufficient and cheap."
    ),
    "library/pillar-3-educational-operations/prompts/workshops/access-card-layout.md": (
        "Claude Haiku 4.5",
        "Card layout spec — Haiku is sufficient. The accessibility/QR constraints are the discipline; the model is the easy part."
    ),
    "library/pillar-3-educational-operations/prompts/workshops/certificate-of-completion.md": (
        "Claude Haiku 4.5",
        "Template generation suits Haiku. Verify CME/accreditation language regardless of model — false credit claims are a regulatory issue, not a model issue."
    ),
    "library/pillar-3-educational-operations/prompts/workshops/post-workshop-thank-you.md": (
        "Claude Haiku 4.5",
        "Short email under 200 words — Haiku is fast and sufficient. The specific moment from the workshop has to come from you regardless."
    ),
    "library/pillar-3-educational-operations/prompts/workshops/faculty-feedback-summary.md": (
        "Claude Opus 4.7",
        "Theme synthesis from raw feedback comments — Opus is better at the 'signal vs noise' distinction and more disciplined about preserving anonymity."
    ),
    "library/pillar-3-educational-operations/prompts/rotations/orientation-onepager.md": (
        "Claude Sonnet 4.6",
        "One-page format with ruthless prioritization — Sonnet handles the constraint well. Haiku can work but tends to omit useful detail."
    ),
    "library/pillar-3-educational-operations/prompts/rotations/expectations-doc.md": (
        "Claude Sonnet 4.6",
        "Structured doc with milestone mapping — Sonnet handles this. Verify milestone codes regardless of model."
    ),
    "library/pillar-3-educational-operations/prompts/rotations/reading-list.md": (
        "Claude Opus 4.7",
        "Curation requires judgment about which papers are landmark vs current. Opus is more careful, but **verify every citation regardless of model** — hallucinated paper titles are common."
    ),
    "library/pillar-3-educational-operations/prompts/rotations/daily-schedule.md": (
        "Claude Haiku 4.5",
        "Template generation — Haiku is sufficient. The constraints (protected reading, slip handling) come from your prompt, not from model depth."
    ),
    "library/pillar-3-educational-operations/prompts/rotations/evaluation-rubric.md": (
        "Claude Opus 4.7",
        "Behavioral anchors that genuinely discriminate between levels are hard. Opus produces more differentiated anchors; Sonnet tends toward all-positive language."
    ),
    "library/pillar-3-educational-operations/prompts/rotations/mid-rotation-feedback.md": (
        "Claude Sonnet 4.6",
        "Template with a meeting structure — Sonnet handles this. The 15-min cap is the discipline; the model is the easy part."
    ),
    "library/pillar-3-educational-operations/prompts/rotations/end-of-rotation-evaluation.md": (
        "Claude Sonnet 4.6",
        "Form generation with milestone alignment — Sonnet is sufficient. Verify milestone codes."
    ),
    "library/pillar-3-educational-operations/prompts/rotations/resident-to-resident-handoff.md": (
        "Claude Sonnet 4.6",
        "Peer-to-peer template with friendly voice — Sonnet is appropriate. Strip any PHI before pasting case content regardless of model."
    ),
    "library/pillar-3-educational-operations/prompts/courses/syllabus.md": (
        "Claude Sonnet 4.6",
        "Structured doc with explicit policies (AI use, integrity) — Sonnet handles this. The AI use policy is the genuinely new part; spend time refining it."
    ),
    "library/pillar-3-educational-operations/prompts/courses/weekly-module-packet.md": (
        "Claude Sonnet 4.6",
        "Two-audience structured doc — Sonnet is the right tier. Verify reading citations regardless of model."
    ),
    "library/pillar-3-educational-operations/prompts/courses/assignment-grading-rubric.md": (
        "Claude Opus 4.7",
        "Independently-assessable dimensions and behavioral level descriptors require care. Opus produces sharper distinctions; Sonnet rubrics tend to have overlapping dimensions."
    ),
    "library/pillar-3-educational-operations/prompts/courses/feedback-collection-form.md": (
        "Claude Sonnet 4.6",
        "Survey design balancing completion and signal — Sonnet handles this. Test the 'every item maps to a decision' discipline regardless of model."
    ),
    "library/pillar-3-educational-operations/prompts/courses/course-postmortem.md": (
        "Claude Sonnet 4.6",
        "Meeting structure + artifact template — Sonnet is sufficient. The 'named owners and dates' discipline is on you, not the model."
    ),
    "library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs/journal-club-packet.md": (
        "Claude Opus 4.7 with paper attached",
        "Quality depends on actually reading the paper. Opus with PDF attached, or Gemini 2.5 Pro for very long papers. Refuse the prompt if you don't have the paper text."
    ),
    "library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs/tumor-board-case-packet.md": (
        "Claude Sonnet 4.6",
        "Template generation — Sonnet is sufficient. The PHI discipline is the entire safety story here; verify before pasting case material regardless of model."
    ),
    "library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs/grand-rounds-speaker-prep.md": (
        "Claude Opus 4.7",
        "Reading the host institution's culture and anticipating sophisticated questions from content experts requires depth. Opus is the right tier."
    ),
    "library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs/conference-schedule.md": (
        "Claude Sonnet 4.6",
        "Schedule planning with constraints — Sonnet handles this. Confirm presenter availability regardless of what the model suggests."
    ),
    "library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs/qa-prep-doc.md": (
        "Claude Opus 4.7",
        "Anticipating sophisticated hostile or content-expert questions requires depth and a kind of mental adversarialism. Opus is materially better than Sonnet at the 'hardest questions' section."
    ),
}

# ---------------------------------------------------------------------------
# Apply
# ---------------------------------------------------------------------------

def update_file(path, refinement, model_name, model_why):
    p = Path(path)
    if not p.exists():
        print(f"MISSING: {path}")
        return False

    text = p.read_text()

    # 1) Inject best_model into frontmatter (between verified_models and last_updated, or before the closing ---)
    if "best_model:" not in text:
        # Insert before the closing --- of the frontmatter block
        # Frontmatter ends at the first "\n---\n" after the opening "---\n"
        m = re.search(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            print(f"NO FRONTMATTER: {path}")
            return False
        fm_block = m.group(1)
        # Insert best_model after verified_models if present, else before last_updated, else at end
        if "verified_models:" in fm_block:
            fm_block_new = re.sub(
                r"(verified_models:.*?\n)",
                rf"\1best_model: {model_name}\n",
                fm_block,
                count=1,
            )
        else:
            fm_block_new = fm_block + f"\nbest_model: {model_name}"
        text = text.replace(f"---\n{fm_block}\n---\n", f"---\n{fm_block_new}\n---\n", 1)

    # 2) Append refinement to the prompt code block (find the first ```...``` block under "## The prompt")
    prompt_section = re.search(
        r"(## The prompt\s*\n\n```\n)(.*?)(\n```)",
        text,
        re.S,
    )
    if prompt_section:
        opening, inner, closing = prompt_section.group(1), prompt_section.group(2), prompt_section.group(3)
        marker = "**Important — refinement:**"
        if marker not in inner:
            new_inner = inner.rstrip() + f"\n\n{marker} {refinement}"
            text = text.replace(opening + inner + closing, opening + new_inner + closing, 1)

    # 3) Add (or replace) "## Best model and why" section before the final newline of the file
    bm_section = f"\n## Best model and why\n\n**{model_name}** — {model_why}\n"
    # Remove any existing section first
    text = re.sub(r"\n## Best model and why\n.*?(?=\n## |\Z)", "", text, flags=re.S)
    # Append new section at the end
    text = text.rstrip() + "\n" + bm_section

    p.write_text(text)
    return True


count = 0
missing = 0
for path, refinement in REFINEMENTS.items():
    model_info = MODELS.get(path)
    if not model_info:
        print(f"NO MODEL: {path}")
        missing += 1
        continue
    model_name, model_why = model_info
    if update_file(path, refinement, model_name, model_why):
        count += 1
    else:
        missing += 1

print(f"Refined {count} files. Missing/failed: {missing}.")
