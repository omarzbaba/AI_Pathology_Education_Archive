#!/usr/bin/env python3
"""
Builds library/manifest.json — a structured index of all prompts that the
library viewer reads to render the card grid views.

Run after any prompt is added/edited/removed:
  python3 scripts/build-manifest.py
"""

import json
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Category mapping per prompt slug
# Categories control which icon shows on the card
# ---------------------------------------------------------------------------

CATEGORY = {
    # Pillar 1 — Self-Education
    "concept-explanation-at-level": "learn",
    "compare-contrast": "learn",
    "guideline-plain-language": "learn",
    "lis-informatics-review": "learn",
    "self-quiz-one-at-a-time": "drill",
    "mcq-generation-with-rationales": "drill",
    "anki-flashcards": "drill",
    "board-prep-schedule": "plan",
    "question-bank-gap-analysis": "drill",
    "diagnostic-algorithm-walkthrough": "drill",
    "reverse-case-drill": "drill",
    "forward-case-drill": "drill",
    "negative-drill": "drill",
    "paper-summarization": "read",
    "paper-methods-critique": "read",
    "journal-club-preread": "read",
    "multimodal-photomicrograph": "image",
    "multimodal-spep-ife": "image",
    # New Pillar 1 prompts (batch 1)
    "ihc-stain-interpretation": "image",
    "molecular-result-interpretation": "drill",
    "differential-by-histologic-pattern": "drill",
    "critical-value-workflow": "drill",
    "blood-smear-systematic-review": "image",
    "frozen-section-thinking-aloud": "drill",
    # Source-grounded AI section (Phase A) — setup guides + grounded variants.
    # Decision-rubric / principles entries moved to /docs/how-to/.
    "sg-board-prep-notebook": "notebook",
    "sg-signout-notebook": "notebook",
    "sg-journal-club-notebook": "notebook",
    "sg-concept-explanation-sourced": "notebook",
    "sg-self-quiz-sourced": "notebook",
    "sg-paper-critique-against-corpus": "notebook",
    "sg-cross-source-comparison": "notebook",
    "sg-mcq-generation-sourced": "notebook",
    "sg-knowledge-gap-discovery": "notebook",
    # Pillar 2 — Teaching
    "acgme-epa-objectives": "assess",
    "blooms-mcq": "assess",
    "case-vignette-pgy": "teach",
    "matched-case-pair": "teach",
    "osce-station": "assess",
    "slide-outline-1hr": "teach",
    "speaker-notes": "teach",
    "visual-metaphor": "teach",
    "audience-polls": "teach",
    "video-script": "teach",
    "resident-feedback-note": "write",
    "ccc-narrative-comment": "write",
    "lor-starting-draft": "write",
    "journal-club-discussion-q": "discuss",
    "tumor-board-presentation": "discuss",
    "resident-as-teacher": "teach",
    # New Pillar 2 prompts (batch 2)
    "microscopy-teaching-session": "teach",
    "sign-out-teaching-turn": "teach",
    "tumor-board-prep-coaching": "discuss",
    "subspecialty-rotation-goals-letter": "comms",
    "difficult-feedback-conversation-prep": "write",
    # New Pillar 3 prompts (batch 3)
    "call-schedule-generator": "plan",
    "lab-incident-debrief": "debrief",
    "visiting-professor-invitation": "comms",
    "irb-qi-protocol": "template",
    "promotion-portfolio-narrative": "write",
    "medical-education-abstract": "write",
    "rotation-block-scheduling": "plan",
    # Pillar 3 — Operations
    "announcement-registration": "comms",
    "pre-workshop-survey": "comms",
    "facilitator-runofshow": "plan",
    "station-by-station-guide": "plan",
    "badge-design-spec": "template",
    "access-card-layout": "template",
    "certificate-of-completion": "template",
    "post-workshop-thank-you": "comms",
    "faculty-feedback-summary": "debrief",
    "orientation-onepager": "template",
    "expectations-doc": "template",
    "reading-list": "read",
    "daily-schedule": "plan",
    "evaluation-rubric": "assess",
    "mid-rotation-feedback": "debrief",
    "end-of-rotation-evaluation": "assess",
    "resident-to-resident-handoff": "debrief",
    "syllabus": "template",
    "weekly-module-packet": "teach",
    "assignment-grading-rubric": "assess",
    "feedback-collection-form": "comms",
    "course-postmortem": "debrief",
    "journal-club-packet": "discuss",
    "tumor-board-case-packet": "discuss",
    "grand-rounds-speaker-prep": "discuss",
    "conference-schedule": "plan",
    "qa-prep-doc": "discuss",
}

PILLAR_DIRS = [
    ("pillar-1-self-education", "Self-Education", "Using AI to learn pathology", [
        ("Concept work", "library/pillar-1-self-education/prompts", [
            "concept-explanation-at-level","compare-contrast","guideline-plain-language","lis-informatics-review",
        ]),
        ("Self-quizzing", "library/pillar-1-self-education/prompts", [
            "self-quiz-one-at-a-time","mcq-generation-with-rationales","anki-flashcards","board-prep-schedule","question-bank-gap-analysis",
        ]),
        ("Case-based drilling", "library/pillar-1-self-education/prompts", [
            "diagnostic-algorithm-walkthrough","reverse-case-drill","forward-case-drill","negative-drill",
            "differential-by-histologic-pattern","frozen-section-thinking-aloud",
        ]),
        ("Reading the literature", "library/pillar-1-self-education/prompts", [
            "paper-summarization","paper-methods-critique","journal-club-preread",
        ]),
        ("Multimodal & lab", "library/pillar-1-self-education/prompts", [
            "multimodal-photomicrograph","multimodal-spep-ife",
            "ihc-stain-interpretation","blood-smear-systematic-review",
        ]),
        ("Molecular & CP workflow", "library/pillar-1-self-education/prompts", [
            "molecular-result-interpretation","critical-value-workflow",
        ]),
        # Source-grounded setup guides + grounded variants of regular prompts.
        # Decision-rubric / principles entries moved to /docs/how-to/.
        ("Source-grounded AI (NotebookLM & Claude Projects)", "library/pillar-1-self-education/prompts", [
            "sg-board-prep-notebook","sg-signout-notebook","sg-journal-club-notebook",
            "sg-concept-explanation-sourced","sg-self-quiz-sourced",
            "sg-mcq-generation-sourced","sg-knowledge-gap-discovery",
            "sg-paper-critique-against-corpus","sg-cross-source-comparison",
        ]),
    ]),
    ("pillar-2-teaching", "Teaching", "Using AI to teach pathology to others", [
        ("Learning objectives & assessment", "library/pillar-2-teaching/prompts", [
            "acgme-epa-objectives","blooms-mcq",
        ]),
        ("Cases & vignettes", "library/pillar-2-teaching/prompts", [
            "case-vignette-pgy","matched-case-pair","osce-station",
        ]),
        ("Lectures & presentations", "library/pillar-2-teaching/prompts", [
            "slide-outline-1hr","speaker-notes","visual-metaphor","audience-polls","video-script",
            "microscopy-teaching-session",
        ]),
        ("Written feedback & narrative", "library/pillar-2-teaching/prompts", [
            "resident-feedback-note","ccc-narrative-comment","lor-starting-draft",
            "difficult-feedback-conversation-prep",
        ]),
        ("Discussion-based formats", "library/pillar-2-teaching/prompts", [
            "journal-club-discussion-q","tumor-board-presentation","resident-as-teacher",
            "sign-out-teaching-turn","tumor-board-prep-coaching",
        ]),
        ("Resident communication", "library/pillar-2-teaching/prompts", [
            "subspecialty-rotation-goals-letter",
        ]),
    ]),
    ("pillar-3-educational-operations", "Educational Operations & Documentation", "Using AI to produce the artifacts around teaching events", [
        ("Workshops", "library/pillar-3-educational-operations/prompts/workshops", [
            "announcement-registration","pre-workshop-survey","facilitator-runofshow","station-by-station-guide",
            "badge-design-spec","access-card-layout","certificate-of-completion","post-workshop-thank-you","faculty-feedback-summary",
            "lab-incident-debrief",
        ]),
        ("Rotations", "library/pillar-3-educational-operations/prompts/rotations", [
            "orientation-onepager","expectations-doc","reading-list","daily-schedule",
            "evaluation-rubric","mid-rotation-feedback","end-of-rotation-evaluation","resident-to-resident-handoff",
            "call-schedule-generator","rotation-block-scheduling",
        ]),
        ("Courses", "library/pillar-3-educational-operations/prompts/courses", [
            "syllabus","weekly-module-packet","assignment-grading-rubric","feedback-collection-form","course-postmortem",
            "irb-qi-protocol","promotion-portfolio-narrative",
        ]),
        ("Conferences & journal clubs", "library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs", [
            "journal-club-packet","tumor-board-case-packet","grand-rounds-speaker-prep","conference-schedule","qa-prep-doc",
            "visiting-professor-invitation","medical-education-abstract",
        ]),
    ]),
]


def parse_prompt(path):
    """Extract metadata + intent from a prompt file."""
    text = Path(path).read_text()
    # Frontmatter
    fm = {}
    m = re.search(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).split("\n"):
            kv = line.split(":", 1)
            if len(kv) == 2:
                fm[kv[0].strip()] = kv[1].strip()
    # Intent ("## What this prompt does" first paragraph)
    intent_m = re.search(r"## What this prompt does\s*\n\n(.+?)(?=\n\n|\Z)", text, re.S)
    intent = intent_m.group(1).strip() if intent_m else ""
    # Truncate intent for the card view (full version on detail page)
    intent_short = intent
    if len(intent_short) > 160:
        intent_short = intent_short[:157].rsplit(" ", 1)[0] + "…"
    return {
        "title": fm.get("title", ""),
        "intent": intent_short,
        "difficulty": fm.get("difficulty", ""),
        "time_to_use": fm.get("time_to_use", ""),
        "visual": fm.get("visual", ""),
        "audience": fm.get("audience", ""),
        "best_model": fm.get("best_model", ""),
        "tags": fm.get("tags", ""),
    }


def build():
    manifest = {"pillars": []}
    for pillar_slug, pillar_title, pillar_desc, sections in PILLAR_DIRS:
        pillar = {
            "slug": pillar_slug,
            "title": pillar_title,
            "description": pillar_desc,
            "sections": []
        }
        for section_title, section_dir, slugs in sections:
            section = {"title": section_title, "prompts": []}
            for slug in slugs:
                path = f"{section_dir}/{slug}.md"
                if not Path(path).exists():
                    print(f"MISSING: {path}")
                    continue
                meta = parse_prompt(path)
                meta["slug"] = slug
                meta["path"] = path
                meta["category"] = CATEGORY.get(slug, "template")
                section["prompts"].append(meta)
            pillar["sections"].append(section)
        manifest["pillars"].append(pillar)
    out = Path("library/manifest.json")
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    n_prompts = sum(len(s["prompts"]) for p in manifest["pillars"] for s in p["sections"])
    print(f"Built manifest with {n_prompts} prompts across {len(manifest['pillars'])} pillars.")

    # Build the search index (separate file, loaded only when search opens)
    build_search_index(manifest)


# ---------------------------------------------------------------------------
# Search index
# ---------------------------------------------------------------------------

def parse_frontmatter_and_body(path):
    """Generic markdown parser: returns (frontmatter_dict, body_text)."""
    text = Path(path).read_text()
    fm = {}
    body = text
    m = re.search(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if m:
        for line in m.group(1).split("\n"):
            kv = line.split(":", 1)
            if len(kv) == 2:
                fm[kv[0].strip()] = kv[1].strip()
        body = m.group(2)
    return fm, body


def first_paragraph(body, max_chars=300):
    """First non-heading paragraph of a markdown body, truncated."""
    for chunk in body.split("\n\n"):
        chunk = chunk.strip()
        if not chunk or chunk.startswith("#"):
            continue
        # Strip simple markdown formatting for snippet
        snippet = re.sub(r"[*_`#>\[\]]", "", chunk)
        snippet = re.sub(r"\s+", " ", snippet).strip()
        if len(snippet) > max_chars:
            snippet = snippet[:max_chars-1].rsplit(" ", 1)[0] + "…"
        return snippet
    return ""


def build_search_index(manifest):
    """Generate library/search-index.json — a flat list of searchable entries
    covering prompts, tutorials, examples, and top-level docs. Loaded by the
    search UI on demand."""
    entries = []

    # Prompts (from the manifest we just built)
    for pillar in manifest["pillars"]:
        for section in pillar["sections"]:
            for p in section["prompts"]:
                entries.append({
                    "type": "prompt",
                    "title": p.get("title", ""),
                    "path": p.get("path", "").replace(".md", ""),
                    "snippet": p.get("intent", ""),
                    "pillar": pillar["slug"],
                    "section": section["title"],
                    "tags": p.get("tags", ""),
                    "difficulty": p.get("difficulty", ""),
                })

    # Worked examples
    for pillar in manifest["pillars"]:
        pillar_dir = f"library/{pillar['slug']}/examples"
        if Path(pillar_dir).exists():
            for ex_path in sorted(Path(pillar_dir).glob("*.md")):
                fm, body = parse_frontmatter_and_body(ex_path)
                entries.append({
                    "type": "example",
                    "title": fm.get("title", ex_path.stem),
                    "path": str(ex_path).replace(".md", ""),
                    "snippet": first_paragraph(body),
                    "pillar": pillar["slug"],
                    "tags": fm.get("tags", ""),
                })

    # How-to tutorials
    for tut_path in sorted(Path("docs/how-to").glob("*.md")):
        fm, body = parse_frontmatter_and_body(tut_path)
        slug = tut_path.stem
        is_index = (slug == "index")
        entries.append({
            "type": "how-to-landing" if is_index else "tutorial",
            "title": fm.get("title", slug),
            "path": str(tut_path).replace(".md", ""),
            "snippet": first_paragraph(body),
            "difficulty": fm.get("difficulty", ""),
            "category": fm.get("category", ""),
        })

    # Top-level docs (about, citation, guardrails, terms, contributors)
    for doc_path in sorted(Path("docs").glob("*.md")):
        fm, body = parse_frontmatter_and_body(doc_path)
        entries.append({
            "type": "doc",
            "title": fm.get("title", doc_path.stem),
            "path": str(doc_path).replace(".md", ""),
            "snippet": first_paragraph(body),
        })

    out = Path("library/search-index.json")
    out.write_text(json.dumps(entries, indent=2, ensure_ascii=False))
    print(f"Built search index with {len(entries)} entries → library/search-index.json")


if __name__ == "__main__":
    build()
