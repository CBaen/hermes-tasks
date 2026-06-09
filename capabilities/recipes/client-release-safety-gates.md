---
id: client-release-safety-gates
name: Client Release Safety Gates
schema_version: 2.1
profile: governed
level: recipe
maturity: candidate
scope: agency-wide client release workflow
currently_true: unknown
verification_level: 1
last_verified: 2026-05-10
evidence_quality: direct
successful_uses: 0
failed_uses: 0
regressions: 0
depends_on: []
used_by: []
tags:
  - client release
  - preflight
  - staging
  - live cutover
  - rollback
  - fail loud
  - status snapshot
---

## What it does

Defines the agency-wide release gate for client work: preflight first, staging
second, audited client review third, live cutover last. Each stage creates a
status snapshot so agents can compare source, staging, and live state before a
change harms a client business.

## When to reach for it

Use this for any client app, site, ERP, commerce flow, DNS cutover, hosting
migration, app upgrade, data migration, payment/email change, or production
configuration change.

## How to use it

No live push is allowed from an unverified or dirty source. The gate is:

1. Run preflight and create a preflight snapshot.
2. Deploy the exact intended artifact/source to staging.
3. Create a staging snapshot and run the staging audit.
4. Resolve every blocker in staging.
5. Get explicit client or owner approval for the reviewed staging state.
6. Create a live-before snapshot, deploy, then create live-after and post-live
   snapshots.
7. Compare staging-final, live-before, and live-after snapshots before calling
   the release safe.

Every failure becomes one of three written states:

- `BLOCKER`: stop the release and fix in source, then return to preflight.
- `APPROVED DEFERRAL`: owner accepts a noncritical issue with written scope,
  rollback, and follow-up date.
- `NOT IN SCOPE`: unrelated to this release and backed by evidence.

Anything else is uncertainty and must stop the release.

2026-05-23 release-control addition from the Locally Twisted Frappe Cloud
failure: written states are not enough unless release commands enforce them.
After one provider/bootstrap/deploy failure, classify the failure and create a
guard before retry. After two related failures, all provider mutation stops
until a fresh artifact-owned release plan is approved. If Guiding Light says
stop, execution stops immediately and only read-only forensics may continue
until release execution is explicitly reopened.

Project implementation rule: a frozen release must have a normal local command
that future agents can run before provider work. The command should prove the
active release lock, typed provider payload contract, required-doc receipt
contract, failure circuit breaker, artifact-owned witness packet, and
readiness-claim wording. Locally Twisted's first implementation is
`npm run test:release-prevention`.

## Required status snapshot fields

Use `tools/release_status_snapshot.py` when available. A sufficient snapshot
records:

- repo path, branch, commit, remote, dirty status, staged files, untracked files
- release label and environment name
- source/app version or deployed artifact identifier
- watched file hashes for lockfiles, migration files, fixtures, hooks, deploy
  manifests, and other release-critical source
- optional environment key names only, never values
- target URL, route status, redirect target, title, response hash, and failures
- migration, fixture, scheduler, queue, and report commands that ran
- backup or rollback identifier
- audit report path and approval reference

Do not store secrets, database dumps, private customer records, OAuth/session
tokens, or raw production logs in a snapshot.

## Preflight gate

Preflight must fail loudly when any of these are true:

- branch or repo rules are violated
- release scope is not written down
- source commit is not known or cannot be reproduced
- worktree contains unrelated or unreviewed changes
- dependencies or lockfiles changed without explanation
- migrations, fixtures, or schema changes have no staging rehearsal plan
- payment, email, DNS, authentication, permissions, or client data paths are
  touched without a specific test plan
- backup and rollback are missing
- staging target is not identified
- required secrets are unknown, missing, or only proven by reading secret values
- a release/forensic freeze lock exists for the target
- the agent has not produced required-doc receipts for active forensics,
  queue, handoff, capability, and release-plan files
- the provider payload shape is unvalidated or contains stringified nested
  JSON where typed objects/arrays are required
- an artifact-owning witness/triad requirement exists but only advisory
  comments are present

## Staging gate

Staging must be a real rehearsal of live, not a cosmetic preview. It should
prove routes, forms, automations, reports, documents, auth/roles, emails,
payments in the correct mode, logs, scheduler jobs, and migrations. Any staging
failure that could affect a customer, contractor, accountant, vendor, owner, or
operator blocks live release.

## Live gate

Live release is allowed only after:

- staging audit is passing or has explicit approved deferrals
- client/owner approval is recorded
- production backup exists and rollback is executable
- production secrets, DNS, SSL, email, payment mode, and domain routing are
  verified without exposing secret values
- the artifact/source being deployed matches the staging-approved state
- a named human or agent is watching logs and customer-facing flows after cutover

If a fix is needed during live preparation, fix source, rerun preflight, deploy
to staging, rerun the relevant staging audit, and reapprove. Do not make
untracked production-only fixes except to roll back or stop active damage.

## What it depends on

- Project `AGENTS.md` and nearest capability roots.
- Hosting-provider documentation for target-specific deployment commands.
- Repo-specific verifier scripts and migration commands.
- A snapshot tool or equivalent written status artifact.

## Rollback / revalidation path

If a release breaks, mark this recipe use as failed evidence, capture the failed
snapshot comparison, and identify which gate missed the issue. The next release
must treat that missed class as a hard preflight or staging audit item until
three later releases pass with direct evidence.

## Adapter notes

For Codex, prefer the paired skills:

- `agency-preflight-gate`
- `agency-staging-audit`
- `agency-staging-to-live`

For retired OpenClaw records or other agents, use this capability as the policy
contract and translate the three gates into that agent's native skill or
workflow format.
