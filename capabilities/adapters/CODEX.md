# Codex Adapter

Codex uses shared capability roots. It does not own them.

## Canonical Roots

- System/user root: `/home/guidingl/capabilities/INDEX.md`
- Source package: `/home/guidingl/projects/capabilities-framework/`
- Project roots: `<project>/capabilities/INDEX.md`
- Purpose roots: `<project>/capabilities-<scope>/INDEX.md`

`/home/guidingl/.codex/capabilities` is a compatibility symlink to
`/home/guidingl/capabilities` on this machine. Keep hardcoded legacy skill paths
working through that symlink, but do not describe `.codex` as the canonical
owner. OpenClaw paths are retired and must not be used as active defaults.

## How Codex Should Use Capabilities

1. Read the nearest applicable `AGENTS.md`.
2. Prefer the most specific visible root for the task.
3. Check `failures/` before recipes when a known-risk surface, approval gate,
   verifier, public chrome, or familiar failure pattern is involved.
4. Open only the specific files needed.
5. Treat capabilities as operating knowledge, not automatic proof.
6. Keep project facts in project roots, agency facts in agency roots, and
   system/user facts in the system/user root.

## What Belongs In Codex Runtime Folders

- Codex config, sessions, logs, caches, skills, plugin runtime state, and memory
  files.
- Small adapter notes explaining how Codex finds shared roots.

Do not put canonical shared capability truth under `.codex` just because Codex
is the current agent.
