"""What changed between two catalogs, structurally.

Compared: models, endpoints (method + path), object fields, parameters,
filter conditions, action parameters, expands, permissions, endpoint
descriptions, webhook events. Not compared: examples, which carry random ids
and timestamps that change on every build of Populi's site.
"""

from __future__ import annotations

from collections import defaultdict

CATEGORIES = [
    "Models",
    "Endpoints",
    "Object fields",
    "Parameters",
    "Filter conditions",
    "Action parameters",
    "Expands",
    "Permissions",
    "Descriptions",
    "Webhook events",
]

Changes = dict[str, list[str]]


def _endpoints(catalog: dict) -> dict[tuple[str, str], tuple[str, dict]]:
    out = {}
    for m in catalog["models"]:
        for a in m["actions"]:
            if a.get("method") and a.get("path"):
                out[(a["method"], a["path"])] = (m["name"], a)
    return out


def _fields(catalog: dict) -> dict[tuple[str, str], dict]:
    return {
        (o["name"], f["name"]): f
        for m in catalog["models"]
        for o in m["objects"]
        for f in o["fields"]
    }


def _named(items: list[dict]) -> dict[str, dict]:
    return {item["name"]: item for item in items}


def _describe(item: dict) -> str:
    bits = []
    if "type" in item and item["type"]:
        bits.append(item["type"])
    if item.get("required"):
        bits.append("required")
    return f" ({', '.join(bits)})" if bits else ""


def _compare_named(
    changes: Changes,
    category: str,
    where: str,
    old: list[dict],
    new: list[dict],
    noun: str,
) -> None:
    old_by, new_by = _named(old), _named(new)
    for name in sorted(new_by.keys() - old_by.keys()):
        changes[category].append(f"+ {where}: {noun} `{name}`{_describe(new_by[name])}")
    for name in sorted(old_by.keys() - new_by.keys()):
        changes[category].append(f"− {where}: {noun} `{name}`")
    for name in sorted(old_by.keys() & new_by.keys()):
        before, after = old_by[name], new_by[name]
        for key in ("type", "required"):
            if before.get(key) != after.get(key):
                changes[category].append(
                    f"~ {where}: {noun} `{name}` {key} "
                    f"{before.get(key)!r} → {after.get(key)!r}"
                )


def diff_catalogs(old: dict, new: dict) -> Changes:
    changes: Changes = defaultdict(list)

    old_models = {m["slug"]: m["name"] for m in old["models"]}
    new_models = {m["slug"]: m["name"] for m in new["models"]}
    for slug in sorted(new_models.keys() - old_models.keys()):
        changes["Models"].append(f"+ {new_models[slug]} (`{slug}`)")
    for slug in sorted(old_models.keys() - new_models.keys()):
        changes["Models"].append(f"− {old_models[slug]} (`{slug}`)")

    old_eps, new_eps = _endpoints(old), _endpoints(new)
    for key in sorted(new_eps.keys() - old_eps.keys()):
        model, action = new_eps[key]
        changes["Endpoints"].append(f"+ `{key[0]} {key[1]}` ({model} {action['name']})")
    for key in sorted(old_eps.keys() - new_eps.keys()):
        model, action = old_eps[key]
        changes["Endpoints"].append(f"− `{key[0]} {key[1]}` ({model} {action['name']})")
    for key in sorted(old_eps.keys() & new_eps.keys()):
        (_, before), (_, after) = old_eps[key], new_eps[key]
        where = f"`{key[0]} {key[1]}`"
        _compare_named(
            changes, "Parameters", where, before["params"], after["params"], "parameter"
        )
        _compare_named(
            changes,
            "Filter conditions",
            where,
            before["filters"],
            after["filters"],
            "filter",
        )
        _compare_named(
            changes,
            "Action parameters",
            where,
            before["action_params"],
            after["action_params"],
            "action parameter",
        )
        added = sorted(set(after["expands"]) - set(before["expands"]))
        removed = sorted(set(before["expands"]) - set(after["expands"]))
        if added:
            changes["Expands"].append(
                f"+ {where}: " + ", ".join(f"`{e}`" for e in added)
            )
        if removed:
            changes["Expands"].append(
                f"− {where}: " + ", ".join(f"`{e}`" for e in removed)
            )
        if sorted(before["permissions"]["roles"]) != sorted(
            after["permissions"]["roles"]
        ):
            changes["Permissions"].append(
                f"~ {where}: {', '.join(before['permissions']['roles']) or 'none'} → "
                f"{', '.join(after['permissions']['roles']) or 'none'}"
            )
        if before["description"] != after["description"]:
            changes["Descriptions"].append(f"~ {where}")

    old_fields, new_fields = _fields(old), _fields(new)
    for key in sorted(new_fields.keys() - old_fields.keys()):
        changes["Object fields"].append(
            f"+ {key[0]}.`{key[1]}`{_describe(new_fields[key])}"
        )
    for key in sorted(old_fields.keys() - new_fields.keys()):
        changes["Object fields"].append(f"− {key[0]}.`{key[1]}`")
    for key in sorted(old_fields.keys() & new_fields.keys()):
        for attr in ("type", "required"):
            before, after = old_fields[key].get(attr), new_fields[key].get(attr)
            if before != after:
                changes["Object fields"].append(
                    f"~ {key[0]}.`{key[1]}` {attr} {before!r} → {after!r}"
                )

    old_events = {e["event"] for e in old.get("webhook_events", [])}
    new_events = {e["event"]: e for e in new.get("webhook_events", [])}
    for event in sorted(new_events.keys() - old_events):
        changes["Webhook events"].append(f"+ `{event}` ({new_events[event]['title']})")
    for event in sorted(old_events - new_events.keys()):
        changes["Webhook events"].append(f"− `{event}`")

    return {c: changes[c] for c in CATEGORIES if changes.get(c)}


def headline(changes: Changes) -> str:
    """One line: counts per category, for a commit subject or a notification."""
    if not changes:
        return "no structural changes"
    parts = []
    for category, lines in changes.items():
        plus = sum(1 for line in lines if line.startswith("+"))
        minus = sum(1 for line in lines if line.startswith("−"))
        tilde = sum(1 for line in lines if line.startswith("~"))
        counts = " ".join(
            f"{sign}{n}" for sign, n in (("+", plus), ("−", minus), ("~", tilde)) if n
        )
        parts.append(f"{category.lower()} {counts}")
    return "; ".join(parts)


def format_changes(changes: Changes) -> str:
    if not changes:
        return "No structural changes (wording or examples only)."
    sections = []
    for category, lines in changes.items():
        sections.append(
            f"### {category}\n\n" + "\n".join(f"- {line}" for line in lines)
        )
    return "\n\n".join(sections)
