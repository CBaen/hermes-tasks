---
id: wardenclyffe-kubuntu-ssh-bridge
name: Wardenclyffe Kubuntu SSH Bridge
schema_version: 2.1
profile: foundation
level: ingredient
maturity: candidate
scope: Banebook to Wardenclyffe Kubuntu connection/control helpers over Tailscale and SSH
currently_true: verified
last_verified: 2026-06-11
tags:
  - banebook
  - wardenclyffe
  - tailscale
  - ssh
  - remote-control
  - kubuntu
---

# Wardenclyffe Kubuntu SSH Bridge

## What it helps with

Use this when Uma needs read-only inventory or approved command execution on Wardenclyffe from Banebook.

## Current verified state

Verified on 2026-06-11T17:52:58-06:00 using `/home/guidingl/bin/wardenclyffe-status`:

- Tailscale ping to `wardenclyffe` succeeded at `100.109.191.31`.
- TCP port `22` succeeded.
- SSH returned user `guidingl`, host `WARDENCLYFFE`, OS `Linux 7.0.0-14-generic x86_64`.
- Root filesystem reported about `916G` total, `16G` used, `854G` available.
- Large NTFS storage mount present at `/mnt/wardenclyffe-homelab-storage` with about `6.7T` free and `7%` used.
- Legacy backup mount `/home/guidingl/wardenclyffe-backups` was not mounted.

## Helper commands

Hermes' current terminal PATH does **not** include `/home/guidingl/bin`, so use absolute paths unless the PATH bridge is fixed:

```bash
/home/guidingl/bin/wardenclyffe-status
/home/guidingl/bin/wardenclyffe-ssh '<linux command>'
/home/guidingl/bin/wardenclyffe-sftp
/home/guidingl/bin/wardenclyffe-rdp
/home/guidingl/bin/wardenclyffe-rdp-multimon
```

Important: `/home/guidingl/bin/wardenclyffe-ps` is retired and exits with a message saying the prior Windows workflow was removed. Current Wardenclyffe is Kubuntu/Linux, not a Windows PowerShell target.

## Guardrails

- Read-only inventory/status checks are okay when task-relevant.
- Ask before rebooting Wardenclyffe, stopping services, pruning Docker, shutting down stacks, deleting files, removing backups, changing network/auth settings, or running long/destructive remote commands.
- Treat older docs claiming Wardenclyffe is Windows/PowerShell as stale unless live verification contradicts this card.
