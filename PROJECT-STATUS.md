# Hermes Tasks Status

Last updated: 2026-06-11T16:06:12-06:00

## What this is

Visible, git-trackable Uma/Hermes operating repo for Banebook. This repo stores AI-readable source-of-truth docs, queue/decisions/index, handoffs, lessons, verifier declarations, and capability roots.

## What this is not

This repo is not the Hermes runtime profile, not a secret store, not a browser/session dump, and not a place for cookies, OAuth tokens, passwords, `.env` contents, wallet keys, raw logs, or copied browser profiles.

## Current state

- Stage: Published to GitHub.
- Branch: `main` tracking `origin/main`.
- Remote: `https://github.com/CBaen/hermes-tasks`.
- Published commit verified on remote: `4cc409d8712561f23c5a9a6b082e5edac769271b`.
- Current source of truth: `README.md`, `HANDOFF.md`, `LESSONS-LEARNED.md`, `GLOBAL-DECISIONS.md`, `AGENTS.md`, queue/index/decisions docs, `agent-lanes/BOARD.md`, `verifier-manifest.json`, baseline `capabilities/INDEX.md`, and sibling capability roots.
- Main active work: Maintain the persistent Hermes task scaffold and verified connection/control capabilities.
- Current blockers: None for publish. Auth detail for future agents: use `HOME=/home/guidingl` for GitHub CLI/git operations from Hermes because default Hermes `$HOME` is not logged in.

## Active workstreams

| Workstream | Outcome | Status | Owner / session | Verification state |
|---|---|---|---|---|
| connections-control | Internet/browser/control capability stack plus agent-only browser profile | Implemented; publish pending until git push completes | Hermes WebUI session 2026-06-11 | Validated locally |

## Required project package

- Project front door: `README.md`
- Project agent entrypoint: `AGENTS.md`
- Current handoff: `HANDOFF.md`
- Queue: `hermes-tasks-queue.md`
- Index: `hermes-tasks-index.md`
- Project decisions: `hermes-tasks-decisions.md`
- Global decisions: `GLOBAL-DECISIONS.md`
- Lessons learned: `LESSONS-LEARNED.md`
- Agent lane board: `agent-lanes/BOARD.md`
- Lane handoff template: `agent-lanes/LANE-HANDOFF.template.md`
- Connections/control lane handoff: `agent-lanes/connections-control-HANDOFF.md`
- Baseline capability root: `capabilities/INDEX.md`
- Connection/control capability root: `capabilities-connections-control/INDEX.md`
- Collaboration/autonomy capability root: `capabilities-collaboration-autonomy/INDEX.md`
- Agent infrastructure capability root: `capabilities-agent-infrastructure/INDEX.md`
- Verifier manifest: `verifier-manifest.json`
- Verification artifacts: `artifacts/`

## Runtime state documented but not copied into repo

- Active Hermes profile: `/home/guidingl/.hermes/profiles/banebook/`
- Active profile SOUL: `/home/guidingl/.hermes/profiles/banebook/SOUL.md`
- User/live Brave CDP lane: `http://127.0.0.1:9222`
- Agent-only Brave CDP lane: `http://127.0.0.1:9223`
- Agent-only profile: `/home/guidingl/.local/share/hermes/agent-brave-profile`
- Agent-only helpers: `/home/guidingl/.local/bin/hermes-agent-brave*`, `/home/guidingl/.local/bin/hermes-agent-cdp`

## Verification notes

Checked this session:

- Full LibreOffice suite installed/verified on Banebook; proof artifact stored at `artifacts/libreoffice/cheese-poem.odt`.
- User/live Brave CDP lane works on `9222`.
- Agent-only Brave profile works on `9223` and can navigate/read/type through CDP.
- `capabilities-connections-control/` contains the verified internet/browser/control stack.
- Project docs were expanded for AI handoff, lessons, decisions, queue, index, lane board, and verifier manifest.

Expected validation commands:

```bash
python /home/guidingl/projects/capabilities-framework/tools/validate_project_shape.py --project /home/guidingl/projects/hermes-tasks --project-slug hermes-tasks
python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-connections-control --json
python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-collaboration-autonomy --json
python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-agent-infrastructure --json
```

## Next safest move

Add only actually verified new capabilities: notification/messaging first if a platform is connected; Wardenclyffe bridge only after helper commands are present and tested.
