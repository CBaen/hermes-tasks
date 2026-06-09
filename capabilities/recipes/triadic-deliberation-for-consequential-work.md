---
id: triadic-deliberation-for-consequential-work
name: Triadic Deliberation For Consequential Work
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: agent-neutral workflow translated for Codex use
currently_true: unknown
last_verified: 2026-05-08
tags:
  - Claude-migration
  - Hermes-local
  - agent-neutral
---

## What it does

Use three independent lenses for consequential ambiguous work, then map convergence/disagreement and recommend a path with evidence.

## When to use it

Use when the current task matches the title/summary and the nearest project capability root does not provide a more specific local version. For project/client work, read the project entrypoint and nearest capability index first.

## How to use it

1. Confirm the task is in scope and check project-specific rules first.
2. Gather direct evidence from current files, docs, tests, live URL, or source material.
3. Keep the first pass separated across three lenses, with at least one
   critical/adversarial lens.
4. When subagent tooling is available, send first-pass findings back to the
   lenses for a second-pass response before final synthesis. If subagents are
   unavailable, label the result as a solo structured review instead of a real
   multi-agent triad.
5. Map agreements, disagreements, changed views, and evidence strength before
   recommending a path.
6. Write durable notes/artifacts when the workflow produces decisions,
   research, reviews, or handoff state.
7. Report outcome with evidence and any blockers or unresolved risks.

## Adapter notes

- This is a Codex/global translation of Claude-era source material, intended for any capable agent.
- Do not copy Claude runtime assumptions, agent names, auth/session material, or private transcripts.
- If a Hermes local or project-specific card with the same id exists, treat it as a peer adapter, not a higher authority.

## Evidence

- Source skill/material: `C:/Users/baenb/.claude/skills/triadic-work/SKILL.md`.
- Historical translation queue (retired OpenClaw source): `C:/Users/baenb/.openclaw/workspace/research/claude-to-openclaw-skill-migration/CLAUDE-SKILL-TRANSLATION-QUEUE-2026-05-08.md`.
