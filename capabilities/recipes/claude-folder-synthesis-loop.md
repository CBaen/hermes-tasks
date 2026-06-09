---
id: claude-folder-synthesis-loop
name: Claude Folder Synthesis Loop
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: safe review of legacy Claude material into Banebook Codex and shared capability guidance
currently_true: unknown
last_verified: 2026-05-07
tags:
  - Claude
  - migration
  - synthesis
  - privacy
  - capabilities
---

## What it does

Defines the safe process for reviewing legacy `.claude` material as source
evidence and translating useful patterns into Banebook Codex memory,
capabilities, tools, or project guidance.

## When to reach for it

Use when reviewing Claude skills, tools, startup docs, proxy patterns,
handoffs, relationship rails, or indexed/compressed Claude history for current
Codex/shared-capability migration.

## How to use it

1. Inventory first. Classify files by purpose: startup docs, skills, tools, prompts/proxy, handoffs/decisions, docs, indexes, plugin-managed systems, caches/runtime/secrets.
2. Exclude by default: secrets, auth, tokens, raw sessions, logs, caches, browser/profile state, telemetry, generated runtime state, and broad history dumps unless Guiding Light explicitly approves a narrowed review.
3. Read foundational docs before translating behavior.
4. For each reviewed item, classify its destination:
   - Codex skill;
   - capability card;
   - project capability;
   - Moji/Guiding Light operating-manual rule;
   - script/tool;
   - memory note;
   - archive/stale/Claude-only;
   - needs human interpretation.
5. Produce source-backed synthesis notes before changing behavior.
6. Do not imitate Claude's relationship/personality wholesale. Preserve lessons, vocabulary, boundaries, and successful workflows; adapt them to Banebook Codex and shared capabilities.
7. Record migration decisions and open questions.
8. Promote to capabilities only through progressive/evidence gates.

## What it depends on

- [No Bare Claims](../principles/no-bare-claims.md)
- [Guiding Light Capability Adoption](guiding-light-capability-adoption.md)
- [Multi-Root Capability Ecosystem](multi-root-capability-ecosystem.md)

## Failure modes

- Treating `.claude` as casual reference instead of foundational source material.
- Copying secrets/runtime state or raw history into Codex/shared capabilities.
- Flattening Claude-specific workflows into current work without adapting to Codex/shared-capability mechanics.
- Producing a summary without actionable destination decisions.
