# Hermes Tasks Handoff

TS:2026-06-11T17:52:58-06:00 | Check:source-of-truth parity continuation after GitHub publish | Confidence:high

## Current state

- Repo: `/home/guidingl/projects/hermes-tasks`
- Branch: `main` tracking `origin/main`
- Remote: `https://github.com/CBaen/hermes-tasks`
- Source-of-truth entrypoint: `SOURCE-OF-TRUTH.md`
- Runtime/profile state remains outside this repo.

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

## Current verified browser/control state

- User/live Brave CDP lane: `http://127.0.0.1:9222`
- Agent-only Brave CDP lane: `http://127.0.0.1:9223`
- Agent-only profile path: `/home/guidingl/.local/share/hermes/agent-brave-profile`
- Wardenclyffe helper path: `/home/guidingl/bin/wardenclyffe-*`; use absolute paths unless Hermes PATH is fixed.

## Guardrails for next agent

- Do not copy browser profiles, cookies, auth stores, `.env` files, tokens, passwords, wallet keys, or raw logs into this repo.
- Use `9222` only for user/live tabs the user asks Uma to inspect.
- Use `9223` for independent public browsing and control tests.
- Prefer CDP/DOM/API/CLI/file artifacts over `xdotool` or `ydotool`.
- Wardenclyffe is currently verified as Kubuntu/Linux over SSH; do not rely on stale Windows/PowerShell assumptions.
- Still stop before final external actions: submissions, messages, uploads, account/security changes, payments, signatures, loan acceptance, production deployments, destructive deletes, Docker pruning, backup removal, reboots, or service stops.

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

- Finish validation, commit, push, and verify remote `main` for this parity update.
- Add messaging/notification capability only after a real platform is connected and verified.
- Decide whether to delete the old 63M test profile at `/home/guidingl/.hermes/profiles/banebook/home/.local/share/hermes/agent-brave-profile`; do not delete without explicit approval.
- Optionally fix Hermes PATH or document a reusable PATH bridge so `/home/guidingl/bin/wardenclyffe-*` and `/home/guidingl/.local/bin/hermes-agent-*` resolve without absolute paths.
