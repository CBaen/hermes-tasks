---
id: progressive-framework-profiles
name: Progressive Framework Profiles
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: machine-wide Codex capability framework
currently_true: unknown
last_verified: 2026-05-07
tags:
  - foundation
  - governed
  - composition
  - cascade
  - profile
---

## What it does

Explains when to keep a capability lightweight and when to upgrade it into
governed, composition, or cascade tracking.

## When to reach for it

Use this when creating a capability, retrofitting an old card, or deciding
whether a note deserves evidence counters or dependency watch fields.

## How to use it

1. Start in `kitchen/` when the idea is still loose.
2. Promote to `profile: foundation` when the note has reusable shape and helps
   routing or execution.
3. Upgrade to `profile: governed` when the card is reused, promoted, or asked to
   carry confidence across sessions or projects.
4. Upgrade to `profile: composition` when the card depends on other
   capabilities and downstream work inherits that risk.
5. Use `profile: cascade` when handling a failure that requires retesting lower
   layers and putting affected dependents on watch.
6. Downgrade, deprecate, or move back to `kitchen/` when evidence is stale,
   scope changes, or maintenance cost outweighs usefulness.

## What it depends on

- [Capabilities Should Enhance, Not Become Chores](../principles/capabilities-should-enhance-not-become-chores.md)
- [Capability Evolution Gates](../principles/capability-evolution-gates.md)

## Failure modes

- Starting every card as governed creates overhead before value.
- Keeping repeated high-risk work at foundation hides confidence and dependency
  questions.
- Leaving a failed composition at normal confidence lets inherited risk spread.
