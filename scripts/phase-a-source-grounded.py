#!/usr/bin/env python3
"""
Phase A — Source-grounded AI section.

13 new items added to Pillar I as a new section:
- 6 how-to guides (NotebookLM/Projects setup for specific use cases)
- 6 prompt templates (calibrated for source-grounded use, not generic chat)
- 1 privacy/copyright guide
"""

from pathlib import Path

def write_prompt(path, fm, body):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("---\n" + "\n".join(f"{k}: {v}" for k, v in fm.items()) + "\n---\n\n" + body)

P1S = "library/pillar-1-self-education/prompts"
TODAY = "2026-05-18"

# ===========================================================================
# HOW-TO GUIDES (6)
# ===========================================================================

write_prompt(f"{P1S}/sg-choose-your-tool.md",
    {"title":"Choose your tool — NotebookLM vs Claude Projects vs generic chat","pillar":"self-education",
     "event_type":"n/a","audience":"resident","difficulty":"quick-win","time_to_use":"<2min",
     "visual":"text-only","tags":"source-grounded, notebooklm, claude-projects, decision-rubric",
     "verified_models":"TODO","best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

A decision rubric for which AI tool to use when. Source-grounded AI (NotebookLM, Claude Projects, ChatGPT Custom GPTs) is different from generic chat — different strengths, different failure modes, different prep work. This guide tells you which one fits your task.

## When to use it

The first time you're considering uploading source materials to an AI tool. Also useful to re-check periodically as the tools evolve (capabilities shift every few months).

## The decision rubric

Walk yourself through these questions in order. The first "yes" determines your tool.

```
DECISION RUBRIC — pick the first one that matches

## Step 1: Do you need the AI to answer ONLY from the materials you provide?
(e.g., you're learning a specific guideline and don't want the model to mix in
its own knowledge, or you're studying for boards and want answers grounded only
in the source you're being tested on)

YES → Use NotebookLM (Google).
- Strongest at "answer only from these sources" grounding
- Citations link back to specific source passages
- Limited model choice (Google's underlying model)
- Free tier available; works well for personal study

GO TO Step 2 if NO.

## Step 2: Do you need to chat with sources AND have a sustained project that
evolves over weeks/months (curriculum design, rotation prep, ongoing journal club)?

YES → Use Claude Projects.
- Project persists; you can add/remove sources over time
- Stronger generic reasoning than NotebookLM if you want both source-grounding
  AND broader knowledge
- Better for collaborative team use within a single project
- Requires Claude Pro/Team subscription

GO TO Step 3 if NO.

## Step 3: Are you doing a quick task where you'd just paste the source into
the conversation each time and don't need a persistent setup?

YES → Use generic chat (Claude.ai, ChatGPT, etc.) with sources pasted in.
- Lowest friction
- No setup
- Source must fit context window
- Loses source after conversation ends

## Step 4: None of the above?

You probably want generic chat. Source-grounded tools are overhead you don't
need for casual queries.

## After picking, ask yourself:
- What's my privacy obligation for these sources? (See the privacy guide.)
- What's the copyright status? (See the privacy guide.)
- How will I verify the model is actually staying grounded vs drifting?
```

## Expected output

A clear decision: which tool you'll use for THIS use case. Plus awareness of the privacy/copyright considerations before you upload anything.

## Common failure modes

- **Defaulting to whatever tool you have a subscription for** rather than what fits the task. NotebookLM is free; if your task is "answer ONLY from these sources," it's likely better than your $20/month subscription.
- **Building a heavy Claude Project for a task that needed 10 minutes of generic chat.** Source-grounded setup is overhead; don't pay it unnecessarily.
- **Assuming the tool will "remember" sources across conversations** when it only persists within a project. Reset behavior varies by tool.

## Required human verification

- **Verify the tool's current grounding behavior before relying on it for high-stakes use.** Capabilities change every few months; what was true 6 months ago may not be true now.
- **Verify your privacy obligation** before uploading institutional materials. See the source-grounded privacy guide.

## Best model and why

This is a meta-prompt about choosing tools, not a prompt to give to a model. **Claude Sonnet 4.6** can help you think through the rubric if your case is ambiguous, but mostly you're using your own judgment here.
""")

write_prompt(f"{P1S}/sg-board-prep-notebook.md",
    {"title":"Build a board prep notebook","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"intermediate","time_to_use":">10min","visual":"text-only",
     "tags":"source-grounded, board-prep, notebooklm, claude-projects",
     "verified_models":"TODO","best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Step-by-step setup for a board prep notebook (NotebookLM or Claude Projects) that becomes your study companion for the months leading up to RISE, ABPath, or in-service exams. The key idea: stop pasting the same source material into every prompt; build a notebook that knows your curriculum and stays grounded in it.

## When to use it

At the start of dedicated board prep (8-16 weeks out), or when you've been pasting the same sources repeatedly and realize a notebook would save time.

**Not for:** quick one-off study (use generic chat), exam prep where the source material is constantly changing (the notebook becomes stale), or when you don't have time to curate sources (curation IS the work).

## The setup — six phases

```
BOARD PREP NOTEBOOK SETUP (NotebookLM or Claude Projects)

## Phase 1: Decide your scope

Pick ONE of these scope patterns:

A. **Full-board notebook** (e.g., one notebook covering CP, one covering AP)
   - Pros: single source of truth, comprehensive
   - Cons: huge corpus, harder to keep focused, slower retrieval

B. **Subspecialty notebooks** (e.g., separate notebooks for heme, chem, blood
   bank, micro)
   - Pros: focused, faster retrieval, easier to update
   - Cons: more setup, switching between notebooks

C. **Topic notebooks** (e.g., separate notebooks for "plasma cell neoplasms",
   "anemia workup", "TMA")
   - Pros: surgically focused on weak topics
   - Cons: many notebooks to manage

RECOMMENDATION: Start with B (subspecialty notebooks). Most board prep is
naturally organized by subspecialty, and it keeps each notebook to a
manageable corpus.

## Phase 2: Curate sources for ONE notebook

For your first notebook (start with your weakest subspecialty):

- **2-4 foundational chapters** from your primary reference (e.g., Henry's,
  Robbins, McPherson)
- **2-3 high-yield review articles** (recent — within last 5 years)
- **1-2 current guidelines** relevant to the subspecialty
- **Your own annotated notes from the rotation** (typed or scanned with OCR)
- **NOT:** old qbank questions verbatim (you want to test against, not
  contaminate the source)
- **NOT:** copyrighted material you don't have legitimate access to
  (see the privacy guide)

Aim for 10-25 documents total. More than 30 dilutes retrieval; fewer than 10
limits coverage.

## Phase 3: Upload and verify grounding

After uploading:

1. Ask a question you KNOW the answer to from the source: "What's the WHO
   classification of [entity X]?"
2. Check the response cites the actual uploaded source (NotebookLM shows
   citations explicitly; Claude Projects you have to ask)
3. Ask a question that's NOT in your source: "What's the latest 2027
   guideline update?" — the model should say "not in my sources" rather
   than confabulating from general knowledge.
4. If the model hallucinates outside the source, the grounding is weak.
   Re-evaluate your tool choice.

## Phase 4: Use it for active retrieval

Don't use the notebook as a search engine. Use it for ACTIVE RETRIEVAL:
- "Quiz me on plasma cell disorders, one question at a time, based ONLY on
  the uploaded sources. Don't reveal the answer until I commit."
- "Generate 5 MCQs based on the uploaded sources, with the source citation
  for each answer."
- "Compare the WHO criteria for X vs Y as described in the uploaded
  sources. Note any discrepancies between sources."

The notebook's value is that the questions and answers are GROUNDED in YOUR
study material, not the model's general knowledge.

## Phase 5: Update the notebook monthly

Board prep evolves. Every month:
- Add 1-2 new high-yield papers as they come out
- Remove sources that turned out to be redundant
- Re-evaluate scope (is the notebook getting too big? too narrow?)

## Phase 6: Plan for end-of-prep

The notebook is a study tool, not a permanent reference. After the exam:
- Save the notebook in archive mode
- Don't delete — useful if you re-take or want to review
- Re-evaluate for fellowship/practice use (different scope)
```

## Expected output

A working notebook you can drill against for weeks of board prep, with sources you trust and grounding you've verified.

## Common failure modes

- **Over-curating the corpus.** Spending 4 hours selecting "perfect" sources before doing any actual studying. The corpus should be good-enough; iterate.
- **Treating the notebook as a search engine.** It's a drill partner. Use it for active retrieval, not passive reading.
- **Forgetting to verify grounding** after uploads. The model may sound authoritative while drifting outside your sources.
- **Mixing copyrighted material you don't have legitimate access to.** Personal study fair-use is murky; institutional uploads can be problematic.

## Required human verification

- **Verify grounding monthly** with a known-answer probe question. Drift happens silently.
- **Cross-check at least one answer per session** against the original source. The model occasionally paraphrases in ways that change meaning.
- **For any answer that surprises you,** open the source and verify directly before incorporating into your mental model.

## Best model and why

For **board prep specifically: NotebookLM is currently the strongest** because its grounding is tighter (refuses to answer outside sources more reliably) and citations are surfaced explicitly. **Claude Projects (Sonnet 4.6 underlying)** is a strong alternative if you want broader reasoning capability alongside grounding. Generic chat with pasted sources works for casual review but loses persistence.
""")

write_prompt(f"{P1S}/sg-signout-notebook.md",
    {"title":"Build a sign-out preview notebook","pillar":"self-education","event_type":"rotation",
     "audience":"resident","difficulty":"intermediate","time_to_use":">10min","visual":"text-only",
     "tags":"source-grounded, sign-out, rotation, notebooklm, claude-projects",
     "verified_models":"TODO","best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Sets up a subspecialty-specific notebook for the rotation you're on right now. Becomes your "preview before sign-out" tool — you load yesterday's cases mentally, the notebook helps you anticipate today's sign-out questions, grounded in the actual literature your service uses.

## When to use it

The first week of a new subspecialty rotation, especially if you'll be on the service for 4+ weeks. Worth the upfront investment because the notebook gets used daily.

**Not for:** short rotations (less than 2 weeks — not worth setup), services where you don't have a clear reference set (build the reference list first), or when your attending uses their own teaching approach that doesn't map to literature.

## The setup

```
SIGN-OUT PREVIEW NOTEBOOK SETUP

## Phase 1: Curate the rotation-specific corpus

For your specific rotation, gather:

- **The 2-3 most-used reference chapters** for this subspecialty (ask the senior
  resident or the fellow — they know what gets pulled at sign-out)
- **Your attendings' published papers** (if relevant to the rotation)
- **Institutional protocols** for the workflows you'll encounter daily
  (with appropriate verification that uploading is OK — see privacy guide)
- **Last year's RISE blueprint topics** for this subspecialty (gives you
  exam-aligned scope)
- **The 3-5 most recent landmark papers** in the subspecialty
- **Your own notes** from didactics and prior rotations

Aim for 8-15 documents. Smaller than a board notebook because your scope is
narrower (one subspecialty for ~4 weeks).

## Phase 2: Add a "what attendings emphasize" companion doc

Create a short doc YOU write that captures:
- "Dr. X always asks about [specific feature] before signing out [case type]"
- "On this service, the workup for [presentation] follows this sequence"
- "The discriminating question for [common differential] is [feature]"

Add this to the notebook. It's the institution-specific layer the public
literature can't supply.

## Phase 3: Daily use pattern

End of each day, before tomorrow:
1. Pull up the notebook
2. Tell it: "Tomorrow I have a [case type] coming up. What should I review
   from the uploaded sources? Give me 3 questions to think about overnight."
3. Read the 1-2 most relevant sections it surfaces
4. Sleep on the questions

Beginning of each day:
1. "Quiz me on yesterday's [topic] in 5 questions, one at a time, from the
   uploaded sources. Don't reveal answers until I commit."
2. 5-10 min before sign-out

## Phase 4: Add to the notebook as you learn

When you encounter a teaching point at sign-out that's not in your corpus,
add it:
- Write a 2-3 sentence note about the teaching point
- Cite the case (de-identified) that illustrated it
- Add the source if your attending mentioned one

This is what makes the notebook valuable over weeks: it accumulates the
specific learning of YOUR rotation, not generic content.

## Phase 5: Archive at end of rotation

Last day of the rotation:
- Add a "what I learned this rotation" summary doc to the notebook
- Save the notebook
- Don't delete — useful when you rotate back, useful for board prep, useful
  if you go into this subspecialty for fellowship
```

## Expected output

A working notebook that becomes your daily preview tool. Should take ~2 hours to set up in week 1; pays off across the remaining weeks of the rotation.

## Common failure modes

- **Spending more time on the notebook than studying** — the notebook is a tool, not the work.
- **Forgetting to add to the notebook** as you learn. Without continuous updates, it stales.
- **Including content you don't have institutional permission to upload.** Read the privacy guide first.
- **Treating the notebook output as authoritative** at sign-out. It's prep; the case is the work.

## Required human verification

- **Verify any uploaded institutional document is OK to upload.** When in doubt, ask your PD or your institutional IT/compliance office.
- **Cross-check the notebook's answers** against the actual source at least once per week. Grounding drift is silent.
- **Your attendings' actual sign-out preferences may differ from the notebook's prediction.** The notebook is a starting hypothesis, not a verdict.

## Best model and why

**Claude Sonnet 4.6 via Claude Projects** for the conversational drill pattern + institutional notes. **NotebookLM** if you want tighter grounding and don't need the conversational flexibility.
""")

write_prompt(f"{P1S}/sg-journal-club-notebook.md",
    {"title":"Build a journal club notebook","pillar":"self-education","event_type":"conference",
     "audience":"resident","difficulty":"intermediate","time_to_use":">10min","visual":"text-only",
     "tags":"source-grounded, journal-club, notebooklm, claude-projects, literature",
     "verified_models":"TODO","best_model":"Claude Opus 4.7","last_updated":TODAY},
    """## What this prompt does

Sets up a journal-club-specific notebook containing the paper you're presenting plus 5-10 related papers, so you can discuss your paper in deep context — citing prior literature, naming contradictions, anticipating questions grounded in the cited work.

## When to use it

When you're presenting at journal club and want to engage the paper at the depth a careful discussant would. Especially valuable for high-stakes presentations (specialty journal club, society meeting, board prep).

**Not for:** casual journal club where the paper is the entire scope, generating the basic summary (use [Paper summarization](library.html#/library/pillar-1-self-education/prompts/paper-summarization) prompt instead), or papers you haven't actually read (the notebook can't substitute for engagement with the primary source).

## The setup

```
JOURNAL CLUB NOTEBOOK SETUP

## Phase 1: Acquire the corpus

1. **The paper itself** (PDF or full text). Confirm you have legitimate access.
2. **The 3-5 most-cited papers from this paper's references.** Look at the
   discussion section — which references do the authors lean on most?
3. **The 2-3 papers that contradict or complicate this paper's findings**
   (search for review articles or recent papers that cite this one critically).
4. **The relevant guideline** that addresses this clinical question
   (NCCN, ASH, society-specific).
5. **Any major prior trial** that this paper builds on or replaces.

Aim for 6-10 documents in the notebook.

## Phase 2: Verify access and provenance

- All papers should be ones you have legitimate access to (institutional
  subscription, open access, your own copies). Do not upload pirated PDFs.
- For institutional protocols or unpublished material, verify upload is OK.

## Phase 3: Initial deep read

Before you ask the notebook anything, read the primary paper yourself.
The notebook is a thinking partner, not a substitute for reading.

## Phase 4: Use the notebook for these specific drills

After your own read, ask the notebook:

1. "Based on the uploaded sources, what's the state of this field BEFORE
   this paper? What was contested, and where did this paper land in that
   debate?"

2. "Where do the uploaded sources DISAGREE with this paper's findings or
   interpretation? Be specific about which source and which point."

3. "What's the most likely critical question someone with [perspective X
   — e.g., 'a hematologist skeptical of this drug class'] would raise
   from the uploaded sources?"

4. "Generate 5 discussion questions for journal club that REQUIRE engaging
   with the broader literature in the notebook, not just the primary paper."

5. "If this paper is wrong about [specific claim], which uploaded source
   would be the strongest counterargument?"

## Phase 5: Pressure-test the notebook's responses

For each notebook response that you'll use in your presentation:
1. Open the cited source
2. Verify the claim is actually in that source as described
3. Check the citation isn't out of context

Notebooks confabulate. Verification is non-optional for journal club.

## Phase 6: Save the notebook for future reference

Even after journal club is over, this notebook becomes useful for:
- Re-presenting if you go to a society meeting
- Citing in a manuscript that touches the same question
- A board-prep reference set on this topic
```

## Expected output

A working notebook you can use to prepare a deep journal club presentation grounded in the actual literature, with verified citations.

## Common failure modes

- **Treating the notebook as a substitute for reading the paper.** It isn't.
- **Confabulated citations.** The model may say "as Smith et al. 2021 demonstrated..." with details that aren't in the actual Smith paper. Verify.
- **Over-relying on the related papers** — the discussion should center the primary paper, not become a literature review.
- **Uploading papers you don't have legitimate access to.** Pirated PDFs in an AI notebook is a copyright and ethics issue.

## Required human verification

- **Verify every citation** the notebook produces before using it in the presentation.
- **Verify the related papers are correctly characterized** — the notebook may misrepresent a paper's argument.
- **Read the primary paper yourself.** Notebook-mediated familiarity is shallow.

## Best model and why

**Claude Opus 4.7 via Claude Projects with the paper PDFs attached** for substantive engagement with literature. **NotebookLM** is a strong alternative when citation linking matters. Generic chat with pasted excerpts works for quick checks but loses the cross-source comparison value.
""")

write_prompt(f"{P1S}/sg-source-curation.md",
    {"title":"Source curation principles for AI notebooks","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"source-grounded, curation, principles","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Principles for choosing what to upload to your AI notebook. The discipline that distinguishes a useful notebook from a noisy one: every source should earn its place. Curation IS the work.

## When to use it

When building any source-grounded notebook (board prep, sign-out, journal club, institutional). Re-read when your notebook starts producing low-quality responses — the cause is almost always corpus drift.

## The principles

```
SOURCE CURATION PRINCIPLES

## Principle 1: Quality over quantity

Notebooks degrade as corpus grows beyond 25-30 documents. Retrieval gets
fuzzier; the model spreads attention across too many sources; responses
become average-of-everything rather than grounded-in-best-source.

**Rule of thumb:** if you wouldn't recommend a source to a colleague, it
doesn't belong in your notebook.

## Principle 2: Mix source types deliberately

A healthy corpus has:
- 30-40% foundational references (textbook chapters, foundational papers)
- 30-40% current evidence (recent review articles, current guidelines)
- 10-20% landmark papers (historical context, why the field thinks this way)
- 10-20% your own notes (rotation notes, attending preferences, case logs)

A corpus that's 100% review articles is shallow. A corpus that's 100%
primary literature is exhausting. Mix deliberately.

## Principle 3: Recency matters but isn't everything

For most subspecialties, sources within the last 5 years are most current.
But:
- Landmark papers from any era stay relevant (the original 1985 paper
  defining [X] is still cited weekly)
- Guidelines have specific versions — make sure you have the CURRENT one,
  not the prior one
- For rapidly evolving fields (molecular pathology, AI in pathology),
  even 2-year-old reviews can be stale

## Principle 4: Exclude what would contaminate retrieval

DO NOT upload:
- **Old qbank questions verbatim** — they bias the notebook toward
  test-question framing
- **Pirated copyrighted material** — copyright and ethics issue
- **Unpublished resident notes from other residents** without permission
- **Patient material of any kind** — never, under any circumstances
- **Drafts of your own papers** that are still under review (confidentiality)
- **Anything you'd be embarrassed for an AI tool to "learn from"** even
  though it doesn't really learn from your notebook in the training sense

## Principle 5: Document your sources

Maintain a separate doc (not in the notebook, in your own notes) listing:
- What's in the notebook
- Why each source is there
- When it was added
- When to re-evaluate

When you revisit the notebook in 6 months, this doc tells you what's stale.

## Principle 6: Iterate

Curation is not a one-time setup. Every 2-4 weeks:
- Remove sources that turned out to be redundant
- Remove sources whose answers you've memorized (they're no longer
  earning their place)
- Add 1-2 new high-yield sources as the field evolves
- Re-check the notebook's responses against current literature

## Principle 7: Different notebooks for different purposes

A board prep notebook needs different sources than a journal club notebook
than a sign-out preview notebook. Resist the temptation to build "one big
notebook for everything." Different use cases need different corpora.
```

## Expected output

A clearer mental model for what belongs in your notebook and what doesn't. Practical filter for the next time you're considering uploading something.

## Common failure modes

- **"More is better" instinct.** Resist. Quality > quantity for retrieval.
- **Uploading qbank questions** and then being surprised when the notebook produces test-style framing.
- **Never auditing the corpus.** A notebook built once and never updated decays.

## Required human verification

- The curation principles are heuristics, not rules. Calibrate to your subspecialty and use case.
- For specific copyright questions about institutional material, consult your institutional library or legal/compliance office.

## Best model and why

This is a principles document, not a prompt. **Claude Sonnet 4.6** can help you think through specific curation decisions if you're unsure.
""")

write_prompt(f"{P1S}/sg-grounding-verification.md",
    {"title":"Verify your AI notebook is actually grounded","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"source-grounded, verification, grounding-drift","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Source-grounded AI tools claim to answer "only from your uploaded sources." In practice, they drift — pulling from the model's general training data when retrieval is weak, paraphrasing in ways that change meaning, citing sources that don't actually contain the claim. This guide gives you a 5-test protocol to verify grounding before trusting your notebook for high-stakes use.

## When to use it

The first time you set up a notebook. Then monthly thereafter. Also any time the notebook's response surprises you in a "this is suspiciously confident" way.

## The protocol — 5 tests

```
GROUNDING VERIFICATION PROTOCOL

Run all 5 tests at notebook setup and monthly thereafter. If any test
fails, the notebook's grounding is weak and you should not rely on it for
high-stakes use until you understand why.

## Test 1: Known-answer probe

Ask a question you KNOW the answer to from a specific source you uploaded.

Example: "Based on the uploaded sources, what is the diagnostic threshold
for [specific entity] per the [specific guideline]?"

The response should:
- Cite the actual uploaded source (NotebookLM shows citations explicitly;
  ask Claude Projects: "Which uploaded source does this come from?")
- Give the answer that's actually in the source
- Not add information from elsewhere

If it confabulates or pulls from outside the source, grounding is weak.

## Test 2: Negative probe — out-of-corpus question

Ask a question that is NOT addressed in any of your uploaded sources.

Example: "Based on the uploaded sources, what does the 2030 guideline
say about [topic]?" (assuming you uploaded only 2024 sources)

The response should:
- Acknowledge that the uploaded sources don't address this
- Refuse to answer or clearly mark its response as drawing from general
  knowledge rather than your corpus

If the model invents a 2030 guideline answer, grounding is weak. This
is the most important test.

## Test 3: Citation verification

For a response that cites a specific source, open that source and check:
- Is the claim actually in the source as described?
- Is the wording paraphrased in a way that changes meaning?
- Is the page/section reference accurate (if cited)?

If the cited claim doesn't match the source, grounding is decorative
rather than real.

## Test 4: Cross-source disagreement detection

Upload two sources that you know disagree on a specific point. Ask:
"How do the uploaded sources differ on [topic]?"

The response should:
- Identify the disagreement
- Cite each source's position accurately
- Not artificially smooth over the conflict

If it pretends the sources agree or makes up a synthetic consensus,
grounding is weak.

## Test 5: Consistency probe — same question, different framings

Ask the same substantive question two different ways, separated by other
queries.

Example:
- Q1: "What's the diagnostic criterion for X per the uploaded sources?"
- (do other questions)
- Q2: "How would I diagnose X using only the uploaded sources?"

The two answers should be substantively the same. If they materially
differ, the model is generating fresh content each time rather than
retrieving from a stable source — that's a grounding failure.

## What to do if a test fails

1. Reduce corpus size — too many sources dilutes retrieval.
2. Check source quality — low-quality PDFs (scanned, OCR errors) degrade
   retrieval.
3. Switch tools — if NotebookLM fails and you have access to Claude
   Projects (or vice versa), try the other.
4. Don't rely on the notebook for high-stakes use until you understand
   the failure mode.

## Frequency

- **At setup:** all 5 tests
- **Monthly:** Tests 1, 2, 3
- **After major corpus changes:** all 5 tests
- **Before any high-stakes use** (board prep, journal club presentation):
  Tests 1 and 3 at minimum
```

## Expected output

A clear assessment of whether your notebook is grounded enough to trust. Often the answer is "mostly, but verify citations before relying on any specific answer."

## Common failure modes

- **Trusting the notebook without verification** because it sounds confident.
- **Skipping Test 2** (negative probe) — this is the most diagnostic test and the most often skipped.
- **Treating one passing test as proof the notebook is grounded.** Run all 5.

## Required human verification

- Verification IS the use. There's no shortcut. The notebook is a thinking partner whose work you check, not a database.

## Best model and why

This is a verification protocol, not a prompt. **Use whichever tool you're verifying.** The tests work the same way across NotebookLM, Claude Projects, and ChatGPT Custom GPTs.
""")

# ===========================================================================
# PROMPT TEMPLATES (6) — calibrated for source-grounded use
# ===========================================================================

write_prompt(f"{P1S}/sg-concept-explanation-sourced.md",
    {"title":"Source-grounded concept explanation","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"intermediate","time_to_use":"<2min","visual":"text-only",
     "tags":"source-grounded, concept, citation-required","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

The source-grounded version of [Concept explanation at level](library.html#/library/pillar-1-self-education/prompts/concept-explanation-at-level). Anchors every substantive claim to a specific uploaded source — not just "this is how it works" but "as described in [source X]". Designed for use in NotebookLM or Claude Projects with curated sources.

## When to use it

Inside a board prep, sign-out, or journal club notebook when you want an explanation anchored to YOUR specific source material, not the model's general knowledge.

## The prompt (paste into your notebook chat after sources are uploaded)

```
You are my study partner working ONLY from the sources I've uploaded to this
notebook. Do not draw from your general knowledge. If something is not in the
uploaded sources, say so explicitly rather than inventing.

## My context

- **PGY level:** [e.g., PGY-2]
- **Why I'm asking:** [e.g., "preparing for tomorrow's bone marrow sign-out"]
- **Target concept:** [the specific thing you're trying to understand]

## Explain the target concept in three layers, ALL grounded in uploaded sources

1. **First-year medical student version (1 sentence).** Plain language.
2. **My-level version (1 paragraph).** Mechanistic explanation at my level.
3. **The "thought hard about this" layer (1 paragraph).** Nuance that
   distinguishes someone who has internalized the concept from someone who
   has memorized.

## Source-grounding rules — non-negotiable

- **Every substantive claim must cite an uploaded source.** Format:
  `[Source filename or title, section if applicable]` inline.
- **If a claim is in multiple sources, cite the strongest one** (most current,
  most authoritative for this topic).
- **If a claim is NOT in any uploaded source, mark it `[NOT IN SOURCES]`** —
  do not fill in from general knowledge.
- **If sources disagree on a point, acknowledge the disagreement** with
  both citations.

## After your explanation

Ask me ONE application question that tests the most likely misunderstanding
for my level. Wait for my answer. If I'm wrong, name the specific gap with
a citation to the source that addresses it before re-explaining.

## What I will NOT accept

- Claims without source citations
- Claims that fill in gaps with general knowledge
- Citations to sources that don't actually contain the claim (I will verify)
- "In general..." statements that bypass the source-grounding rule
```

## Expected output

A 3-layer explanation where every substantive claim is followed by an inline source citation, with `[NOT IN SOURCES]` marks where the uploaded corpus doesn't address something.

## Common failure modes

- **Citations that don't match the source content.** The model paraphrases and confabulates citations. Verify.
- **General knowledge slipping in** without `[NOT IN SOURCES]` flag. The hardest failure mode to catch because the content sounds right.
- **Smoothing over source disagreements.** Push back if you know two sources disagree.

## Required human verification

- **Open every cited source and verify the claim is there.** Source-grounded does not mean truth-grounded — it means the model claims to be drawing from your sources, and you have to verify.
- For high-stakes use (e.g., before a board exam), spot-check at least 30% of citations.

## Best model and why

**Claude Sonnet 4.6 via Claude Projects** or **NotebookLM**. Both handle source citation well. NotebookLM is more reliable about staying in-corpus; Claude Projects is more flexible if you want to switch to general knowledge mid-conversation when needed.
""")

write_prompt(f"{P1S}/sg-self-quiz-sourced.md",
    {"title":"Source-grounded self-quiz from notebook material","pillar":"self-education",
     "event_type":"n/a","audience":"resident","difficulty":"quick-win","time_to_use":"2-10min",
     "visual":"text-only","tags":"source-grounded, self-quiz, drilling","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

The source-grounded version of [Self-quiz one at a time](library.html#/library/pillar-1-self-education/prompts/self-quiz-one-at-a-time). Drills you with questions that the model generates FROM your uploaded sources, with the answers traceable to specific source passages. Useful for active retrieval against YOUR specific study material.

## When to use it

Inside a board prep notebook when you want to test retention of the actual material you've been reading — not generic board questions.

## The prompt

```
You are my quiz partner working ONLY from the sources uploaded to this
notebook. Generate questions from those sources, not from your general
knowledge. Cite the source for each question's answer.

## My context

- **PGY level + topic:** [level + topic from the corpus]
- **Number of questions for this round:** [usually 5-10]
- **Difficulty calibration:** [recall / application / synthesis — pick one]

## Strict interaction rules

1. **Ask ONE question at a time.** Wait for my answer.
2. **Each question must be answerable from the uploaded sources.** If you
   can't generate a good question from the sources on this topic, tell me
   the corpus is thin on this topic rather than making up a question.
3. **After my answer, give feedback:**
   - "Correct" / "Wrong" / "Partially correct"
   - Cite the source that contains the answer: `[Source X, section Y]`
   - If wrong, name the specific gap and direct me to the source passage
4. **Adapt difficulty based on my response.**
5. **After [N] questions, give synthesis:**
   - Strongest area (cite specific responses)
   - Biggest gap (cite specific responses)
   - Which source I should re-read to address the gap

## Source-grounding rules

- **Every question must trace to a specific uploaded source.**
- **Every answer must cite the source where it's found.**
- **Do not generate questions whose answers come from your general
  knowledge rather than the uploaded corpus.**
- **If you correct me, the correction must be sourced.**

## Start now

Begin with a calibration question on [topic] drawn from the uploaded
sources. Don't tell me it's calibration; just ask.
```

## Expected output

A back-and-forth where every question and every correction is traceable to a specific uploaded source.

## Common failure modes

- **Questions whose "correct" answer is actually from the model's general knowledge** rather than your sources. Catch by asking "where in the corpus does this come from?"
- **Correction citations that don't match the source.** Verify spot-checks.
- **Model abandons source-grounding when retrieval is weak** — falls back to general knowledge silently. Watch for unsourced confidence.

## Required human verification

- **Spot-check 20-30% of citations** against the actual source.
- **For any answer that surprises you, verify directly.**
- **If the model seems consistently to "always have an answer" regardless of corpus content,** the grounding is decorative. Switch tools.

## Best model and why

**NotebookLM** for tightest grounding. **Claude Sonnet 4.6 via Claude Projects** for more conversational drill rhythm.
""")

write_prompt(f"{P1S}/sg-paper-critique-against-corpus.md",
    {"title":"Source-grounded paper critique against your corpus","pillar":"self-education",
     "event_type":"n/a","audience":"resident","difficulty":"advanced","time_to_use":"2-10min",
     "visual":"text-only","tags":"source-grounded, paper-critique, cross-source-comparison",
     "verified_models":"TODO","best_model":"Claude Opus 4.7","last_updated":TODAY},
    """## What this prompt does

Critiques a paper against the broader literature in your notebook — not against the model's general training. Surfaces where this paper agrees with, extends, or contradicts the other sources you've uploaded. Useful for journal club prep and for deciding whether to incorporate a paper into your practice.

## When to use it

Inside a journal club or topic-specific notebook that contains the primary paper plus 5-10 related sources.

## The prompt

```
You are critiquing this paper against the broader literature in the uploaded
notebook. Your job is to surface where this paper agrees with, extends,
or contradicts the other sources — based ONLY on what's in the notebook,
not your general knowledge.

## What I'm asking

- **Primary paper to critique:** [filename or title — must be in the notebook]
- **My focus:** [e.g., "Is the headline result consistent with prior trials?",
  "What's the strongest critique of the methods based on the related literature?"]

## What to produce — 5 parts

### 1. Where this paper AGREES with the broader corpus

Specific points where the primary paper aligns with conclusions in other
uploaded sources. Cite each agreement: `[primary paper claim] aligns with
[other source X, finding Y]`.

### 2. Where this paper EXTENDS the broader corpus

Novel contributions — claims or findings that go beyond what other uploaded
sources address. Be honest about whether this is genuinely new vs incremental.

### 3. Where this paper CONTRADICTS the broader corpus

Specific points where the primary paper disagrees with conclusions in other
uploaded sources. Cite both sides: `[primary paper claim X] contradicts
[other source Y conclusion Z]`. Acknowledge if you can tell from the
sources WHY they disagree (different methods, different populations,
publication date difference).

### 4. The single strongest critique from the corpus

If you had to pick ONE point from the other uploaded sources that most
challenges this paper's conclusions, what is it? Why is it the strongest?

### 5. Open questions the corpus doesn't resolve

What questions does this critique surface that no source in the notebook
can answer? These are the questions for journal club discussion.

## Source-grounding rules

- **Every comparative claim must cite both sides** (the primary paper and
  the other source).
- **If the corpus doesn't contain a relevant comparison source, say so.**
  Do not fill in from general literature you weren't shown.
- **If you're uncertain whether two sources actually disagree** (vs use
  different language for similar concepts), say so.

## What I will NOT accept

- Unsourced claims about "the literature" generally
- Vague "this paper extends our understanding" without specifics
- Synthesized contradictions that aren't actually in the sources
```

## Expected output

A 5-part critique grounded in actual cross-source comparison from your notebook, with verifiable citations on both sides of every comparison.

## Common failure modes

- **Synthetic contradictions.** The model invents disagreements that aren't actually in the sources.
- **Smoothed-over disagreements.** Push back: "Source X clearly disagrees with this paper on [Y]; address that."
- **Citation slippage.** A claim attributed to Smith 2021 isn't actually in that paper. Verify.

## Required human verification

- **Open every cited source and verify the comparison.** Both the primary paper's claim and the related source's position.
- **For journal club use, every contradiction you'll mention must be verified.** The cost of mis-citing a paper in front of colleagues is high.

## Best model and why

**Claude Opus 4.7 via Claude Projects with PDFs attached** for substantive cross-source reasoning. **NotebookLM** for tighter grounding but less reasoning depth.
""")

write_prompt(f"{P1S}/sg-cross-source-comparison.md",
    {"title":"Cross-source comparison drill","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"source-grounded, comparison, discrepancy-detection","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":TODAY},
    """## What this prompt does

Asks the notebook to compare how multiple uploaded sources address the same topic — surfacing discrepancies, definitional differences, and version drift between editions. Especially valuable when your corpus spans multiple guidelines or editions.

## When to use it

When studying a topic where you suspect (or know) the sources you've uploaded don't agree — different WHO editions, different society guidelines, different country conventions, foundational textbook vs current review.

## The prompt

```
You are surfacing discrepancies between the uploaded sources on a specific
topic. Your job is to identify where the sources disagree, not to synthesize
a consensus — disagreement IS the finding.

## What I'm asking about

- **Topic:** [be specific — e.g., "diagnostic criteria for MGUS"]
- **Which sources to compare:** [optional — name specific filenames if you
  want a focused comparison; otherwise compare across the full corpus]

## What to produce — 4 sections

### 1. Side-by-side comparison

| Aspect | Source A | Source B | Source C |
|---|---|---|---|

Rows: the specific aspects where the sources differ (definitions, cutoffs,
recommendations, terminology).

### 2. Categorize each discrepancy

For each row, label it:
- **Substantive disagreement** — sources genuinely contradict
- **Version drift** — sources agree but use different editions/years
- **Definitional difference** — sources use different terms for similar
  concepts
- **Scope difference** — sources address slightly different populations
  or use cases

### 3. The most consequential discrepancy

Which discrepancy would most change practice or interpretation if you
chose the wrong source? Why?

### 4. Recommended source for clinical use

If a learner had to pick ONE source from the uploaded corpus to use
clinically right now, which would you recommend and why? Acknowledge
tradeoffs.

## Source-grounding rules

- **Cite specific source passages** for each comparison row.
- **If you're uncertain whether two sources actually disagree** (vs
  using different language for similar concepts), say so.
- **If one source addresses a row and others don't,** mark the empty
  cells as "[not addressed]" rather than inventing a position.
- **For 'recommended source for clinical use,' acknowledge the limits
  of your information.** You're recommending based on what's in the
  notebook, not based on real-world institutional practice.

## What I will NOT accept

- A synthesized "consensus" that smooths over real disagreement
- Claims of agreement that aren't actually verified
- Recommendations beyond what the sources support
```

## Expected output

A 4-section comparison: side-by-side table, categorized discrepancies, most consequential one named, recommended source with tradeoffs.

## Common failure modes

- **Synthetic consensus.** Push back: "Source X says different. Don't smooth that over."
- **Confabulated positions** for sources that don't actually address a row.
- **Recommendation that ignores institutional context.** Your institution may use a different source for reasons you didn't share with the notebook.

## Required human verification

- **Verify each comparison row against both sources.** Cross-source comparison is where the model is most likely to invent.
- **For clinical decisions, check with the attending which source your service uses.**

## Best model and why

**Claude Opus 4.7 via Claude Projects** — substantive comparison across multiple sources rewards depth. **NotebookLM** if you want stricter citation linking but expect less synthesis.
""")

write_prompt(f"{P1S}/sg-mcq-generation-sourced.md",
    {"title":"Source-grounded MCQ generation","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"source-grounded, mcq, board-prep","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":TODAY},
    """## What this prompt does

The source-grounded version of [MCQ generation with rationales](library.html#/library/pillar-1-self-education/prompts/mcq-generation-with-rationales). Generates board-style MCQs from YOUR uploaded study materials, with every answer's correctness traceable to a specific source passage. Useful when you want to test against material you've actually been reading.

## When to use it

Inside a board prep notebook when you want practice questions calibrated to YOUR specific source material rather than generic board questions. Note: AI-generated MCQs are study tools, not validated assessment items — use real qbanks for serious prep.

## The prompt

```
You are generating MCQs from the sources uploaded to this notebook. Every
question's answer must trace to a specific uploaded source passage. If you
cannot generate a question from the sources on a topic, say so rather than
inventing.

## What I'm requesting

- **Topic from the corpus:** [be specific — e.g., "diagnostic workup of
  isolated prolonged aPTT"]
- **Number of questions:** [usually 3-5 for a focused drill]
- **Target level:** [PGY level / board level]
- **Question style:** [clinical vignette / lab values only / mixed]

## Format for each question

```
Question N (sourced from: [Source filename or title, section if applicable]):

[Vignette]

A. [Choice]
B. [Choice]
C. [Choice]
D. [Choice]
E. [Choice]

---

ANSWER: [Letter]

SOURCE PASSAGE FOR THE ANSWER:
[Quote or paraphrase the specific passage in the uploaded source that
contains the answer]

RATIONALES FOR EACH CHOICE:
A. [Why correct OR what misunderstanding leads here, with source citation
where relevant]
B. [Same]
C. [Same]
D. [Same]
E. [Same]

TEACHING POINT: The cognitive skill or content this question tests.
```

## Source-grounding rules

- **Every question must trace to specific uploaded source content.**
- **The "correct" answer must be VERIFIABLY in the source** — not interpolated
  from the source.
- **Distractor rationales should reflect actual misconceptions** the source
  addresses, where possible.
- **If you cannot generate a good MCQ from the sources on a topic,** tell me
  the corpus is thin on that topic rather than inventing.

## What I will NOT accept

- "Correct" answers that aren't actually in the uploaded source
- Citations to source passages that don't contain the claim
- Questions whose answers come from general knowledge dressed up as
  source-grounded
- Distractor rationales that are obviously implausible
```

## Expected output

N MCQs with verifiable source citations, vignette, choices, sourced answer, sourced rationales, teaching point.

## Common failure modes

- **Confabulated source passages.** The model claims the answer is in Section X but Section X doesn't contain it. Verify spot-checks.
- **"Source-grounded" questions that are really general-knowledge** dressed up. The vignette and choices are generic; only the citation is sourced.
- **Distractor rationales that don't trace to anything** (made-up misconceptions).

## Required human verification

- **VERIFY EVERY CORRECT ANSWER against the cited source passage.** The model's confidence about correctness should not be trusted.
- **For high-stakes use** (sharing with co-residents, using for formal assessment), 100% verification — not just spot-checks.
- **Remember these are study aids, not psychometrically validated questions.** Real qbanks for real board prep.

## Best model and why

**Claude Opus 4.7 via Claude Projects** — distractor generation with substantive rationales benefits from Opus's depth. **NotebookLM** for tighter source-citation linkage but weaker distractor quality.
""")

write_prompt(f"{P1S}/sg-knowledge-gap-discovery.md",
    {"title":"Knowledge gap discovery from uploaded sources","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"intermediate","time_to_use":">10min","visual":"text-only",
     "tags":"source-grounded, gap-discovery, study-planning","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":TODAY},
    """## What this prompt does

Asks the notebook to surface YOUR knowledge gaps relative to YOUR uploaded study material — through an adaptive quiz that progressively narrows on weak topics, then summarizes the gaps with specific reading recommendations from the corpus.

This is metacognition aided: the notebook helps you discover what you don't know that you don't know, based on a corpus you've decided defines "what you should know."

## When to use it

After a study block, when planning the next week of board prep, or when you have a sense you're weak somewhere but can't pin down what. Best done in a single 30-60 minute session.

## The prompt

```
You are helping me discover knowledge gaps from the sources in this notebook.
Adaptive quiz: start broad, narrow on weakness, then summarize what I should
study and which sources to read.

## My context

- **PGY level + use case:** [e.g., "PGY-3, 8 weeks until ABPath in-service"]
- **Topic scope:** [broad area to cover — e.g., "all of plasma cell neoplasms
  as covered in this notebook"]
- **Time I have for this session:** [e.g., 45 minutes]
- **My current self-assessment:** [optional — where I think my gaps are]

## Adaptive quiz protocol

### Phase 1: Breadth probe (10 questions)

Ask 10 broad questions covering the topic, one at a time, drawn from
different uploaded sources. Wait for my answer to each. Track which I
get right, partially right, wrong.

### Phase 2: Identify weak topic

After 10 questions, identify the topic (or 2-3 topics) where my responses
indicate genuine knowledge gaps (not just imprecise wording, but real
misunderstanding).

### Phase 3: Narrow drill (5-8 questions on weak topic)

Drill the identified weak topic with progressively more specific questions.
Continue until you've characterized the gap precisely:
- Is it a recall failure (I know the concept but couldn't retrieve)?
- Is it a concept gap (I don't understand the underlying mechanism)?
- Is it an integration gap (I know the pieces but can't connect them)?

### Phase 4: Gap summary

Produce a written summary:

**Topic with confirmed gap:** [name]
**Type of gap:** recall / concept / integration
**Specific subtopics where I'm weak:** [list]
**Source passages to re-read:** [specific sources and sections]
**Estimated time to address:** [hours]
**A check question I should be able to answer after re-reading:**
[specific question]

### Phase 5: Action plan

Based on the gap and my stated time budget, recommend:
- The highest-priority action to take this week
- What I should drop or defer
- When to re-test (suggest a date)

## Source-grounding rules

- All questions drawn from uploaded sources.
- Source citations on every "correct" answer.
- Reading recommendations cite specific sources in the corpus.
- If a gap is in a topic the corpus doesn't cover well, name that as
  a corpus limitation, not just my gap.

## What I will NOT accept

- Generic "study harder" recommendations
- Gap summary that doesn't name specific sources
- Quiz that doesn't actually adapt based on my responses
```

## Expected output

A 5-phase adaptive session ending with a specific gap diagnosis and source-grounded study recommendation. Takes 30-60 minutes of active engagement.

## Common failure modes

- **Model labels you "wrong" generously** to find gaps. Be skeptical — sometimes you really did know it.
- **Recommendations to "re-read" sources that don't actually address the gap.** Verify the recommended source contains what you need.
- **Gap diagnoses that confuse recall failure with concept gap.** The interventions differ — push back if labeling feels off.

## Required human verification

- **Verify the gap diagnosis** against your own sense of where you struggle. The model is one diagnostic; your self-assessment is another.
- **Verify the recommended reading actually addresses the gap** by opening the source.
- **Re-test after re-reading** to confirm the gap is closed.

## Best model and why

**Claude Opus 4.7 via Claude Projects** — adaptive reasoning across many turns rewards Opus. **NotebookLM** can do this but the adaptive logic is less smooth.
""")

# ===========================================================================
# PRIVACY AND COPYRIGHT GUIDE (1)
# ===========================================================================

write_prompt(f"{P1S}/sg-privacy-and-copyright.md",
    {"title":"Privacy and copyright for source-grounded AI","pillar":"self-education","event_type":"n/a",
     "audience":"resident","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"source-grounded, privacy, copyright, safety","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Walks through the privacy, copyright, and institutional-policy considerations BEFORE you upload anything to an AI notebook. Source-grounded AI is genuinely useful for education, but it sits on top of a complicated web of copyright, vendor terms of service, and institutional data policies — most of which are unsettled and most of which can bite you in unexpected ways.

## When to use it

The first time you're considering setting up an AI notebook with educational materials. Re-read whenever you're adding new source types you haven't uploaded before.

## The principles — 6 categories with hard rules

```
PRIVACY AND COPYRIGHT GUIDE FOR SOURCE-GROUNDED AI

## Category 1: Patient material — NEVER, UNDER ANY CIRCUMSTANCES

DO NOT upload to any AI notebook:
- Patient images (photomicrographs, gel images, gross photos, radiology
  images) from real cases — even "de-identified" ones
- Patient reports, lab results, or chart data
- Institutional case material from your sign-out, your tumor board, your
  resident teaching files

WHY: vendor terms of service vary, models retrain on unknown schedules,
and combinations of "de-identified" data are often re-identifiable in ways
you cannot predict. The educational value of using your own case material
is not worth the risk.

WHAT TO USE INSTEAD: published teaching cases, public-domain images,
legitimately-cleared teaching collections. Pathology Outlines, the WHO
classification image collections, society teaching sets, atlas chapters —
these are designed for exactly this use.

## Category 2: Copyrighted textbook material — depends on access route

Textbook chapters you have legitimate access to (institutional subscription
or personal purchase) sit in a gray zone:

PROBABLY OK:
- Uploading a chapter you legitimately purchased, for your own personal
  study, to a notebook only you can access
- Fair use for personal educational purposes is generally defensible

PROBABLY NOT OK:
- Sharing the notebook with co-residents (no longer personal use)
- Uploading material from institutional subscriptions to a personal AI
  account (terms of service violation for the subscription)
- Uploading scanned/pirated copies of textbooks you don't have access to

CONSULT YOUR LIBRARY: your institutional librarian can tell you which of
your subscriptions explicitly address AI tools. Some publishers now have
specific AI-use policies; some prohibit AI training/use entirely.

## Category 3: Institutional protocols and unpublished material

DO NOT upload without explicit permission:
- Your institution's specific clinical protocols (laboratory procedures,
  reversal protocols, sign-out workflows)
- Unpublished case material from your service
- Internal QI documents
- Resident or faculty unpublished notes without their permission
- Drafts of manuscripts under peer review (yours or others')

CONSULT YOUR COMPLIANCE OFFICE: institutional documents may be confidential
even if they don't carry an explicit "confidential" label. The default
should be "ask, don't assume."

## Category 4: Published guidelines and society documents

GENERALLY OK to upload guidelines that are publicly available:
- NCCN guidelines (verify your subscription terms)
- ASH, ASCP, CAP guideline statements when publicly accessible
- WHO classification when accessed through legitimate channels
- Open-access journal content under CC-BY licenses

WATCH OUT FOR:
- Subscription-only versions you're accessing through your institution
- Drafts or preprints not yet formally released
- Older versions when newer ones exist (use the current one)

## Category 5: Your own notes — generally OK

Your own typed notes, rotation observations (de-identified), study summaries,
and similar personal material:

GENERALLY OK to upload, BUT:
- If your notes contain attending preferences or institutional specifics,
  treat them as institutional material (Category 3)
- If your notes contain patient details (even de-identified), treat them
  as patient material (Category 1) — strip them first
- If your notes contain content you'd be embarrassed to share publicly,
  remember that the notebook is one data leak away from public

## Category 6: Vendor terms of service vary — check them

Different AI vendors have different policies:

- **NotebookLM (Google):** check current terms re: data use for training
- **Claude Projects (Anthropic):** Anthropic's policies on Project data
  are generally favorable for educational use but read current ToS
- **OpenAI Custom GPTs:** OpenAI's training data policies have evolved
  — verify what's current

THE QUESTION TO ASK FOR ANY VENDOR:
- Does my uploaded content become training data?
- Is there a way to opt out of training?
- What happens to my content if I delete the notebook?
- Are there enterprise/business tier options with stricter data
  segregation?

Read the terms before uploading anything sensitive.

## Bottom-line decision rubric

Before uploading any source, ask:

1. Is this patient material in any form? → STOP. Do not upload.
2. Is this institutional/confidential material? → Get permission first.
3. Is this copyrighted material I have legitimate access to? → Probably OK
   for personal use; not for sharing.
4. Is this material I created or that's public-domain? → Generally OK.
5. Have I checked the vendor's current terms of service? → Required for
   sensitive material.
```

## Expected output

A clearer understanding of what's safe to upload, what's gray-zone, and what's never OK. The guide doesn't replace your institutional compliance office for specific questions — but it tells you when to call them.

## Common failure modes

- **"Everyone does it" reasoning.** Other residents may be uploading patient material to AI tools. Don't follow them off the cliff.
- **Treating "de-identification" as a safety guarantee.** It isn't, especially for combinations of features (rare diagnosis + age + location can re-identify).
- **Assuming institutional subscriptions cover AI use.** Most don't explicitly; many publishers have new AI-use restrictions.
- **Treating vendor ToS as static.** Policies evolve; check periodically.

## Required human verification

- **For any sensitive upload, consult your institutional librarian or compliance office.** They have specific knowledge of your institution's policies and subscriptions.
- **For copyright questions, your institutional library is the right resource.** Not the AI vendor, not your co-residents, not online forums.
- **For patient material, the answer is always no.** No verification needed.

## Best model and why

This is a guidance document, not a prompt. The model has nothing to do with the answer to "should I upload this?"  — that's a human judgment call grounded in your institution's specific context.
""")

print("Phase A done — 13 new items in Pillar I (Source-grounded AI section):")
print("  How-to guides (6):")
print("    sg-choose-your-tool, sg-board-prep-notebook, sg-signout-notebook,")
print("    sg-journal-club-notebook, sg-source-curation, sg-grounding-verification")
print("  Prompt templates (6):")
print("    sg-concept-explanation-sourced, sg-self-quiz-sourced,")
print("    sg-paper-critique-against-corpus, sg-cross-source-comparison,")
print("    sg-mcq-generation-sourced, sg-knowledge-gap-discovery")
print("  Privacy/copyright guide (1):")
print("    sg-privacy-and-copyright")
