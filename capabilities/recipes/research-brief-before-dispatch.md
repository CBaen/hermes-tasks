---
id: research-brief-before-dispatch
name: Research Brief Before Dispatch
schema_version: 2.0
level: recipe
maturity: candidate
scope: Codex and peer-agent research dispatches before expeditions, councils, or external/fresh-agent research
currently_true: planned
verification_level: 1
last_verified: 2026-05-09
evidence_quality: migrated from Claude skill by GL request
tags:
  - research
  - expedition
  - brief
  - verification
---

# Research Brief Before Dispatch

Use before sending a fresh agent/researcher into `/expedition`, extended expedition, research council, or any decision-shaping research task.

## Rule

A research brief is for a stranger. It gives current state, constraints, and questions. It is not a handoff, history, or proof of prior work.

## Required Format

Write exactly five sections:

1. **Want** — one paragraph describing success as a concrete outcome/experience.
2. **Have** — one paragraph of current stack/state and integration points.
3. **Won't Accept** — bullets for constraints and unacceptable failure modes.
4. **Open To** — one paragraph naming what architecture/tooling/process can change.
5. **Questions** — numbered research questions, each tied to a decision.

## Bloat Filter

Remove:

- project archeology and long migration stories;
- narrative quotes and emotional history;
- file-path tours beyond necessary orientation;
- code comments treated as proof;
- stale memory claims without verification;
- failed approaches beyond a one-line warning if relevant;
- duplicated constraints.

## Verification Pass

Before dispatch, verify factual claims against current code/state where possible:

- paths/files exist;
- named services/libraries/versions are checked when relevant;
- pipeline behavior is read from current code/config/live state;
- unverified claims are labeled.

## Delivery

Save to:

- `research/expedition-<topic>/research-brief.md`
- `research/council-<topic>/research-brief.md`
- or `research/research-<topic>/research-brief.md`

Show the requester only a short summary + path + approval ask. Do not dispatch before approval when review was requested.
