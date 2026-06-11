# Agent Lane Board

Last updated: 2026-06-11T16:06:12-06:00

## Purpose

Give every agent a fast view of active lanes, write scopes, owners, and handoff files before editing this project or adjacent sources.

## Rules

- Read this board before starting or resuming multi-agent work.
- Each lane agent writes its own handoff file in this folder.
- Each lane agent may update only its own table row and status block in this board.
- Avoid multiple agents editing the same source scope at the same time.
- If a lane needs to cross scopes, update this board first and wait for the main coordinating agent to approve the change.
- Do not write secrets, auth material, session logs, caches, or private runtime state into lane handoffs.
- Use timestamped status updates: `TS:YYYY-MM-DDTHH:MM:SS±HH:MM | Check:<source/date-or-command> | Confidence:<label>`.

## Active Lanes

| Lane | Owner | Write scope | Handoff | Status | Last update |
|---|---|---|---|---|---|
| publish-session-state | current Hermes session | root docs, verifier manifest, git metadata only | `HANDOFF.md` | Pushed; final status commit in progress | 2026-06-11T16:44:49-06:00 |

## Coordination Notes

- Main coordinating agent owns this board and final integration.
- Lane agents may update their own row when they start, pause, block, or finish.
- Detailed progress belongs in the lane's handoff file.
- Broad search output that truncates in chat is not proof. Save complete findings into a lane handoff or scoped artifact, then summarize.

## Lane Status Blocks

### publish-session-state

TS:2026-06-11T16:06:12-06:00 | Check:docs consolidated before final validation/commit | Confidence:high

- Status: Initial push succeeded; final status commit in progress.
- Current focus: push this final publish-status update.
- Latest changed files: `HANDOFF.md`, `PROJECT-STATUS.md`, `hermes-tasks-queue.md`, `hermes-tasks-decisions.md`, `agent-lanes/BOARD.md`.
- Latest validation: project shape ok=true; new capability roots ok=true; browser lanes verified after relaunch.
- Blockers: none. Use `HOME=/home/guidingl` for GitHub operations from Hermes.

## Done / Closed Lanes

- `connections-control` - implemented and verified; see `agent-lanes/connections-control-HANDOFF.md`.
