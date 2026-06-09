---
id: agent-gui-input-isolation
name: Agent GUI Input Isolation
schema_version: 2.1
profile: governed
level: recipe
maturity: candidate
scope: wardenclyffe agent desktop, keyboard, mouse, cursor, clipboard, and GUI automation routing
currently_true: unknown
verification_level: 1
last_verified: 2026-05-12
evidence_quality: mixed
successful_uses: 0
failed_uses: 0
regressions: 0
depends_on:
  - multi-machine-project-operations
  - windows-popup-process-containment
used_by: []
tags:
  - wardenclyffe
  - windows
  - cursor
  - mouse
  - keyboard
  - hotkeys
  - clipboard
  - gui-automation
  - hermes
  - codex
  - hyper-v
  - accessibility
---

# Agent GUI Input Isolation

Use this when an agent may need browser, desktop, or GUI control on
`wardenclyffe` and the user still needs their physical keyboard, cursor, and
clipboard focus.

Banebook migration note: this recipe is about isolating remote or Windows GUI
automation from the user's active desktop. It is not a reason to install or use
OpenClaw, Hermes, `windows-computer-use`, or Windows host-desktop automation as
a Banebook default. Recheck current Banebook and Wardenclyffe tooling before
choosing an automation surface.

## Core Rule

Do not treat a second physical mouse or keyboard as the fix. Windows desktop
automation that sends normal mouse, keyboard, text, shortcut, or clipboard
events targets the current interactive desktop/session. The fix is a separate
automation surface: browser/API control, a separate VM, Windows Sandbox, or
another isolated desktop/session.

Agent GUI control on the user's active desktop is a last resort. Before using a
host-desktop computer-use tool, tell the user it will take the cursor/keyboard
focus and wait for explicit approval.

## Why

- Windows routes ordinary mouse input through the system cursor hot spot.
- Windows routes ordinary keyboard input to the foreground thread/window with
  keyboard focus. Text entry, shortcuts, and system key combinations can affect
  the user's active apps.
- Raw Input can distinguish HID devices for applications that explicitly read
  raw device data, but that does not give ordinary desktop apps independent
  per-process cursors or keyboard focus.
- Browser-level automation tools provide safer web/app control than
  full-desktop input. Use Playwright, CDP, DOM, or verified current browser
  tooling before full-desktop control when the task is browser work.
- Hyper-V and Windows Sandbox provide separate Windows environments. A GUI
  agent driving input inside those environments should not move the host
  desktop cursor.

## Preferred Routing

1. Use non-GUI routes first: CLI, API, SSH, PowerShell on Wardenclyffe,
   Playwright, CDP, DOM selectors, or verified browser-tool commands.
2. For browser work that needs a visible browser, use a Codex-managed or other
   verified isolated
   browser profile before screen-coordinate clicking or keyboard typing.
3. For full desktop work, use a persistent Hyper-V VM such as
   `agent-desktop-01` on `wardenclyffe`.
4. For disposable or risky GUI checks, use Windows Sandbox with no host drive
   mapping unless the task explicitly needs it.
5. Use the physical host desktop only after explicit user approval.

## Recommended Wardenclyffe Build

Target state:

- A persistent local Hyper-V VM named `agent-desktop-01`.
- A low-privilege Windows account inside the VM for GUI agents.
- Tailscale or loopback-only access for agent control, scoped to the VM.
- Codex or other verified browser tooling installed inside the VM, not pointed at the
  user's host desktop session.
- No default host `C:` drive sharing. Use git remotes, explicit Tailscale share
  folders, or one-way staging paths for files.
- Clipboard sharing disabled by default; enable it only for a specific task and
  disable it again after verification.
- A fixed display size, for example 1440x900 or 1920x1080, so screenshots and
  computer-use coordinates are stable.

## Host Safety Rules

- Do not enable `windows-computer-use`, desktop-control runtimes, VNC, RDP
  shadowing, or similar tooling against the user's active host session without
  explicit approval.
- Do not use unsupported client-Windows multi-session patches or RDP wrapper
  approaches. Use a supported VM, Windows Sandbox, Windows Server RDS, Azure
  Virtual Desktop, Windows 365, or another legitimate isolated desktop.
- Do not map sensitive host folders, auth files, browser profiles, `.codex`,
  `.claude`, Hermes auth/state, or client data into the VM by default.
- Do not send keystrokes, paste text, trigger shortcuts, read/overwrite the
  host clipboard, or change host keyboard focus without explicit approval.
- Treat surprise cursor movement, unexpected typed text, stolen keyboard focus,
  or host clipboard changes as accessibility/work interruptions, similar to
  foreground console popups.

## Verification Checklist

Before claiming the isolation is working:

1. Record host identity with `hostname` and `whoami`.
2. Confirm the agent tool is connected to the VM or sandbox, not the host
   desktop.
3. Put the host cursor at a known position and keep a harmless host text field
   unfocused, then run a small GUI action inside the isolated desktop.
4. Confirm the host cursor position did not change, no host text was typed, no
   host hotkey fired, and the host clipboard value stayed intact unless
   clipboard sharing was explicitly part of the test.
5. Capture a screenshot or status output from the isolated desktop proving the
   GUI action happened there.
6. Record any exposed shared folders, clipboard settings, network access, and
   credentials scope.

## Current Wardenclyffe Evidence

Checked on 2026-05-12:

- Host/user: `Wardenclyffe` / `wardenclyffe\baenb`.
- OS: Windows 11 Pro, build 26200, 64-bit.
- Hardware hypervisor reported present.
- Hyper-V PowerShell `Get-VM` and Windows optional feature inventory need an
  elevated shell for this user/session.
- Current live Codex config does not register `windows-computer-use`.
- `C:\Users\baenb\plugins\windows-computer-use` was not present.
- OpenClaw was retired on 2026-05-14. Browser-level automation should now use
  Playwright, CDP, DOM, Hermes browser tooling, or an isolated desktop surface.
- Microsoft keyboard input docs confirm keyboard messages go to the foreground
  thread/window with keyboard focus.
- Emergency containment on 2026-05-12 removed the host-desktop
  `com.openai.codexextension` native messaging registry key after Codex browser
  control stole the user's active typing. Backup:
  `C:\Users\baenb\.codex\tmp\input-containment-20260512\com.openai.codexextension.reg`.
- Later on 2026-05-12, the user explicitly asked to restore that bridge if
  disabling it blocked the higher-priority agent work. The registry key was
  restored from the backup. This is a temporary priority override, not a safe
  steady state; the isolated agent desktop remains urgent.

## Current Source Checks

- Microsoft Mouse Input Overview:
  https://learn.microsoft.com/en-us/windows/win32/inputdev/about-mouse-input
- Microsoft Keyboard Input Overview:
  https://learn.microsoft.com/en-us/windows/win32/inputdev/about-keyboard-input
- Microsoft Keyboard Input getting-started docs:
  https://learn.microsoft.com/en-us/windows/win32/learnwin32/keyboard-input
- Microsoft Raw Input Overview:
  https://learn.microsoft.com/en-us/windows/win32/inputdev/about-raw-input
- Microsoft Hyper-V Enhanced Session Mode:
  https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/enhanced-session-mode
- Microsoft Windows Sandbox:
  https://learn.microsoft.com/en-gb/windows/security/application-security/application-isolation/windows-sandbox/
- Hermes browser tooling should be checked against the current installed Hermes
  docs/source before use; do not assume it is installed or current on Banebook.
