---
id: loud-failure-customer-forms
name: Loud-Failure Customer Forms
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: customer-facing forms across frameworks
currently_true: unknown
last_verified: 2026-05-07
tags:
  - forms
  - customer-pipeline
  - deploy-gates
  - Claude-migration
  - scar-tissue
---

## What it does

Treats customer forms as critical-path business infrastructure: every submission must visibly succeed or visibly fail, never silently disappear.

Adapted from Claude's `form-integrity` skill.

## When to reach for it

Use before building, editing, reviewing, debugging, or deploying any customer-facing form:

- contact forms;
- booking/request forms;
- CRM/lead forms;
- newsletter/signup forms;
- payment-intent/request forms;
- any form whose failure could lose a customer or lead.

## How to use it

1. Identify every user-facing submit path and downstream business effect.
2. Require all three detection layers:
   - visible client confirmation or visible error within a short window;
   - server-side attempt/success/failure logging;
   - deploy/staging smoke test that blocks promotion when forms fail.
3. Smoke-test the full path:
   - fill realistic required fields;
   - submit;
   - capture console/page errors;
   - verify network response;
   - verify visible confirmation;
   - verify downstream record/notification where possible.
4. Test the test: intentionally break a staging/sandbox form and confirm the gate screams.
5. For framework-specific forms, inspect the current framework source/working reference form before changing structure.
6. Never accept “lead created somewhere” as enough if the customer saw nothing.

## What it depends on

- [No Bare Claims](../principles/no-bare-claims.md)
- [Conversational UAT Verification](conversational-uat-verification.md)
- [Codebase-Verified Docs Update](codebase-verified-docs-update.md)

## Failure modes

- Form posts successfully but user sees no confirmation.
- Widget crashes and browser falls back to plain HTML POST.
- Defense only patches XHR while framework uses fetch, or vice versa.
- Success URL/hash does not match a DOM anchor/modal id.
- Smoke test checks only record creation and misses notification/downstream failure.
- Logger/smoke test itself fails silently.

## Evidence

- `C:/Users/baenb/.claude/skills/form-integrity/SKILL.md:10-18` states forms must visibly confirm or visibly error; silent nothing is unacceptable because it loses customers, pipeline, and trust.
- `C:/Users/baenb/.claude/skills/form-integrity/SKILL.md:34-57` defines the three required detection layers: visible confirmation, server logging, and deploy-gate smoke test.
- `C:/Users/baenb/.claude/skills/form-integrity/SKILL.md:60-145` documents production traps including widget crash fallback, XHR/fetch mismatch, entity double-encoding, and success hash mismatch.
