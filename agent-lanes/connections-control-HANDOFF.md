# Connections Control Lane

TS:2026-06-11T22:37:43-06:00 | Check:Wardenclyffe reverse SSH, Slack manifest, messaging discovery | Confidence:high

## Scope

- Write scope: `capabilities-connections-control/`, connection/control docs in root project files, and this lane handoff.
- Do not edit: secrets, browser profiles, cookies, raw auth/session state, account data dumps, unrelated project roots, or external profile runtime material unless explicitly approved.

## Goal

Make Uma/Hermes better connected and able to execute internet/browser/remote-control tasks independently on Banebook while avoiding physical cursor/keyboard takeover and preserving approval gates.

## Current Status

Status: Implemented and expanded with verified Wardenclyffe bidirectional SSH; messaging prepared but not connected.

## Changed Files

- `capabilities-connections-control/INDEX.md`
- `capabilities-connections-control/ingredients/public-internet-access.md`
- `capabilities-connections-control/ingredients/local-brave-cdp-open-tabs.md`
- `capabilities-connections-control/ingredients/browser-protocol-page-control-and-typing.md`
- `capabilities-connections-control/ingredients/desktop-input-control-boundary.md`
- `capabilities-connections-control/ingredients/wardenclyffe-kubuntu-ssh-bridge.md`
- `capabilities-connections-control/ingredients/wardenclyffe-to-banebook-ssh-access.md`
- `capabilities-connections-control/recipes/agent-only-browser-lane.md`
- `capabilities-connections-control/meals/internet-and-browser-control-stack.md`
- Root docs that route/record this work: `README.md`, `PROJECT-STATUS.md`, `hermes-tasks-index.md`, `hermes-tasks-decisions.md`, `GLOBAL-DECISIONS.md`, `LESSONS-LEARNED.md`, `HANDOFF.md`, `SOURCE-OF-TRUTH.md`.

## Messaging Artifacts

- `artifacts/messaging/hermes-slack-manifest.json` - generated Slack manifest, no tokens.
- `artifacts/messaging/messaging-options-2026-06-11.md` - Slack/WhatsApp/Signal setup assessment.

## Runtime Files Created Outside Repo

- `/home/guidingl/.local/bin/hermes-agent-brave`
- `/home/guidingl/.local/bin/hermes-agent-brave-status`
- `/home/guidingl/.local/bin/hermes-agent-brave-stop`
- `/home/guidingl/.local/bin/hermes-agent-cdp`
- `/home/guidingl/.local/share/applications/hermes-agent-brave.desktop`
- `/home/guidingl/.local/share/hermes/agent-brave-profile/`

Do not commit those runtime files into this repo. This handoff and the capability recipe document their expected behavior.

## Runtime Files Discovered Outside Repo

- `/home/guidingl/bin/wardenclyffe-status`
- `/home/guidingl/bin/wardenclyffe-ssh`
- `/home/guidingl/bin/wardenclyffe-sftp`
- `/home/guidingl/bin/wardenclyffe-rdp`
- `/home/guidingl/bin/wardenclyffe-rdp-multimon`
- `/home/guidingl/bin/wardenclyffe-ps` - retired prior Windows workflow; exits with instruction to use SSH/Linux commands.

Hermes terminal PATH bridge is now active through `/home/guidingl/.hermes/profiles/banebook/terminal-path-bridge.sh`; helper command names resolve in new terminal calls. Absolute paths remain safe fallbacks.

## Validation

Latest known checks:

- Project shape validator: ok=true, 0 errors, 0 warnings.
- Connections/control capability graph: ok=true, 7 cards, 0 errors, 0 warnings.
- Agent-only CDP lane: `127.0.0.1:9223` reachable.
- User/live CDP lane: `127.0.0.1:9222` reachable.
- Agent-only browser control proof: inserted/read back `Hermes agent profile typed this via CDP` in earlier session.
- Messaging target discovery: `send_message(action="list")` returned no connected targets; Slack manifest validates but user account/app linking is still required.
- Wardenclyffe status: Tailscale ping, TCP 22, and SSH inventory succeeded; current OS is Kubuntu/Linux, not retired Windows PowerShell workflow.
- Wardenclyffe -> Banebook reverse SSH succeeded after exact key authorization from the Wardenclyffe handoff.
- PATH bridge: `hermes-agent-brave-status` and `wardenclyffe-ssh` resolve by name and smoke checks passed on 2026-06-11T18:17:03-06:00.

## Remaining Debt

- Add a real notification/messaging capability only after a platform target is connected and verified. Prepared path: Slack manifest plus user-installed app/tokens.
- Decide whether to keep, ignore, or delete the old 63M test profile under Hermes internal profile-home path; do not delete without explicit approval.

## Handoff Notes

Use the agent-only browser lane for public research and independent browsing. Use the user/live lane only when the user needs help with a page already open in their normal Brave session, especially logged-in account pages. Use Wardenclyffe only through verified Linux/SSH helpers and keep risky remote actions behind approval gates.
