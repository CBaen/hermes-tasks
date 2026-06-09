---
id: runtime-source-retirement
name: Runtime Source Retirement
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: active runtime folders that duplicate Git-backed durable source
currently_true: unknown
last_verified: 2026-05-14
tags:
  - source-of-truth
  - runtime
  - junctions
  - skills
  - capabilities
  - hermes
  - codex
---

## What it does

Turns a runtime folder that has become a second editable source into a
Git-backed canonical source plus runtime junctions or marker files.

## When to reach for it

Use when:

- Codex or another verified active runtime can load a skill/tool from the right
  place, but old physical copies still exist elsewhere;
- slash-command routing works but peer agents can still find two editable
  copies;
- a runtime capability, skill, agent, or tool folder must become shared source
  without losing command availability;
- memory-backed procedures need promotion into normal callable skills.

## How to use it

1. Identify the canonical Git-backed repo and verify it is on the allowed branch.
2. Audit runtime and canonical folders before moving anything.
3. Merge intentional runtime-only work into the repo.
4. Delete or move stale generated/backup files that are no longer source.
5. Commit and push the merged canonical source.
6. Replace runtime duplicates with junctions to the repo, or marker files when
   the runtime path must stay as a non-source entrypoint.
7. Retire memory-backed skill copies only after the procedures exist as normal
   skills.
8. Verify:
   - repo clean and pushed;
   - Codex enabled skill paths are canonical and exist;
   - active runtime skill paths point at canonical roots or intentionally
     migrated local skill folders;
   - runtime paths resolve to canonical folders when they are meant to be
     source-backed;
   - command counts are preserved.
9. Record the decision, lesson, queue status, and workstream handoff.

## Required guards

- Do not delete `.claude`, `.codex`, peer-agent runtime folders, memories, sessions, logs, caches,
  or auth/config state wholesale without a fresh inventory and explicit task
  approval.
- Do not commit live runtime config that can contain gateway/auth material.
- Do not leave a duplicate source copy in the repo as "backup"; git history is
  the archive.
- Do not describe compatibility junctions as ownership.

## Evidence

On 2026-05-10, the Codex/OpenClaw framework source was merged into the Windows
source repo at `C:\Users\baenb\projects\codex-framework-backup`, runtime copies
were retired to junctions, `.codex\memories\skills` was retired after
promotion to top-level `skills/`, and OpenClaw still reported `Available as
command: 30`. This is Wardenclyffe/OpenClaw legacy evidence. The Banebook
source repo is `/home/guidingl/codex-framework`.

On 2026-05-14, OpenClaw was retired from `wardenclyffe`: non-secret workflow
skills were migrated into then-current local skills, OpenClaw runtime/source
copies were removed, and future runtime-source work should target verified
active runtimes only.
