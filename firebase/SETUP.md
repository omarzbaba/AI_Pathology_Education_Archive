# Firebase Setup — Step-by-Step Console Walkthrough

The code in this repo is fully written, but it can't do anything until you create the Firebase project, enable the right services, and paste three values back into the repo. This walkthrough takes ~20 minutes start to finish.

You will end up with:

- A Firebase project that hosts a single Firestore collection (`access_log`)
- Email/password auth with exactly one admin user (you)
- App Check + reCAPTCHA v3 protecting Firestore writes from bots
- Security rules that enforce append-only writes and admin-only reads
- Three values pasted into `assets/js/firebase-config.js` and one into `firebase/firestore.rules`

You'll need a Google account.

---

## 1. Create the Firebase project (~3 min)

1. Go to https://console.firebase.google.com/
2. Click **Add project**
3. Name it something like `ai-pathology-education` (the slug becomes your project ID — write it down)
4. Disable Google Analytics for this project — you don't need it, and skipping it avoids creating a linked GA property
5. Click **Create project**, wait ~30 seconds, then **Continue**

---

## 2. Register the web app (~2 min)

1. On the project home, click the **`</>`** (web) icon to add a web app
2. Nickname it `companion-site`
3. **Do not** check "Also set up Firebase Hosting" — we're using GitHub Pages
4. Click **Register app**
5. You'll see a code block with a `firebaseConfig` object. **Copy it** — you'll paste these values in Step 7.
6. Click **Continue to console**

---

## 3. Enable Firestore (~3 min)

1. Left sidebar → **Build → Firestore Database**
2. Click **Create database**
3. **Start in production mode** (not test mode — we'll deploy strict rules in Step 8)
4. Choose a location: pick **`us-east1`** (South Carolina) or **`us-central1`** (Iowa) — closest to you/the API Summit audience. **This is permanent**, you can't change it later for this project.
5. Click **Create**, wait ~30 seconds

---

## 4. Enable Authentication and create the admin user (~3 min)

1. Left sidebar → **Build → Authentication**
2. Click **Get started**
3. Under **Sign-in method**, click **Email/Password**
4. Toggle **Enable** on (leave "Email link" off)
5. Click **Save**
6. Go to the **Users** tab → **Add user**
7. Enter your professional email and a **strong, unique password** (use a password manager — this is the only credential standing between someone with the URL and your access log)
8. Click **Add user**
9. The user list now shows your account with a **User UID** column. **Copy that UID** — it's a ~28-character string. You'll paste it in Steps 7 and 8.

---

## 5. Enable App Check with reCAPTCHA v3 (~5 min)

This is the step that stops bots from spamming your access log.

1. Left sidebar → **Build → App Check**
2. Click your web app (`companion-site`) → **Register**
3. Choose **reCAPTCHA v3** as the provider
4. Open https://www.google.com/recaptcha/admin/create in a new tab
5. Label: `ai-pathology-education-companion`
6. reCAPTCHA type: **v3**
7. Domains: add `localhost`, your `*.github.io` domain (you'll know it after Phase 6), and any custom domain you plan to use. You can edit this list later — for now add what you know.
8. Accept terms, click **Submit**
9. Copy the **Site key** (NOT the secret key — the secret stays on Google's side)
10. Paste the site key into the Firebase App Check registration dialog
11. Click **Save**
12. Back on the App Check page, click the **Firestore** product → **Enforce**
13. Confirm — this rejects all Firestore requests that don't carry a valid App Check token

> **Critical:** until you complete Step 12, App Check is in "monitor" mode and won't block bad requests. Don't skip it.

---

## 6. Lock down authorized domains (~1 min)

1. Authentication → **Settings → Authorized domains**
2. Make sure only these are listed: `localhost`, your `*.github.io` domain, and any custom domain
3. Remove anything else you don't recognize

---

## 7. Paste the config into the repo (~2 min)

Open `assets/js/firebase-config.js` and replace the placeholder block with the real values:

```js
export const firebaseConfig = {
  apiKey:            "...",      // from Step 2
  authDomain:        "...",      // from Step 2
  projectId:         "...",      // from Step 2
  storageBucket:     "...",      // from Step 2
  messagingSenderId: "...",      // from Step 2
  appId:             "..."       // from Step 2
};

export const appCheckSiteKey = "...";   // reCAPTCHA v3 site key from Step 5
export const adminUid        = "...";   // admin User UID from Step 4
```

**Remember:** these values are public. They are meant to be in the repo. Security comes from the rules + App Check + Auth, not from hiding the config.

---

## 8. Update and deploy the Firestore rules (~3 min)

Open `firebase/firestore.rules`. Find the line:

```
&& request.auth.uid == 'REPLACE_ADMIN_UID';
```

Replace `REPLACE_ADMIN_UID` with the User UID from Step 4 (the same one you put in `firebase-config.js`).

Install the Firebase CLI if you don't have it:

```bash
npm install -g firebase-tools
```

Log in and link the project:

```bash
firebase login
cd ~/Projects/ai-pathology-education-companion
firebase use --add
# pick the project you created, alias it "default"
```

Deploy the rules:

```bash
firebase deploy --only firestore:rules
```

You should see `+  cloud.firestore: released rules ... to cloud.firestore` and no errors.

---

## 9. Smoke tests (~5 min)

Run these before declaring Phase 3 done.

**Test A — happy path write.** Open the site (locally with `python3 -m http.server` or your live URL), fill out the form, submit. Open the Firestore console — you should see a new document in `access_log` with a server timestamp.

**Test B — direct write without App Check is rejected.** Open the browser console on a page where Firebase isn't initialized. Paste a fetch call to the Firestore REST API trying to create a doc. Expect a 403/permission-denied. (Detailed script in `firebase/TESTS.md` — you can write this later; for now the manual happy-path test is enough.)

**Test C — admin read while signed out is rejected.** Open `admin.html` without signing in. Open the browser console. The query in `admin.js` only runs after sign-in, but you can manually fire one — expect permission-denied.

**Test D — append-only.** In the Firestore console, try to edit a field on an existing `access_log` document. Click Save. Expect a Permission Denied error (this proves the rule prevents updates even from the Firebase web console when authenticated as the admin).

**Test E — admin sign-in.** Open `admin.html`, sign in with your admin credentials, see the dashboard load with your test entry from Test A.

---

## What's NOT in this walkthrough (intentional)

- Firebase Hosting — we use GitHub Pages
- Cloud Functions — not needed, the architecture is fully client-side
- Storage — no file uploads
- Cloud Messaging, Crashlytics, Performance Monitoring, Remote Config — not needed
- Analytics — explicitly avoided (privacy)

If the Firebase console shows you offers to enable any of these, decline. Smaller surface area = smaller attack surface.

---

## After setup is done

Commit the updated `firebase-config.js` and `firestore.rules` to the repo:

```bash
cd ~/Projects/ai-pathology-education-companion
git add assets/js/firebase-config.js firebase/firestore.rules
git commit -m "Phase 3: live Firebase config + admin UID"
git push
```

The config values are safe to commit. The rules become the source of truth for what the deployed Firestore project allows — if you ever change them, redeploy with `firebase deploy --only firestore:rules`.
