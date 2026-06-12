# Hermes Messaging Options For Banebook

TS:2026-06-11T22:37:43-06:00 | Check:Hermes docs, local CLI help, gateway status, prerequisites, Slack manifest generation | Confidence:high

## Current truth

No messaging platform is connected yet.

Evidence:

```text
send_message(action="list") -> No messaging platforms connected or no channels discovered yet.
hermes send --list -> No messaging platforms configured or no channels discovered yet.
hermes gateway status -> Gateway is not running.
```

## Prepared artifact

Slack manifest regenerated and JSON-validated here:

```text
artifacts/messaging/hermes-slack-manifest.json
```

Verified manifest facts:

```text
name: Hermes Uma
slash_commands: 50
socket_mode_enabled: true
bot_scopes: 14
```

## Option ranking

### 1. Slack — best prepared path

Why:

- Hermes officially supports Slack through Socket Mode.
- Socket Mode does not require a public HTTP endpoint.
- Manifest generation is already complete.
- Good for durable notifications, cron outputs, background-task completion, and multi-device use.

Still requires user/account action:

- Create/import Slack app from `artifacts/messaging/hermes-slack-manifest.json`.
- Install app to workspace.
- Provide `SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN`, and `SLACK_ALLOWED_USERS` / home channel through Hermes setup or secure env/config flow.
- Invite bot to target channels or use DM.
- Start/install gateway.

### 2. WhatsApp — fastest personal-phone style path, but with policy risk

Why:

- Hermes supports `hermes whatsapp` QR pairing.
- Local prerequisites are present: Node.js and npm are installed.
- No Meta developer account is required.

Risks / blockers:

- Hermes docs call this an unofficial WhatsApp Web/Baileys bridge with account-restriction risk.
- Best practice is a dedicated bot phone number, not the user's personal number.
- Requires phone QR pairing by the user.
- Session directory becomes account credential material and must never be committed.

### 3. Signal — best privacy posture, more setup work

Why:

- Hermes supports Signal through `signal-cli` HTTP daemon.
- Signal is privacy-focused and supports Note to Self style use.

Blockers:

- `signal-cli` is not installed on Banebook.
- Requires Java 17+; Banebook has Java available.
- Requires linking a Signal number as a device from the user's phone.
- Installs external `signal-cli` from GitHub releases, which should be approved before doing account linkage.

## Recommendation

Use **Slack first** for reliable Hermes notifications if the user is willing to create/install a Slack app. Use **WhatsApp** only if the user prefers phone chat and accepts unofficial bridge risk. Use **Signal** if privacy matters more than setup speed and the user is ready to link `signal-cli`.

## Safe next actions without user account linking

- Keep the Slack manifest artifact current.
- Keep docs/capability queue updated.
- Do not run `hermes whatsapp` for QR pairing unless the user is present.
- Do not install/link `signal-cli` unless the user explicitly approves.
- Do not write Slack/WhatsApp/Signal tokens into repo docs.
