---
id: per-agent-evolving-capabilities
name: Per-Agent Evolving Capabilities
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: Codex, Claude-derived patterns, named agents, verified peer agents, and project agents
currently_true: unknown
last_verified: 2026-05-07
tags:
  - agents
  - capability roots
  - evolution
  - specialization
  - adapters
---

## What it does

Lets different agents and agent roles develop their own capability surfaces while sharing agent-neutral lessons through visible roots and sanitized exports.

## When to reach for it

Use when designing Moji, Codex, Claude-derived migration lessons, named subagents, project specialists, agency/business agents, content/art agents, or software/Frappe agents.

## How to use it

1. Separate role from runtime:
   - runtime adapter: Codex, Claude-derived references, browser/CLI/session constraints;
   - agent role: researcher, implementer, reviewer, vocabulary coach, Frappe specialist, content strategist;
   - project domain: client, product, workstream.
2. Give persistent agents or recurring roles a visible or adapter-specific capability root when they have enough repeated work to justify it.
3. Keep role-specific cards scoped. Do not put every agent behavior into Moji's global root.
4. Shared lessons move through sanitized exports, evidence events, and promotion gates, not raw runtime/session sharing.
5. Agent capabilities should declare:
   - what the agent is for;
   - what sources it may use;
   - what it must not touch/export;
   - output path/format;
   - verification expectations;
   - how failure affects downstream confidence.
6. Named agents should use narrow lanes and output files before their behavior is promoted.

## What it depends on

- [Multi-Root Capability Ecosystem](multi-root-capability-ecosystem.md)
- [Named Agent Orchestration](named-agent-orchestration.md)
- [Cross-Agent Learning Loop Container](cross-agent-learning-loop-container.md)

## Failure modes

- Treating all agent personalities/processes as one Moji behavior blob.
- Copying one runtime's assumptions into another agent.
- Letting agents evolve without evidence, privacy boundaries, or rollback.
- Creating many specialized agents before their lanes are stable.
