---
id: first-capability-root-install
name: First Capability Root Install
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: capability framework
currently_true: unknown
last_verified: 2026-05-07
tags:
  - first install
  - project setup
  - capability root
  - foundation
  - standard project
---

## What it does

Defines the first capability framework folder setup for a project. This is the
baseline root that makes the project discoverable to agents without locking the
project into agent-specific storage.

## When to reach for it

Use this when a persistent project has no capability framework folder yet, or when
starting a new standard project from templates.

## How to use it

1. Confirm the project has its foundational files: `AGENTS.md`, queue, index,
   decisions log, and any needed status or workstream files.
2. Copy the full `capabilities/` folder from the framework source into a visible
   top-level project root when starting fresh:

   ```text
   <project>/capabilities/
   ```

   Existing projects may keep a hidden runtime path only when it is an adapter,
   compatibility pointer, or explicitly preserved legacy install being migrated;
   do not make `.codex`, `.claude`, or retired runtime roots the owner of shared
   project capability truth.
3. Add a short routing section to the project `AGENTS.md` that points to the
   new index and tells agents to open only the needed files.
4. Add a root label to `INDEX.md`: what this root does, what belongs here, what
   does not belong here, and related roots.
5. Keep the first root foundation-light. It should include `INDEX.md`,
   `SCHEMA.md`, layer folders, `kitchen/`, `failures/`, `evidence/`, and
   `registry/`, but it does not need many cards on day one.
6. Add a "Start Here" note in the project index or handoff that says where the
   root lives and that agents should read it on demand.
7. Run the registry validator if tooling is present:

   ```bash
   python /home/guidingl/projects/capabilities-framework/tools/capability_registry.py --root <project>/capabilities --write-registry
   ```

8. Verify a fresh agent can find the project `AGENTS.md`, the capability index,
   and one linked capability file.

## What it depends on

- [Progressive Framework Profiles](progressive-framework-profiles.md)
- [Visible Capability Root Contract](visible-capability-root-contract.md)

## Failure modes

- Installing only an `INDEX.md` without the folder structure makes later growth
  ad hoc.
- Copying every old card from another project imports stale claims.
- Forgetting the `AGENTS.md` route means the folder exists but agents do not
  know to use it.
- Hiding the first root under an agent-specific folder in a new project can make
  the portable package look runtime-specific when it is not.
