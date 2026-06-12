# Hermes Tasks Agent Infrastructure Capabilities

## Root Label

- Purpose: Reusable capabilities for Uma/Hermes infrastructure on Banebook: profile files, SOUL routing, project docs, launcher setup, background jobs, workspace conventions, timestamp parity, and validation.
- Belongs here: Main repo/project maps, Hermes profile/runtime boundaries, SOUL file pointers, launcher configuration, scheduled job patterns, local artifact conventions, source-of-truth rules, and verification commands.
- Does not belong here: Secrets, `.env` contents, auth stores, raw browser state, OAuth tokens, raw logs, or unrelated project implementation details.
- Related roots:
  - `capabilities/` - baseline project operating capabilities
  - `capabilities-connections-control/` - connection/control capabilities enabled by infrastructure
  - `capabilities-collaboration-autonomy/` - collaboration rules enabled by infrastructure
  - `/home/guidingl/.hermes/profiles/banebook` - active Hermes runtime profile, reference only unless explicitly maintaining profile files

## How To Use This Root

1. Start here when the task is about Uma/Hermes' own operating setup on Banebook.
2. Keep visible source-of-truth project docs in this repo; keep runtime config in the active Hermes profile.
3. Link to runtime/profile files by path when useful, but do not copy secrets or auth/session state.
4. Prefer reversible local launcher/config changes and verify them with real commands.
5. Update project index/status/decisions when infrastructure changes affect future sessions.
6. Run the source-of-truth parity check after state-bearing doc changes.

## Principles

- [Source Of Truth Timestamp Parity](principles/source-of-truth-timestamp-parity.md) - timestamp and parity rules for AI-readable current-state docs.

## Recipes

- Add setup, repair, and validation workflows here.

## Ingredients

- [Hermes Profile And SOUL Map](ingredients/hermes-profile-and-soul-map.md) - verified routing between active Hermes profile, SOUL files, visible project repo, and Uma notes.
- [Hermes Terminal PATH Bridge](ingredients/hermes-terminal-path-bridge.md) - verified profile-local shell init that exposes `/home/guidingl/.local/bin` and `/home/guidingl/bin` helpers to Hermes terminal calls.

## Meals

- Add composed operating modes here when multiple infrastructure capabilities work together.

## Kitchen

- Use `kitchen/` for rough infrastructure notes.

## Failures

- Use `failures/` for setup mistakes and rollback notes.

## Evidence And Registry

- `evidence/` - compact evidence events for verified infrastructure changes.
- `registry/` - generated or curated indexes for this root when needed.
