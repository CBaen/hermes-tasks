---
id: safety-contracts
name: Safety Contracts
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: systemwide capability root, agency release gates, and project verifier planning
currently_true: unknown
last_verified: 2026-05-17
tags:
  - safety contract
  - positive guard
  - negative guard
  - regression guard
  - release gate
  - fail loud
---

## What it does

Turns a lesson, regression, or risky change into a small written contract that
names both sides of safety: the bad path to block and the known-good path to
preserve.

## When to reach for it

Use this before changing a guard, verifier, release gate, form, payment path,
email path, permission rule, spam filter, media cascade, customer-facing UI, or
other workflow where "block the bad thing" could accidentally remove approved
behavior.

Also use it after an incident or Failure Recipe when the next agent needs a
repeatable guard instead of another warning note.

## How to use it

1. Create a safety contract artifact before the risky implementation or release
   decision. Use `templates/safety-contract.template.md` from this root or copy
   the same sections into a project workstream.
2. Fill in the change in plain language.
3. Fill in `Bad Thing To Block` with the unsafe, unapproved, spammy, broken, or
   false-success path.
4. Fill in `Good Thing To Preserve` with the behavior that already works and
   must not disappear.
5. Add a `Negative Guard` with a `Verifier:` and `Expected result:`.
6. Add a `Positive Guard` with a `Verifier:` and `Expected result:`.
7. Add the evidence path where the verifier output, screenshot, report,
   workstream note, or evidence ledger row will live.
8. Run the validator before using the contract as a release or review gate:

```bash
python /home/guidingl/capabilities/tools/safety_contract_gate.py path/to/safety-contract.md --json
```

9. Link the passing contract from the relevant queue, handoff, Failure Recipe,
   release gate, or project capability card.
10. If either guard cannot be verified yet, mark the release blocked or write an
    approved deferral with owner, scope, rollback, and follow-up date.

## What it depends on

- [Contracts As Capabilities](contracts-as-capabilities.md)
- [Capability Evidence And Promotion](capability-evidence-and-promotion.md)
- [Failure Cascade And Watch Status](failure-cascade-and-watch-status.md)

## Failure modes

- A negative guard without a positive guard creates over-blocking: the system
  stops the bad path by deleting useful behavior.
- A positive guard that says only "make sure it still works" is not a guard.
  It needs a verifier and expected result.
- A human approval note without an artifact path cannot teach the next agent.
- A safety contract that is not linked from the release, queue, or handoff will
  not be found when it matters.

## Examples

- Spam filter: block obvious sales solicitation while preserving real customer
  inquiries about events, pickup, delivery, and product questions.
- Media review gate: hold unclassified uploaded photos while preserving already
  approved Item image and variant media behavior.
- Permission gate: block marketing-review users from sensitive ERP records
  while preserving Administrator, migration, and bench operations.

## Rollback / revalidation path

If a safety contract fails, treat the guarded change as blocked. Fix the
contract or the implementation, rerun both verifiers, and record the failed
class in a Failure Recipe if it is recurring, high-cost, or likely to be
repeated.
