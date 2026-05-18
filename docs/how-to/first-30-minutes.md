---
title: Your first 30 minutes with an LLM — a beginner's onboarding
last_updated: 2026-05-18
---

This guide is for the pathologist who has heard of ChatGPT, maybe seen a colleague use it, but has not actually typed anything into one of these tools on purpose. The goal is to turn "I should probably try AI someday" into "I've used AI, with intent, and I know what to do next."

You'll need: a laptop or phone, an email address, and 30 minutes. No prior experience.

---

## Minute 0–5 — pick a tool and sign in

You need exactly one of these to start. Pick whichever appeals; they are roughly equivalent for the first hour.

- **Claude** — https://claude.ai. Sign in with Google or an email. The library is built around Claude, so this is the natural choice if you want to follow along with later guides.
- **ChatGPT** — https://chatgpt.com. Sign in with Google, Microsoft, or an email. Largest user base.
- **Gemini** — https://gemini.google.com. Sign in with a Google account.

Free tiers exist for all three and are sufficient for the first 30 minutes. You do not need a paid subscription to learn.

Skip the tour if one pops up. The first 30 minutes is about doing, not reading vendor onboarding screens.

---

## Minute 5–10 — your first message

You will see a chat box at the bottom of the screen with a prompt like *"How can I help you today?"* or *"Message Claude…"*.

Type this exact prompt, replacing the bracketed part with something you actually want to know:

> Act as a senior pathologist explaining a concept to a first-year pathology resident. Explain [insert a concept you've been meaning to understand better] in three layers: a one-sentence version, a mechanistic explanation, and a nuanced detail that distinguishes someone who has thought hard about this. After your explanation, ask me one follow-up question to check my understanding.

Press Enter. Wait. The response will take 5–20 seconds.

If you can't think of a concept, try one of these: *paroxysmal nocturnal hemoglobinuria*, *cold agglutinin disease*, *the difference between MGUS and smoldering myeloma*, *how a free light chain assay works*.

What you'll get back: roughly four paragraphs of text, organized into the three layers you asked for, ending in one follow-up question.

---

## Minute 10–15 — read it like an attending, not a student

Most beginners read AI output the way they read a textbook: as authoritative. This is the wrong posture. The correct posture is: read it the way you'd read a junior resident's note that you have to sign.

Three things to do:

**1. Read for accuracy.** Is anything in the response factually wrong? Wrong threshold? Misremembered drug name? Confused mechanism? If you don't know the answer well enough to judge, that's a separate problem — you should not be using AI to learn topics where you can't catch its errors yet, without external verification.

**2. Read for calibration.** Did the "first-year resident" layer actually land at first-year level, or was it secretly a fellow-level layer with simpler words? Was the "nuanced detail" actually nuanced, or was it the same point restated?

**3. Read for hedging.** Count the phrases like "could be," "may include," "in some cases." If most sentences hedge, the answer is fluent-mush. If no sentences hedge, the model is overconfident.

Then answer the model's follow-up question. Don't think of it as a quiz; think of it as a starting point for the next exchange.

---

## Minute 15–20 — refine your prompt

Now you'll see why one shot is almost never the answer. Look back at the response and identify one specific thing you'd change. Then write a follow-up message in the same conversation:

- *"The first layer was good, but the third layer wasn't actually nuanced — it was a restatement. Give me a real third layer: something that would distinguish a fellow from a resident."*
- *"You used [X mechanism] as your explanation. I learned [Y mechanism]. Are they the same thing, or am I confused?"*
- *"This is too dense. Re-do the second layer as if I'm a PGY-1 in my first week of CP."*

Send it. Read the new response with the same three lenses (accuracy, calibration, hedging).

This second exchange is where the value compounds. The model now has context: it knows what you wanted, what you got, and what you'd change. It will adjust.

---

## Minute 20–25 — try a real pathology question

Now leave the artificial exercise behind. Ask something you actually wanted answered this week. Examples:

- *"Walk me through the workup of an isolated elevation in alkaline phosphatase, the way I'd think about it if a resident handed me the case."*
- *"My patient has a polyclonal gammopathy and an elevated kappa free light chain. Help me think through the differential."*
- *"What's the current first-line treatment for AIHA per the 2024 ASH guideline? Cite the specific recommendation."*

When the model responds, **verify at least one specific claim** before you trust the rest. Cross-check a threshold, a drug name, a guideline citation against your usual source (UpToDate, the actual guideline PDF, your institutional protocol). If the model got that one right, the rest is *more likely* correct but not guaranteed. If the model got that one wrong, treat the whole response as suspect.

This habit — verify-one-detail — is the single most important discipline you can develop. Build it in your first hour and it will protect you for years.

---

## Minute 25–30 — what NOT to do

A short list of things to avoid before you're more experienced.

**Do not upload real patient material.** Not images. Not reports. Not lab results. Not even "de-identified" ones. The risk of re-identification combined with vendor data policies you haven't read makes this a bad bet for marginal educational value. Use published teaching cases instead.

**Do not paste material from your institutional EMR or LIS.** Even if it looks generic to you, it may identify your institution's protocols, your subspecialty conventions, or patterns that map to specific patients. The default is "ask your compliance office before uploading."

**Do not cite AI output as a source.** "Claude said…" is not a citation. The model is a thinking partner, not a primary source. If a claim matters, find the actual paper or guideline and cite that.

**Do not trust the first response on any high-stakes question.** Verify. The model is fluent and that fluency is exactly what makes its errors dangerous.

**Do not assume the model has memory of past conversations.** Each conversation is independent (with rare exceptions for paid tiers with explicit memory enabled). If you tell the model your context today, it won't know it tomorrow in a new chat.

---

## What you've learned

In 30 minutes you've done five things that take most pathologists weeks to do on their own:

1. **Made a real prompt** with role, task, format, and an interactive verification cue
2. **Read the response critically** for accuracy, calibration, and hedging
3. **Refined and iterated** instead of accepting the first answer
4. **Asked something you actually wanted to know** — moved from exercise to use
5. **Established the verify-one-detail discipline** that protects against confident-wrong

---

## What to read next

- [How to write a good prompt](library.html#/docs/how-to/how-to-write-a-good-prompt) — formalizes the prompt structure you used in minute 5
- [What to do when the AI is wrong](library.html#/docs/how-to/what-to-do-when-ai-is-wrong) — the next discipline once you've started catching errors
- [The LLM landscape](library.html#/docs/how-to/llm-comparison) — which model is best for which task, with pathology examples
- The [prompt library](library.html#/library/pillar-1-self-education/index) itself — once you're ready to use prompts other people have battle-tested

---

## One last note

The most common mistake at this stage is to try AI once, get a mediocre answer, and conclude that "it's not ready" or "it can't do what I need." The model is rarely the bottleneck; the prompt usually is. If a response disappoints you, the right next step is almost always to refine the prompt — not to give up on the tool.

The pathologists who get value from AI are not necessarily the most technically skilled. They are the ones who treat the first response as a draft and keep working with it.
