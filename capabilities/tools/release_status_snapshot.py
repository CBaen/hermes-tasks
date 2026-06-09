#!/usr/bin/env python
"""Create and compare release status snapshots.

The tool is intentionally read-only and standard-library only. It captures
evidence that helps an agent compare local, staging, and live release state
without printing secrets or relying on a specific hosting provider.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen


SNAPSHOT_SCHEMA = "release-status-snapshot/v1"
TITLE_RE = re.compile(rb"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
REMOTE_SECRET_RE = re.compile(r"(https?://)([^/@]+)@")


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def run(command: list[str], cwd: Path) -> tuple[int, str, str]:
    try:
        result = subprocess.run(
            command,
            cwd=str(cwd),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except FileNotFoundError as exc:
        return 127, "", str(exc)
    return result.returncode, result.stdout.rstrip("\r\n"), result.stderr.strip()


def sanitize_remote(value: str) -> str:
    return REMOTE_SECRET_RE.sub(r"\1REDACTED@", value)


def git_state(repo: Path) -> dict[str, Any]:
    state: dict[str, Any] = {
        "path": str(repo),
        "is_git_repo": False,
        "branch": None,
        "head": None,
        "remote_url": None,
        "dirty": None,
        "dirty_count": 0,
        "staged_count": 0,
        "untracked_count": 0,
        "changed_paths": [],
        "warnings": [],
    }
    code, _, _ = run(["git", "rev-parse", "--is-inside-work-tree"], repo)
    if code != 0:
        state["warnings"].append("repo is not a git worktree")
        return state

    state["is_git_repo"] = True
    for key, command in {
        "branch": ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        "head": ["git", "rev-parse", "HEAD"],
        "remote_url": ["git", "config", "--get", "remote.origin.url"],
    }.items():
        code, stdout, stderr = run(command, repo)
        if code == 0:
            state[key] = sanitize_remote(stdout) if key == "remote_url" else stdout
        elif stderr:
            state["warnings"].append(f"{' '.join(command)} failed: {stderr}")

    code, stdout, stderr = run(["git", "status", "--short"], repo)
    if code != 0:
        state["warnings"].append(f"git status failed: {stderr}")
        return state

    changed_paths: list[str] = []
    staged_count = 0
    untracked_count = 0
    for line in stdout.splitlines():
        if not line:
            continue
        status = line[:2]
        path = line[3:].strip()
        changed_paths.append(f"{status} {path}")
        if status == "??":
            untracked_count += 1
        elif status[0] != " ":
            staged_count += 1
    state["changed_paths"] = changed_paths[:500]
    state["dirty_count"] = len(changed_paths)
    state["staged_count"] = staged_count
    state["untracked_count"] = untracked_count
    state["dirty"] = bool(changed_paths)
    if len(changed_paths) > 500:
        state["warnings"].append("changed path list truncated at 500 entries")
    return state


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def split_values(values: list[str] | None) -> list[str]:
    items: list[str] = []
    for value in values or []:
        for part in value.split(","):
            part = part.strip()
            if part:
                items.append(part)
    return items


def watched_files(repo: Path, patterns: list[str]) -> dict[str, Any]:
    files: list[dict[str, Any]] = []
    missing: list[str] = []
    for pattern in patterns:
        matches = sorted(path for path in repo.glob(pattern) if path.is_file())
        if not matches:
            missing.append(pattern)
        for path in matches[:500]:
            relpath = path.relative_to(repo).as_posix()
            files.append(
                {
                    "path": relpath,
                    "sha256": sha256_file(path),
                    "size_bytes": path.stat().st_size,
                }
            )
        if len(matches) > 500:
            missing.append(f"{pattern} matched more than 500 files; snapshot truncated")
    return {"files": files, "missing_patterns": missing}


def env_key_names(repo: Path, env_files: list[str]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for name in env_files:
        path = (repo / name).resolve()
        item: dict[str, Any] = {
            "path": name,
            "present": path.exists() and path.is_file(),
            "key_names": [],
        }
        if item["present"]:
            keys: list[str] = []
            for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
                line = raw_line.strip()
                if not line or line.startswith("#"):
                    continue
                if line.startswith("export "):
                    line = line[len("export ") :].strip()
                if "=" not in line:
                    continue
                key = line.split("=", 1)[0].strip()
                if key and re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
                    keys.append(key)
            item["key_names"] = sorted(set(keys))
        results.append(item)
    return results


def normalize_route(route: str) -> str:
    if route.startswith("http://") or route.startswith("https://"):
        return route
    if not route.startswith("/"):
        route = "/" + route
    return route


def page_title(body: bytes) -> str | None:
    match = TITLE_RE.search(body[:200_000])
    if not match:
        return None
    title = re.sub(rb"\s+", b" ", match.group(1)).strip()
    return title.decode("utf-8", errors="replace")[:200]


def fetch_route(target_url: str, route: str, timeout: float) -> dict[str, Any]:
    normalized = normalize_route(route)
    url = normalized if normalized.startswith(("http://", "https://")) else urljoin(target_url.rstrip("/") + "/", normalized.lstrip("/"))
    item: dict[str, Any] = {
        "route": route,
        "url": url,
        "status": None,
        "ok": False,
        "final_url": None,
        "body_sha256": None,
        "body_size_bytes": None,
        "title": None,
        "error": None,
    }
    try:
        request = Request(url, headers={"User-Agent": "CodexReleaseSnapshot/1.0"})
        with urlopen(request, timeout=timeout) as response:
            body = response.read()
            status = getattr(response, "status", response.getcode())
            item.update(
                {
                    "status": int(status),
                    "ok": 200 <= int(status) < 400,
                    "final_url": response.geturl(),
                    "body_sha256": hashlib.sha256(body).hexdigest(),
                    "body_size_bytes": len(body),
                    "title": page_title(body),
                }
            )
    except HTTPError as exc:
        body = exc.read()
        item.update(
            {
                "status": int(exc.code),
                "ok": False,
                "final_url": exc.geturl(),
                "body_sha256": hashlib.sha256(body).hexdigest() if body else None,
                "body_size_bytes": len(body),
                "title": page_title(body) if body else None,
                "error": str(exc),
            }
        )
    except (URLError, TimeoutError, OSError) as exc:
        item["error"] = str(exc)
    return item


def http_snapshot(target_url: str | None, routes: list[str], timeout: float) -> dict[str, Any]:
    result: dict[str, Any] = {"target_url": target_url, "routes": [], "failures": []}
    if not target_url and routes:
        result["failures"].append("routes were provided without --target-url")
        return result
    if not target_url:
        return result
    for route in routes:
        item = fetch_route(target_url, route, timeout)
        result["routes"].append(item)
        if not item["ok"]:
            result["failures"].append(f"{route} returned {item['status'] or item['error']}")
    return result


def make_snapshot(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    repo = Path(args.repo).resolve()
    warnings: list[str] = []
    if not repo.exists():
        raise SystemExit(f"repo path does not exist: {repo}")
    if not repo.is_dir():
        raise SystemExit(f"repo path is not a directory: {repo}")

    watch = watched_files(repo, split_values(args.watch))
    if watch["missing_patterns"]:
        warnings.extend(f"watch pattern missing: {pattern}" for pattern in watch["missing_patterns"])

    http = http_snapshot(args.target_url, split_values(args.routes), args.timeout)
    warnings.extend(http["failures"])

    git = git_state(repo)
    warnings.extend(git.pop("warnings", []))

    snapshot = {
        "schema_version": SNAPSHOT_SCHEMA,
        "created_at_utc": now_utc(),
        "label": args.label,
        "environment": args.environment,
        "repo": git,
        "watch": watch,
        "env_files": env_key_names(repo, split_values(args.env_file)),
        "http": http,
        "warnings": warnings,
    }
    return snapshot, 2 if http["failures"] else 0


def by_path(files: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(item.get("path")): item for item in files}


def compare_snapshots(base: dict[str, Any], other: dict[str, Any], strict_body: bool) -> dict[str, Any]:
    critical: list[dict[str, Any]] = []
    info: list[dict[str, Any]] = []

    def add(bucket: list[dict[str, Any]], field: str, left: Any, right: Any) -> None:
        bucket.append({"field": field, "base": left, "other": right})

    for field in ("branch", "head", "remote_url"):
        left = base.get("repo", {}).get(field)
        right = other.get("repo", {}).get(field)
        if left and right and left != right:
            add(critical, f"repo.{field}", left, right)

    base_files = by_path(base.get("watch", {}).get("files", []))
    other_files = by_path(other.get("watch", {}).get("files", []))
    for path in sorted(set(base_files) | set(other_files)):
        left = base_files.get(path, {}).get("sha256")
        right = other_files.get(path, {}).get("sha256")
        if left != right:
            add(critical, f"watch.{path}.sha256", left, right)

    for index, (left_env, right_env) in enumerate(zip(base.get("env_files", []), other.get("env_files", []))):
        left_keys = left_env.get("key_names", [])
        right_keys = right_env.get("key_names", [])
        if left_keys != right_keys:
            add(critical, f"env_files[{index}].key_names", left_keys, right_keys)

    base_routes = {item.get("route"): item for item in base.get("http", {}).get("routes", [])}
    other_routes = {item.get("route"): item for item in other.get("http", {}).get("routes", [])}
    for route in sorted(set(base_routes) | set(other_routes)):
        left = base_routes.get(route, {})
        right = other_routes.get(route, {})
        if left.get("ok") != right.get("ok") or left.get("status") != right.get("status"):
            add(critical, f"http.{route}.status", left.get("status"), right.get("status"))
        if left.get("final_url") != right.get("final_url"):
            add(info, f"http.{route}.final_url", left.get("final_url"), right.get("final_url"))
        if left.get("body_sha256") != right.get("body_sha256"):
            add(critical if strict_body else info, f"http.{route}.body_sha256", left.get("body_sha256"), right.get("body_sha256"))

    return {
        "schema_version": "release-status-comparison/v1",
        "created_at_utc": now_utc(),
        "base_label": base.get("label"),
        "other_label": other.get("label"),
        "critical_changes": critical,
        "informational_changes": info,
        "ok": not critical,
    }


def write_json(path: str | None, payload: dict[str, Any]) -> None:
    if not path:
        return
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create or compare release status snapshots.")
    parser.add_argument("--repo", default=".", help="Repository/project root to inspect.")
    parser.add_argument("--label", default="snapshot", help="Human label for this snapshot.")
    parser.add_argument("--env", dest="environment", default="unknown", help="Environment name, such as local, staging, or live.")
    parser.add_argument("--target-url", help="Base URL to probe.")
    parser.add_argument("--routes", action="append", help="Comma-separated or repeated routes to fetch.")
    parser.add_argument("--watch", action="append", help="Comma-separated or repeated repo-relative file globs to hash.")
    parser.add_argument("--env-file", action="append", help="Optional env files to read for key names only, never values.")
    parser.add_argument("--timeout", type=float, default=10.0, help="HTTP timeout in seconds.")
    parser.add_argument("--out", help="Write snapshot or comparison JSON to this path.")
    parser.add_argument("--compare", nargs=2, metavar=("BASE", "OTHER"), help="Compare two existing snapshot JSON files.")
    parser.add_argument("--strict-body", action="store_true", help="Treat route body hash differences as critical.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.compare:
        base = json.loads(Path(args.compare[0]).read_text(encoding="utf-8"))
        other = json.loads(Path(args.compare[1]).read_text(encoding="utf-8"))
        comparison = compare_snapshots(base, other, args.strict_body)
        write_json(args.out, comparison)
        print(json.dumps(comparison, indent=2, sort_keys=True))
        return 0 if comparison["ok"] else 2

    snapshot, exit_code = make_snapshot(args)
    write_json(args.out, snapshot)
    print(json.dumps(snapshot, indent=2, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
