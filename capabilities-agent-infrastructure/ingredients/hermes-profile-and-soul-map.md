---
id: hermes-profile-and-soul-map
name: Hermes Profile And SOUL Map
schema_version: 2.1
profile: foundation
level: ingredient
maturity: candidate
scope: Banebook Hermes profile, SOUL file, visible project repo, and browser-lane routing
currently_true: verified
last_verified: 2026-06-11
tags:
  - banebook
  - hermes
  - soul
  - profile
  - repo
  - infrastructure
  - browser
---

# Hermes Profile And SOUL Map

## Practical answer

Uma/Hermes has a runtime/profile home, local helper/runtime paths, and a visible project/repo home on Banebook.

## Current verified paths

- Active Hermes profile: `/home/guidingl/.hermes/profiles/banebook/`
- Active profile SOUL: `/home/guidingl/.hermes/profiles/banebook/SOUL.md`
- Root/default Hermes SOUL template: `/home/guidingl/.hermes/SOUL.md`
- Visible persistent operating project repo: `/home/guidingl/projects/hermes-tasks/`
- Cross-project Uma notes: `/home/guidingl/Uma/`
- Main pointer note: `/home/guidingl/Uma/HERMES-MAIN-PROJECT.md`
- User/live Brave CDP lane: `http://127.0.0.1:9222`
- Agent-only Brave CDP lane: `http://127.0.0.1:9223`
- Agent-only Brave profile: `/home/guidingl/.local/share/hermes/agent-brave-profile`
- Agent-only browser helpers: `/home/guidingl/.local/bin/hermes-agent-brave`, `/home/guidingl/.local/bin/hermes-agent-brave-status`, `/home/guidingl/.local/bin/hermes-agent-brave-stop`, `/home/guidingl/.local/bin/hermes-agent-cdp`

## Routing rule

Keep source-of-truth operating docs in `/home/guidingl/projects/hermes-tasks/` where they are visible and git-trackable. Keep runtime config and profile material in `/home/guidingl/.hermes/profiles/banebook/` or the appropriate local runtime path. Link to runtime paths when useful, but do not copy secrets, auth/session files, `.env` contents, raw logs, browser profiles, cookies, or tokens into this repo.
