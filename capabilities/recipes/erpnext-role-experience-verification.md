---
id: erpnext-role-experience-verification
name: ERPNext Role Experience Verification
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: ERPNext non-admin user/role/workspace verification
currently_true: unknown
last_verified: 2026-05-07
tags:
  - ERPNext
  - roles
  - permissions
  - Desk
  - verification
---

## What it does

ERPNext Role Experience Verification captures Frappe/ERPNext safety behavior from the designated read-only audit so future agents do not blend old Odoo, Claude, Codex, and current project truth.

## When to reach for it

Use before work touching this scope: ERPNext non-admin user/role/workspace verification.

## How to use it

1. Verify with the actual user/role experience, not only Administrator.
2. Check workspace visibility, shortcuts, routes, permissions, and real record counts.
3. Use role-specific browser/Desk checks before claiming an operator flow works.
4. Record exact role/user context without exposing credentials.

## What it depends on

- [No Bare Claims](../principles/no-bare-claims.md)
- [Current Truth Needs Evidence](../principles/current-truth-needs-evidence.md)
- [Claude Reference Library Readonly](claude-reference-library-readonly.md)

## Failure modes

- Administrator path hides operator permission failure.
- Workspace shortcut visible but route/record permission fails.
- Claim made without non-admin witness.

## Evidence

- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 1 lists the source files inspected for this read-only audit.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 3 documents Frappe safety patterns worth migrating.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 4 documents ERPNext project-operation patterns worth migrating.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 8 recommends `erpnext-role-experience-verification.md` as an OpenClaw capability card.
