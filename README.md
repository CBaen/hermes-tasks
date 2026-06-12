# Hermes Tasks

Persistent operating project for Uma/Hermes work on Banebook.

## What this is

This repo is the visible, git-trackable source of truth for Hermes task routing, operating decisions, global decisions, lessons learned, indexes, capability roots, verifier declarations, and workstream handoffs.

## What this is not

This repo is not the Hermes runtime profile, not a secret store, not a browser/session dump, and not the place for OAuth tokens, `.env` contents, cookies, wallet keys, raw logs, copied browser profiles, or auth/session files.

## Start here

1. `AGENTS.md`
2. `SOURCE-OF-TRUTH.md`
3. `PROJECT-STATUS.md`
4. `HANDOFF.md`
5. `hermes-tasks-queue.md`
6. `hermes-tasks-decisions.md`
7. `GLOBAL-DECISIONS.md`
8. `LESSONS-LEARNED.md`
9. `hermes-tasks-index.md`
10. `capabilities/INDEX.md`

## Capability roots

- `capabilities/` - baseline project operating capabilities
- `capabilities-connections-control/` - internal/external connection and control capabilities
- `capabilities-collaboration-autonomy/` - standing permission, decision queue, and collaboration capabilities
- `capabilities-agent-infrastructure/` - Hermes/Uma profile, repo, launcher, background-job, and validation infrastructure capabilities

## Runtime pointers

- Active Hermes profile: `/home/guidingl/.hermes/profiles/banebook/`
- Active profile SOUL: `/home/guidingl/.hermes/profiles/banebook/SOUL.md`
- Cross-project Uma notes: `/home/guidingl/Uma/`
- User/live Brave CDP lane: `http://127.0.0.1:9222`
- Agent-only Brave CDP lane: `http://127.0.0.1:9223`
- Agent-only Brave profile: `/home/guidingl/.local/share/hermes/agent-brave-profile`
- Hermes terminal PATH bridge: `/home/guidingl/.hermes/profiles/banebook/terminal-path-bridge.sh`
- Agent-only browser helpers: command names resolve through the PATH bridge; absolute path fallback `/home/guidingl/.local/bin/hermes-agent-*`
- Wardenclyffe helpers: command names resolve through the PATH bridge; absolute path fallback `/home/guidingl/bin/wardenclyffe-*`

## Publishing target

- GitHub target requested by Guiding Light: `https://github.com/CBaen/hermes-tasks`
