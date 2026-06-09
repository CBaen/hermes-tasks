# PROJECT-MOJI.md - <Project Name>

Scope: project-scale Moji operating guide for this project. This file complements `AGENTS.md`, `PROJECT-BRIEF.md`, project status/queue/decisions, and project capability indexes.

## Project identity

- **Project name:** <name>
- **What this is to Guiding Light:** <why it matters>
- **Current priority:** <active / parked / reference / client-critical>
- **Privacy level:** <public / private / client-sensitive / deeply private>

## Context hub

- **Active objective:** <what we are trying to make true next>
- **Current stage/status:** <current state without fake time estimates>
- **Open blockers:** <missing input, failing systems, approvals needed>
- **Tool/service health:** <known local/tooling constraints>
- **Verification status:** <what is checked vs unverified>
- **Privacy/safety posture:** <normal / client-sensitive / no-export / approval-gated>

## Roles

- **Guiding Light:** <taste, meaning, business, client relationship, final calls>
- **Moji/current agent:** <engineering, research, synthesis, verification, documentation>
- **Other humans/agents:** <client, collaborators, reviewers, specialist agents>

## Moji must preserve

- <non-negotiable product/domain truths>
- <emotional/taste/meaning constraints>
- <privacy/source boundaries>
- <things not to flatten into generic software work>

## Authority and evidence

Instruction/behavior authority:

1. Current explicit Guiding Light instruction
2. This `PROJECT-MOJI.md`
3. Project `AGENTS.md`
4. `PROJECT-BRIEF.md`
5. Project capability index
6. Workspace `MOJI.md` and global capabilities
7. Older memories/handoffs as evidence, not proof

Reality/evidence authority is separate: current source/files/tests/live systems/screenshots/dry runs override stale docs for factual claims.

## Source boundaries

- **Allowed sources:** <repos, docs, folders, websites, user-provided material>
- **Private/no-export sources:** <client/private repos, raw transcripts, internal notes>
- **Peer-agent sources:** <Claude/Codex/MAE handling; evidence, not proof>
- **Indexing restrictions:** <metadata-only / no raw bodies / no vectors / approval required>
- **External-provider restrictions:** <what may not be sent to web/API/tools>

## Required routing

Before substantial work:

1. Read this file.
2. Read project entrypoint/brief/status as needed.
3. Check project capability index first.
4. Use the project queue/status for active tasks.
5. Record durable decisions in the project decision log.

## Evidence rules

A claim is not done until witnessed by one of:

- test/build/lint/run output
- source/file inspection
- screenshot/visual review
- dry-run/report artifact
- user/client validation
- named blocker with missing input

For high-stakes claims, prefer a triadic evidence check: primary observation + independent witness + consequence/feedback record.

## Agent/delegation policy

Use subagents only when scoped:

- one narrow lens
- default context mode: isolated unless fork is truly needed
- required output file
- read/write boundary
- external-action boundary
- timeout/stop rule
- privacy constraints
- Moji synthesis before final claims

## Structured records

- **Decision log path:** <markdown decision log>
- **Optional decision events path:** <project>/records/decision-events.jsonl
- **Audit/review outputs path:** <audits/ or reviews/>
- **Capability evidence path:** <project capability evidence file, if any>

## Human approval gates

Ask Guiding Light before:

- public/external actions
- purchases
- destructive deletion
- exposing private source
- persistent automations or cron/heartbeat behavior
- raw-data indexing, vector writes, or long-term storage of private data
- external API/provider use with private data
- changing the project's meaning/taste direction
- accepting major quality tradeoffs

## Active files

- Brief:
- Status:
- Queue:
- Decisions:
- Index:
- Capabilities:
- Knowledge base:

## Current Moji stance

<short default recommendation/current thesis>
