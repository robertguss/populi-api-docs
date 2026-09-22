"""`populi-docs`: keep a local, LLM-oriented copy of Populi's API2 reference.

    populi-docs check          is the live reference newer than this copy?
    populi-docs sync           fetch and rebuild if it is (--force to refetch)
    populi-docs build          rebuild reference/ from raw/, offline
    populi-docs diff           what changed in the reference since a git ref

Exit codes: 0 done or up to date; 1 (check only) a newer version is live;
2 something failed and nothing was written.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import httpx

from .diff import diff_catalogs, format_changes, headline
from .fetch import Fetcher
from .parse import ParseError, docs_stamp
from .sync import (
    RAW,
    SCRATCH,
    build_from_raw,
    fetch_raw,
    git_commit,
    install,
    load_catalog,
    load_meta,
    record_changes,
    sanity,
)


def default_root() -> Path:
    env = os.environ.get("POPULI_DOCS_ROOT")
    if env:
        return Path(env).expanduser()
    checkout = Path(__file__).resolve().parents[2]
    if (checkout / "pyproject.toml").exists():
        return checkout
    return Path.cwd()


def cmd_check(root: Path) -> int:
    meta = load_meta(root)
    local = meta["docs_updated_on"] if meta else None
    with Fetcher() as fetcher:
        live = docs_stamp(fetcher.get(""))
    if live == local:
        print(f"up to date: {live}")
        return 0
    print(f"newer docs live: {live} (this copy: {local or 'none'})")
    return 1


def cmd_sync(root: Path, force: bool, allow_shrink: bool, commit: bool) -> int:
    meta = load_meta(root)
    scratch = root / SCRATCH
    shutil.rmtree(scratch, ignore_errors=True)
    scratch.mkdir()
    with Fetcher() as fetcher:
        index_html = fetcher.get("")
        stamp = docs_stamp(index_html)
        if meta and meta.get("docs_updated_on") == stamp and not force:
            shutil.rmtree(scratch)
            print(f"up to date: {stamp}")
            return 0
        print(f"fetching the reference, docs version {stamp}")
        fetch_raw(fetcher, scratch / RAW, index_html, print)

    build = build_from_raw(scratch / RAW)
    old = load_catalog(root)
    problems = sanity(old, build)
    if problems:
        print("sanity checks failed:", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        if not allow_shrink:
            print(
                f"nothing written; the fetched pages are in {scratch / RAW}. "
                "Fix the parser, or rerun with --allow-shrink if the change is real.",
                file=sys.stderr,
            )
            return 2
    install(root, build, scratch / RAW)
    changes = diff_catalogs(old, build.catalog) if old else None
    if old and old["docs_updated_on"] == build.stamp and not changes:
        # A forced refetch of the version we already have: nothing to record.
        line = "refetched the same docs version; no structural changes"
    else:
        line = record_changes(root, build, changes)
    report(build, line)
    if commit:
        committed = git_commit(root, f"Populi docs {build.stamp}: {line}")
        print("committed" if committed else "nothing to commit")
    return 0


def cmd_build(root: Path) -> int:
    old = load_catalog(root)
    build = build_from_raw(root / RAW)
    for problem in sanity(old, build):
        print(f"warning: {problem}", file=sys.stderr)
    install(root, build, None)
    line = headline(diff_catalogs(old, build.catalog)) if old else "first build"
    report(build, f"against the previous build: {line}")
    return 0


def cmd_diff(root: Path, against: str) -> int:
    new = load_catalog(root)
    if new is None:
        print("no reference/catalog.json; run populi-docs sync first", file=sys.stderr)
        return 2
    shown = subprocess.run(
        ["git", "-C", str(root), "show", f"{against}:reference/catalog.json"],
        capture_output=True,
        text=True,
    )
    if shown.returncode != 0:
        print(shown.stderr.strip(), file=sys.stderr)
        return 2
    old = json.loads(shown.stdout)
    print(
        f"{old['docs_updated_on']} ({against}) → "
        f"{new['docs_updated_on']} (working copy)\n"
    )
    print(format_changes(diff_catalogs(old, new)))
    return 0


def report(build, line: str) -> None:
    counts = build.catalog["counts"]
    print(
        f"docs {build.stamp}: {counts['models']} models, "
        f"{counts['endpoints']} endpoints, "
        f"{counts['webhook_events']} webhook events"
    )
    print(line)
    if build.warnings:
        print(f"{len(build.warnings)} parser warnings (in reference/catalog.json):")
        for warning in build.warnings[:10]:
            print(f"  - {warning}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="populi-docs",
        description="Keep a local, LLM-oriented copy of Populi's API2 reference.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=default_root(),
        help="the populi-api-docs checkout (default: this package's checkout, "
        "or $POPULI_DOCS_ROOT)",
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="is the live reference newer than this copy?")
    sync = sub.add_parser(
        "sync", help="fetch and rebuild if the live reference changed"
    )
    sync.add_argument("--force", action="store_true", help="refetch even if unchanged")
    sync.add_argument(
        "--allow-shrink",
        action="store_true",
        help="install even if the sanity checks fail",
    )
    sync.add_argument("--commit", action="store_true", help="git commit the result")
    sub.add_parser("build", help="rebuild reference/ from raw/, offline")
    diff = sub.add_parser("diff", help="changes to the reference since a git ref")
    diff.add_argument("--against", default="HEAD", help="git ref (default: HEAD)")
    args = parser.parse_args(argv)
    root = args.root.resolve()

    try:
        if args.command == "check":
            return cmd_check(root)
        if args.command == "sync":
            return cmd_sync(root, args.force, args.allow_shrink, args.commit)
        if args.command == "build":
            return cmd_build(root)
        return cmd_diff(root, args.against)
    except (httpx.HTTPError, ParseError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
