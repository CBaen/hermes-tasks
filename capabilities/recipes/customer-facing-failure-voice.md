---
id: customer-facing-failure-voice
name: Customer-Facing Failure Voice
schema_version: 2.0
level: recipe
maturity: candidate
scope: Machine-wide public/customer-facing failure copy across forms, checkout, payments, documents, portals, websites, and automations
currently_true: true
verification_level: 1
last_verified: 2026-05-08
evidence_quality: user_directive
successful_uses: 1
failed_uses: 0
regressions: 0
depends_on:
  - current-truth-needs-evidence
used_by:
  - loud-failure-customer-forms
tags:
  - copy
  - failures
  - customer-facing
  - fail-loud
  - voice
---

# Customer-Facing Failure Voice

Use this whenever a real person outside the build team sees a failure, warning,
blocked state, partial-success note, payment issue, form issue, document issue,
or retry prompt.

Computer-wide rule:

> Customer-facing failures must sound like a calm kindergarten teacher: warm,
> simple, specific, and safe. Backend failures must still fail loudly with
> precise evidence.

## Contract

Every customer-facing failure message must:

- name the snag in plain language;
- avoid blame, shame, panic, or technical jargon;
- say only what is true;
- give one clear next step;
- include a real retry/contact path when the customer cannot fix it alone;
- stay on brand for the project/client.

## Good Shape

Use patterns like:

- "Tiny snag: we could not save that just now. Please try once more, or call
  us at ..."
- "We have your request. One photo did not come through, so we made a note for
  the team to follow up."
- "Your payment came through. The final receipt is still being checked, and the
  team has a note to finish it."

## Do Not Show Customers

- stack traces, exception names, DocType names, integration labels, webhook
  language, or database details;
- "failed", "fatal", "invalid payload", "unauthorized", or "exception" unless
  there is no gentler accurate wording;
- false reassurance such as "all set" when a downstream step is incomplete;
- vague dead ends such as "Something went wrong" without a next step.

## Split The Surfaces

One failure can have two voices:

- Customer surface: gentle, accurate, actionable.
- Operator/developer surface: exact failure, record ID, route, field, stack,
  report row, verifier failure, and next repair action.

If both voices cannot be found in the implementation, the feature is not
finished.
