---
id: guiding-light-perspective-tender
name: Guiding Light Perspective Tender
schema_version: 2.0
level: recipe
maturity: candidate
scope: machine-wide memory review and agent-scope protection
currently_true: unknown
verification_level: 1
last_verified: 2026-05-05
evidence_quality: direct
successful_uses: 1
failed_uses: 0
regressions: 0
depends_on:
  - guiding-light-communication-protocol
  - codex-memory-bridge
used_by:
  - conversation-learning-loop
tags:
  - GL Proxy
  - perspective review
  - memory tender
  - scope guard
  - protective review
---

# Guiding Light Perspective Tender

Use this when Codex is turning conversations into durable memory, decisions, tasks, project context, or other reusable knowledge that claims to represent Guiding Light's perspective.

## Purpose

This is the Codex-native form of the older GL Proxy pattern. It does not pretend to be Guiding Light. It protects Guiding Light from Codex and from agent-side distortions before those distortions become durable memory.

The tender checks whether a candidate memory:

- overstates what Guiding Light said
- turns an agent inference into a user-confirmed preference
- pushes engineering choices onto the user
- mistakes technical details for user priorities
- treats the user's designer/business-owner scope as an engineering role
- carries privacy, client, or high-stakes risk
- contains agent overreach, false certainty, sycophancy, or other behavior that should not be reinforced

## Scope Boundary

Guiding Light is the designer, creator, business owner, and source of meaning. Codex owns engineering details when evidence is available.

The tender should flag cards where future agents might ask or remember the wrong thing, for example:

- asking Guiding Light to choose implementation details that Codex should resolve
- preserving technical noise as if it mattered to the user
- making a durable card that says "GL wants X" when the source only shows an agent guessed X
- promoting client/private context before speaker and privacy review

## Pipeline Role

Run after conversation-card preview and before promotion planning:

```bash
python /home/guidingl/.codex/automations/memory-bridge/guiding-light-perspective-tender.py /home/guidingl/.codex/tmp/memory-bridge/conversation-card-previews/conversation-card-preview-YYYYMMDD-HHMMSS.jsonl
```

Promotion planning must treat missing or held perspective review as a blocker.

## Output Meaning

- `passed_protective_preview`: no protective risk was detected in the card preview.
- `hold_for_gl_perspective_review`: the card may distort perspective, scope, priority, privacy, or agent behavior if promoted without review.
- `explicit_user_signal_present`: the card excerpt contains a direct user approval/preference signal.
- `not_confirmed_by_user_in_card_excerpt`: do not treat the card as user-confirmed without source review.

## Failure Modes

- If this becomes a persona, it fails. It is a review guard, not a simulated user.
- If it blocks every card forever, it fails. The job is to identify review work, not prevent memory.
- If it blesses agent inference as user truth, it fails.
- If it treats engineering details as Guiding Light's responsibility, it fails.
- If it copies conversation excerpts into reports, it fails its privacy boundary.
