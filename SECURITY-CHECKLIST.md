# Security Checklist — Verification Results

Final pass through the 17 items in the original Security Checklist. Items marked **REPO** are verified in code/configuration here; items marked **CONSOLE** depend on Firebase console state that the author controls (verify after running the console walkthrough in `firebase/SETUP.md`).

| # | Item | Status | Where verified |
|---|---|---|---|
| 1 | No service account keys, `.env` files, or admin SDK code in the repo | ✓ REPO | `.gitignore` excludes them; `git log --all --full-history -- "*adminsdk*" "*.env" "*serviceAccount*"` returns no hits |
| 2 | Firebase web config is in the repo (correct — it is public) | ✓ REPO | `assets/js/firebase-config.js`, with explicit comment block explaining why this is correct |
| 3 | Firestore rules deployed and tested: anonymous create allowed only with App Check, all other ops denied | ◐ CONSOLE | Rules written in `firebase/firestore.rules`; user deploys via `firebase deploy --only firestore:rules` (Step 8 of `firebase/SETUP.md`). Smoke test in Step 9. |
| 4 | Append-only verified: update and delete denied even for admin | ◐ CONSOLE | `firestore.rules` has explicit `allow update, delete: if false;` on the `access_log` collection. Smoke Test D in `firebase/SETUP.md` confirms via the Firebase console UI. |
| 5 | Document shape validation tested with a malformed payload | ◐ CONSOLE | `isValidAccessLogPayload()` helper in `firestore.rules` enforces required keys, length caps, role enum, server-set timestamp. Smoke Test B in `firebase/SETUP.md`. |
| 6 | App Check enforcement ON for Firestore in the Firebase console | ◐ CONSOLE | Step 5 of `firebase/SETUP.md` walks through enabling reCAPTCHA v3 + flipping enforcement to ON. **This is the most-skipped step — do not skip it.** |
| 7 | Authorized Domains for Auth restricted to localhost + production domain(s) | ◐ CONSOLE | Step 6 of `firebase/SETUP.md`. After GitHub Pages is live, also re-verify per Step 3 of `DEPLOY.md`. |
| 8 | Admin dashboard requires Firebase Auth sign-in; no client-side passphrase anywhere | ✓ REPO | `admin.js` uses `signInWithEmailAndPassword`; `firestore.rules` enforces `request.auth.uid == ADMIN_UID`. Grep for "passphrase" returns no hits. |
| 9 | CSP meta tag present on all HTML pages | ✓ REPO | All five HTML pages have a `<meta http-equiv="Content-Security-Policy">` tag. Firebase-aware on `index.html` + `admin.html`; tight `'self'`-only on the other three. |
| 10 | SRI hashes on all vendored JS | ✓ REPO | `library.html` loads `marked.min.js` and `dompurify.min.js` with `integrity="sha384-..."` and `crossorigin="anonymous"`. |
| 11 | All fonts self-hosted; no external font CDN | ✓ REPO | `styles.css` `@font-face` declarations point to `/assets/fonts/`. No `fonts.googleapis.com` or `fonts.gstatic.com` references in any HTML or CSS. |
| 12 | No analytics, tracking pixels, or third-party tags | ✓ REPO | Grep across all HTML pages for `analytics`, `gtag`, `googletagmanager`, `facebook`, `pixel`, `clarity`, `hotjar`, `segment`: zero matches. |
| 13 | DOMPurify sanitizes all rendered markdown before injection | ✓ REPO | `library-router.js` calls `window.DOMPurify.sanitize(rawHtml, ...)` between `marked.parse()` and `innerHTML` injection. |
| 14 | Input length caps enforced both client-side and in Firestore rules | ✓ REPO | Client: `sanitizeString(value, maxLen)` in `access-gate.js` + `maxlength` HTML attributes. Server: `data.X.size() <= N` checks in `firestore.rules`. |
| 15 | PRIVACY.md linked from the access form and the footer | ✓ REPO | `index.html` form has `<a href="PRIVACY.md">full privacy notice</a>`; footer has `<a href="PRIVACY.md">Privacy</a>`. |
| 16 | GitHub branch protection on `main` | ◐ EXTERNAL | Step 4 of `DEPLOY.md`. Not enforceable from the repo itself. |
| 17 | Firestore export procedure documented in maintenance README | ✓ REPO | `README.md` § "Archive the access log to Cloud Storage" documents the `gcloud firestore export` command. |

## Additional defensive measures added beyond the original checklist

- **App Check rejection of direct-config-scraping bots.** Even if someone copies the public Firebase config from `firebase-config.js`, they cannot write to Firestore because App Check requires a valid reCAPTCHA v3 token. Smoke Test B in `firebase/SETUP.md` verifies this.
- **Path traversal defense in the markdown router.** `library-router.js` `parseHash()` rejects path segments that aren't `[A-Za-z0-9_\-]` and strips `..` segments, preventing requests for paths outside the served tree.
- **Admin UID double-check.** Even though Firestore rules block non-admin reads, `admin.js` also checks `user.uid === adminUid` client-side and force-signs-out any authenticated user whose UID doesn't match. Belt and braces.
- **HTML escaping on rendered admin data.** `admin.js` `escapeHtml()` is applied to every value rendered into the dashboard table, preventing stored XSS if a malformed entry ever made it past validation.
- **Idle auto-sign-out.** 30-minute idle timer in `admin.js`. Reduces window if the dashboard tab is left open and the workstation walked away from.
- **Append-only enforcement at the rule layer.** Even the admin cannot edit or delete log entries. Prevents accidental wipes, prevents post-hoc tampering with research evidence, prevents an attacker who somehow obtained admin credentials from covering their tracks.
- **noindex/nofollow on `thank-you.html`, `library.html`, `admin.html`.** Search engines won't surface these pages. Library content is still public on GitHub, but the deployed instances aren't indexed.
- **No inline scripts anywhere.** The greeting script that was originally inline in `thank-you.html` was extracted to `assets/js/greeting.js`. This means CSP `script-src` can stay strict — no `'unsafe-inline'` for scripts on any page.

## Pre-launch checklist

Before sharing the QR code at the workshop, complete these steps in order:

- [ ] **CONSOLE:** Walk through `firebase/SETUP.md` end to end (~20 min) — items 3, 4, 5, 6, 7 above
- [ ] **DEPLOY:** Walk through `DEPLOY.md` Steps 1–5 (~30 min) — Pages live, Firebase wired, authorized domains updated, branch protection on, QR code generated
- [ ] **TEST:** Submit the access form as yourself. Verify a Firestore entry appears with the correct timestamp.
- [ ] **TEST:** Sign into the admin dashboard. Export a CSV. Verify the entry is there.
- [ ] **TEST:** Open the live site on your phone. Verify the layout works at mobile width.
- [ ] **TEST:** Try to read `access_log` from the browser console while signed out — should get permission denied (Smoke Test C in `firebase/SETUP.md`).
- [ ] **TEST:** Try to edit a Firestore document from the Firebase console UI while signed in — should be rejected by append-only rule (Smoke Test D).
- [ ] **PRINT:** Drop the generated QR code into the workshop's final slide. Print at slide size. Scan it with your own phone to confirm it resolves to the live URL.

When all eight boxes are checked, the site is launch-ready.
