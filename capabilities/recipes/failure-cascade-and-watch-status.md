---
id: failure-cascade-and-watch-status
name: Failure Cascade And Watch Status
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: capability framework
currently_true: unknown
last_verified: 2026-05-07
tags:
  - cascade
  - watch status
  - dependency
  - regression
  - revalidation
---

## What it does

Defines what to do when a composed capability fails. The failure may belong to
the meal, a recipe, an ingredient, or a lower atomic behavior.

## When to reach for it

Use this when a meal, feast, contract, recipe, or dependency-backed card fails,
regresses, or becomes stale.

## How to use it

1. Identify the failing card and the observed result.
2. Check `depends_on` and test the layer below before rewriting the top layer.
3. Mark the failing or affected card with an appropriate watch status when it
   uses composition/cascade tracking:
   - `watch`: affected by a possible dependency issue.
   - `failed`: directly failed or caused a regression.
   - `stale`: confidence expired because external state drifted.
   - `probation`: repaired or reconnected enough to retry, but not greenlit.
   - `revalidating`: under active retest.
   - `clear`: revalidated and safe within scope.
4. Check `used_by` and put downstream cards on watch when they inherit the risk.
5. Record date, result, confidence, and rollback or revalidation path.
6. Move repaired dependency chains to probation instead of greenlighting them
   immediately.
7. Restore confidence only after the lower layer and affected dependents pass
   their relevant checks and the affected capability has three subsequent
   evidence-backed successful uses.

## What it depends on

- [Capability Evolution Gates](../principles/capability-evolution-gates.md)
- [Probationary Revalidation](probationary-revalidation.md)

## Failure modes

- Fixing the visible meal while the ingredient below remains broken.
- Leaving downstream cards at normal confidence after a dependency failure.
- Clearing watch status because prose was updated instead of because behavior
  was revalidated.
- Creating a permanent scraps pile for broken attempts instead of keeping only
  useful failure receipts.
