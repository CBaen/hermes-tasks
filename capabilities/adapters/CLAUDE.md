# Claude Adapter

Claude can use shared capability roots. Claude-era imports and `.claude`
folders are not the canonical capability store.

## Canonical Roots

- System/user root: `/home/guidingl/capabilities/INDEX.md`
- Source package: `/home/guidingl/projects/capabilities-framework/`
- Agency root: `/home/guidingl/projects/Built_by_Cameron/capabilities/INDEX.md` when imported
- Project roots: `<project>/capabilities/INDEX.md`

## How Claude Should Use Capabilities

1. Start from the project or agency entrypoint.
2. Reference the shared visible capability root for reusable operating
   knowledge.
3. Use older `.claude` material as historical/reference evidence unless it has
   been intentionally translated into a shared root. On Banebook, `.claude`
   material is legacy/reference evidence, not a current default path.
4. Do not copy raw `.claude` runtime state, logs, sessions, auth, or private
   transcripts into shared capabilities.
5. If a Claude-specific command or import behavior matters, document it as an
   adapter note, not as the capability source of truth.

## Failure Recipes

Claude should use the same `failures/` / Failure Recipe schema as every other
agent. Do not fork failure records into Claude-only memory when the pattern is
shared.
