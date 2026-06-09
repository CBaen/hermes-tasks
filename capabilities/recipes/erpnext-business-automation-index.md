---
id: erpnext-business-automation-index
name: ERPNext Business Automation Index
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: ERPNext operational readiness map for automations/templates/documents
currently_true: unknown
last_verified: 2026-05-07
tags:
  - ERPNext
  - automation
  - readiness
  - fail-loud
---

## What it does

ERPNext Business Automation Index captures Frappe/ERPNext safety behavior from the designated read-only audit so future agents do not blend old Odoo, Claude, Codex, and current project truth.

## When to reach for it

Use before work touching this scope: ERPNext operational readiness map for automations/templates/documents.

## How to use it

1. DocTypes/templates do not equal operational readiness.
2. Track surfaces as connected, disconnected, required-missing, useful-missing, fake-data, or loud-failure.
3. Use the index to prevent fake readiness in documents, reminders, reports, customer messages, and workflows.
4. Each automation needs owner, trigger, downstream effect, verification, and disabled/fake-data status when applicable.

## What it depends on

- [No Bare Claims](../principles/no-bare-claims.md)
- [Current Truth Needs Evidence](../principles/current-truth-needs-evidence.md)
- [Claude Reference Library Readonly](claude-reference-library-readonly.md)

## Failure modes

- Feature exists as DocType/template but has no safe trigger/path.
- Reminder/report/document silently fails or sends unexpectedly.
- Fake-data readiness confused with live readiness.

## Evidence

- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 1 lists the source files inspected for this read-only audit.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 3 documents Frappe safety patterns worth migrating.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 4 documents ERPNext project-operation patterns worth migrating.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 8 recommends `erpnext-business-automation-index.md` as an OpenClaw capability card.
