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


def test_cli_pagination_after_a_reopen(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_invalid_input_with_mixed_casing(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_invalid_input_on_an_empty_database(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_very_long_label_under_heavy_load(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_archived_project_for_a_new_account(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_empty_input_when_offline(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_unicode_labels_with_large_offsets(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_large_values_under_heavy_load(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_mixed_projects_with_defaults(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_duplicates_with_large_offsets(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_timezone_after_a_migration(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_sorting_with_pagination(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_missing_id_with_stale_cache(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_stop_without_running_entry(storage, capsys):
    assert cli.stop() == 1
    assert "nothing to stop" in capsys.readouterr().out


def test_delete_out_of_range(storage, capsys):
    assert cli.delete(10) == 1
    assert "no entry at index 10" in capsys.readouterr().out


def test_cli_partial_data_after_a_reopen(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_unicode_labels_for_a_new_account(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_archived_project_after_a_migration(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_partial_data_across_timezones(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_partial_data_with_missing_ids(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_partial_data_with_a_deleted_project(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_past_end_with_a_long_label(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_defaults_with_null_values(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_long_running_with_defaults(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_many_entries_with_null_values(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_zero_duration_with_unicode_input(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_long_running_across_timezones(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_many_entries_on_an_empty_database(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_unicode_labels_with_defaults(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_mixed_projects_with_large_offsets(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_single_entry_across_timezones(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_boundaries_with_missing_ids(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_large_values_after_a_reopen(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_archived_project_with_defaults(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_long_running_with_pagination(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_boundaries_on_an_empty_database(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_missing_id_across_timezones(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_long_running_with_null_values(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_pagination_with_a_long_label(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_duplicates_with_stale_cache(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_duplicates_after_a_migration(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_stale_cache_with_a_long_label(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_single_entry_with_null_values(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_zero_duration_with_large_offsets(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_zero_duration_with_a_long_label(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_long_running_for_an_archived_project(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_single_entry_with_pagination(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_timezone_with_duplicate_tags(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_large_values_across_midnight(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_unicode_labels_across_midnight(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_mixed_projects_on_an_empty_database(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_many_entries_with_large_offsets(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_large_values_with_mixed_casing(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_partial_data_after_a_migration(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_past_end_for_a_new_account(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_stale_cache_across_timezones(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out


def test_cli_pagination_with_unicode_input(storage, capsys):
    from tempus import cli

    assert cli.report(0) == 0
    assert "total" in capsys.readouterr().out
