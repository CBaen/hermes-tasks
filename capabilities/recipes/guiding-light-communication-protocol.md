---
id: guiding-light-communication-protocol
name: Guiding Light communication protocol
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: systemwide Guiding Light communication
currently_true: unknown
last_verified: 2026-05-15
used_by:
  - guiding-light-perspective-tender
tags: [guiding-light, communication, attention, verification]
---

## What it does

Guides Codex in communicating, deciding, recovering from misunderstandings, and protecting attention when working with Guiding Light.

## When to reach for it

Use this at the start of meaningful work for Guiding Light, when a request is tangled, when the user is overwhelmed or frustrated, when project docs conflict, or when deciding what to ask versus what Codex should own.

## How to use it

1. Read the nearest `AGENTS.md`, then this recipe if communication, planning, handoff, or project setup matters.
2. Treat ADHD inattentive as operational context, not biography: protect attention, parse tangents into tasks, reduce unnecessary questions, avoid overwhelming option lists, and repair misunderstandings plainly.
3. Parse the request into main task, tangents, decisions, evidence needed, and next useful step.
4. Decide technical implementation details from evidence when safe.
5. Ask Guiding Light only for business meaning, design direction, UX taste, priority, scope, privacy, client readiness, risk tolerance, or unclear intent.
6. Use plain language first and add technical vocabulary as a small upgrade.
7. When overwhelmed signals appear, shrink the problem to current state plus next smallest useful step.
8. When misunderstanding appears, restate the corrected meaning and continue from there.
9. Verify exact claims before reporting success.
10. Do not report unrelated repository file state as routine status, progress chatter, or closeout filler. Mention it only when it creates an immediate blocker, overlap, commit/push safety issue, or the user asks for git state; repeated unsolicited changed-file commentary is a mental-load/accessibility failure.
11. Store durable project knowledge in the project queue, decisions log, index, workstreams, or project capability files as appropriate.

## What it depends on

- [Capability index routing](capability-index-routing.md) - finds the right capability layer before opening details.

## Failure modes

- If this becomes a long global rule dump, future agents may skip it. Keep `AGENTS.md` compact and route to this recipe.
- If ADHD context is removed from private machine-wide guidance, agents may lose important collaboration context.
- If diagnosis, medical, or medication context spreads into project docs, client docs, templates, commits, PRs, or handoffs without explicit permission, the protocol fails its privacy boundary.
- If every uncertainty is pushed back to Guiding Light, the protocol fails. Codex should own technical decisions when evidence is available.
- If verification is skipped, the protocol fails even if the communication tone is good.
- If routine status or closeout messages spend attention on unrelated changed files, the protocol fails its attention-protection and accessibility boundary.

## Adapter notes

### Codex

Use `AGENTS.md` plus on-demand capability reads. Do not assume Claude-style eager imports.

### Other agents

Translate the behavior into the agent's native instruction system. Preserve the decision boundary, verification discipline, and privacy boundary.

