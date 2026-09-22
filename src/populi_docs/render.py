"""Structured models to the Markdown an agent reads.

`llms.txt` is the entry point. `reference/overview.md` is Populi's own
introduction (auth, request format, expands, paging, filters, errors, rate
limits). `reference/endpoints.md` is every endpoint on one line.
`reference/models/<slug>.md` is one page per model.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from .html2md import cell, fence, table_md
from .parse import Model

INTRO = (
    "A local copy of Populi's API2 reference (https://populi.co/api/), "
    "rebuilt for agents by `populi-docs`. Do not edit by hand; run "
    "`populi-docs sync` to refresh."
)


def summary(description: str, limit: int = 140) -> str:
    """The first sentence of a description, one line, trimmed."""
    flat = re.sub(r"\s+", " ", description).strip()
    match = re.match(r"(.+?[.!?])(\s|$)", flat)
    first = match.group(1) if match else flat
    return first if len(first) <= limit else first[: limit - 1].rstrip() + "…"


def endpoints_of(model: Model) -> list[dict]:
    return [a for a in model["actions"] if a["method"]]


def render_llms_txt(models: list[Model], stamp: str) -> str:
    n_endpoints = sum(len(endpoints_of(m)) for m in models)
    lines = [
        "# Populi API2 reference",
        "",
        f"> {INTRO} Docs version: {stamp}. {len(models)} models, "
        f"{n_endpoints} endpoints.",
        "",
        "Start with the overview for how every request works. To find an "
        "endpoint, search `reference/endpoints.md` (one line per endpoint), then "
        "open its model page for fields, parameters, filter conditions, "
        "expands, permissions, and examples.",
        "",
        "## Start here",
        "",
        "- [Overview](reference/overview.md): authentication, request and "
        "response format, expandable objects, paging, filter conditions, "
        "errors, rate limits",
        "- [Endpoints](reference/endpoints.md): every endpoint, one line each, "
        "sorted by path",
        "- [Catalog](reference/catalog.json): the same reference as JSON, for "
        "programs; no examples",
        "- [Changes](CHANGES.md): what changed in Populi's reference, per sync",
        "",
        "## Models",
        "",
    ]
    for m in sorted(models, key=lambda m: m["name"].lower()):
        eps = endpoints_of(m)
        if m["webhook_events"]:
            detail = f"{len(m['webhook_events'])} webhook events and their payloads"
        elif eps:
            paths = sorted({a["path"] for a in eps}, key=lambda p: (len(p), p))[:3]
            more = "" if len(eps) <= 3 else ", …"
            noun = "endpoint" if len(eps) == 1 else "endpoints"
            detail = f"{len(eps)} {noun}: " + ", ".join(f"`{p}`" for p in paths) + more
        else:
            detail = "object only"
        lines.append(f"- [{m['name']}](reference/models/{m['slug']}.md): {detail}")
    return "\n".join(lines) + "\n"


def render_overview(overview_md: str, stamp: str) -> str:
    return (
        f"# Populi API2: overview\n\n> {INTRO} Docs version: {stamp}. Source: "
        f"https://populi.co/api/\n\n{overview_md}\n"
    )


def render_endpoints(models: list[Model], stamp: str) -> str:
    found = [(a["path"], a["method"], a, m) for m in models for a in endpoints_of(m)]
    found.sort(key=lambda item: (item[0], item[1]))
    rows = [
        [
            method,
            f"`{path}`",
            a["name"],
            f"[{m['name']}](models/{m['slug']}.md)",
            summary(a["description"]),
        ]
        for path, method, a, m in found
    ]
    return (
        f"# Populi API2: every endpoint\n\n> {INTRO} Docs version: {stamp}. "
        f"{len(rows)} endpoints, sorted by path. Paths are relative to "
        "`https://<school>.populiweb.com/api2`; `(name)` is an id in the path.\n\n"
        + table_md(["Method", "Path", "Action", "Model", "Summary"], rows)
        + "\n"
    )


def render_params(title: str, items: list[dict], columns: list[tuple[str, str]]) -> str:
    rows = []
    for item in items:
        row = []
        for key, _ in columns:
            value = item.get(key, "")
            if key == "required":
                value = "yes" if value else "no"
            elif key == "name":
                value = f"`{value}`"
            row.append(str(value))
        rows.append(row)
    return f"**{title}**\n\n" + table_md([label for _, label in columns], rows)


def render_action(action: dict) -> str:
    request = (
        f"`{action['method']} {action['path']}`"
        if action["method"]
        else "(no request line)"
    )
    parts = [f"## {action['name']}: {request}"]
    if action["description"]:
        parts.append(action["description"])
    if action["params"]:
        parts.append(
            render_params(
                "Parameters",
                action["params"],
                [
                    ("name", "Name"),
                    ("required", "Required"),
                    ("type", "Type"),
                    ("description", "Description"),
                ],
            )
        )
    if action["params_note"]:
        parts.append(f"**Parameters:** {action['params_note']}")
    if action["filters"]:
        parts.append(
            render_params(
                "Filter conditions (see overview.md, Filter conditions for reports)",
                action["filters"],
                [("name", "Name"), ("type", "Type")],
            )
        )
    if action["filters_note"]:
        parts.append(action["filters_note"])
    if action["action_params"]:
        parts.append(
            render_params(
                "Action parameters",
                action["action_params"],
                [("name", "Name"), ("type", "Type"), ("description", "Description")],
            )
        )
    if action["expands"]:
        parts.append(
            "**Expandable:** " + ", ".join(f"`{e}`" for e in action["expands"])
        )
    perms = action["permissions"]
    if perms["roles"] or perms["note"]:
        roles = ", ".join(perms["roles"])
        parts.append(f"**Permissions:** {perms['note']} {roles}".rstrip())
    for title, body in action["extra"].items():
        parts.append(f"**{title}**\n\n{body}")
    if action["example_request"]:
        parts.append("Example request:\n\n" + fence(action["example_request"], "shell"))
    if action["example_response"]:
        parts.append(
            "Example response:\n\n"
            + fence(
                action["example_response"], action["example_response_language"] or ""
            )
        )
    return "\n\n".join(parts)


def render_object(obj: dict) -> str:
    parts = [f"## The {obj['name']} object"]
    if obj.get("description"):
        parts.append(obj["description"])
    if obj["fields"]:
        rows = [
            [f"`{f['name']}`", "yes" if f.get("required") else "no", f.get("type", "")]
            for f in obj["fields"]
        ]
        parts.append(table_md(["Field", "Required", "Type"], rows))
    if obj.get("extra_tables"):
        parts.append(obj["extra_tables"])
    if obj["example"]:
        parts.append("Example:\n\n" + fence(obj["example"], "json"))
    return "\n\n".join(parts)


def render_model(model: Model, stamp: str) -> str:
    parts = [
        f"# {model['name']}",
        f"> Populi API2 model. Source: {model['url']}. Docs version: {stamp}. "
        "Generated by `populi-docs`; do not edit.",
    ]
    if model["description"]:
        parts.append(model["description"])
    eps = endpoints_of(model)
    if eps:
        rows = [
            [a["method"], f"`{a['path']}`", a["name"], cell(summary(a["description"]))]
            for a in eps
        ]
        parts.append(
            "## Endpoints\n\n" + table_md(["Method", "Path", "Action", "Summary"], rows)
        )
    parts.extend(render_object(o) for o in model["objects"])
    parts.extend(render_action(a) for a in model["actions"])
    for section in model["guide"]:
        if model["webhook_events"] and any(
            section["title"] == e["title"] for e in model["webhook_events"]
        ):
            continue
        parts.append(f"## {section['title']}\n\n{section['markdown']}".rstrip())
    if model["webhook_events"]:
        parts.append("## Event payloads")
        for e in model["webhook_events"]:
            block = [f"### {e['title']} (`{e['event']}`)"]
            if e.get("description"):
                block.append(e["description"])
            if e.get("example"):
                block.append(fence(e["example"], "json"))
            parts.append("\n\n".join(block))
    return "\n\n".join(parts) + "\n"


def write_reference(
    out: Path, models: list[Model], overview_md: str, stamp: str, catalog: dict
) -> None:
    """Write llms.txt and reference/ under `out`."""
    ref = out / "reference"
    (ref / "models").mkdir(parents=True, exist_ok=True)
    (out / "llms.txt").write_text(render_llms_txt(models, stamp))
    (ref / "overview.md").write_text(render_overview(overview_md, stamp))
    (ref / "endpoints.md").write_text(render_endpoints(models, stamp))
    (ref / "catalog.json").write_text(
        json.dumps(catalog, indent=1, ensure_ascii=False) + "\n"
    )
    for m in models:
        (ref / "models" / f"{m['slug']}.md").write_text(render_model(m, stamp))
