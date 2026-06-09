---
id: project-operating-scaffold
name: Project Operating Scaffold
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: starting or regularizing serious projects in Banebook Codex/current-agent workflows
currently_true: unknown
last_verified: 2026-05-07
tags:
  - project-scaffold
  - planning
  - GSD-migration
  - durable-state
---

## What it does

Creates a durable project operating surface: project brief, Moji guide,
requirements/roadmap/status/decision files, and capability roots where
warranted.

Adapted from Claude GSD's `gsd-new-project`, but aligned with current
Banebook Codex/current-agent project files instead of `.planning/` as a required shape.

## When to reach for it

Use when a project is serious enough that losing state would be costly:

- client or income-relevant projects;
- multi-phase builds;
- products with requirements/roadmaps;
- research-to-build efforts;
- any work likely to span sessions.

## How to use it

1. Check whether the project already has an entrypoint:
   - `PROJECT-MOJI.md`, `PROJECT-BRIEF.md`, `AGENTS.md`, queue/status/decision files, capability index.
2. If missing, create the smallest useful scaffold:
   - `PROJECT-BRIEF.md` — what this is and why it matters;
   - `PROJECT-MOJI.md` — how Moji should work here;
   - `PROJECT-STATUS.md` — current state and verification;
   - `<project>-queue.md` or `workstreams/` — active/later work;
   - `<project>-decisions.md` — durable decisions;
   - `capabilities/INDEX.md` or a visible purpose root such as
     `capabilities-<scope>/INDEX.md` when reusable project knowledge exists.
3. Capture requirements and roadmap only at the granularity needed now. Do not overbuild ceremony.
4. Verify current state from files/git/tool output before writing status.
5. Keep GL-facing setup minimal: recommended scaffold + one correction path.

## What it depends on

- [Serious Project Scaffold](../meals/serious-project-scaffold.md)
- [Capability Index Routing](capability-index-routing.md)
- [Phase Decision Context](phase-decision-context.md)
- [Zero-Friction Idea Capture](zero-friction-idea-capture.md)

## Failure modes

- Copying GSD's `.planning/` shape as mandatory when the project needs a different visible root.
- Creating more process than the project can use.
- Writing status from memory instead of current evidence.
- Making GL manually configure project scaffolding fields Moji can choose.

## Evidence

- `C:/Users/baenb/.claude/skills/gsd-new-project/SKILL.md:20-31` creates durable project context, config, research, requirements, roadmap, and state files.
- `research/claude-to-openclaw-skill-migration/GSD-SKILL-FAMILY-AUDIT-2026-05-07.md` identifies durable project memory in files as a migration-worthy pattern.
