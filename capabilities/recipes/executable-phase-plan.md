---
id: executable-phase-plan
name: Executable Phase Plan
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: turning phase context into buildable, verifiable plans
currently_true: unknown
last_verified: 2026-05-07
tags:
  - planning
  - execution
  - verification
  - GSD-migration
---

## What it does

Turns phase context into a plan that a builder can execute and a reviewer can verify.

Adapted from Claude GSD's `gsd-plan-phase` pattern.

## When to reach for it

Use after [Phase Decision Context](phase-decision-context.md) and before building when work has more than one step or needs verification.

## How to use it

1. Read phase/workstream context and project capability index.
2. Decide whether research is needed:
   - if external/current/library/API uncertainty exists, use source-separated research or plan-deepen;
   - if requirements are already clear, proceed directly to planning.
3. Write an executable plan with:
   - objective;
   - scope / non-scope;
   - files likely touched;
   - ordered tasks;
   - verification gates;
   - rollback/safety notes;
   - open blockers;
   - user-facing outcome.
4. Verify the plan before execution:
   - do tasks match objective?
   - are dependencies ordered?
   - are verification steps concrete?
   - does it ask GL for technical choices Moji should own?
5. Iterate only until pass or a small cap; if a plan cannot pass, surface the blocker.

## What it depends on

- [Phase Decision Context](phase-decision-context.md)
- [Plan Deepen Before Build](plan-deepen-before-build.md)
- [Source-Separated Decision Research](source-separated-decision-research.md)
- [Safe Rollback Review](safe-rollback-review.md)

## Failure modes

- Beautiful plan with no verification witness.
- Planning from stale requirements.
- Skipping research when the plan depends on unknown API/library behavior.
- Endless plan iteration instead of naming the blocker.

## Evidence

- `C:/Users/baenb/.claude/skills/gsd-plan-phase/SKILL.md:14-20` defines executable phase prompts with integrated research and verification.
- `C:/Users/baenb/.claude/skills/gsd-plan-phase/SKILL.md:22-24` defines the flow: research if needed, plan, verify, iterate.
- `research/claude-to-openclaw-skill-migration/GSD-SKILL-FAMILY-AUDIT-2026-05-07.md` identifies executable plans with verification loops as migration-worthy.
