---
id: advisory-evolution-review-loop
name: Advisory Evolution Review Loop
schema_version: 2.0
level: recipe
maturity: candidate
scope: workspace/project scheduled learning reviews for Guiding Light, Codex, and verified peer agents
currently_true: unknown
verification_level: 1
last_verified: 2026-05-06
evidence_quality: direct
successful_uses: 0
failed_uses: 0
regressions: 0
depends_on:
  - no-bare-claims
  - moji-project-capability-layers
  - moji-conversation-index
used_by:
  - cross-agent-learning-loop-container
tags:
  - evolution
  - scheduled review
  - advisory
  - capability maturity
  - commits
  - conversation review
  - codex
  - hermes
---

## What it does

Defines the common pattern behind Moji's scheduled learning reviews: notice useful patterns, strengths, friction, and capability opportunities without turning the process into unsupervised action.

This is the human-facing support loop around the technical learning-loop infrastructure.

## When to reach for it

Use when setting up or auditing recurring reviews of:

- conversation/session learning opportunities;
- Qdrant or memory-bridge outputs;
- commit metadata/deltas;
- project capability maturity;
- workstation-wide workflow patterns;
- skill growth for Guiding Light, Codex, and verified peer agents.

Claude is excluded while Guiding Light says so.

## How to use it

Use this review shape:

```text
approved observations
-> advisory report
-> candidate lessons/opportunities
-> suggested tiny next improvement
-> optional human-approved capability/memory/export update
```

Required report sections:

1. **Sources reviewed** - paths/tools, minimized and audience-safe.
2. **What is working well** - strengths worth reinforcing.
3. **Opportunities** - patterns, gaps, refinements, or support ideas.
4. **Risks / guardrails** - privacy, autonomy, noise, overcollection, stale evidence.
5. **Candidate lessons** - not automatically promoted.
6. **Next tiny improvement** - one small useful action.
7. **Evidence level** - direct / inferred / needs review.

Default guardrails:

- Advisory/reporting only.
- No public/external actions.
- No destructive repo operations.
- No raw conversation body exposure.
- No raw private-source excerpts in user-facing summaries.
- No Qdrant/vector writes without explicit approval.
- No capability auto-promotion.
- No Claude/.claude/Claude exports while excluded.

## What it depends on

- `no-bare-claims`
- `moji-project-capability-layers`
- `moji-conversation-index`

## Failure modes

- Becoming noisy recurring homework for Guiding Light.
- Producing vague self-improvement theater without evidence.
- Recommending too many improvements at once.
- Treating commit/session history as proof of current truth.
- Accidentally turning advisory reviews into autonomous changes.

## Evidence notes

Created after Guiding Light asked for recurring reviews of conversation/Qdrant history, commits, and capabilities to surface what is working, opportunities, and new skill levels for Guiding Light, Moji, and Codex.
