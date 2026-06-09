---
name: Artifactless research delegation
type: failure
failure_kind: process_failure
schema_version: 0.1
date_discovered: 2026-05-10
last_updated: 2026-05-10
status: open
scope: global
owner_context: Locally Twisted ecommerce audit / multi-agent research lanes
related_capabilities:
  - current-truth-needs-evidence
related_failures: []
tags:
  - subagents
  - research
  - delegation
  - artifacts
  - truncation
  - evidence
  - ecommerce
---

# Failure Recipe: Artifactless research delegation

## Symptom

A delegated agent or research lane does substantial-looking work, may even
announce success, but fails to leave the required durable artifact. The parent
session receives huge routed output, truncated output, partial progress, or a
completion event without the named report. The work feels like progress but
cannot be safely used as evidence.

## Trigger conditions

- Multi-agent research dispatches where the prompt requires a named artifact.
- High-token audits over many pages, products, code paths, docs, or browser
  actions.
- Lanes that scrape/enumerate many records and stream raw data back instead of
  writing compact findings first.
- Time-limited subagents with broad scope.
- Parent sessions tempted to summarize child output from routed chat rather than
  verifying files on disk.
- Work where downstream synthesis depends on comparing multiple lanes.

## Known instances

| Date | Project | Surface | Action being taken | Bad outcome | Evidence | Guard state | Status |
|---|---|---|---|---|---|---|---|
| 2026-05-10 | Locally Twisted ERPNext ecommerce | Ecommerce audit Lane E | Odoo docs / agent-action convergence researcher | Timed out after partial progress and left no `workstreams/ecommerce-audit/odoo-docs-agent-action-convergence-2026-05-10.md`; no usable evidence | Parent verified `MISSING_ARTIFACT`; daily memory records no-artifact rule | added but not yet automated | open |
| 2026-05-10 | Locally Twisted ERPNext ecommerce | Ecommerce audit Lane A | Odoo Source Mapper | Returned very large/truncated routed extraction output but left no `workstreams/ecommerce-audit/odoo-source-commerce-map-2026-05-10.md`; raw output could not be trusted as complete evidence | Parent verified `MISSING_ARTIFACT`; routed result was truncated | added but not yet automated | open |
| 2026-05-10 | Locally Twisted ERPNext ecommerce | Ecommerce audit Lane B | ERPNext/Frappe Receiving Parity Auditor | Returned very large routed search output but left no `workstreams/ecommerce-audit/erpnext-receiving-parity-matrix-2026-05-10.md`; parity evidence missing | Parent verified `MISSING_ARTIFACT` | added but not yet automated | open |
| 2026-05-10 | Locally Twisted regression research | Copy/nav/banner regression expedition lanes | Source-separated research dispatch around recurring business-inventory regressions | Multiple lanes timed out or produced unusable/truncated output; failed lanes could not be treated as evidence and became process-failure examples themselves | `memory/2026-05-10.md` notes failed/timed-out lanes are not evidence | weak | open |

## Root pattern

The workflow treats **task completion** or **subagent output volume** as a proxy
for evidence. It forgets that durable research requires a named artifact with
bounded findings, evidence paths, unknowns, and status. When the artifact is
missing, the parent can accidentally synthesize from partial/truncated output
and turn an evidence gap into a confident decision.

## Why it seemed reasonable at the time

The child agent appears to have worked: it ran tools, found data, and may report
"completed successfully." Routed output may contain useful-looking snippets,
counts, or examples. Under time pressure, the parent wants to keep momentum and
avoid rerunning expensive work. That makes it tempting to treat the child output
as enough, even when the actual contract was "write the report."

## Detection signals

- Completion event says success but the required artifact path is missing.
- Output contains huge raw dumps, long grep results, product enumerations, or
  browser observations instead of a compact report.
- Output is explicitly truncated or includes omitted middle content.
- Tool result says timed out, partial progress, or no named file.
- Parent says "interesting raw output" or "looks useful" before verifying disk.
- Required artifact directory exists but expected lane file does not.
- Synthesis is blocked because one lane has only chat output.

## Required guard

- Every delegated lane must name its required artifact path in the prompt.
- Parent must verify `Test-Path` / file existence and inspect the status block
  before counting a lane as evidence.
- Child prompts should require "write summary artifact first, raw extraction
  second" for high-volume lanes.
- Large extraction lanes should write bounded summaries plus separate raw data
  files when needed; never stream raw data as the main result.
- Synthesis/referee lanes must refuse to run until required artifacts exist or
  are explicitly marked `[NO EVIDENCE]`.
- Timeout/truncation/no-artifact outcomes should be recorded as process failures,
  not silently retried without changing scope.

## Recovery recipe

1. Stop synthesis; do not use routed child output as complete evidence.
2. Verify the required artifact path directly.
3. If missing, mark the lane `[NO EVIDENCE]` in the parent workstream/status.
4. Capture the failure instance before rerunning.
5. Rerun narrower or split the lane so the first action is writing a compact
   artifact/status block.
6. If raw extraction is needed, require a separate data file and a bounded
   summary report.
7. Only resume synthesis after artifacts exist or the missing lane is explicitly
   excluded with its blast radius named.

## What not to do

- Do not treat a child completion event as evidence.
- Do not summarize from truncated routed output.
- Do not paste massive raw dumps into the parent report as a substitute for a
  durable artifact.
- Do not rerun the same broad prompt unchanged after a timeout/no-artifact
  failure.
- Do not blame the child agent and move on; fix the delegation contract.

## Cross-links

- Related capability: `current-truth-needs-evidence`
- Related principle: artifact-first evidence / truncation recovery law
- Related workstream: Locally Twisted ecommerce audit dispatch prompts
- Related adapter note: subagent orchestration and completion events
- Related Failure Recipe: source/example text counted as approval gates; stale
  source resurrection; verifier rewritten to match regression

## Evidence quality

[VERIFIED] Parent session directly checked the expected Lane A/B/E artifact paths
and found them missing after completion/timeout events on 2026-05-10.

[VERIFIED] Lane C and Lane D showed the positive version of the guard by leaving
named artifacts under `workstreams/ecommerce-audit/`, allowing direct inspection.

[TRUNCATED] Lane A and Lane B routed outputs included large/truncated content and
therefore cannot be used as complete evidence.

[OPEN] Guard is documented but not yet automated in tooling. A future verifier
could check dispatch manifests against expected artifact paths before allowing
synthesis.
