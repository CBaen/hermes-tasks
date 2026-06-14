# Hermes Tasks Source Of Truth

Last updated: 2026-06-14T13:09:00-06:00

## Purpose

Prevent stale-doc and source-of-truth drift for AI agents inheriting this repo.

## Authority order

When project facts conflict, use this order:

1. Live verification from the relevant system, command, browser/CDP endpoint, remote host, or official source.
2. Git state in this repo: `git status -sb`, `git log --oneline --decorate -n 5`, and `HOME=/home/guidingl git ls-remote --heads origin main`.
3. `PROJECT-STATUS.md` for current project state.
4. `HANDOFF.md` for session inheritance and known runtime details.
5. `hermes-tasks-queue.md` for active/next/parked/done work.
6. `hermes-tasks-decisions.md` and `GLOBAL-DECISIONS.md` for durable decisions and why.
7. `LESSONS-LEARNED.md` for reusable lessons, not live state.
8. Capability roots for reusable procedures and verified ingredients.
9. Older docs, memory, and conversation summaries only as clues until reverified.

## Timestamp contract

State-bearing updates must include an ISO-8601 timestamp with timezone, for example:

```text
2026-06-11T17:52:58-06:00
```

Required timestamp locations:

- `PROJECT-STATUS.md`: `Last updated:` line.
- `HANDOFF.md`: top `TS:` line and any new status block.
- `agent-lanes/BOARD.md`: `Last updated:` line plus lane status `TS:` blocks.
- `hermes-tasks-queue.md`: timestamp each new `Done` item and any time-sensitive active/blocked note.
- `hermes-tasks-decisions.md` / `GLOBAL-DECISIONS.md`: timestamp every decision heading.
- Capability cards: update `last_verified` only when real verification occurs.

## Parity rule

If an agent changes current state, the agent must update the matching docs in the same work session before committing:

- Current status changed -> update `PROJECT-STATUS.md` and `HANDOFF.md`.
- Active/next work changed -> update `hermes-tasks-queue.md`.
- Durable rule/decision changed -> update `hermes-tasks-decisions.md` or `GLOBAL-DECISIONS.md`.
- Capability changed -> update the owning capability root/index and run graph validation.
- Lane status changed -> update `agent-lanes/BOARD.md` and the lane handoff.
- Runtime fact discovered -> document the path/command/evidence, not secrets or raw runtime state.

## Self-referential commit rule

Do not rely on a document embedding the hash of the commit that contains itself. Use live git commands for the current commit/remote state. Embedded commit hashes are evidence snapshots only.

## Required parity check

Run this before publish when docs or capabilities change:

```bash
python tools/check_source_of_truth_parity.py
```

If the check fails because the worktree is intentionally dirty before commit, fix doc issues first, commit, then rerun after push.

## Known current facts

- Repo: `/home/guidingl/projects/hermes-tasks`
- Remote: `https://github.com/CBaen/hermes-tasks`
- Branch: `main`
- GitHub auth from Hermes terminal: use `HOME=/home/guidingl` for `git`/`gh` network operations.
- User/live Brave CDP lane: `http://127.0.0.1:9222`
- Agent-only Brave CDP lane: `http://127.0.0.1:9223`
- Hermes terminal PATH bridge: active via `/home/guidingl/.hermes/profiles/banebook/terminal-path-bridge.sh`; helper command names now resolve in new terminal calls.
- Wardenclyffe helper scripts: `/home/guidingl/bin/wardenclyffe-*`; command names now resolve through the PATH bridge, with absolute paths still safe as fallback.
- Wardenclyffe -> Banebook reverse SSH: verified on 2026-06-11T22:37:43-06:00 after authorizing the Wardenclyffe public key fingerprint `SHA256:Cl5SYra87E5eyA/cy4PWPDAj1aoYm9HmxYLU0hhzmGM` on Banebook.
- Wardenclyffe is the approved primary always-on Uma/Hermes home base as of 2026-06-13T13:01:08-06:00. Fresh Hermes install lives at `/home/guidingl/.hermes/hermes-agent`; the user gateway service `hermes-gateway.service` is enabled/running with linger enabled; `hermes` resolves on Wardenclyffe through `/usr/local/bin/hermes` -> `/home/guidingl/.local/bin/hermes`.
- Banebook remains the daily cockpit/review/browser-control station. Do not blindly sync runtime state between Banebook and Wardenclyffe; sync docs/source/patches through Git or explicit clean patches.
- Wardenclyffe Hermes has no copied Banebook auth/session/browser state. Script-only cron scheduling is verified, and fresh Wardenclyffe Nous Portal login is verified as of 2026-06-13T18:51:06-06:00; `hermes status` shows Provider `Nous Portal`, model `anthropic/claude-opus-4.6`, and managed tools available.
- Wardenclyffe Uma worker-lane rules v1.1 are documented at `capabilities-collaboration-autonomy/recipes/wardenclyffe-uma-worker-lanes-v1.md`, including named lanes for finance clerk, researcher, builder, verifier, client ops, life admin, and browser worker. Wardenclyffe Codex CLI local-only smoke passed and wrote `artifacts/worker-smoke/wardenclyffe-codex-worker-smoke.md`.
- Wardenclyffe Codex CLI is logged in and can support approved local-only worker lanes; Wardenclyffe Hermes provider auth is verified, and a small local-only model-backed smoke test passed using Nous Portal free model `stepfun/step-3.7-flash:free` with artifact `artifacts/model-smoke/wardenclyffe-nous-free-model-smoke-20260613.json`. Broad autonomous dispatch is still off by default; future workers must use the v1.1 dispatch checklist and task-specific approval boundaries.
- Wardenclyffe Hermes WebUI access from Banebook is configured: Wardenclyffe runs enabled user service `hermes-dashboard.service` bound to `127.0.0.1:9119`; Banebook reaches it through SSH tunnel helper `wardenclyffe-hermes-webui` at `http://127.0.0.1:9129`; no `--insecure` network bind is used.
- Wardenclyffe default Hermes model is now `stepfun/step-3.7-flash:free` with provider `nous`, because the Free subscription cannot run the previous default `anthropic/claude-opus-4.6`; default one-shot smoke returned `WARDENCLYFFE_DEFAULT_MODEL_PASS`.
- Messaging/notification: no connected targets yet; Slack manifest prepared at `artifacts/messaging/hermes-slack-manifest.json`; account/platform linking still required before delivery works.
- Banebook<->Wardenclyffe bidirectional SSH is verified as of 2026-06-14T13:09:00-06:00; agents may coordinate through lane-gated SSH/Tailscale workflows, but security/account changes still require explicit approval.
- Samsung S24 appears on Tailscale as `Bane  24Ultra` / `100.75.32.46` / Android, but was offline during 2026-06-14T13:09:00-06:00 inventory. Tailscale presence is not phone control; use an approved phone-side service such as Syncthing/KDE Connect/Termux SSH/ADB before agents can work with it.
