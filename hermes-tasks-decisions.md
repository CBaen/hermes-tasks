## 2026-06-13T20:04:31-06:00 - Configure Wardenclyffe WebUI as localhost service plus Banebook SSH tunnel

Decision: Run Wardenclyffe Hermes dashboard persistently as a user systemd service bound to `127.0.0.1:9119`, and expose it to Banebook through an SSH localhost tunnel at `http://127.0.0.1:9129` using helper commands. Do not use `hermes dashboard --insecure` or bind the dashboard to `0.0.0.0`.

Reason: Wardenclyffe should own the always-on Hermes runtime while Banebook remains the cockpit. The dashboard can expose sensitive configuration surfaces, so localhost-only binding plus SSH tunneling gives broad cockpit access without copying auth/session/browser state or exposing the dashboard on Tailscale/LAN.

Evidence: Built Wardenclyffe dashboard assets, installed/enabled `~/.config/systemd/user/hermes-dashboard.service`, verified `systemctl --user is-enabled/is-active` => enabled/active, verified Wardenclyffe listener `127.0.0.1:9119`, installed Banebook helpers `wardenclyffe-hermes-webui`, `wardenclyffe-hermes-webui-status`, `wardenclyffe-hermes-webui-stop`, verified local listener `127.0.0.1:9129`, and browser navigation loaded `Hermes Agent - Dashboard`. Also changed Wardenclyffe default model to `stepfun/step-3.7-flash:free` with provider `nous` so the Free subscription's WebUI path works by default; no-override `hermes -z` smoke returned `WARDENCLYFFE_DEFAULT_MODEL_PASS`.

Rollback / next: Stop Banebook tunnel with `wardenclyffe-hermes-webui-stop`; stop remote service with `wardenclyffe-hermes-webui-stop --remote` or `systemctl --user stop hermes-dashboard.service` on Wardenclyffe. Next operating-loop work can use the WebUI/tunnel directly while preserving hard stops for external sends, account/security changes, money, production/client mutation, destructive deletion, Docker pruning, and backup removal.

## 2026-06-13T19:48:26-06:00 - Document named Wardenclyffe worker dispatch gates v1.1

Decision: Expand the Wardenclyffe worker-lane recipe into a named dispatch matrix for `finance-clerk`, `researcher`, `builder`, `verifier`, `client-ops`, `life-admin`, and `browser-worker`, each with green/yellow/red action boundaries and minimum evidence requirements.

Reason: Provider auth and a free-model smoke are now verified, but that proves execution only. Wardenclyffe still needs human-readable gates so future Kanban cards can be safely routed without confusing local preparation with external/account/client/financial execution.

Evidence: Updated `capabilities-collaboration-autonomy/recipes/wardenclyffe-uma-worker-lanes-v1.md` with v1.1 named lanes, dispatch readiness checklist, model/provider free-tier rule, anti-overlap rule, evidence bars, and stop conditions. This change documents how future workers may be scoped; it does not turn on broad autonomous dispatch.

Rollback / next: Revert or revise the v1.1 section if the user changes the autonomy boundary. Future worker cards should cite a lane/profile, workspace, green/yellow/red classification, allowed actions, evidence artifact, stop condition, and anti-overlap rule before leaving blocked/triage.

## 2026-06-13T18:59:57-06:00 - Use free Nous model for Wardenclyffe model-backed smoke

Decision: Treat the first Wardenclyffe Hermes model-backed smoke as a local-only one-shot inference using explicit Nous free model `stepfun/step-3.7-flash:free`, not the configured paid default model.

Reason: Wardenclyffe is authenticated to Nous Portal on the Free subscription. The configured default model `anthropic/claude-opus-4.6` required available credits and returned a low-balance/paid-model error. Hermes' own model-selection helpers reported selectable free models `stepfun/step-3.7-flash:free` and `nvidia/nemotron-3-ultra:free`.

Evidence: `wardenclyffe-ssh` ran `hermes --provider nous --model "stepfun/step-3.7-flash:free" -z <local-only prompt>`. The response was valid JSON with `result: PASS`, `provider_actual: Nous Portal`, `model_actual: stepfun/step-3.7-flash:free`, and `local_only: true`, saved at `artifacts/model-smoke/wardenclyffe-nous-free-model-smoke-20260613.json` on both Wardenclyffe and Banebook.

Rollback / next: Do not enable broad model-backed dispatch based solely on this smoke. Keep default paid-model mismatch in mind; either choose a free default model or use explicit free model overrides until credits/plan are intentionally changed.

## 2026-06-13T18:51:06-06:00 - Complete fresh Wardenclyffe Nous Portal provider authentication

Decision: Use Nous Portal as the fresh Wardenclyffe Hermes provider login path and verify it before any model-backed worker dispatch.

Reason: Wardenclyffe is the approved always-on Hermes runtime host, but auth/session/browser state must not be copied from Banebook. A fresh provider login on the runtime host satisfies the runtime requirement while preserving the machine-boundary rule.

Evidence: User selected Nous Portal, approved the Free $0/mo plan path, selected email login, approved the email-login submission, and completed the Privy email confirmation. Wardenclyffe background helper reported `NOUS_BROWSER_APPROVAL_RECEIVED` and `NOUS_CREDENTIALS_SAVED label=Wardenclyffe Nous Portal`. Verification with `wardenclyffe-ssh 'hermes status'` showed `Nous Portal ✓ logged in`, Provider `Nous Portal`, model `anthropic/claude-opus-4.6`, managed tools available, gateway active/enabled, and no scheduled cron jobs.

Rollback / next: Remove/revoke Wardenclyffe Nous credentials only if the user asks or account security requires it. Do not copy these auth files to Banebook. Next model-backed work should be a narrow smoke/worker task with explicit approval-boundary review before broad dispatch.

# Hermes Tasks Decisions

Newest entries first.

## 2026-06-14T13:09:00-06:00 - Treat Banebook and Wardenclyffe as lane-gated bidirectional agent hosts

Decision: Support automated agents on both Banebook and Wardenclyffe through Tailscale/SSH, but route work through explicit worker lanes, route records, and approval boundaries instead of broad unsupervised cross-machine control.

Reason: The user wants both computers to connect and work with each other. Bidirectional SSH is verified, Wardenclyffe is the always-on runtime, and Banebook remains the cockpit/live-desktop station. Lane gates prevent file overlap, secret copying, and accidental account/security/external actions.

Evidence: `wardenclyffe-ssh 'hostname; whoami'` returned `WARDENCLYFFE guidingl`; `wardenclyffe-ssh 'ssh -o BatchMode=yes banebook "hostname; whoami"'` returned `BANEBOOK guidingl`.

## 2026-06-14T13:09:00-06:00 - Treat Samsung S24 Tailscale presence as inventory, not control

Decision: Document the Samsung S24 as a visible Tailscale Android peer and require an explicit phone-side service choice before agents can access or work on it.

Reason: Tailscale gives reachability, not Android control. File access, shell access, notifications/SMS, screen control, and app automation each require different phone permissions and risk gates.

Evidence: `tailscale status --json` from Banebook and Wardenclyffe showed `Bane  24Ultra` at `100.75.32.46`, OS `android`, offline during the check.

## 2026-06-13T13:20:40-06:00 - Use documented local-only Wardenclyffe worker lanes before dispatching Codex/Hermes workers

Decision: Create Wardenclyffe Uma worker-lane rules v1 from Codex AGENTS, agent-coordination, Hermes Tasks docs, and capability roots, and use those rules before further worker dispatch. Treat Codex CLI and Hermes provider auth as separate runtime credentials.

Reason: Wardenclyffe is now the always-on runtime host, but autonomous work needs clear lanes, anti-overlap rules, evidence requirements, and explicit stop conditions. Codex can support approved local-only worker lanes now, while Hermes LLM worker execution still requires fresh provider authentication.

Evidence: User approved local-only worker-lane rule creation and one Codex smoke test with boundaries forbidding external sends, account changes, production deploys, money movement, secrets, and destructive cleanup. Added `capabilities-collaboration-autonomy/recipes/wardenclyffe-uma-worker-lanes-v1.md` and `capabilities-agent-infrastructure/ingredients/wardenclyffe-codex-hermes-auth-boundary.md`. Wardenclyffe Codex CLI smoke ran in `/home/guidingl/projects/hermes-tasks`, wrote only `artifacts/worker-smoke/wardenclyffe-codex-worker-smoke.md`, and recorded `Result: PASS`.

Rollback / next: Remove or revise the v1 rule files if the user changes the autonomy boundary. Provider login was later completed fresh via Nous Portal on Wardenclyffe; do not copy auth between machines, and require a scoped smoke/dispatch decision before broad model-backed worker use.

## 2026-06-13T13:01:08-06:00 - Make Wardenclyffe the primary always-on Uma/Hermes runtime host

Decision: Use Wardenclyffe as the primary always-on Uma/Hermes home base for gateway, scheduled jobs, Kanban dispatch/workers, and future uninterrupted background work, while Banebook remains the daily cockpit/review/live-browser station.

Reason: Wardenclyffe runs continuously and is reachable over Tailscale/OpenSSH, while Banebook does not stay on reliably enough for scheduled tasks or uninterrupted workers. Splitting runtime ownership this way avoids missed jobs and avoids unsafe bidirectional syncing of mutable Hermes runtime state.

Evidence: User explicitly approved this setup. Wardenclyffe fresh Hermes install succeeded at `/home/guidingl/.hermes/hermes-agent` without copying Banebook auth/session/browser state. `hermes-gateway.service` is enabled/running as a user service with linger enabled; script-only one-shot cron job fired automatically at `2026-06-13T13:00:19-06:00`; `hermes cron list` showed no remaining smoke jobs afterward. WebUI Scheduled Kanban patch on Wardenclyffe branch `scheduled-kanban-webui` passed syntax checks, `git diff --check`, targeted Kanban tests (`90 passed`), and isolated real-Hermes scheduled-card smoke.

Rollback / next: Stop/disable Wardenclyffe gateway with `hermes gateway stop` and `systemctl --user disable hermes-gateway.service` if Wardenclyffe should no longer own always-on work. Do not sync `~/.hermes`, auth, sessions, browser state, logs, caches, or Kanban SQLite across machines. Fresh Wardenclyffe Nous Portal provider authentication was completed later on 2026-06-13T18:51:06-06:00; next requirement is a scoped model-backed worker smoke before broad dispatch.

## 2026-06-12T16:26:51-06:00 - Disable Bluehost auto-renew while preserving Locally Twisted registrar safety

Decision: Turn off auto-renew for Bluehost SiteLock Essentials and WordPress Basic Hosting tied to `locallytwisted.com`, and keep GoDaddy registrar cleanup separate until domain registration is transferred or intentionally retained.

Reason: Public verification showed Cloudflare is authoritative DNS, Cloudflare MX is present, and Frappe Cloud serves the live site, so the Bluehost hosting/security renewals were not needed for the current live website. Registrar/ownership renewal is a separate control plane; GoDaddy still appeared to be registrar, so cancelling/closing GoDaddy would risk domain ownership if done before transfer or explicit registrar decision.

Evidence: User explicitly approved disabling Bluehost auto-renew for both named products. Bluehost confirmation flows completed and showed processing notices. Bluehost Renewal Center/API verification showed `AutoRenewOn=0`, `AutoRenewOff=1`, and WordPress Basic Hosting `autoRenew=false`, while the visible Angular table/cache remained stale. RDAP verification showed GoDaddy still appeared to be registrar with expiration `2027-05-19`; GoDaddy access remained blocked by EdgeSuite/504-style login errors.

Rollback / next: Re-enable or repurchase Bluehost products only if intentionally needed. Recover GoDaddy access, check only non-domain GoDaddy products for cancellation, and preserve domain registration until Cloudflare Registrar transfer or explicit registrar decision is complete.

## 2026-06-11T22:37:43-06:00 - Authorize exact Wardenclyffe public key for reverse SSH into Banebook

Decision: Follow the Wardenclyffe handoff and add only the exact public key ending `wardenclyffe-1-to-banebook-tailscale-2026-06-11` to Banebook `/home/guidingl/.ssh/authorized_keys`.

Reason: The Wardenclyffe agent identified that Wardenclyffe could reach Banebook over Tailscale/OpenSSH but Banebook rejected Wardenclyffe's configured public key. The user directed this agent to follow that handoff.

Evidence: Fingerprint matched `SHA256:Cl5SYra87E5eyA/cy4PWPDAj1aoYm9HmxYLU0hhzmGM`; `authorized_keys` permissions are `600`; Wardenclyffe-side `ssh -o BatchMode=yes banebook` returned `BANEBOOK`, `guidingl`, and expected framework skill paths.

Rollback: Remove the `authorized_keys` line ending `wardenclyffe-1-to-banebook-tailscale-2026-06-11` or restore the timestamped `authorized_keys.bak-wardenclyffe-unblock-*` backup.

## 2026-06-11T22:37:43-06:00 - Prepare Slack first for Hermes notifications, park WhatsApp/Signal until user linking

Decision: Keep Slack as the best-prepared notification path because the Hermes Slack manifest is generated and Socket Mode does not need a public endpoint. WhatsApp and Signal remain assessed but blocked on user account/device linking.

Reason: Slack manifest generation is local and non-secret. WhatsApp requires QR pairing and carries unofficial bridge risk; Signal requires installing/linking `signal-cli`. All three require user-side account steps before real delivery.

Evidence: `artifacts/messaging/hermes-slack-manifest.json` validates with `socket_mode_enabled=true`, 50 slash commands, and 14 bot scopes; `send_message(action=list)` and `hermes send --list` report no connected targets.

Rollback: Delete or regenerate the Slack manifest artifact. Do not remove any real messaging integration without checking live gateway config first.

## 2026-06-11T18:17:03-06:00 - Use a profile-local terminal PATH bridge for Banebook helper commands

Decision: Expose `/home/guidingl/.local/bin` and `/home/guidingl/bin` to Hermes terminal calls through the Banebook profile's `terminal.shell_init_files` and `/home/guidingl/.hermes/profiles/banebook/terminal-path-bridge.sh`.

Reason: The Hermes terminal PATH omitted real-user helper directories, so commands such as `hermes-agent-brave-status` and `wardenclyffe-ssh` required absolute paths. A profile-local init file is reversible and avoids changing system-owned PATH directories.

Evidence: On 2026-06-11T18:17:03-06:00, new terminal calls resolved `hermes-agent-brave`, `hermes-agent-cdp`, `hermes-agent-brave-status`, `wardenclyffe-status`, and `wardenclyffe-ssh`; smoke checks passed for `hermes-agent-brave-status` and `wardenclyffe-ssh 'hostname; uname -srm'`.

Rollback: Remove `/home/guidingl/.hermes/profiles/banebook/terminal-path-bridge.sh` from `terminal.shell_init_files` or restore backup `/home/guidingl/.hermes/profiles/banebook/config.yaml.bak-path-bridge-20260611T181644-0600`.

## 2026-06-11T17:52:58-06:00 - Wardenclyffe current target is Kubuntu SSH, not retired Windows PowerShell

Decision: Document Wardenclyffe's current reachable control surface as Kubuntu/Linux over Tailscale and SSH, while treating older Windows/PowerShell assumptions as stale unless reverified.

Reason: Live helper inspection and `/home/guidingl/bin/wardenclyffe-status` showed Wardenclyffe reachable as `WARDENCLYFFE` running Linux `7.0.0-14-generic x86_64`. The `wardenclyffe-ps` helper explicitly says the prior Windows workflow was removed.

Applies to: `capabilities-connections-control/ingredients/wardenclyffe-kubuntu-ssh-bridge.md`, future Wardenclyffe operations, and any doc claiming PowerShell/Windows routing.

Verification / evidence: Tailscale ping, TCP 22, SSH `id/hostname/uname`, filesystem inventory, and helper script inspection on 2026-06-11.

## 2026-06-11T16:44:49-06:00 - GitHub auth lives under real user HOME for Hermes shell pushes

Decision: Use `HOME=/home/guidingl` for GitHub CLI and git network operations from this Hermes session when pushing `hermes-tasks`.

Reason: Hermes terminal default `$HOME` is `/home/guidingl/.hermes/profiles/banebook/home`, where `gh auth status` is not logged in. The user completed GitHub auth under `/home/guidingl`, where `gh auth status` reports account `CBaen` with HTTPS git protocol.

Applies to: `git push`, `git ls-remote`, `gh auth status`, and future GitHub operations for `/home/guidingl/projects/hermes-tasks` from Hermes.

Verification / evidence: `HOME=/home/guidingl gh auth status` reported logged in to github.com account `CBaen`; `HOME=/home/guidingl git push -u origin main` succeeded and remote `main` reached `70c83bbb5c746c84ab6c77d1659e25ee87b4fe23`.

## 2026-06-11T16:21:24-06:00 - Remote push requires explicit GitHub authentication setup

Decision: Do not fake or bypass the GitHub push when credentials are unavailable. Record the local commit and auth blocker, then wait for an authenticated path.

Reason: The user asked to commit and push, but pushing to GitHub requires account authentication. This shell has no HTTPS credential helper/token, `gh` is not logged in, and SSH is denied. Adding persistent GitHub auth or SSH keys affects account/security state and needs the user's active login/authorization.

Applies to: remote `origin` at `https://github.com/CBaen/hermes-tasks`, local commit `f5033b8e5edcc5fa2cf01fcedd1a2f40c137c881`, and the `publish-session-state` queue item.

Verification / evidence: `git push -u origin main` failed with `could not read Username for 'https://github.com'`; `gh auth status` reported not logged in; `ssh -T git@github.com` returned permission denied.

## 2026-06-11T16:06:12-06:00 - Publish AI-readable operating state rather than runtime state

Decision: Commit/push the visible Hermes Tasks repo with AI-readable docs, capability cards, verifier declarations, handoffs, lessons, and safe verification artifacts; do not copy runtime browser profiles, cookies, auth stores, helper script contents from outside the repo, raw logs, or secrets into git.

Reason: The user asked for future agents to inherit the right information in the right documents. The durable inheritance value is the organized map, decisions, commands, guardrails, and verification evidence, not raw runtime state.

Applies to: `README.md`, `HANDOFF.md`, `LESSONS-LEARNED.md`, `GLOBAL-DECISIONS.md`, `PROJECT-STATUS.md`, queue/index/decisions docs, `agent-lanes/`, `capabilities-*`, `verifier-manifest.json`, and `artifacts/`.

Verification / evidence: New docs were written before final validation/commit. Runtime paths are documented but not copied. LibreOffice lock files are ignored with `.gitignore` pattern `.~lock.*#`.

## 2026-06-11T15:54:59-06:00 - Add verified agent-only Brave profile lane

Decision: Give Uma a separate persistent Brave profile for independent web work, distinct from Guiding Light's normal Brave profile.

Reason: The user explicitly approved Uma having her own profile and more access/control. A separate browser profile on its own CDP port lets Uma browse, navigate, inspect, and type through browser protocol without cluttering or taking over the user's live Brave tabs.

Applies to: `/home/guidingl/.local/share/hermes/agent-brave-profile`, `/home/guidingl/.local/bin/hermes-agent-brave`, `/home/guidingl/.local/bin/hermes-agent-brave-status`, `/home/guidingl/.local/bin/hermes-agent-brave-stop`, `/home/guidingl/.local/bin/hermes-agent-cdp`, `/home/guidingl/.local/share/applications/hermes-agent-brave.desktop`, and `capabilities-connections-control/recipes/agent-only-browser-lane.md`.

Verification / evidence: Agent-only Brave launched with `--user-data-dir=/home/guidingl/.local/share/hermes/agent-brave-profile` and CDP on `127.0.0.1:9223`; user/live Brave stayed reachable on `9222`; `hermes-agent-cdp control-proof` inserted/read back `Hermes agent profile typed this via CDP`; agent tab navigated to Hermes browser docs and read back title `Browser Automation | Hermes Agent`; `validate_capability_graph.py` for `capabilities-connections-control/` returned ok=true with 6 cards, 0 errors, 0 warnings.

## 2026-06-11T15:43:16-06:00 - Focus capability growth on connections/control first

Decision: Treat `capabilities-connections-control/` as the active capability-development focus and add actual verified internet/browser/control capabilities there before expanding other process roots.

Reason: Guiding Light clarified that the important current capability is Uma's connection to the internet plus ability to read, control, and type in browser pages. That is a real ingredient/ingredient collection, while broader collaboration/infrastructure roots should remain secondary until they contain tested capabilities.

Applies to: `capabilities-connections-control/`.

Verification / evidence: Added verified cards for public internet access, browser protocol page control and typing, desktop input control boundary, and the composed internet/browser control stack. `validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-connections-control --json` returned ok=true with 6 cards, 0 errors, and 0 warnings.

## 2026-06-11T15:35:57-06:00 - Split Uma/Hermes operating capabilities into dedicated roots

Decision: Treat `/home/guidingl/projects/hermes-tasks` as the visible main Uma/Hermes operating repo, keep runtime/profile files under `/home/guidingl/.hermes/profiles/banebook`, and add sibling capability roots for connections/control, collaboration/autonomy, and agent infrastructure.

Reason: Connection/control capabilities are important enough to be their own discoverable framework instead of being buried in the baseline project root. Collaboration permissions and infrastructure setup also need separate routing so future sessions can work in parallel without unnecessary pauses while preserving approval gates.

Applies to: `/home/guidingl/projects/hermes-tasks`, `/home/guidingl/Uma/HERMES-MAIN-PROJECT.md`, and the new roots `capabilities-connections-control/`, `capabilities-collaboration-autonomy/`, and `capabilities-agent-infrastructure/`.

Verification / evidence: Filesystem writes completed; indexes/status were patched; starter capability cards were added. `validate_project_shape.py` returned ok=true with 0 errors/0 warnings. `validate_capability_graph.py` returned ok=true with 0 errors/0 warnings for all three new sibling roots. The baseline root remains ok=true with pre-existing backlink warnings only.

## 2026-06-10T22:56:24-06:00 - Bring scaffold up to current lane/verifier standard

Decision: Add the current standard `agent-lanes/BOARD.md`, `agent-lanes/LANE-HANDOFF.template.md`, and `verifier-manifest.json` files to this persistent Hermes task project.

Reason: The current project shape validator expects these files for new serious-project scaffolds. Adding them keeps future Codex/Hermes sessions from treating the project as an older partial scaffold.

Applies to: `/home/guidingl/projects/hermes-tasks`.

Verification / evidence: project-shape and capability graph validators re-run after the scaffold update.

## YYYY-MM-DD - <Decision>

Decision:

Reason:

Applies to:

Verification / evidence:
