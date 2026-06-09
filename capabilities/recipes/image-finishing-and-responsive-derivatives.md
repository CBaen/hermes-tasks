---
name: Image finishing and responsive derivatives
schema_version: 1.1
level: recipe
last_verified: 2026-05-06
---

## What it does

Gives all Codex projects a machine-wide workflow for preparing raster images before they are used in websites, apps, portfolios, documents, presentations, or generated visual mockups.

This recipe is the routing contract. The executable tool lives in `/home/guidingl/.codex/skills/image-finishing/scripts/finish_images.py`.

## When to reach for it

Use this when a project references large originals, generated images, screenshots, portfolio photos, hero photos, product photos, social graphics, or document images that need resizing, optimization, light cleanup, responsive derivatives, or final visual QA.

Use it especially when:

- An image looks trapped, tiny, distorted, cropped, fuzzy, blank, or too heavy in a rendered surface.
- A portfolio/gallery needs whole-photo proof rather than uniform card crops.
- A page is slow because original PNG/JPEG files are being served directly.
- A design mockup uses good photo placement but the production implementation needs web-ready files.
- Multiple clients/projects under `/home/guidingl/projects` need the same finishing workflow.

## How to use it

1. Classify the asset:
   - **Proof photo:** real client work. Preserve truth and whole-photo readability.
   - **Representative image:** generated/conceptual. Optimize freely, but do not imply completed work.
   - **UI/document image:** preserve text/diagram clarity.
2. Read `/home/guidingl/.codex/skills/image-finishing/SKILL.md`.
3. Load `references/surface-presets.md` from that skill when choosing dimensions.
4. Generate derivatives with `finish_images.py`.
5. Update the consuming project to reference derivatives, not huge originals.
6. Verify in the actual consuming surface at the real breakpoints.

## Defaults

- Preserve aspect ratio.
- Use fit/no-crop mode unless the user or design explicitly calls for a crop.
- Use WebP for web derivatives unless the project needs JPEG/PNG compatibility.
- Keep originals in the project's source/archive location when one exists.
- Do not let layout convenience turn real portfolio photos into uniform cropped cards.

## Verification

Before saying image work is finished:

- Confirm the referenced files exist.
- Confirm web-served assets return `200`.
- Confirm desktop and mobile screenshots show the intended image, not a blank placeholder.
- Confirm no horizontal overflow was introduced.
- Confirm image dimensions match the intended display surface.
- Confirm large originals are not still being loaded by the public route unless intentionally linked for download or modal full-size viewing.

## Related

- [Safe visual asset sourcing and generation](safe-visual-asset-sourcing-and-generation.md) - rights/source/truth classification before using or generating assets.
- [Capability index routing](capability-index-routing.md) - how to decide whether a global, agency, or project capability should own the guidance.
