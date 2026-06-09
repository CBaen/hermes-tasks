---
id: safe-rollback-review
name: Safe Rollback Review
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: rollback/revert planning before destructive or history-affecting changes
currently_true: unknown
last_verified: 2026-05-07
tags:
  - rollback
  - git
  - safety
  - GSD-migration
---

## What it does

Plans rollback/revert actions with dependency checks and a human gate before execution.

Adapted from Claude GSD's `gsd-undo` pattern.

## When to reach for it

Use before:

- reverting commits;
- removing generated/project files;
- archiving or cleaning workspaces;
- undoing a phase/workstream;
- touching history or destructive state.

## How to use it

1. Identify rollback target: last N changes, phase/workstream, specific commit(s), or file set.
2. Inspect current git/status/diffs and any project manifest/status files.
3. Map dependency risk:
   - later work depending on the target;
   - generated files vs hand-written files;
   - external/public state not represented in git;
   - config/runtime side effects.
4. Prefer reversible actions: archive/trash before delete, patch before destructive reset.
5. Present a plain-language rollback plan and confirmation gate before execution.
6. After rollback, verify the original issue and any neighboring affected area.
7. Record what changed and why.

## What it depends on

- [No Bare Claims](../principles/no-bare-claims.md)
- [Stale File Cleanup Process](stale-file-cleanup-process.md)
- [Capped Review Fix Loop](capped-review-fix-loop.md)

## Failure modes

- Reverting without checking downstream dependencies.
- Destroying uncommitted/user-authored work.
- Treating git as the whole truth when external services/config changed.
- Skipping the human gate for destructive/history-affecting actions.

## Evidence

- `C:/Users/baenb/.claude/skills/gsd-undo/SKILL.md:12-17` defines safe git revert using phase manifest, dependency checks, and a confirmation gate.
- `C:/Users/baenb/.claude/skills/gsd-undo/SKILL.md:19-22` defines rollback target modes: last commits, phase, or plan.
- `research/claude-to-openclaw-skill-migration/GSD-SKILL-FAMILY-AUDIT-2026-05-07.md` identifies safe undo as migration-worthy.
