---
id: milestone-archive-and-reset
name: Milestone Archive and Reset
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: completing project milestones while preserving history and preparing next work
currently_true: unknown
last_verified: 2026-05-07
tags:
  - milestone
  - archive
  - project-state
  - GSD-migration
---

## What it does

Closes a milestone by auditing readiness, archiving what shipped, preserving requirements/outcomes, updating current project state, and preparing the next milestone without letting roadmap/status files grow forever.

Adapted from Claude GSD's `gsd-complete-milestone` pattern.

## When to reach for it

Use when a project milestone/version/work chunk is complete enough to become history and the active project surface should reset for the next chunk.

## How to use it

1. Pre-flight audit:
   - are planned phases/tasks complete?
   - did UAT/review pass or are gaps accepted as tech debt?
   - are docs/status/decisions current?
2. Gather summary evidence:
   - key accomplishments;
   - files/artifacts changed;
   - tests/builds/UAT/reviews;
   - remaining known gaps.
3. Archive milestone artifacts before deleting/collapsing active files.
4. Update project status/current state with shipped reality.
5. Collapse roadmap/requirements to concise links/summaries so active context stays small.
6. If using git tags/commits, do local checkpoint only under project policy; ask before pushing.
7. Start the next milestone with fresh requirements/context, not stale leftovers.

## What it depends on

- [Conversational UAT Verification](conversational-uat-verification.md)
- [Codebase-Verified Docs Update](codebase-verified-docs-update.md)
- [Safe Rollback Review](safe-rollback-review.md)
- [Workstream State Management](workstream-state-management.md)

## Failure modes

- Archiving without audit.
- Deleting or overwriting active artifacts before archive exists.
- Letting old milestone requirements remain active by accident.
- Treating milestone completion as “everything is perfect” instead of “this state is recorded.”
- Pushing tags/remotes without explicit permission.

## Evidence

- `C:/Users/baenb/.claude/skills/gsd-complete-milestone/SKILL.md:12-17` defines milestone completion as archive + roadmap/requirements/project-state update.
- `C:/Users/baenb/.claude/skills/gsd-complete-milestone/SKILL.md:40-55` requires audit/gap pre-flight before completion.
- `C:/Users/baenb/.claude/skills/gsd-complete-milestone/SKILL.md:102-109` includes critical rules: verify completion, user confirmation, archive before deleting, one-line summary, fresh requirements.
- `research/claude-to-openclaw-skill-migration/GSD-SKILL-FAMILY-AUDIT-2026-05-07.md` identifies milestone archive and state reset as migration-worthy.
