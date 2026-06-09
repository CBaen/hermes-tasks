---
id: agent-authored-evidence
name: Agent-Authored Evidence
schema_version: 2.1
profile: foundation
level: principle
maturity: candidate
scope: machine-wide Codex capability framework
currently_true: unknown
last_verified: 2026-05-07
tags:
  - evidence
  - agent
  - human review
  - verification
---

## What it does

Makes evidence usable without assuming a human reviewed every capability event.
Agent-authored evidence is valid when it names the verification performed.

## When to reach for it

Use this when adding evidence events, promotion notes, upvotes, downvotes,
failure records, or revalidation notes.

## How to use it

1. Record the actor as the agent, tool, or human who performed the check.
2. Name the verification in concrete terms: command, file inspection, live
   browser check, test result, review, or user approval.
3. Keep entries compact and non-sensitive.
4. Do not copy private conversation text, secrets, tokens, or long logs into the
   ledger.
5. Treat human review as valuable when it exists, not as a mandatory condition
   for all evidence.

## What it depends on

None.

## Failure modes

- Assuming every valid event needs human approval slows the framework down.
- Allowing vague agent notes without verification turns evidence into opinion.
- Copying raw private text into evidence creates avoidable privacy risk.
