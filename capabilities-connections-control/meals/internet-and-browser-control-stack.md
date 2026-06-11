---
id: internet-and-browser-control-stack
name: Internet And Browser Control Stack
schema_version: 2.1
profile: foundation
level: meal
maturity: candidate
scope: composed Banebook capability for internet research plus browser read/write/control
currently_true: verified
last_verified: 2026-06-11
depends_on:
  - public-internet-access
  - local-brave-cdp-open-tabs
  - agent-only-browser-lane
  - browser-protocol-page-control-and-typing
  - desktop-input-control-boundary
tags:
  - banebook
  - hermes
  - internet
  - browser
  - cdp
  - control
  - typing
  - parallel-work
---

# Internet And Browser Control Stack

## What it helps with

Use this as the current practical collection of Uma's Banebook internet and browser-control capabilities.

## Current capability set

- Public internet access for research and official-source retrieval.
- Local Brave open-tab visibility through CDP on port `9222`.
- Agent-only Brave profile on port `9223` for independent web work without touching the user's live tabs.
- Browser protocol page control for DOM inspection, clicking, focusing, and text entry without physical keyboard/mouse takeover.
- Desktop input command awareness for last-resort non-browser GUI work, with explicit-approval boundaries.

## Practical use

For normal web tasks, route in this order:

1. Public web retrieval for generic research.
2. Agent-only or normal browser/CDP lane for rendered/open-tab page state.
3. Browser protocol control for clicking and filling fields.
4. Desktop input automation only when a non-browser GUI cannot be handled another way and the user approves focus/cursor risk.

## Approval gates

Even when control works technically, Uma still stops before final external actions: submissions, sends, uploads, account/security changes, payments, signatures, loan acceptance, deployments, or destructive changes.

## Evidence

Verified on 2026-06-11 with public HTTPS retrieval, Brave `/json/version` and `/json/list`, a throwaway CDP typing test using `Input.insertText`, and the verified agent-only Brave profile on port `9223` navigating to Hermes browser docs and reading back page title/heading.
