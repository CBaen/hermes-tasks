---
id: reliable-subagent-execution
name: Reliable Subagent Execution
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: Codex and peer-agent delegated work
currently_true: unknown
last_verified: 2026-05-10
tags:
  - subagents
  - reliability
  - swarms
  - orchestration
  - failure handling
---

## Date / Check / Confidence Header Contract

Every user-visible assistant reply and every delegated-agent handoff/report must start with the compact evidence header:

`D:YYYY-MM-DD | Check:<source/date> | Confidence:<label>`

Rules:
- Use the current runtime date in the user's timezone when available.
- `Check` names the freshest basis actually used: user msg, session_status, local runtime, local docs/source, official docs, web/source check, test/build/lint, artifact path, or `[NOT CHECKED]`.
- `Confidence` is evidence language, not reassurance. Preferred labels: `[VERIFIED]`, `[CURRENT]`, `[MULTI-SOURCE]`, `[LOCAL-PROOF]`, `[CONFIDENT]`, `[UNVERIFIED]`, `[STALE-RISK]`, `[NO EVIDENCE]`, `[BLOCKED]`.
- For current technology, agent orchestration, customer/company-impacting work, architecture, deployment, payments, checkout, email, data import/export, or external claims: check current docs/source/runtime/web before presenting confidence.
- If no current check was performed, say so in `Check` and lower confidence; do not imply freshness.
- Exception: platform-mandated silent replies such as exact `NO_REPLY` / `HEARTBEAT_OK` must remain exact.

## What it does

Turns failed broad fanout into a safer execution pattern: fewer agents, narrower lanes, required artifacts, status checks on demand, and manual fallback when the swarm is unstable.

## When to reach for it

Use before launching multiple subagents, delegating research/review lanes, or building command-center/agency-agent workflows.

## How to use it

1. Prefer one to three scoped agents over broad swarms.
2. Use `context: isolated` by default; use forked context only when the current transcript is necessary.
3. Give each agent, in the actual spawned-agent task prompt:
   - exact source paths;
   - allowed tools/actions;
   - explicit no-export/private boundaries;
   - required output file;
   - required headings;
   - required compact header: `D:YYYY-MM-DD | Check:<source/date> | Confidence:<label>`;
   - current-source rule for current technology/company-impacting claims;
   - no-evidence labels for missing artifacts/checks;
   - stop rule and partial-output rule.
4. Parent accountability: Moji/parent owns the quality of delegation and must reject missing-header/missing-evidence reports. Do not blame spawned agents for contracts that were not injected into their prompts.
5. Require the same compact header in every handoff/report artifact and user-visible summary; if current-source checks were not performed, the header must say `[NOT CHECKED]` / `[STALE-RISK]` / `[NO EVIDENCE]` as appropriate.
6. Use durable output files as the source of truth, not completion summaries.
7. Do not poll subagent lists in loops. Check status only on demand or when intervention is needed.
8. If the runtime reports lost context, long-running orphan sessions, noisy output, or argument/tool errors:
   - stop spawning replacements;
   - recover logs/output if useful;
   - document the failure pattern;
   - switch to manual/fewer-agent work.
9. Treat subagent output as evidence, not proof.

## What it depends on

- [Named Agent Orchestration](named-agent-orchestration.md)
- [No Bare Claims](../principles/no-bare-claims.md)

## Failure modes

- Recreating loose swarm failures with more agents.
- Trusting completion events without reading files.
- Losing useful partial work because output paths were not required.
- Letting agent-management overhead exceed the value of delegation.
