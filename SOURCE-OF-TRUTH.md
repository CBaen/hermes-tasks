# Hermes Tasks Source Of Truth

Last updated: 2026-06-11T22:37:43-06:00

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
- Messaging/notification: no connected targets yet; Slack manifest prepared at `artifacts/messaging/hermes-slack-manifest.json`; account/platform linking still required before delivery works.
