import json

from pages import INDEX, WEBHOOKS, WIDGETS

from populi_docs import sync
from populi_docs.render import render_endpoints, render_llms_txt


def write_raw(raw, index=INDEX, widgets=WIDGETS):
    (raw / "models").mkdir(parents=True)
    (raw / "index.html").write_text(index)
    (raw / "models" / "widgets.html").write_text(widgets)
    (raw / "models" / "webhooks.html").write_text(WEBHOOKS)
    (raw / "meta.json").write_text(
        json.dumps({"fetched_at": "2026-09-22T00:00:00+00:00"})
    )


def test_build_install_and_first_changes_entry(tmp_path):
    write_raw(tmp_path / "staged")
    build = sync.build_from_raw(tmp_path / "staged")
    assert build.catalog["counts"] == {"models": 2, "endpoints": 2, "webhook_events": 2}

    sync.install(tmp_path, build, tmp_path / "staged")
    assert (tmp_path / "raw" / "models" / "widgets.html").exists()
    assert not (tmp_path / "staged").exists()
    assert (
        "[Widget](reference/models/widgets.md): 2 endpoints"
        in (tmp_path / "llms.txt").read_text()
    )
    page = (tmp_path / "reference" / "models" / "widgets.md").read_text()
    assert "## index: `GET /widgets`" in page
    assert "HTTParty" not in page and "requests.get" not in page
    assert json.loads((tmp_path / "reference" / "catalog.json").read_text())["counts"]

    line = sync.record_changes(tmp_path, build, None)
    assert line.startswith("first snapshot: 2 models, 2 endpoints")
    changes_md = (tmp_path / "CHANGES.md").read_text()
    assert "## 2026-09-21 11:05:10 PST" in changes_md


def test_later_entries_go_on_top(tmp_path):
    write_raw(tmp_path / "raw")
    build = sync.build_from_raw(tmp_path / "raw")
    sync.record_changes(tmp_path, build, None)
    build.stamp = "2026-10-01 09:00:00 PST"
    sync.record_changes(
        tmp_path, build, {"Endpoints": ["+ `GET /ltitools` (LtiTool index)"]}
    )
    text = (tmp_path / "CHANGES.md").read_text()
    assert text.index("2026-10-01") < text.index("2026-09-21")
    assert text.count("<!-- entries -->") == 1


def test_sanity_refuses_a_shrunken_or_empty_build(tmp_path):
    write_raw(
        tmp_path / "raw",
        widgets="<html><div class='content'><h1>Widget</h1></div></html>",
    )
    build = sync.build_from_raw(tmp_path / "raw")
    problems = sync.sanity({"counts": {"models": 2, "endpoints": 600}}, build)
    assert any("models (expected at least" in p for p in problems)
    assert any("endpoints fell from 600 to 0" in p for p in problems)
    assert any("parsed to nothing: Widget" in p for p in problems)


def test_a_whole_build_passes_sanity_at_real_scale(tmp_path, monkeypatch):
    write_raw(tmp_path / "raw")
    build = sync.build_from_raw(tmp_path / "raw")
    monkeypatch.setattr(sync, "MIN_MODELS", 2)
    monkeypatch.setattr(sync, "MIN_ENDPOINTS", 2)
    assert sync.sanity(build.catalog, build) == []


def test_endpoints_sort_by_bare_path(tmp_path):
    write_raw(tmp_path / "raw")
    build = sync.build_from_raw(tmp_path / "raw")
    rows = [
        line
        for line in render_endpoints(build.models, "x").splitlines()
        if "| GET |" in line
    ]
    assert "`/widgets`" in rows[0] and "`/widgets/(widget)`" in rows[1]


def test_one_endpoint_is_singular(tmp_path):
    write_raw(tmp_path / "raw")
    build = sync.build_from_raw(tmp_path / "raw")
    widgets = build.models[0]
    widgets["actions"] = widgets["actions"][:1]
    assert "[Widget](reference/models/widgets.md): 1 endpoint:" in render_llms_txt(
        build.models, "x"
    )


def test_llms_txt_is_the_same_on_every_run(tmp_path):
    """Equal-length paths are ordered by name, not by set iteration order."""
    import subprocess
    import sys

    write_raw(tmp_path / "raw")
    script = (
        "import sys; from populi_docs import sync, render;"
        "b = sync.build_from_raw(__import__('pathlib').Path(sys.argv[1]));"
        "b.models[0]['actions'] += [dict(b.models[0]['actions'][0], path=p)"
        " for p in ('/zz', '/aa', '/mm')];"
        "print(render.render_llms_txt(b.models, 'x'))"
    )
    outputs = {
        subprocess.run(
            [sys.executable, "-c", script, str(tmp_path / "raw")],
            env={"PYTHONHASHSEED": seed},
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        for seed in ("1", "2", "3", "4")
    }
    assert len(outputs) == 1
    assert "`/aa`, `/mm`, `/zz`" in outputs.pop()
