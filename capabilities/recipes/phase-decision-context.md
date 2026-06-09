---
id: phase-decision-context
name: Phase Decision Context
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: current-agent project phase setup before research/planning/building
currently_true: unknown
last_verified: 2026-05-07
tags:
  - planning
  - project-state
  - decisions
  - ADHD-support
  - GSD-migration
---

## What it does

Captures the implementation decisions downstream agents need before planning or building, without making Guiding Light re-answer settled questions.

Adapted from Claude GSD's `gsd-discuss-phase` pattern.

## When to reach for it

Use before research, planning, or execution when a project phase/work chunk has:

- unclear implementation choices;
- prior decisions scattered across project files;
- risk of asking GL questions already answered;
- tangents that need parking without losing them;
- downstream agents/planners that need a compact `CONTEXT.md`-style artifact.

Skip for tiny obvious tasks or when a current plan already has all needed decisions and evidence.

## How to use it

1. **Load prior context first.** Read the project entrypoint and current state files before asking anything:
   - `PROJECT-MOJI.md`, `PROJECT-BRIEF.md`, `AGENTS.md`, project queue/status/decision files;
   - nearest capability index;
   - relevant prior `CONTEXT.md`/phase notes if present.
2. **Scout current ground truth.** Inspect files/code/docs enough to know what choices are actually open.
3. **Identify gray areas.** Separate:
   - already-decided choices;
   - technical defaults Moji can choose;
   - genuine GL decisions about taste, meaning, business, risk, or external commitments.
4. **Ask sparingly.** Ask at most one blocking question at a time. If a safe default exists, choose it and document it.
5. **Park tangents.** Capture interesting but non-critical ideas in a queue/backlog note instead of derailing the active phase.
6. **Write the artifact.** Create or update a compact phase context note with:
   - objective;
   - locked decisions;
   - recommended defaults chosen by Moji;
   - open blockers, if any;
   - boundaries / what not to touch;
   - source files inspected;
   - next planning/research/build step.
7. **Use the artifact downstream.** Research briefs, plan-deepen, source-separated research, or build plans should read this file instead of re-interviewing GL.

## Suggested artifact path

Use the project's existing convention. If none exists:

```text
<project>/workstreams/<slug>/CONTEXT.md
```

For workspace/internal work:

```text
research/<topic>/CONTEXT.md
```

## What it depends on

- [Capability Index Routing](capability-index-routing.md)
- [Stranger-Ready Research Brief](stranger-ready-research-brief.md)
- [Plan Deepen Before Build](plan-deepen-before-build.md)
- [No Bare Claims](../principles/no-bare-claims.md)
- [Guiding Light Proxy Review](guiding-light-proxy-review.md)

## Failure modes

- Asking GL to repeat decisions already present in files.
- Treating vague vision as an implementation decision.
- Letting tangents silently become scope creep.
- Writing a bloated handoff instead of a compact downstream context artifact.
- Choosing no default when Moji can safely decide.

## Evidence

- `C:/Users/baenb/.claude/skills/gsd-discuss-phase/SKILL.md:13-20` states the objective: extract implementation decisions downstream agents need and write a `CONTEXT.md` artifact.
- `C:/Users/baenb/.claude/skills/gsd-discuss-phase/SKILL.md:23-29` outlines loading prior context, scouting codebase, skipping already-decided gray areas, discussing remaining areas, and writing context.
- `C:/Users/baenb/.claude/skills/gsd-discuss-phase/SKILL.md:62-68` defines success criteria: no re-asking decided questions, gray areas identified, scope creep redirected, and decisions captured clearly.
- `research/claude-to-openclaw-skill-migration/GSD-SKILL-FAMILY-AUDIT-2026-05-07.md` recommends this as the first tiny GSD migration action.
