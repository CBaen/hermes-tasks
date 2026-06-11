# Hermes Tasks Lessons Learned

Newest entries first. AI-facing, concise, and evidence-oriented. Do not store secrets or raw session dumps here.

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
