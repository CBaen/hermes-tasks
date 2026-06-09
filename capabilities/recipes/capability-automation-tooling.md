---
id: capability-automation-tooling
name: Capability Automation Tooling
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: capability framework projects
currently_true: unknown
last_verified: 2026-05-07
tags:
  - automation
  - scaffold
  - validation
  - evidence
  - handoff
---

## What it does

Uses the standard-library command-line tools in `tools/` to scaffold projects,
validate capability roots, record evidence, gate promotion, summarize status,
and export handoff packets.

## When to reach for it

Use this before trusting framework prose for a new project shape, after editing
capability cards, before promoting a capability, or when preparing a fresh
agent handoff.

## How to use it

From the framework source package:

```bash
cd /home/guidingl/projects/capabilities-framework
python tools/scaffold_project.py --target <project> --name "<Project Name>" --project-slug <project>
python tools/validate_project_shape.py --project <project>
python tools/validate_capability_graph.py --root <project>/capabilities
python tools/capability_registry.py --root <project>/capabilities --write-registry
python tools/capability_report.py --root <project>/capabilities
python tools/handoff_export.py --project <project> --root <project>/capabilities --verification-command "<exact command>"
```

For evidence-backed trust changes:

```bash
cd /home/guidingl/projects/capabilities-framework
python tools/capability_event.py --root /home/guidingl/capabilities --capability-id <id> --event use --result "<result>" --verification "<command or check>" --confidence 2 --rollback "<revalidation path>" --update-card
python tools/capability_gate.py --root /home/guidingl/capabilities --capability-id <id> --action promote
python tools/capability_gate.py --root /home/guidingl/capabilities --capability-id <id> --action clear-probation
```

For dependency maps, failure propagation, and learning-review packages:

```bash
cd /home/guidingl/projects/capabilities-framework
python tools/capability_dependency_report.py --root /home/guidingl/capabilities --json
python tools/capability_dependency_report.py --root /home/guidingl/capabilities --related-root shared=/home/guidingl/capabilities --json
python tools/capability_failure_cascade.py --root /home/guidingl/capabilities --capability-id <id> --event failure --json
python tools/learning_candidate_gate.py --package <candidate-package> --json
python tools/capability_maintenance_review.py --root shared=/home/guidingl/capabilities --no-write --json
```

Use root-qualified dependency refs such as `shared::capability-id` when a card
depends on another capability root. Use the failure cascade command as a
dry-run first; add `--apply` only after the affected watch-status changes are
reviewed. Learning candidate packages stay blocked until
`promotion-review.json` records target root, reviewer, privacy gates,
evidence, rollback, and dependency/watch metadata.
Use the maintenance review as the scheduled steward. It proposes downgrades,
failure cascades, replacement searches, backlink repairs, recipe tests, and
cross-root collaborations; it does not apply any of them. The steward discovers
visible active roots by default, including system, purpose, agency, and project
roots, while skipping runtime adapters and the legacy backup root. Its action
ledger is a work-packet queue: each action includes an id, priority, owner role,
target root/card, write scope, next safe step, evidence requirement, acceptance
criteria, approval gate, `cwd`, absolute tool commands, read-only validation
commands, and separate post-approval commands. Scheduled agents may only run
read-only validation commands when `can_autorun` is true. Use `--no-write
--json` only when a reviewer needs a stdout-only dry inspection.

Use `--json` when another tool or agent needs machine-readable output.

## What it depends on

- [Capability Registry Generation](capability-registry-generation.md) - compact retrieval index.
- [Capability Evidence And Promotion](capability-evidence-and-promotion.md) - evidence and promotion rules.
- [Probationary Revalidation](probationary-revalidation.md) - three-success rule for repaired chains.

## Failure modes

- Automation output is evidence, not proof of live business behavior.
- A successful shape check does not mean a project is complete.
- `capability_gate.py` refuses promotion when evidence is missing, dependencies
  are failed/stale/probation, regressions are open, or rollback/revalidation is
  absent.
- `learning_candidate_gate.py` refuses packages that skip review, privacy,
  target-root, evidence, rollback, or dependency/watch metadata.
- `capability_failure_cascade.py` is a dry-run unless `--apply` is present.

## Rollback / revalidation path

Re-run the exact command that produced the claim. If a tool result conflicts
with current files, treat the tool output as stale and re-run after regenerating
the registry or evidence ledger.
