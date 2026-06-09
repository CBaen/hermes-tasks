---
id: voice-capture-transcription-reliability
name: Voice Capture Transcription Reliability
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: local Windows voice capture, dictation, recorder, and STT debugging
currently_true: unknown
last_verified: 2026-05-05
tags:
  - voice capture
  - transcription
  - STT
  - dictation
  - recorder
---

# Voice Capture Transcription Reliability

Date: 2026-05-05
Maturity: emerging
Scope: local Windows voice capture, dictation, recorder, STT debugging

## Decision

Do not treat browser SpeechRecognition or Windows dictation `listening` state as proof that transcription works.

## Reliable Evidence

Use these signals instead:

- Visible transcript text changed in the target field.
- Captured audio metrics show usable chunks, bytes, duration, and signal.
- Backend logs show the real STT endpoint was called.
- A direct STT smoke with generated non-client audio returns non-empty text.
- Tests cover duplicate handling and minimum audio thresholds.

## Failure Pattern

An OS or browser dictation UI can look active while no transcript text is emitted and no backend transcription request is made. In that case, testing only the hotkey or UI request endpoint proves the wrong layer.

## Default Fix Pattern

Build the reliable path around recorded audio:

1. Capture audio locally.
2. Validate duration, size, chunks, and signal.
3. Send usable audio to a local STT endpoint.
4. Write returned text to the visible field.
5. Keep OS/browser dictation as optional help, not the foundation.

## Privacy Rule

Use generated speech or other non-client audio for smoke tests. Do not store raw meeting audio, transcripts, private provider responses, or client notes in git or global capability evidence.
