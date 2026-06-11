---
id: public-internet-access
name: Public Internet Access
schema_version: 2.1
profile: foundation
level: ingredient
maturity: candidate
scope: Banebook Hermes public internet retrieval and research access
currently_true: verified
last_verified: 2026-06-11
used_by:
  - internet-and-browser-control-stack
tags:
  - banebook
  - hermes
  - internet
  - web
  - research
  - docs
---

# Public Internet Access

## What it helps with

Use this when Uma needs to retrieve public web pages, official docs, package metadata, public forms, PDFs, or research sources from the internet.

## Verified proof

On 2026-06-11, Banebook Hermes fetched the Hermes browser automation docs over HTTPS from:

- `https://hermes-agent.nousresearch.com/docs/user-guide/features/browser`

The request returned the expected HTML document title `Browser Automation | Hermes Agent`.

## Current access lanes

- Terminal/Python HTTP requests for public pages and files.
- Hermes web/browser tools when configured and appropriate.
- Brave/CDP lane when the page is already open or needs browser rendering.

## Guardrails

- Public internet access is not the same as account authority.
- Logged-in pages, private inboxes, account forms, payment screens, and school/benefits portals follow account-page approval gates.
- Do not submit, send, purchase, sign, upload sensitive files, or change account settings without explicit approval.
