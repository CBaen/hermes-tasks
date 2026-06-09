#!/usr/bin/env python
"""Validate safety-contract Markdown artifacts.

The validator is intentionally small and standard-library only. It checks for
the missing middle that release gates often skip: every risky guard needs both a
negative verifier and a positive preservation verifier.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REQUIRED_SECTIONS = [
    "Change",
    "Bad Thing To Block",
    "Good Thing To Preserve",
    "Deferred Or Out Of Scope",
    "Negative Guard",
    "Positive Guard",
    "Evidence",
    "Owner",
    "Promotion Rule",
    "Rollback / Revalidation Path",
]

GUARD_SECTIONS = {"Negative Guard", "Positive Guard"}
PLACEHOLDER_RE = re.compile(r"<[^>]+>|\b(TBD|TODO|FIXME)\b", re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*$", re.MULTILINE)


@dataclass
class ContractResult:
    path: str
    ok: bool
    errors: list[str]
    warnings: list[str]


def normalize_heading(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def section_map(text: str) -> dict[str, str]:
    matches = list(HEADING_RE.finditer(text))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        label = normalize_heading(match.group(2))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[label] = text[start:end].strip()
    return sections


def has_labeled_value(content: str, label: str) -> bool:
    return bool(re.search(rf"(?im)^\s*(?:-\s*)?{re.escape(label)}\s*:\s*\S", content))


def useful_content(content: str) -> bool:
    stripped = content.strip()
    return bool(stripped) and not PLACEHOLDER_RE.fullmatch(stripped)


def validate_text(text: str, path: Path) -> ContractResult:
    sections = section_map(text)
    errors: list[str] = []
    warnings: list[str] = []

    for heading in REQUIRED_SECTIONS:
        key = normalize_heading(heading)
        content = sections.get(key)
        if content is None:
            errors.append(f"missing section: {heading}")
            continue
        if not useful_content(content):
            errors.append(f"section has no usable content: {heading}")
            continue
        if PLACEHOLDER_RE.search(content):
            errors.append(f"section still contains placeholder text: {heading}")

    for heading in GUARD_SECTIONS:
        content = sections.get(normalize_heading(heading), "")
        if not content:
            continue
        if not has_labeled_value(content, "Verifier"):
            errors.append(f"{heading} must include a Verifier: line")
        if not has_labeled_value(content, "Expected result"):
            errors.append(f"{heading} must include an Expected result: line")

    evidence = sections.get(normalize_heading("Evidence"), "")
    if evidence and not has_labeled_value(evidence, "Evidence path"):
        errors.append("Evidence must include an Evidence path: line")

    return ContractResult(path=str(path), ok=not errors, errors=errors, warnings=warnings)


def iter_targets(paths: Iterable[str]) -> list[Path]:
    targets: list[Path] = []
    for raw in paths:
        path = Path(raw)
        if path.is_dir():
            targets.extend(sorted(path.rglob("*.md")))
        else:
            targets.append(path)
    return targets


def validate_path(path: Path) -> ContractResult:
    if not path.exists():
        return ContractResult(str(path), False, [f"path does not exist: {path}"], [])
    if not path.is_file():
        return ContractResult(str(path), False, [f"path is not a file: {path}"], [])
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    return validate_text(text, path)


def payload(results: list[ContractResult]) -> dict[str, object]:
    return {
        "ok": all(result.ok for result in results) and bool(results),
        "checked": len(results),
        "results": [
            {
                "path": result.path,
                "ok": result.ok,
                "errors": result.errors,
                "warnings": result.warnings,
            }
            for result in results
        ],
    }


def print_text(data: dict[str, object]) -> None:
    print(f"ok={str(data['ok']).lower()}")
    print(f"checked={data['checked']}")
    for result in data["results"]:  # type: ignore[index]
        print(f"- {result['path']}: ok={str(result['ok']).lower()}")
        for error in result["errors"]:
            print(f"  error: {error}")
        for warning in result["warnings"]:
            print(f"  warning: {warning}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="Safety contract Markdown file or directory paths.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable output.")
    args = parser.parse_args()

    results = [validate_path(path) for path in iter_targets(args.paths)]
    data = payload(results)
    if args.json:
        print(json.dumps(data, indent=2, sort_keys=True))
    else:
        print_text(data)
    return 0 if data["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
