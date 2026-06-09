---
id: mandatory-main-agent-witness-protocol
name: Mandatory Main-Agent Witness Protocol
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: machine-wide high-risk Codex work
currently_true: unknown
last_verified: 2026-05-22
tags:
  - witness
  - subagents
  - code-review
  - architecture
  - research
  - verification
---

# Mandatory Main-Agent Witness Protocol

## What It Does

Requires a main Codex agent to use independent witness lanes for risky work
before deciding, while acting, and before claiming completion.

The purpose is to prevent one confident agent misunderstanding from becoming
architecture, code, research, or review output that Guiding Light cannot easily
evaluate at engineering depth.

## Mandatory Triggers

Use this protocol for:

- major architecture planning or architecture builds;
- multi-file or cross-domain implementation;
- bug review, root-cause analysis, and bug fixes;
- external internet research or current-source claims;
- code review;
- security, payments, auth, deployment, data, client, or income-critical work;
- any task where Guiding Light may approve technical work they cannot fully
  inspect.

Tiny reversible edits, direct status checks, and simple commands may skip the
protocol. If unsure, use the light version.

## Roles

- Main agent: communicates with Guiding Light, owns edits, integrates evidence,
  verifies outcomes, and cleans up sessions.
- Intent witness: checks whether the task interpretation matches Guiding
  Light's actual request and names likely misunderstanding points.
- Technical witness: checks architecture, code path, failure path, test plan,
  and review risk.
- Research/reality witness: required for external sources; separates source
  facts from interpretation and checks whether outside claims apply locally.

Witnesses advise and challenge. They do not replace main-agent accountability.

For launch, staging, provider, payment, auth, client-data, or income-critical
work, witnesses must own artifacts that can block the next step. Advice-only
helpers are not release control. Required artifacts can include provider-state
proof, sanitized payload validation, executable gate output, patch review,
rollback proof, docs parity, or an explicit blocker report.

Witness agents use the main agent's same model. Do not downgrade, upgrade, or
switch models for this process. If the runtime inherits the main model when no
model is specified, leave the model unspecified.

Witness reasoning effort is limited to `medium` or `high`. Use `medium` by
default and `high` for complex architecture, bug analysis, external research,
security, payments, deployment, code review, or client/income-critical work.
Never use `xhigh` or extra-high reasoning for witness agents.

## Workflow

1. Trigger gate: state why the witness protocol applies or why it is safely
   skipped.
2. Witness brief: write the goal, current understanding, risk areas, sources,
   stop conditions, and witness lanes.
3. Witness work: run narrow, artifact-producing witness lanes when tools allow.
4. Synthesis: compare agreement, disagreement, missing evidence, and source
   conflicts before implementation or final recommendation.
5. Apply: main agent performs code edits or final synthesis.
6. Review: account for each witness before finalizing.
7. Verify: use tests, builds, browser/runtime checks, source checks, or
   citations.
8. Cleanup: close spawned agents and record cleanup of helper processes or
   sessions.

Release-process stop rule: after one provider/bootstrap/deploy failure, require
failure classification and a written guard before retry. After two related
failures, all provider mutation stops until a fresh artifact-owned release plan
is approved. If Guiding Light says stop, execution stops immediately; only
read-only forensics may continue until release execution is explicitly
reopened.

## State Packet

Use the `witnessed-work` skill template:

`/home/guidingl/codex-framework/skills/witnessed-work/templates/witness-state-packet.md`

If a witness compacts, dies, or times out, rehydrate the replacement from the
packet. If the packet is missing, reconstruct it before making risky claims.

## Related Skills And Capabilities

Start from `/home/guidingl/capabilities/INDEX.md`. The index exists so agents
do not read the whole capability library. Open only the indexed recipe,
principle, or skill that is directly relevant to the active witness task.

- `/home/guidingl/codex-framework/skills/witnessed-work/templates/witness-state-packet.md`
- `/home/guidingl/codex-framework/skills/witnessed-work/SKILL.md`
- `/home/guidingl/capabilities/principles/no-bare-claims.md`
- `/home/guidingl/capabilities/recipes/named-agent-orchestration.md`
- `/home/guidingl/capabilities/recipes/reliable-subagent-execution.md`
- `/home/guidingl/capabilities/recipes/triadic-construction-with-independent-review.md`
- `/home/guidingl/capabilities/recipes/triadic-deliberation-for-consequential-work.md`
