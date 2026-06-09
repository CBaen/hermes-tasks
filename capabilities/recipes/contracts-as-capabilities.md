---
id: contracts-as-capabilities
name: Contracts As Capabilities
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: machine-wide Codex capability framework
currently_true: unknown
last_verified: 2026-05-07
tags:
  - contract
  - reusable rule
  - verification
  - UI
  - business process
---

## What it does

Turns reusable UI, business, process, or integration rules into capability
cards with explicit verification instead of leaving them as scattered prose.

## When to reach for it

Use this when the same rule needs to shape multiple pages, projects, clients,
agents, or workflows.

## How to use it

1. Name the contract in plain language.
2. State the scope where it applies.
3. Describe the observable behavior the contract protects.
4. Add the verification path: test, browser check, schema check, business
   review, or file inspection.
5. Record dependencies that would break the contract if they changed.
6. Keep it foundation while it routes behavior. Upgrade to governed when the
   contract becomes launch-critical, cross-project, or repeatedly reused.
7. Add a rollback or revalidation path before changing the contract.

## What it depends on

- [Capability Evolution Gates](../principles/capability-evolution-gates.md)

## Failure modes

- A contract without verification becomes a preference.
- A contract copied between projects without scope becomes false certainty.
- Changing contract wording without rollback makes downstream work hard to
  audit.
