---
id: wave-based-phase-execution
name: Wave-Based Phase Execution
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: executing multi-plan project phases with controlled parallelism
currently_true: unknown
last_verified: 2026-05-07
tags:
  - execution
  - waves
  - subagents
  - GSD-migration
  - TaskFlow
---

## What it does

Executes a multi-plan phase in dependency-aware waves, keeping the orchestrator lean and requiring verification before declaring phase completion.

Adapted from Claude GSD's `gsd-execute-phase`, but constrained by OpenClaw's reliable-subagent rules.

## When to reach for it

Use when a phase has multiple executable plans that can be grouped by dependency or risk.

Prefer sequential/manual execution when the phase is small, high-risk, or subagent instability would cost more than it saves.

## How to use it

1. Read the executable phase plan(s) and dependency notes.
2. Group work into waves:
   - wave 1: prerequisites/foundations;
   - later waves: dependent or independent chunks;
   - gap-only wave: fixes from UAT/review.
3. For each lane, define exact source/write boundaries and required output artifacts.
4. Use the smallest number of agents that reduces risk. Do not spawn broad swarms.
5. Execute one wave at a time unless independence is clear.
6. After each wave, collect artifacts, inspect changes, and run verification gates.
7. Only mark phase complete when all required plans are complete and verification passes.
8. Treat optional flags as active only when explicitly requested; never infer them from documentation.

## What it depends on

- [Executable Phase Plan](executable-phase-plan.md)
- [Reliable Subagent Execution](reliable-subagent-execution.md)
- [Named Agent Orchestration](named-agent-orchestration.md)
- [Conversational UAT Verification](conversational-uat-verification.md)
- [Capped Review Fix Loop](capped-review-fix-loop.md)

## Failure modes

- Parallelizing work with hidden dependencies.
- Letting orchestrator do builder work and lose synthesis role.
- Trusting agent summaries without reading artifacts.
- Treating documented flags/options as active behavior.
- Marking complete before verification.

## Evidence

- `C:/Users/baenb/.claude/skills/gsd-execute-phase/SKILL.md:14-17` defines wave-based parallel execution and a lean orchestrator.
- `C:/Users/baenb/.claude/skills/gsd-execute-phase/SKILL.md:19-24` defines wave and gaps-only execution filters.
- `C:/Users/baenb/.claude/skills/gsd-execute-phase/SKILL.md:25-29` warns that optional flags are active only when literal tokens appear.
- `research/claude-to-openclaw-skill-migration/GSD-SKILL-FAMILY-AUDIT-2026-05-07.md` identifies wave execution as useful but needing OpenClaw adaptation.
