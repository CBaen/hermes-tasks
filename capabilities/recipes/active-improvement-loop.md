---
id: active-improvement-loop
name: Active Improvement Loop
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: Banebook Codex, Qdrant, memory, and capability evolution
currently_true: unknown
last_verified: 2026-05-07
tags:
  - Qdrant
  - memory
  - improvement loop
  - review
  - synthesis
---

## What it does

Defines the safe path from observations to improvements: metadata/reports first, reviewed lessons second, sanitized exports third, optional Qdrant/vector writes last.

## When to reach for it

Use when designing automatic Claude-folder synthesis, Qdrant-backed improvement, conversation-log review, git/docs review, capability evolution, or cross-agent learning.

## How to use it

Use this progression:

```text
source observations
-> metadata/index/dry-run report
-> reviewed lesson candidates
-> sanitized exports
-> capability/memory/tool/project updates
-> optional Qdrant/vector write after explicit approval
```

Rules:

1. Start read-only and dry-run.
2. Do not store raw private conversation bodies by default.
3. Do not write Qdrant/vector memory until the export is reviewed and eligible.
4. Every applied improvement needs:
   - source/evidence;
   - date;
   - result;
   - confidence;
   - rollback or revalidation path.
5. Improvements can target:
   - daily memory;
   - `MEMORY.md`;
   - capability cards;
   - project status/queue/decisions;
   - glossary/terminology notes;
   - retired OpenClaw skills/tools as migration evidence;
   - templates;
   - stale-file cleanup queue.
6. Keep user-facing reports concise: what worked, what changed, what is risky, what is the next useful action.

## What it depends on

- [Cross-Agent Learning Loop Container](cross-agent-learning-loop-container.md)
- [Advisory Evolution Review Loop](advisory-evolution-review-loop.md)
- [Capability Evolution Gates](../principles/capability-evolution-gates.md)
- [No Bare Claims](../principles/no-bare-claims.md)

## Failure modes

- Treating Qdrant as a magic truth machine.
- Writing embeddings before redaction/review.
- Generating self-improvement theater with no applied benefit.
- Letting the improvement loop become noisy homework for Guiding Light.
