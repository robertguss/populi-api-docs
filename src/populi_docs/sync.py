"""The pipeline: fetch into a scratch directory, parse, check, then swap in.

Nothing under raw/, reference/, or llms.txt is touched until the new copy has
been fetched completely, parsed, and passed the sanity checks. A site redesign
that breaks the parser therefore stops the sync; it does not write empty docs.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from .diff import Changes, format_changes, headline
from .fetch import Fetcher
from .parse import (
    BASE_URL,
    Model,
    ParseError,
    catalog,
    docs_stamp,
    model_pages,
    parse_model_page,
    parse_overview,
    slug_of,
)
from .render import write_reference

RAW = "raw"
REFERENCE = "reference"
LLMS_TXT = "llms.txt"
CHANGES = "CHANGES.md"
META = "meta.json"
SCRATCH = ".sync-tmp"
OLD = ".sync-old"

# A full copy today is 177 models and 683 endpoints (2026-09-21). A parse that
# finds far fewer means the site changed shape, not that Populi deleted half
# its API.
MIN_MODELS = 100
MIN_ENDPOINTS = 400
MAX_SHRINK = 0.05

CHANGES_HEADER = """# Changes to Populi's API2 reference

One entry per sync that found a new version of the docs, newest first, written
by `populi-docs sync`. Structural changes only: models, endpoints, fields,
parameters, filters, expands, permissions, webhook events, and which endpoint
descriptions were reworded. Examples are not compared.

<!-- entries -->
"""

Log = Callable[[str], None]


@dataclass
class Build:
    models: list[Model]
    overview_md: str
    stamp: str
    warnings: list[str]
    catalog: dict


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def load_meta(root: Path) -> dict | None:
    path = root / RAW / META
    return json.loads(path.read_text()) if path.exists() else None


def load_catalog(root: Path) -> dict | None:
    path = root / REFERENCE / "catalog.json"
    return json.loads(path.read_text()) if path.exists() else None


def fetch_raw(fetcher: Fetcher, dest: Path, index_html: str, log: Log) -> None:
    """Every model page the index links to, plus the index, into `dest`."""
    stamp = docs_stamp(index_html)
    (dest / "models").mkdir(parents=True, exist_ok=True)
    (dest / "index.html").write_text(index_html)
    pages = model_pages(index_html)
    hashes = {"index": sha256(index_html)}
    for i, (_, page) in enumerate(pages, 1):
        html = fetcher.get(page)
        slug = slug_of(page)
        (dest / "models" / f"{slug}.html").write_text(html)
        hashes[slug] = sha256(html)
        if i % 25 == 0 or i == len(pages):
            log(f"  fetched {i}/{len(pages)} pages")
    meta = {
        "source": BASE_URL,
        "docs_updated_on": stamp,
        "fetched_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "pages": hashes,
    }
    (dest / META).write_text(json.dumps(meta, indent=1) + "\n")


def build_from_raw(raw: Path) -> Build:
    index_html = (raw / "index.html").read_text()
    stamp = docs_stamp(index_html)
    meta = json.loads((raw / META).read_text()) if (raw / META).exists() else {}
    models: list[Model] = []
    warnings: list[str] = []
    for name, page in model_pages(index_html):
        path = raw / "models" / f"{slug_of(page)}.html"
        if not path.exists():
            raise ParseError(f"missing page {path}")
        model, page_warnings = parse_model_page(path.read_text(), name, page)
        models.append(model)
        warnings.extend(page_warnings)
    cat = catalog(models, stamp, meta.get("fetched_at", ""), warnings)
    return Build(models, parse_overview(index_html), stamp, warnings, cat)


def sanity(old: dict | None, build: Build) -> list[str]:
    """Reasons not to install this build; empty when it looks whole."""
    problems = []
    counts = build.catalog["counts"]
    if counts["models"] < MIN_MODELS:
        problems.append(
            f"only {counts['models']} models (expected at least {MIN_MODELS})"
        )
    if counts["endpoints"] < MIN_ENDPOINTS:
        problems.append(
            f"only {counts['endpoints']} endpoints (expected at least {MIN_ENDPOINTS})"
        )
    empty = [
        m["name"]
        for m in build.models
        if not (m["objects"] or m["actions"] or m["webhook_events"])
    ]
    if empty:
        problems.append(f"pages that parsed to nothing: {', '.join(empty)}")
    if old:
        for key in ("models", "endpoints"):
            before, after = old["counts"][key], counts[key]
            if after < before * (1 - MAX_SHRINK):
                problems.append(f"{key} fell from {before} to {after}")
    return problems


def stage(root: Path, build: Build) -> Path:
    out = root / SCRATCH / "out"
    shutil.rmtree(out, ignore_errors=True)
    write_reference(out, build.models, build.overview_md, build.stamp, build.catalog)
    return out


def swap(root: Path, replacements: dict[str, Path]) -> None:
    """Move each staged path over its live one, keeping the old until all moved."""
    old = root / OLD
    shutil.rmtree(old, ignore_errors=True)
    old.mkdir()
    for name, new in replacements.items():
        live = root / name
        if live.exists():
            live.rename(old / name)
        new.rename(live)
    shutil.rmtree(old)


def install(root: Path, build: Build, raw: Path | None) -> None:
    out = stage(root, build)
    replacements = {REFERENCE: out / REFERENCE, LLMS_TXT: out / LLMS_TXT}
    if raw is not None:
        replacements = {RAW: raw, **replacements}
    swap(root, replacements)
    shutil.rmtree(root / SCRATCH, ignore_errors=True)


def record_changes(root: Path, build: Build, changes: Changes | None) -> str:
    """Prepend an entry to CHANGES.md; return the one-line summary."""
    path = root / CHANGES
    existing = path.read_text() if path.exists() else CHANGES_HEADER
    marker = "<!-- entries -->\n"
    if marker not in existing:
        existing = CHANGES_HEADER + existing
    head, _, tail = existing.partition(marker)
    counts = build.catalog["counts"]
    today = datetime.now(UTC).date().isoformat()
    if changes is None:
        line = (
            f"first snapshot: {counts['models']} models, {counts['endpoints']} "
            f"endpoints, {counts['webhook_events']} webhook events"
        )
        body = (
            f"First snapshot, synced {today}: {line.removeprefix('first snapshot: ')}."
        )
    else:
        line = headline(changes)
        body = f"Synced {today}.\n\n{format_changes(changes)}"
    entry = f"\n## {build.stamp}\n\n{body}\n"
    path.write_text(head + marker + entry + tail)
    return line


def git_commit(root: Path, message: str) -> bool:
    paths = [RAW, REFERENCE, LLMS_TXT, CHANGES]
    subprocess.run(["git", "-C", str(root), "add", "--", *paths], check=True)
    staged = subprocess.run(["git", "-C", str(root), "diff", "--cached", "--quiet"])
    if staged.returncode == 0:
        return False
    subprocess.run(["git", "-C", str(root), "commit", "-q", "-m", message], check=True)
    return True
