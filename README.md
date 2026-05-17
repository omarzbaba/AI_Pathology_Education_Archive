# AI in Pathology Education — Companion Library

Companion website for the API Summit 2026 workshop *AI in Pathology Education: A Practical Framework Across Learning, Teaching, and Educational Operations*, by Omar Z. Baba, MD (Henry Ford Health, Department of Pathology, Clinical Pathology & Informatics).

A curated prompt library and worked-example collection organized around three pillars:

1. **Self-Education** — using AI to learn pathology
2. **Teaching** — using AI to teach pathology to others
3. **Educational Operations & Documentation** — using AI to produce the artifacts around teaching events

Hosted on GitHub Pages. Access form and admin dashboard backed by Firebase (Firestore + Auth + App Check). Licensed under [CC BY 4.0](LICENSE).

**Live URL:** https://omarzbaba.github.io/AI_Pathology_Education/

---

## Quick links

- [Live site](https://omarzbaba.github.io/AI_Pathology_Education/)
- [Privacy notice](PRIVACY.md)
- [Deployment walkthrough](DEPLOY.md) — get the site live and the backend wired
- [Firebase setup walkthrough](firebase/SETUP.md) — 9-step console walkthrough (~20 min)

---

## Repo layout

```
.
├── index.html                landing page with access form
├── thank-you.html            library home (post sign-in)
├── library.html              markdown viewer shell
├── admin.html                Firebase-Auth-gated admin dashboard
├── 404.html                  styled not-found page
├── assets/
│   ├── css/styles.css        full design system (navy + burgundy + white)
│   ├── js/                   firebase-config, access-gate, library-router, admin, greeting
│   ├── vendor/               marked + DOMPurify with SRI hashes
│   ├── fonts/                self-hosted WOFF2 fonts + download-fonts.sh
│   └── img/                  headshot, logos, generated QR code
├── library/                  the actual prompt library
│   ├── pillar-1-self-education/
│   ├── pillar-2-teaching/
│   └── pillar-3-educational-operations/
│       └── companion-app-builder/  the headline reusable artifact
├── docs/                     about, how-to-use, guardrails, citation
├── firebase/                 firestore.rules + SETUP.md walkthrough
├── scripts/                  generate-qr.sh, generate-qr.py
├── PRIVACY.md                privacy notice (linked from form + footer)
├── DEPLOY.md                 7-step deployment walkthrough
├── LICENSE                   CC-BY-4.0
└── README.md                 you are here
```

---

## Daily maintenance — adding new content

### Add a new prompt to an existing pillar

1. Pick the right directory: `library/pillar-X-Y/prompts/` (and the right subdirectory if it's Pillar 3)
2. Copy the frontmatter from an existing prompt file as a template
3. Update `title`, `pillar`, `audience`, `difficulty`, `time_to_use`, `tags`, `verified_models`, `last_updated`
4. Fill in the seven sections: What this prompt does, When to use it, The prompt, Expected output, Common failure modes, Required human verification, Worked example (optional)
5. Add a link to the new prompt in the relevant pillar's `index.md`
6. Commit and push — GitHub Pages redeploys in ~1 minute

### Add a worked example

1. Drop the file in `library/pillar-X-Y/examples/`
2. Use the same seven-section structure as a prompt, but the body should be the actual transcript / before-after / annotation content
3. Link from the relevant pillar's `index.md` and (if relevant) from the prompt file that the example demonstrates

### Update a pillar overview

Edit `library/pillar-X-Y/index.md` and push. The markdown viewer picks up the new content immediately on next page load.

### Update the documentation pages

Edit any of `docs/*.md` or `PRIVACY.md` and push. The `last_updated` field in the frontmatter should be bumped manually.

---

## Operational tasks

### Export the access log

Sign into [admin.html](https://omarzbaba.github.io/AI_Pathology_Education/admin.html) with your Firebase Auth credentials. Use the **Export CSV** button. The exported file is named `access_log_YYYY-MM-DD.csv` and contains all visible rows (filter first if you want a subset).

For the manuscript, periodic exports should be saved with the manuscript working files.

### Archive the access log to Cloud Storage (Firestore export)

For tamper-resistant backups, periodically run a Firestore export to Cloud Storage:

```bash
gcloud firestore export gs://[YOUR-BUCKET-NAME]/exports/$(date +%Y-%m-%d)
```

You'll need a Cloud Storage bucket in the same project. One-time setup: `gcloud storage buckets create gs://[BUCKET-NAME] --location=us-central1` (or your Firestore region). Schedule the export monthly via Cloud Scheduler if desired.

### Revoke the admin account

Firebase console → Authentication → Users → select your account → three-dot menu → **Disable account** (or Delete). The dashboard immediately becomes inaccessible. The log entries themselves are unaffected.

### Switch the access log to fully read-only (post-manuscript)

When the manuscript work is complete and you want to lock the log against any further writes:

Edit `firebase/firestore.rules`. Change the `access_log` create rule:

```
allow create: if false;    // was: if isValidAccessLogPayload();
```

Deploy: `firebase deploy --only firestore:rules`. The log is now fully frozen — no writes, no updates, no deletes, only admin reads.

### Add a new admin (e.g., handoff to a successor)

1. Firebase console → Authentication → Users → Add user with the successor's email
2. Note their UID
3. Edit `firebase/firestore.rules` — change `isAdmin()` to allow multiple UIDs:

   ```
   function isAdmin() {
     return request.auth != null
       && request.auth.uid in [
         'YOUR_UID',
         'SUCCESSOR_UID'
       ];
   }
   ```

4. Deploy the rules
5. Have the successor sign into `admin.html` and verify they see the dashboard

When fully transitioning ownership, remove your UID from the list and deploy again.

### Roll back a broken deployment

GitHub Pages serves whatever is on `main`. To roll back:

```bash
cd ~/Projects/ai-pathology-education-companion
git log --oneline -10                       # find the good commit
git revert <bad-commit-sha>                 # safer than reset
git push
```

Pages redeploys in ~1 minute. Site is back.

If you absolutely need to reset (e.g., a secret was committed):

```bash
git reset --hard <good-commit-sha>
git push --force-with-lease
```

But avoid this unless necessary. `git revert` is reversible; `git push --force` is not.

### Update the version stamp / last-updated date

The site doesn't surface a global version, but each markdown file has `last_updated` in its frontmatter. Update the file you changed, plus root `PRIVACY.md` and `docs/*.md` if those changed.

---

## Where things live

| Concern | Location |
|---|---|
| Branding / colors / fonts | `assets/css/styles.css` (CSS variables in `:root`) |
| Site title / event name | Edit each HTML file's `<title>` and masthead block |
| Privacy text | `PRIVACY.md` |
| Form fields and validation | `index.html` (markup) + `assets/js/access-gate.js` (logic) + `firebase/firestore.rules` (server-side validation) |
| Admin dashboard layout | `assets/js/admin.js` |
| Firestore security rules | `firebase/firestore.rules` |
| Firebase web config | `assets/js/firebase-config.js` (public; safe to commit) |
| Vendored libs (marked, DOMPurify) | `assets/vendor/` with SRI hashes in `library.html` |
| QR code | `assets/img/companion-qr.png` (generated by `scripts/generate-qr.{sh,py}`) |

---

## Where things do NOT live

Things that are intentionally outside this repo:

- **Firebase Admin SDK service account keys** — never. The repo has zero server-side credentials. The only Firebase secret is your admin user's password, which lives in your password manager.
- **Patient data of any kind** — see [guardrails](docs/guardrails.md).
- **Pre-built JS bundles or transpilation output** — the site is vanilla HTML/CSS/JS; what's in the repo is what runs in the browser.
- **Analytics scripts, tracking pixels, marketing tags** — by design.

---

## Ownership and handoff

Current owner: Omar Z. Baba, MD (omarzbaba on GitHub). Firebase project lives in his Google account. Admin user is the only one with read access to the access log.

If ownership transfers:

1. Add the new owner as a collaborator on the GitHub repo (Settings → Collaborators)
2. Transfer ownership of the Firebase project (Firebase console → Project Settings → Users and permissions → transfer)
3. Add the new owner as an admin user (see "Add a new admin" above)
4. Update `LICENSE` and citation files with the new contact
5. Update the Henry Ford Health institutional affiliation if the new owner is elsewhere
6. Push the changes

---

## License

[CC BY 4.0](LICENSE). Share and adapt with attribution.

Suggested citation:

> Baba OZ (2026). *AI in Pathology Education — Companion Library*. API Summit 2026. https://github.com/omarzbaba/AI_Pathology_Education

See [docs/citation.md](docs/citation.md) for formatted variants and how to cite specific prompts.
