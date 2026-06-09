---
id: multi-machine-project-operations
name: Multi-Machine Project Operations
schema_version: 2.0
level: recipe
maturity: candidate
scope: Banebook Linux-first local work and Wardenclyffe remote Windows operations
currently_true: unknown
verification_level: 2
last_verified: 2026-05-06
evidence_quality: direct
successful_uses: 2
failed_uses: 0
regressions: 0
depends_on: []
used_by: []
tags:
  - banebook
  - kubuntu
  - linux
  - wardenclyffe
  - tailscale
  - ssh
  - rdp
  - docker
  - multi-machine
---

# Multi-Machine Project Operations

Use this when work might involve Banebook, Wardenclyffe, Tailscale, remote file
edits, RDP, SSH, SMB, or deciding where a project should run.

## Machine Roles

`Banebook`

- Linux user: `guidingl`.
- Hostname observed during the 2026-06-08 migration edit: `BANEBOOK`.
- Role: Kubuntu/Linux-first daily work laptop, control station, and default
  Codex workstation.
- Best for normal daily work, communication, browsing, browser/editor tooling,
  Codex sessions, light local project work, planning, review, checking files,
  and remote-controlling `wardenclyffe`.
- Canonical local paths use `/home/guidingl`, especially
  `/home/guidingl/projects`, `/home/guidingl/agent-worktrees`,
  `/home/guidingl/agent-coordination`, and `/home/guidingl/capabilities`.

`wardenclyffe`

- Windows user: `baenb`.
- Tailscale name/IP: `wardenclyffe` / `100.77.85.23`.
- Role: remote/headless Windows server/workhorse.
- Best for existing Docker/WSL, ERPNext/Frappe, long-running services, heavy
  browser automation, large media/audio/video work, and migrated project roots
  that still live under `C:\Users\baenb`.
- Source of truth for income-critical Docker/ERPNext systems unless a project
  doc says otherwise.

Windows paths under `C:\Users\baenb` are valid only while operating on
Wardenclyffe through the bridge helpers. Do not use them as Banebook-local
paths.

## Critical Income Systems

Treat the user's income-generating systems as standing operational responsibilities when a task is adjacent to them.

- Current known critical system: Locally Twisted ERPNext/Frappe stack on `wardenclyffe`.
- Business model: `wardenclyffe` is a private build, staging, template, and live-demo host for Built by Cameron ERPNext/Frappe client systems. Finished client systems should move to Frappe Cloud or another appropriate cloud environment, then ownership/control is passed to the client. Do not treat `wardenclyffe` as long-term public production hosting for client ERPNext ecosystems.
- The user's target client base is estate lawyers. Treat client data as highly sensitive. Prefer limited, explicit support access for website/module updates and requested maintenance; avoid support designs that require broad access to client records.
- Preserve one or two reusable ERPNext/Frappe template stacks for repeat client types when present. During cleanup, protect template stacks, Docker volumes, databases, backups, custom apps, compose files, and migration/export artifacts.
- Wardenclyffe stack path:
  `C:\Users\baenb\projects\Built_by_Cameron\_CLIENTS\locally-twisted\Locally-Twisted-Backend\frappe_docker`.
- Compose project: `locally-twisted-erpnext-v15`.
- Host URL on `wardenclyffe`: `http://localhost:8081`; from Banebook over
  Tailscale: `http://wardenclyffe:8081`.
- Watchdog: Windows Scheduled Task `Codex Locally Twisted ERPNext Health Watchdog` runs every 5 minutes as `baenb` on `wardenclyffe`.
- Wardenclyffe watchdog script/status/logs:
  `C:\Users\baenb\.codex\monitoring\locally-twisted-health-watchdog.ps1`,
  `locally-twisted-health-status.json`, and `locally-twisted-health.log`.
- If Docker, ERPNext/Frappe, Built by Cameron, Locally Twisted, `wardenclyffe`, server health, deployment, payments, forms, or launch readiness comes up, check the relevant health state or explicitly say why not.
- Do not ignore restart loops, exited runtime containers, unhealthy database state, failed HTTP checks, or broken remote access. Fix safely when the cause is clear, otherwise record exact symptoms, paths, and commands for handoff.
- Avoid destructive Docker/database actions unless the user explicitly asks after an inventory. Do not remove volumes, prune broadly, rebuild blindly, or rerun one-shot site creation jobs on an existing stack without confirming the intended outcome.

## Current Banebook Bridge

Use `/home/guidingl/WARDENCLYFFE_BRIDGE.md` as the current access source before
operating on Wardenclyffe. Current helper commands include:

```bash
wardenclyffe-status
wardenclyffe-ssh
wardenclyffe-sftp
wardenclyffe-rdp
wardenclyffe-ps '<PowerShell command>'
```

Current bridge facts from that file:

- Primary SSH: `ssh wardenclyffe`.
- Fallback SSH: `ssh wardenclyffe-baenb`.
- Banebook Tailscale IP: `100.114.57.47`.
- Wardenclyffe Tailscale IP: `100.77.85.23`.
- External backup/reference mount: `/home/guidingl/wardenclyffe-backups`.
- Local primary key: `/home/guidingl/.ssh/banebook_wardenclyffe_ed25519`.
- Local fallback key: `/home/guidingl/.ssh/codex_tailscale_banebook2_to_wardenclyffe`.

## Legacy Windows-To-Windows Evidence

The old `banebook2` Windows laptop facts below are migration evidence, not the
current Banebook default:

- Old Windows user: `camer`.
- Old Tailscale name/IP: `banebook2` / `100.83.23.115`.
- Old Windows-to-Windows RDP commands used `mstsc /v:wardenclyffe` and
  `mstsc /v:banebook2`.
- Old Windows key paths used
  `C:\Users\camer\.ssh\codex_tailscale_banebook2_to_wardenclyffe` and
  `C:\Users\baenb\.ssh\codex_tailscale_wardenclyffe`.

Do not route new Banebook work through `banebook2` or `mstsc` unless a task is
explicitly about the retired Windows laptop evidence.

## Routing Workflow

1. Identify the current host and user before touching files:

   ```bash
   hostname
   whoami
   ```

2. Decide where the source of truth lives:

   - If the project already lives only on `wardenclyffe`, keep active work
     there unless a migration plan says otherwise.
   - If the task needs existing Wardenclyffe Docker/WSL/ERPNext stacks, heavy
     browser automation, or media rendering, route to `wardenclyffe`.
   - If the task is normal daily computing, communication, writing, planning,
     review, browser/editor work, light local project work, or a quick file
     check, Banebook is the default.

3. Do not treat matching folder names as proof that two project copies are synced. Check git remotes, branch, status, and timestamps before editing.

4. Avoid blind bidirectional sync. Prefer one active working copy and one remote-control path.

5. When moving a small file intentionally, use an explicit staging path such as `TailscaleShare` and verify the final destination.

## Commands

From Banebook to Wardenclyffe:

```bash
wardenclyffe-status
wardenclyffe-ssh
wardenclyffe-sftp
wardenclyffe-rdp
wardenclyffe-ps 'hostname; whoami'
```

When launching `codex exec` on a peer machine over SSH, close SSH stdin so
Codex does not wait for extra piped input:

```bash
ssh -n wardenclyffe "codex exec --skip-git-repo-check --sandbox read-only --ephemeral 'Reply READY only.'"
```

## ADHD-Friendly Operating Rule

Keep the state obvious. When a task crosses machines, report:

- current host,
- target host,
- why the work belongs there,
- exact path being edited,
- what remains local-only.


