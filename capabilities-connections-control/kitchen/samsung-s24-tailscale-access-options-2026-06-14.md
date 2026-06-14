# Samsung S24 Tailscale Access Options

TS:2026-06-14T13:09:00-06:00 | Check:`tailscale status --json` from Banebook and Wardenclyffe | Confidence:medium

## Current verified state

The Samsung S24 appears in the tailnet as:

```text
HostName: Bane  24Ultra
DNSName: bane--24ultra.tailc95f4d.ts.net
Tailscale IPv4: 100.75.32.46
OS: android
Online: false
LastSeen: 2026-06-14T08:13:47.1Z
```

Practical meaning: Banebook and Wardenclyffe can identify the phone as a Tailscale peer, but it is currently offline on Tailscale, so agents cannot reach it right now.

## Important reality check

Tailscale gives the phone a private network address. It does **not** automatically let agents read files, control the screen, send messages, or inspect apps. Android access requires a service/app on the phone plus user-granted permissions.

## Safe access levels

### Level 0 — Presence only

What it enables:

- Know whether the phone is online on Tailscale.
- Ping/reachability checks.

Requirements:

- Tailscale app installed and connected on the phone.
- Phone awake enough for Tailscale to stay online.

Risk: low.

### Level 1 — File drop / file pickup

Good options:

- Syncthing between phone and one computer.
- FolderSync/WebDAV/SFTP style app on Android.
- KDE Connect file transfer when paired.

Use for:

- photos/docs transfer;
- local artifacts to review on phone;
- importing phone exports provided by the user.

Risk: medium; files may contain private phone data.

### Level 2 — Phone-side shell via Termux SSH

Option:

- Install Termux + OpenSSH on Samsung S24.
- Run SSH on a nonstandard port such as `8022`.
- Access it from Banebook/Wardenclyffe over `100.75.32.46:8022` when phone is online.

Use for:

- limited file operations inside Termux storage;
- scripted local Android-side tasks;
- safe command checks.

Limits:

- Does not grant full Android root or app data access.
- Requires user setup on the phone.
- Must not be used to bypass app/account approvals.

Risk: medium-high; this is real remote shell access.

### Level 3 — KDE Connect companion control

Option:

- Pair KDE Connect on Banebook/Wardenclyffe and Samsung S24.

Use for:

- notification relay if approved;
- clipboard/file share;
- ring phone;
- battery status;
- limited remote input features.

Limits:

- Tailscale may not support multicast discovery automatically; direct host pairing may be needed.
- Notification/SMS permissions are sensitive.

Risk: medium-high depending on enabled plugins.

### Level 4 — ADB wireless debugging / scrcpy

Option:

- Enable Android Developer Options and Wireless Debugging.
- Pair `adb` with a phone-displayed code.
- Use `scrcpy` or ADB commands when explicitly approved.

Use for:

- screen mirroring/control;
- app testing;
- advanced diagnostics.

Limits:

- Requires phone-side pairing approval.
- Very powerful. Should be task-specific and temporary.

Risk: high. Do not enable as a standing autonomous permission.

## Recommendation

For automation that is useful but not reckless:

1. Start with **Level 0 presence checks** once the phone is online.
2. If the user wants file flows, use **Syncthing or KDE Connect** with narrow folders/plugins.
3. If agents need shell-like phone automation, use **Termux SSH** with a nonstandard port and a dedicated key, but only after explicit setup approval.
4. Reserve **ADB/scrcpy** for attended sessions only.

## Next setup checklist when the phone is available

1. Turn on Tailscale on Samsung S24 and verify it appears online from Banebook:

```bash
tailscale ping 100.75.32.46
```

2. Pick one access level above.
3. Install/enable the matching phone app/service.
4. Create a dedicated key/service identity if SSH is used.
5. Document the exact allowed actions and stop conditions before giving agents access.
