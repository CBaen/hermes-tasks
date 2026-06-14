# Hermes Tasks Queue

## Active

| Priority | Workstream | Outcome | Status | Owner | Verification |
|---|---|---|---|---|---|
| P0 | source-of-truth-parity | Timestamp contract, authority order, parity checker, and updated docs/capabilities | Done; maintain on every docs/capability change | current/future Hermes sessions | Parity checker passes |
| P1 | messaging-notification | Connect one notification platform; Slack is prepared, WhatsApp/Signal are assessed | Blocked on user account/platform linking | future Hermes session | Slack manifest validated; no Hermes targets discovered on 2026-06-11T22:37:43-06:00 |
| P1 | wardenclyffe-bridge | Use verified Wardenclyffe Kubuntu SSH bridge through resolved helper commands | Implemented as bidirectional SSH capability cards | future Hermes session | Wardenclyffe -> Banebook SSH verification succeeded on 2026-06-11T22:37:43-06:00 |
| P0 | wardenclyffe-hermes-always-on | Wardenclyffe owns always-on Hermes gateway/dashboard/scheduled runtime; Banebook remains cockpit | Implemented for fresh install/gateway/dashboard/script-only scheduler, Nous Portal provider auth, free-model default/smokes, and worker dispatch gates; operating backlog remains partially blocked pending separate decisions | current/future Hermes sessions | Gateway active/enabled; dashboard active/enabled behind SSH tunnel; no-agent cron smoke fired; Nous Portal auth verified; default/free-model smoke PASS; `uma-operating-loop` board has three done cards and three blocked cards |
| P0 | wardenclyffe-worker-lanes | Local-only Wardenclyffe worker-lane rules, named dispatch gates, and smoke proofs | Implemented for v1.1; use gates before further worker dispatch | current/future Hermes sessions | Codex smoke PASS; Nous free-model smoke PASS; lane card done |
| P0 | wardenclyffe-webui-access | Banebook cockpit access to Wardenclyffe Hermes WebUI | Implemented with localhost-only remote dashboard plus Banebook SSH tunnel/helper/launcher | current/future Hermes sessions | `hermes-dashboard.service` active/enabled; `http://127.0.0.1:9129` loads dashboard from Banebook; card done |
| P1 | mobile-s24-access | Explore Samsung S24 as Tailscale-accessible mobile edge device | Online/reachable; setup blocked on choosing phone-side service level | future Hermes session | `Bane  24Ultra` / Android / `100.75.32.46` online and `tailscale ping` succeeded on 2026-06-14T13:29:12-06:00 |

## Next

- Use the v1.1 Wardenclyffe dispatch gates plus bidirectional Banebook/Wardenclyffe coordination recipe for future scoped worker cards; do not enable external/account/security/money/production/destructive actions without exact approval.
- Pick a Samsung S24 access level when the phone is online: presence-only, file sync, KDE Connect, Termux SSH, or attended ADB/scrcpy.
- Use `wardenclyffe-hermes-webui` from Banebook to open the persistent Wardenclyffe dashboard via SSH tunnel.
- Complete Slack app install/token setup when user is present; do not store tokens in repo.
- Add notification/messaging capability only after an actual target/platform is connected and verified.
- Keep parity checker passing before/after docs/capability publish.
- Decide whether to keep or delete the old 63M test profile under `/home/guidingl/.hermes/profiles/banebook/home/.local/share/hermes/agent-brave-profile`; do not delete without explicit approval.
- 2026-06-12T16:21:19-06:00: Review GoDaddy cleanup path for `locallytwisted.com`. Verified today: Cloudflare is authoritative DNS, Cloudflare MX is present, Frappe Cloud serves the live site, Bluehost auto-renew cleanup was handled separately, and GoDaddy still appears to be the registrar with domain expiration `2027-05-19`. Do not fully cancel/close GoDaddy until either the domain registration is transferred to Cloudflare Registrar or the user intentionally keeps GoDaddy as registrar. Next review steps: recover GoDaddy access despite EdgeSuite/504 errors, check for non-domain GoDaddy products to cancel, and preserve/continue domain registration until transfer is complete.

## Parked

- Promoting `standing-permission-tiers` beyond proposed/candidate status. Needs explicit user acceptance and repeated successful use.
- Additional non-browser desktop control capability. Needs a real task and explicit focus/cursor-risk approval.

## Done

- 2026-06-14T13:29:12-06:00: Reverse SSH hardening applied to Wardenclyffe -> Banebook key and verified; Samsung S24 is online/pingable and phone-access explanation expanded.
- 2026-06-13T13:20:40-06:00: Added Wardenclyffe Uma worker-lane rules v1, documented Codex/Hermes auth boundaries, synced the non-secret lane docs to Wardenclyffe, and ran a bounded Wardenclyffe Codex CLI local-only smoke test. Result: PASS artifact at `artifacts/worker-smoke/wardenclyffe-codex-worker-smoke.md`.
- 2026-06-13T13:01:08-06:00: Approved and configured Wardenclyffe as the primary always-on Uma/Hermes runtime host. Fresh Hermes installed without copying Banebook secrets/auth/sessions/browser state; gateway user service is enabled/running with linger; `/usr/local/bin/hermes` resolves the launcher for non-interactive SSH; script-only cron smoke fired automatically and removed its one-shot job.
- 2026-06-13T13:01:08-06:00: Cloned Hermes Tasks and Hermes WebUI on Wardenclyffe, applied the Scheduled Kanban WebUI patch on branch `scheduled-kanban-webui`, and verified syntax, whitespace, targeted Kanban tests (`90 passed`), and isolated real-Hermes scheduled-card smoke.
- 2026-06-13T13:01:08-06:00: Created Wardenclyffe Kanban board `uma-operating-loop` and seeded six blocked backlog cards for the remaining always-on Uma buildout so they are preserved but cannot dispatch prematurely.
- 2026-06-12T16:26:51-06:00: Completed Bluehost auto-renew cleanup for `locallytwisted.com` after explicit user approval. Turned off auto-renew through Bluehost confirmation flows for SiteLock Essentials and WordPress Basic Hosting tied to the domain. Bluehost showed processing notices; Renewal Center/API verification showed `AutoRenewOn=0`, `AutoRenewOff=1`, and WordPress Basic Hosting `autoRenew=false`. Visible Bluehost Angular table/cache remained stale after reload, so future agents should verify backend/API state before retrying account actions.
- 2026-06-11T22:37:43-06:00: Followed Wardenclyffe reverse SSH handoff, authorized exact verified key on Banebook, confirmed Wardenclyffe can SSH back into Banebook, regenerated/validated Slack manifest, and documented messaging options.
- 2026-06-11T18:17:03-06:00: Added and verified profile-local Hermes terminal PATH bridge; helper commands now resolve by name and smoke checks passed for `hermes-agent-brave-status` and `wardenclyffe-ssh`.
- 2026-06-11T17:52:58-06:00: Added source-of-truth/timestamp parity policy draft, parity checker, and verified Wardenclyffe Kubuntu SSH bridge card; messaging remains blocked with no connected targets.
- 2026-06-11T17:03:04-06:00: Cleaned stale publish-status wording; remote main verified at `4cc409d8712561f23c5a9a6b082e5edac769271b` before cleanup commit.
- 2026-06-11T16:44:49-06:00: Resolved GitHub auth path by using `HOME=/home/guidingl`; pushed `main` to `origin` with remote ref `70c83bbb5c746c84ab6c77d1659e25ee87b4fe23` before final status commit.
- 2026-06-11T16:21:24-06:00: Created local commit `f5033b8e5edcc5fa2cf01fcedd1a2f40c137c881`; later pushed successfully once real-user HOME GitHub auth was used.
- 2026-06-11T16:06:12-06:00: Added AI-facing handoff, lessons learned, global decisions, lane handoff, and LibreOffice artifact documentation for this session.
- 2026-06-11T15:54:59-06:00: Created and verified Uma's agent-only Brave profile lane on port `9223` with launch/status/stop/CDP helpers.
- 2026-06-11T15:43:16-06:00: Focused capability work on `capabilities-connections-control/` and added verified internet/browser/control ingredients plus the composed control stack.
- 2026-06-11T15:35:57-06:00: Created main Uma/Hermes project pointer and dedicated capability roots for connections/control, collaboration/autonomy, and agent infrastructure.
- 2026-06-11: Confirmed/finished full LibreOffice suite install on Banebook and created `artifacts/libreoffice/cheese-poem.odt` as a small proof artifact.
