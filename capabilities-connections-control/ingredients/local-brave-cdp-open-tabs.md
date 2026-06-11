---
id: local-brave-cdp-open-tabs
name: Local Brave CDP Open Tabs
schema_version: 2.1
profile: foundation
level: ingredient
maturity: candidate
scope: Banebook local Brave browser open-tab access for Hermes
currently_true: verified
last_verified: 2026-06-11
used_by:
  - agent-only-browser-lane
  - browser-protocol-page-control-and-typing
  - internet-and-browser-control-stack
tags:
  - banebook
  - hermes
  - brave
  - cdp
  - browser
  - open-tabs
  - account-pages
---

# Local Brave CDP Open Tabs

## What it helps with

Use this when Uma needs to inspect or interact with already-open Brave tabs on Banebook without taking over Guiding Light's physical cursor or keyboard.

## Current verified setup

- Hermes Banebook profile points `browser.cdp_url` to `http://127.0.0.1:9222`.
- User-level Brave launcher override exists at `/home/guidingl/.local/share/applications/brave-browser.desktop`.
- The launcher starts Brave with `--remote-debugging-port=9222`.
- Verification on 2026-06-11T15:35:57-06:00: `/json/version` returned `Chrome/149.0.7827.103`; `/json/list` returned visible page targets.

## Use pattern

1. Verify endpoint:

```bash
python3 - <<'PY'
import json, urllib.request
for url in ['http://127.0.0.1:9222/json/version', 'http://127.0.0.1:9222/json/list']:
    with urllib.request.urlopen(url, timeout=3) as r:
        print(url, r.read(1000).decode('utf-8', 'replace'))
PY
```

2. Use browser/CDP tooling to list targets and inspect the intended tab.
3. Prefer DOM/CDP interactions over desktop-coordinate mouse/keyboard control.
4. For logged-in account pages, summarize only eligibility/status-impacting facts unless the user asks for more detail.

## Guardrails

- Do not read or store cookies, tokens, auth stores, passwords, raw browser profiles, or session state.
- Do not submit forms, change account settings, send messages, upload files, sign documents, accept loans, or make external commitments without explicit final approval.
- If Brave was not launched with the debug port, ask before restarting the user's active browser session.
