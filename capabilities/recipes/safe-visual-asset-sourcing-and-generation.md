---
id: safe-visual-asset-sourcing-and-generation
name: Safe visual asset sourcing and generation
schema_version: 1.1
profile: foundation
level: recipe
maturity: candidate
scope: visual asset sourcing, generation, and publishing
currently_true: unknown
last_verified: 2026-05-02
---

## What it does

Gives agents a safe workflow for sourcing, generating, editing, and publishing visual assets without trusting stale asset packs, unclear rights, AI-recreated trademarks, fake proof imagery, or unsafe files.

## When to reach for it

Use this when a project needs any visual asset: social icons, SVGs, brand badges, trust bars, review-platform links, client/partner logos, app-store badges, payment marks, lifestyle images, generated hero art, blog images, product mockups, representative decor renders, photo post-production, gallery images, or visual proof of prior work.

Use it especially when:

- The user points to a GitHub icon repo, Canva asset, image search result, screenshot, or generated image.
- The asset may imply a business claim, completed work, client relationship, product shape, or current platform logo.
- The mark or platform may have changed recently, such as Twitter becoming X.
- The asset will appear on a client or production website.
- The design calls for generated style consistency across a website, blog, product page, gallery, or marketing surface.

## How to use it

1. Classify the asset before making or copying it.
   - **Exact mark:** third-party logo, payment mark, platform icon, app-store badge, client logo. Use current official or clearly licensed vector sources. Do not AI-generate.
   - **Proof photo:** real client work, completed install, review photo, gallery image, portfolio image. Use only with permission/source confidence. Do not generate or stage as proof.
   - **Representative/product render:** generated product image, decor concept, size cue, variant illustration, or balloon structure mockup. Allowed, but label and manage it as representative unless the business confirms otherwise.
   - **Lifestyle/editorial image:** generated hero, blog, service, seasonal, or mood image. Allowed when it supports the brand and does not imply a false event, client, or completed install.
   - **Decorative asset:** pattern, texture, icon, UI graphic, background, divider, or non-claim visual. Generated or Canva-built assets are usually fine after rights/export checks.
2. Identify the exact surface and user-facing claim.
   - A gallery image says "we did this."
   - A product render says "this is what this option can look like."
   - A blog image says "this supports the article."
   - A social icon says "this links to this current platform."
3. Verify rights and source.
   - Official brand resources, client-owned photos, user-provided assets with permission, or clearly licensed open-source assets can be acceptable.
   - A public GitHub repo with no license is not safe to copy into a client production site.
   - A screenshot, Google image result, Google review photo, Canva search result, or social post is not enough proof of reuse rights by itself.
4. Decide whether generation or editing is allowed.
   - Use image generation for stylistic website art, blog visuals, representative product/decor renders, backgrounds, mockups, and concept images.
   - Use post-production for real photos when the edits preserve truth: crop, straighten, brighten, color-correct, clean minor distractions, upscale, or prepare responsive sizes.
   - Do not alter proof photos in ways that change what was delivered, who was present, event scale, colors sold, safety conditions, or install quality.
   - Do not generate exact third-party marks or fake "customer photos."
5. For generated images, write prompts from real constraints.
   - Include domain physics, scale cues, material constraints, brand palette, customer type, location, and use case.
   - For balloon decor, preserve construction logic such as classic 4-balloon-cluster arches versus organic garlands, realistic density, attachment points, clearance, and color placement.
   - Record the prompt or source note where future agents can find it if the asset becomes durable.
6. For SVGs and icons, prefer local vendored files over remote hotlinks or package dependencies.
   - Copy only the specific assets needed.
   - Do not install a whole icon package or pull a whole repo for a few assets.
   - Keep filenames stable and obvious, such as `facebook.svg`, `instagram.svg`, `x.svg`, `google-reviews.svg`, or `delivery-truck.svg`.
7. Sanitize SVGs before committing them.
   - Remove `script`, `foreignObject`, external `href` / `xlink:href`, `javascript:`, remote URLs, embedded raster payloads, XML declarations, and DOCTYPE.
   - Keep `xmlns`, `viewBox`, explicit `width` / `height`, and simple path/shape/gradient data.
   - Use stable intrinsic dimensions and avoid layout-shifting assets.
8. Optimize raster images before publishing.
   - Create responsive sizes when the site supports them.
   - Preserve originals in the correct source/archive location when the project has one.
   - Export web-ready formats and dimensions appropriate to the surface.
   - Avoid cropping that hides the important part of the work unless the crop is deliberate for that layout.
   - For repeatable resizing and finishing, use [Image finishing and responsive derivatives](image-finishing-and-responsive-derivatives.md) and the global `image-finishing` skill.
9. Keep accessibility and meaning intentional.
   - Decorative images use empty alt text.
   - Informational images need plain alt text that describes the image's purpose.
   - Proof/gallery images should name the decor type and context without inventing client facts.
   - Link icons should have useful labels like `Locally Twisted on X (opens in new tab)`.
10. Verify in the running site.
   - Clear the website/cache layer when the framework needs it.
   - Confirm every referenced asset returns `200`.
   - Confirm rendered pages reference the intended files and no old stale links remain.
   - Use browser screenshots or DOM checks at desktop and mobile sizes before claiming the visual work is done.
   - Check that images are not badly cropped, distorted, blank, oversized, or text-overlapping.
11. Record the source decision.
   - Add a short queue, workstream, style-guide, or asset manifest note when the decision matters later.
   - Include what source was accepted or rejected, whether the asset is proof or representative, and any permission/rights caveat.

## What it depends on

- [Capability index routing](capability-index-routing.md) - find the nearest project capability and documentation surfaces.

## Failure modes

- **No license found.** Treat the asset as inspiration only. Do not copy it into a client production site.
- **Current mark mismatch.** Stop and update the source. A visually nice icon is still wrong if it is a stale logo.
- **SVG has external or executable content.** Sanitize it or choose a cleaner source.
- **Generated proof looks convincing.** Do not let it imply completed work, a real customer event, or a real client unless that is true and confirmed.
- **Generated logo looks close.** Do not use it as a real third-party logo. Use official/current vectors for exact marks.
- **Pretty image, wrong physics.** For physical products, revise the prompt or reject the image if it shows impossible construction, wrong scale, or misleading density.
- **Only one surface was updated.** Search the whole app for old asset names, stale URLs, and duplicate surfaces before declaring the work complete.

## Examples

For Locally Twisted on 2026-05-02, a GitHub social icon pack looked visually close but was rejected as a production source because the repo had no clear license and still shipped `Twitter.svg` without current `X.svg`. The safe path was to vendor only current, reviewed SVGs and verify the footer and contact page against the running ERPNext site.

For Locally Twisted balloon decor imagery, generated images can be useful for consistent product visuals, style exploration, blog art, and representative size cues. They must not replace real portfolio proof, and prompts need real balloon-construction constraints so arches, columns, garlands, and parade-clearance examples do not misrepresent what the company builds.
