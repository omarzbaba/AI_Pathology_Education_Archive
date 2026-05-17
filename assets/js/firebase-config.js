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
 */

export const firebaseConfig = {
  apiKey:            "AIzaSyA304rce7Us1SPa6Pj-cQ2D4IlDKFdcM4Q",
  authDomain:        "ai-pathology-education.firebaseapp.com",
  projectId:         "ai-pathology-education",
  storageBucket:     "ai-pathology-education.firebasestorage.app",
  messagingSenderId: "17132018749",
  appId:             "1:17132018749:web:58c445df667cd2d9395e54"
};

// reCAPTCHA v3 site key (public — secret key stays at Google)
export const appCheckSiteKey = "6LcVHe8sAAAAADtOP39wY-tt109ZxVBXvVnHo4hY";

// Firebase Auth UID of the single admin user
export const adminUid = "gXIEl0ajRzfXHgUye54WvemBf642";
