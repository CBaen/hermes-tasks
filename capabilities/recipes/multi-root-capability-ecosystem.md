---
id: multi-root-capability-ecosystem
name: Multi-Root Capability Ecosystem
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: Codex, verified peer agents, and Guiding Light projects
currently_true: unknown
last_verified: 2026-05-07
tags:
  - capabilities
  - multi-root
  - routing
  - agents
  - composition
  - visible roots
---

## What it does

Treats Guiding Light's work as a connected ecosystem of capability roots rather
than one central folder. Multiple capability frameworks can coexist by purpose:
system/user, agency, project, feature, domain, subsystem, process, software,
situation, person/user, runtime adapter, client, or workstream.

## When to reach for it

Use when a project has more than one meaningful context source, when Codex,
peer-agent, or Claude-era material all matter as peer evidence, when a
client/project needs its own domain knowledge, or when a situation,
person/user, process, or workstream deserves a specialized capability root.

## How to use it

1. Start from the named project/workspace path.
2. Read the nearest entrypoint: `AGENTS.md`, `PROJECT-MOJI.md`, `PROJECT-BRIEF.md`, or equivalent.
3. Build a small root map instead of choosing only one folder:
   - source framework root, if relevant;
   - neutral system/user root;
   - workspace/Moji root when it is a shared root rather than raw runtime state;
   - project root;
   - visible scoped roots such as `capabilities-frappe/`,
     `capabilities-content/`, `capabilities-jeff/`, or
     `capabilities-agent-adapter/`;
   - runtime adapter pointers such as `.codex/capabilities/`;
   - external/peer roots only when deliberately consulted.
4. For each root, identify:
   - purpose;
   - what belongs there;
   - what does not belong there;
   - related roots/backlinks;
   - privacy/source boundary;
   - whether it is foundation/governed/composition/cascade-heavy.
5. Open only the root indexes and task-relevant cards. Do not eagerly load everything.
6. Place new capabilities where the future agent will naturally look:
   - shared user/process behavior -> neutral system/user root;
   - Moji behavior -> visible shared Moji root, not raw runtime state;
   - project/domain knowledge -> project visible root;
   - agent-specific adapter behavior -> visible adapter root or runtime
     adapter pointer;
   - shared public framework rule -> source package/root after sanitization;
   - rough idea -> nearest `kitchen/`.
7. For composed capabilities, put the meal with the consuming root and link dependencies across roots.
8. If a dependency fails, downgrade or watch the consuming capability until revalidated.

## What it depends on

- [Capability Index Routing](capability-index-routing.md)
- [Visible Capability Root Contract](visible-capability-root-contract.md)
- [Cross-Root Meal Placement And Trust](cross-root-meal-placement-and-trust.md)
- [Progressive Framework Profiles](progressive-framework-profiles.md)

## Failure modes

- One giant root becomes a junk drawer.
- Hidden adapter roots hide reusable project knowledge from other agents.
- Visible roots multiply without labels/backlinks and become silos.
- Meals pretend dependencies are local when they actually inherit risk from another root.
- Private/client/agent runtime material leaks upward into a shared/public root.
