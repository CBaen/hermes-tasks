---
id: desktop-input-control-boundary
name: Desktop Input Control Boundary
schema_version: 2.1
profile: foundation
level: ingredient
maturity: candidate
scope: Banebook desktop input command availability and last-resort control boundary
currently_true: verified
last_verified: 2026-06-11
used_by:
  - internet-and-browser-control-stack
tags:
  - banebook
  - hermes
  - desktop-control
  - xdotool
  - ydotool
  - keyboard
  - mouse
  - safety
---

# Desktop Input Control Boundary

## What it helps with

Use this when the task may require controlling non-browser desktop apps or GUI surfaces where protocol/API control is unavailable.

## Verified local commands

On 2026-06-11, these desktop/window/input tools were available on Banebook:

- `wmctrl` - window listing/focusing/closing checks
- `xdotool` - X11 keyboard/mouse/window automation
- `ydotool` - lower-level input automation

## Boundary

Desktop input tools can affect the active desktop, focus, keyboard, mouse, or user workflow. They are a last resort compared with browser protocol, APIs, CLI tools, file generation, or app-specific commands.

## Preferred routing

1. Use API/CLI/file generation when possible.
2. Use CDP/DOM/browser protocol for web pages.
3. Use app-specific command line or DBus if available.
4. Use desktop input automation only after explicit user approval when it may steal focus, move the cursor, type into active windows, or touch the clipboard.

## Guardrails

- Do not use screen-coordinate clicking or raw keyboard input against the user's active desktop without explicit approval for that task.
- Do not assume a second physical input device gives safe isolation.
- Treat surprise cursor movement, typed text, or focus stealing as a user-work interruption.
