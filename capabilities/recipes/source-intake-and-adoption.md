---
id: source-intake-and-adoption
name: Source Intake And Adoption
schema_version: 2.0
level: recipe
maturity: candidate
scope: machine-wide Wardenclyffe/Codex idea intake
currently_true: unknown
verification_level: 1
last_verified: 2026-05-05
evidence_quality: direct
successful_uses: 1
failed_uses: 0
regressions: 0
depends_on:
  - current-truth-needs-evidence
  - safe-visual-asset-sourcing-and-generation
used_by: []
tags:
  - source intake
  - idea capture
  - public APIs
  - repositories
  - link intake
  - attribution
  - wardenclyffe
---

## What it does

Turns links, videos, repositories, API catalogs, tools, screenshots, and quick
ideas into usable Wardenclyffe intake cards without copying blindly, scraping
recklessly, or letting useful references disappear into chat history.

## When to reach for it

Use this when the user shares a source for possible adoption, inspiration,
research, tool scouting, API discovery, project seeds, repo collection, visual
reference, TikTok/YouTube/social video ideas, or "this might be useful later"
material.

Use it especially when:

- The source is a public repository, API list, tool, product pattern, or social
  post that could influence future work.
- The user is collecting broadly and wants future creative extraction.
- The source may have licensing, platform terms, client privacy, or attribution
  implications.
- The idea belongs to Wardenclyffe generally rather than a single active repo.

## How to use it

1. Preserve the original source.
   - Keep the canonical link.
   - Capture the user's reason for sharing it when stated.
   - Do not replace the user's source with a summary-only memory.
2. Classify the item.
   - **Idea:** concept, workflow, UX pattern, or product shape.
   - **Repo:** codebase, library, template, example, or self-hosted tool.
   - **API:** data source, service endpoint, API catalog, or integration lead.
   - **Tool:** usable app, CLI, service, plugin, or workflow helper.
   - **Visual reference:** layout, motion, image style, product shot, diagram, or
     UI reference.
   - **Media/content source:** video, audio, transcript, article, thread, or
     social post.
   - **Project/client relevant:** tied to a named repo, client, launch, or
     business decision.
3. Verify only what matters for the current decision.
   - For repos: check license, activity, docs, install/runtime shape, and whether
     adoption would create obligations.
   - For APIs: check auth, free tier, CORS, rate limits, terms, current docs, and
     one tiny proof request before treating it as usable.
   - For tools: check official source, local/self-host path, data flow, license,
     and whether hosted APIs forbid third-party reuse.
   - For media: check access, ownership, attribution, allowed use, and whether
     extraction is necessary or a summary is enough.
4. Extract the reusable principle.
   - Prefer "what pattern is worth learning from this?" over "how do we copy
     this?"
   - Separate product insight, UX shape, data capability, technical method,
     business model, and style reference.
5. Decide an adoption lane.
   - **Note:** keep as reference only.
   - **Pattern:** turn into a reusable capability or design principle.
   - **Project seed:** attach to a specific queue, handoff, or workstream.
   - **Investigation:** schedule a bounded verification pass.
   - **Reject/archive:** keep the source but record why it is not a fit.
6. Record a short intake card when the item should survive the conversation.
   - Source:
   - User signal:
   - Classification:
   - Why it matters:
   - Verification needed:
   - Rights/terms caveat:
   - Possible use:
   - Next lane:
7. Keep attribution and boundaries visible.
   - Store source links with derived ideas.
   - Do not present public inspiration as original proof, client work, or a
     completed implementation.
   - Do not copy code, media, names, branding, or proprietary methods unless the
     license and use case allow it.

## What it depends on

- [Current Truth Needs Evidence](../principles/current-truth-needs-evidence.md) -
  avoids treating stale links, API claims, or tool docs as current truth.
- [Safe Visual Asset Sourcing and Generation](safe-visual-asset-sourcing-and-generation.md) -
  handles visual and media rights when an intake item may become an asset.

## Failure modes

- **Link pile without routing.** A saved link with no classification, signal, or
  lane becomes clutter instead of reusable knowledge.
- **Copying instead of extracting.** The useful move is usually to adopt the
  principle, not duplicate the source.
- **Hosted API misuse.** A public web tool may expose docs but still forbid
  using its hosted API from other projects.
- **Stale API assumption.** Catalog entries can be old. Verify the exact API
  before building around it.
- **Rights drift.** A social post, video, screenshot, or repo can inspire a
  direction without granting reuse rights.
- **Client scope leak.** Client-specific discoveries should move into the
  relevant project docs instead of global machine guidance.

## Examples

`public-apis/public-apis` is a good API scouting source, not proof that any
listed API is currently free, healthy, or production-ready. Use it to find
candidate APIs, then verify the chosen API directly.

`imputnet/cobalt` is useful as a clean source-intake UX pattern: paste a link,
normalize the output, preserve the source, and move on. Its hosted API should
not be reused without permission; if API behavior matters, verify self-hosting
or explicit access first.
