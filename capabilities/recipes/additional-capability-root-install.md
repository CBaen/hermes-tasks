---
id: additional-capability-root-install
name: Additional Capability Root Install
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: capability framework
currently_true: unknown
last_verified: 2026-05-07
tags:
  - additional root
  - multi-root
  - capability root
  - workstream
  - agent adapter
---

## What it does

Defines how to add another capability framework folder to a project that already
has one. Additional roots are allowed when they make discovery clearer.

## When to reach for it

Use this when adding a visible capability root for a major feature lane, domain
area, reusable subsystem, process, software system, situation, person/business
subject, or runtime adapter.

## How to use it

1. Confirm there is already a project baseline capability root.
2. Name why the new root exists in one sentence. Prefer visible project-root
   names for new roots, such as `capabilities-checkout/`,
   `capabilities-storefront/`, `capabilities-finance/`, or
   `capabilities-jeff/`.
3. Use hidden runtime roots, such as `.codex/capabilities/`, only when the root
   is specifically an adapter for that runtime, a compatibility pointer, or an
   explicitly preserved legacy install being migrated. Retired OpenClaw roots
   must not receive new work.
4. Give the root its own `INDEX.md` with a root label: what it does, what
   belongs here, what does not belong here, and related roots.
5. Copy the full framework structure only when that root is expected to grow.
6. Link to the new root from the nearest parent index and from the baseline
   project capability index.
7. Add backlinks from the new root to the parent project root and any peer roots
   it relies on.
8. Keep each root hub/spoke: local `INDEX.md` routes to files or folder indexes;
   it should not become a full manual.
9. Record cross-root dependencies in `depends_on`, `used_by`, evidence notes, or
   normal Markdown links.

## What it depends on

- [First Capability Root Install](first-capability-root-install.md)
- [Visible Capability Root Contract](visible-capability-root-contract.md)
- [Hub/Spoke Capability Indexing](hub-spoke-capability-indexing.md)

## Failure modes

- Adding roots because of folder preference instead of discoverability creates
  fragmentation.
- Hiding a root without parent links makes it effectively invisible.
- Nesting all roots under one parent folder hides the sibling roots agents need
  to notice quickly.
- Treating roots as silos prevents useful ingredients from composing across
  projects or domains.
