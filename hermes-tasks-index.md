# Hermes Tasks Index

Use this for references, research, source maps, and durable pointers. Do not use it as the active queue.

## Source Of Truth

- `README.md`
- `SOURCE-OF-TRUTH.md`
- `HANDOFF.md`
- `LESSONS-LEARNED.md`
- `GLOBAL-DECISIONS.md`
- `AGENTS.md`
- `PROJECT-STATUS.md`
- `hermes-tasks-queue.md`
- `hermes-tasks-decisions.md`
- `agent-lanes/BOARD.md`
- `agent-lanes/connections-control-HANDOFF.md`
- `verifier-manifest.json`
- `capabilities/INDEX.md`
- `capabilities-connections-control/INDEX.md`
- `capabilities-collaboration-autonomy/INDEX.md`
- `capabilities-agent-infrastructure/INDEX.md`

## Start Here

1. Read `AGENTS.md`.
2. Read `SOURCE-OF-TRUTH.md`.
3. Read `PROJECT-STATUS.md`.
4. Read `HANDOFF.md`.
5. Read `hermes-tasks-queue.md`, `hermes-tasks-decisions.md`, and `GLOBAL-DECISIONS.md`.
6. Open only the specific capability root needed for the task.

## Capability Roots

- Baseline capability root: `capabilities/INDEX.md`.
- Connection/control root: `capabilities-connections-control/INDEX.md`.
- Collaboration/autonomy root: `capabilities-collaboration-autonomy/INDEX.md`.
- Agent infrastructure root: `capabilities-agent-infrastructure/INDEX.md`.
- Cross-project pointer note outside repo: `/home/guidingl/Uma/HERMES-MAIN-PROJECT.md`.

## Agent Coordination

- Lane board: `agent-lanes/BOARD.md`
- Lane handoff template: `agent-lanes/LANE-HANDOFF.template.md`
- Connections/control lane handoff: `agent-lanes/connections-control-HANDOFF.md`

## Locally Twisted Service Map

Verified on 2026-06-12 for `locallytwisted.com`:

- Cloudflare is authoritative DNS.
- Cloudflare MX is present.
- Frappe Cloud serves the live site.
- Bluehost auto-renew was disabled after explicit user approval for SiteLock Essentials and WordPress Basic Hosting tied to the domain; Renewal Center/API showed `AutoRenewOn=0`, `AutoRenewOff=1`, and WordPress Basic Hosting `autoRenew=false`.
- GoDaddy still appeared to be registrar with expiration `2027-05-19`; access was blocked by GoDaddy/Akamai EdgeSuite/504-style errors.

Pointers:

- Handoff detail: `HANDOFF.md`
- Queue follow-up: `hermes-tasks-queue.md`
- Project decision: `hermes-tasks-decisions.md`
- Reusable workflow: `capabilities-connections-control/recipes/approval-gated-account-page-automation.md`

## Runtime References

- Active Hermes profile: `/home/guidingl/.hermes/profiles/banebook/`
- Active Hermes SOUL: `/home/guidingl/.hermes/profiles/banebook/SOUL.md`
- Wardenclyffe always-on Hermes runtime: `/home/guidingl/.hermes/hermes-agent` on `wardenclyffe`; gateway enabled/running as the `guidingl` user service.
- Wardenclyffe worker-lane rules: `capabilities-collaboration-autonomy/recipes/wardenclyffe-uma-worker-lanes-v1.md`
- Wardenclyffe Codex/Hermes auth boundary: `capabilities-agent-infrastructure/ingredients/wardenclyffe-codex-hermes-auth-boundary.md`
- User/live Brave CDP: `http://127.0.0.1:9222`
- Agent-only Brave CDP: `http://127.0.0.1:9223`
- Agent-only profile: `/home/guidingl/.local/share/hermes/agent-brave-profile`
- Agent browser helpers: `hermes-agent-brave`, `hermes-agent-brave-status`, `hermes-agent-brave-stop`, `hermes-agent-cdp`

## Technical References

- Source-of-truth parity check: `python tools/check_source_of_truth_parity.py`
- Project shape check: `python /home/guidingl/projects/capabilities-framework/tools/validate_project_shape.py --project /home/guidingl/projects/hermes-tasks --project-slug hermes-tasks`
- Baseline capability graph check: `python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities --json`
- Connections/control graph check: `python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-connections-control --json`
- Collaboration/autonomy graph check: `python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-collaboration-autonomy --json`
- Agent infrastructure graph check: `python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-agent-infrastructure --json`
- Agent browser status check: `hermes-agent-brave-status`
- Agent browser page-state check: `hermes-agent-cdp eval '({title: document.title, url: location.href})'`

## Artifacts

- `artifacts/libreoffice/cheese-poem.odt` - harmless LibreOffice Writer/ODT verification artifact.
- `artifacts/libreoffice/README.md` - artifact purpose and boundaries.
- `artifacts/worker-smoke/wardenclyffe-codex-worker-smoke.md` - Wardenclyffe Codex local-only worker smoke proof, result PASS.

## External Links

- GitHub target requested by user: `https://github.com/CBaen/hermes-tasks`
- Hermes docs used for browser verification: `https://hermes-agent.nousresearch.com/docs/user-guide/features/browser`

## Messaging Artifacts

- `artifacts/messaging/hermes-slack-manifest.json` - generated Slack app manifest, no tokens.
- `artifacts/messaging/messaging-options-2026-06-11.md` - current WhatsApp/Signal/Slack setup assessment.

- Wardenclyffe Hermes WebUI tunnel: remote service `hermes-dashboard.service` on `127.0.0.1:9119`, Banebook helper `wardenclyffe-hermes-webui`, local URL `http://127.0.0.1:9129`, capability `capabilities-connections-control/ingredients/wardenclyffe-hermes-webui-tunnel.md` (verified 2026-06-13T20:04:31-06:00).
## Bidirectional / Mobile Coordination

- `capabilities-collaboration-autonomy/recipes/banebook-wardenclyffe-bidirectional-agent-coordination.md` - cross-machine worker route pattern.
- `capabilities-connections-control/kitchen/samsung-s24-tailscale-access-options-2026-06-14.md` - mobile peer inventory and access options.
## 2026-06-14T13:29:12-06:00 Reverse SSH hardening / S24 online

- `capabilities-connections-control/ingredients/wardenclyffe-to-banebook-ssh-access.md` - hardened reverse SSH key state.
- `capabilities-connections-control/kitchen/samsung-s24-tailscale-access-options-2026-06-14.md` - expanded explanation of Android access options and ADB/scrcpy.
