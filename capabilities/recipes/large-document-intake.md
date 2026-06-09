---
id: large-document-intake
name: Large Document Intake
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: installed Codex global capability and skill pointer
currently_true: unknown
last_verified: 2026-05-08
tags:
  - Codex
  - truncation
  - documents
  - source packets
  - citations
---

## What it does

Routes Codex to the installed `large-document-intake` skill and its deterministic
chunking script before relying on large, structured, scanned, or
truncation-prone source material.

## When to use it

Use when a task depends on a PDF, DOCX, XLSX/CSV, HTML, Markdown, JSON/JSONL,
log, handoff, contract, source packet, scraped page, or terminal/tool output
that may truncate.

## How to use it

1. Prefer the triggerable Codex skill:
   `/home/guidingl/.codex/skills/large-document-intake/SKILL.md`
2. Run the script from the skill when direct intake is needed:

```bash
python /home/guidingl/.codex/skills/large-document-intake/scripts/intake_document.py <source> --out <output-dir> --chunk-chars 12000 --overlap-chars 500
```

3. Trust the output only when `manifest.json` has `status: ok` and matching
   extraction/reassembly hashes.
4. If the script exits `2`, `3`, or `4`, report the blocker and do not summarize
   from partial text.
5. Cite the relevant chunk IDs and `source-map.jsonl` spans in claims.
6. For bulky or truncation-recovery work, protect the main context: use a
   bounded recovery lane/subagent or local chunk reads, then bring back only the
   source path, chunk IDs/spans, decision-changing evidence, and unresolved
   gaps.

## Adapter notes

- The portable source concept lives in
  `/home/guidingl/projects/capabilities-framework/capabilities/recipes/large-document-intake.md`.
- Other runtimes may adopt the concept, but they do not inherit the
  Codex skill trigger automatically.
- Generated chunks are temporary working artifacts unless the user explicitly
  asks to preserve them.
- A recovery lane's summary is not proof by itself. Proof is the recovered
  source path plus exact chunks, line ranges, or source-map spans.
