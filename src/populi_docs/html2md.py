"""HTML to Markdown, for the Slate pages Populi publishes.

Only what those pages use: headings, paragraphs, lists, tables, code blocks,
blockquote captions, asides, and inline code, links, and emphasis. Every code
sample on the site comes in six tabs; the Ruby, Python, C#, and PHP tabs are
dropped, the shell (curl) and JSON ones kept.
"""

from __future__ import annotations

import re
from collections.abc import Callable, Iterable

from bs4 import Comment, NavigableString, Tag

SKIPPED_LANGUAGES = frozenset({"ruby", "python", "csharp", "php"})

LinkMap = Callable[[str], str]


def keep_link(href: str) -> str:
    return href


def text(node: Tag) -> str:
    """The node's visible text, whitespace collapsed."""
    return re.sub(r"\s+", " ", node.get_text(" ")).strip()


def inline(node: Tag, link: LinkMap = keep_link) -> str:
    return inline_nodes(node.children, link)


def inline_nodes(nodes: Iterable, link: LinkMap = keep_link) -> str:
    parts: list[str] = []
    for child in nodes:
        if isinstance(child, Comment):
            continue
        if isinstance(child, NavigableString):
            parts.append(str(child))
            continue
        if not isinstance(child, Tag):
            continue
        name = child.name
        if name == "code":
            parts.append(f"`{child.get_text().strip()}`")
        elif name in ("strong", "b"):
            inner = inline(child, link)
            parts.append(f"**{inner}**" if inner else "")
        elif name in ("em", "i"):
            inner = inline(child, link)
            parts.append(f"*{inner}*" if inner else "")
        elif name == "a":
            inner = inline(child, link)
            href = link(child.get("href", ""))
            parts.append(f"[{inner}]({href})" if href and inner else inner)
        elif name == "br":
            parts.append(" ")
        else:
            parts.append(inline(child, link))
    return re.sub(r"\s+", " ", "".join(parts)).strip()


def cell(value: str) -> str:
    return value.replace("|", "\\|")


def table_rows(
    table: Tag, link: LinkMap = keep_link
) -> tuple[list[str], list[list[str]]]:
    headers = [text(th) for th in table.find_all("th")]
    rows = []
    for tr in table.find_all("tr"):
        cells = tr.find_all("td")
        if cells:
            rows.append([inline(td, link) for td in cells])
    return headers, rows


def table_md(headers: list[str], rows: list[list[str]]) -> str:
    width = max([len(headers), *(len(r) for r in rows)] or [0])
    if not width:
        return ""
    headers = headers + [""] * (width - len(headers))
    lines = [
        "| " + " | ".join(cell(h) for h in headers) + " |",
        "|" + "---|" * width,
    ]
    for row in rows:
        row = row + [""] * (width - len(row))
        lines.append("| " + " | ".join(cell(c) for c in row) + " |")
    return "\n".join(lines)


def list_md(node: Tag, link: LinkMap = keep_link, depth: int = 0) -> str:
    lines = []
    ordered = node.name == "ol"
    for i, li in enumerate(node.find_all("li", recursive=False), 1):
        nested = [
            c for c in li.children if isinstance(c, Tag) and c.name in ("ul", "ol")
        ]
        own = [c for c in li.children if c not in nested]
        marker = f"{i}." if ordered else "-"
        lines.append("  " * depth + f"{marker} {inline_nodes(own, link)}")
        for sub in nested:
            lines.append(list_md(sub, link, depth + 1))
    return "\n".join(lines)


def list_items(node: Tag, link: LinkMap = keep_link) -> list[str]:
    return [inline(li, link) for li in node.find_all("li")]


def code_language(node: Tag) -> str:
    pre = node if node.name == "pre" else node.find("pre")
    if pre is None:
        return ""
    for cls in pre.get("class") or []:
        if cls != "highlight" and not cls.startswith("tab-"):
            return cls
    return ""


def code_text(node: Tag) -> str:
    pre = node if node.name == "pre" else node.find("pre")
    return (pre or node).get_text().strip("\n")


def is_code(node: Tag) -> bool:
    return node.name == "pre" or (node.name == "div" and node.find("pre") is not None)


def fence(body: str, language: str = "") -> str:
    longest = max((len(m) for m in re.findall(r"`+", body)), default=0)
    ticks = "`" * max(3, longest + 1)
    return f"{ticks}{language}\n{body}\n{ticks}"


def blocks(nodes: Iterable, link: LinkMap = keep_link, heading_offset: int = 0) -> str:
    """Block-level HTML to Markdown, one block per element, blank-line separated."""
    out: list[str] = []
    for node in nodes:
        if not isinstance(node, Tag):
            continue
        name = node.name
        if re.fullmatch(r"h[1-6]", name):
            level = min(6, int(name[1]) + heading_offset)
            out.append("#" * level + " " + inline(node, link))
        elif name == "p":
            out.append(inline(node, link))
        elif name in ("ul", "ol"):
            out.append(list_md(node, link))
        elif name == "table":
            out.append(table_md(*table_rows(node, link)))
        elif name == "blockquote":
            out.append("> " + inline(node, link))
        elif name == "aside":
            out.append("> **Note:** " + inline(node, link))
        elif is_code(node):
            language = code_language(node)
            if language not in SKIPPED_LANGUAGES:
                out.append(fence(code_text(node), language))
        else:
            out.append(inline(node, link))
    return "\n\n".join(block for block in out if block.strip() and block != "> ")
