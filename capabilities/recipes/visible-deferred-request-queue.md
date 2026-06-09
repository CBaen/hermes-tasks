---
id: visible-deferred-request-queue
name: Visible Deferred Request Queue
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: important user requests, skill migrations, command-center improvements, and feature work that cannot finish immediately
currently_true: unknown
last_verified: 2026-05-08
tags:
  - queue
  - parking-lot
  - handoff
  - command-center
  - continuity
  - Guiding-Light-rule
---

## What it does

Turns important but not-immediately-finished requests into visible queue entries with status, owner, next action, and source boundary. Chat acknowledgement is not enough. If the work matters, future agents need a file they can route from.

## When to reach for it

Use when Guiding Light names or implies an important item that will not be completed in the current turn or current lane, including:

- Claude/Codex/OpenClaw skill migration;
- command-center design requirements;
- project feature requests;
- safety/security operating rules;
- client/project workstreams;
- parked tangents that are valuable but not current-lane.

## How to use it

1. Pick the nearest durable queue:
   - project queue for project feature work;
   - research/workstream queue for migration/design lanes;
   - root/system queue for shared agent infrastructure.
2. Add entry with:
   - request/source;
   - status: active, queued, blocked, completed, parked;
   - owner/agent surface;
   - next action;
   - source/privacy boundary;
   - expected artifact or verification gate.
3. If the queue entry creates a decision, also update the relevant decision log.
4. If it creates a reusable lesson, update lessons/capabilities.
5. If work completes, mark the queue entry complete and name the artifact/commit.

## Failure modes

- Leaving the only copy in chat.
- Creating a queue item without a next action.
- Burying a project-specific item in global memory only.
- Letting completed items stay marked active.
- Duplicating the same item across roots without a source-of-truth note.

## Evidence

- `research/claude-to-openclaw-skill-migration/CLAUDE-SKILL-TRANSLATION-QUEUE-2026-05-08.md` was created after GL corrected that important skill migrations must be parked visibly.
- `memory/2026-05-08.md` records the design lesson: deferred important user requests must land in a visible queue immediately.
