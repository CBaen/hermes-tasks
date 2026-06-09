---
id: conversational-uat-verification
name: Conversational UAT Verification
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: user-perspective verification after current-agent builds or behavior changes
currently_true: unknown
last_verified: 2026-05-07
tags:
  - verification
  - UAT
  - user-testing
  - GSD-migration
  - ADHD-support
---

## What it does

Verifies built work from the user's perspective with plain-language, one-test-at-a-time checks and a persistent UAT artifact.

Adapted from Claude GSD's `gsd-verify-work` pattern.

## When to reach for it

Use after building or changing something that GL, a client, or an end user will experience:

- UI/workflow changes;
- forms and checkout/payment flows;
- generated content/layouts;
- command-center or project-management surfaces;
- anything where tests can pass but the human experience may still be wrong.

Skip for pure internal docs unless the doc itself is the deliverable.

## How to use it

1. Define the feature/work item being verified.
2. Create or update a UAT artifact. Suggested path:
   - `<project>/workstreams/<slug>/UAT.md`, or
   - `research/<topic>/UAT.md` for internal workspace work.
3. Present one test at a time in plain language:
   - what to open/do;
   - what “good” looks like;
   - what to report if it feels wrong.
4. Prefer Moji-run verification first when possible: tests, screenshots, browser checks, logs, direct inspection.
5. When GL input is needed, do not interrogate. Ask for the smallest useful observation.
6. Record each result:
   - pass/fail/blocked;
   - evidence;
   - issue found;
   - diagnosis path;
   - fix plan or next gate.
7. If issues are found, route to plan-deepen/fix plan before execution. Do not claim done until re-verified.

## What it depends on

- [No Bare Claims](../principles/no-bare-claims.md)
- [Plan Deepen Before Build](plan-deepen-before-build.md)
- [Guiding Light Proxy Review](guiding-light-proxy-review.md)

## Failure modes

- Treating automated tests as enough for human-facing work.
- Asking GL to debug instead of observe.
- Asking many questions at once.
- Losing UAT state in chat instead of writing it down.
- Fixing issues without re-verifying the original symptom.

## Evidence

- `C:/Users/baenb/.claude/skills/gsd-verify-work/SKILL.md:12-15` defines conversational testing with persistent state, one test at a time, plain text responses, and no interrogation.
- `C:/Users/baenb/.claude/skills/gsd-verify-work/SKILL.md:17` defines `{phase_num}-UAT.md` as the output tracking test results.
- `research/claude-to-openclaw-skill-migration/GSD-SKILL-FAMILY-AUDIT-2026-05-07.md` identifies UAT as a strong migration-worthy gate.
