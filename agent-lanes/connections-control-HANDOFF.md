# Connections Control Lane

TS:2026-06-11T16:06:12-06:00 | Check:verified browser lanes, capability graph, and helper commands | Confidence:high

## Scope

- Write scope: `capabilities-connections-control/`, connection/control docs in root project files, and this lane handoff.
- Do not edit: secrets, browser profiles, cookies, raw auth/session state, account data dumps, unrelated project roots, or external profile runtime material unless explicitly approved.

## Goal

Make Uma/Hermes better connected and able to execute internet/browser tasks independently on Banebook while avoiding physical cursor/keyboard takeover and preserving approval gates.

## Current Status

Status: Implemented and verified.

## Changed Files

- `capabilities-connections-control/INDEX.md`
- `capabilities-connections-control/ingredients/public-internet-access.md`
- `capabilities-connections-control/ingredients/local-brave-cdp-open-tabs.md`
- `capabilities-connections-control/ingredients/browser-protocol-page-control-and-typing.md`
- `capabilities-connections-control/ingredients/desktop-input-control-boundary.md`
- `capabilities-connections-control/recipes/agent-only-browser-lane.md`
- `capabilities-connections-control/meals/internet-and-browser-control-stack.md`
- Root docs that route/record this work: `README.md`, `PROJECT-STATUS.md`, `hermes-tasks-index.md`, `hermes-tasks-decisions.md`, `GLOBAL-DECISIONS.md`, `LESSONS-LEARNED.md`, `HANDOFF.md`.

## Runtime Files Created Outside Repo

- `/home/guidingl/.local/bin/hermes-agent-brave`
- `/home/guidingl/.local/bin/hermes-agent-brave-status`
- `/home/guidingl/.local/bin/hermes-agent-brave-stop`
- `/home/guidingl/.local/bin/hermes-agent-cdp`
- `/home/guidingl/.local/share/applications/hermes-agent-brave.desktop`
- `/home/guidingl/.local/share/hermes/agent-brave-profile/`

Do not commit those runtime files into this repo. This handoff and the capability recipe document their expected behavior.

## Validation

Latest known checks:

- Project shape validator: expected ok=true, 0 errors, 0 warnings.
- Connections/control capability graph: ok=true, 6 cards, 0 errors, 0 warnings.
- Agent-only CDP lane: `127.0.0.1:9223` reachable.
- User/live CDP lane: `127.0.0.1:9222` reachable.
- Agent-only browser control proof: inserted/read back `Hermes agent profile typed this via CDP`.

## Remaining Debt

- Add a real notification/messaging capability only after a platform target is connected and verified.
- Add Wardenclyffe connection/control card only after helper commands are present and tested from this Hermes session.
- Decide whether to keep, ignore, or delete the old empty test profile under Hermes internal profile-home path.

## Handoff Notes

Use the agent-only browser lane for public research and independent browsing. Use the user/live lane only when the user needs help with a page already open in their normal Brave session, especially logged-in account pages.
