---
title: Common mistakes and antipatterns — what not to do
last_updated: 2026-05-18
difficulty: intermediate
category: practice
---

Every other tutorial in this section tells you what to do. This one tells you what not to do. It's the companion piece — the catalog of failure modes that take pathologists from "AI seems useful" to "AI got me into trouble" or "AI hasn't really changed my work."

Twelve antipatterns, in rough order of frequency and consequence. Read once for orientation; come back when you notice yourself drifting into one.

---

## Antipattern 1 — Over-reliance: treating AI as authoritative

**What it looks like:** you ask the AI a clinical or factual question; the answer sounds confident; you accept it; you act on it without verification.

**Why it happens:** the fluent prose is a strong social signal of correctness. Models speak in the voice of a confident expert. Without active counter-discipline, you accept what the voice says.

**Why it's harmful:** you propagate confident-wrong answers into your teaching, your assessment of residents, your own clinical reasoning, and (worst case) your patient care. The error is harder to detect later because the prose was so persuasive.

**Corrective:** verify-one-detail per response, always. The [What to do when the AI is wrong](library.html#/docs/how-to/what-to-do-when-ai-is-wrong) tutorial is the working manual. Build the verification habit early; it never stops being necessary.

---

## Antipattern 2 — Single-shot mindset: one prompt, no refinement

**What it looks like:** you type a question, read the response, accept what you got, move on. If the response is mediocre, you conclude "the AI isn't good at this."

**Why it happens:** ChatGPT looks like a search engine; people use it like a search engine. Search engines don't reward iteration; AI rewards it enormously.

**Why it's harmful:** the difference between a poorly-prompted first answer and a well-iterated third answer is dramatic. The pathologists who quit AI after one bad answer never see the second half of the value.

**Corrective:** treat the first answer as a draft, never the deliverable. Three rounds is the right unit. The [How to write a good prompt](library.html#/docs/how-to/how-to-write-a-good-prompt) tutorial covers the iteration pattern in detail.

---

## Antipattern 3 — Copy-paste without editing

**What it looks like:** you generate a case vignette, an MCQ, a slide outline, a feedback note. You paste it directly into your work product without editing.

**Why it happens:** the output looks polished. Editing feels redundant. You're busy.

**Why it's harmful:** several layers.

- Generic AI output is recognizably AI-shaped — residents will notice. Trust in your materials erodes.
- The output may contain subtle factual errors you'd have caught in editing.
- The output reflects the model's defaults (demographic, presentational, geographic) rather than your context.
- You're not learning the underlying material at the depth you would if you'd written it yourself.

**Corrective:** AI generates drafts; you edit the drafts. Always. If the draft is unusable, prompt again or write from scratch. Never publish unedited AI output to anyone whose opinion of you matters.

---

## Antipattern 4 — Citing AI as a source

**What it looks like:** "Per Claude" or "According to ChatGPT, the threshold is X" — in a presentation, an article, a teaching slide, a CCC narrative, a manuscript.

**Why it happens:** the AI delivered the information; it feels intellectually honest to credit the source.

**Why it's harmful:** AI is not a primary source. It can't be cited because the underlying provenance isn't traceable. Citing AI in scholarly work has been treated as a methodological flaw or worse by editors and reviewers. In educational materials, it implicitly teaches your residents to do the same.

**Corrective:** if a claim matters, find the actual primary source (paper, guideline, textbook) and cite that. If you can't find the primary source, the claim shouldn't appear in your work. The [Disclosure and authorship](library.html#/docs/how-to/disclosure-and-authorship) tutorial covers the right way to credit AI use — as a tool used, not as a source cited.

---

## Antipattern 5 — Building a notebook nobody uses

**What it looks like:** you spend two hours setting up a NotebookLM or Claude Project with 25 carefully curated sources. You ask it three questions over the next week, then forget it exists.

**Why it happens:** the setup is more fun than the use. Curation has a clean ending; daily use is a habit that requires maintenance.

**Why it's harmful:** sunk-cost mistake. The two hours of setup is a real opportunity cost. And the unused notebook can't earn the investment back.

**Corrective:** before building a notebook, write down three specific questions you anticipate asking it in the next week. If you can't write three, don't build the notebook. Use the [Source curation principles](library.html#/docs/how-to/curate-sources) tutorial to keep notebooks small and useful rather than impressive and inert.

---

## Antipattern 6 — "Asking for the answer" instead of thinking with the model

**What it looks like:** you encounter a diagnostic question, paste it into the AI, accept the answer, and move on. You did no cognitive work.

**Why it happens:** the AI answers faster than you can think through it yourself. The temptation is to outsource the cognition.

**Why it's harmful:** for any case you might see again — which is most cases in a teaching practice — you've skipped the learning. You're building dependency without building skill. Your AI-augmented reasoning is shallower than your unaided reasoning would have been if you'd worked the case.

**Corrective:** frame AI sessions as drills, not lookups. "Help me think through this" produces different prompts and different output than "give me the answer." The [Working with images](library.html#/docs/how-to/working-with-images) tutorial calls out this trap specifically in the context of image-based work.

---

## Antipattern 7 — Letting AI write things you can't defend

**What it looks like:** you submit a manuscript section, a grant paragraph, or a teaching slide that uses AI-drafted prose. Later, someone asks you to clarify a specific claim. You can't, without going back to the AI to figure out what was meant.

**Why it happens:** AI prose looks finished. The temptation is to keep it. The cost of revising it down to what you actually understand feels like wasted work.

**Why it's harmful:** if you can't defend it, it isn't yours. In a scholarly context this borders on misconduct. In a teaching context, you lose authority with learners the moment your inability to defend the content becomes visible. In a clinical context, the consequences can be material.

**Corrective:** a working test. Before submitting any AI-assisted content, give a 5-minute extempore talk on it to a co-author, a colleague, or your reflection in the mirror. If you can't, you don't yet own it. Either learn it well enough to defend, or remove it.

---

## Antipattern 8 — Not verifying numerical thresholds

**What it looks like:** the AI mentions a specific cutoff, threshold, dose, reference range, or sensitivity / specificity number. You incorporate it into your teaching or your decision without checking it against the current authoritative source.

**Why it happens:** numbers look authoritative. They feel like the kind of thing the AI would get right.

**Why it's harmful:** numerical thresholds are *the* most common type of confident-wrong from current models. Guidelines change; the model's training data is frozen. The number that was right in 2022 may not be right in 2026. The model will recite the 2022 number with full confidence.

**Corrective:** add this to every prompt where a threshold might matter: *"For any numerical threshold or diagnostic cutoff, flag it explicitly so I can verify against the current guideline."* Then verify the flagged thresholds against the actual current guideline before using them. Never trust a model-recalled number for a clinical decision.

---

## Antipattern 9 — Letting AI replace genuine learning

**What it looks like:** you stop reading primary literature in your subspecialty because the AI summarizes it. You stop working through cases manually because the AI walks you through them. Over months, your skill plateaus or regresses while your perceived skill rises.

**Why it happens:** AI offers an attractive bargain — the appearance of competence without the work. The trade is invisible until it matters.

**Why it's harmful:** when the AI is unavailable, wrong, or out of its depth, you have nothing to fall back on. The skill you would have built by reading and reasoning didn't get built. You're more dependent than you realize.

**Corrective:** use AI to *accelerate* your learning, not to *replace* it. Read the paper yourself, then ask the AI to challenge your interpretation. Work the case yourself, then ask the AI to critique your reasoning. The discipline: AI is a tutor; tutoring works only when the student does the work.

---

## Antipattern 10 — Treating "the model said it" as cover

**What it looks like:** something goes wrong with AI-assisted work — an incorrect threshold in a slide, a misattributed citation in a manuscript, a misdiagnosis in a teaching case. Asked to account for it, you say "well, that's what the AI returned."

**Why it happens:** the responsibility feels diffused. The AI generated the content; surely some of the fault is its.

**Why it's harmful:** there is no shared responsibility with the AI. You are the author of the work. The model is a tool. A pathologist whose CCC narrative says "patient improved appropriately" but actually meant the opposite cannot blame the EMR's auto-complete; the same is true here.

**Corrective:** internalize that AI-assisted work is your work. The accountability is undivided. This isn't punitive — it's just the actual relationship between you and the tool.

---

## Antipattern 11 — Disclosing too much or too little

**What it looks like:** either (a) you disclaim every minor use of AI in every email, slide, and informal note ("AI-assisted draft, may contain errors") — to the point that the disclaimers become noise; or (b) you use AI substantially in scholarly work and don't disclose it at all because "it was only assistance."

**Why it happens:** both extremes come from not having a clear personal policy on what triggers disclosure.

**Why it's harmful:** over-disclosure trains your audience to ignore disclaimers, including the ones that matter. Under-disclosure is misconduct in scholarly contexts and erodes trust in informal ones.

**Corrective:** follow the [Disclosure and authorship](library.html#/docs/how-to/disclosure-and-authorship) tutorial. Disclose when AI materially shaped the work (substantial drafting, key analytical decisions, framing of an argument). Don't disclose for routine spell-check, grammar polish, or brainstorming you didn't ultimately use.

---

## Antipattern 12 — Refusing to engage with AI at all

**What it looks like:** you decide the technology isn't ready, isn't ethical, isn't worth the complexity. You don't use it. You expect your residents not to.

**Why it happens:** legitimate concerns about accuracy, bias, ethics, and disclosure that haven't been resolved at the field level.

**Why it's harmful:** your residents are using AI whether you bless it or not. They are getting their AI literacy from peers, social media, and trial-and-error rather than from a faculty member who could shape it. The technology is now ambient in medical education; opting out as faculty means opting out of shaping how the next generation uses it.

**Corrective:** you don't have to use AI extensively for your own work to engage with it as an educator. Read enough to understand what your residents are doing, talk to them about it, set explicit norms for your service. Your engagement doesn't have to be enthusiastic — it does have to be informed.

---

## Summary card

The thirteen things to avoid:

1. Trusting AI as authoritative without verification
2. Accepting first answers instead of iterating
3. Pasting AI output without editing
4. Citing AI as a source
5. Building notebooks you don't use
6. Asking for answers instead of thinking with the model
7. Submitting work you can't defend
8. Not verifying numerical thresholds
9. Letting AI replace genuine learning
10. Treating "the AI said it" as cover
11. Over-disclosing OR under-disclosing
12. Opting out of AI entirely as an educator

If you can avoid these, you're using AI in a way that compounds your skill rather than substituting for it. That's the durable outcome — not "I used AI today" but "I'm a better pathologist and educator because of how I use AI."

---

## One closing observation

The antipatterns above are the same shape as antipatterns with any powerful tool. The microscope user who skips the gross. The fellow who reads UpToDate without ever opening the primary literature. The resident who lets the senior do all the difficult sign-outs. The pattern is always: take a tool that can amplify thinking and use it instead to bypass thinking.

AI is more tempting because it's better at the bypass than most tools. But the corrective is the same one experienced teachers have applied for generations: use the tool to do the work *better*, not to skip it.

If you internalize that, every antipattern above corrects itself.
