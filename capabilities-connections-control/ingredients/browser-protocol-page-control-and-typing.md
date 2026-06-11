---
id: browser-protocol-page-control-and-typing
name: Browser Protocol Page Control And Typing
schema_version: 2.1
profile: foundation
level: ingredient
maturity: candidate
scope: CDP/DOM browser page reading, clicking, and text entry without physical keyboard or mouse takeover
currently_true: verified
last_verified: 2026-06-11
depends_on:
  - local-brave-cdp-open-tabs
used_by:
  - internet-and-browser-control-stack
tags:
  - banebook
  - hermes
  - cdp
  - dom
  - browser-control
  - typing
  - cursor-isolation
---

# Browser Protocol Page Control And Typing

## What it helps with

Use this when Uma needs to read, click, focus fields, or type into browser pages without taking over Guiding Light's physical mouse cursor or keyboard.

## Verified proof

On 2026-06-11, Uma created a temporary `about:blank` target through CDP, inserted an input field, focused it, used `Input.insertText` to type `CDP typed this without the physical keyboard`, read the value back from the DOM, and closed the temporary target.

Proof result:

- Input value read back exactly: `CDP typed this without the physical keyboard`
- The throwaway tab was closed with `Target.closeTarget`.

## What this can do

- Read visible page text and structured DOM state.
- Click page elements by DOM/CDP target rather than screen coordinates.
- Focus fields and insert text through the browser protocol.
- Preserve the user's physical cursor and keyboard for their own work.

## What this is not

- It is not permission to submit third-party forms.
- It is not permission to change account settings, accept loans, sign forms, send messages, or upload sensitive files.
- It is not a full desktop-control method for non-browser apps.

## Preferred routing

Use this before desktop-coordinate tools such as `xdotool` or `ydotool` when the work is inside a browser page.
