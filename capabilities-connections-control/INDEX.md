# Hermes Tasks Connections And Control Capabilities

## Root Label

- Purpose: Reusable capabilities for how Uma/Hermes connects to, reads from, writes to, and controls internal and external systems from Banebook.
- Belongs here: Browser/CDP access, agent-only browsing, messaging and notification channels, local hardware/control surfaces, Wardenclyffe bridges, API/MCP integrations, account-page interaction patterns, and connection health checks.
- Does not belong here: Secrets, passwords, OAuth tokens, raw cookies, browser profiles, raw session dumps, wallet keys, client data, or one-off account facts that belong in a workstream or private approved note.
- Related roots:
  - `capabilities/` - baseline project operating capabilities
  - `capabilities-collaboration-autonomy/` - standing permission and approval-boundary capabilities
  - `capabilities-agent-infrastructure/` - Hermes profile/repo/runtime infrastructure capabilities
  - `/home/guidingl/.hermes/profiles/banebook/capabilities` - Banebook Hermes runtime guidance

## How To Use This Root

1. Start here when a task depends on whether Uma can access, inspect, control, or automate a system.
2. Prefer protocol/API/browser-level control over desktop-coordinate control.
3. Keep external side effects behind approval gates: submissions, sends, uploads, account changes, payments, signatures, deployments, and destructive actions.
4. Record connection methods as reusable capabilities only after they are verified on Banebook.
5. Store secrets in the proper secret store or user-managed account flow, never in this root.

## Principles

- Add stable connection/control rules here after they are proven useful.

## Recipes

- [Agent-Only Browser Lane](recipes/agent-only-browser-lane.md) - verified separate Brave profile on port `9223` for independent Uma browsing without cluttering the user's live tabs.

## Ingredients

- [Public Internet Access](ingredients/public-internet-access.md) - verified public HTTPS retrieval for research and official-source checks.
- [Local Brave CDP Open Tabs](ingredients/local-brave-cdp-open-tabs.md) - verified open-tab access through Brave CDP on Banebook.
- [Browser Protocol Page Control And Typing](ingredients/browser-protocol-page-control-and-typing.md) - verified DOM/CDP reading, focusing, and text entry without physical keyboard or mouse takeover.
- [Desktop Input Control Boundary](ingredients/desktop-input-control-boundary.md) - verified desktop input tools exist, with last-resort safety boundary.

## Meals

- [Internet And Browser Control Stack](meals/internet-and-browser-control-stack.md) - current composed capability set for internet research plus browser read/write/control on Banebook.

## Kitchen

- Use `kitchen/` for rough connection/control notes that are not yet trusted capabilities.

## Failures

- Use `failures/` for connection/control mistakes that should not be repeated.

## Evidence And Registry

- `evidence/` - compact evidence events for verified connection/control changes.
- `registry/` - generated or curated indexes for this root when needed.
