/*
 * Firebase web app configuration.
 *
 * IMPORTANT: This file is intentionally public. The Firebase web config
 * (apiKey, authDomain, projectId, etc.) is NOT a secret — it identifies the
 * Firebase project but does not grant any privileges by itself. Security is
 * enforced by:
 *   1. Firestore security rules (firebase/firestore.rules)
 *   2. Firebase App Check with reCAPTCHA v3
 *   3. Firebase Auth (for the admin dashboard)
 *
 * Do NOT add service account keys, admin SDK credentials, or any other
 * actual secrets to this file. Those belong only in the Firebase console
 * and never in the repo.
 *
 * Values below are placeholders. Phase 3 walks through creating the Firebase
 * project and replacing them with the real config from the Firebase console.
 */

export const firebaseConfig = {
  apiKey: "REPLACE_IN_PHASE_3",
  authDomain: "REPLACE_IN_PHASE_3.firebaseapp.com",
  projectId: "REPLACE_IN_PHASE_3",
  storageBucket: "REPLACE_IN_PHASE_3.appspot.com",
  messagingSenderId: "REPLACE_IN_PHASE_3",
  appId: "REPLACE_IN_PHASE_3"
};

export const appCheckSiteKey = "REPLACE_IN_PHASE_3"; // reCAPTCHA v3 site key

export const adminUid = "REPLACE_IN_PHASE_3"; // Firebase Auth UID of the single admin user
