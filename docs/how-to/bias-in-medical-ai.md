---
title: Bias in medical AI — watching for it, working around it
last_updated: 2026-05-18
---

Every LLM you use was trained on a corpus that does not look like the world. Some populations are over-represented; others barely appear. Some specialties are deeply covered; others are sparse. Some practice patterns dominate; others are invisible. The resulting model is fluent in everything but evenly accurate in nothing.

For a pathologist using AI in education, this matters. The model's biases will subtly shape the case vignettes it generates, the differentials it offers, the images it interprets, the patient demographics it imagines. If you don't actively watch for it, you'll propagate those biases into your teaching, your assessment, and your residents' developing clinical reasoning.

This guide is the practical version of "what biases to watch for, and what to do about them." Not a screed. A working checklist.

---

## Part 1 — Where the bias comes from

Three sources, in rough order of how often they matter for medical work:

### 1. Training data composition

LLMs are trained on enormous text corpora scraped from the public internet, books, academic papers, code, and (increasingly) curated medical content. The composition of that corpus has well-documented skews:

- **English-language sources dominate.** Most medical AI knowledge is filtered through Anglophone academic medicine.
- **Western, urban, academic-center medicine is over-represented.** Major US teaching hospitals, Western European centers, Australian/Canadian academic systems generate disproportionate content.
- **Common entities are over-represented relative to rare ones.** This is structurally true of any corpus — but the imbalance is more extreme for AI than for individual pathologists, who actively study zebras.
- **Recent literature is under-represented if it's behind paywalls.** Open-access journals and pre-prints are heavily included; subscription journals less so. This skews toward certain subfields and publication models.

### 2. Reinforcement learning from human feedback (RLHF)

After pre-training, models are fine-tuned with human feedback to be "helpful, harmless, and honest." The humans doing the feedback are themselves a non-representative population (typically contractors in specific geographies, often without medical training). Their preferences get baked into the model.

For medical use, this shows up as: a tendency toward verbose hedging, a default to "consult your doctor" deflection on clinical questions, occasional refusal to engage with educationally-valid questions because they sound clinical, and a flattening of legitimate expert disagreement into apparent consensus.

### 3. The "default patient" the model imagines

Ask an LLM to generate a case vignette without specifying demographics, and you'll get patterns. Note them:

- The default age skews to adult, often white, often male (varies by entity)
- The default presentation skews to "classic textbook"
- The default geographic context skews to US academic medicine
- The default socioeconomic context is often invisible, but when probed defaults to insured patients with reliable follow-up

These defaults are not the model's bias *per se*; they're the bias of the training corpus expressed through generative defaults. But the practical effect is the same: your residents will get repeated exposure to a narrow slice of patient archetypes unless you explicitly broaden the prompts.

---

## Part 2 — Pathology-specific bias examples

The general patterns above translate into specific patterns in pathology work. Watch for these.

### Skin pathology on white skin

The dermpath literature, especially older textbook material, heavily over-represents lesions on white skin. AI-generated case vignettes for melanocytic lesions, inflammatory dermatoses, and pigmentary disorders default to white-patient framing. AI image interpretation on dermpath also performs measurably worse on darker skin — both for clinical lesions and for histologic stains where background melanin matters for interpretation.

**Mitigation:** explicitly prompt for diverse skin tones in generated vignettes. When using AI to interpret dermpath images, cross-check with at least one model trained on more diverse data, and verify against your own reading.

### Hematology reference ranges from non-representative cohorts

Many hematology reference ranges in widespread use were established in northern European cohorts. Hemoglobin thresholds for anemia, MCV-based RBC classification, and certain coagulation reference intervals reflect this. AI will often quote these reference ranges as universal when they aren't.

**Mitigation:** verify any clinically-meaningful threshold against your institutional reference range. For teaching, explicitly raise that reference ranges are population-specific — don't let AI-generated material implicitly teach that one set of cutoffs applies to everyone.

### "Classic" cases that aren't representative

AI defaults to textbook presentations. The vignette for *Mycobacterium tuberculosis* will feature the upper-lobe cavitary lesion in an immunocompetent adult; the model is less likely to generate the disseminated MAC in a person with advanced HIV, or the constitutional symptoms in a sub-Saharan African child. The vignette for sickle cell disease will likely feature acute crisis presentation; less likely to feature renal complications in middle age.

**Mitigation:** explicitly request unusual presentations. *"Generate three vignettes for tuberculosis: one classic cavitary disease, one disseminated in immunocompromise, one pediatric extrapulmonary."* This costs you nothing but produces dramatically more representative teaching material.

### Genetic/molecular bias

Variants associated with specific ancestral populations are under-represented in genomic databases the models were trained on. *BRCA1* variants common in Ashkenazi Jewish populations have rich documentation; founder variants in less-studied populations may be unfamiliar to the model or returned with low confidence. Pharmacogenomic variants follow similar patterns.

**Mitigation:** for any teaching that involves variant interpretation, especially across ancestral backgrounds, verify against ClinVar, gnomAD, or specialty databases rather than trusting the model's recall.

### Subspecialty depth bias

The model knows more about common subspecialties than rare ones. AI assistance on a heme path question is generally stronger than on, say, ophthalmic pathology or specialized neuropath subentities. This is partly training-data volume, partly RLHF priority.

**Mitigation:** for sparse subspecialties, expect more verification work per query. Use AI as a starting framework rather than as a definitive guide. Cross-check across multiple models.

### Gender presentation bias

Default patient gender in generated cases is non-random. The vignette for a heart attack defaults to male middle-aged. The vignette for "vague abdominal symptoms" defaults to female. The vignette for autoimmune disease defaults to female. These are not entirely wrong (epidemiology does have gender associations), but the defaults are stronger than the underlying epidemiology warrants.

**Mitigation:** explicitly prompt for gender, age, and presentation diversity. When the entity has known gender-different presentations (e.g., MI in women vs men), demand both versions.

---

## Part 3 — How bias surfaces in your work (concretely)

Three places to watch carefully:

### In MCQ generation

You ask the AI to generate 10 MCQs for a teaching session. By default, the cases will skew to:

- White patients
- Middle-aged adults
- Classic presentations
- US-based clinical context
- "Best answer" framings that match dominant practice patterns

If you publish or distribute these MCQs, you've propagated the biases. If your residents drill on them repeatedly, you've shaped their default mental models of disease presentation toward a non-representative archetype.

### In case vignette generation

Same problem, more visible. Generated vignettes for teaching are often striking in their demographic homogeneity. A residency teaching set that's 80% white middle-aged patients will not equip your residents to recognize disease in the patients they actually see.

### In differential diagnosis prompts

You give the AI a presentation and ask for the differential. The order in which the model lists possibilities reflects training-data priors. Common-in-corpus diagnoses appear higher than common-in-your-patient-population diagnoses, when those differ.

### In paper critique

You ask the AI to critique a study. The model's notion of "good methodology" reflects the journals it was trained on. Studies from regional journals, non-English-language journals, or fields with different methodological traditions may be unfairly criticized as "low quality" when the issue is genuinely just unfamiliarity.

---

## Part 4 — The verification discipline (specific to bias)

Beyond the general verification disciplines covered in [What to do when the AI is wrong](library.html#/docs/how-to/what-to-do-when-ai-is-wrong), three habits specifically counter bias:

### Habit 1 — Demand demographic diversity explicitly

Default-prompted output will be biased toward the dominant training-data patterns. Counter this by prompting for diversity:

> Generate three case vignettes for [entity]. Vary by: patient age (one child, one young adult, one elderly), patient race / ethnicity (intentional diversity), and clinical presentation (one classic, one atypical, one in immunocompromise). Do not default to "the textbook case."

This costs three sentences in your prompt. Output quality improves substantially.

### Habit 2 — Probe the "default patient"

When the AI generates a case without your specifying demographics, ask:

> *Why did you pick that age / sex / ethnicity for this case? Was that random, or based on epidemiology, or something else?*

The model will usually explain its default — and the explanation often reveals the training-data prior driving it. Useful both for your awareness and as a teaching opportunity for residents using the same tools.

### Habit 3 — Cross-source against epidemiology

When the AI gives you a "this typically presents as X" claim, check it against actual epidemiology data (CDC, WHO, specialty society epidemiology statements). The model's notion of "typical" is corpus-shaped, not epidemiology-shaped. The two often disagree.

---

## Part 5 — What to do in teaching

If you're using AI to generate teaching material, you have an extra responsibility: you're shaping residents' default mental models, not just answering your own questions.

Three teaching-specific practices:

### Practice 1 — Pre-screen AI-generated teaching material for representativeness

Before distributing AI-generated MCQs, vignettes, or teaching cases, audit them as a set:

- What's the demographic distribution? Is it broader than the default would have been?
- What's the presentation distribution? Are atypical presentations represented?
- What's the geographic / institutional context? Is it varied?

If a set fails this audit, re-prompt with explicit diversity requirements and re-audit. The cost is small; the benefit (residents who recognize disease in diverse patients) is large.

### Practice 2 — Teach the bias explicitly

When teaching residents to use AI, teach them about its biases too. Not as a one-time disclaimer but as ongoing discipline. *"What do you notice about the default demographics of the cases the model is generating? Now re-prompt for diversity and compare."* This is a 5-minute teaching exercise that produces a permanent habit.

### Practice 3 — Pair AI-generated cases with real-world data

The strongest counter to AI bias is real cases from real practice. A teaching set that uses AI for the *framework* of a case but pulls demographic and presentation patterns from your institution's actual case mix combines AI's efficiency with reality's representativeness.

---

## Part 6 — Bias in image-based AI specifically

Image interpretation models inherit and amplify the biases of their training images. Specific patterns:

- **Dermpath models trained on lighter skin perform worse on darker skin** (well documented across radiology and dermatology AI)
- **Histology models trained on a single institution's scanner perform worse on slides from other scanners** (the "domain shift" problem)
- **Models trained primarily on academic-center cases may misinterpret community-hospital workups** that look subtly different (different staining protocols, different scanner brands, different cropping conventions)

These are not flaws you can prompt your way around in real time. They are properties of the model. The mitigation is: don't treat any AI image interpretation as definitive, especially on cases that come from populations or settings under-represented in training.

The cross-model verification habit ([Working with images](library.html#/docs/how-to/working-with-images), Part 6) is partially protective: if two models trained on different datasets converge, the bias is less likely to be the explanation. If they diverge, treat the case as one where AI is unreliable rather than picking a winner.

---

## Part 7 — Practical checklist

A card for your wall:

- [ ] When generating teaching material, did I prompt for demographic diversity explicitly?
- [ ] When generating case vignettes, did I vary the presentation (classic / atypical / extreme)?
- [ ] When the AI gave me a "typical" claim, did I verify against actual epidemiology?
- [ ] When interpreting images, did I cross-check with a different model?
- [ ] When using image AI on patients underrepresented in training data, did I weight my own judgment more heavily?
- [ ] When teaching residents about AI, did I explicitly cover its biases as a discipline, not a disclaimer?
- [ ] When publishing AI-assisted work, did I audit my generated examples for representativeness before they go out?

If you can answer yes to most of these on a routine basis, you are using AI in a way that doesn't propagate its biases. That is a meaningful piece of professional discipline, and it's worth building.

---

## Part 8 — One last frame

AI bias is not a fixable property of the current models. It's a structural feature of how they're built. New models reduce some biases and introduce others. Hoping the next version will be unbiased is not a strategy.

The realistic posture: assume bias, design your workflow to counter it, teach the next generation of pathologists that this is part of being a competent AI user.

If you can do that, you're not waiting for the technology to fix itself. You're doing your part to use it well.
