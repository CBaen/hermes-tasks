---
id: truncation-recovery-law
name: Truncation Recovery Law
schema_version: 2.0
level: principle
maturity: candidate
scope: machine-wide agent context handling across Codex, current agents, and project workbenches
currently_true: unknown
verification_level: 1
last_verified: 2026-05-08
evidence_quality: direct
successful_uses: 0
failed_uses: 0
regressions: 0
depends_on:
  - current-truth-needs-evidence
used_by: []
tags:
  - truncation
  - context recovery
  - source of truth
  - no exceptions
  - handoffs
---

## What it does

Prevents agents from treating truncated information as complete. Truncation is
a recovery task, not a permission slip to infer, skip, summarize from fragments,
or proceed with partial context.

## Law

If context, tool output, file content, conversation history, search results,
logs, diffs, or handoffs are truncated, the agent must recover the missing
span from the source of truth before relying on the material.

There are no exceptions for convenience, token limits, time pressure, or "enough
visible context." Token limits require chunking, paging, narrower searches, line
ranges, or follow-up reads.

Protect the main agent's working context while recovering missing material. If
the source is large or a subagent/witness output is truncated, use a bounded
recovery lane, subagent, chunked artifact, or line-range read. Bring back source
paths, ranges/chunks, decision-changing evidence, and unresolved gaps, not the
whole bulky source.

## Required behavior

1. Identify what was truncated.
2. Identify the source of truth that can provide the missing span.
3. Preserve context by using a bounded recovery lane, subagent, line ranges, or
   chunked intake when direct reading would flood the main thread.
4. Read the missing chunks in order.
5. Reassemble the recovered content into the correct surrounding context.
6. Only then summarize, decide, edit, verify, or hand off.
7. If the missing content belongs in a durable place, update the correct queue,
   handoff, memory, capability, project doc, artifact, or lesson.
8. If the source cannot be safely recovered, state exactly what is missing and
   mark every dependent conclusion as unverified or blocked.

## Examples

- A tool output says "truncated" after line 200: reopen the file or rerun the
  command by line range before using line 201+ conclusions.
- A memory summary says a section was truncated: search/open the referenced
  memory or rollout file instead of relying on the summary gap.
- A handoff or queue excerpt cuts off mid-section: read the full file around
  that section before editing or marking work complete.
- A search result returns partial surrounding context: open the source file and
  inspect the full relevant block before quoting or applying the rule.

## Failure modes

- The agent assumes visible context is representative and misses a later
  exception, caveat, blocker, or contrary instruction.
- A partial handoff becomes false certainty and future agents repeat stale work.
- A truncated log hides the actual root cause.
- A truncated file read leads to editing the wrong section or duplicating a
  rule that already exists elsewhere.
