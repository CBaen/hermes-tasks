# Hermes Adapter

Hermes can use shared capability roots. Hermes does not own them.

## Canonical Roots

- System/user root: `/home/guidingl/capabilities/INDEX.md`
- Hermes purpose root: `/home/guidingl/capabilities-hermes/INDEX.md`
- Source package: `/home/guidingl/projects/capabilities-framework/`
- Project roots: `<project>/capabilities/INDEX.md`

`/home/guidingl/.hermes/profiles/banebook/capabilities` may point to
`/home/guidingl/capabilities-hermes` as a runtime convenience. That link is an
entrypoint, not the canonical source.

## How Hermes Should Use Capabilities

1. Read the Banebook Hermes profile policy before acting on local files,
   accounts, browser sessions, finance, web3, or Wardenclyffe.
2. Prefer the most specific visible root for the task:
   - use `/home/guidingl/capabilities-hermes` for Hermes-specific execution
     rules;
   - use `/home/guidingl/capabilities` for shared user/system rules;
   - use a project capability root for project-specific work.
3. Treat browser/CDP control as preparation and navigation authority, not final
   authority to submit forms, place orders, sign transactions, change account
   security, or send messages.
4. Keep approval gates close to the final irreversible action.
5. Treat conversation memory, logs, session files, auth stores, browser state,
   wallet state, and API keys as runtime or sensitive data. Do not copy them
   into capability roots.
6. When a Hermes-specific rule proves reusable, promote it into the visible
   Hermes purpose root or shared root after review.

## What Belongs In Hermes Runtime Folders

- Hermes profile config, sessions, logs, caches, profile skills, memories, and
  runtime state.
- Small adapter links that help Hermes find visible capability roots.

Do not put canonical shared capability truth under `.hermes` just because
Hermes is the current runtime.

## Current Banebook Notes

- Hermes is active on Banebook and authenticated with OpenAI Codex OAuth.
- Hermes uses Brave/CDP for browser automation on the configured local endpoint.
- The profile can see Codex framework skills through explicit external
  directories, but the durable skill source remains
  `/home/guidingl/codex-framework/skills`.
- OpenClaw-era procedures have been translated into Codex/framework skills or
  shared capabilities where still useful. Do not reopen OpenClaw local install
  paths unless Guiding Light explicitly asks.
