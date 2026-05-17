/*
 * Admin dashboard — Firebase Auth sign-in + Firestore reads.
 * Built in Phase 3.
 *
 * Responsibilities:
 *   - Show sign-in form (Firebase Auth, email/password)
 *   - On sign-in, query the access_log collection (Firestore enforces UID match)
 *   - Render paginated table: sortable, filterable by role, searchable
 *   - CSV export button
 *   - Sign-out button + 30-minute idle auto-sign-out
 *   - Append-only banner: reminder that entries cannot be edited or deleted
 *
 * No client-side passphrase. No hardcoded admin shortcut. The Firestore
 * security rule (request.auth.uid == adminUid) is the actual gate; this
 * page is just the UX shell.
 */
