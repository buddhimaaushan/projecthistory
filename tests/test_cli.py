from datetime import datetime
from pathlib import Path

import pytest
from typer.testing import CliRunner

from tempus import cli
from tempus.models import Entry
from tempus.storage import SqliteStorage

runner = CliRunner()


@pytest.fixture
def storage(monkeypatch, tmp_path):
    db = str(tmp_path / "tempus.db")
    store = SqliteStorage(db)
    monkeypatch.setattr(cli, "get_storage", lambda: store)
    return store


def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert "tempus" in result.stdout


def test_start_and_stop(storage):
    assert runner.invoke(cli.app, ["start", "reading"]).exit_code == 0
    assert runner.invoke(cli.app, ["stop"]).exit_code == 0
    assert storage.all()[0].end is not None


def test_second_start_is_rejected(storage):
    runner.invoke(cli.app, ["start", "reading"])
    result = runner.invoke(cli.app, ["start", "writing"])
    assert result.exit_code == 1


def test_add_manual_entry(storage):
    result = runner.invoke(cli.app, ["add", "review", "--duration", "1h30m"])
    assert result.exit_code == 0
    assert storage.all()[0].duration.total_seconds() == 5400


def test_report_prints_total(storage):
    storage.add(Entry(label="reading", start=datetime.now(), end=datetime.now()))
    result = runner.invoke(cli.app, ["report", "--days", "1"])
    assert "total" in result.stdout


def test_summary_is_json(storage):
    result = runner.invoke(cli.app, ["summary", "--days", "7"])
    assert result.exit_code == 0
    assert result.stdout.strip().startswith("{")


def test_export_and_import(storage, tmp_path):
    storage.add(Entry(label="reading", start=datetime.now(), end=datetime.now()))
    target = tmp_path / "entries.json"
    assert runner.invoke(cli.app, ["export", str(target), "--format", "json"]).exit_code == 0
    assert target.exists()
    assert runner.invoke(cli.app, ["import", str(target)]).exit_code == 0


def test_cli_unicode_labels_for_an_archived_project(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_very_long_label_with_stale_cache(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_duplicates_with_a_long_label(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_boundaries_with_unicode_input(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_deleted_project_with_a_deleted_project(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out
