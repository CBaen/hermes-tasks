---
id: wardenclyffe-uma-worker-lanes-v1
name: Wardenclyffe Uma Worker Lanes v1
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: local-only Wardenclyffe Uma/Codex/Hermes worker-lane rules
currently_true: v1.1 named dispatch gates documented; broad dispatch remains task-approval-gated
last_verified: 2026-06-13T19:48:26-06:00
tags:
  - wardenclyffe
  - worker-lanes
  - codex
  - hermes
  - autonomy
  - approvals
---

# Wardenclyffe Uma Worker Lanes v1

## What it helps with

Use this when Wardenclyffe is running always-on Uma/Hermes work and a task needs
safe worker lanes instead of one broad unsupervised agent.

This recipe is approved for local-only setup and smoke testing under the
2026-06-13 user boundary: no external sends, no account changes, no production
deploys, no money movement, no secrets, and no destructive cleanup.

As of 2026-06-13T19:48:26-06:00, the named dispatch-gate matrix below is
documented for future Wardenclyffe workers. It does **not** turn on broad
autonomous dispatch by itself. Each non-trivial worker still needs a concrete
Kanban card, route record, allowed actions, evidence bar, and stop condition.

## Source hierarchy

1. Live verification from Wardenclyffe, Banebook, Hermes, Codex, Git, tests, or
   services.
2. Machine/project instruction files:
   - `/home/guidingl/AGENTS.md`
   - `/home/guidingl/projects/hermes-tasks/AGENTS.md`
   - `/home/guidingl/projects/hermes-tasks/SOURCE-OF-TRUTH.md`
3. Agent coordination files:
   - `/home/guidingl/agent-coordination/LIVE-BOARD.md`
   - `/home/guidingl/agent-coordination/TASK-LIFECYCLE.md`
   - `/home/guidingl/agent-coordination/HUMAN-CONTINUATION-CONTRACT.md`
4. Capability roots:
   - `capabilities-collaboration-autonomy/`
   - `capabilities-agent-infrastructure/`
   - `capabilities-connections-control/`
5. Prior handoffs, memory, and conversation summaries only as clues until
   verified.

## Default route record

Before spawning or instructing a worker, record the compact route:

```markdown
Mode: subagent-brief / triadic-review / construction-review / local smoke
Decision needed: <what this lane decides or proves>
Scope owner: Wardenclyffe Uma runtime, Banebook cockpit, or specific project
System/project/runtime classification: <remote Wardenclyffe | single project | runtime/cache/auth | external account/service>
Allowed actions: <exact safe actions>
Forbidden actions: <hard stops>
Evidence bar: <command/test/artifact required>
Stop condition: <when to pause and return to Guiding Light>
```

For delegated lanes, add:

```markdown
Lane owner:
Artifact path:
Coordination path:
File/system ownership:
Dependencies:
Anti-overlap rule:
Escalation trigger:
```

## Core rules

- Prefer one to three narrow lanes over a swarm.
- Parent Uma owns synthesis and verification. Worker output is evidence, not
  proof.
- Use isolated context and exact source paths.
- Keep durable outputs in project docs/artifacts; keep runtime auth/session/logs
  out of docs.
- Use `/home/guidingl/agent-coordination` for substantial, overlapping, or
  resumable work claims.
- Do not let two workers edit the same files, feature lane, generated assets,
  database, service, deployment path, or customer-facing surface in parallel.
- If overlap appears, stop the lane and escalate.

## Named Wardenclyffe dispatch matrix v1.1

Use these lane names when creating or routing Wardenclyffe worker cards. The
lane name is the job shape, not a standing permission grant.

### Green / Yellow / Red meanings

- **Green**: Uma may prepare, inspect, draft, test, and write local artifacts
  within the exact scope. No final external action.
- **Yellow**: Requires explicit task-specific approval before the worker starts
  or before it continues past read-only/prep. Examples: logged-in account pages,
  private inboxes, client data, service restarts, real financial records, or
  anything that could affect a person/business if wrong.
- **Red**: Hard stop. The worker must not do this; return to Guiding Light or
  parent Uma for final approval/handling.

| Lane / profile | Green actions | Yellow actions | Red hard stops | Minimum evidence |
|---|---|---|---|---|
| `finance-clerk` | Local specs, fake/sample ledgers, invoice/checklist drafts, reconciliation templates, finance pipeline design. | Read-only review of a named finance/accounting/email/Sheet source after explicit approval for that account and time window. | Move money, place orders, file taxes, submit forms, change books/records, change payment settings, sign, or store raw sensitive data in repo docs. | Data-source label (`fake`, `user-provided`, `account-derived`), artifact path, blocked approvals list. |
| `researcher` | Public web/docs research, local repo search, comparison notes, cited summaries. | Logged-in/private pages or user-provided sensitive files with explicit scope. | Messages/forms/posts/purchases, account/provider choices, scraping private data into durable docs. | Source URLs/paths, access date, verified/unverified labels. |
| `builder` | Scoped local code/doc edits, tests, builds, dry-run scripts, reversible local setup. | Multi-repo edits, staging/client-system changes, service restarts, dependency upgrades, or anything with release impact. | Production deploy, DNS, public release, secret movement, destructive deletion, Docker prune, backup removal, unrelated cleanup. | Changed-file list, test/build output, rollback note, dirty-worktree note. |
| `verifier` | Read-only review of diffs, tests, artifacts, policy boundaries, security/privacy risks. | Reproduction using private data/accounts or live services. | Mutating the thing it verifies, approving its own work as final proof, release/deploy decisions. | PASS/FAIL/WARN findings with file/command citations and unresolved risks. |
| `client-ops` | Draft client emails, SOPs, checklists, website/module notes, non-sent support plans. | Read-only client account/project inspection after explicit client/scope approval. | Send client messages, mutate CRM/ERP/client site/data, submit forms, publish, deploy, change DNS/billing/security. | Client/scope label, draft artifact, no-send confirmation, next approval needed. |
| `life-admin` | Personal planning, forms checklists, schedules, summaries, draft messages, local trackers. | Logged-in account/inbox/portal read-only work after explicit account/scope approval. | Submit applications/forms, send messages, cancel/renew services, purchases, legal/medical/financial attestations, account security changes. | Source of facts, draft/checklist path, exact user decisions remaining. |
| `browser-worker` | Public browsing, local WebUI checks, read-only DOM/CDP inspection, screenshot/HTML evidence. | Logged-in pages, private dashboards, account settings, or XRDP/browser session control with explicit scope. | Final submit, subscribe/cancel, payment, wallet, MFA/security changes, password manager export, external send/post. | URL/tab identity, actions taken, screenshot/DOM evidence when useful, no-final-submit confirmation. |

### Dispatch readiness checklist

A Wardenclyffe worker card may move out of blocked only when the card body or
comment contains:

1. Lane/profile name from the matrix above.
2. Workspace/path and machine ownership (`Wardenclyffe runtime`, `Banebook
   cockpit`, or a specific project path).
3. Green/yellow/red classification and the exact allowed actions.
4. Evidence artifact path and verification command.
5. Stop condition and escalation trigger.
6. Anti-overlap statement: what files/services/accounts the worker must not
   touch because another lane owns them or because they are out of scope.
7. Model/provider rule when Hermes is used: on Nous Free subscription, use an
   explicit selectable free model such as `stepfun/step-3.7-flash:free` until
   credits/default model are intentionally changed.

### Dispatch limits now in force

- Start with one worker, not a swarm, unless the user explicitly approves a
  multi-worker graph.
- Prefer local-only, no-tool or minimal-tool smokes before real work.
- Workers may prepare and verify; parent Uma owns synthesis and closeout.
- Yellow work pauses for explicit approval before logged-in/private/live action.
- Red work is never delegated as an autonomous worker task.

## Lanes

### Researcher

Allowed:

- public web/documentation research;
- local repo/document search;
- comparison notes with cited sources;
- non-secret summaries and decision prep.

Forbidden:

- logging into accounts;
- reading inboxes or private pages unless separately approved;
- form submissions, messages, posts, purchases, payments, or account mutations;
- copying secrets or raw private transcripts into artifacts.

Must verify:

- cite source paths/URLs and date;
- label unverified claims.

### Builder

Allowed:

- scoped local file edits in the assigned repo/path;
- tests, builds, syntax checks, smoke checks;
- reversible local-only setup already approved by Guiding Light.

Forbidden:

- production deploys;
- provider/staging/live mutations without fresh approval;
- pushes to deploy-triggering remotes without release-gate review;
- broad staging, deletion, pruning, credential movement, or unrelated dirty-file cleanup.

Must verify:

- exact changed files;
- test/build command and result;
- diff cleanliness or known unrelated dirt.

### Reviewer

Allowed:

- inspect diffs, tests, contracts, security, privacy, and edge cases;
- produce findings and recommended fixes;
- challenge assumptions in triad/construction-review lanes.

Forbidden:

- mutating code unless explicitly assigned as fixer;
- approving its own output as final proof;
- widening scope from review into deploy/account actions.

Must verify:

- cite exact files/commands reviewed;
- distinguish blocker, warning, and note.

### Ops

Allowed:

- health/status checks;
- service/log summaries without dumping secrets;
- local-only scheduled-job smoke checks;
- reversible user-service checks when already approved.

Forbidden:

- deleting/pruning backups, Docker volumes, images, databases, or runtime state;
- exposing ports publicly;
- changing account/security settings;
- restarting income-critical services without explicit approval.

Must verify:

- command output summary;
- service state and next safe action.

### Finance/Admin

Allowed:

- draft workflows, summaries, templates, checklists, and reconciliation plans;
- local-only sample artifacts with fake/non-sensitive data.

Forbidden:

- private financial account access unless separately approved for that account;
- Gmail/Sheets/account inspection without separate approval;
- sending messages, submitting forms, moving money, signing, ordering, or changing records;
- storing secrets or sensitive raw data in project docs.

Must verify:

- whether data is fake/sample, user-provided, or account-derived;
- what remains blocked for user approval.

## Triad shape

For consequential decisions, use a real triad only when runtime support exists
and the user requested/approved delegation. Label the output as either:

- `real multi-agent triad`; or
- `solo structured triad`.

Suggested lenses:

1. Practical execution lens.
2. Safety/security/privacy lens.
3. Business/user-impact lens.

## Current standing boundary

This v1.1 is approved for local-only worker-lane setup, one safe Codex smoke,
one safe Hermes free-model smoke, and documented dispatch-gate design. It does
not grant standing approval for logged-in account actions, external sends,
production/client changes, money, secrets, destructive cleanup, or broad
multi-worker autonomous dispatch.

## Stop or escalate when

- A worker needs credentials, account login, private pages, inboxes, raw logs,
  `.env`, OAuth/API tokens, browser cookies, wallet keys, or password stores.
- A task would send, submit, purchase, post, deploy, expose ports, mutate client
  systems, move money, sign, delete destructively, prune Docker, remove backups,
  or change account security.
- The provider/login choice is ambiguous.
- Another active claim owns the same files, feature lane, runtime, or
  customer-facing outcome.
- Verification cannot be performed with the allowed tools.

## First smoke-test contract

The first Wardenclyffe Codex worker smoke test must be local-only and produce a
non-secret artifact under `/home/guidingl/projects/hermes-tasks/artifacts/` or
`/tmp`. It may inspect approved source docs and run harmless commands. It must
not edit production/client repos, read secrets, send messages, submit forms,
change accounts, deploy, prune, delete backups, or mutate services.

The first Wardenclyffe Hermes model-backed smoke must also be local-only and
no-tools unless a tool is explicitly required. On the verified Nous Free
subscription, use an explicit free model override such as
`stepfun/step-3.7-flash:free`; the configured default
`anthropic/claude-opus-4.6` is credit-gated unless credits/plan/default model
are intentionally changed.
