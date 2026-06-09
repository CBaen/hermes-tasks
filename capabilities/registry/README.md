# Registry

This folder contains generated retrieval indexes.

The registry is intentionally compact. It lets agents see names, ids, profiles,
levels, maturity, watch status, tags, and paths without loading every capability
file.

Regenerate it with:

```bash
python /home/guidingl/projects/capabilities-framework/tools/capability_registry.py --root /home/guidingl/capabilities --write-registry
```
