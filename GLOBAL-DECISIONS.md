# Hermes Tasks Global Decisions

Newest entries first. These are machine/project-global decisions for future AI agents. They are not private memory, not a secret store, and not a runtime config file.

## 2026-06-11T16:06:12-06:00 - Browser control uses two lanes on Banebook

Decision: Maintain two separate Brave/CDP browser lanes on Banebook:

- User/live lane: normal Brave profile, CDP endpoint `http://127.0.0.1:9222`, for pages Guiding Light is actively using or explicitly asks Uma to inspect.
- Agent-only lane: separate Brave profile at `/home/guidingl/.local/share/hermes/agent-brave-profile`, CDP endpoint `http://127.0.0.1:9223`, for Uma's independent browsing, research, navigation, and browser-control checks.

Reason: Guiding Light wants Uma to be better connected and able to work through the internet and local hardware without taking over the physical cursor/keyboard or unnecessarily interrupting the user.

Operational rule: Prefer protocol/API/CDP/DOM/file-level work before desktop-coordinate input. The agent-only lane increases technical capability, not authority; final external actions still need explicit approval.

Evidence: `hermes-agent-brave-status` returned a live agent-only profile on `9223`; user/live Brave remained reachable on `9222`; `hermes-agent-cdp control-proof` inserted and read back text via CDP; the agent tab navigated to Hermes docs and read page title/heading.

## 2026-06-11T16:06:12-06:00 - Visible repo is the source-of-truth for AI-readable Uma/Hermes operating docs

Decision: Use `/home/guidingl/projects/hermes-tasks` as the visible, git-trackable operating repo for AI-readable Uma/Hermes task state, decisions, lessons, capability routing, and handoffs.

Reason: Runtime/profile files under `/home/guidingl/.hermes/profiles/banebook` and local helpers under `/home/guidingl/.local/bin` are real machine state, but the durable explanatory map for future agents belongs in this repo.

Operational rule: Link to runtime paths when useful; do not copy secrets, tokens, cookies, raw browser profiles, `.env` contents, auth stores, or raw logs into the repo.

Evidence: Main README, project status, queue, index, handoff, lessons, decisions, and capability roots were updated and validated locally.

## 2026-06-11T16:06:12-06:00 - Connections/control is the active capability-development focus

Decision: Grow `capabilities-connections-control/` first when improving Uma's ability to access, read, control, and type through internet/browser/hardware surfaces.

Reason: Guiding Light clarified that real capabilities matter more than creating many empty process folders. Connection to the internet and ability to control/type in pages are concrete ingredients and should be recorded there first.

Operational rule: Add capabilities only after live verification on Banebook. Keep collaboration/autonomy and agent-infrastructure roots as support roots unless they contain tested capabilities.

Evidence: `capabilities-connections-control/` validates with 6 cards, 0 errors, 0 warnings.
