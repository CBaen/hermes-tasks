#!/usr/bin/env python
"""Validate capability cards and write a compact retrieval registry.

This tool intentionally uses only the Python standard library so it can run on
project machines without package setup.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


FORMAL_LEVELS = {
    "atomic_ingredient": "atomic_ingredients",
    "ingredient": "ingredients",
    "principle": "principles",
    "recipe": "recipes",
    "meal": "meals",
    "feast": "feasts",
}
SPECIAL_DIRS = {
    "kitchen",
    "failures",
    "evidence",
    "registry",
    "tools",
    "adapters",
    "templates",
}
ROOT_DOCS = {"INDEX.md", "SCHEMA.md", "README.md", "ROOTS.md"}
MATURITIES = {"kitchen", "candidate", "verified", "staple", "deprecated"}
PROFILES = {"foundation", "governed", "composition", "cascade"}
CURRENTLY_TRUE = {"true", "false", "unknown", True, False}
EVIDENCE_QUALITY = {"direct", "inferred", "retrofitted", "mixed", "unknown"}
WATCH_STATUS = {"clear", "watch", "failed", "stale", "probation", "revalidating", "unknown"}
FOUNDATION_REQUIRED = {
    "id",
    "name",
    "schema_version",
    "profile",
    "level",
    "maturity",
    "scope",
    "currently_true",
    "last_verified",
    "tags",
}
GOVERNED_REQUIRED = FOUNDATION_REQUIRED | {
    "verification_level",
    "evidence_quality",
    "successful_uses",
    "failed_uses",
    "regressions",
    "depends_on",
    "used_by",
}
COMPOSITION_REQUIRED = GOVERNED_REQUIRED | {
    "watch_status",
    "last_success",
    "last_failure",
    "confidence_notes",
}
PROFILE_REQUIRED = {
    "foundation": FOUNDATION_REQUIRED,
    "governed": GOVERNED_REQUIRED,
    "composition": COMPOSITION_REQUIRED,
    "cascade": COMPOSITION_REQUIRED,
}


@dataclass
class Card:
    path: Path
    relpath: str
    frontmatter: dict[str, Any]
    status: str
    warnings: list[str]


def scalar(value: str) -> Any:
    value = value.strip()
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip("\"'") for item in inner.split(",")]
    lower = value.lower()
    if lower == "true":
        return True
    if lower == "false":
        return False
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value.strip("\"'")


def parse_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---"):
        return {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    end = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = index
            break
    if end is None:
        return {}

    data: dict[str, Any] = {}
    current_key: str | None = None
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("  - ") and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(scalar(raw[4:]))
            continue
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        if value == "":
            data[key] = []
        else:
            data[key] = scalar(value)
    return data


def first_folder(relpath: str) -> str:
    parts = Path(relpath).parts
    if len(parts) <= 1:
        return ""
    return parts[0]


def slug_from_path(relpath: str) -> str:
    path = Path(relpath)
    folder = path.parts[0] if len(path.parts) > 1 else "root"
    return f"{folder}:{path.stem}".lower()


def analyze_card(path: Path, root: Path) -> Card:
    relpath = path.relative_to(root).as_posix()
    warnings: list[str] = []
    folder = first_folder(relpath)
    name = path.name

    if name in ROOT_DOCS or name == ".gitkeep":
        return Card(path, relpath, {}, "support", warnings)
    if folder in SPECIAL_DIRS - {"kitchen", "failures"}:
        return Card(path, relpath, {}, "support", warnings)

    text = path.read_text(encoding="utf-8-sig", errors="replace")
    fm = parse_frontmatter(text)

    if folder == "failures":
        if fm.get("type") != "failure":
            warnings.append("failure file missing type: failure")
        for field in ("name", "date_discovered"):
            if field not in fm:
                warnings.append(f"missing {field}")
        return Card(path, relpath, fm, "failure", warnings)

    if folder == "kitchen":
        status = "kitchen"
        if fm and fm.get("maturity") not in (None, "kitchen", "candidate"):
            warnings.append("kitchen entry should not claim verified/staple maturity")
        return Card(path, relpath, fm, status, warnings)

    if not fm:
        return Card(path, relpath, fm, "retrofit_needed", ["missing frontmatter"])

    version = str(fm.get("schema_version", "")).strip()
    if version in {"", "1.0", "1.1"}:
        for field in ("name", "level", "last_verified"):
            if field not in fm:
                warnings.append(f"missing legacy field {field}")
        if "level" in fm:
            expected = FORMAL_LEVELS.get(str(fm["level"]))
            if expected and folder != expected:
                warnings.append(f"level {fm['level']} does not match folder {folder}")
        return Card(path, relpath, fm, "legacy", warnings)

    if version not in {"2.0", "2.1"}:
        warnings.append(f"unknown schema_version {version}")

    if version == "2.0":
        profile = "governed"
    else:
        profile = str(fm.get("profile", "foundation")).strip() or "foundation"
        if profile not in PROFILES:
            warnings.append(f"invalid profile {profile}")
            profile = "foundation"

    required_fields = PROFILE_REQUIRED[profile]
    if version == "2.0":
        required_fields = required_fields - {"profile"}
    missing = sorted(required_fields - set(fm))
    for field in missing:
        warnings.append(f"missing {profile} field {field}")

    level = str(fm.get("level", ""))
    expected_folder = FORMAL_LEVELS.get(level)
    if not expected_folder:
        warnings.append(f"invalid level {level}")
    elif folder != expected_folder:
        warnings.append(f"level {level} does not match folder {folder}")

    maturity = str(fm.get("maturity", ""))
    if maturity and maturity not in MATURITIES:
        warnings.append(f"invalid maturity {maturity}")

    if fm.get("currently_true") not in CURRENTLY_TRUE:
        warnings.append("currently_true must be true, false, or unknown")

    true_value = fm.get("currently_true") is True or str(fm.get("currently_true")).lower() == "true"
    if profile == "foundation":
        if true_value:
            warnings.append("foundation profile cannot set currently_true: true")
        if maturity in {"verified", "staple"}:
            warnings.append("foundation profile cannot claim verified/staple maturity")

    try:
        verification_level = int(fm.get("verification_level", 0 if profile == "foundation" else -1))
    except (TypeError, ValueError):
        verification_level = -1
    if verification_level not in {0, 1, 2, 3}:
        warnings.append("verification_level must be 0, 1, 2, or 3")
    if profile == "foundation" and verification_level > 1:
        warnings.append("foundation profile should not use verification_level above 1")

    evidence_quality = str(fm.get("evidence_quality", "unknown"))
    if evidence_quality not in EVIDENCE_QUALITY:
        warnings.append("invalid evidence_quality")

    for count_field in ("successful_uses", "failed_uses", "regressions"):
        value = fm.get(count_field, 0)
        if not isinstance(value, int) or value < 0:
            warnings.append(f"{count_field} must be a non-negative integer")

    if profile in {"composition", "cascade"}:
        watch_status = str(fm.get("watch_status", "unknown"))
        if watch_status not in WATCH_STATUS:
            warnings.append("watch_status must be clear, watch, failed, stale, probation, revalidating, or unknown")
        if not fm.get("depends_on") and not fm.get("used_by"):
            warnings.append(f"{profile} profile should declare depends_on or used_by")

    if true_value:
        successes = fm.get("successful_uses", 0)
        regressions = fm.get("regressions", 0)
        if not isinstance(successes, int) or successes < 3:
            warnings.append("currently_true requires at least 3 successful_uses")
        if regressions != 0:
            warnings.append("currently_true requires 0 open regressions")
        if maturity not in {"verified", "staple"}:
            warnings.append("currently_true requires maturity verified or staple")
        if profile == "foundation":
            warnings.append("currently_true requires a governed, composition, or cascade profile")

    return Card(path, relpath, fm, "ok" if not warnings else "warn", warnings)


def card_record(card: Card) -> dict[str, Any]:
    fm = card.frontmatter
    return {
        "id": fm.get("id") or slug_from_path(card.relpath),
        "name": fm.get("name") or Path(card.relpath).stem.replace("-", " ").title(),
        "path": card.relpath,
        "schema_version": fm.get("schema_version") or "legacy-or-none",
        "profile": fm.get("profile") or ("governed" if str(fm.get("schema_version", "")) == "2.0" else "foundation"),
        "level": fm.get("level") or first_folder(card.relpath),
        "maturity": fm.get("maturity") or ("kitchen" if card.status == "kitchen" else "legacy"),
        "currently_true": fm.get("currently_true", "unknown"),
        "verification_level": fm.get("verification_level", 0),
        "last_verified": fm.get("last_verified", "unknown"),
        "evidence_quality": fm.get("evidence_quality", "retrofitted" if card.status == "legacy" else "unknown"),
        "successful_uses": fm.get("successful_uses", 0),
        "failed_uses": fm.get("failed_uses", 0),
        "regressions": fm.get("regressions", 0),
        "watch_status": fm.get("watch_status", "unknown"),
        "last_success": fm.get("last_success", "unknown"),
        "last_failure": fm.get("last_failure", "unknown"),
        "tags": fm.get("tags", []),
        "status": card.status,
        "warnings": card.warnings,
    }


def iter_markdown(root: Path) -> list[Path]:
    ignored_dirs = {".git", "__pycache__"}
    paths: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in ignored_dirs for part in path.parts):
            continue
        paths.append(path)
    return sorted(paths)


def analyze_root(root: Path) -> list[Card]:
    return [analyze_card(path, root) for path in iter_markdown(root)]


def write_registry(root: Path, cards: list[Card]) -> Path:
    registry_dir = root / "registry"
    registry_dir.mkdir(exist_ok=True)
    output = registry_dir / "capability-registry.jsonl"
    records = [
        card_record(card)
        for card in cards
        if card.status not in {"support"} and not card.relpath.startswith("registry/")
    ]
    with output.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=True, sort_keys=True) + "\n")
    return output


def print_summary(root: Path, cards: list[Card]) -> int:
    counts: dict[str, int] = {}
    warning_count = 0
    for card in cards:
        counts[card.status] = counts.get(card.status, 0) + 1
        warning_count += len(card.warnings)
    print(f"root={root}")
    for key in sorted(counts):
        print(f"{key}={counts[key]}")
    print(f"warnings={warning_count}")

    for card in cards:
        if card.warnings:
            print(f"- {card.relpath}: {'; '.join(card.warnings)}")
    return 1 if warning_count else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, help="Capability root to scan.")
    parser.add_argument("--write-registry", action="store_true", help="Write registry/capability-registry.jsonl.")
    parser.add_argument("--strict", action="store_true", help="Exit nonzero on warnings.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        raise SystemExit(f"root does not exist: {root}")

    cards = analyze_root(root)
    warning_exit = print_summary(root, cards)
    if args.write_registry:
        output = write_registry(root, cards)
        print(f"registry={output}")

    return warning_exit if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
