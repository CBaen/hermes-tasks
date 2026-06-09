---
id: moji-conversation-index
name: Moji Conversation Index
schema_version: 2.0
level: recipe
maturity: deprecated
scope: retired OpenClaw/Moji session continuity metadata indexing
currently_true: false
verification_level: 1
last_verified: 2026-05-14
evidence_quality: direct
successful_uses: 0
failed_uses: 0
regressions: 0
depends_on:
  - moji-project-capability-layers
used_by: []
tags:
  - moji
  - conversation index
  - memory bridge
  - session history
  - sqlite
  - dry run
  - provenance
---

## What it does

Defines the retired OpenClaw-local conversation indexing process that existed
before the 2026-05-14 OpenClaw removal. It is preserved as historical evidence
for privacy and metadata-only indexing patterns, not as a current command path.

## When to reach for it

Do not use the `.openclaw` commands below for current work. Use active Codex or
other verified memory tooling instead, and verify the current path before
claiming a session index exists.

## How to use it

Retired primary folder:

```text
C:/Users/baenb/.openclaw/automations/conversation-index
```

Retired policy:

```text
C:/Users/baenb/.openclaw/automations/conversation-index/index-policy.json
```

Retired indexer:

```text
C:/Users/baenb/.openclaw/automations/conversation-index/moji-session-indexer.py
```

Retired ledger:

```text
C:/Users/baenb/.openclaw/automations/conversation-index/state/source-ledger.sqlite
```

Retired routine safe audit:

```powershell
python C:/Users/baenb/.openclaw/automations/conversation-index/moji-session-indexer.py --update-ledger --json --summary-only
```

Retired memory-promotion queue dry run:

```powershell
python C:/Users/baenb/.openclaw/automations/conversation-index/moji-memory-promotion-queue.py --json
```

This writes advisory outputs to:

```text
C:/Users/baenb/.openclaw/workspace/audits/memory-promotion-queue/
```

Retired debug limited run:

```powershell
python C:/Users/baenb/.openclaw/automations/conversation-index/moji-session-indexer.py --limit 5 --json
```

Historical behavior:

- scanned OpenClaw main session JSONL files;
- skips trajectory/checkpoint files;
- records metadata only;
- writes local SQLite source ledger only when `--update-ledger` is used;
- does not store raw conversation bodies;
- does not store raw session filenames;
- does not write Qdrant;
- has no delete/prune/apply mode;
- can generate a metadata-only memory-promotion candidate queue for Moji review.

This is intentionally less ambitious than Codex's bridge until the basics are proven.

## Promotion and retention gates

Session-index findings may become daily memory, `MEMORY.md`, project status, project decisions, or capability evidence only after Moji reviews the metadata against the actual source/session context and writes a minimized summary. Metadata is a pointer, not proof.

Retention/access notes:

- Historical ledger location was local and privacy-sensitive:
  `C:/Users/baenb/.openclaw/automations/conversation-index/state/source-ledger.sqlite`.
- Treat the ledger as internal continuity infrastructure, not shareable output.
- Rebuild/delete procedures should be added before any pruning or destructive maintenance is introduced.
- Adding raw bodies, raw filenames, embeddings/vector writes, external sync, or additional persistent fields requires explicit Guiding Light approval and a redaction review.
- Backups/copies of the ledger inherit the same privacy restrictions.

## What it depends on

- `moji-project-capability-layers`

## Failure modes

- Accidentally storing raw private chat in a durable index. Avoided by metadata-only first version.
- Confusing old conversation claims with current truth. Always verify action-relevant claims.
- Letting indexes become junk drawers. Use review/promotion gates before long-term memory.
- Copying any runtime's implementation blindly despite different session format.

## Evidence notes

Created after Guiding Light asked for Moji's own conversation indexing process
adapted from Codex's process. Retired on 2026-05-14 with OpenClaw removal.
Codex source inspected: `C:/Users/baenb/.codex/framework/codex-memory-indexing-operating-design-2026-05-05.md`, `C:/Users/baenb/.codex/capabilities/recipes/codex-memory-bridge.md`, and `C:/Users/baenb/.codex/automations/memory-bridge/`.
