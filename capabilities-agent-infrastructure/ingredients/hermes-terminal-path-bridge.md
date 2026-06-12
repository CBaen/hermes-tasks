---
id: hermes-terminal-path-bridge
name: Hermes Terminal PATH Bridge
schema_version: 2.1
profile: foundation
level: ingredient
maturity: candidate
scope: Banebook Hermes terminal helper command discovery for real-user helper directories
currently_true: verified
last_verified: 2026-06-11
tags:
  - hermes
  - terminal
  - path
  - banebook
  - helpers
  - wardenclyffe
  - browser-control
---

# Hermes Terminal PATH Bridge

## What it helps with

Use this when Hermes terminal commands need to call Banebook real-user helper scripts by command name instead of absolute path.

## Current verified state

Verified on 2026-06-11T18:17:03-06:00:

- Active profile config: `/home/guidingl/.hermes/profiles/banebook/config.yaml`
- Shell init file: `/home/guidingl/.hermes/profiles/banebook/terminal-path-bridge.sh`
- The init file prepends these directories when present:
  - `/home/guidingl/.local/bin`
  - `/home/guidingl/bin`
- New Hermes terminal calls now resolve:
  - `hermes-agent-brave`
  - `hermes-agent-cdp`
  - `hermes-agent-brave-status`
  - `wardenclyffe-status`
  - `wardenclyffe-ssh`
- Smoke checks passed:
  - `hermes-agent-brave-status` printed the agent profile/CDP status.
  - `wardenclyffe-ssh 'hostname; uname -srm'` returned `WARDENCLYFFE` and `Linux 7.0.0-14-generic x86_64`.

## Implementation

Profile-local shell init file:

```bash
/home/guidingl/.hermes/profiles/banebook/terminal-path-bridge.sh
```

Relevant config key:

```yaml
terminal:
  shell_init_files:
  - /home/guidingl/.hermes/profiles/banebook/terminal-path-bridge.sh
```

Backup made before manual config repair:

```text
/home/guidingl/.hermes/profiles/banebook/config.yaml.bak-path-bridge-20260611T181644-0600
```

## Pitfall discovered

`hermes config set terminal.shell_init_files '["..."]'` stored the list as a quoted string in this Hermes version. `hermes config set terminal.shell_init_files.0 ...` then converted it into a dict-like mapping because it started from the wrong type. The config had to be repaired by replacing only the incorrect non-secret `shell_init_files` block with a real YAML list.

## Guardrails

- This bridge only exposes existing local helper directories on PATH. It does not copy secrets or change system-owned PATH directories.
- Do not add broad, writable, untrusted directories to PATH.
- If helper command resolution fails later, first inspect `terminal.shell_init_files` and source `/home/guidingl/.hermes/profiles/banebook/terminal-path-bridge.sh` manually as a diagnostic.
