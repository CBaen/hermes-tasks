# Safety Contract: <short name>

## Change

Describe the exact change or release decision this contract guards.

## Bad Thing To Block

Name the unsafe, unapproved, spammy, broken, privacy-sensitive, or false-success
path that must fail loudly.

## Good Thing To Preserve

Name the already-approved behavior that must continue working after the guard is
added.

## Deferred Or Out Of Scope

Name anything intentionally not solved by this contract. Use `None.` only when
the contract is truly complete for this slice.

## Negative Guard

- Verifier: `<command, script, browser path, review check, or evidence path>`
- Expected result: `<the unsafe path is blocked loudly and no false success is shown>`

## Positive Guard

- Verifier: `<command, script, browser path, review check, or evidence path>`
- Expected result: `<the known-good customer/operator behavior still works>`

## Evidence

- Evidence path: `<workstream, test report, screenshot folder, evidence ledger, or verifier output>`

## Owner

Name the accountable agent, project, owner, or role.

## Promotion Rule

State when this contract can be treated as reusable, verified, or no longer
blocking.

## Rollback / Revalidation Path

State how to undo, re-run, or downgrade the guarded behavior if either guard
fails later.
