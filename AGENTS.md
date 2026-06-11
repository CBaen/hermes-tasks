# Hermes Tasks - Agent Instructions

This project inherits the machine-wide Guiding Light Codex communication protocol from `/home/guidingl/AGENTS.md`.

Use this file for project-specific truth, routing, and constraints. Do not duplicate the full global protocol here.

## If You Are New, Do This First

1. Confirm the current git branch is `main` when this is a git repo.
2. Read `SOURCE-OF-TRUTH.md`, then the current handoff/status file if present.
3. Read `hermes-tasks-queue.md`, `hermes-tasks-decisions.md`, `GLOBAL-DECISIONS.md`, and `hermes-tasks-index.md`.
4. Read `capabilities/INDEX.md` or the nearest project capability root only as needed for the task.
5. Verify before claiming work is done.

## Capability Framework Setup

If this is the first capabilities framework folder in this project:

1. Copy the starter folder from `/home/guidingl/capabilities/` into a visible project root such as `capabilities/`.
2. Keep it foundation-light on day one.
3. Add a root label to `capabilities/INDEX.md`: what it does, what belongs there, what does not belong there, and related roots.
4. Link `capabilities/INDEX.md` from this file and the project index.
5. Use `/home/guidingl/capabilities/recipes/first-capability-root-install.md`.

If adding another capabilities framework folder in this project:

1. Name why the root exists: agent, feature, domain, subsystem, or subject.
2. Prefer a visible sibling root such as `capabilities-<scope>/`.
3. Use hidden roots such as `.codex/capabilities/` only when the root is runtime-specific or already evolved in that shape. Retired runtime roots should not receive new work.
4. Give it a slim `INDEX.md` with a root label.
5. Link it from the nearest parent index and the baseline project capability index.
6. Use `/home/guidingl/capabilities/recipes/additional-capability-root-install.md`.

## Project Reality

- Client / owner: Guiding Light
- What this project is: A new persistent project scaffold rooted at this repo, ready for queue/decision/index/capability-driven work.
- What this project is not: A finished app, runtime state dump, or secret store.
- Current source of truth: `AGENTS.md`, `SOURCE-OF-TRUTH.md`, `PROJECT-STATUS.md`, `HANDOFF.md`, `hermes-tasks-queue.md`, `hermes-tasks-decisions.md`, `GLOBAL-DECISIONS.md`, `LESSONS-LEARNED.md`, `hermes-tasks-index.md`, `agent-lanes/BOARD.md`, and the relevant capability root index.

## Read First

1. `hermes-tasks-queue.md`
2. `hermes-tasks-decisions.md`
3. `hermes-tasks-index.md`
4. `capabilities/INDEX.md` or the nearest project capability root
5. Recent git history when this is a git repo

## Current Work Model

- Queue stores active work.
- Decisions log stores durable decisions and why they were made.
- Index stores references and research pointers.
- Workstreams store active multi-agent feature handoffs.
- Capability files store reusable project operating knowledge.
- Capability roots are not silos. Link ingredients, recipes, meals, and feasts
  across roots/projects when the work actually composes that way.
- Meals live with the consuming capability root that references and uses the
  ingredient chain, not automatically with the whole project.
- If a linked dependency fails, affected capabilities go on watch or probation.
  Three evidence-backed successful uses are required before greenlit trust
  returns.
- Foundation capability cards are the default. Governed evidence,
  composition tracking, and cascade watch status are used only when earned by
  complexity, risk, repeated use, or dependency impact.

## Verification Rules

- Treat old docs and handoffs as claims until verified.
- Verify against files, git state, tests, live systems, or official sources before claiming success.
- Say clearly when something is unverified.
- Changes to trust-bearing capability fields need evidence, date, result,
  confidence, and rollback or revalidation.

## Start Here

- Project capability root: `capabilities/INDEX.md`
- Open only the specific capability files needed for the task.
