# Hermes Tasks Status

Last updated: 2026-06-12T16:26:51-06:00

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
- Main active work: Keep source-of-truth docs timestamped/in parity, add only verified connection/control capabilities, and preserve the current Locally Twisted vendor cleanup truth for future agents.
- Current blockers: messaging/notification has no connected targets; Slack manifest is prepared but account/platform linking is still required. Old empty test browser profile cleanup requires explicit deletion approval. GoDaddy access for `locallytwisted.com` is blocked by EdgeSuite/504-style login errors; do not cancel or close GoDaddy until the domain registration path is intentionally handled.

## Active workstreams

| Workstream | Outcome | Status | Owner / session | Verification state |
|---|---|---|---|---|
| source-of-truth-parity | Timestamp policy, authority order, and parity verifier | Implemented and published | Hermes WebUI session 2026-06-11 | Parity checker passing |
| connections-control | Internet/browser/control stack plus Wardenclyffe bridge | Implemented with verified-only cards | Hermes WebUI session 2026-06-11 | Browser stack, Wardenclyffe bidirectional SSH, and PATH bridge verified locally |
| locallytwisted-domain-hosting-cleanup | Keep `locallytwisted.com` live on Cloudflare/Frappe while retiring unneeded Bluehost renewals and preserving registrar safety | Bluehost auto-renew disabled; GoDaddy registrar/access follow-up queued | Hermes WebUI session 2026-06-12 | Cloudflare DNS/MX, Frappe Cloud live site, Bluehost Renewal Center API, and RDAP checked |

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
- Slack manifest regenerated/validated at `artifacts/messaging/hermes-slack-manifest.json`; WhatsApp and Signal remain account-linking/setup paths.
- Wardenclyffe status: Tailscale/SSH reachable; current target `WARDENCLYFFE` is Linux/Kubuntu, not retired Windows PowerShell workflow.
- Wardenclyffe reverse SSH from Wardenclyffe into Banebook is verified after user-directed key authorization.
- Agent-only browser profile remains reachable on `9223`.
- 2026-06-11T18:17:03-06:00: PATH bridge verified: `hermes-agent-brave-status` and `wardenclyffe-ssh` resolve by name and smoke checks passed.
- GitHub auth for publish works with `HOME=/home/guidingl`.
- 2026-06-12T16:26:51-06:00: `locallytwisted.com` public service posture verified: Cloudflare is authoritative DNS, Cloudflare MX is present, and Frappe Cloud serves the live site.
- 2026-06-12T16:26:51-06:00: Bluehost auto-renew cleanup completed after explicit user approval for the two products tied to `locallytwisted.com`: SiteLock Essentials and WordPress Basic Hosting. Bluehost showed processing notices; Renewal Center/API verification showed `AutoRenewOn=0`, `AutoRenewOff=1`, and WordPress Basic Hosting `autoRenew=false`. The visible Bluehost Angular table/cache remained stale, so future agents should verify backend/API state before retrying.
- 2026-06-12T16:26:51-06:00: GoDaddy still appears to be the registrar for `locallytwisted.com` with expiration `2027-05-19`; login/access remained blocked by GoDaddy/Akamai EdgeSuite/504-style errors. GoDaddy cleanup remains a queued follow-up, not complete.

Expected validation commands:

```bash
python tools/check_source_of_truth_parity.py
python /home/guidingl/projects/capabilities-framework/tools/validate_project_shape.py --project /home/guidingl/projects/hermes-tasks --project-slug hermes-tasks
python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-connections-control --json
python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-agent-infrastructure --json
```

## Next safest move

Next non-blocked work is to keep docs/capabilities in timestamp parity as new facts are verified. Messaging delivery remains blocked until the user completes platform linking (recommended prepared path: Slack). Do not delete the old test profile without explicit approval. For Locally Twisted, next safe work is to recover GoDaddy access, check only non-domain GoDaddy products for cancellation, and preserve domain registration until Cloudflare Registrar transfer or an explicit registrar decision is complete.
