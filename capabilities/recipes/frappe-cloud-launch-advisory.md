---
id: frappe-cloud-launch-advisory
name: Frappe Cloud Launch Advisory
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: Frappe Cloud launch, cutover, transfer, and client handoff advice
currently_true: unknown
last_verified: 2026-05-07
tags:
  - Frappe Cloud
  - launch
  - cutover
  - client-handoff
  - ERPNext
---

## What it does

Provides a read-only/advisory launch lens for moving Built by Cameron Frappe/ERPNext client systems from Wardenclyffe/private build to Frappe Cloud or another appropriate client-owned environment.

## When to reach for it

Use when discussing:

- Frappe Cloud signup;
- production deployment;
- site transfer to client;
- custom app readiness;
- DNS/domain setup;
- live Stripe/webhook/payment readiness;
- client handoff and support access;
- cutover/go-live decisions.

## How to use it

1. Confirm source authority:
   - current project entrypoint and launch workstreams;
   - current Frappe Cloud docs/pricing/transfer docs when cost/transfer matters;
   - running local ERPNext/Frappe verifier outputs for readiness.
2. Separate advisory facts from live actions.
3. Check launch surfaces:
   - app/custom app/dependencies;
   - data/export/import/migration;
   - domains/DNS/email;
   - payments/webhooks/live-mode secrets;
   - scheduled jobs/automation index;
   - backups/rollback;
   - client ownership/support access.
4. Produce a CLEAR / FLAGS / HOLD recommendation.
5. Do not perform cloud dashboard, DNS, deploy, payment, transfer, or public actions without explicit approval.

## What it depends on

- [Frappe Deploy Safety](frappe-deploy-safety.md)
- [Frappe Payment Checkout Safety](frappe-payment-checkout-safety.md)
- [ERPNext Business Automation Index](erpnext-business-automation-index.md)
- [ERPNext Role Experience Verification](erpnext-role-experience-verification.md)
- [No Bare Claims](../principles/no-bare-claims.md)

## Failure modes

- Quoting Frappe Cloud cost/transfer facts from memory instead of live docs.
- Treating Wardenclyffe as long-term public production hosting for clients.
- Moving to cloud before forms/payments/automations fail loudly.
- Live DNS/payment/ownership actions without explicit approval.
- Broad support access to sensitive client records when limited access would do.

## Evidence

- The neutral system/user capability root documents Wardenclyffe as a private
  build/staging/template/live-demo host and finished client systems as
  candidates for Frappe Cloud or another appropriate client-owned environment.
- `C:/Users/baenb/projects/Built_by_Cameron/_CLIENTS/locally-twisted/lessons-learned.md` documents a prior Frappe Cloud pricing error and says hosting costs must be verified against the live pricing page.
- `C:/Users/baenb/projects/Built_by_Cameron/_CLIENTS/locally-twisted/PROJECT-STATUS.md` and queue entries identify Frappe Cloud cutover as a later launch phase rather than the current default local build target.
