/*
 * Library router — loads + renders /library/**.md into library.html.
 * Built in Phase 4.
 *
 * Responsibilities:
 *   - Read the URL hash (e.g. #/pillar-1-self-education/prompts/foo)
 *   - Fetch the corresponding .md file
 *   - Parse YAML frontmatter into a metadata card
 *   - Parse markdown body with marked.js
 *   - Sanitize the resulting HTML with DOMPurify before injecting
 *   - Add copy-to-clipboard buttons to code blocks
 *
 * Security note: DOMPurify is required. Never inject marked.js output
 * directly into the DOM — markdown can contain raw HTML that turns into
 * stored XSS if rendered unsanitized.
 */
