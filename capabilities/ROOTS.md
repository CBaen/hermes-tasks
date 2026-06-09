# Capability Root Map

This file explains where capability roots belong on this machine. Capabilities
are organized by purpose and scope, not by which agent happens to read them.

## Root Types

| Scope | Default path | What belongs there |
|---|---|---|
| System/user | `/home/guidingl/capabilities/` | Active shared user, machine, process, and cross-agent operating knowledge consumed by Codex, Claude, and compatibility runtime paths. |
| Codex framework reference | `/home/guidingl/codex-framework/capabilities/` | Historical backup/reference material only. Do not route new agents here as the canonical shared capability root. |
| Legacy alias | `/home/guidingl/projects/codex-framework-backup/capabilities/` | Compatibility symlink to the Codex framework reference copy. Do not route new agents here. |
| Source package | `/home/guidingl/projects/capabilities-framework/` | Templates, schema, starter package, framework tooling, and distribution work. |
| Agency | `/home/guidingl/projects/Built_by_Cameron/capabilities/` when imported | Cross-client Built by Cameron standards, release gates, ERPNext/Frappe agency patterns, and agency-level Failure Recipes. |
| Project | `<project>/capabilities/` | Project-specific reusable operating knowledge, contracts, failures, and evidence. |
| Purpose root | `<project>/capabilities-<scope>/` | A visible sibling root for a domain, subsystem, feature, process, software stack, person, or situation that is evolving enough to deserve its own index. |
| Machine purpose root | `/home/guidingl/capabilities-<scope>/` | Visible machine-level roots for cross-project subjects that are narrower than the shared system root, such as Hermes-specific operating rules. |
| Runtime adapter | `.codex/`, `.claude/`, or other runtime paths | How a specific runtime discovers or executes against shared roots. Adapter paths are not the source of capability truth. |

## Placement Rule

- Put knowledge where its scope is true.
- Do not flatten evolved roots into one folder just to simplify discovery.
- Do not duplicate a shared capability into every agent runtime.
- Link across roots with root labels, related-root notes, backlinks,
  `depends_on`, `used_by`, and registry entries.
- If a dependency or composed root fails, put affected cards on watch or
  probation until revalidated.

## Current Shared And Compatibility Entrypoints

These paths are available on this machine:

- `/home/guidingl/capabilities` - real system/user root
- `/home/guidingl/.codex/capabilities` - compatibility symlink to the real root
- `/home/guidingl/capabilities-hermes` - visible Hermes-specific purpose root
  for Banebook operating rules that should not be hidden under `.hermes`
- Purpose roots such as `capabilities-human-ai-communication` or
  `capabilities-external-access` should be recreated as visible folders under
  `/home/guidingl/` only after a focused migration review.
- OpenClaw adapter paths were retired on 2026-05-14.

They exist so old skills and runtime instructions keep working while the
canonical shared root lives outside agent-owned folders. Do not recreate
`openclaw/workspace/.openclaw/capabilities/` as a repo copy.

## Migration Rule

When moving an existing root:

1. Inventory files first.
2. Classify each card by scope: system/user, agency, project, purpose root,
   runtime adapter, stale/historical, or duplicate.
3. Move shared knowledge to the right visible root.
4. Keep runtime-specific instructions in `adapters/` or the runtime's own config
   docs.
5. Update active routing docs.
6. Leave historical decisions readable with a dated supersession note instead of
   rewriting history.
