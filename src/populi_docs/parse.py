"""Populi's reference pages to structured data.

Every model page has one `h1` (the model), then `h2` sections: "The X object"
(a JSON example and an Attribute/Required/Data Type table), and one section
per action (index, show, create, ...). An action section holds its code
examples and description, then `h3` subsections: HTTP Request, Parameters,
Filter Condition Parameters, Action Parameters, Expandable Properties,
Permissions. A page with neither objects nor actions (Webhooks) is a guide
page, kept as prose, with its event table pulled out.

Anything the parser does not recognise is kept as Markdown under `extra` and
reported as a warning, never dropped.
"""

from __future__ import annotations

import re
from typing import Any

from bs4 import BeautifulSoup, Tag

from .html2md import (
    SKIPPED_LANGUAGES,
    LinkMap,
    blocks,
    code_language,
    code_text,
    is_code,
    list_items,
    table_rows,
    text,
)

BASE_URL = "https://populi.co/api/"
OBJECT_TITLE = re.compile(r"^The (.+) object$")
REQUEST_LINE = re.compile(r"^(GET|POST|PUT|PATCH|DELETE)\s+(/\S*)$")
STAMP = re.compile(
    r"documentation updated on (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(?: [A-Z]{2,5})?)"
)
KNOWN_SUBSECTIONS = {
    "HTTP Request",
    "Parameters",
    "Filter Condition Parameters",
    "Action Parameters",
    "Expandable Properties",
    "Permissions",
}

Model = dict[str, Any]


class ParseError(Exception):
    pass


def content(html: str) -> Tag:
    node = BeautifulSoup(html, "html.parser").select_one(".content")
    if node is None:
        raise ParseError("no .content element; the page layout has changed")
    return node


def elements(node: Tag) -> list[Tag]:
    return [child for child in node.children if isinstance(child, Tag)]


def split_sections(
    node: Tag, level: str = "h2"
) -> tuple[list[Tag], list[tuple[Tag, list[Tag]]]]:
    """Elements before the first heading, and (heading, elements) per heading."""
    preamble: list[Tag] = []
    sections: list[tuple[Tag, list[Tag]]] = []
    for el in elements(node) if isinstance(node, Tag) else node:
        if el.name == level:
            sections.append((el, []))
        elif sections:
            sections[-1][1].append(el)
        else:
            preamble.append(el)
    return preamble, sections


def docs_stamp(html: str) -> str:
    match = STAMP.search(BeautifulSoup(html, "html.parser").get_text(" "))
    if not match:
        raise ParseError("no 'documentation updated on' stamp on the index page")
    return match.group(1)


def model_pages(index_html: str) -> list[tuple[str, str]]:
    """(model name, page path) for every model the index links to, in order."""
    soup = BeautifulSoup(index_html, "html.parser")
    seen: dict[str, str] = {}
    for a in soup.select("a.toc-h1"):
        href = (a.get("href") or "").split("#")[0]
        if href.startswith("models/") and href.endswith(".html") and href not in seen:
            seen[href] = a.get("data-title") or text(a)
    if not seen:
        raise ParseError("the index links to no model pages; the layout has changed")
    return [(name, href) for href, name in seen.items()]


def slug_of(page: str) -> str:
    return page.rsplit("/", 1)[-1].removesuffix(".html")


# Links inside a model page point at sibling pages (`people.html#index`) or the
# index (`../index.html#filter-conditions`); both become links into this copy.
def model_link(href: str) -> str:
    if not href or href.startswith(("http:", "https:", "mailto:")):
        return href
    if href.startswith("#"):
        return href
    page, _, _ = href.partition("#")
    if page.endswith("index.html"):
        return "../overview.md"
    if page.endswith(".html"):
        return slug_of(page) + ".md"
    return BASE_URL + "models/" + href


def overview_link(href: str) -> str:
    if not href or href.startswith(("http:", "https:", "mailto:", "#")):
        return href
    page, _, _ = href.partition("#")
    if page.startswith("models/") and page.endswith(".html"):
        return "models/" + slug_of(page) + ".md"
    if page == "index.html":
        return "#"
    return BASE_URL + href


def parse_overview(index_html: str) -> str:
    """The index page (authentication, paging, filters, errors, rate limits)."""
    return blocks(elements(content(index_html)), overview_link, heading_offset=1)


def parse_table(table: Tag, link: LinkMap) -> list[dict[str, Any]]:
    headers, rows = table_rows(table, link)
    keys = []
    for h in headers:
        h = h.lower()
        if h in ("name", "attribute", "event"):
            keys.append("name")
        elif h in ("data type", "type"):
            keys.append("type")
        else:
            keys.append(h)
    out = []
    for row in rows:
        item = {key: value for key, value in zip(keys, row, strict=False)}
        if "required" in item:
            item["required"] = item["required"].strip().lower() in ("yes", "true")
        item["name"] = item.get("name", "").strip("`")
        out.append(item)
    return out


def parse_object(
    heading: Tag, els: list[Tag], link: LinkMap, warnings: list[str]
) -> dict:
    name = OBJECT_TITLE.match(text(heading)).group(1)
    obj: dict[str, Any] = {
        "name": name,
        "anchor": heading.get("id", ""),
        "fields": [],
        "example": None,
    }
    prose = []
    tables = [el for el in els if el.name == "table"]
    for el in els:
        if is_code(el) and obj["example"] is None:
            obj["example"] = code_text(el)
        elif el.name == "p":
            prose.append(el)
    if tables:
        obj["fields"] = parse_table(tables[0], link)
    if len(tables) > 1:
        obj["extra_tables"] = blocks(tables[1:], link)
        warnings.append(
            f"object {name}: {len(tables) - 1} extra table(s) kept as Markdown"
        )
    obj["description"] = blocks(prose, link)
    return obj


def parse_action(
    heading: Tag, els: list[Tag], link: LinkMap, where: str, warnings: list[str]
) -> dict:
    action: dict[str, Any] = {
        "name": text(heading),
        "anchor": heading.get("id", ""),
        "method": None,
        "path": None,
        "description": "",
        "params": [],
        "params_note": "",
        "filters": [],
        "filters_note": "",
        "action_params": [],
        "expands": [],
        "permissions": {"note": "", "roles": []},
        "example_request": None,
        "example_response": None,
        "example_response_language": None,
        "extra": {},
    }
    before, subsections = split_sections(els, level="h3")

    response_captioned = False
    description = []
    for el in before:
        if el.name == "blockquote":
            response_captioned = response_captioned or "response" in text(el).lower()
        elif is_code(el):
            language = code_language(el)
            if language == "shell" and action["example_request"] is None:
                action["example_request"] = code_text(el)
            elif language in SKIPPED_LANGUAGES or language == "shell":
                continue
            elif response_captioned and action["example_response"] is None:
                action["example_response"] = code_text(el)
                action["example_response_language"] = language or None
        else:
            description.append(el)
    action["description"] = blocks(description, link)

    for sub_heading, sub in subsections:
        title = text(sub_heading)
        tables = [el for el in sub if el.name == "table"]
        prose = [el for el in sub if el.name != "table"]
        note = blocks(prose, link)
        if title == "HTTP Request":
            for el in sub:
                match = REQUEST_LINE.match(text(el).replace("`", ""))
                if match:
                    action["method"], action["path"] = match.groups()
                    break
            else:
                warnings.append(
                    f"{where} {action['name']}: no request line in {note!r}"
                )
        elif title == "Parameters":
            action["params"] = parse_table(tables[0], link) if tables else []
            action["params_note"] = "" if note == "None" else note
        elif title == "Filter Condition Parameters":
            action["filters"] = parse_table(tables[0], link) if tables else []
            action["filters_note"] = note
        elif title == "Action Parameters":
            action["action_params"] = parse_table(tables[0], link) if tables else []
        elif title == "Expandable Properties":
            lists = [el for el in sub if el.name in ("ul", "ol")]
            action["expands"] = [
                item.strip("`") for lst in lists for item in list_items(lst, link)
            ]
        elif title == "Permissions":
            lists = [el for el in sub if el.name in ("ul", "ol")]
            action["permissions"] = {
                "note": blocks([el for el in sub if el.name == "p"], link),
                "roles": [item for lst in lists for item in list_items(lst, link)],
            }
        else:
            action["extra"][title] = blocks(sub, link)
            warnings.append(f"{where} {action['name']}: unknown subsection {title!r}")
    return action


def parse_model_page(html: str, name: str, page: str) -> tuple[Model, list[str]]:
    """One model page to a model dict, plus any warnings."""
    node = content(html)
    slug = slug_of(page)
    warnings: list[str] = []
    h1 = node.find("h1")
    if h1 is None:
        raise ParseError(f"{slug}: no h1")
    preamble, sections = split_sections(node)
    model: Model = {
        "name": text(h1) or name,
        "slug": slug,
        "url": BASE_URL + page,
        "description": blocks([el for el in preamble if el.name != "h1"], model_link),
        "objects": [],
        "actions": [],
        "guide": [],
        "webhook_events": [],
    }
    for heading, els in sections:
        title = text(heading)
        if OBJECT_TITLE.match(title):
            model["objects"].append(parse_object(heading, els, model_link, warnings))
        elif any(el.name == "h3" and text(el) == "HTTP Request" for el in els):
            model["actions"].append(
                parse_action(heading, els, model_link, model["name"], warnings)
            )
        else:
            model["guide"].append(
                {"title": title, "anchor": heading.get("id", ""), "elements": els}
            )
    if model["guide"] and not (model["objects"] or model["actions"]):
        model["webhook_events"] = webhook_events(model["guide"], warnings)
    elif model["guide"]:
        titles = ", ".join(repr(g["title"]) for g in model["guide"])
        warnings.append(f"{model['name']}: sections kept as prose: {titles}")
    for section in model["guide"]:
        section["markdown"] = blocks(section.pop("elements"), model_link)
    return model, warnings


def webhook_events(guide: list[dict], warnings: list[str]) -> list[dict]:
    """The event table (Event, Name), joined to each event's own section."""
    events: list[dict] = []
    for section in guide:
        for table in (el for el in section["elements"] if el.name == "table"):
            headers = [text(th).lower() for th in table.find_all("th")]
            if headers[:2] == ["event", "name"]:
                _, rows = table_rows(table)
                for row in rows:
                    if len(row) >= 2:
                        events.append({"event": row[0].strip("`"), "title": row[1]})
    by_title = {e["title"]: e for e in events}
    for section in guide:
        event = by_title.get(section["title"])
        if event is None:
            continue
        prose = [el for el in section["elements"] if not is_code(el)]
        code = [el for el in section["elements"] if is_code(el)]
        event["description"] = blocks(prose, model_link)
        event["example"] = code_text(code[0]) if code else None
        event["anchor"] = section["anchor"]
    missing = [e["event"] for e in events if "description" not in e]
    if missing:
        warnings.append(f"webhook events with no section: {', '.join(missing)}")
    return events


def endpoint_count(models: list[Model]) -> int:
    return sum(1 for m in models for a in m["actions"] if a["method"])


def catalog(
    models: list[Model], stamp: str, fetched_at: str, warnings: list[str]
) -> dict:
    """The machine-readable reference: everything except examples and prose."""
    out_models = []
    for m in models:
        out_models.append(
            {
                "name": m["name"],
                "slug": m["slug"],
                "url": m["url"],
                "objects": [
                    {"name": o["name"], "fields": o["fields"]} for o in m["objects"]
                ],
                "actions": [
                    {
                        key: a[key]
                        for key in (
                            "name",
                            "method",
                            "path",
                            "description",
                            "params",
                            "filters",
                            "action_params",
                            "expands",
                            "permissions",
                        )
                    }
                    for a in m["actions"]
                ],
            }
        )
    events = [
        {
            "event": e["event"],
            "title": e["title"],
            "description": e.get("description", ""),
        }
        for m in models
        for e in m["webhook_events"]
    ]
    return {
        "source": BASE_URL,
        "docs_updated_on": stamp,
        "fetched_at": fetched_at,
        "counts": {
            "models": len(models),
            "endpoints": endpoint_count(models),
            "webhook_events": len(events),
        },
        "models": out_models,
        "webhook_events": events,
        "warnings": warnings,
    }
