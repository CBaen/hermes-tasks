---
id: codex-memory-bridge
name: Codex Memory Bridge
schema_version: 2.0
level: recipe
maturity: candidate
scope: machine-wide Codex memory and prior-session retrieval
currently_true: unknown
verification_level: 2
last_verified: 2026-05-23
evidence_quality: direct
successful_uses: 4
failed_uses: 0
regressions: 0
depends_on: []
used_by:
  - conversation-learning-loop
  - codex-thread-delivery-bridge
  - guiding-light-perspective-tender
tags:
  - memory bridge
  - qdrant
  - codex sessions
  - claude history
  - conversation retrieval
  - redaction
---

# Codex Memory Bridge

Latest feature handoff:
`/home/guidingl/codex-framework/framework/workstreams/universal-ai-conversation-memory-gpu-indexing-2026-05-22.md`.

Use this when a Codex session needs awareness of prior Claude-era conversations, compressed memories, old project memories, Qdrant archives, or current Codex session continuity.

## Policy

If a migrated `/home/guidingl/.claude` workspace or Claude archive exists, treat
it as a protected legacy source. Read it only when the task requires legacy
evidence. Do not edit, move, delete, rewrite, prune, or normalize it without
explicit approval for the exact action.

Do not print or copy secrets. Skip files whose names indicate credentials, tokens, OAuth state, `.env`, `.mcp.json`, auth state, API keys, or private keys.

Old memory is evidence, not proof. Use it to find likely context, then verify against current files, git state, Qdrant, Docker, or the live system when the answer depends on reality.

## Tools

Primary bridge folder:

```text
/home/guidingl/.codex/automations/memory-bridge
```

Metadata inventory:

The older Windows inventory script is preserved in the bridge folder as
`inventory-memory-sources.ps1`, but no Banebook Bash replacement is verified in
this card. Do not use the PowerShell script as the current Linux default.

Semantic search:

```bash
python /home/guidingl/.codex/automations/memory-bridge/codex-memory-search.py "search terms"
```

Metadata-only semantic search:

```bash
python /home/guidingl/.codex/automations/memory-bridge/codex-memory-search.py "search terms" --metadata-only
```

The search tool dedupes repeated point IDs across collections and redacts secret-like metadata or snippets as `REDACTED_SECRET_RISK`. Use `--metadata-only` first for broad discovery.

Decision recall wrapper:

Legacy docs referenced `codex-recall.py`, but that wrapper was not present in
`/home/guidingl/.codex/automations/memory-bridge` during the 2026-06-08
Banebook migration edit. Until a Linux-native wrapper is restored and verified,
use metadata-only `codex-memory-search.py` first, then fetch only vetted point
IDs through `conversation-qdrant-fetch.py`.

Use `codex-recall.py` before manual search/fetch when the task involves a prior
decision, pasted conversation detail, disputed memory, handoff recovery, or
repeated user correction. It is read-only, searches `ai_conversations_v1`
metadata first, fetches only a small number of safe exact chunks, and returns a
compact evidence pack with one of: `conversation_evidence_found`, `not_found`,
`conflicting`, `coverage_incomplete`, or `unsafe_or_ambiguous_fetch`.
Fetched chunks must pass direct relevance checks before the wrapper can report
`conversation_evidence_found`; they also need explicit expected account/project
scope, a trusted account label (`personal` or `business`), and one exact
matching associated project root. Unscoped recall is discovery only and must
not fetch transcript text or confirm a decision. Generic queries, weak matches,
missing, ambiguous, or mismatched provenance, unfetched top results, and fetch
warnings remain incomplete or conflicting. Fetched excerpts are omitted by
default; use
`--include-excerpts` only when a short redacted excerpt is needed for review.
Use `--include-redacted-text` only for local debugging or review artifacts that
can safely contain a redacted exact chunk; redaction is not a confidentiality
classifier. Excerpt flags still omit text from unscoped,
provenance-incomplete, ambiguous, or provenance-mismatched hits. Completed
recall runs exit `0` by default; use `--strict-status-exit` only when automation
intentionally wants incomplete, unsafe, or conflicting recall to return nonzero.

List collections:

```bash
python /home/guidingl/.codex/automations/memory-bridge/codex-memory-search.py --list-collections
```

## Current Architecture

- Claude raw history: migrated Claude archives when present. `/home/guidingl/.claude`
  was not present during the 2026-06-08 Banebook migration edit.
- Codex raw history: `/home/guidingl/.codex/sessions`.
- Durable Codex summaries: `/home/guidingl/.codex/memories`.
- Searchable vector layer: local Qdrant at `http://localhost:6333`.
- Embedding model: Ollama `mxbai-embed-large:latest`, 1024 dimensions.

The bridge searches already-indexed Qdrant collections and now has an explicit
guarded writer for approved local `ai_conversations_v1` batches. Default ledger
scans remain dry-run. Do not confuse the 20-point `ai_conversations_v1` pilot
with complete backlog coverage.

Account-profile indexing and command-center routing are cross-repo work. The
memory/indexing source of truth is this capability plus the workstream linked
above. Older Wardenclyffe docs referenced an account-router handoff at
`C:\Users\baenb\projects\account-silo-router\workstreams\codex-account-command-center-2026-05-23.md`;
that file was not present at `/home/guidingl/projects/account-silo-router/...`
during the 2026-06-08 Banebook migration edit, so verify before relying on that
handoff.

Actionable lesson promotion is handled by [Conversation Learning Loop](conversation-learning-loop.md). Use it when reviewed conversation cards should become memories, capabilities, skills, project guides, verifiers, or workstream updates.

First Codex-session indexing milestone:

- `/home/guidingl/.codex/automations/memory-bridge/index-policy.json`
- `/home/guidingl/.codex/automations/memory-bridge/codex-session-indexer.py`
- `/home/guidingl/.codex/automations/memory-bridge/state/source-ledger.sqlite`
- `/home/guidingl/.codex/automations/memory-bridge/git-discrepancy-audit.py`

This milestone is dry-run by default. It scans AI conversation JSONL files,
writes source metadata to the local ledger when `--update-ledger` is used, and
keeps Qdrant writes disabled unless the separate guarded writer is called with
explicit write flags. It does not print conversation bodies or raw session
filenames.

Codex account-isolated roots are part of the policy surface:
`/home/guidingl/.codex-accounts/personal/...` and
`/home/guidingl/.codex-accounts/business/...`. Source-ledger rows, Qdrant chunk
rows, and `ai_conversations_v1` payload metadata should carry `account_profile`
as `shared`, `personal`, or `business` when the source root is known.

Current account mapping:

- `personal`: `cameronbpaul@gmail.com`
- `business`: `locallytwisted@gmail.com`
- `shared`: mixed, legacy, or unproven Codex sources

For routine audits, prefer summary-only JSON:

```bash
python /home/guidingl/.codex/automations/memory-bridge/codex-session-indexer.py --update-ledger --json --summary-only
```

Latest verified ledger status on 2026-05-22: 8,107 source rows across Claude
7,210, Codex 684, and Paperclip 213; Qdrant writes planned by the ledger scan
remain 0. A separate guarded pilot created `ai_conversations_v1` with 20 clean
points after stale pilot vectors were deleted.

Latest verified account-profile indexing status on 2026-05-23:

- `ai_conversations_v1` contains 4,500 points.
- All 1,500 Codex seed points carry `account_profile=shared`.
- Claude and Paperclip seed points intentionally remain account-profile
  `unspecified`.
- A synthetic temp-collection smoke test wrote one personal and one business
  Codex chunk, searched Qdrant, saw `metadata.account_profile=business`, found
  no raw payload text keys, and deleted the temp collection/files.
- Canonical memory-bridge tests passed: `76`.
- Account router tests passed: `28`.

Before any Qdrant write batch, prove GPU placement:

```bash
python /home/guidingl/.codex/automations/memory-bridge/ollama-gpu-health.py --embed --json
```

Approved write batches must use the guarded writer:

```bash
python /home/guidingl/.codex/automations/memory-bridge/conversation-qdrant-indexer.py --write-qdrant --allow-private-embeddings --batch-size 4 --max-chars 700 --json
```

Metadata-only payload backfills are allowed through the same writer when they
only set `account_profile` from the local chunk ledger and do not embed or store
conversation text:

```bash
python /home/guidingl/.codex/automations/memory-bridge/conversation-qdrant-indexer.py --backfill-account-profile-payloads --write-qdrant --json
```

`ai_conversations_v1` payloads must not contain raw text or body fields. Long
events must split, not truncate, and each chunk must keep `conversation_id`,
`account_profile`, `source_hash`, `path_hash`, `event_start`, `event_end`,
`chunk_part`, and `chunk_offset`.

Qdrant search results must expose metadata fields such as `account_profile`,
`source_root`, `conversation_id`, and chunk coordinates. Storing the field is
not enough; agents need to see it in search results before relying on account
provenance.

Fetch only the needed local source chunk after metadata search:

```bash
python /home/guidingl/.codex/automations/memory-bridge/conversation-qdrant-fetch.py <point-id> --show-text
```

Use direct fetch only when you already have a vetted `ai_conversations_v1`
point ID and need the exact local chunk. Do not persist raw fetched transcript text into memories,
capabilities, workstreams, or reports; promote only distilled behavior with a
source pointer and current-verification status.

`git-discrepancy-audit.py` is also read-only. It uses git metadata and changed-path lists to find auto-commit clusters, vague commit messages, bulk session flushes, and message/diff mismatches. It does not read file contents or modify repositories.

When `git-discrepancy-audit.py --update-ledger` is used, it writes only metadata to:

```text
/home/guidingl/.codex/automations/memory-bridge/state/action-ledger.sqlite
```

Sensitive-looking path names and commit messages are redacted before ledger storage.

`memory-bridge-report.py` turns the source and action ledgers into a local markdown report under:

```text
/home/guidingl/.codex/tmp/memory-bridge/reports
```

The report is a metadata summary only. It includes the source ledger, action ledger, latest conversation/git link health, and latest conversation-card review queue when those artifacts exist. It does not read conversation bodies, inspect file contents, copy git diffs or commit messages, write Qdrant, or change repositories.

`conversation-card-preview.py` is the conversation-first bridge step. It creates local memory-card drafts from Codex session JSONL files under:

```text
/home/guidingl/.codex/tmp/memory-bridge/conversation-card-previews
```

The preview applies redaction before writing cards and keeps Qdrant writes at zero. Review these preview cards before approving any `codex_memory_v1` Qdrant write path.

Some user-provided conversations may include clients or other people without clear speaker labels. The preview marks these as `speaker_formatting_required` when explicit speaker labels or likely third-party conversation language appears. Do not promote these cards into long-term search as settled memory until the speaker ambiguity is formatted or accepted as unresolved.

`conversation-card-review-queue.py` is the pre-storage gate for conversation cards. Run it against a preview JSONL before any future Qdrant promotion path:

```bash
python /home/guidingl/.codex/automations/memory-bridge/conversation-card-review-queue.py /home/guidingl/.codex/tmp/memory-bridge/conversation-card-previews/conversation-card-preview-YYYYMMDD-HHMMSS.jsonl
```

The queue writes metadata-only review artifacts under:

```text
/home/guidingl/.codex/tmp/memory-bridge/conversation-card-review-queues
```

It separates cards into `eligible_after_preview_review`, `hold_for_speaker_formatting`, `hold_for_redaction_review`, and `hold_for_redaction_and_speaker_review`. It does not write Qdrant and intentionally marks `qdrant_eligible_now` as false for every card. Treat this as a human/agent review checkpoint, not an automatic approval.

`guiding-light-perspective-tender.py` is the protective Codex-native GL Proxy layer. It is not a persona and does not impersonate Guiding Light. Its job is to protect the user's perspective and scope from agent overreach, false certainty, privacy risk, memory distortion, and engineering decisions being pushed onto the user when Codex should own them.

Run it against the same conversation-card preview before promotion planning:

```bash
python /home/guidingl/.codex/automations/memory-bridge/guiding-light-perspective-tender.py /home/guidingl/.codex/tmp/memory-bridge/conversation-card-previews/conversation-card-preview-YYYYMMDD-HHMMSS.jsonl
```

It writes metadata-only artifacts under:

```text
/home/guidingl/.codex/tmp/memory-bridge/guiding-light-perspective-reviews
```

It flags designer/business-owner scope signals, possible false priorities, agent anomaly/overreach signals, unverified claims about the user's perspective, and engineering detail scope drift. It does not declare `GL confirmed` unless the source card contains explicit user confirmation.

`conversation-promotion-planner.py` is the dry-run planner for reviewed cards. Run it after a review queue and perspective review exist:

```bash
python /home/guidingl/.codex/automations/memory-bridge/conversation-promotion-planner.py
```

The planner writes metadata-only artifacts under:

```text
/home/guidingl/.codex/tmp/memory-bridge/conversation-promotion-plans
```

It identifies `candidate_after_review_approval` cards and keeps held cards blocked for redaction, speaker formatting, missing perspective review, or held perspective review. It does not include conversation excerpts and does not write Qdrant.

`memory-bridge-retention.py` is the dry-run retention planner for generated memory-bridge artifacts:

```bash
python /home/guidingl/.codex/automations/memory-bridge/memory-bridge-retention.py
```

It uses:

```text
/home/guidingl/.codex/automations/memory-bridge/retention-policy.json
```

The built-in policy keeps ledgers indefinitely, keeps the latest 2 generated runs per artifact family, keeps the latest inventory snapshot, marks older generated artifacts and Python `__pycache__` folders as prune candidates, and requires explicit approval before destructive cleanup. The retention planner has no apply/delete mode.

`conversation-git-link-preview.py` links conversation card previews to project repos through `cwd_hint` and the action ledger. It stores only repo/count/flag context, not diffs, changed paths, commit messages, or conversation bodies. Use it to support project-aware retrieval without bloating memory with data GitHub already tracks.

## Practical Workflow

1. Run a verified Linux-native inventory or report command when source freshness
   matters; do not assume the legacy PowerShell inventory is usable on Banebook.
2. Use metadata-only search first if the user has not asked to inspect exact conversation text.
3. Use snippets only when needed to identify the right prior context.
4. If a hit affects an implementation decision, verify against the current source of truth before acting.
5. If current Codex conversations need to become searchable, build a Codex-native indexer rather than re-enabling the old Claude scheduled task unchanged.
6. Before writing any Codex session data to Qdrant, run the dry-run indexer and inspect counts, skipped files, redaction-risk files, and planned writes.
7. Before promoting conversation-card previews, generate the review queue and resolve or intentionally accept redaction and speaker-formatting holds.
8. Run the Guiding Light perspective tender and resolve cards where Codex may be distorting the user's perspective, creating false priorities, pushing engineering scope upward, or introducing agent-side weirdness.
9. Run the promotion planner to estimate candidate count and holds while keeping Qdrant writes at zero.
10. Run the retention planner before cleanup discussions so generated artifacts have an explicit keep/prune map.
11. Generate the memory bridge report after queue/link previews so one local artifact shows source-session health, git-link health, and storage-readiness holds.
12. When reconstructing old work, use the git discrepancy audit as an evidence map, then verify important claims against current repo files or live systems before acting.
