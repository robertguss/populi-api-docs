from pages import INDEX, WEBHOOKS, WIDGETS

from populi_docs import cli, sync

PAGES = {"": INDEX, "models/widgets.html": WIDGETS, "models/webhooks.html": WEBHOOKS}


class FakeFetcher:
    """Serves the synthetic pages; counts requests."""

    requests = 0

    def __init__(self, *args, **kwargs):
        pass

    def get(self, path):
        FakeFetcher.requests += 1
        return PAGES[path]

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return None


def test_sync_then_up_to_date_then_forced_refetch(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(cli, "Fetcher", FakeFetcher)
    monkeypatch.setattr(sync, "MIN_MODELS", 1)
    monkeypatch.setattr(sync, "MIN_ENDPOINTS", 1)

    assert cli.main(["--root", str(tmp_path), "sync"]) == 0
    assert (tmp_path / "reference" / "models" / "widgets.md").exists()
    assert "first snapshot" in capsys.readouterr().out

    FakeFetcher.requests = 0
    assert cli.main(["--root", str(tmp_path), "sync"]) == 0
    assert FakeFetcher.requests == 1
    assert "up to date" in capsys.readouterr().out

    assert cli.main(["--root", str(tmp_path), "sync", "--force"]) == 0
    assert "refetched the same docs version" in capsys.readouterr().out
    assert (tmp_path / "CHANGES.md").read_text().count("## 2026-09-21") == 1
    assert not (tmp_path / sync.SCRATCH).exists()


def test_a_failed_sanity_check_writes_nothing(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(cli, "Fetcher", FakeFetcher)
    assert cli.main(["--root", str(tmp_path), "sync"]) == 2
    assert not (tmp_path / "reference").exists()
    assert not (tmp_path / "llms.txt").exists()
    assert "sanity checks failed" in capsys.readouterr().err


def test_check_reports_a_newer_version(tmp_path, monkeypatch):
    monkeypatch.setattr(cli, "Fetcher", FakeFetcher)
    assert cli.main(["--root", str(tmp_path), "check"]) == 1
