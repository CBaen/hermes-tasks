# Samsung S24 Tailscale Access Options

TS:2026-06-14T13:29:12-06:00 | Check:`tailscale status --json` and `tailscale ping --timeout=5s --c 3 100.75.32.46` from Banebook | Confidence:high for reachability, low for app/control readiness

## Current verified state

The Samsung S24 is online in the tailnet as:

```text
HostName: Bane  24Ultra
DNSName: bane--24ultra.tailc95f4d.ts.net
Tailscale IPv4: 100.75.32.46
Tailscale IPv6: fd7a:115c:a1e0::783a:202e
OS: android
Online: true
```

`tailscale ping` returned pongs through DERP first and then direct LAN:

```text
pong from bane--24ultra (100.75.32.46) via DERP(den) in 130ms
pong from bane--24ultra (100.75.32.46) via 192.168.0.252:58542 in 108ms
```

Practical meaning: the private network road to the phone exists. It is online and reachable. This still does **not** mean Uma can read the phone, control apps, send messages, or see the screen. For that, the phone must run/approve a phone-side service.

## Uma explanation: what the access levels really mean

Think of the Samsung S24 like a locked building on a private road. Tailscale built the private road. We still have to choose which door, if any, to install.

### Level 0 — Presence only: "Can we see the building?"

What Uma can do:

- check whether the S24 is online;
- ping it over Tailscale;
- record last-seen/reachability evidence.

What Uma cannot do:

- read files;
- see notifications;
- control apps;
- send texts;
- mirror the screen.

Risk: low. This is already verified.

### Level 1 — File sync/drop: "A mail slot for chosen folders"

Good tools:

- Syncthing;
- KDE Connect file transfer;
- FolderSync/WebDAV/SFTP app.

What Uma could do after setup:

- move approved files/photos/docs between the phone and computer;
- pick up files you intentionally place in a shared folder;
- put review artifacts on the phone.

What Uma should not get:

- whole-phone storage;
- all photos by default;
- app-private data;
- SMS/notification access.

Risk: medium, because files may contain private data. Good first useful step if we choose narrow folders.

### Level 2 — KDE Connect: "A companion remote"

What it can provide depending on enabled plugins:

- battery status;
- ring/find phone;
- clipboard sharing;
- file transfer;
- notification relay if explicitly allowed;
- limited remote input/media controls.

Plain-English warning: KDE Connect can become sensitive if notification or clipboard plugins are enabled, because notifications and clipboard can contain passwords, OTPs, private messages, or account details.

Risk: medium to high depending on plugins. Good for convenience, but choose plugins carefully.

### Level 3 — Termux SSH: "A small Linux-like toolbox inside Android"

Termux is an Android app that gives the phone a Linux-style terminal area. With OpenSSH inside Termux, Banebook/Wardenclyffe could SSH into **Termux's own sandbox**, usually on port `8022`.

What Uma could do:

- run scripts inside Termux;
- manage files inside Termux storage;
- interact with explicitly shared Android folders if you grant storage access;
- run lightweight phone-side automations.

What it does **not** automatically grant:

- root access;
- all app data;
- full screen control;
- access to banking/social apps;
- permission to send messages.

Risk: medium-high. It is real remote shell access, but much narrower than full phone control when configured carefully. This is the likely best choice for "agent can work on the phone" without going straight to screen takeover.

### Level 4 — ADB wireless debugging + scrcpy: "Developer remote-control mode"

ADB means **Android Debug Bridge**. It is Google's developer/debugging channel for Android devices. Wireless ADB lets a trusted computer connect to the phone after you enable Developer Options and approve a pairing code on the phone.

Scrcpy is a tool that uses ADB to mirror and control the Android screen from a computer. It is basically "remote screen and keyboard/mouse for Android."

What Uma/computer could do with ADB/scrcpy when paired:

- see the phone screen;
- click/type/swipe through apps;
- install/uninstall/debug apps;
- pull/push some files;
- capture screenshots/screen recordings;
- run powerful device commands.

Why this is high-risk:

- it can operate logged-in apps;
- it may expose private notifications, messages, finance apps, OTPs, health data, etc.;
- a mistake can tap real buttons in real apps;
- it is closer to "Uma can use my phone" than "Uma can exchange files with my phone."

Recommendation: because the user identified app testing as the real need, ADB/scrcpy is approved as an attended app-testing lane. It remains unsuitable as standing unattended phone-control access.

## Recommendation ladder

For your goal — agents working across devices without making privacy/security chaotic — the practical ladder is:

1. Keep **Level 0 presence** enabled. Already done.
2. Choose **Level 1 file sync** for safe artifact movement.
3. Add **Level 2 KDE Connect** only with narrow plugins.
4. Add **Level 3 Termux SSH** if we want phone-side scripts/automation.
5. Use **Level 4 ADB/scrcpy** for attended, task-specific app testing only.

## Suggested default for now

ADB/scrcpy is the chosen path for app testing, but not for standing unattended phone access. For non-app-testing convenience, still consider:

- **Syncthing narrow folder** if the goal is moving files/photos/docs.
- **KDE Connect narrow plugins** if the goal is convenience/status/file transfer.
- **Termux SSH** if the goal is real agent-executable phone-side automation.

## Next discussion questions

Before setup, answer in plain terms:

1. Do we want Uma to move files to/from the phone?
2. Do we want Uma to see phone notifications?
3. Do we want Uma to run scripts on the phone?
4. Do we want Uma to see/control the phone screen while you are present?
5. Are there apps/data that should be completely off-limits?
## 2026-06-14T13:57:08-06:00 update — ADB/scrcpy chosen for app testing

The user clarified that Level 4 is needed for app testing. Banebook and Wardenclyffe now have the host toolchain installed:

```text
adb 34.0.5-debian
fastboot 34.0.5-debian
scrcpy 3.3.4
android-udev-rules installed
```

The phone is still not paired. Pairing requires the S24 to show a Wireless Debugging pairing code and port, which must be user-provided live.

See `../ingredients/samsung-s24-adb-scrcpy-app-testing.md` for the attended app-testing workflow.
