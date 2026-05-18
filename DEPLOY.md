# Deployment Walkthrough

The code is complete and pushed. This document gets the site live, the backend operational, and the QR code printed. Roughly 60 minutes end to end, split between GitHub, Firebase, and the terminal.

You can complete the steps in any order, but the recommended sequence is GitHub Pages → Firebase → QR code. GitHub Pages is the fastest win and gives you a live URL to use everywhere else.

---

## 1. Enable GitHub Pages (~5 minutes)

1. Open https://github.com/omarzbaba/AI_Pathology_Education
2. Click **Settings** → **Pages** (left sidebar, under "Code and automation")
3. Under **Build and deployment**:
   - Source: **Deploy from a branch**
   - Branch: **main** (the only branch)
   - Folder: **/ (root)**
4. Click **Save**
5. Wait 1–2 minutes. The page will refresh and show: *Your site is live at https://omarzbaba.github.io/AI_Pathology_Education/*
6. Open that URL — you should see the masthead, the three-pillar grid, and the access form

**The site is live, but the form won't work yet** because Firebase isn't configured. That's the next step.

---

## 2. Run the Firebase console walkthrough (~20 minutes)

Open [`firebase/SETUP.md`](firebase/SETUP.md) and walk through it. It is a 9-step process covering:

- Create the Firebase project
- Register the web app and copy the config
- Enable Firestore
- Enable Auth and create your admin user (copy the UID)
- Enable App Check + reCAPTCHA v3
- Lock the authorized domains
- Paste the config into `assets/js/firebase-config.js`
- Paste the admin UID into `firebase/firestore.rules` and deploy
- Smoke tests

When you finish, commit and push the two updated files:

```bash
cd ~/Projects/ai-pathology-education-companion
git add assets/js/firebase-config.js firebase/firestore.rules
git commit -m "Phase 3 (console): live Firebase config + admin UID"
git push
```

GitHub Pages will redeploy automatically in ~1 minute. Refresh the live URL, submit the form as a test, then sign into the admin dashboard and verify you see the entry.

---

## 3. Add the GitHub Pages URL to reCAPTCHA + Firebase authorized domains (~3 minutes)

This is the small but important detail people forget. The site is live at `omarzbaba.github.io/AI_Pathology_Education/`, but if you set up Firebase with only `localhost` in the authorized lists, form submissions from the live site will be rejected.

1. **reCAPTCHA console** (https://www.google.com/recaptcha/admin) → your site key → Settings → Domains. Add `omarzbaba.github.io`. Save.
2. **Firebase console** → Authentication → Settings → Authorized domains. Confirm `omarzbaba.github.io` is in the list (Firebase often auto-adds it but verify).
3. Hard-refresh the live site (`Cmd+Shift+R` on macOS). Submit the form. Verify the entry appears in the admin dashboard.

---

## 4. Lock down GitHub (~3 minutes)

1. **Settings → Branches → Add classic branch protection rule** for `main`:
   - Require a pull request before merging (uncheck "Require approvals" if you're solo)
   - Do not allow force pushes
   - Do not allow deletions
2. Click **Save changes**
3. **Settings → Code security → Secret scanning**: enable (free for public repos)
4. **Settings → Code security → Push protection**: enable

These don't change day-to-day work for a solo author, but they prevent accidents — the kind of accidents that take down a live workshop URL the night before the event.

---

## 4b. Re-deploy Firestore rules after Phase B + C1 (~1 minute)

Phase B added the `prompt_submissions` collection. Phase C1 added the `comments` and `votes` collections. The Firestore rules need to be re-deployed so the new collections are gated correctly.

**Option A — paste in console (fastest):**
1. Firebase console → Firestore Database → Rules tab
2. Select-all and delete the existing text
3. Paste the current contents of `firebase/firestore.rules` (now includes the `prompt_submissions` block)
4. Click **Publish** → confirm

**Option B — Firebase CLI:** `firebase deploy --only firestore:rules`

After deploy, smoke-test by submitting a prompt at `/submit.html` and confirming it lands in the Firestore console under the `prompt_submissions` collection.

---

## 5. Generate the QR code for the workshop slide (~5 minutes)

Two options. Pick whichever is easier:

**Option A — qrencode CLI (macOS/Linux):**

```bash
brew install qrencode    # macOS, one-time
cd ~/Projects/ai-pathology-education-companion
bash scripts/generate-qr.sh https://omarzbaba.github.io/AI_Pathology_Education/
```

**Option B — Python:**

```bash
pip install "qrcode[pil]"    # one-time
cd ~/Projects/ai-pathology-education-companion
python3 scripts/generate-qr.py https://omarzbaba.github.io/AI_Pathology_Education/
```

Either path produces `assets/img/companion-qr.png` — a 1000×1000 PNG with error-correction level H (survives partial occlusion / printing imperfection). Drop it into the final slide of the workshop deck.

Commit and push the QR (it doesn't change unless the URL changes):

```bash
git add assets/img/companion-qr.png
git commit -m "Phase 6: add QR code for workshop slide"
git push
```

---

## 6. (Optional) Custom domain (~15 minutes if you want it)

The default URL `omarzbaba.github.io/AI_Pathology_Education/` is fine. If you want a custom domain (e.g., `aipatholgyeducation.org`):

1. Buy the domain through a registrar (Namecheap, Cloudflare, etc.)
2. At the registrar, add CNAME records pointing to `omarzbaba.github.io`
3. GitHub → repo Settings → Pages → Custom domain. Enter the domain, save.
4. Wait 15–30 minutes for DNS propagation
5. Enable "Enforce HTTPS" once the certificate provisions

If you go this route, remember to update:
- The reCAPTCHA authorized domains (add the custom domain)
- The Firebase authorized domains (add the custom domain)
- `LICENSE` (the suggested attribution URL)
- `docs/citation.md` (all the citation URL fields)
- Regenerate the QR code with the new URL and re-commit

---

## 7. Self-host the fonts (~2 minutes, optional polish)

The site uses system-font fallbacks and looks fine, but the design is sharper with the custom fonts in place:

```bash
cd ~/Projects/ai-pathology-education-companion/assets/fonts
bash download-fonts.sh
cd ../..
git add assets/fonts/*.woff2
git commit -m "Phase 6: vendored WOFF2 font files for self-hosting"
git push
```

---

## Done

The site is live, the backend is enforced, the access log writes, the QR code is printable, and the repo is locked. Phase 6 complete.

Phase 7 is the final piece — the maintenance README that future-you (or a successor) will read to keep this thing running.

---

## Troubleshooting

**Form submission fails with App Check error.** Check that the live domain is in the reCAPTCHA v3 authorized domains list. Hard-refresh after adding.

**Admin dashboard shows "Sign-in failed: auth/invalid-credential".** Triple-check the admin email + password in the Firebase console. Reset the password if needed.

**Admin dashboard signs in but shows "Failed to load: Missing or insufficient permissions".** The `ADMIN_UID` in `firestore.rules` doesn't match the UID of the account you signed in with. Update the rules file, redeploy with `firebase deploy --only firestore:rules`, sign out and back in.

**Library pages show "That document could not be found (404)".** The hash routing expects paths from repo root, e.g. `library.html#/library/pillar-1-self-education/index`. Check the link you clicked or typed.

**Fonts look wrong.** Either the system fallback is rendering (fine, ignore) or the WOFF2 files were downloaded but their MIME type isn't being served — GitHub Pages handles WOFF2 correctly by default, so this is unusual. Open dev tools, Network tab, find the .woff2 request, check the status.
