#!/usr/bin/env python3
"""Lightweight source-of-truth parity checks for hermes-tasks.

This intentionally checks current docs and git state without reading secrets or
runtime profiles. It is a guardrail, not a proof of every project fact.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ISO_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}")

REQUIRED = [
    "README.md",
    "SOURCE-OF-TRUTH.md",
    "PROJECT-STATUS.md",
    "HANDOFF.md",
    "hermes-tasks-queue.md",
    "hermes-tasks-decisions.md",
    "hermes-tasks-index.md",
    "GLOBAL-DECISIONS.md",
    "LESSONS-LEARNED.md",
    "agent-lanes/BOARD.md",
    "agent-lanes/connections-control-HANDOFF.md",
    "capabilities-connections-control/INDEX.md",
    "capabilities-agent-infrastructure/INDEX.md",
]

CURRENT_STATE_DOCS = [
    "PROJECT-STATUS.md",
    "HANDOFF.md",
    "hermes-tasks-queue.md",
    "agent-lanes/BOARD.md",
]

STALE_CURRENT_PHRASES = [
    "final publish-status commit in progress",
    "publish pending until git push completes",
    "blocked on GitHub authentication after local commit",
    "remote push is blocked by missing GitHub authentication",
]

TIMESTAMP_REQUIRED_PATTERNS = {
    "PROJECT-STATUS.md": r"Last updated:\s*" + ISO_RE.pattern,
    "SOURCE-OF-TRUTH.md": r"Last updated:\s*" + ISO_RE.pattern,
    "HANDOFF.md": r"TS:" + ISO_RE.pattern,
    "agent-lanes/BOARD.md": r"Last updated:\s*" + ISO_RE.pattern,
}


def run(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, cwd=ROOT, text=True, stderr=subprocess.STDOUT).strip()


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f"missing required source-of-truth file: {rel}")

    for rel, pattern in TIMESTAMP_REQUIRED_PATTERNS.items():
        p = ROOT / rel
        if p.exists() and not re.search(pattern, p.read_text(encoding="utf-8")):
            errors.append(f"missing required timestamp pattern in {rel}")

    for rel in CURRENT_STATE_DOCS:
        p = ROOT / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8").lower()
        for phrase in STALE_CURRENT_PHRASES:
            if phrase in text:
                errors.append(f"stale current-state phrase in {rel}: {phrase}")

    try:
        status = run(["git", "status", "--porcelain=v1", "-uall"])
        branch = run(["git", "status", "-sb"])
    except Exception as exc:  # pragma: no cover - defensive CLI path
        errors.append(f"git status failed: {exc}")
        status = ""
        branch = "unknown"

    if status:
        warnings.append("git worktree is dirty; remote HEAD parity skipped until after commit")
    else:
        try:
            head = run(["git", "rev-parse", "HEAD"])
            upstream = run(["git", "rev-parse", "@{u}"])
            if head != upstream:
                errors.append(f"HEAD {head} does not match upstream {upstream}")
        except Exception as exc:
            warnings.append(f"upstream parity not checked: {exc}")

    print("source_of_truth_parity=", "ok" if not errors else "fail")
    print("branch=", branch)
    if warnings:
        print("warnings:")
        for item in warnings:
            print(f"- {item}")
    if errors:
        print("errors:")
        for item in errors:
            print(f"- {item}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
