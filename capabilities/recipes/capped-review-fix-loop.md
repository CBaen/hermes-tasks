---
id: capped-review-fix-loop
name: Capped Review Fix Loop
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: current-agent code/doc/work artifact review and repair cycles
currently_true: unknown
last_verified: 2026-05-07
tags:
  - review
  - fixes
  - verification
  - loops
  - GSD-migration
---

## What it does

Runs a bounded review → fix → re-review loop without letting autonomous repair spiral forever.

Adapted from Claude GSD's `gsd-code-review-fix` pattern.

## When to reach for it

Use when a review artifact exists and issues need repair:

- code review findings;
- UAT failures;
- doc verification gaps;
- security/accessibility warnings;
- capability registry/lint issues.

Skip when the issue is a single obvious edit that can be fixed and verified directly.

## How to use it

1. Start from a written review artifact (`REVIEW.md`, `UAT.md`, audit report, lint output, etc.).
2. Classify findings:
   - Critical / must fix;
   - Warning / should fix;
   - Info / optional;
   - Won't fix / documented reason.
3. Fix Critical + Warning by default. Include Info only when explicitly useful.
4. Make fixes in small, inspectable batches. For code, prefer atomic commits when project policy allows and no external push is involved.
5. Re-run the original verification witness.
6. If new issues appear, loop only up to a fixed cap. Default cap: 3 total repair passes.
7. If still failing at cap, stop and write a blocker summary with evidence and recommended next action.
8. Update the review artifact with what changed and how it was verified.

## What it depends on

- [No Bare Claims](../principles/no-bare-claims.md)
- [Conversational UAT Verification](conversational-uat-verification.md)
- [Plan Deepen Before Build](plan-deepen-before-build.md)
- [Guiding Light Proxy Review](guiding-light-proxy-review.md)

## Failure modes

- Infinite repair loops.
- Fixing symptoms without re-running the original failing check.
- Treating Info-level suggestions as mandatory and bloating scope.
- Bundling unrelated fixes so rollback is hard.
- Declaring success from code edits alone.

## Evidence

- `C:/Users/baenb/.claude/skills/gsd-code-review-fix/SKILL.md:13-20` defines reading `REVIEW.md`, fixing review findings, and producing a `REVIEW-FIX.md` summary.
- `C:/Users/baenb/.claude/skills/gsd-code-review-fix/SKILL.md:26-28` fixes Critical + Warning by default, with `--all` for Info findings.
- `C:/Users/baenb/.claude/skills/gsd-code-review-fix/SKILL.md:29-31` caps auto fix + re-review iterations at 3.
- `research/claude-to-openclaw-skill-migration/GSD-SKILL-FAMILY-AUDIT-2026-05-07.md` identifies capped review/fix loops as migration-worthy.
