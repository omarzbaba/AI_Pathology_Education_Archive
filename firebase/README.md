# Firebase configuration

This directory holds Firebase configuration that lives in source control:

- `firestore.rules` — security rules for the `access_log` collection

Operational artifacts that should **never** be committed:

- Firebase Admin SDK service account keys (`*-firebase-adminsdk-*.json`)
- `.env` files containing secrets
- `firebase-debug.log`

These are excluded by the repo `.gitignore`.

## Deploying rules (after Phase 3 setup)

```
npm install -g firebase-tools
firebase login
firebase use [project-id]
firebase deploy --only firestore:rules
```

Phase 3 walks through Firebase project creation, App Check enablement, admin user creation, and rule deployment in detail.
