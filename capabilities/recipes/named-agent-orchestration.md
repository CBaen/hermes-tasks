---
id: named-agent-orchestration
name: Named Agent Orchestration
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: Banebook Codex and peer-agent subagent work
currently_true: unknown
last_verified: 2026-05-07
tags:
  - subagents
  - orchestration
  - review lanes
  - source boundaries
  - synthesis
---

## What it does

Uses agents/subagents without recreating loose swarm failures. A good agent run has a narrow lane, clear source boundary, required output, stop rule, and Moji synthesis.

## When to reach for it

Use when independent review lenses, source inventory/extraction, audit passes, narrow research summaries, or long-running work would reduce risk or cognitive load.

Avoid it for tiny edits, unclear broad exploration, tasks needing taste/meaning decisions from Guiding Light, or work where subagent instability would cost more than doing it directly.

## How to use it

Default rule: do not spawn broad exploratory swarms. Use the smallest number of agents that reduces risk or cognitive load.

For each agent/reviewer, define:

- **Name/label:** stable, descriptive lane name
- **Purpose:** one narrow lens
- **Context mode:** isolated by default; fork only when current transcript is required
- **Source inputs:** exact files/folders/URLs allowed
- **Private/no-export boundary:** what must not leave the workspace
- **Write boundary:** read-only or exact output path(s)
- **Required output:** report file path and section headings
- **Stop rule:** timeout, max scope, and when to return partial findings
- **External-action boundary:** no external writes/public actions unless separately approved
- **Synthesis owner:** Moji/main integrates and verifies before user-facing conclusions

Prompt checklist:

1. Read-only vs write boundary.
2. Exact source path(s).
3. Required output file.
4. Required report sections.
5. Privacy/source handling.
6. No external web/actions unless explicitly needed.
7. Concise, source-backed output.
8. Stop rule or timeout.

After agents finish, Moji must:

1. Read output files, not just completion summaries.
2. Treat agent reports as evidence, not proof.
3. Verify important claims against source/tool output.
4. Apply safe edits directly when requested.
5. Summarize what changed, what remains, and named blockers.

## What it depends on

- [No Bare Claims](../principles/no-bare-claims.md)

## Failure modes

If agents time out, lose context, or produce noisy output: stop the run if needed, preserve useful partial outputs, document the failure pattern, do not keep spawning replacements blindly, and switch to manual or fewer-agent work.
