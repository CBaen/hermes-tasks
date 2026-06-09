---
id: stale-file-cleanup-process
name: Stale File Cleanup Process
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: Banebook Codex and current Guiding Light projects
currently_true: unknown
last_verified: 2026-05-07
tags:
  - cleanup
  - stale files
  - documentation
  - archive
  - git
---

## What it does

Finds stale, duplicated, contradicted, or abandoned files and turns cleanup into a safe review process instead of accidental deletion.

## When to reach for it

Use after large research/build attempts, migration work, command-center experiments, failed agent runs, project pivots, or when docs conflict with current reality.

## How to use it

1. Inventory candidates first. Do not delete while confused.
2. For each candidate, identify:
   - why it appears stale;
   - current replacement/source of truth, if any;
   - whether it is historical evidence;
   - whether it contains private/client-sensitive material;
   - safe action: keep, update, archive, move to failure note, or delete/trash after approval.
3. Prefer `archive/`, `failures/`, or explicit stale-note headers before deletion.
4. Use `trash` or reversible moves over destructive removal when possible.
5. If a stale file is linked from docs/indexes, update the links or mark the mismatch.
6. Record meaningful cleanup decisions in a queue/decision log or capability evidence.
7. Ask before destructive deletion, public-facing cleanup, or removing files whose purpose is unclear.

## What it depends on

- [Git Documentation Story Synthesis](git-documentation-story-synthesis.md)
- [No Bare Claims](../principles/no-bare-claims.md)

## Failure modes

- Deleting historical evidence needed to understand a failed path.
- Leaving obsolete docs that future agents will trust.
- Moving files without updating indexes, causing hidden drift.
- Treating untracked as garbage when it may be intentional work product.
