/*
 * Access gate — handles the contact-capture form on index.html.
 * Built in Phase 3.
 *
 * Responsibilities:
 *   - Initialize Firebase App Check (reCAPTCHA v3) BEFORE any Firestore call
 *   - Validate + sanitize inputs client-side (length caps, regex, trim)
 *   - Write the submission to Firestore using serverTimestamp()
 *   - On success: set localStorage.companion_access_granted, redirect to thank-you.html
 *   - On failure: show a clear error + fallback email link
 *
 * Security notes:
 *   - This is a courtesy gate, not real access control. Library content is
 *     public on GitHub regardless.
 *   - The Firestore rule is the actual enforcement point. Client validation
 *     is defense in depth; never trust it.
 */
