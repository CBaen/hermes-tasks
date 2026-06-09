---
id: odoo-upgrade-preflight
name: Odoo Upgrade Preflight
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: Odoo deploy/upgrade readiness checks before `deploy.py` or `odoo -u`
currently_true: unknown
last_verified: 2026-05-07
tags:
  - Odoo
  - deploy
  - upgrade
  - lint
  - schema
  - Claude-migration
  - scar-tissue
---

## What it does

Runs scar-tissue checks before Odoo upgrades/deploys so known upgrade killers and Odoo 19 breaking patterns are caught before client-facing systems break.

Adapted from Claude's `odoo-19-lint`, `odoo-migration-guard`, and `odoo-deploy-safety` skills.

## When to reach for it

Use before any Odoo deploy/upgrade, especially when touching:

- model fields or `models/*.py`;
- XML views/templates/pages;
- `__manifest__.py` data/assets;
- SCSS/JS assets;
- migration scripts;
- deploy scripts.

## How to use it

1. Run structural lint against changed Python/XML/manifest/static files.
2. For model field changes, check schema parity against the actual target database before deploy.
3. Before upgrade, check known upgrade killers:
   - NULL `arch_db` / non-string `arch` views;
   - copy-on-write orphan views;
   - DB views whose XML files were deleted;
   - unsupported SCSS functions such as `color-mix()` under Odoo libsass.
4. Confirm manifest/data/assets include any new static files/templates.
5. Treat connection/check failure as “unknown/blocking,” not as a pass.
6. Only claim safe-to-deploy after the checks have witnesses.

## What it depends on

- [Odoo Production Change Gate](odoo-production-change-gate.md)
- [Codebase-Verified Docs Update](codebase-verified-docs-update.md)
- [No Bare Claims](../principles/no-bare-claims.md)

## Failure modes

- Python declares a new field but production DB lacks the column.
- Static JS/SCSS exists but is missing from manifest assets.
- Odoo 19 XML breaking changes survive to upgrade (`<tree>`, `numbercall`, invalid search attributes, QWeb literals).
- `website.page`/`ir.ui.view` has NULL/non-string arch.
- Deleted XML leaves orphan DB view records.
- Copy-on-write website views keep stale `arch_fs` pointers.
- A failed preflight connection is misread as safe.

## Evidence

- `C:/Users/baenb/.claude/skills/odoo-19-lint/SKILL.md:17-42` lists structural Odoo 19 lint rules including `model_create_multi`, manifest asset registration, tree/list changes, cron `numbercall`, search attributes, QWeb literals, and website descriptions.
- `C:/Users/baenb/.claude/skills/odoo-migration-guard/SKILL.md:10-29` documents the 2026-04-08 production `UndefinedColumn` incident and the schema-parity check steps.
- `C:/Users/baenb/.claude/skills/odoo-migration-guard/SKILL.md:46-53` defines exit codes and says connection failure is blocking.
- `C:/Users/baenb/.claude/skills/odoo-deploy-safety/SKILL.md:10-83` lists upgrade killers: NULL arch views, COW orphans, orphan views from deleted XML, and `color-mix()` in SCSS.
- `C:/Users/baenb/.claude/skills/SKILL-AUDIT-ODOO-2026-04-23.md:24-47` classifies `form-integrity`, `odoo-19-lint`, `odoo-migration-guard`, `odoo-deploy-safety`, and `odoo-production-changes` among the first enforceable/strong Odoo safety surfaces while demoting stale `odoo-form-validator`.
