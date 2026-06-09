---
id: guiding-light-capability-adoption
name: Guiding Light Capability Adoption
schema_version: 2.0
level: recipe
maturity: candidate
scope: Banebook Codex and verified peer-agent use of Guiding Light's shared capability framework
currently_true: unknown
verification_level: 1
last_verified: 2026-05-06
evidence_quality: direct
successful_uses: 0
failed_uses: 0
regressions: 0
depends_on:
  - capability-index-routing
  - capability-evidence-and-promotion
used_by: []
tags:
  - Guiding Light
  - capabilities framework
  - shared capabilities
  - peer agents
  - memory safety
  - global state
---

## What it does

Makes active Banebook Codex and verified peer-agent workflows adopt Guiding Light's shared capabilities framework while
respecting privacy, agent differences, and the boundary between reusable
knowledge and sensitive runtime state.

## When to reach for it

Use when Guiding Light starts a serious project, asks about memory, mentions
capabilities, asks to standardize project structure, or wants work to be
portable across Claude, general agents, Codex, and Hermes.

## How to use it

1. Treat capabilities as mandatory infrastructure, not optional notes.
2. For every serious project, create or use a project capability index.
3. Keep the project brief separate from capability cards:
   - `PROJECT-BRIEF.md` says what the project is and why it matters.
   - capabilities say how agents should work on it repeatedly.
4. Preserve project-specific differences. Remotion, Locally Twisted, and Calming Engine may all use the framework differently.
5. Use the neutral system/user root as the shared source on this machine:
   - `/home/guidingl/capabilities`
6. Do not copy these blindly into Hermes, Codex, or any runtime:
   - secrets
   - auth files
   - runtime logs
   - raw session files
   - `.codex-global-state.json`
   - `.codex-global-state.json.bak`
7. Treat global state files as sensitive source material. If they contain valuable information about Guiding Light, extract only safe, durable, non-secret lessons into memory/capabilities after review.
8. When prior context matters, intentionally consult the Codex memory bridge,
   Codex memories, or verified current peer-agent memory surfaces. Do not pretend one
   runtime automatically remembers another runtime's state.
9. After a meaningful session, update:
   - project brief for project-shape changes
   - decisions log for decisions
   - queue/workstream for active tasks
   - capabilities for reusable process
   - memory for durable Guiding Light preferences/context

## What it depends on

- [Capability index routing](capability-index-routing.md)
- [Capability evidence and promotion](capability-evidence-and-promotion.md)

## Failure modes

- Copying global state wholesale leaks or preserves private runtime context.
- Treating Codex memory as automatically available in another runtime creates false confidence.
- Flattening all projects into one template erases useful project-specific differences.
- Promoting agent guesses as Guiding Light preferences distorts memory.

## Evidence notes

Created after direct inspection of the then-current Codex capability root,
OpenClaw memory behavior, and Guiding Light's explicit non-negotiable
requirement on 2026-05-06. Superseded on 2026-05-10 by the neutral
`C:\Users\baenb\capabilities` Windows root and compatibility junctions, then
migrated to the Banebook neutral root `/home/guidingl/capabilities`.
