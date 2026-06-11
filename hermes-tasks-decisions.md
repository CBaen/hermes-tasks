# Hermes Tasks Decisions

Newest entries first.

## 2026-06-11T17:52:58-06:00 - Wardenclyffe current target is Kubuntu SSH, not retired Windows PowerShell

Decision: Document Wardenclyffe's current reachable control surface as Kubuntu/Linux over Tailscale and SSH, while treating older Windows/PowerShell assumptions as stale unless reverified.

Reason: Live helper inspection and `/home/guidingl/bin/wardenclyffe-status` showed Wardenclyffe reachable as `WARDENCLYFFE` running Linux `7.0.0-14-generic x86_64`. The `wardenclyffe-ps` helper explicitly says the prior Windows workflow was removed.

Applies to: `capabilities-connections-control/ingredients/wardenclyffe-kubuntu-ssh-bridge.md`, future Wardenclyffe operations, and any doc claiming PowerShell/Windows routing.

Verification / evidence: Tailscale ping, TCP 22, SSH `id/hostname/uname`, filesystem inventory, and helper script inspection on 2026-06-11.

## 2026-06-11T16:44:49-06:00 - GitHub auth lives under real user HOME for Hermes shell pushes

Decision: Use `HOME=/home/guidingl` for GitHub CLI and git network operations from this Hermes session when pushing `hermes-tasks`.

Reason: Hermes terminal default `$HOME` is `/home/guidingl/.hermes/profiles/banebook/home`, where `gh auth status` is not logged in. The user completed GitHub auth under `/home/guidingl`, where `gh auth status` reports account `CBaen` with HTTPS git protocol.

Applies to: `git push`, `git ls-remote`, `gh auth status`, and future GitHub operations for `/home/guidingl/projects/hermes-tasks` from Hermes.

Verification / evidence: `HOME=/home/guidingl gh auth status` reported logged in to github.com account `CBaen`; `HOME=/home/guidingl git push -u origin main` succeeded and remote `main` reached `70c83bbb5c746c84ab6c77d1659e25ee87b4fe23`.

## 2026-06-11T16:21:24-06:00 - Remote push requires explicit GitHub authentication setup

Decision: Do not fake or bypass the GitHub push when credentials are unavailable. Record the local commit and auth blocker, then wait for an authenticated path.

Reason: The user asked to commit and push, but pushing to GitHub requires account authentication. This shell has no HTTPS credential helper/token, `gh` is not logged in, and SSH is denied. Adding persistent GitHub auth or SSH keys affects account/security state and needs the user's active login/authorization.

Applies to: remote `origin` at `https://github.com/CBaen/hermes-tasks`, local commit `f5033b8e5edcc5fa2cf01fcedd1a2f40c137c881`, and the `publish-session-state` queue item.

Verification / evidence: `git push -u origin main` failed with `could not read Username for 'https://github.com'`; `gh auth status` reported not logged in; `ssh -T git@github.com` returned permission denied.

## 2026-06-11T16:06:12-06:00 - Publish AI-readable operating state rather than runtime state

Decision: Commit/push the visible Hermes Tasks repo with AI-readable docs, capability cards, verifier declarations, handoffs, lessons, and safe verification artifacts; do not copy runtime browser profiles, cookies, auth stores, helper script contents from outside the repo, raw logs, or secrets into git.

Reason: The user asked for future agents to inherit the right information in the right documents. The durable inheritance value is the organized map, decisions, commands, guardrails, and verification evidence, not raw runtime state.

Applies to: `README.md`, `HANDOFF.md`, `LESSONS-LEARNED.md`, `GLOBAL-DECISIONS.md`, `PROJECT-STATUS.md`, queue/index/decisions docs, `agent-lanes/`, `capabilities-*`, `verifier-manifest.json`, and `artifacts/`.

Verification / evidence: New docs were written before final validation/commit. Runtime paths are documented but not copied. LibreOffice lock files are ignored with `.gitignore` pattern `.~lock.*#`.

## 2026-06-11T15:54:59-06:00 - Add verified agent-only Brave profile lane

Decision: Give Uma a separate persistent Brave profile for independent web work, distinct from Guiding Light's normal Brave profile.

Reason: The user explicitly approved Uma having her own profile and more access/control. A separate browser profile on its own CDP port lets Uma browse, navigate, inspect, and type through browser protocol without cluttering or taking over the user's live Brave tabs.

Applies to: `/home/guidingl/.local/share/hermes/agent-brave-profile`, `/home/guidingl/.local/bin/hermes-agent-brave`, `/home/guidingl/.local/bin/hermes-agent-brave-status`, `/home/guidingl/.local/bin/hermes-agent-brave-stop`, `/home/guidingl/.local/bin/hermes-agent-cdp`, `/home/guidingl/.local/share/applications/hermes-agent-brave.desktop`, and `capabilities-connections-control/recipes/agent-only-browser-lane.md`.

Verification / evidence: Agent-only Brave launched with `--user-data-dir=/home/guidingl/.local/share/hermes/agent-brave-profile` and CDP on `127.0.0.1:9223`; user/live Brave stayed reachable on `9222`; `hermes-agent-cdp control-proof` inserted/read back `Hermes agent profile typed this via CDP`; agent tab navigated to Hermes browser docs and read back title `Browser Automation | Hermes Agent`; `validate_capability_graph.py` for `capabilities-connections-control/` returned ok=true with 6 cards, 0 errors, 0 warnings.

## 2026-06-11T15:43:16-06:00 - Focus capability growth on connections/control first

Decision: Treat `capabilities-connections-control/` as the active capability-development focus and add actual verified internet/browser/control capabilities there before expanding other process roots.

Reason: Guiding Light clarified that the important current capability is Uma's connection to the internet plus ability to read, control, and type in browser pages. That is a real ingredient/ingredient collection, while broader collaboration/infrastructure roots should remain secondary until they contain tested capabilities.

Applies to: `capabilities-connections-control/`.

Verification / evidence: Added verified cards for public internet access, browser protocol page control and typing, desktop input control boundary, and the composed internet/browser control stack. `validate_capability_graph.py --root /home/guidingl/projects/hermes-tasks/capabilities-connections-control --json` returned ok=true with 6 cards, 0 errors, and 0 warnings.

## 2026-06-11T15:35:57-06:00 - Split Uma/Hermes operating capabilities into dedicated roots

Decision: Treat `/home/guidingl/projects/hermes-tasks` as the visible main Uma/Hermes operating repo, keep runtime/profile files under `/home/guidingl/.hermes/profiles/banebook`, and add sibling capability roots for connections/control, collaboration/autonomy, and agent infrastructure.

Reason: Connection/control capabilities are important enough to be their own discoverable framework instead of being buried in the baseline project root. Collaboration permissions and infrastructure setup also need separate routing so future sessions can work in parallel without unnecessary pauses while preserving approval gates.

Applies to: `/home/guidingl/projects/hermes-tasks`, `/home/guidingl/Uma/HERMES-MAIN-PROJECT.md`, and the new roots `capabilities-connections-control/`, `capabilities-collaboration-autonomy/`, and `capabilities-agent-infrastructure/`.

Verification / evidence: Filesystem writes completed; indexes/status were patched; starter capability cards were added. `validate_project_shape.py` returned ok=true with 0 errors/0 warnings. `validate_capability_graph.py` returned ok=true with 0 errors/0 warnings for all three new sibling roots. The baseline root remains ok=true with pre-existing backlink warnings only.

## 2026-06-10T22:56:24-06:00 - Bring scaffold up to current lane/verifier standard

Decision: Add the current standard `agent-lanes/BOARD.md`, `agent-lanes/LANE-HANDOFF.template.md`, and `verifier-manifest.json` files to this persistent Hermes task project.

Reason: The current project shape validator expects these files for new serious-project scaffolds. Adding them keeps future Codex/Hermes sessions from treating the project as an older partial scaffold.

Applies to: `/home/guidingl/projects/hermes-tasks`.

Verification / evidence: project-shape and capability graph validators re-run after the scaffold update.

## YYYY-MM-DD - <Decision>

Decision:

Reason:

Applies to:

Verification / evidence:
