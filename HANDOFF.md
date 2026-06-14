# Hermes Tasks Handoff

## 2026-06-14T13:57:08-06:00 continuation - ADB/scrcpy app-testing lane prepared

- User clarified Level 4 ADB/scrcpy is needed for app testing. Treat this as attended app-testing, not standing unattended phone control.
- Installed `adb`, `fastboot`, `scrcpy`, and `android-udev-rules` on Banebook and Wardenclyffe.
- Verified versions on both: ADB/Fastboot `34.0.5-debian`, scrcpy `3.3.4`.
- `adb devices -l` shows no paired devices yet on either machine; pairing requires user-present S24 Wireless Debugging code/ports.
- Added `capabilities-connections-control/ingredients/samsung-s24-adb-scrcpy-app-testing.md`.

## 2026-06-14T13:29:12-06:00 continuation - reverse SSH hardened and S24 online explained

- User confirmed the Samsung S24 is online in Tailscale and asked for an Uma explanation before choosing phone access level.
- Verified `Bane  24Ultra` / `100.75.32.46` is online and `tailscale ping` returns pongs via DERP and direct LAN.
- Expanded `capabilities-connections-control/kitchen/samsung-s24-tailscale-access-options-2026-06-14.md` with plain-English explanations of presence, file sync, KDE Connect, Termux SSH, and ADB/scrcpy.
- User approved Wardenclyffe -> Banebook SSH hardening. Updated Banebook `/home/guidingl/.ssh/authorized_keys` line for the existing Wardenclyffe key with `from="100.109.191.31,fd7a:115c:a1e0::e43a:bf20",no-agent-forwarding,no-X11-forwarding,no-port-forwarding`.
- Verification after hardening returned `BANEBOOK`, `guidingl`, and `REVERSE_SSH_HARDENED_PASS`. Backup: `/home/guidingl/.ssh/authorized_keys.bak-wardenclyffe-harden-20260614T132855-0600`.

## 2026-06-14T13:09:00-06:00 continuation - bidirectional agent and mobile access inventory

- Verified Banebook -> Wardenclyffe SSH and Wardenclyffe -> Banebook SSH live.
- Added `capabilities-collaboration-autonomy/recipes/banebook-wardenclyffe-bidirectional-agent-coordination.md` for lane-gated cross-machine agent work.
- Samsung S24 appears on Tailscale as `Bane  24Ultra` / `100.75.32.46` / Android, but was offline during inventory.
- Added `capabilities-connections-control/kitchen/samsung-s24-tailscale-access-options-2026-06-14.md` explaining safe access levels: presence, file sync, Termux SSH, KDE Connect, and attended ADB/scrcpy.
- No additional SSH/security settings were changed in this continuation; future key hardening or phone pairing still needs explicit approval.

## 2026-06-13T20:04:31-06:00 continuation - Wardenclyffe WebUI access configured from Banebook

- Built Wardenclyffe Hermes dashboard assets and installed enabled user service `~/.config/systemd/user/hermes-dashboard.service`.
- Service command: `hermes dashboard --host 127.0.0.1 --port 9119 --no-open --skip-build`.
- Banebook access is through SSH tunnel helper `wardenclyffe-hermes-webui`; local URL is `http://127.0.0.1:9129`.
- Helpers installed on Banebook: `wardenclyffe-hermes-webui`, `wardenclyffe-hermes-webui-status`, `wardenclyffe-hermes-webui-stop`; desktop launcher installed at `~/.local/share/applications/wardenclyffe-hermes-webui.desktop`.
- Browser verification loaded `Hermes Agent - Dashboard`; gateway displayed running.
- Wardenclyffe default Hermes config changed from credit-gated `anthropic/claude-opus-4.6` to provider `nous`, model `stepfun/step-3.7-flash:free`; default no-override one-shot smoke returned `WARDENCLYFFE_DEFAULT_MODEL_PASS`.
- Kanban card `t_30f3972d` marked done; board stats are now done=3, blocked=3.
- Still do not use `--insecure` dashboard binding or copy auth/session/browser state between machines.


## 2026-06-13T19:48:26-06:00 continuation - Wardenclyffe worker dispatch gates v1.1 documented

- Expanded `capabilities-collaboration-autonomy/recipes/wardenclyffe-uma-worker-lanes-v1.md` with a v1.1 named dispatch matrix for `finance-clerk`, `researcher`, `builder`, `verifier`, `client-ops`, `life-admin`, and `browser-worker`.
- Each lane now has green/yellow/red action boundaries and minimum evidence requirements. The recipe also includes a dispatch readiness checklist, anti-overlap rule, stop/escalation requirements, and the Nous Free model rule (`stepfun/step-3.7-flash:free` unless credits/default model are intentionally changed).
- This documents future worker routing; it does **not** enable broad autonomous dispatch. Future cards still need lane/profile, workspace, allowed actions, evidence path, stop condition, and task-specific approval boundaries.
- Next safe step is likely Wardenclyffe WebUI access from Banebook (`t_30f3972d`) or a specific scoped worker card that cites the v1.1 gates.


## 2026-06-13T18:59:57-06:00 continuation - Wardenclyffe free-model Hermes smoke passed

- Ran one small local-only Wardenclyffe Hermes one-shot using verified Nous Portal auth and explicit free model `stepfun/step-3.7-flash:free`.
- The configured default `anthropic/claude-opus-4.6` is a paid model and returned a low-credits error on the Free subscription, so free-model discovery was performed through Hermes' own model-selection helpers. Selectable free models observed: `stepfun/step-3.7-flash:free` and `nvidia/nemotron-3-ultra:free`.
- Smoke artifact is `artifacts/model-smoke/wardenclyffe-nous-free-model-smoke-20260613.json` and validates as JSON with `result: PASS`, `provider_actual: Nous Portal`, `model_actual: stepfun/step-3.7-flash:free`, and `local_only: true`.
- Wardenclyffe Kanban card `t_89e4c633` received a non-secret comment with this evidence but remains blocked for broader dispatch/approval-rule design.
- Do not treat this as broad autonomous-worker approval; it proves model execution only.


## 2026-06-13T18:51:06-06:00 continuation - Wardenclyffe Nous Portal provider auth verified

- Wardenclyffe Hermes Nous Portal login completed through user-approved Free-plan/email device-code flow; no Banebook auth/session/browser state was copied.
- Verification from Wardenclyffe: `hermes status` shows `Nous Portal ✓ logged in`, Provider `Nous Portal`, model `anthropic/claude-opus-4.6`, inference URL `https://inference-api.nousresearch.com/v1`, managed tools available, gateway active/enabled, and `hermes cron list` shows no scheduled jobs.
- Wardenclyffe Kanban card `t_626918f9` (`Fresh provider auth for Wardenclyffe Hermes workers`) was marked done and commented with the verification. The remaining five `uma-operating-loop` cards stay blocked until their separate access/dispatch/approval decisions are made.
- Next safe step is not broad autonomous dispatch; run a scoped model-backed Hermes worker smoke only after explicit approval for that smoke and its boundaries.


TS:2026-06-13T13:20:40-06:00 | Check:Wardenclyffe worker-lane rules and Codex local-only smoke | Confidence:high

## Current state

- Repo: `/home/guidingl/projects/hermes-tasks`
- Branch: `main` tracking `origin/main`
- Remote: `https://github.com/CBaen/hermes-tasks`
- Source-of-truth entrypoint: `SOURCE-OF-TRUTH.md`
- Runtime/profile state remains outside this repo.


## 2026-06-13T13:20:40-06:00 continuation - Wardenclyffe worker-lane rules and Codex smoke

- User approved creating Wardenclyffe Uma worker-lane rules from Codex AGENTS, agent-coordination, Hermes Tasks docs, and capability roots. Boundary: local-only Codex smoke; no external sends, no account changes, no production deploys, no money movement, no secrets, and no destructive cleanup.
- Added `capabilities-collaboration-autonomy/recipes/wardenclyffe-uma-worker-lanes-v1.md` with v1 lane rules for Researcher, Builder, Reviewer, Ops, and Finance/Admin lanes. The existing global standing-permission tiers remain candidate/proposed; this v1 approval is narrower and local-only.
- Added `capabilities-agent-infrastructure/ingredients/wardenclyffe-codex-hermes-auth-boundary.md` recording the verified split: Wardenclyffe Codex CLI is logged in via ChatGPT, Wardenclyffe Hermes gateway/scheduler works, and Wardenclyffe Hermes provider auth was later completed via Nous Portal.
- Ran Wardenclyffe Codex CLI as a bounded local-only worker with workspace-write sandbox and ephemeral session. It inspected only the approved local docs, wrote only `artifacts/worker-smoke/wardenclyffe-codex-worker-smoke.md`, and recorded `Result: PASS`.
- Synced the new non-secret lane docs/index links to Wardenclyffe's `~/projects/hermes-tasks` clone and copied the smoke artifact back to Banebook.
- Provider-login blocker resolved later at 2026-06-13T18:51:06-06:00: user selected Nous Portal Free-plan/email flow, completed Privy email confirmation, and Wardenclyffe `hermes status` verified Nous Portal login.

## 2026-06-13T13:01:08-06:00 continuation - Wardenclyffe primary Uma/Hermes home base

- User explicitly approved Wardenclyffe as the primary always-on Uma/Hermes home base and approved fresh install/config there without copying Banebook secrets/auth/session/browser state.
- Verified target: Banebook controls `WARDENCLYFFE` over Tailscale/OpenSSH. Wardenclyffe user is `guidingl`; OS reported Linux `7.0.0-22-generic`.
- Fresh Hermes installed on Wardenclyffe at `/home/guidingl/.hermes/hermes-agent`; `~/.hermes` was absent before install. Installer used official `https://hermes-agent.nousresearch.com/install.sh` with setup skipped.
- No Banebook `auth.json`, sessions, browser profile, caches, logs, or `.env` secrets were copied. Wardenclyffe provider auth was later completed fresh via Nous Portal; broad autonomous model-backed work still needs scoped smoke/dispatch approval.
- Gateway installed as enabled user systemd service `hermes-gateway.service`; `loginctl` linger is enabled; status verified active/running. `/usr/local/bin/hermes` points to `/home/guidingl/.local/bin/hermes` so non-interactive SSH commands resolve `hermes`.
- Script-only cron scheduling verified without model credentials: one-shot job `5ef2a9f71a02` ran via gateway and wrote `Wardenclyffe Hermes gateway smoke fired at 2026-06-13T13:00:19-06:00`; after repeat `1`, `hermes cron list` showed no scheduled jobs.
- Cloned repos on Wardenclyffe:
  - `/home/guidingl/projects/hermes-tasks` on `main` tracking `origin/main`.
  - `/home/guidingl/projects/hermes-webui` on branch `scheduled-kanban-webui` with only the seven intended Scheduled Kanban files dirty.
- Applied Scheduled Kanban WebUI patch cleanly on Wardenclyffe. Validation passed: `python3 -m py_compile api/kanban_bridge.py`, `node --check static/panels.js`, `node --check static/i18n.js`, `git diff --check`, `python3 -m pytest tests/test_kanban_bridge.py tests/test_kanban_ui_static.py -q` -> `90 passed`, and isolated real-Hermes scheduled-card smoke returned scheduled column + `after_unblock_status= ready`.
- Playwright bundled Chromium install failed during Hermes install because Playwright does not support `ubuntu26.04-x64`; browser automation on Wardenclyffe should use the installed Brave/CDP path or a later supported Playwright/browser workaround.
- Wardenclyffe Kanban board `uma-operating-loop` created with six blocked backlog cards: provider auth, Wardenclyffe WebUI access, worker lanes/approval gates, daily review job, decision cockpit, and finance pipeline spec. All are blocked to avoid premature dispatch before provider auth and approval rules are configured.

## What changed this continuation

1. Identified stale timestamp/status drift in `PROJECT-STATUS.md`, `HANDOFF.md`, and `agent-lanes/BOARD.md` after the publish cleanup.
2. Added `SOURCE-OF-TRUTH.md` with authority order, timestamp contract, parity rule, and self-referential commit rule.
3. Added `tools/check_source_of_truth_parity.py` as a lightweight parity verifier.
4. Added `capabilities-agent-infrastructure/principles/source-of-truth-timestamp-parity.md`.
5. Verified messaging is not ready: no connected delivery targets discovered.
6. Verified Wardenclyffe bridge by absolute helper path:
   - `/home/guidingl/bin/wardenclyffe-status`
   - Tailscale ping and SSH succeeded.
   - Current target is `WARDENCLYFFE` running `Linux 7.0.0-14-generic x86_64`.
   - `/home/guidingl/bin/wardenclyffe-ps` is retired and says to use SSH/Linux commands.
7. Added `capabilities-connections-control/ingredients/wardenclyffe-kubuntu-ssh-bridge.md`.
8. Verified and documented the Hermes terminal PATH bridge so helper commands resolve by name in new terminal calls.


## 2026-06-11T22:37:43-06:00 continuation

- Followed Wardenclyffe handoff `agent-coordination/wardenclyffe-kubuntu-restore/handoffs/banebook-ssh-unblock-2026-06-11.md`.
- Added only the exact verified Wardenclyffe public key to Banebook `/home/guidingl/.ssh/authorized_keys`; fingerprint `SHA256:Cl5SYra87E5eyA/cy4PWPDAj1aoYm9HmxYLU0hhzmGM`.
- Wardenclyffe-side `ssh -o BatchMode=yes banebook` verification succeeded and returned `BANEBOOK`, `guidingl`, and expected Codex framework skills.
- Regenerated and validated Slack manifest at `artifacts/messaging/hermes-slack-manifest.json`.
- Messaging target discovery still finds no connected targets; Slack/WhatsApp/Signal require user-side account linking before delivery works.

## 2026-06-12T16:26:51-06:00 continuation - Locally Twisted vendor cleanup

- Reviewed user-open Bluehost, Locally Twisted Gmail, and GoDaddy tabs through the user/live Brave CDP lane after the user asked Uma to confirm cancellation safety.
- Verified public `locallytwisted.com` service posture before account changes:
  - Cloudflare is authoritative DNS.
  - Cloudflare MX is present.
  - Frappe Cloud serves the live site.
- Verified GoDaddy still appeared to be registrar for `locallytwisted.com`; expiration observed as `2027-05-19`.
- GoDaddy login/access remained blocked by GoDaddy/Akamai EdgeSuite/504-style errors; this is queued as later work.
- Bluehost Billing Center showed two relevant products tied to `locallytwisted.com`: SiteLock Essentials and WordPress Basic Hosting.
- User explicitly approved turning off auto-renew for both Bluehost products and approved retiring the old Bluehost WordPress entries under that plan.
- Completed Bluehost confirmation flows for both products. Bluehost showed processing notices.
- Verified Bluehost Renewal Center/API state after the flows: `AutoRenewOn=0`, `AutoRenewOff=1`, and WordPress Basic Hosting `autoRenew=false`.
- Important caveat: the visible Bluehost Angular table/cache continued to paint stale on-state switches after reload. Treat provider/backend renewal API state as stronger evidence than the stale table, and do not retry toggles solely because that visible table looks old.
- Added reusable capability recipe `capabilities-connections-control/recipes/approval-gated-account-page-automation.md` for logged-in account-page work with explicit approval gates and stale-UI/API verification.

## Current verified browser/control state

- User/live Brave CDP lane: `http://127.0.0.1:9222`
- Agent-only Brave CDP lane: `http://127.0.0.1:9223`
- Agent-only profile path: `/home/guidingl/.local/share/hermes/agent-brave-profile`
- Hermes terminal PATH bridge: `/home/guidingl/.hermes/profiles/banebook/terminal-path-bridge.sh` is active through `terminal.shell_init_files`.
- Helper command names now resolve in new terminal calls: `hermes-agent-brave-status`, `hermes-agent-cdp`, `wardenclyffe-status`, `wardenclyffe-ssh`.
- Absolute helper paths remain safe fallbacks.

## Guardrails for next agent

- Do not copy browser profiles, cookies, auth stores, `.env` files, tokens, passwords, wallet keys, or raw logs into this repo.
- Use `9222` only for user/live tabs the user asks Uma to inspect.
- Use `9223` for independent public browsing and control tests.
- Prefer CDP/DOM/API/CLI/file artifacts over `xdotool` or `ydotool`.
- Wardenclyffe is currently verified as Kubuntu/Linux over SSH; do not rely on stale Windows/PowerShell assumptions.
- Wardenclyffe now owns always-on Hermes gateway/scheduler runtime. Banebook remains the cockpit/review/live-browser station. Do not blindly sync `~/.hermes`, auth, sessions, browser state, logs, or Kanban SQLite between machines.
- Wardenclyffe reverse SSH into Banebook is now authorized for the exact handoff key; do not add more keys or weaken SSH settings without explicit approval.
- Still stop before final external actions: submissions, messages, uploads, account/security changes, payments, signatures, loan acceptance, production deployments, destructive deletes, Docker pruning, backup removal, reboots, or service stops.
- For logged-in account pages, keep private details out of repo docs: no raw emails, account IDs, payment details, personal contact fields, screenshots containing sensitive account data, cookies, tokens, or raw browser/session dumps.
- For `locallytwisted.com`, do not cancel/close GoDaddy or allow domain registration to lapse until Cloudflare Registrar transfer is complete or the user explicitly chooses to keep/change the registrar path.
- Re-verify vendor state before future billing/domain actions; cached single-page app UI may be stale after a provider success response.

## Publish/GitHub status

- GitHub operations from Hermes terminal require real-user home auth: `HOME=/home/guidingl git ...` or `HOME=/home/guidingl gh ...`.
- Use live git commands for current remote truth; embedded SHAs are only historical evidence snapshots.

## Validation commands

```bash
python tools/check_source_of_truth_parity.py
python /home/guidingl/projects/capabilities-framework/tools/validate_project_shape.py --project /home/guidingl/projects/hermes-tasks --project-slug hermes-tasks
python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-connections-control --json
python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-agent-infrastructure --json
```

## Remaining work

- Choose the Wardenclyffe Hermes provider, then authenticate/configure Hermes fresh for LLM workers; no Banebook auth was copied.
- Decide whether to run Wardenclyffe WebUI as a persistent service and how Banebook should reach it over Tailscale.
- Add messaging/notification capability only after a real platform is connected and verified. Prepared path is Slack manifest + user-provided Slack tokens/app install.
- Decide whether to delete the old 63M test profile at `/home/guidingl/.hermes/profiles/banebook/home/.local/share/hermes/agent-brave-profile`; do not delete without explicit approval.
- Keep `SOURCE-OF-TRUTH.md` and parity docs current whenever state changes.
- Recover GoDaddy access for `locallytwisted.com`, check only non-domain GoDaddy products for cancellation, and preserve domain registration until Cloudflare Registrar transfer or explicit registrar decision is complete.
