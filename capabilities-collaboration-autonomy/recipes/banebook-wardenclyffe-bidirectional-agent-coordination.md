---
id: banebook-wardenclyffe-bidirectional-agent-coordination
name: Banebook Wardenclyffe Bidirectional Agent Coordination
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: safe bidirectional automation between Banebook cockpit and Wardenclyffe always-on runtime
currently_true: verified transport; dispatch still approval-gated by lane
last_verified: 2026-06-14
tags:
  - banebook
  - wardenclyffe
  - automation
  - ssh
  - worker-lanes
  - tailscale
---

# Banebook Wardenclyffe Bidirectional Agent Coordination

## What this means practically

Banebook and Wardenclyffe can now talk to each other over Tailscale/OpenSSH, so agents can coordinate work across both computers without copying runtime secrets or taking over the user's physical keyboard/mouse.

Verified again on 2026-06-14T13:29:12-06:00:

```text
Banebook -> Wardenclyffe: WARDENCLYFFE guidingl
Wardenclyffe -> Banebook: BANEBOOK guidingl
```

## Roles

- **Banebook**: daily cockpit, user/live browser, review, local desktop/file handoff, human-facing decisions.
- **Wardenclyffe**: always-on Hermes runtime, gateway/dashboard/scheduler, long-running workers, heavier jobs, worker-lane execution.
- **Samsung S24**: possible mobile edge device/personal-phone surface, but not an agent host until the phone is online and an approved service is installed/enabled.

## Default architecture

1. Use Git for shared source/docs, not blind folder sync.
2. Use SSH/Tailscale for command/control checks.
3. Use lane cards and explicit route records for automated workers.
4. Keep account/security/money/client/live-system/destructive actions behind explicit approval.
5. Keep secrets, auth stores, session files, browser profiles, raw logs, and private mobile data out of repo docs and cross-machine copies.

## Approved-by-default green work

When a task has a clear lane and workspace, agents may do:

- read-only health checks;
- local repo/file inspection;
- drafting docs, plans, scripts, manifests, and capability cards;
- local-only tests, smokes, builds, and verifiers;
- reversible setup already documented in the lane;
- evidence artifacts that do not contain secrets/private raw data.

## Yellow work requiring task-specific approval

Pause and get approval before:

- logged-in account pages, inboxes, private dashboards, private customer/client data;
- editing `authorized_keys`, Tailscale ACLs, OAuth apps, API keys, provider auth, or account security settings;
- restarting services with income/client impact;
- phone pairing, Android debug access, SMS/notification access, or remote mobile control;
- staging/client/public deployment changes.

## Red hard stops

Do not delegate or automate:

- money movement, purchases, trades, crypto signatures, forms, legal attestations;
- final external sends/posts/uploads/submissions;
- production deploys or DNS changes;
- deleting/pruning backups, Docker volumes, databases, account records, or phone data;
- copying secrets/auth/session/browser/mobile state between devices.

## Route record template

Use this before instructing a worker:

```markdown
Machine owner: Banebook cockpit / Wardenclyffe runtime / Samsung S24 mobile edge
Lane: researcher / builder / verifier / browser-worker / client-ops / life-admin / finance-clerk
Workspace/path:
Allowed actions:
Forbidden actions:
Data sensitivity:
Evidence required:
Stop condition:
Anti-overlap rule:
```

## Current verifier commands

```bash
wardenclyffe-ssh 'hostname; whoami'
wardenclyffe-ssh 'ssh -o BatchMode=yes banebook "hostname; whoami"'
python tools/check_source_of_truth_parity.py
```

## 2026-06-14 security hardening applied

Guiding Light approved hardening the Wardenclyffe -> Banebook key on 2026-06-14T13:29:12-06:00. The key is now restricted to Wardenclyffe's Tailscale IPv4/IPv6 addresses and has SSH agent forwarding, X11 forwarding, and port forwarding disabled. Normal SSH command execution still works.

Verification returned:

```text
BANEBOOK
guidingl
REVERSE_SSH_HARDENED_PASS
```
