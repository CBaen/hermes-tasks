---
id: moji-project-capability-layers
name: Moji and Project Capability Layers
schema_version: 2.0
level: principle
maturity: candidate
scope: historical Moji capability routing and active Banebook shared capability layering
currently_true: unknown
verification_level: 1
last_verified: 2026-05-06
evidence_quality: direct
successful_uses: 0
failed_uses: 0
regressions: 0
depends_on:
  - capability-index-routing
used_by: []
tags:
  - moji
  - project capabilities
  - workspace capabilities
  - persistent agent
  - framework
---

## What it does

Defines the difference between Moji-level capabilities and project-level
capabilities so an active runtime can preserve persistent operating guidance
while still letting each serious project grow its own specialized framework.

## When to reach for it

Use this when deciding where a new rule, lesson, failure, workflow, recipe, or agent behavior belongs.

## How to use it

Think in layers:

### 1. Runtime session layer

The currently running model/session.

- Ephemeral.
- Can be restarted, compacted, interrupted, or replaced.
- Should not be trusted as memory by itself.

### 2. Shared operating layer

Files that define persistent operating guidance across sessions:

- `IDENTITY.md`
- `SOUL.md`
- `USER.md`
- `RELATIONSHIP.md`
- `MOJI_OPERATING_SYSTEM.md`
- `MEMORY.md`
- shared capability roots for reusable behavior; hidden runtime folders only
  when they are active adapters or compatibility pointers

Use this layer for patterns that apply across many projects:

- how agents conserve Guiding Light's cognitive battery;
- how agents route through capabilities;
- how agents handle private sources;
- how agents run/avoid swarms;
- how agents verify claims;
- how agents collaborate with Guiding Light.

### 3. Project capability layer

Each serious project should have its own capability index:

- `<project>/capabilities/INDEX.md` for the baseline project root;
- `<project>/capabilities-<scope>/INDEX.md` when a project needs additional
  purpose roots.

Use this layer for project-specific domain knowledge:

- balloon construction grammar;
- Frappe/PlayCanvas handoff for Locally Twisted;
- CGTrader arch benchmark rules;
- project-specific agent lanes;
- client-specific guardrails;
- project-specific failures.

### 4. Upstream/framework layer

External or peer framework sources:

- `/home/guidingl/capabilities/`
- `/home/guidingl/.codex/framework/templates/serious-project/`
- `/home/guidingl/projects/capabilities-framework/`

Use this layer as source material, not automatic truth. Translate useful patterns into shared or project capabilities with evidence.

## Placement rule

Ask: “Who should remember this?”

- If **agents should always behave this way**, put it in the shared operating layer.
- If **only this project needs it**, put it in the project layer.
- If **it is still rough**, put it in `kitchen/`.
- If **it failed and should warn future agents**, put it in `failures/`.
- If **it proves a capability worked or failed**, append compact evidence to `evidence/capability-evidence.jsonl`.

## Promotion rule

A project capability can later be promoted upward if it proves reusable across multiple projects.

Example:

- Project-specific: `event-space-balloon-designer/principles/knowledge-base-first.md`
- Workspace-level reusable candidate: `research-intake-before-agent-swarm`
- Later global/community framework pattern: “source-indexed research before parallel agents.”

## What it depends on

- `capability-index-routing`

## Failure modes

- Putting everything at shared/workspace level turns the root into a junk drawer.
- Putting everything inside one project makes agents repeat lessons in future projects.
- Copying Codex/global files blindly can import stale assumptions or private runtime state.
- Treating the live runtime as the persistent self loses important lessons after restarts.

## Evidence notes

Created after Guiding Light explicitly asked whether there is just one Moji and
identified the need for both persistent shared operating guidance and
per-project capability frameworks.
