---
id: cross-agent-learning-loop-container
name: Cross-Agent Learning Loop Container
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: local shared learning infrastructure for Codex and verified peer agents; Claude runtime paused, Claude history is legacy source material
currently_true: unknown
last_verified: 2026-05-07
evidence_quality: inferred
successful_uses: 0
failed_uses: 0
regressions: 0
depends_on:
  - moji-conversation-index
  - moji-project-capability-layers
  - no-bare-claims
used_by: []
tags:
  - memory bridge
  - learning loop
  - container
  - codex
  - hermes
  - qdrant
  - privacy
  - dry run
---

## What it does

Defines the safe architecture for a local **learning-loop container**: a
neutral memory foundry that reads approved agent/project evidence, runs
memory-bridge/review tooling, and produces reviewed/sanitized outputs that
Codex and any verified current peer agent can consume.

Claude runtime is not currently participating, but Claude conversation history/Qdrant archives are important source material and should be reviewed carefully through approved, privacy-minimized paths.

This does **not** containerize Codex, Hermes, Claude, or their runtimes. It
containerizes the learning pipeline. Claude-derived lessons may enter only
through reviewed/sanitized archive outputs, not raw runtime sharing.

## Core design correction

The container owns the learning loop, not the agents.

Agents are:

- contributors of approved/session/project evidence;
- consumers of reviewed lessons;
- never required to expose their auth/runtime guts to one another.

The container is:

- local;
- review-first;
- privacy-minimized;
- dry-run by default;
- allowed to write ledgers/reports/lesson plans/sanitized exports;
- not allowed to mount broad home folders or secrets.

## Pipeline

```text
Codex sessions / verified peer-agent metadata / selected git metadata
-> learning-loop container
-> SQLite ledgers + reports + reviewed lesson plans
-> sanitized exports for Codex and verified peer agents
-> optional Qdrant write only after approval
```

## Read-only inputs

Allowed only when deliberately configured:

- `/home/guidingl/.codex/sessions`
- Peer-agent or Codex metadata/index outputs, not raw private session bodies by
  default
- selected project git roots, preferably read-only and narrowed to specific projects

## Writable outputs

Recommended volumes:

- `memory-bridge-state` - SQLite ledgers and run state
- `memory-bridge-output` - reports, review queues, lesson plans
- `sanitized-exports` - reviewed Codex/peer-agent-readable lessons

Recommended output shape:

```text
/reports/
  memory-bridge-report.md

/lesson-plans/
  conversation-lesson-plan.jsonl
  conversation-lesson-plan.md

/exports/
  codex-learning.jsonl
  peer-agent-learning.jsonl
```

## Network

Optional and gated:

- `qdrant:6333` for reviewed semantic memory writes
- Ollama/embedding service only if needed

Default posture: no vector writes.

## Never mount

- `auth.json`
- `.credentials.json`
- `.sandbox-secrets`
- broad `/home/guidingl`
- raw `.claude` wholesale; prefer approved indexed/compressed Claude-history sources first
- arbitrary browser profiles/cookies
- provider token stores
- full private repos unless explicitly approved and narrowed

## Export schema

The old OpenClaw-local export schema path was retired on 2026-05-14 and is
legacy Windows evidence, not a current Banebook path:

```text
C:/Users/baenb/.openclaw/automations/learning-loop-container/learning-export-schema.template.json
```

Sanitized exports should identify audience, scope, privacy level, source references, evidence level, lesson type, suggested action, promotion target, and whether Qdrant writes are eligible. Default: `qdrant_eligible=false` and `requires_human_review=true`.

## Review gates

Required progression:

```text
dry-run -> reviewed lesson plan -> sanitized export -> optional codex_memory_v1/Qdrant write
```

No step should silently upgrade itself to the next level.

## Failure modes

- Treating containerization as permission to mount everything.
- Letting one agent consume another agent's raw private runtime/auth/session data.
- Writing embeddings/vector memory before redaction and lesson review.
- Confusing old session claims with current truth.
- Creating a second opaque memory system that Moji cannot explain or audit.

## Recommended first implementation

1. Create a template-only `learning-loop-container/` folder.
2. Define mount policy as data before any Docker run.
3. Port/adapt Codex memory bridge scripts into the container image only after reviewing inputs/outputs.
4. Run in dry-run/report-only mode.
5. Produce sanitized exports, then have each participating agent consume only the export format intended for it.

## Status

Design captured from Codex proposal relayed by Guiding Light on 2026-05-06. Not implemented or run yet.
