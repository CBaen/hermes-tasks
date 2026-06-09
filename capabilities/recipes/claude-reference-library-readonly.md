---
id: claude-reference-library-readonly
name: Claude Reference Library Readonly
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: safe consultation of Claude-era files during Banebook Codex/shared-capability migration
currently_true: unknown
last_verified: 2026-05-07
tags:
  - Claude
  - privacy
  - migration
  - reference-library
---

## What it does

Claude Reference Library Readonly captures Frappe/ERPNext safety behavior from the designated read-only audit so future agents do not blend old Odoo, Claude, Codex, and current project truth.

## When to reach for it

Use before work touching this scope: safe consultation of Claude-era files during Banebook Codex/shared-capability migration.

## How to use it

1. Use Claude-era files as evidence/reference, not current truth by themselves.
2. Read narrow entrypoints and specific SKILL.md files; avoid broad directory ingestion.
3. Do not copy Claude skills wholesale; translate behavior into Codex skills, shared capabilities, project docs, or agent cards.
4. Do not read secrets, auth, raw sessions, logs, caches, browser profiles, or generated runtime state.
5. Verify current claims against project files/git/running systems before acting.

## What it depends on

- [No Bare Claims](../principles/no-bare-claims.md)
- [Current Truth Needs Evidence](../principles/current-truth-needs-evidence.md)

## Failure modes

- Old Claude/Odoo claim treated as current ERPNext truth.
- Whole folders copied into Codex or shared capabilities.
- Sensitive runtime/auth/session material inspected without need/approval.

## Evidence

- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 1 lists the source files inspected for this read-only audit.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 3 documents Frappe safety patterns worth migrating.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 4 documents ERPNext project-operation patterns worth migrating.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 8 recommends `claude-reference-library-readonly.md` as an OpenClaw capability card.
