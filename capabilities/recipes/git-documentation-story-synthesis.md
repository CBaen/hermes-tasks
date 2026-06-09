---
id: git-documentation-story-synthesis
name: Git Documentation Story Synthesis
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: workspace and project history review
currently_true: unknown
last_verified: 2026-05-07
tags:
  - git
  - documentation
  - story synthesis
  - provenance
  - project memory
---

## What it does

Reads commits, diffs, docs, queues, decisions, and status files as a project story: what changed, why, what broke, what succeeded, what became stale, and what should be promoted into capabilities or memory.

## When to reach for it

Use when reviewing a project after heavy agent work, before cleanup, after a failed build/research lane, when reconstructing decisions, or when Guiding Light asks what happened.

## How to use it

1. Start read-only.
2. Inspect current git state: status, recent commits, untracked files, and major changed paths.
3. Read project maps in this order when present:
   - `AGENTS.md` / `PROJECT-MOJI.md`;
   - project index;
   - project status;
   - queue/workstreams;
   - decisions/audits;
   - capability indexes.
4. Build a narrative in plain English:
   - intention;
   - actual changes;
   - evidence/verification;
   - unresolved blockers;
   - stale/conflicting docs;
   - reusable lessons;
   - candidate capability promotions.
5. Treat git/docs as evidence, not proof. Verify important claims against files, tests, screenshots, or live systems.
6. Do not push, rewrite history, delete, or publish without approval.

## What it depends on

- [No Bare Claims](../principles/no-bare-claims.md)
- [Stale File Cleanup Process](stale-file-cleanup-process.md)
- [Capability Evidence And Promotion](capability-evidence-and-promotion.md)

## Failure modes

- Treating a commit message as truth when the files disagree.
- Producing a huge changelog instead of a useful story.
- Cleaning files before understanding what they represent.
- Losing the human/business reason behind technical changes.
