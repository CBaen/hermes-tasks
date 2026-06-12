---
id: approval-gated-account-page-automation
name: Approval-Gated Account Page Automation
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: logged-in browser account-page inspection and narrowly approved account actions from Banebook
currently_true: verified
last_verified: 2026-06-12
depends_on:
  - public-internet-access
  - local-brave-cdp-open-tabs
  - browser-protocol-page-control-and-typing
tags:
  - banebook
  - hermes
  - browser
  - cdp
  - account-pages
  - approval-gate
  - verification
---

# Approval-Gated Account Page Automation

## What it helps with

Use this when Uma needs to help with a logged-in account page that the user has opened, especially billing, hosting, domain, school, benefits, or other account workflows where public research is not enough.

This recipe is for protocol-level browser work: read the current page, identify the exact account/product/setting, prepare a safe action, get explicit approval for the external/account change, perform only that approved action, then verify the result.

## Required setup

- Use the user/live Brave CDP lane on `127.0.0.1:9222` when the user has already opened the logged-in page.
- Use public internet/DNS/official-source checks before touching account settings when the page affects a live domain, website, email, money, security, or public system.
- Prefer DOM/CDP reads and clicks over physical cursor/keyboard control.

## Procedure

1. **State the approval boundary before acting.**
   - Read-only inspection is allowed when the user asks for review.
   - Account changes, cancellations, renewals, security changes, payments, form submissions, sends, uploads, and final confirmations require explicit approval.

2. **Verify outside the account page first when possible.**
   - For domains/sites, check live DNS, MX, HTTP headers, RDAP/registrar, and hosting response before judging a subscription safe to retire.
   - Treat account dashboards as claims until checked against live service state or provider APIs.

3. **Target only the named scope.**
   - Identify the exact account, domain, site, product, subscription, or row before clicking.
   - Avoid broad account-wide cleanup when the user named only one domain/product.

4. **Summarize without dumping private data.**
   - Record product names, public domain names, statuses, and verification results.
   - Do not store raw emails, account IDs, card details, addresses, phone numbers, cookies, tokens, screenshots of sensitive pages, or raw browser/session dumps.

5. **Execute only after explicit approval.**
   - Repeat the approved action in narrow terms: which product/setting and what change.
   - Stop if the site asks for a broader action than approved.

6. **Verify through more than one signal when possible.**
   - Check the visible UI.
   - Check provider API/backend state when accessible through the page.
   - If a single-page app table or local cache stays stale after a success response, do not repeat the change blindly. Prefer backend/API renewal state and provider success notices, then tell the user the visible table may catch up after logout/login.

7. **Document durable inheritance without secrets.**
   - Put project/domain follow-ups in the project queue or handoff.
   - Put reusable pitfalls in lessons/capabilities.
   - Keep raw account/private material out of git and memory.

## Verified proof

Verified on 2026-06-12 during the `locallytwisted.com` vendor cleanup workflow:

- Public checks showed Cloudflare authoritative DNS, Cloudflare MX, and Frappe Cloud serving the live site.
- RDAP showed GoDaddy still appeared to be registrar for `locallytwisted.com`, with expiration `2027-05-19`; GoDaddy access remained blocked by EdgeSuite/504-style errors.
- Bluehost Billing Center showed two relevant products tied to `locallytwisted.com`: SiteLock Essentials and WordPress Basic Hosting.
- After explicit user approval, Uma completed Bluehost confirmation flows to turn off auto-renew for those two products.
- Bluehost showed processing/success notices.
- Bluehost Renewal Center API reported `AutoRenewOn=0`, `AutoRenewOff=1`, and WordPress Basic Hosting `autoRenew=false`.
- The visible Bluehost Angular table/cache still painted stale on-state switches after reload, so the result was reported as verified by Renewal Center API with a stale-UI caveat.

## Guardrails

- Never infer permission to cancel a registrar/domain renewal from the fact that DNS moved elsewhere. DNS authority, hosting, email routing, and registrar/ownership renewal are separate control planes.
- Do not cancel or close the registrar account for a domain until registration has transferred or the user explicitly chooses the registrar path.
- Do not re-click toggles or submit cancellation actions solely because a stale SPA table looks unchanged after a provider success response.
- Do not write account IDs, payment details, personal contact fields, private email bodies, auth/session details, or raw logs into capability cards, project docs, skills, or memory.

## Related collaboration boundary

The approval behavior follows the collaboration/autonomy principle at `../../capabilities-collaboration-autonomy/principles/standing-permission-tiers.md`: account changes and externally visible actions are not green-light technical actions; they need explicit user approval.
