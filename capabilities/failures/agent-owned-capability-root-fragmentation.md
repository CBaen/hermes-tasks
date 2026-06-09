---
name: Agent-owned capability root fragmentation
type: failure
failure_kind: process_failure
schema_version: 0.1
date_discovered: 2026-05-10
last_updated: 2026-05-10
status: guarded
scope: system
owner_context: C:\Users\baenb shared capability framework
related_capabilities:
  - ../ROOTS.md
  - ../recipes/visible-capability-root-contract.md
  - ../recipes/additional-capability-root-install.md
  - ../recipes/cross-project-capability-composition.md
related_failures: []
tags:
  - capabilities
  - agent-agnostic
  - parity
  - codex
  - retired-runtime
  - claude
---

# Failure Recipe: Agent-owned capability root fragmentation

## Symptom

Capabilities are described as owned by a runtime folder such as `.codex`,
`.openclaw`, or `.claude`, causing each agent to grow a separate framework copy.

## Trigger conditions

- A new capability root is installed under an agent runtime folder because that
  is the current tool in use.
- A plan says "global Codex capabilities" or similar when the knowledge should
  be shared across agents.
- Runtime adapter needs are confused with the capability source of truth.
- Path cleanup proposals blindly merge all roots or blindly duplicate one root
  into every agent workspace.

## Known instances

| Date | Project | Surface | Action being taken | Bad outcome | Evidence | Guard state | Status |
|---|---|---|---|---|---|---|---|
| 2026-05-10 | Systemwide capability framework | `C:\Users\baenb\.codex\capabilities` planning | Redesigning shared capabilities for Codex, OpenClaw, Claude, agency, and LT | Initial plan kept systemwide root under `.codex`, which made Codex the owner by path and would split parity across agents | User rejected the plan and clarified capabilities are agent-agnostic shared knowledge | added neutral `C:\Users\baenb\capabilities` root plus runtime junctions/adapters | guarded |

## Root pattern

The agent confuses the folder it can currently access with the owner of the
knowledge. That produces separate agent-owned stores instead of a shared
capability graph.

## Why it seemed reasonable at the time

Existing tools and skills referenced `.codex\capabilities`, and some old docs
used "Codex capabilities" as shorthand. Keeping that path looked compatible,
but it encoded ownership in the filesystem.

## Detection signals

- Phrases like "Global Codex capabilities" for shared knowledge.
- Canonical roots under `.codex`, `.openclaw`, or `.claude`.
- Multiple agent folders containing duplicated framework cards.
- Plans that "sync" agents by copying whole roots instead of linking to shared
  purpose roots.
- Missing root labels explaining what a capability root owns.

## Required guard

Capability roots are organized by purpose and scope, not by agent. Runtime
folders may contain adapters or compatibility pointers only. Shared roots must
be visible and agent-agnostic, such as `C:\Users\baenb\capabilities`,
`<agency>\capabilities`, `<project>\capabilities`, or
`<project>\capabilities-<scope>`.

## Recovery recipe

1. Stop treating the agent runtime path as the canonical root.
2. Create or identify the neutral purpose root.
3. Inventory existing runtime/project capability files.
4. Move shared knowledge to the purpose root.
5. Keep runtime-specific behavior in adapters.
6. Add compatibility pointers only when old tools need legacy paths.
7. Update active routing docs and leave historical notes with supersession.
8. Validate with registry generation and stale-path searches.

## What not to do

- Do not maintain separate Codex, OpenClaw, and Claude copies of the same shared
  capability truth.
- Do not delete protected runtime folders without an inventory.
- Do not smash unrelated purpose roots together just to avoid multiple folders.
- Do not call compatibility junctions the canonical source.

## Cross-links

- Related capability: `../ROOTS.md`
- Related recipe: `../recipes/visible-capability-root-contract.md`
- Related recipe: `../recipes/additional-capability-root-install.md`
- Related adapter note: `../adapters/CODEX.md`
- Related adapter note: `../adapters/CLAUDE.md`

## Evidence quality

Verified by filesystem checks on 2026-05-10 and OpenClaw retirement checks on
2026-05-14: the neutral root now lives at `C:\Users\baenb\capabilities`, Codex
keeps only compatibility routing, and OpenClaw adapter/source paths were
removed. Future project/agency roots still need their own scope checks.
