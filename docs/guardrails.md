---
title: Guardrails
last_updated: 2026-05-17
---

## Read this once before you use anything in the library

The library has five hard guardrails. They are not stylistic recommendations or hedges against unlikely risks. They are observed failure modes from real use of AI in pathology education contexts. Crossing them produces concrete harms — to learners, to patients, to your professional standing, to the institution.

## 1. Accuracy

**Cross-check every clinically relevant output against an authoritative source before treating it as correct.**

Large language models routinely produce text that is *structurally correct* — it reads like a textbook chapter, with appropriate sentence rhythm and reasonable transitions — while containing factual errors. The structural fluency is exactly what makes the errors dangerous: there is no surface signal that something is wrong.

Specific rules:

- **Numerical thresholds, dosing, cutoffs, and reference ranges:** verify against the current guideline or your institutional protocol. Models confidently misremember these.
- **Drug names and indications:** verify against the FDA label or a maintained reference (UpToDate, DynaMed). Models confuse similar drug names, especially with newer agents.
- **Guideline recommendations:** verify against the current published guideline, not a paraphrase. Models tend to soften recommendations and to attribute recommendations to the wrong organization.
- **Statistical claims:** verify against the cited paper. Models routinely cite papers that do not exist, or cite real papers that do not contain the claim attributed to them.

If a piece of AI output would meaningfully change clinical or educational decisions, **verification is not optional**.

## 2. PHI and identifiable cases

**Zero patient data of any kind enters any AI tool, ever.**

This rule has no exceptions and no gradations. It applies to:

- Identifiable patient information (names, MRNs, accession numbers, demographic combinations sufficient for re-identification)
- De-identified-but-real cases from your institution
- Screenshots, photomicrographs, or images derived from actual specimens
- Institutional exam material, mock cases written from real specimens, ABP/RCPath/equivalent practice materials drawn from real cases

Why the absolute rule:

1. **You cannot prove a case is non-identifiable in court.** Combinations of age, location, rare diagnosis, and date are often re-identifiable. Your good-faith de-identification effort is not a defense.
2. **You cannot control what the AI provider does with the data.** Terms of service vary, models retrain, contracts change. Assume anything you paste is permanent and searchable.
3. **The teaching value is not worth the risk.** Published teaching cases and public-domain material exist precisely for this purpose. Use them.

For multimodal prompts: published atlas cases, public domain images, or images from your own legitimately-cleared teaching collection. Nothing else.

## 3. Bias and representation

**Review generated cases and vignettes for demographic representation and pattern bias.**

AI-generated case vignettes tend toward statistical defaults that under-represent women, racial minorities, older adults, and presentations that diverge from the textbook archetype. Over a series, this produces:

- Vignettes that are disproportionately middle-aged white male
- Symptom presentations that under-represent atypical-but-common variants
- Diagnostic algorithms that under-weight pretest probability adjustments for relevant demographics

Mitigations:

- **Review at the series level, not the case level.** A single case can be any demographic. A series of 20 cases should reflect the actual epidemiology of the conditions taught.
- **Specify demographics in the prompt.** If you do not, the model defaults; if you do, you control.
- **Audit periodically.** Pull a random sample of vignettes you have used and check the distribution.

This is particularly important for residency-program-wide materials (CCC banks, OSCE stations, board prep collections) where the cumulative effect of bias shapes how residents reason about populations.

## 4. Authorship and disclosure

**AI cannot be an author. AI use must be disclosed in formal scholarly work.**

The relevant norms come from ICMJE, COPE, and most journal-specific policies (including the Journal of Pathology Informatics). The current consensus is:

- **Authors are humans accountable for the work.** AI tools do not qualify because they cannot take responsibility, cannot respond to peer review, and cannot consent to publication.
- **AI use must be disclosed.** Most journals now require a disclosure statement naming the tools used, what they were used for (literature search, drafting, editing, figure generation), and the human author's verification process.
- **The author is responsible for the accuracy of AI-assisted content.** "The AI said so" is not a defense against a factual error in a published manuscript.

For educational use of the prompts in this library:

- Drafts of resident feedback, CCC narratives, and LORs should be reviewed before submission. The author of the comment is *you*, not the AI.
- Slides and teaching materials adapted from AI drafts do not typically require disclosure unless your institution or the venue has a specific policy.
- Any publication, conference abstract, or peer-reviewed work that uses AI-assisted drafting **must** disclose per the venue's policy.

## 5. The structural plausibility failure mode

This deserves its own section because it is the failure mode that most often gets pathologists into trouble.

**AI-generated text reads as competent prose while being subtly wrong in ways that a domain expert will catch and a junior reviewer will not.**

The mechanism: the model has learned what a paragraph about, say, the Bethesda System grading of cervical cytology *looks* like. It produces something with the right structure (criteria, examples, pitfalls, references), the right tone (measured, hedged, citing landmark papers), and the right length. Then one of the criteria is subtly miscategorized, one of the examples is from the wrong specimen type, and the cited paper does not contain the claim.

A pathologist reading the paragraph in their own subspecialty notices immediately. A pathologist reading the paragraph outside their subspecialty does not.

The implications:

- **AI-drafted teaching content for learners requires faculty review in the relevant subspecialty.** Faculty within the subspecialty can verify; cross-subspecialty review is not sufficient.
- **AI-drafted content for personal study requires verification against authoritative sources.** You are, by definition, in your knowledge gap when you're studying — you cannot rely on your own subspecialty recognition.
- **AI-drafted material that will appear in formal documents (CCC, LOR, syllabus) requires the human author to read every sentence with the question "would I write this exact sentence?" — and rewrite the ones where the answer is no.**

## Educational integrity

Do not submit AI-generated content as your own work for formal assessment. This includes:

- Course assignments, written examinations, board preparation questions submitted to a program
- Manuscripts, abstracts, or grant applications
- Letters of recommendation written for someone else (you, the recommender, are the author and must do the substantive writing)

Using AI as a brainstorming partner, drafting assistant, or editor is acceptable in most academic contexts. Submitting AI output as if it were your independent intellectual work is not.

## In summary

Five rules. None of them are unreasonable. All of them are observed-from-the-field. The cost of following them is modest. The cost of crossing them is high enough that none of these prompts is worth it.
