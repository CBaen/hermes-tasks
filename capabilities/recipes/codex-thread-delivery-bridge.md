---
id: codex-thread-delivery-bridge
name: Codex Thread Delivery Bridge
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: machine-wide scheduled learning/action post delivery
currently_true: unknown
last_verified: 2026-05-21
depends_on:
  - codex-memory-bridge
  - conversation-learning-loop
used_by: []
tags:
  - codex
  - delivery
  - learning-review
  - local-ledger
  - adapters
---

# Codex Thread Delivery Bridge

## Use When

A scheduled learning review, capability action manager, or related automation
has a post that should be delivered somewhere visible.

## Rule

Do not pretend there is a Codex Desktop thread-posting API until a callable
tool is verified in the active runtime. Use a local outbox/ledger adapter first
and mark Codex Thread delivery as blocked.

## Current Source

Dedicated repo:

```text
/home/guidingl/projects/codex-thread-delivery
```

Banebook migration note: this directory was not present during the 2026-06-08
shared-root migration edit. Verify or restore the repo before treating this
bridge as runnable on Banebook.

## Adapter Boundary

- `local-ledger`: safe default. Writes local JSONL/markdown delivery records.
- `codex-thread`: blocked until a real callable Codex thread-posting API,
  connector, or app tool is verified.
- `chrome-ui`: manual/unsafe unless Guiding Light explicitly approves active
  browser control for that task.
- `openai-api`: not equivalent to posting into this Codex Desktop thread.

## Safety

- Include local and UTC date in every delivery request.
- Preserve date-boundary warnings when local and UTC dates differ.
- Redact secret-like text before writing delivery artifacts.
- Do not write Qdrant.
- Do not mutate trusted capability roots.
- Do not treat delivery as approval to promote candidate capabilities.

## Verification

Run the delivery bridge tests in its repo, then verify the scheduled producer
still writes local posts and action-manager briefs.
