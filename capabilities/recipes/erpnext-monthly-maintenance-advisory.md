---
id: erpnext-monthly-maintenance-advisory
name: ERPNext Monthly Maintenance Advisory
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: monthly maintenance and review cadence for ERPNext/Frappe client systems
currently_true: unknown
last_verified: 2026-05-07
tags:
  - ERPNext
  - maintenance
  - monthly
  - finance
  - client-ops
---

## What it does

Turns monthly ERPNext/Frappe maintenance into an advisory checklist/report instead of silent background automation or risky live changes.

## When to reach for it

Use for monthly/recurring review of client systems, especially:

- finance/reconciliation;
- unpaid invoices/review packets;
- checkout/payment readiness;
- forms/intake/CRM pipeline;
- business automation index;
- scheduler health;
- backups/updates/Frappe Cloud status;
- user/role/access review.

## How to use it

1. Load the client/project authority files and approved monthly checklist.
2. Run/read safe verifier scripts where available.
3. Mark each item:
   - PASS with witness;
   - FAIL with exact issue;
   - BLOCKED with needed input/access;
   - UNVERIFIED when not checked.
4. Keep live-risk actions advisory unless approved:
   - no customer reminders/emails;
   - no accounting submission/mutation;
   - no payroll/tax/bank sync;
   - no deploy or provider changes.
5. Produce a short report with blockers, approvals needed, and safe next actions.

## Starter monthly checklist

Adapt per client before operational use:

- Import/review bank or payout statements.
- Match Stripe deposits, fees, refunds, and adjustments.
- Match supplier/vendor payments.
- Review unmatched transactions.
- Reconcile bank account.
- Save accountant review reports.
- Run/read business automation index.
- Check forms/intake/CRM pipeline failures.
- Check payment/checkout/paperwork verifiers.
- Check scheduler/automation health.
- Review backups/update status/Frappe Cloud status.
- Review users/roles/support access.

## What it depends on

- [ERPNext Business Automation Index](erpnext-business-automation-index.md)
- [ERPNext Finance Controlled Automation](erpnext-finance-controlled-automation.md)
- [Frappe Payment Checkout Safety](frappe-payment-checkout-safety.md)
- [ERPNext Role Experience Verification](erpnext-role-experience-verification.md)
- [No Bare Claims](../principles/no-bare-claims.md)

## Failure modes

- Monthly maintenance sends customer reminders or mutates finance records without approval.
- Bank/payroll/tax/provider credentials are requested casually.
- Unchecked items are marked green.
- Report hides blockers behind “looks okay.”
- Maintenance requires broad client-data access when a limited report would do.

## Evidence

- `C:/Users/baenb/projects/Built_by_Cameron/_CLIENTS/locally-twisted/workstreams/finance-payroll-quickbooks-migration.md` includes a monthly checklist for bank/payout import, Stripe deposit/fee/refund matching, supplier/vendor payment matching, unmatched transaction review, reconciliation, and accountant reports.
- `C:/Users/baenb/projects/Built_by_Cameron/_CLIENTS/locally-twisted/locally-twisted-decisions.md` documents the decision that ERPNext backend automation must be indexed/scheduled before Frappe Cloud trust.
- `FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` recommends finance controlled automation, no-live customer reminders, and automation-index guardrails before trusting ERPNext business operations.
