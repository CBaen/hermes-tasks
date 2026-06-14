---
id: wardenclyffe-hermes-webui-tunnel
name: Wardenclyffe Hermes WebUI Tunnel
schema_version: 2.1
profile: foundation
level: ingredient
maturity: candidate
scope: Banebook localhost SSH tunnel to Wardenclyffe Hermes dashboard
currently_true: verified
last_verified: 2026-06-13T20:01:27-06:00
tags:
  - wardenclyffe
  - banebook
  - hermes
  - webui
  - ssh-tunnel
  - tailscale
---

# Wardenclyffe Hermes WebUI Tunnel

## What it helps with

Use this when Banebook needs cockpit access to the always-on Hermes dashboard
running on Wardenclyffe without exposing the dashboard/API-key surface on the
Tailscale or LAN interface.

## Verified shape

- Wardenclyffe runs a user-level service:
  - unit: `~/.config/systemd/user/hermes-dashboard.service`
  - command: `hermes dashboard --host 127.0.0.1 --port 9119 --no-open --skip-build`
  - state: enabled and active
- Wardenclyffe binds the dashboard to localhost only:
  - remote URL: `http://127.0.0.1:9119`
- Banebook reaches it through a local SSH tunnel:
  - local URL: `http://127.0.0.1:9129`
  - helper: `/home/guidingl/.local/bin/wardenclyffe-hermes-webui`
  - status helper: `/home/guidingl/.local/bin/wardenclyffe-hermes-webui-status`
  - stop helper: `/home/guidingl/.local/bin/wardenclyffe-hermes-webui-stop`
- Banebook also has a desktop launcher:
  - `~/.local/share/applications/wardenclyffe-hermes-webui.desktop`

## Why this route

`hermes dashboard --insecure` allows non-localhost binding and is explicitly
labeled dangerous by the CLI because the dashboard can expose sensitive config
and API-key surfaces. The approved operating shape keeps Wardenclyffe as the
runtime host and Banebook as the cockpit without copying auth/session/browser
state or exposing the dashboard broadly.

## Commands

Open/reuse tunnel and launch browser:

```bash
wardenclyffe-hermes-webui
```

Open/reuse tunnel without launching a browser:

```bash
wardenclyffe-hermes-webui --no-open
```

Check service/tunnel/URL:

```bash
wardenclyffe-hermes-webui-status
```

Close the Banebook SSH tunnel only:

```bash
wardenclyffe-hermes-webui-stop
```

Close the Banebook tunnel and stop the remote dashboard service:

```bash
wardenclyffe-hermes-webui-stop --remote
```

## Verification evidence

- Wardenclyffe `systemctl --user is-enabled hermes-dashboard.service` returned
  `enabled`.
- Wardenclyffe `systemctl --user is-active hermes-dashboard.service` returned
  `active`.
- Wardenclyffe `ss -ltnp` showed `127.0.0.1:9119` only for the dashboard.
- Banebook `wardenclyffe-hermes-webui-status` showed an active SSH ControlMaster
  tunnel and local listener `127.0.0.1:9129`.
- Browser navigation to `http://127.0.0.1:9129` loaded `Hermes Agent - Dashboard`
  with gateway status running.

## Stop rules

- Do not use `--insecure` or bind the dashboard to `0.0.0.0` without a separate
  explicit security decision.
- Do not copy Wardenclyffe auth/session/browser state to Banebook.
- Do not click dashboard actions that change accounts, secrets, provider auth,
  security settings, external channels, production systems, or destructive data
  without task-specific approval.
