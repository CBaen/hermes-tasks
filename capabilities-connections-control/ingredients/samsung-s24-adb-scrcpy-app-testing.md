---
id: samsung-s24-adb-scrcpy-app-testing
name: Samsung S24 ADB Scrcpy App Testing
schema_version: 2.1
profile: foundation
level: ingredient
maturity: candidate
scope: attended Android app testing against Samsung S24 from Banebook and Wardenclyffe
currently_true: host toolchain installed; S24 reachable on Tailscale; phone not paired yet
last_verified: 2026-06-14
tags:
  - android
  - samsung-s24
  - adb
  - scrcpy
  - app-testing
  - tailscale
  - banebook
  - wardenclyffe
---

# Samsung S24 ADB Scrcpy App Testing

## What this enables

Use this when Uma needs to test Android apps on the real Samsung S24 instead of only using web/browser checks or emulators.

This is an **attended developer-testing lane**, not a standing unattended phone-control lane.

## Verified host state

Verified on 2026-06-14T13:57:08-06:00.

### Banebook

```text
adb: Android Debug Bridge 1.0.41 / 34.0.5-debian
fastboot: 34.0.5-debian
scrcpy: 3.3.4
ADB devices before pairing: none
```

Installed packages:

```text
adb
fastboot
scrcpy
android-udev-rules
```

### Wardenclyffe

```text
adb: Android Debug Bridge 1.0.41 / 34.0.5-debian
fastboot: 34.0.5-debian
scrcpy: 3.3.4
ADB devices before pairing: none
```

Installed packages:

```text
adb
fastboot
scrcpy
android-udev-rules
```

### Samsung S24 reachability

```text
HostName: Bane  24Ultra
Tailscale IP: 100.75.32.46
OS: android
Online: true
```

`tailscale ping` from Banebook succeeded over the direct LAN route.

## Plain-English safety model

ADB/scrcpy means "developer remote-control mode."

- **ADB** is the command/control bridge Android exposes for developers after the phone user enables Developer Options and approves pairing.
- **scrcpy** uses ADB to mirror/control the phone screen from a computer.

That makes it appropriate for app testing, but it can expose private apps, messages, OTPs, notifications, financial screens, and account sessions if used broadly.

## Allowed green actions after pairing

For a named app-testing task, Uma may:

- list connected devices with `adb devices -l`;
- install or reinstall a user-approved APK/build artifact;
- launch the named test app/package;
- capture screenshots or screen recordings of the named test app;
- inspect logs for the named app with filters where practical;
- use `scrcpy` while the user is present to observe/control the test app;
- document PASS/FAIL evidence without secrets or unrelated phone data.

## Yellow actions requiring explicit task approval

Pause before:

- enabling Developer Options or Wireless Debugging instructions on the phone;
- pairing a new computer with ADB;
- running `adb shell` outside the named test-app scope;
- reading broad logs that could include other apps/private data;
- changing device settings;
- granting app permissions;
- installing any APK not built/provided for the current test;
- using scrcpy when private apps/notifications are visible.

## Red hard stops

Do not:

- use ADB/scrcpy unattended as standing autonomous phone control;
- open banking, authenticator, wallet, health, private messaging, password manager, or account-security apps;
- read SMS, notifications, contacts, photos, downloads, or app data unless the user explicitly approves that exact source;
- send messages, submit forms, make purchases, approve MFA, change account/security settings, or delete phone data;
- store pairing codes, screenshots with private data, raw logs, or phone dumps in repo docs.

## Pairing workflow when user is present

On the Samsung S24:

1. Open **Settings**.
2. Go to **About phone** -> **Software information**.
3. Tap **Build number** seven times to enable Developer Options, if not already enabled.
4. Go back to **Settings** -> **Developer options**.
5. Enable **Wireless debugging**.
6. Tap **Wireless debugging** -> **Pair device with pairing code**.
7. Read the pairing IP/port and pairing code to Uma.

On Banebook or Wardenclyffe:

```bash
adb pair <phone-ip-or-tailscale-ip>:<pairing-port>
# enter the phone-displayed pairing code when prompted
```

Then on the phone's Wireless debugging screen, note the **IP address & port** for normal connection, and run:

```bash
adb connect 100.75.32.46:<connect-port>
adb devices -l
```

If Tailscale IP does not work for the pairing/connect port, try the phone-displayed local Wi-Fi IP/port while on the same LAN. Do not guess ports; use the phone-displayed values.

## scrcpy commands

Start mirrored app-testing session after `adb devices -l` shows the S24:

```bash
scrcpy --serial 100.75.32.46:<connect-port>
```

Common safer options:

```bash
scrcpy --serial 100.75.32.46:<connect-port> --stay-awake --turn-screen-off=false
scrcpy --serial 100.75.32.46:<connect-port> --record /tmp/s24-app-test.mp4
```

Prefer Banebook for interactive scrcpy because Banebook is the cockpit desktop. Wardenclyffe can run headless ADB/log/build tasks after pairing, but screen mirroring/control should usually be driven from Banebook unless a specific Wardenclyffe desktop session is intended.

## Verification checklist

Before claiming app-device readiness:

```bash
adb version
scrcpy --version
adb devices -l
tailscale ping --timeout=5s --c 2 100.75.32.46
```

For a specific app test, also record:

- app/package name;
- build/APK path and hash if relevant;
- install command/result;
- launch command/result;
- screenshots/video/log evidence path;
- what was not touched.
