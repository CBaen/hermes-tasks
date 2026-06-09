---
id: codebase-verified-docs-update
name: Codebase-Verified Docs Update
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: documentation updates that must match current project/source truth
currently_true: unknown
last_verified: 2026-05-07
tags:
  - documentation
  - verification
  - codebase
  - GSD-migration
---

## What it does

Updates or checks project documentation against current source truth instead of memory, aspiration, or stale comments.

Adapted from Claude GSD's `gsd-docs-update` pattern.

## When to reach for it

Use when writing or refreshing:

- README / architecture docs;
- API/route/component docs;
- setup/deployment docs;
- project handoff docs;
- capability/project indexes;
- client-facing technical summaries that mention current behavior.

## How to use it

1. Identify the docs and claim types being updated.
2. Decide mode:
   - **verify-only**: inspect existing docs and report mismatches;
   - **update**: edit docs after verification;
   - **regenerate**: only with explicit preservation checks.
3. For each factual claim, inspect current source/tool output:
   - paths exist;
   - commands/scripts exist;
   - endpoints/components/config names match;
   - versions/dependencies are current;
   - behavior is observed or tested when claimed.
4. Preserve hand-written context unless stale or explicitly replaced.
5. Write verification notes: what was checked, what changed, what remains uncertain.
6. Do not infer optional flags/settings are active just because docs mention them.

## What it depends on

- [No Bare Claims](../principles/no-bare-claims.md)
- [Current truth needs evidence](../principles/current-truth-needs-evidence.md)
- [Capped Review Fix Loop](capped-review-fix-loop.md)

## Failure modes

- Hallucinated paths, endpoints, commands, or signatures.
- Updating docs from memory without checking files.
- Overwriting useful human-written documentation without preservation review.
- Treating documented optional behavior as active configuration.

## Evidence

- `C:/Users/baenb/.claude/skills/gsd-docs-update/SKILL.md:12-13` says docs are written by agents that explore the codebase directly, avoiding hallucinated paths/endpoints/stale signatures.
- `C:/Users/baenb/.claude/skills/gsd-docs-update/SKILL.md:15-25` defines explicit flag handling and verify-only behavior.
- `research/claude-to-openclaw-skill-migration/GSD-SKILL-FAMILY-AUDIT-2026-05-07.md` identifies verified docs as migration-worthy.
