# Hermes Tasks Handoff

TS:2026-06-12T16:26:51-06:00 | Check:Locally Twisted vendor cleanup inheritance and capability update | Confidence:high

## Current state

- Repo: `/home/guidingl/projects/hermes-tasks`
- Branch: `main` tracking `origin/main`
- Remote: `https://github.com/CBaen/hermes-tasks`
- Source-of-truth entrypoint: `SOURCE-OF-TRUTH.md`
- Runtime/profile state remains outside this repo.

## What changed this continuation

1. Identified stale timestamp/status drift in `PROJECT-STATUS.md`, `HANDOFF.md`, and `agent-lanes/BOARD.md` after the publish cleanup.
2. Added `SOURCE-OF-TRUTH.md` with authority order, timestamp contract, parity rule, and self-referential commit rule.
3. Added `tools/check_source_of_truth_parity.py` as a lightweight parity verifier.
4. Added `capabilities-agent-infrastructure/principles/source-of-truth-timestamp-parity.md`.
5. Verified messaging is not ready: no connected delivery targets discovered.
6. Verified Wardenclyffe bridge by absolute helper path:
   - `/home/guidingl/bin/wardenclyffe-status`
   - Tailscale ping and SSH succeeded.
   - Current target is `WARDENCLYFFE` running `Linux 7.0.0-14-generic x86_64`.
   - `/home/guidingl/bin/wardenclyffe-ps` is retired and says to use SSH/Linux commands.
7. Added `capabilities-connections-control/ingredients/wardenclyffe-kubuntu-ssh-bridge.md`.
8. Verified and documented the Hermes terminal PATH bridge so helper commands resolve by name in new terminal calls.


## 2026-06-11T22:37:43-06:00 continuation

- Followed Wardenclyffe handoff `agent-coordination/wardenclyffe-kubuntu-restore/handoffs/banebook-ssh-unblock-2026-06-11.md`.
- Added only the exact verified Wardenclyffe public key to Banebook `/home/guidingl/.ssh/authorized_keys`; fingerprint `SHA256:Cl5SYra87E5eyA/cy4PWPDAj1aoYm9HmxYLU0hhzmGM`.
- Wardenclyffe-side `ssh -o BatchMode=yes banebook` verification succeeded and returned `BANEBOOK`, `guidingl`, and expected Codex framework skills.
- Regenerated and validated Slack manifest at `artifacts/messaging/hermes-slack-manifest.json`.
- Messaging target discovery still finds no connected targets; Slack/WhatsApp/Signal require user-side account linking before delivery works.

## 2026-06-12T16:26:51-06:00 continuation - Locally Twisted vendor cleanup

- Reviewed user-open Bluehost, Locally Twisted Gmail, and GoDaddy tabs through the user/live Brave CDP lane after the user asked Uma to confirm cancellation safety.
- Verified public `locallytwisted.com` service posture before account changes:
  - Cloudflare is authoritative DNS.
  - Cloudflare MX is present.
  - Frappe Cloud serves the live site.
- Verified GoDaddy still appeared to be registrar for `locallytwisted.com`; expiration observed as `2027-05-19`.
- GoDaddy login/access remained blocked by GoDaddy/Akamai EdgeSuite/504-style errors; this is queued as later work.
- Bluehost Billing Center showed two relevant products tied to `locallytwisted.com`: SiteLock Essentials and WordPress Basic Hosting.
- User explicitly approved turning off auto-renew for both Bluehost products and approved retiring the old Bluehost WordPress entries under that plan.
- Completed Bluehost confirmation flows for both products. Bluehost showed processing notices.
- Verified Bluehost Renewal Center/API state after the flows: `AutoRenewOn=0`, `AutoRenewOff=1`, and WordPress Basic Hosting `autoRenew=false`.
- Important caveat: the visible Bluehost Angular table/cache continued to paint stale on-state switches after reload. Treat provider/backend renewal API state as stronger evidence than the stale table, and do not retry toggles solely because that visible table looks old.
- Added reusable capability recipe `capabilities-connections-control/recipes/approval-gated-account-page-automation.md` for logged-in account-page work with explicit approval gates and stale-UI/API verification.

## Current verified browser/control state

- User/live Brave CDP lane: `http://127.0.0.1:9222`
- Agent-only Brave CDP lane: `http://127.0.0.1:9223`
- Agent-only profile path: `/home/guidingl/.local/share/hermes/agent-brave-profile`
- Hermes terminal PATH bridge: `/home/guidingl/.hermes/profiles/banebook/terminal-path-bridge.sh` is active through `terminal.shell_init_files`.
- Helper command names now resolve in new terminal calls: `hermes-agent-brave-status`, `hermes-agent-cdp`, `wardenclyffe-status`, `wardenclyffe-ssh`.
- Absolute helper paths remain safe fallbacks.

## Guardrails for next agent

- Do not copy browser profiles, cookies, auth stores, `.env` files, tokens, passwords, wallet keys, or raw logs into this repo.
- Use `9222` only for user/live tabs the user asks Uma to inspect.
- Use `9223` for independent public browsing and control tests.
- Prefer CDP/DOM/API/CLI/file artifacts over `xdotool` or `ydotool`.
- Wardenclyffe is currently verified as Kubuntu/Linux over SSH; do not rely on stale Windows/PowerShell assumptions.
- Wardenclyffe reverse SSH into Banebook is now authorized for the exact handoff key; do not add more keys or weaken SSH settings without explicit approval.
- Still stop before final external actions: submissions, messages, uploads, account/security changes, payments, signatures, loan acceptance, production deployments, destructive deletes, Docker pruning, backup removal, reboots, or service stops.
- For logged-in account pages, keep private details out of repo docs: no raw emails, account IDs, payment details, personal contact fields, screenshots containing sensitive account data, cookies, tokens, or raw browser/session dumps.
- For `locallytwisted.com`, do not cancel/close GoDaddy or allow domain registration to lapse until Cloudflare Registrar transfer is complete or the user explicitly chooses to keep/change the registrar path.
- Re-verify vendor state before future billing/domain actions; cached single-page app UI may be stale after a provider success response.

## Publish/GitHub status

- GitHub operations from Hermes terminal require real-user home auth: `HOME=/home/guidingl git ...` or `HOME=/home/guidingl gh ...`.
- Use live git commands for current remote truth; embedded SHAs are only historical evidence snapshots.

## Validation commands

```bash
python tools/check_source_of_truth_parity.py
python /home/guidingl/projects/capabilities-framework/tools/validate_project_shape.py --project /home/guidingl/projects/hermes-tasks --project-slug hermes-tasks
python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-connections-control --json
python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-agent-infrastructure --json
```

## Remaining work

- Add messaging/notification capability only after a real platform is connected and verified. Prepared path is Slack manifest + user-provided Slack tokens/app install.
- Decide whether to delete the old 63M test profile at `/home/guidingl/.hermes/profiles/banebook/home/.local/share/hermes/agent-brave-profile`; do not delete without explicit approval.
- Keep `SOURCE-OF-TRUTH.md` and parity docs current whenever state changes.
- Recover GoDaddy access for `locallytwisted.com`, check only non-domain GoDaddy products for cancellation, and preserve domain registration until Cloudflare Registrar transfer or explicit registrar decision is complete.
