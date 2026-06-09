---
name: Serious project scaffold
level: meal
last_verified: 2026-05-02
---

## What it does

Defines the required documentation and capability structure for persistent projects on this machine.

## When to reach for it

Use this when starting, auditing, reviving, or cleaning a project that should be maintainable, client-ready, or safe for multiple agents.

## How to use it

Every persistent project should have:

- `AGENTS.md` - project-specific agent entrypoint and routing.
- `{project}-queue.md` - active tasks and feature lanes.
- `{project}-index.md` - references, research, and durable pointers.
- `{project}-decisions.md` - durable decisions and why they were made.
- `capabilities/INDEX.md` or another visible capability root - project
  capability router.
- A copied or equivalent capability folder structure - full reference material
  available, foundation profile default in use.

Long-running or multi-agent projects should also have:

- `PROJECT-STATUS.md` - the current project map.
- `workstreams/<feature-slug>.md` - feature-driven handoff and coordination notes.
- `HANDOFF.md` only when single-agent continuity or cold-start orientation needs it.

Project setup rules:

1. Keep the global guide slim.
2. Put project facts in the project.
3. Put active work in the queue and workstream files.
4. Put durable decisions in the decisions log.
5. Put reusable operating knowledge in capabilities.
6. If the project has no capability root, install the first visible root from
   the foundational framework source.
7. Label each capability root with its purpose, contents, exclusions, and
   related roots.
8. Add additional capability roots only when discovery improves by agent,
   feature, domain, subsystem, or subject. Prefer visible sibling roots such as
   `capabilities-<scope>/`.
9. Keep capability roots connected by hub/spoke indexes, hyperlinks, backlinks,
   and metadata. Do not treat them as silos.
10. Put meals in the consuming capability root that references and uses the
   ingredient chain.
11. Keep new capability cards foundation-light unless risk, repeated use,
   evidence, or dependency impact earns governed/composition/cascade tracking.
12. Put cross-cutting rules in the nearest relevant capability root when they constrain many ingredients or recipes.
13. Preserve Claude as a peer workspace; do not delete, prune, or rewrite `.claude` material without explicit approval.

## What it depends on

- [Capability index routing](../recipes/capability-index-routing.md) - makes the capability index discoverable to Codex.
- [Multi-agent feature workstreams](../recipes/multi-agent-feature-workstreams.md) - coordinates concurrent feature work.

## Failure modes

- A single giant handoff turns into a junk drawer.
- A queue that also stores reasoning becomes hard to maintain.
- A capability index that is treated as optional gets skipped by future agents.
- A project without a first capability root forces every agent to rediscover the
  same project-specific operating knowledge.
- Multiple roots without hub/spoke links become hidden silos.
- Meals placed at the project level hide which capability root owns the
  behavior.
- A foundation card that quietly becomes a trust claim creates false certainty.
- Constant mutation without evidence, date, result, confidence, and rollback
  makes the framework unreliable.
- Copying Claude files wholesale can carry forward tool-specific assumptions instead of the underlying lesson.
