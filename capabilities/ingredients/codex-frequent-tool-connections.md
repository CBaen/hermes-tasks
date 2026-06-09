---
id: codex-frequent-tool-connections
name: Codex Frequent Tool Connections
schema_version: 2.1
profile: foundation
level: ingredient
maturity: candidate
scope: Codex-accessible app connectors and local CLI identities; Wardenclyffe checks preserved as migration evidence
currently_true: unknown
last_verified: 2026-05-14
evidence_quality: direct
tags:
  - codex
  - connectors
  - github
  - gmail
  - canva
  - vercel
  - cloudflare
  - stripe
  - frappe-cloud
  - hermes
---

# Codex Frequent Tool Connections

Use this when a task depends on Guiding Light's common external tools and you
need to know which route is already usable from Codex.

Banebook migration note: the verified checks below were captured on
Wardenclyffe on 2026-05-14 unless a line says otherwise. Treat them as
migration evidence until the same connector or CLI is rechecked on Banebook.
OpenClaw is not a current default. `hermes` was not found on Banebook during
the 2026-06-08 shared-root migration edit.

## Wardenclyffe Verification Evidence

- Codex CLI account: `codex login status` reports `Logged in using ChatGPT`.
- Google app connectors: Gmail, Calendar, and Contacts profile checks work for
  `cameronbpaul@gmail.com`.
- GitHub app connector: authenticated as `CBaen`; installed account is `CBaen`.
- GitHub CLI: `gh auth status` is logged in as `CBaen` with `repo`,
  `workflow`, `read:org`, and `gist` scopes.
- Canva app connector: brand-kit lookup works. Verified brand kits were
  `LoomTem` and `Tesla Mandela Effects`.
- Vercel app connector: team lookup works for `cameron-built`; project listing
  works for that team.
- Stripe CLI: `stripe whoami` worked for `Built by Cameron` on device
  `Wardenclyffe`; test and live mode keys were available and expiring
  2026-06-08 at verification time. Recheck on Banebook before relying on it.
- Cloudflare MCP: `cloudflare-api` is enabled as OAuth-backed
  `streamable_http` at `https://mcp.cloudflare.com/mcp`. On 2026-05-14,
  stale saved OAuth state was cleared with `codex mcp logout cloudflare-api`
  and repaired with `codex mcp login cloudflare-api`.
- Wrangler: `npx wrangler whoami` works after `npx wrangler logout` and
  `npx wrangler login`; verified account email was `locallytwisted@gmail.com`.
- Frappe Cloud public route health for Locally Twisted: on 2026-05-14,
  `https://locallytwisted.com` returned HTTP 200 with `Server: Frappe Cloud`,
  `/api/method/frappe.ping` returned `{"message":"pong"}`, and the project
  Cloudflare dynamic-route gate passed. This is public-route proof, not direct
  dashboard/API control.
- Hermes CLI: on Wardenclyffe, `hermes status` worked with provider
  `OpenAI Codex`, model `gpt-5.5`, gateway stopped, and zero active sessions.
  OpenClaw was removed on 2026-05-14; `openclaw` no longer resolves and
  `.openclaw` no longer exists. Recheck Hermes on Banebook before using it as a
  current route.

## Config State

Banebook config paths are:

- Active runtime config: `/home/guidingl/.codex/config.toml`
- Source config: `/home/guidingl/codex-framework/config.toml`

The older Wardenclyffe runtime config at `C:\Users\baenb\.codex\config.toml`
was synced from
`C:\Users\baenb\projects\codex-framework-backup\config.toml` on 2026-05-14.
That is historical evidence, not Banebook proof. Recheck the Banebook config
before claiming the current plugin surfaces are enabled:

- `github@openai-curated`
- `gmail@openai-curated`
- `canva@openai-curated`
- `cloudflare@openai-curated`
- `stripe@openai-curated`
- `vercel@openai-curated`

Plugin packages are skill/documentation surfaces. App connector tools are a
separate live surface exposed by the current Codex session.

## Known Gaps

- Cloudflare app account tools were not exposed by live tool discovery in this
  session, but the official Cloudflare MCP and Wrangler CLI are authenticated.
- Stripe app account tools were not exposed by live tool discovery in this
  session. Use the authenticated Stripe CLI only for tasks that genuinely need
  it, and never print keys or config files.
- Stripe remote MCP at `https://mcp.stripe.com` was tested on 2026-05-14.
  Codex registered it, but `codex mcp login stripe` timed out and `codex mcp
  list` reported `Unsupported`; leaving it registered caused every new
  `codex exec` run to emit a Stripe auth warning. It was removed from active and
  canonical config. Use Stripe CLI unless a future Codex version supports Stripe
  OAuth or Guiding Light explicitly approves a restricted-key MCP setup.
- Vercel app connector works, but `vercel whoami` hung twice on 2026-05-14 and
  left `node ... vercel/dist/vc.js whoami` processes that had to be stopped.
  Prefer the Vercel app connector for account/project checks until the CLI is
  repaired.
- Frappe Cloud dashboard/API tools were not exposed by live tool discovery in
  this session. Host inspection found no direct `fcloud`/Frappe Cloud CLI, no
  host `bench`, and no Frappe Cloud environment variables. Use project-specific
  runbooks and authenticated dashboard/SSH/browser/API paths before claiming
  management control.

## Safety Rules

- Do not read email bodies, calendar event details, contacts, Canva designs, or
  repository contents merely to prove a connection. Use profile/team/metadata
  checks for health checks.
- Do not send Gmail messages or commit Canva editing transactions without
  explicit user approval for the specific outgoing change.
- Do not run Cloudflare browser login, Vercel browser login, or any desktop
  auth flow that can steal focus unless Guiding Light explicitly approves it.
- Do not treat a public Frappe Cloud route, DNS record, or SSH key preflight as
  proof that Codex can mutate the Frappe Cloud dashboard or API.
- Do not read or print OAuth files, API keys, Stripe config files, Wrangler
  auth logs, browser cookies, or session tokens.
