---
id: agent-only-browser-lane
name: Agent-Only Browser Lane
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: separate browser profile for Uma independent web work on Banebook
currently_true: verified
last_verified: 2026-06-11
depends_on:
  - local-brave-cdp-open-tabs
used_by:
  - internet-and-browser-control-stack
tags:
  - banebook
  - hermes
  - browser
  - parallel-work
  - isolation
  - cdp
---

# Agent-Only Browser Lane

## What it helps with

Use this when Uma needs to research, browse, inspect public pages, or run browser-control checks while Guiding Light keeps using the normal Brave session.

## Verified local setup

- User/live Brave lane: `http://127.0.0.1:9222`, normal user profile, for tabs Guiding Light is using.
- Agent-only Brave lane: `http://127.0.0.1:9223`, separate profile directory.
- Agent-only profile directory: `/home/guidingl/.local/share/hermes/agent-brave-profile`.
- Launcher helper: `/home/guidingl/.local/bin/hermes-agent-brave`.
- Status helper: `/home/guidingl/.local/bin/hermes-agent-brave-status`.
- Stop helper: `/home/guidingl/.local/bin/hermes-agent-brave-stop`.
- CDP helper: `/home/guidingl/.local/bin/hermes-agent-cdp`.
- Desktop launcher: `/home/guidingl/.local/share/applications/hermes-agent-brave.desktop`.

## Commands

Launch the agent-only browser:

```bash
/home/guidingl/.local/bin/hermes-agent-brave about:blank
```

Check status:

```bash
/home/guidingl/.local/bin/hermes-agent-brave-status
```

List agent-browser tabs:

```bash
/home/guidingl/.local/bin/hermes-agent-cdp list
```

Navigate the current agent tab:

```bash
/home/guidingl/.local/bin/hermes-agent-cdp navigate https://example.com
```

Evaluate page state in the current agent tab:

```bash
/home/guidingl/.local/bin/hermes-agent-cdp eval '({title: document.title, url: location.href})'
```

Run a protocol typing proof:

```bash
/home/guidingl/.local/bin/hermes-agent-cdp control-proof
```

Stop only the agent browser profile:

```bash
/home/guidingl/.local/bin/hermes-agent-brave-stop
```

## Verification evidence

Verified on 2026-06-11:

- The agent-only browser launched with `--user-data-dir=/home/guidingl/.local/share/hermes/agent-brave-profile`.
- `http://127.0.0.1:9223/json/version` returned `Chrome/149.0.7827.103`.
- `http://127.0.0.1:9223/json/list` returned the agent-only tab list.
- User/live Brave on `9222` stayed reachable separately.
- `/home/guidingl/.local/bin/hermes-agent-cdp control-proof` inserted and read back `Hermes agent profile typed this via CDP`.
- Agent tab successfully navigated to `https://hermes-agent.nousresearch.com/docs/user-guide/features/browser` and read back title `Browser Automation | Hermes Agent` plus heading `Browser Automation`.

## Guardrails

- Do not log into sensitive accounts in the agent-only profile unless Guiding Light explicitly chooses that workflow.
- Keep personal/live account work on the user's normal Brave lane unless a separate account/session is safer.
- Do not copy browser profiles, cookies, tokens, passwords, auth stores, or raw session state between lanes.
- The agent-only lane increases capability, not authority: still stop before submissions, sends, uploads, account/security changes, payments, signatures, loan acceptance, production deploys, or destructive actions.
