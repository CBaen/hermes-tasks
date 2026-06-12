---
id: wardenclyffe-to-banebook-ssh-access
name: Wardenclyffe To Banebook SSH Access
schema_version: 2.1
profile: foundation
level: ingredient
maturity: candidate
scope: reverse SSH from Wardenclyffe Kubuntu into Banebook over Tailscale
currently_true: verified
last_verified: 2026-06-11
tags:
  - banebook
  - wardenclyffe
  - ssh
  - tailscale
  - reverse-access
  - coordination
---

# Wardenclyffe To Banebook SSH Access

## What it enables

Wardenclyffe agents can now verify or coordinate with Banebook over SSH when a multi-machine workstream needs reverse access back to the daily-control workstation.

## Current verified state

Verified on 2026-06-11T22:37:43-06:00 from Banebook after following Wardenclyffe handoff:

```text
agent-coordination/wardenclyffe-kubuntu-restore/handoffs/banebook-ssh-unblock-2026-06-11.md
```

Banebook authorized this exact public key comment:

```text
wardenclyffe-1-to-banebook-tailscale-2026-06-11
```

Fingerprint verified before and after authorization:

```text
SHA256:Cl5SYra87E5eyA/cy4PWPDAj1aoYm9HmxYLU0hhzmGM
```

Permissions after setup:

```text
/home/guidingl/.ssh -> 700
/home/guidingl/.ssh/authorized_keys -> 600
```

Wardenclyffe-side verification succeeded:

```bash
wardenclyffe-ssh 'ssh -o BatchMode=yes banebook "hostname; whoami; find ~/.codex/skills ~/codex-framework/skills -maxdepth 2 -name SKILL.md 2>/dev/null | sort | rg -i "triad|witness|construction" || true"'
```

Returned:

```text
BANEBOOK
guidingl
/home/guidingl/codex-framework/skills/triadic-construction-v2/SKILL.md
/home/guidingl/codex-framework/skills/triadic-work/SKILL.md
/home/guidingl/codex-framework/skills/witnessed-work/SKILL.md
```

## Guardrails

- This is account-access/security-sensitive. Only the exact user-directed handoff key was added.
- Do not add more keys, weaken SSH auth, enable password login, or expose Banebook SSH outside Tailscale without explicit approval.
- Use this for coordination and read/check workflows by default. Destructive or sensitive Banebook changes still require normal approval gates.
- Public keys and fingerprints may be documented; private keys, SSH agent sockets, auth stores, and secrets must never be copied into repo docs.

## Rollback

Remove the `authorized_keys` line ending with:

```text
wardenclyffe-1-to-banebook-tailscale-2026-06-11
```

A backup was created before appending:

```text
/home/guidingl/.ssh/authorized_keys.bak-wardenclyffe-unblock-<timestamp>
```
