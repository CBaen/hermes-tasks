# Hermes Tasks Status

Last updated: 2026-06-11T18:17:03-06:00

## What this is

Visible, git-trackable Uma/Hermes operating repo for Banebook. This repo stores AI-readable source-of-truth docs, queue/decisions/index, handoffs, lessons, verifier declarations, and capability roots.

## What this is not

This repo is not the Hermes runtime profile, not a secret store, not a browser/session dump, and not a place for cookies, OAuth tokens, passwords, `.env` contents, wallet keys, raw logs, or copied browser profiles.

## Current state

- Stage: Published to GitHub; continuing verified capability/documentation maintenance.
- Branch: `main` tracking `origin/main`.
- Remote: `https://github.com/CBaen/hermes-tasks`.
- Current publish truth: use live `git status -sb` and `HOME=/home/guidingl git ls-remote --heads origin main`; do not rely on embedded SHAs as current after new commits.
- Current source-of-truth entrypoint: `SOURCE-OF-TRUTH.md`.
- Main active work: Keep source-of-truth docs timestamped/in parity and add only verified connection/control capabilities.
- Current blockers: messaging/notification has no connected targets; old empty test browser profile cleanup requires explicit deletion approval. PATH bridge is now verified for helper command discovery.

## Active workstreams

| Workstream | Outcome | Status | Owner / session | Verification state |
|---|---|---|---|---|
| source-of-truth-parity | Timestamp policy, authority order, and parity verifier | Implemented and published | Hermes WebUI session 2026-06-11 | Parity checker passing |
| connections-control | Internet/browser/control stack plus Wardenclyffe bridge | Implemented with verified-only cards | Hermes WebUI session 2026-06-11 | Browser stack, Wardenclyffe status, and PATH bridge verified locally |

## Required project package

- Source-of-truth contract: `SOURCE-OF-TRUTH.md`
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
- Verification artifacts/scripts: `artifacts/`, `tools/check_source_of_truth_parity.py`

## Runtime state documented but not copied into repo

- Active Hermes profile: `/home/guidingl/.hermes/profiles/banebook/`
- Active profile SOUL: `/home/guidingl/.hermes/profiles/banebook/SOUL.md`
- User/live Brave CDP lane: `http://127.0.0.1:9222`
- Agent-only Brave CDP lane: `http://127.0.0.1:9223`
- Agent-only profile: `/home/guidingl/.local/share/hermes/agent-brave-profile`
- Agent-only helpers: `/home/guidingl/.local/bin/hermes-agent-brave*`, `/home/guidingl/.local/bin/hermes-agent-cdp`; command names resolve through the PATH bridge
- Wardenclyffe helpers: `/home/guidingl/bin/wardenclyffe-*`; command names resolve through the PATH bridge

## Verification notes

Checked this session:

- Messaging delivery targets: none connected/discovered via `send_message(action="list")`.
- Wardenclyffe status: Tailscale/SSH reachable; current target `WARDENCLYFFE` is Linux/Kubuntu, not retired Windows PowerShell workflow.
- Agent-only browser profile remains reachable on `9223`.
- 2026-06-11T18:17:03-06:00: PATH bridge verified: `hermes-agent-brave-status` and `wardenclyffe-ssh` resolve by name and smoke checks passed.
- GitHub auth for publish works with `HOME=/home/guidingl`.

Expected validation commands:

```bash
python tools/check_source_of_truth_parity.py
python /home/guidingl/projects/capabilities-framework/tools/validate_project_shape.py --project /home/guidingl/projects/hermes-tasks --project-slug hermes-tasks
python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-connections-control --json
python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-agent-infrastructure --json
```

## Next safest move

Next non-blocked work is to keep docs/capabilities in timestamp parity as new facts are verified. Add notification capability only after a real messaging platform is connected. Do not delete the old test profile without explicit approval.
