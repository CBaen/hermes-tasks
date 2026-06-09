---
id: conversation-learning-loop
name: Conversation Learning Loop
schema_version: 2.0
level: recipe
maturity: candidate
scope: machine-wide Codex memory promotion and actionable lesson routing
currently_true: unknown
verification_level: 2
last_verified: 2026-05-06
evidence_quality: direct
successful_uses: 1
failed_uses: 0
regressions: 0
depends_on:
  - codex-memory-bridge
  - guiding-light-perspective-tender
used_by:
  - codex-thread-delivery-bridge
tags:
  - indexed conversations
  - lesson promotion
  - memory bridge
  - capability routing
  - verification
---

# Conversation Learning Loop

## Purpose

Turn indexed conversations into actionable system behavior without blindly trusting raw chat, leaking private material, or turning agent inference into durable truth.

The loop is:

```text
indexed conversation -> reviewed lesson -> correct system layer -> verifier/default behavior -> audit report
```

The lesson is not learned until a file, verifier, skill, capability, memory, or workstream changes and the change has a verification path.

## When To Use

Use this recipe when:

- A conversation review shows a repeated user correction, failure, preference, or workflow.
- A verified memory-bridge recall/search result returns conversation evidence
  that should change future agent behavior after current verification and
  promotion review, not just the current answer.
- A memory-bridge report identifies ready lesson actions.
- A project repeats the same failure mode, such as stale docs, wrong machine context, unverified git claims, or unsafe cleanup scope.
- The user asks how to make Codex learn from prior indexed conversations.

## Non-Negotiables

- Do not promote raw conversation bodies to durable memory.
- Do not promote cards with unresolved redaction, speaker attribution, or Guiding Light perspective blockers.
- Do not write Qdrant from this loop until the reviewed promotion gate is explicitly approved.
- Do not treat commit messages, handoffs, or old memories as proof. They are evidence maps.
- Do not treat recall evidence as current truth until the relevant repo, git,
  live system, account state, or explicit user correction has been checked.
- Keep project-specific lessons inside the project unless the behavior is clearly reusable across projects.

## Lesson Schema

Every promoted lesson must fit this shape:

```text
trigger -> rule -> action -> verification -> owner
```

Fields:

- `trigger`: the situation that should activate the lesson.
- `rule`: the durable operating rule.
- `action`: what Codex should do differently.
- `verification`: the command, live check, test, or inspection that proves the rule was followed.
- `owner`: usually Codex. Use the user only for meaning, design, privacy, client-readiness, or business-risk decisions.

## Target Layers

Choose the smallest layer that will actually change behavior:

- `memories/`: small cross-project preference or correction.
- `capabilities/recipes/`: reusable workflow with a clear start and finish.
- `skills/`: repeatable procedure Codex should actively invoke.
- `project AGENTS.md`: project-specific arrival/routing rule.
- `project capability root`: project capability routing, usually
  `capabilities/INDEX.md` for new projects or an existing
  `.codex/capabilities/INDEX.md` root where that shape has already evolved.
- `project verifier script`: anything that can be checked automatically.
- `workstreams/*.md`: active project state, ownership, and current next actions.
- `no durable action`: one-off, stale, private, unsafe, or not yet clear.

## Promotion Gate

A lesson may be acted on only when all are true:

- Redaction status is clean or manually approved.
- Speaker status is platform-only or manually resolved.
- Guiding Light perspective review passed or the held item was rewritten as Codex-owned responsibility.
- Recall evidence has been checked against current files, git, live system,
  account state, or explicit user correction before becoming a durable rule.
- The lesson has a concrete target layer and suggested file.
- The lesson includes a verification path.
- The change will not overwrite protected workspaces such as `.claude` or project files outside scope.

## Command Flow

Refresh the local dry-run index:

```bash
python /home/guidingl/.codex/automations/memory-bridge/codex-session-indexer.py --update-ledger --json --summary-only
```

Generate or refresh cards and review gates:

```bash
python /home/guidingl/.codex/automations/memory-bridge/review-source-discovery.py --scope core-systemwide --json
python /home/guidingl/.codex/automations/memory-bridge/learning-review-runner.py --mode daily
```

Manual diagnostic previews may still use `--limit`, but scheduled quality
review must use the review-ledger-selected source list created by the runner.

For a specific selected session source list:

```bash
python /home/guidingl/.codex/automations/memory-bridge/conversation-card-preview.py --source-list /home/guidingl/.codex/tmp/memory-bridge/review-source-lists/selected-session-sources-YYYYMMDD-HHMMSS.jsonl
python /home/guidingl/.codex/automations/memory-bridge/conversation-card-review-queue.py /home/guidingl/.codex/tmp/memory-bridge/conversation-card-previews/conversation-card-preview-YYYYMMDD-HHMMSS.jsonl
python /home/guidingl/.codex/automations/memory-bridge/guiding-light-perspective-tender.py /home/guidingl/.codex/tmp/memory-bridge/conversation-card-previews/conversation-card-preview-YYYYMMDD-HHMMSS.jsonl
python /home/guidingl/.codex/automations/memory-bridge/conversation-git-link-preview.py /home/guidingl/.codex/tmp/memory-bridge/conversation-card-previews/conversation-card-preview-YYYYMMDD-HHMMSS.jsonl
```

Create the actionable lesson plan:

```bash
python /home/guidingl/.codex/automations/memory-bridge/conversation-lesson-planner.py
```

Review the integrated status:

```bash
python /home/guidingl/.codex/automations/memory-bridge/memory-bridge-report.py --print
```

## How To Apply A Ready Lesson

1. Open the latest lesson plan under:

```text
/home/guidingl/.codex/tmp/memory-bridge/conversation-lesson-plans
```

2. For each `ready_for_manual_action` item, read only the card hash, pattern, target layer, suggested files, rule, action, verification, blockers, and git warning metadata.

3. For recall-driven lessons, record the source pointer, date, redaction
   status, current-verification status, and reason. Do not paste raw transcript
   text.

4. Edit the smallest appropriate durable file.

5. Add or reference the verifier that proves the lesson is active.

6. Rerun the relevant tests or report.

7. If the lesson is project-specific, update the project index/workstream rather than global state.

7. If the result needs to be posted somewhere visible, hand it to
   [Codex Thread Delivery Bridge](codex-thread-delivery-bridge.md). Do not
   embed delivery logic in the lesson planner or pretend Codex Thread posting
   is available before a callable adapter is verified.

## Current Pattern Map

Use these default mappings unless newer evidence says otherwise:

- `locally_twisted_reality_verification`: LT docs are claims; verify live ERPNext/Frappe state before relying on them.
- `locally_twisted_finance_gates`: finance/payroll automation starts as drafts, reminders, and approval gates.
- `locally_twisted_design_studio_boundary`: current style guide/live site wins; PlayCanvas owns experience; Frappe owns business workflow.
- `multi_machine_routing`: Banebook is the Linux-first daily/control laptop;
  Wardenclyffe remains the remote Windows workhorse for existing heavy/server
  work unless a project migration says otherwise.
- `windows_cleanup_surgical_scope`: inventory first, preserve protected work, then take narrow approved action.
- `codex_conversation_learning_loop`: reviewed indexed conversations become system changes only through this loop.
- `codex_framework_routing`: translate lessons into Codex-native layers instead of copying Claude-era mechanics wholesale.

## External Design Checks

The external research added three guardrails:

- Filtered semantic retrieval needs structured metadata and payload indexes. Future `codex_memory_v1` points should include fields such as `project_slug`, `topics`, `source_type`, `speaker_attribution_status`, `redaction_status`, `retention_class`, and `created_at`, with indexes on fields used for filtering.
- A lightweight SQLite control plane is appropriate for ledgers, metadata, local search views, and audit state. Do not make Qdrant the first home for raw or ambiguous conversation material.
- Treat this as a governance loop: map what the lesson means, measure risk and evidence, manage promotion, and keep governance visible through reports.

## Failure Modes

- Symptom: a memory says "the user wants X" but the card had no explicit user confirmation. Fix: hold or rewrite as Codex-owned responsibility.
- Symptom: a lesson is globally promoted but only applies to one client repo. Fix: move it to the project `AGENTS.md`, project capability index, or workstream.
- Symptom: the report shows a ready lesson but no behavior changes. Fix: apply it to a durable file and add a verifier.
- Symptom: the system stores more text but behaves the same. Fix: reject text-only memory; require `trigger -> rule -> action -> verification -> owner`.
- Symptom: Qdrant search finds semantically relevant but unsafe cards. Fix: keep writes disabled until redaction, speaker, and perspective gates pass.

## Source Notes

- Qdrant payload/indexing docs: https://qdrant.tech/documentation/concepts/payload/ and https://qdrant.tech/documentation/manage-data/indexing/
- SQLite FTS5 docs: https://www.sqlite.org/fts5.html
- OpenAI evals API reference: https://developers.openai.com/api/reference/resources/evals
- NIST AI RMF core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
