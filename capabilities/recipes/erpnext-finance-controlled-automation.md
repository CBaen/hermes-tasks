---
id: erpnext-finance-controlled-automation
name: ERPNext Finance Controlled Automation
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: ERPNext finance/payroll/reminder/bank/accounting automation guardrails
currently_true: unknown
last_verified: 2026-05-07
tags:
  - ERPNext
  - finance
  - automation
  - payroll
  - accounting
---

## What it does

ERPNext Finance Controlled Automation captures Frappe/ERPNext safety behavior from the designated read-only audit so future agents do not blend old Odoo, Claude, Codex, and current project truth.

## When to reach for it

Use before work touching this scope: ERPNext finance/payroll/reminder/bank/accounting automation guardrails.

## How to use it

1. Start with inventory, dashboards, review queues, reports, and accountant-approved cutover rules.
2. Do not auto-submit, write off, send reminders, run payroll, file taxes, sync banks, or direct-deposit without explicit approval of exact rules.
3. No live customer delivery or accounting mutation from synthetic readiness work.
4. Rows/packets must carry delivery/mutation disabled flags and blockers.

## What it depends on

- [No Bare Claims](../principles/no-bare-claims.md)
- [Current Truth Needs Evidence](../principles/current-truth-needs-evidence.md)
- [Claude Reference Library Readonly](claude-reference-library-readonly.md)

## Failure modes

- Finance automation mutates records before review.
- Customer reminder/email/payment link sent from test/readiness lane.
- Accountant/legal approval implied but not documented.

## Evidence

- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 1 lists the source files inspected for this read-only audit.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 3 documents Frappe safety patterns worth migrating.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 4 documents ERPNext project-operation patterns worth migrating.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 8 recommends `erpnext-finance-controlled-automation.md` as an OpenClaw capability card.
