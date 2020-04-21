from datetime import datetime

import pytest

from tempus import cli
from tempus.models import Entry
from tempus.storage import SqliteStorage


@pytest.fixture
def storage(monkeypatch, tmp_path):
    db = str(tmp_path / "tempus.db")
    monkeypatch.setattr(cli, "get_storage", lambda: SqliteStorage(db))
    return db


def test_start_creates_entry(storage, capsys):
    assert cli.start("reading") == 0
    assert "started: reading" in capsys.readouterr().out


def test_start_refuses_second_running_entry(storage):
    cli.start("reading")
    assert cli.start("writing") == 1


def test_stop_marks_entry_finished(storage):
    cli.start("reading")
    assert cli.stop() == 0
    entries = cli.get_storage().all()
    assert entries[0].end is not None


def test_report_totals(storage, capsys):
    store = cli.get_storage()
    store.add(Entry(label="reading", start=datetime.now(), end=datetime.now()))
    assert cli.report(1) == 0
    assert "total" in capsys.readouterr().out


def test_start_records_tags(storage):
    cli.start("reading", tags="books, evening")
    entry = cli.get_storage().all()[0]
    assert entry.tags == ["books", "evening"]


def test_cli_duplicates_for_an_archived_project(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_invalid_input_with_unicode_input(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_partial_data_after_a_reopen(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_missing_id_for_a_new_account(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_sorting_with_pagination(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out
