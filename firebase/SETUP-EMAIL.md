# Email Notifications Setup — Optional

This walkthrough enables email notifications for new comments, new submissions, and submission status changes. It is **optional** — without it, the library still works fine, and you monitor activity via the admin dashboard's pending-count badges.

## What you get with email enabled

- **You** get an email when a new comment is submitted (linked to the prompt + admin dashboard)
- **You** get an email when a new prompt submission lands (with the full submission body)
- **You** get an email when a visitor sends feedback via the floating Feedback button (with Reply-To set to their email if provided, so you can reply directly)
- **Submitters** get an email when their submission status changes (approved / rejected / needs revision)

## What it costs

- **Firebase Blaze plan upgrade required.** This sounds scary but at our scale costs ~$0/month. Blaze just means you've added a billing account; you're only charged if you exceed the free tier of each service, which we won't.
- **Resend free tier sufficient.** 100 emails/day, 3,000/month. We'll send <50/month at typical engagement.

## What it requires

- A Resend.com account (free)
- A verified sender domain on Resend (or use their default for testing)
- Firebase CLI installed locally
- ~25 minutes for first-time setup

## Step 1 — Upgrade Firebase to Blaze (~5 min)

1. Firebase Console → ⚙️ → **Usage and billing**
2. Click **Modify plan** → **Blaze (pay-as-you-go)** → **Select plan**
3. Link a Google Cloud billing account (existing or new — you'll need a credit card on file)
4. Set a **budget alert** (e.g., $5/month) so you're notified if usage ever spikes. We won't approach this number, but the alert is a safety net.

**Why this is required:** Firebase Cloud Functions only run on Blaze. The Spark (free) plan doesn't include them.

## Step 2 — Create Resend account + API key (~5 min)

1. Sign up at https://resend.com (free)
2. Verify your email
3. Go to **API Keys** → **Create API Key**
4. Name it `companion-library-prod`
5. Permission: **Sending access** (only)
6. Copy the key (starts with `re_`) — you'll paste it in Step 4

## Step 3 — Set up the sender domain (~5 min)

You have two options:

**Option A: Use Resend's default domain (fastest, for testing)**
- Use `from: notifications@onresend.dev` (or similar Resend-provided)
- No DNS setup required
- Limitation: emails come from `@onresend.dev`, which looks less professional

**Option B: Use your own domain (recommended for production)**
1. Resend dashboard → **Domains** → **Add domain** → enter your domain
2. Resend gives you DNS records (TXT, MX, CNAME) to add at your DNS provider
3. Add them; wait 5-15 min for verification
4. Once verified, you can use `from: notifications@yourdomain.com`

If you don't have a domain yet, start with Option A; switch later.

## Step 4 — Install Firebase CLI + log in (~5 min)

If not already done:

```bash
npm install -g firebase-tools
firebase login
cd ~/Projects/ai-pathology-education-companion
firebase use --add
# select your project (ai-pathology-education) and alias as "default"
```

## Step 5 — Configure the function's environment (~3 min)

The function needs three values: your Resend API key, your sender address, and your admin email.

**For the API key (secret, stored in Google Secret Manager):**

```bash
firebase functions:secrets:set RESEND_API_KEY
# paste the re_xxx key when prompted, press enter
```

**For the from-address and admin-email (non-secret env vars):**

Create `functions/.env` (NOT committed to git — `.gitignore` excludes it):

```
RESEND_FROM=notifications@yourdomain.com
ADMIN_EMAIL=youremail@yourdomain.com
SITE_URL=https://omarzbaba.github.io/AI_Pathology_Education
```

## Step 6 — Install function dependencies + deploy (~5 min)

```bash
cd functions
npm install
cd ..
firebase deploy --only functions
```

First deploy takes ~5 minutes (Google provisions a Cloud Build pipeline). Subsequent deploys are faster.

You'll see four functions deployed:
- `onCommentCreated`
- `onSubmissionCreated`
- `onFeedbackCreated`
- `onSubmissionStatusChanged`

## Step 7 — Smoke test

1. Open `/submit.html` and submit a test prompt
2. Within ~30 seconds you should receive an email at your admin address
3. Open `/admin.html`, approve the submission
4. Within ~30 seconds, the submitter address (your test email) should receive an "approved" email

If something doesn't arrive:
- Check spam/junk
- `firebase functions:log` shows function execution logs
- Resend dashboard → **Emails** shows delivery status

## Disabling later

If you want to stop notifications:

```bash
firebase functions:delete onCommentCreated
firebase functions:delete onSubmissionCreated
firebase functions:delete onFeedbackCreated
firebase functions:delete onSubmissionStatusChanged
```

Or just downgrade to Spark plan — the functions stop running automatically.

## Cost estimate at our scale

- Firebase Functions: free tier covers 2M invocations/month; we'll use <100
- Cloud Build (used during deploy only): free tier covers 120 build-min/day
- Resend: free tier covers 3,000 emails/month
- Cloud Logging: included free at our volume

**Expected monthly cost: $0**

Set the $5 budget alert anyway — defensive.

## Privacy notes

When email notifications are enabled:

- Submitter emails are forwarded to Resend's servers (US-based) for delivery
- Comment text and submission content are included in notification email bodies
- Resend retains email delivery logs per their privacy policy

Update the library's [PRIVACY.md](../PRIVACY.md) "Where it is stored" section to reflect Resend as an additional sub-processor if you enable this.
