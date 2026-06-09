---
id: persistent-debug-session
name: Persistent Debug Session
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: debugging issues across context resets or multi-step investigations
currently_true: unknown
last_verified: 2026-05-07
tags:
  - debugging
  - root-cause
  - persistent-state
  - GSD-migration
---

## What it does

Keeps debugging scientific and stateful: symptoms, hypotheses, tests, evidence, eliminated causes, root cause, fix, and verification survive context resets.

Adapted from Claude GSD's `gsd-debug` pattern.

## When to reach for it

Use when:

- a bug has unclear root cause;
- multiple fix attempts have failed;
- investigation will require reading many files/logs;
- work may span sessions;
- diagnosis should be validated before fixes.

Skip for simple obvious errors with a direct verification path.

## How to use it

1. Create a debug session note. Suggested path:
   - `<project>/debug/<slug>.md`, or
   - `research/<topic>/debug-<slug>.md` for workspace/internal work.
2. Record:
   - symptom;
   - reproduction path;
   - current hypothesis;
   - test being run;
   - expected result;
   - evidence collected;
   - eliminated hypotheses;
   - next action;
   - blocker/status.
3. Prefer diagnose-only mode when a wrong fix could make things worse.
4. Use narrow agents only when isolation/context helps; require them to write into the debug note or linked artifact.
5. Do not apply fixes until the hypothesis has a witness.
6. After fixing, verify against the original symptom and record the result.

## What it depends on

- [No Bare Claims](../principles/no-bare-claims.md)
- [Capped Review Fix Loop](capped-review-fix-loop.md)
- [Triadic Deliberation for Consequential Work](triadic-deliberation-for-consequential-work.md) for repeated/high-stakes failures.

## Failure modes

- Random-walk debugging.
- Patching symptoms without proving root cause.
- Losing investigation state in chat.
- Continuing after repeated failure without escalating lens/review.
- Claiming fix without reproducing/clearing original symptom.

## Evidence

- `C:/Users/baenb/.claude/skills/gsd-debug/SKILL.md:12-18` defines scientific debugging with subagent isolation and diagnose-only mode.
- `C:/Users/baenb/.claude/skills/gsd-debug/SKILL.md:20-26` defines list/status/continue subcommands for persistent debug sessions.
- `C:/Users/baenb/.claude/skills/gsd-debug/SKILL.md:70-90` describes session summaries with hypothesis and next action.
- `research/claude-to-openclaw-skill-migration/GSD-SKILL-FAMILY-AUDIT-2026-05-07.md` identifies persistent debugging as migration-worthy.
