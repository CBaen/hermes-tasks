---
id: organic-capabilities-framework-notes
name: Organic Capabilities Framework Notes
schema_version: 2.1
profile: foundation
level: recipe
maturity: kitchen
scope: Banebook shared capability framework design
currently_true: unknown
last_verified: 2026-05-07
evidence_quality: direct
successful_uses: 0
failed_uses: 0
regressions: 0
depends_on: []
used_by: []
tags:
  - capabilities
  - framework
  - kitchen
  - metadata
  - provenance
  - confidence
  - cooking-metaphor
---

# Organic Capabilities Framework Notes

Captured from Guiding Light on 2026-05-06.

## Core inspiration

Guiding Light wants to give back to the AI/coding-agent world by creating a framework for systems, capabilities, and reusable knowledge. The kitchen/cooking metaphor is not cosmetic; it is the organizing model.

Guiding Light has real-world systems experience: they once restructured a hospital network's HIPAA infrastructure after data management had been mishandled for six years. That experience matters because the capability framework is partly about making complex systems governable, traceable, and repairable.

## Metaphor stack

- **Atomic ingredients** - smallest reusable units; still carry metadata.
- **Ingredients** - composed from atomic ingredients, with their own metadata and references back down.
- **Recipes** - repeatable workflows made from ingredients.
- **Meals** - complete project shapes or larger coordinated workflows.
- **Feasts** - mature operating systems / multi-capability ecosystems.
- **Kitchen** - the test place where rough ideas are tried, tasted, adjusted, and either promoted or discarded.

## Metadata Guiding Light wants

Capabilities/items should be able to track:

- whether they were used;
- when they were used;
- where they were used;
- what evidence proves usage;
- confidence level;
- how much was actually read/used vs merely referenced;
- upvotes/downvotes or success/failure signals;
- relevance decay over time;
- last verification date;
- whether assumptions still stand.

## Important principle

Relevance does not stay true forever. Capability systems need decay and review, not just accumulation.

A capability that was useful once may become stale, harmful, or context-specific. The framework should make this visible.

## Current project use case

The Event Space Balloon Designer is a live proving ground:

- project-specific capabilities capture domain rules;
- failed subagent swarm becomes a failure/recipe capability;
- balloon physics research becomes construction grammar and validation capability;
- agent roles consume capabilities rather than loose chat context;
- later, reusable pieces can be promoted to workspace/global capabilities.

## Guardrail

This broader framework idea is parked in the idea incubator unless Guiding Light explicitly promotes it. However, the balloon project can safely use and test the framework because it directly improves current paid work.
