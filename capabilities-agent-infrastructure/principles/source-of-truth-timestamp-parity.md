---
id: source-of-truth-timestamp-parity
name: Source Of Truth Timestamp Parity
schema_version: 2.1
profile: foundation
level: principle
maturity: candidate
scope: AI-readable current-state docs and capability parity in hermes-tasks
currently_true: verified
last_verified: 2026-06-11
tags:
  - source-of-truth
  - timestamps
  - documentation
  - parity
  - handoff
  - git
---

# Source Of Truth Timestamp Parity

## What it helps with

Use this when current state, handoffs, queue, decisions, capability cards, or publish status could drift out of sync.

## Rule

Every current-state change needs a timestamped doc update in the same work session. If a claim spans multiple source-of-truth docs, update all affected docs before committing.

## Required docs

- `SOURCE-OF-TRUTH.md` - authority order and parity contract.
- `PROJECT-STATUS.md` - current project state.
- `HANDOFF.md` - session inheritance and runtime facts.
- `hermes-tasks-queue.md` - active/next/parked/done work.
- `hermes-tasks-decisions.md` and `GLOBAL-DECISIONS.md` - durable decisions.
- `agent-lanes/BOARD.md` and lane handoffs - lane state.
- Owning capability roots - reusable verified procedures.

## Verification

Run:

```bash
python tools/check_source_of_truth_parity.py
```

Then run relevant capability graph validators if capability cards changed.

## Pitfalls

- A document cannot know the hash of the commit that contains itself before commit. Use live git commands for current commit/remote truth.
- Historical decision entries can mention old blockers; current-state docs must not leave stale blocker text as if it is still active.
- Memory and conversation summaries are clues only. Live git/system verification and current source-of-truth docs outrank them.
