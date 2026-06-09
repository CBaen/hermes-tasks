---
id: terminology-vocabulary-coach
name: Terminology Vocabulary Coach
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: Guiding Light technical vocabulary support
currently_true: unknown
last_verified: 2026-05-07
tags:
  - vocabulary
  - terminology
  - teaching
  - translation layer
  - ADHD support
---

## What it does

Turns repeated terminology mismatches into useful teaching moments and a durable glossary, without interrupting momentum or shaming Guiding Light.

## When to reach for it

Use when Guiding Light uses a likely wrong/mixed technical term, a voice-to-text artifact, a metaphor that maps to a precise engineering concept, or asks for language/terminology coaching.

## How to use it

1. Preserve momentum first. Do not derail the task for a vocabulary lecture.
2. Infer likely voice-to-text artifacts from context. Example: `frap` means Frappe in current project context.
3. When useful, give a tiny correction in this shape:
   - "Term note: what you're describing is usually called **X**. Your phrase maps to **Y** because..."
4. Capture repeated/high-value terms in a glossary or capability note.
5. Prefer plain-English translations:
   - user phrase;
   - engineering term;
   - why it matters;
   - where it applies;
   - example from current work.
6. Do not correct every wording error. Correct terms that improve agency, searchability, collaboration with agents, or communication with developers/clients.
7. Treat metaphors as useful concept maps, not mistakes.

## What it depends on

- [Agent-Centered Infrastructure](../principles/agent-centered-infrastructure.md)
- [Capabilities Should Enhance, Not Become Chores](../principles/capabilities-should-enhance-not-become-chores.md)

## Failure modes

- Pedantry that spends cognitive battery.
- Letting wrong terms harden into project docs when the correct term matters for search or implementation.
- Flattening Guiding Light's metaphors instead of translating them into useful technical handles.
