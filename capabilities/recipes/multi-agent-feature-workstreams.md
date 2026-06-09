---
name: Multi-agent feature workstreams
level: recipe
last_verified: 2026-05-02
---

## What it does

Coordinates multiple agents in the same project by feature lane or user-facing outcome instead of frontend/backend ownership.

## When to reach for it

Use this when more than one agent is working in a project, when work crosses technical layers, or when the user thinks about the work as features, stages, or big rocks.

## How to use it

1. Use `PROJECT-STATUS.md` as the project map.
2. Use `workstreams/<feature-slug>.md` as the active job sheet for each feature lane.
3. Define ownership by outcome:
   - Feature or big rock
   - User-facing goal
   - Current stage
   - Agent/session owner
   - Touched areas
   - Known dependencies or collision points
   - Verification state
4. Keep the queue as the source of active tasks.
5. Keep durable decisions in `{project}-decisions.md`.
6. Keep references in `{project}-index.md`.
7. Keep reusable process knowledge in the project `capabilities/` root, a
   visible purpose root such as `capabilities-<scope>/`, or the neutral
   system/user root when the knowledge is truly cross-project.
8. Update shared handoff surfaces at completion and handoff stages.
9. Resolve code-level overlap automatically when it does not change scope, design, priority, user experience, client boundary, or business/data meaning.
10. Ask the user only when an overlap changes one of those user-visible or business-facing concerns.

## Workstream template

```markdown
# <Feature Name> Workstream

## Outcome

What this feature does for the user, client, or project.

## Current Stage

Not started | Active | Blocked | Ready for review | Complete | Handed off

## Owner

Agent/session and branch/worktree if relevant.

## User-Facing Impact

What changes in the product or workflow.

## Touched Areas

Pages, services, docs, data, design surfaces, or systems involved.

## Dependencies And Collision Points

Other feature lanes, shared files, shared data, or design decisions that could overlap.

## Verification

What was checked, what still needs checking, and the source of truth.

## Decisions And References

Links to queue items, decisions, index entries, or capability files.

## Next Handoff Stage

What the next agent should do first.
```

## What it depends on

- [Capability index routing](capability-index-routing.md) - finds the capability structure that stores project knowledge.

## Failure modes

- One shared handoff file can become a traffic jam when multiple agents edit it.
- Layer-based ownership can hide real overlap because feature work often touches design, data, backend, frontend, docs, and verification together.
- A workstream file should not duplicate every task in the queue. It should explain the state of that feature lane.
