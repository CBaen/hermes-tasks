# Hermes Tasks Lessons Learned

Newest entries first. AI-facing, concise, and evidence-oriented. Do not store secrets or raw session dumps here.

## 2026-06-11T22:37:43-06:00 - Verify SSH handoff keys by fingerprint before authorizing

Lesson: When another agent hands off an SSH unblock request, compute the fingerprint from the exact public key line locally before editing `authorized_keys`, then verify access from the requesting machine.

Why it matters: SSH key authorization is an account-security change. Matching the fingerprint and comment prevents adding the wrong key while keeping the action narrow and reversible.

Evidence: Wardenclyffe handoff fingerprint `SHA256:Cl5SYra87E5eyA/cy4PWPDAj1aoYm9HmxYLU0hhzmGM` matched locally; Wardenclyffe then SSHed into Banebook successfully.

## 2026-06-11T22:37:43-06:00 - Messaging setup can be prepared without making delivery live

Lesson: For Hermes messaging, generating/validating a Slack manifest is safe local prep, but Slack/WhatsApp/Signal are not real notification capabilities until a platform target is connected and `send_message(action=list)` discovers it.

Why it matters: A manifest or installed prerequisite is not delivery. Keep capability cards blocked/candidate until a message target exists and a send/list check proves it.

Evidence: Slack manifest validated locally; no targets were discovered by Hermes send/list tools.

## 2026-06-11T18:17:03-06:00 - Verify Hermes config value types after `hermes config set`

Lesson: For list-valued Hermes config keys, verify the YAML type after using `hermes config set`. In this session, setting `terminal.shell_init_files` with a JSON-looking list wrote a string, and then indexed set produced a mapping because it started from that wrong type.

Why it matters: A syntactically valid YAML config can still hold the wrong type and silently fail to affect terminal behavior.

Verification: Repaired `terminal.shell_init_files` to a real YAML list and confirmed new terminal calls resolve helper commands through the PATH bridge.

## 2026-06-11T17:52:58-06:00 - Timestamp current-state docs together to avoid source-of-truth drift

Lesson: When current state changes, update all affected AI-facing docs in one pass and timestamp them with ISO-8601 timezone values.

Why it matters: A successful push can still leave stale lines like "publish pending" or old `Last updated` values. Future agents should verify live state, then immediately repair stale current-state docs.

Verification: Added `SOURCE-OF-TRUTH.md` and `tools/check_source_of_truth_parity.py`.

## 2026-06-11T16:06:12-06:00 - Separate browser profile avoids interfering with the user's live tabs

Lesson: For independent web work, use the agent-only Brave lane on `127.0.0.1:9223` instead of navigating the user's normal Brave tabs on `127.0.0.1:9222`.

Why it matters: CDP can read/click/type without physical cursor takeover, but using the user's live profile can still clutter tabs or change visible page state. The separate profile gives Uma a safer workspace.

Reusable commands:

```bash
hermes-agent-brave about:blank
hermes-agent-brave-status
hermes-agent-cdp list
hermes-agent-cdp navigate https://example.com
hermes-agent-cdp eval '({title: document.title, url: location.href})'
hermes-agent-cdp control-proof
hermes-agent-brave-stop
```

Guardrail: Do not copy auth stores/cookies/session files between profiles. Do not log into sensitive accounts in the agent-only profile unless the user explicitly chooses that workflow.

## 2026-06-11T16:06:12-06:00 - Browser protocol typing is preferred over desktop input tools

Lesson: `Input.insertText` through CDP successfully typed into a focused page field and read the value back from the DOM.

Why it matters: This satisfies the user's preference for page interaction that does not take over the physical mouse cursor or keyboard.

Verification: A throwaway tab proof inserted and read back `CDP typed this without the physical keyboard`; the agent-only profile proof inserted and read back `Hermes agent profile typed this via CDP`.

Guardrail: CDP typing proves technical control, not approval to submit forms, send messages, upload files, change accounts, sign documents, accept loans, or make payments.

## 2026-06-11T16:06:12-06:00 - Runtime state belongs outside the repo; explanatory maps belong inside it

Lesson: Keep the Hermes profile, SOUL, browser profiles, launchers, caches, and helper scripts in their native Banebook runtime paths. Record only paths, commands, guardrails, and verification evidence in this repo.

Why it matters: Future agents need inheritance without leaking secrets or copying unstable runtime state.

Key paths:

- Active Hermes profile: `/home/guidingl/.hermes/profiles/banebook/`
- Active SOUL: `/home/guidingl/.hermes/profiles/banebook/SOUL.md`
- User/live Brave launcher override: `/home/guidingl/.local/share/applications/brave-browser.desktop`
- Agent-only Brave profile: `/home/guidingl/.local/share/hermes/agent-brave-profile`
- Agent-only helper scripts: `/home/guidingl/.local/bin/hermes-agent-*`

## 2026-06-11 - LibreOffice full-suite install is verified on Banebook

Lesson: Banebook has the full LibreOffice suite installed via apt, including Writer, Calc, Impress, Draw, Math, Base, and Java support for Base/report features.

Verification: LibreOffice version `26.2.3.2` was observed; `apt-get check` returned clean; a small `.odt` file was created as `artifacts/libreoffice/cheese-poem.odt`.

Guardrail: Generated proof documents should live under `artifacts/` and transient LibreOffice lock files matching `.~lock.*#` should be ignored.

## 2026-06-11T16:06:12-06:00 - Use scoped staging in this repo

Lesson: This repo is a shared operating scaffold and can contain unrelated local artifacts. Before publishing, inspect `git status --porcelain=v1 -uall`, stage exact files, and inspect the cached diff before commit.

Why it matters: Avoid accidentally committing runtime caches, browser/session state, lock files, or unrelated agent work.
