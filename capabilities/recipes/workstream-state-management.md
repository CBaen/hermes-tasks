---
id: workstream-state-management
name: Workstream State Management
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: managing concurrent or parked project workstreams for current agents
currently_true: unknown
last_verified: 2026-05-07
tags:
  - workstreams
  - project-state
  - resume
  - GSD-migration
---

## What it does

Keeps parallel or parked workstreams visible, resumable, and separated so one project does not become a pile of half-remembered threads.

Adapted from Claude GSD's `gsd-workstreams` pattern.

## When to reach for it

Use when a project has multiple active/parked lanes, such as:

- research vs build vs client/admin;
- design vs architecture vs content;
- current milestone vs future idea;
- bugfix lane vs main feature lane.

## How to use it

1. Create a workstream record with:
   - name/slug;
   - purpose;
   - current status;
   - current phase/task;
   - last evidence/witness;
   - next action;
   - blockers;
   - related files.
2. Keep a project-level workstream index or queue.
3. Switch context explicitly: read the workstream state before acting.
4. Park work by writing pause/resume notes, not by relying on chat memory.
5. Complete/archive workstreams with a short outcome and links to artifacts.
6. Avoid concurrent writes to the same files unless the plan explicitly coordinates them.

## What it depends on

- [Zero-Friction Idea Capture](zero-friction-idea-capture.md)
- [Phase Decision Context](phase-decision-context.md)
- [Executable Phase Plan](executable-phase-plan.md)
- [Stale File Cleanup Process](stale-file-cleanup-process.md)

## Failure modes

- Hidden active workstream in chat only.
- Multiple lanes editing the same file without coordination.
- Parking an idea without a resume trigger or next action.
- Treating a workstream switch as permission to ignore the previous lane's state.

## Evidence

- `C:/Users/baenb/.claude/skills/gsd-workstreams/SKILL.md:12-22` lists workstream operations: list/create/status/switch/progress/complete/resume.
- `C:/Users/baenb/.claude/skills/gsd-workstreams/SKILL.md:50-65` describes status/progress/complete/resume operations and active workstream handling.
- `research/claude-to-openclaw-skill-migration/GSD-SKILL-FAMILY-AUDIT-2026-05-07.md` identifies workstreams as useful concepts with mechanics to adapt.
