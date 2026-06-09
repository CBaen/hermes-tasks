---
id: capability-index-routing
name: Capability index routing
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: systemwide capability routing
currently_true: unknown
last_verified: 2026-05-02
tags: [capability-routing, indexes, roots, agents]
---

## What it does

Teaches agents how to find and use capability indexes at the system/user,
agency, project, purpose-root, and workstream levels without treating runtime
folders as owners.

## When to reach for it

Use this when starting meaningful work in a project, setting up a new project,
or translating older runtime-specific capability knowledge into shared roots.

## How to use it

1. Start from the current working directory.
2. Read the nearest `AGENTS.md` that applies.
3. Look for a capability index in this order:
   - visible project roots such as `<current project>/capabilities/INDEX.md`
     or `<current project>/capabilities-<scope>/INDEX.md`
   - visible purpose roots named for the reason they exist, such as
     `<current project>/capabilities-checkout/INDEX.md`
   - The nearest parent workspace capability index referenced by `AGENTS.md`
   - `/home/guidingl/capabilities/INDEX.md`
   - runtime compatibility pointers such as `.codex/capabilities/INDEX.md`
     only when an active adapter explicitly routes there
4. Skim the index before substantial project work.
5. Open only the capability files needed for the current task.
6. If the project is missing any capability root, treat that as a setup gap for persistent projects.
7. If the project has no capability framework folder, use
   [First Capability Root Install](first-capability-root-install.md).
8. If the project needs another capability framework folder, use
   [Additional Capability Root Install](additional-capability-root-install.md).
9. Keep indexes hub/spoke for token protection and label each root's purpose,
   contents, exclusions, and related roots.
10. Use foundation capability cards by default. They route work; they are not proof.
11. Upgrade to governed, composition, or cascade tracking only when evidence,
   risk, repeated use, or dependency impact earns it.
12. If a useful process emerges, add it to `kitchen/` first unless it is already verified enough to become a foundation candidate.
13. Put meals in the consuming capability root that references and uses the
   ingredient chain.
14. If a linked dependency fails, downgrade or watch consuming capabilities.
   Repaired chains enter probation and need three evidence-backed successful
   uses before greenlit trust returns.
15. Before changing maturity, `currently_true`, confidence, promotion state, or watch status, record evidence, date, result, confidence, and rollback or revalidation.

## What it depends on

None.

## Adapter notes

### Codex

Codex should route through `AGENTS.md` and on-demand reads. Do not copy Claude
`@import` behavior, and do not treat `.codex` as the owner of shared capability
truth.

### Claude

Claude may use its own import behavior, but it should import visible shared
roots such as `capabilities/INDEX.md` or the neutral user root. Preserve the
Claude workspace and translate only the useful operating idea.
