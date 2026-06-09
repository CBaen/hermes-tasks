---
id: evidence-helper
name: Evidence Helper
schema_version: 2.1
profile: foundation
level: ingredient
maturity: candidate
scope: Banebook capability evidence helper and retired OpenClaw evidence-helper record
currently_true: unknown
last_verified: 2026-06-08
tags:
  - evidence
  - jsonl
  - helper
  - capability ledger
---

## What it does

Points agents to the current framework helper for appending valid compact JSONL
capability evidence events, while preserving the retired OpenClaw helper as
historical migration evidence.

Retirement note: this card described an OpenClaw-local helper. OpenClaw was
removed from `wardenclyffe` on 2026-05-14, and the helper path below no longer
exists. Do not use the OpenClaw command for current capability evidence work.

## When to reach for it

Use when recording capability use, fixes, failures, promotions, revalidation, or rollback notes and you want to avoid malformed JSONL.

For current work, follow the capability schema directly and verify JSON/JSONL
with the active project's tooling.

## How to use it

Current helper:

```bash
python /home/guidingl/projects/capabilities-framework/tools/capability_event.py --root /home/guidingl/capabilities --capability-id <id> --event use --result "What happened" --verification "What witnessed it" --confidence 2 --rollback "<revalidation path>" --json
```

This appends an evidence event. There is no dry-run flag; inspect `--help`
before use when in doubt.

Retired OpenClaw script path:

```text
C:/Users/baenb/.openclaw/workspace/.openclaw/tools/append_capability_evidence.py
```

Historical OpenClaw dry-run command:

```powershell
python C:/Users/baenb/.openclaw/workspace/.openclaw/tools/append_capability_evidence.py --capability-id example --event use --result "What happened" --verification "What witnessed it" --dry-run
```

Append for real only after checking the event contains no secrets or raw private content.

## What it depends on

- [Evidence Ledger Event](../atomic_ingredients/evidence-ledger-event.md)
- [Capability Evolution Gates](../principles/capability-evolution-gates.md)

## Failure modes

- Recording vague evidence that does not name a witness.
- Including secrets, raw transcript text, or private source excerpts in notes.
- Treating an evidence entry as proof beyond its stated scope.
