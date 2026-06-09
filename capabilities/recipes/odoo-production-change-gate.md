---
id: odoo-production-change-gate
name: Odoo Production Change Gate
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: Odoo production data/config/code changes for client systems
currently_true: unknown
last_verified: 2026-05-07
tags:
  - Odoo
  - production
  - migration
  - deploy-safety
  - Claude-migration
  - scar-tissue
---

## What it does

Prevents quick direct production fixes from becoming outages by routing Odoo production changes through code, migrations, or explicit deploy functions with verification.

Adapted from Claude's `odoo-production-changes` skill.

## When to reach for it

Use before any Odoo production change involving:

- database records;
- website/page `arch_db`;
- stages/templates/config params;
- production-only form/content fixes;
- deploy scripts or one-off production repair commands.

## How to use it

1. Treat direct SSH/psql production edits as blocked by default.
2. Pick the durable path:
   - code change → local test → commit → deploy script;
   - DB/config fix → migration script preferred;
   - urgent one-off → add explicit deploy/helper function, not ad-hoc shell edits.
3. Before `arch_db` or `noupdate` edits:
   - check `arch_fs`;
   - avoid full replacement;
   - use targeted replacement preserving website-builder edits.
4. Verify survival:
   - will the change persist through module upgrade/deploy?
   - is rollback/backup path known?
   - did production/staging witness match the intended state?
5. If a hook fails to block unsafe direct access, treat that as a hook bug, not permission.

## What it depends on

- [Safe Rollback Review](safe-rollback-review.md)
- [Odoo Upgrade Preflight](odoo-upgrade-preflight.md)
- [No Bare Claims](../principles/no-bare-claims.md)

## Failure modes

- “Just one quick prod fix” through SSH/psql.
- Full `arch_db` replacement destroys website-builder edits.
- Fix works once but is overwritten by next deploy/module upgrade.
- Localhost test treated as proof for production-only issue.
- Production data/config changed without durable migration record.

## Evidence

- `C:/Users/baenb/.claude/skills/odoo-production-changes/SKILL.md:10-18` documents the 2026-04-13 production incident and states never to make direct production DB changes via SSH.
- `C:/Users/baenb/.claude/skills/odoo-production-changes/SKILL.md:20-58` defines approved paths: code deploy, migration script, deploy helper, targeted `arch_db` fixes.
- `C:/Users/baenb/.claude/skills/odoo-production-changes/SKILL.md:60-82` lists failure modes from shortcuts including direct psql, arch_fs ignorance, full arch_db replacement, and local-only testing.
