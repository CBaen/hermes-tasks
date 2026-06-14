# Hermes Tasks Status

Last updated: 2026-06-14T13:57:08-06:00

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
- Main active work: Keep source-of-truth docs timestamped/in parity, use Wardenclyffe as the always-on Uma/Hermes runtime host, use Banebook as the daily cockpit/review/browser-control station, and run worker lanes only inside documented approval boundaries.
- Current blockers: messaging/notification has no connected targets; Slack manifest is prepared but account/platform linking is still required. Old empty test browser profile cleanup requires explicit deletion approval. GoDaddy access for `locallytwisted.com` is blocked by EdgeSuite/504-style login errors; do not cancel or close GoDaddy until the domain registration path is intentionally handled. Wardenclyffe Hermes provider auth, free-model default, model smoke, worker dispatch gates, and Banebook WebUI tunnel are verified; external sends/account/security/money/production/destructive actions still require exact approval.

## Active workstreams

| Workstream | Outcome | Status | Owner / session | Verification state |
|---|---|---|---|---|
| source-of-truth-parity | Timestamp policy, authority order, and parity verifier | Implemented and published | Hermes WebUI session 2026-06-11 | Parity checker passing |
| connections-control | Internet/browser/control stack plus Wardenclyffe bridge | Implemented with verified-only cards | Hermes WebUI session 2026-06-11 | Browser stack, Wardenclyffe bidirectional SSH, and PATH bridge verified locally |
| locallytwisted-domain-hosting-cleanup | Keep `locallytwisted.com` live on Cloudflare/Frappe while retiring unneeded Bluehost renewals and preserving registrar safety | Bluehost auto-renew disabled; GoDaddy registrar/access follow-up queued | Hermes WebUI session 2026-06-12 | Cloudflare DNS/MX, Frappe Cloud live site, Bluehost Renewal Center API, and RDAP checked |
| wardenclyffe-hermes-always-on | Move always-on Uma/Hermes runtime ownership to Wardenclyffe while Banebook remains cockpit | Implemented for fresh install/gateway/dashboard/script-only scheduler, verified Nous Portal provider auth, free-model default/smoke, and seeded operating backlog | Hermes WebUI session 2026-06-13 | `hermes status`, systemd user gateway, dashboard service/tunnel, cron smoke marker, WebUI Kanban tests/smoke, `uma-operating-loop` board, Nous Portal login, and free-model one-shot artifacts verified on Wardenclyffe |
| wardenclyffe-worker-lanes | Convert Codex/AGENTS/capability guidance into local-only Wardenclyffe worker-lane rules | Implemented for v1.1 named lanes/approval gates, Codex smoke, provider-auth prerequisite, and one local-only model-backed smoke; broad dispatch remains task-approval-gated | Hermes WebUI session 2026-06-13 | Capability files linked; Wardenclyffe Codex smoke artifact PASS; Wardenclyffe Nous Portal auth verified; free-model smoke artifact PASS; Kanban lane card done |

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

- Banebook active Hermes profile: `/home/guidingl/.hermes/profiles/banebook/`
- Wardenclyffe fresh Hermes runtime: `/home/guidingl/.hermes/`; code at `/home/guidingl/.hermes/hermes-agent`; gateway service `hermes-gateway.service` enabled/running as user `guidingl`.
- Wardenclyffe cloned operating repos: `/home/guidingl/projects/hermes-tasks` and `/home/guidingl/projects/hermes-webui`; WebUI Scheduled Kanban patch is on branch `scheduled-kanban-webui`.
- Active profile SOUL: `/home/guidingl/.hermes/profiles/banebook/SOUL.md`
- User/live Brave CDP lane: `http://127.0.0.1:9222`
- Agent-only Brave CDP lane: `http://127.0.0.1:9223`
- Agent-only profile: `/home/guidingl/.local/share/hermes/agent-brave-profile`
- Agent-only helpers: `/home/guidingl/.local/bin/hermes-agent-brave*`, `/home/guidingl/.local/bin/hermes-agent-cdp`; command names resolve through the PATH bridge
- Wardenclyffe helpers: `/home/guidingl/bin/wardenclyffe-*`; command names resolve through the PATH bridge

## Verification notes

Checked this session:

- 2026-06-13T13:01:08-06:00: Wardenclyffe was approved and configured as the primary always-on Uma/Hermes home base. Fresh Hermes install completed without copying Banebook secrets/auth/sessions/browser state; `/usr/local/bin/hermes` points to the user launcher; user gateway service is enabled/running with linger enabled; no-agent cron smoke fired automatically at `2026-06-13T13:00:19-06:00` and the one-shot job removed itself.
- 2026-06-13T13:01:08-06:00: Wardenclyffe WebUI clone received a narrow Scheduled Kanban patch on branch `scheduled-kanban-webui`; syntax checks, `git diff --check`, targeted Kanban pytest suite (`90 passed`), and isolated real-Hermes scheduled-card smoke all passed.
- 2026-06-13T13:01:08-06:00: Wardenclyffe Kanban board `uma-operating-loop` was created and seeded with six blocked backlog cards for provider auth, WebUI access, worker lanes, daily review, decision cockpit, and finance pipeline. All cards are blocked until provider auth and dispatch/approval rules are ready.
- 2026-06-13T13:20:40-06:00: Wardenclyffe worker-lane rules v1 were added under collaboration/autonomy, Codex/Hermes auth-boundary ingredient was added under agent infrastructure, and Wardenclyffe Codex CLI completed a local-only smoke test with PASS artifact `artifacts/worker-smoke/wardenclyffe-codex-worker-smoke.md`.
- 2026-06-13T18:51:06-06:00: Wardenclyffe Nous Portal login completed through user-approved Free-plan/email device-code flow. Verification: `hermes status` shows Provider `Nous Portal`, model `anthropic/claude-opus-4.6`, managed tools available, gateway active/enabled, and no cron jobs pending. Kanban card `t_626918f9` (`Fresh provider auth for Wardenclyffe Hermes workers`) is marked done; three operating-loop cards remain blocked for their own decisions.
- 2026-06-13T18:59:57-06:00: Small local-only Wardenclyffe Hermes model-backed smoke passed using Nous Portal free model `stepfun/step-3.7-flash:free`. The configured default `anthropic/claude-opus-4.6` returned a low-credits/paid-model error on the Free subscription, so the smoke used a selectable free model discovered through Hermes model helpers. Artifact: `artifacts/model-smoke/wardenclyffe-nous-free-model-smoke-20260613.json`.
- 2026-06-13T19:48:26-06:00: Wardenclyffe worker-lane recipe expanded to v1.1 named dispatch matrix for `finance-clerk`, `researcher`, `builder`, `verifier`, `client-ops`, `life-admin`, and `browser-worker`, with green/yellow/red actions, evidence bars, dispatch readiness checklist, and explicit reminder that broad autonomous dispatch remains off by default.
- 2026-06-13T20:01:27-06:00: Wardenclyffe Hermes WebUI access from Banebook configured. Wardenclyffe user service `hermes-dashboard.service` is enabled/active and bound to `127.0.0.1:9119`; Banebook helpers `wardenclyffe-hermes-webui`, `wardenclyffe-hermes-webui-status`, and `wardenclyffe-hermes-webui-stop` manage an SSH tunnel to `http://127.0.0.1:9129`; browser verification loaded `Hermes Agent - Dashboard`. Kanban card `t_30f3972d` marked done; board is now three done / three blocked.
- 2026-06-13T20:03:24-06:00: Wardenclyffe default Hermes config changed to provider `nous` and model `stepfun/step-3.7-flash:free`; dashboard restarted cleanly; no-override `hermes -z` smoke returned `WARDENCLYFFE_DEFAULT_MODEL_PASS`.
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

Next non-blocked work is to decide how Banebook should open/control the Wardenclyffe WebUI, then use the v1.1 dispatch gates for future scoped workers without enabling broad autonomous dispatch by default, and keep docs/capabilities in timestamp parity as new facts are verified. Messaging delivery remains blocked until the user completes platform linking (recommended prepared path: Slack). Do not delete the old test profile without explicit approval. For Locally Twisted, next safe work is to recover GoDaddy access, check only non-domain GoDaddy products for cancellation, and preserve domain registration until Cloudflare Registrar transfer or an explicit registrar decision is complete.
## 2026-06-14T13:09:00-06:00 - Bidirectional agent and mobile access note

- Banebook and Wardenclyffe are verified for bidirectional SSH over Tailscale. Use lane-gated route records for automated agents on either machine.
- Samsung S24 appears on Tailscale as `Bane  24Ultra` / `100.75.32.46` / Android, but was offline during inventory. Mobile access is possible only after choosing and setting up a phone-side service.
## 2026-06-14T13:29:12-06:00 - Reverse SSH hardened and S24 online

- Wardenclyffe -> Banebook reverse SSH key was hardened after explicit approval: restricted to Wardenclyffe Tailscale IPs and no SSH agent/X11/port forwarding; normal command execution still verified.
- Samsung S24 `Bane  24Ultra` / `100.75.32.46` is online in Tailscale and pingable. Phone access remains discussion-gated until a phone-side service is chosen.
## 2026-06-14T13:57:08-06:00 - ADB/scrcpy app-testing prerequisites installed

- Installed `adb`, `fastboot`, `scrcpy`, and `android-udev-rules` on Banebook and Wardenclyffe from Ubuntu repos.
- Verified `adb` 34.0.5-debian, `fastboot` 34.0.5-debian, and `scrcpy` 3.3.4 on both machines.
- S24 remains reachable on Tailscale at `100.75.32.46`; no ADB devices are paired yet. Pairing is user-present and app-test scoped.
