# Hermes Tasks Handoff

TS:2026-06-11T16:06:12-06:00 | Check:session handoff created after browser/control setup and pre-publish doc consolidation | Confidence:high

## Current state

- Repo: `/home/guidingl/projects/hermes-tasks`
- Branch: `main`
- Intended remote: `https://github.com/CBaen/hermes-tasks`
- Role of this repo: visible, git-trackable AI-readable source of truth for Uma/Hermes task routing, decisions, lessons, handoffs, and capability roots on Banebook.
- Runtime/profile state remains outside this repo.

## What changed this session

1. LibreOffice was confirmed/finished as a full-suite apt install on Banebook.
2. User/live Brave was configured/verified for open-tab CDP access on `127.0.0.1:9222`.
3. Main Uma/Hermes project docs were created/updated in this repo.
4. Dedicated capability roots were created:
   - `capabilities-connections-control/`
   - `capabilities-collaboration-autonomy/`
   - `capabilities-agent-infrastructure/`
5. `capabilities-connections-control/` was made the active capability-development focus.
6. Verified connection/control capabilities were added for:
   - public internet access,
   - user/live Brave open-tab CDP access,
   - protocol page control and typing,
   - desktop input control boundary,
   - agent-only Brave profile lane,
   - composed internet/browser control stack.
7. Agent-only Brave profile was created and verified outside the repo:
   - profile: `/home/guidingl/.local/share/hermes/agent-brave-profile`
   - endpoint: `http://127.0.0.1:9223`
   - helpers: `hermes-agent-brave`, `hermes-agent-brave-status`, `hermes-agent-brave-stop`, `hermes-agent-cdp`
   - desktop launcher: `/home/guidingl/.local/share/applications/hermes-agent-brave.desktop`
8. AI-readable inheritance docs were added:
   - `HANDOFF.md`
   - `LESSONS-LEARNED.md`
   - `GLOBAL-DECISIONS.md`
   - `agent-lanes/connections-control-HANDOFF.md`
   - `artifacts/libreoffice/README.md`

## Verified browser/control state

- User/live Brave CDP lane: `http://127.0.0.1:9222`
- Agent-only Brave CDP lane: `http://127.0.0.1:9223`
- Agent-only profile path: `/home/guidingl/.local/share/hermes/agent-brave-profile`
- Agent helper proof: `hermes-agent-cdp control-proof` inserted/read back `Hermes agent profile typed this via CDP`.
- Agent navigation proof: agent tab navigated to `https://hermes-agent.nousresearch.com/docs/user-guide/features/browser` and read back title `Browser Automation | Hermes Agent`.

## Guardrails for next agent

- Do not copy browser profiles, cookies, auth stores, `.env` files, tokens, passwords, wallet keys, or raw logs into this repo.
- Use `9222` only for user/live tabs the user asks Uma to inspect.
- Use `9223` for independent public browsing and control tests.
- Prefer CDP/DOM/API/CLI/file artifacts over `xdotool` or `ydotool`.
- Still stop before final external actions: submissions, messages, uploads, account/security changes, payments, signatures, loan acceptance, production deployments, destructive deletes, Docker pruning, or backup removal.

## Validation commands

```bash
python /home/guidingl/projects/capabilities-framework/tools/validate_project_shape.py --project /home/guidingl/projects/hermes-tasks --project-slug hermes-tasks
python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-connections-control --json
python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-collaboration-autonomy --json
python /home/guidingl/projects/capabilities-framework/tools/validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-agent-infrastructure --json
hermes-agent-brave-status
hermes-agent-cdp eval '({title: document.title, url: location.href})'
```

## Publish status

- Remote configured: `origin https://github.com/CBaen/hermes-tasks`.
- Initial push succeeded at 2026-06-11T16:44:49-06:00: remote `main` reached `70c83bbb5c746c84ab6c77d1659e25ee87b4fe23`.
- Important auth detail: Hermes terminal default `$HOME` is `/home/guidingl/.hermes/profiles/banebook/home` and is not logged into GitHub. GitHub auth is available under the real user home. Use `HOME=/home/guidingl git ...` or `HOME=/home/guidingl gh ...` for GitHub operations from this Hermes session.
- Final publish-status commit is expected after this handoff update.

## Remaining work

- Add messaging/notification capability only after a real platform is connected and verified.
- Repair or document Wardenclyffe bridge only after current helper availability is verified.
- If the user wants a cleaner workspace, decide whether to delete the old empty test profile at `/home/guidingl/.hermes/profiles/banebook/home/.local/share/hermes/agent-brave-profile`; do not delete without approval.
