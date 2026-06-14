# Agent Lane Board

Last updated: 2026-06-14T13:57:08-06:00

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
| source-of-truth-parity | current Hermes session | `SOURCE-OF-TRUTH.md`, root docs, verifier manifest, agent-infrastructure capability, parity script | `HANDOFF.md` | Maintained; Wardenclyffe always-on runtime documented | 2026-06-13T13:01:08-06:00 |
| wardenclyffe-worker-lanes | current Hermes session + bounded Codex/Hermes smoke workers | `capabilities-collaboration-autonomy/`, `capabilities-agent-infrastructure/`, `artifacts/worker-smoke/`, `artifacts/model-smoke/` | `HANDOFF.md` | v1.1 named lanes/gates implemented; Codex smoke PASS; Nous Portal auth verified; free-model Hermes smoke PASS | 2026-06-13T19:48:26-06:00 |
| wardenclyffe-webui-access | current Hermes session | `capabilities-connections-control/ingredients/wardenclyffe-hermes-webui-tunnel.md`, Banebook helper scripts, Wardenclyffe `hermes-dashboard.service` | `HANDOFF.md` | implemented; localhost-only dashboard plus SSH tunnel; default free model verified | 2026-06-13T20:04:31-06:00 |
| connections-control | current Hermes session | `capabilities-connections-control/`, connection/control docs, lane handoff | `agent-lanes/connections-control-HANDOFF.md` | Account-page automation recipe added; messaging prepared but not connected | 2026-06-12T16:26:51-06:00 |

## Coordination Notes

- Main coordinating agent owns this board and final integration.
- Lane agents may update their own row when they start, pause, block, or finish.
- Detailed progress belongs in the lane's handoff file.
- Broad search output that truncates in chat is not proof. Save complete findings into a lane handoff or scoped artifact, then summarize.

## Lane Status Blocks

### source-of-truth-parity

TS:2026-06-13T13:01:08-06:00 | Check:Wardenclyffe Hermes always-on bootstrap docs updated | Confidence:high

- Status: Maintained; Wardenclyffe always-on Hermes runtime documented.
- Current focus: keep Banebook cockpit / Wardenclyffe runtime split in parity and prepare only scoped model-backed worker smoke/dispatch after explicit approval.
- Latest changed files: `SOURCE-OF-TRUTH.md`, `tools/check_source_of_truth_parity.py`, root docs, `verifier-manifest.json`, agent-infrastructure parity principle.
- Latest validation: Wardenclyffe gateway active/enabled, no-agent cron smoke fired, WebUI Scheduled Kanban tests passed on Wardenclyffe, and source-of-truth parity should be rerun after these doc edits.
- Blockers: none.

### wardenclyffe-worker-lanes

TS:2026-06-13T13:20:40-06:00 | Check:capability docs plus Wardenclyffe Codex smoke artifact | Confidence:high

- Status: v1.1 local-only worker-lane rules and named dispatch gates implemented and linked.
- Current focus: use v1.1 rules before additional Codex/Hermes worker dispatch; broad autonomous dispatch remains off by default and task-approval-gated.
- Latest changed files: `capabilities-collaboration-autonomy/recipes/wardenclyffe-uma-worker-lanes-v1.md`, `capabilities-agent-infrastructure/ingredients/wardenclyffe-codex-hermes-auth-boundary.md`, capability indexes, `artifacts/worker-smoke/`, and `artifacts/model-smoke/`.
- Latest validation: Wardenclyffe Codex CLI smoke recorded `Result: PASS`; Wardenclyffe `hermes status` verified Nous Portal login; Wardenclyffe Hermes one-shot with `stepfun/step-3.7-flash:free` returned PASS JSON; v1.1 lane/gate recipe validates under capability graph checks.
- Blockers: broad autonomous dispatch remains off by default pending task-specific approval; messaging targets remain unconnected.

### connections-control

TS:2026-06-12T16:26:51-06:00 | Check:approval-gated account-page automation recipe and graph validation | Confidence:high

- Status: Browser stack implemented; Wardenclyffe bidirectional SSH verified; approval-gated logged-in account-page automation recipe added; messaging prepared but not connected.
- Current focus: publish current docs/capability parity; wait for user account linking for messaging; keep GoDaddy registrar follow-up queued.
- Latest changed files: `capabilities-connections-control/INDEX.md`, `capabilities-connections-control/recipes/approval-gated-account-page-automation.md`, ingredient backlinks, `agent-lanes/connections-control-HANDOFF.md`.
- Latest validation: connections/control capability graph ok=true with 9 cards, 0 errors, 0 warnings.
- Blockers: messaging needs a connected platform. GoDaddy access for `locallytwisted.com` is blocked by EdgeSuite/504-style errors and must be handled without risking domain registration.

## Done / Closed Lanes

- `publish-session-state` - complete and pushed to GitHub; see git history ending at `c9a6418` before this continuation.
