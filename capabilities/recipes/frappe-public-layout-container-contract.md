---
id: frappe-public-layout-container-contract
name: Frappe Public Layout Container Contract
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: Frappe/Webshop route containment, responsive layout, and browser evidence
currently_true: unknown
last_verified: 2026-05-07
tags:
  - Frappe
  - Webshop
  - layout
  - responsive
  - visual-verification
---

## What it does

Frappe Public Layout Container Contract captures Frappe/ERPNext safety behavior from the designated read-only audit so future agents do not blend old Odoo, Claude, Codex, and current project truth.

## When to reach for it

Use before work touching this scope: Frappe/Webshop route containment, responsive layout, and browser evidence.

## How to use it

1. Preserve Frappe website shell and Webshop hooks/selectors; wrap/style instead of replacing pipelines.
2. Every public section chooses containment mode: contained, full-bleed, clipping track, etc.
3. Do not hide real layout failure with body-wide overflow-x hidden.
4. New routes/sections need executable route contract updates and browser/layout verification.
5. Screenshots/Playwright gates are required before visual/layout claims.

## What it depends on

- [No Bare Claims](../principles/no-bare-claims.md)
- [Current Truth Needs Evidence](../principles/current-truth-needs-evidence.md)
- [Claude Reference Library Readonly](claude-reference-library-readonly.md)

## Failure modes

- Webshop lifecycle broken by template replacement.
- Horizontal overflow hidden globally instead of fixed.
- Visual readiness claimed from code inspection only.

## Evidence

- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 1 lists the source files inspected for this read-only audit.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 3 documents Frappe safety patterns worth migrating.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 4 documents ERPNext project-operation patterns worth migrating.
- `research/claude-to-openclaw-skill-migration/FRAPPE-ERPNEXT-SAFETY-AUDIT-2026-05-07.md` section 8 recommends `frappe-public-layout-container-contract.md` as an OpenClaw capability card.
