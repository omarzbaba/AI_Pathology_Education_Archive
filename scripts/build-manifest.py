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
        ]),
        ("Reading the literature", "library/pillar-1-self-education/prompts", [
            "paper-summarization","paper-methods-critique","journal-club-preread",
        ]),
        ("Multimodal", "library/pillar-1-self-education/prompts", [
            "multimodal-photomicrograph","multimodal-spep-ife",
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
        ]),
        ("Written feedback & narrative", "library/pillar-2-teaching/prompts", [
            "resident-feedback-note","ccc-narrative-comment","lor-starting-draft",
        ]),
        ("Discussion-based formats", "library/pillar-2-teaching/prompts", [
            "journal-club-discussion-q","tumor-board-presentation","resident-as-teacher",
        ]),
    ]),
    ("pillar-3-educational-operations", "Educational Operations & Documentation", "Using AI to produce the artifacts around teaching events", [
        ("Workshops", "library/pillar-3-educational-operations/prompts/workshops", [
            "announcement-registration","pre-workshop-survey","facilitator-runofshow","station-by-station-guide",
            "badge-design-spec","access-card-layout","certificate-of-completion","post-workshop-thank-you","faculty-feedback-summary",
        ]),
        ("Rotations", "library/pillar-3-educational-operations/prompts/rotations", [
            "orientation-onepager","expectations-doc","reading-list","daily-schedule",
            "evaluation-rubric","mid-rotation-feedback","end-of-rotation-evaluation","resident-to-resident-handoff",
        ]),
        ("Courses", "library/pillar-3-educational-operations/prompts/courses", [
            "syllabus","weekly-module-packet","assignment-grading-rubric","feedback-collection-form","course-postmortem",
        ]),
        ("Conferences & journal clubs", "library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs", [
            "journal-club-packet","tumor-board-case-packet","grand-rounds-speaker-prep","conference-schedule","qa-prep-doc",
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


if __name__ == "__main__":
    build()
