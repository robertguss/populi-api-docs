from pathlib import Path

import pytest
from pages import INDEX, WEBHOOKS, WIDGETS

from populi_docs.parse import (
    ParseError,
    docs_stamp,
    model_pages,
    parse_model_page,
    parse_overview,
)

FIXTURES = Path(__file__).parent / "fixtures"


def test_stamp_and_model_list_come_from_the_index():
    assert docs_stamp(INDEX) == "2026-09-21 11:05:10 PST"
    assert model_pages(INDEX) == [
        ("Widget", "models/widgets.html"),
        ("Webhooks", "models/webhooks.html"),
    ]


def test_a_missing_stamp_is_an_error_not_a_blank():
    with pytest.raises(ParseError):
        docs_stamp("<html><div class='content'><h1>Intro</h1></div></html>")


def test_a_page_without_content_is_an_error():
    with pytest.raises(ParseError):
        parse_model_page("<html><body><p>moved</p></body></html>", "X", "models/x.html")


def test_overview_links_point_into_this_copy():
    overview = parse_overview(INDEX)
    assert "## Introduction" in overview
    assert "[widgets](models/widgets.md)" in overview
    assert "```plaintext\nGET /people\n```" in overview


def test_object_fields_and_example():
    model, warnings = parse_model_page(WIDGETS, "Widget", "models/widgets.html")
    [obj] = model["objects"]
    assert obj["name"] == "Widget"
    assert obj["fields"] == [
        {"name": "id", "required": True, "type": "int"},
        {"name": "name", "required": False, "type": "text (50)"},
    ]
    assert obj["example"] == '{"object": "widget", "id": 1}'
    assert model["description"] == "A widget belongs to a [person](people.md)."


def test_action_sections():
    model, warnings = parse_model_page(WIDGETS, "Widget", "models/widgets.html")
    index, show = model["actions"]
    assert (index["method"], index["path"]) == ("GET", "/widgets")
    assert index["description"] == (
        "Retrieves all Widget objects. Uses the `filter` | parameter."
    )
    assert [p["name"] for p in index["params"]] == ["filter", "page"]
    assert index["params"][0] == {
        "name": "filter",
        "required": False,
        "type": "mixed",
        "description": "See available filter conditions",
    }
    assert index["filters"] == [{"name": "added_at", "type": "datetime"}]
    assert index["expands"] == ["owner", "tags"]
    assert index["permissions"]["roles"] == ["Registrar", "Academic Admin"]
    assert index["example_request"].startswith("curl ")
    assert index["example_response"] == '{"object": "list"}'
    assert (show["method"], show["path"]) == ("GET", "/widgets/(widget)")
    assert show["params"] == [] and show["params_note"] == ""


def test_unknown_subsections_are_kept_and_reported():
    model, warnings = parse_model_page(WIDGETS, "Widget", "models/widgets.html")
    show = model["actions"][1]
    assert show["extra"] == {"Rate Notes": "Slow."}
    assert warnings == ["Widget show: unknown subsection 'Rate Notes'"]


def test_webhook_events_join_the_table_to_their_sections():
    model, warnings = parse_model_page(WEBHOOKS, "Webhooks", "models/webhooks.html")
    assert warnings == []
    assert model["objects"] == [] and model["actions"] == []
    events = {e["event"]: e for e in model["webhook_events"]}
    assert events["term_updated"]["title"] == "Academic Term Updated"
    assert (
        events["term_updated"]["description"] == "Whenever an academic term is updated."
    )
    assert events["person_created"]["example"] == '{"event": "person_created"}'


def test_a_real_page():
    html = (FIXTURES / "academicyears.html").read_text()
    model, warnings = parse_model_page(
        html, "AcademicYear", "models/academicyears.html"
    )
    assert warnings == []
    assert [(a["name"], a["method"], a["path"]) for a in model["actions"]] == [
        ("index", "GET", "/academicyears"),
        ("show", "GET", "/academicyears/(academicyear)"),
        ("current", "GET", "/academicyears/current"),
    ]
    fields = [f["name"] for f in model["objects"][0]["fields"]]
    assert fields[:3] == ["id", "start_year", "end_year"]
    show = model["actions"][1]
    assert show["expands"] == ["academic_terms", "academic_super_terms"]
    assert show["permissions"]["roles"] == ["Academic Admin", "Registrar"]
