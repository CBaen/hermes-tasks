---
id: wardenclyffe-codex-hermes-auth-boundary
name: Wardenclyffe Codex Hermes Auth Boundary
schema_version: 2.1
profile: foundation
level: ingredient
maturity: maintained
scope: Wardenclyffe agent-runtime authentication split for Codex CLI and Hermes Agent
currently_true: verified
last_verified: 2026-06-13
tags:
  - wardenclyffe
  - codex
  - hermes
  - auth
  - gateway
  - worker-lanes
---

# Wardenclyffe Codex Hermes Auth Boundary

## What it helps with

Use this when deciding whether Wardenclyffe can run Codex workers, Hermes
workers, scheduled jobs, or Kanban dispatchers.

## Verified state

Verified on 2026-06-13 from Banebook over `wardenclyffe-ssh`:

- Wardenclyffe Codex CLI is installed and `codex login status` reports
  `Logged in using ChatGPT`.
- Wardenclyffe Hermes Agent is installed fresh under
  `/home/guidingl/.hermes/hermes-agent`.
- Wardenclyffe Hermes user gateway service is enabled/running with linger.
- `/usr/local/bin/hermes` resolves to `/home/guidingl/.local/bin/hermes` for
  non-interactive SSH.
- Wardenclyffe Hermes script-only/no-agent scheduled smoke fired successfully.
- Wardenclyffe Hermes provider auth is now configured through Nous Portal; free-model smoke passed with `stepfun/step-3.7-flash:free`.

## Practical meaning

- Codex CLI can be used for approved local-only worker smoke tests and likely
  local coding/review lanes.
- Hermes can run gateway/scheduler/cron infrastructure and script-only jobs.
- Hermes LLM-backed workers may run only within scoped, approved worker lanes using the verified Nous/free-model path or a separately approved provider/model.
- Codex login and Hermes provider login are separate. Do not assume one
  satisfies the other.

## Safe login rule

Do not copy Banebook auth, sessions, browser state, OAuth files, API keys,
`.env`, logs, private keys, wallet keys, or password-manager exports to
Wardenclyffe.

Provider login for Hermes must be fresh and user-mediated. If the provider is
not selected clearly, stop and ask the user to choose the provider instead of
starting an ambiguous OAuth/account flow.

## Useful checks

Use live checks before claiming readiness:

```bash
wardenclyffe-ssh 'codex login status'
wardenclyffe-ssh 'hermes status'
wardenclyffe-ssh 'hermes gateway status'
wardenclyffe-ssh 'hermes cron list'
```

## Stop conditions

Stop before:

- copying credentials or runtime auth files;
- reading secrets/logs/cookies/browser profiles;
- using an unclear provider choice;
- letting both Codex and Hermes workers mutate the same files without an
  explicit lane contract;
- claiming broad autonomous worker readiness without a concrete lane/card, evidence artifact, and approval boundary.

## 2026-06-13 free-model smoke note

- Wardenclyffe Nous Portal auth is verified, but the configured default model
  `anthropic/claude-opus-4.6` required paid credits on the Free subscription.
- Hermes model helpers reported selectable free models:
  `stepfun/step-3.7-flash:free` and `nvidia/nemotron-3-ultra:free`.
- A local-only one-shot smoke with explicit `--provider nous --model
  stepfun/step-3.7-flash:free` returned PASS JSON and was saved at
  `artifacts/model-smoke/wardenclyffe-nous-free-model-smoke-20260613.json`.
- Until credits/plan/default model are intentionally changed, use explicit free
  model overrides for smoke tests and low-risk worker proofs.
