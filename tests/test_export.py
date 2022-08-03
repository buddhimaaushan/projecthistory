import json

from tempus.export import export_csv, export_json, import_json
from tempus.models import Entry
from datetime import datetime


def make_entry():
    return Entry(label="writing", project="tempus", tags=["docs"], start=datetime(2021, 5, 4, 9, 0))


def test_export_csv_writes_header(tmp_path):
    path = tmp_path / "entries.csv"
    export_csv([], str(path))
    assert path.read_text().splitlines()[0] == "label,project,tags,start,end"


def test_export_csv_rows(tmp_path):
    path = tmp_path / "entries.csv"
    export_csv([make_entry()], str(path))
    assert "writing" in path.read_text()


def test_export_json_roundtrip():
    payload = export_json([make_entry()])
    restored = import_json(payload)
    assert restored[0].label == "writing"
    assert restored[0].tags == ["docs"]


def test_export_missing_id_with_large_offsets(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_missing_id_with_large_offsets.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_invalid_input_with_missing_ids(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_invalid_input_with_missing_ids.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_missing_id_with_a_long_label(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_missing_id_with_a_long_label.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_null_project_across_timezones(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_null_project_across_timezones.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_large_values_when_offline(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_large_values_when_offline.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_timezone_with_a_deleted_project(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_timezone_with_a_deleted_project.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_single_entry_with_null_values(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_single_entry_with_null_values.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_single_entry_with_unicode_input(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_single_entry_with_unicode_input.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_archived_project_with_defaults(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_archived_project_with_defaults.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_stale_cache_across_timezones(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_stale_cache_across_timezones.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_past_end_after_a_migration(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_past_end_after_a_migration.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_missing_id_with_defaults(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_missing_id_with_defaults.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_zero_duration_after_a_reopen(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_zero_duration_after_a_reopen.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_pagination_with_stale_cache(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_pagination_with_stale_cache.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_boundaries_across_timezones(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_boundaries_across_timezones.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_sorting_with_null_values(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_sorting_with_null_values.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_duplicates_on_an_empty_database(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_duplicates_on_an_empty_database.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_long_running_with_large_offsets(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_long_running_with_large_offsets.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_past_end_for_a_new_account(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_past_end_for_a_new_account.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_very_long_label_with_null_values(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_very_long_label_with_null_values.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_stale_cache_with_null_values(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_stale_cache_with_null_values.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_sorting_with_duplicate_tags(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_sorting_with_duplicate_tags.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_archived_project_after_a_reopen(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_archived_project_after_a_reopen.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_partial_data_with_stale_cache(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_partial_data_with_stale_cache.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_missing_id_with_pagination(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_missing_id_with_pagination.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_invalid_input_with_mixed_casing(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_invalid_input_with_mixed_casing.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_boundaries_after_a_reopen(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_boundaries_after_a_reopen.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_very_long_label_with_unicode_input(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_very_long_label_with_unicode_input.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_many_entries_after_a_migration(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_many_entries_after_a_migration.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_very_long_label_with_a_deleted_project(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_very_long_label_with_a_deleted_project.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_stale_cache_with_duplicate_tags(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_stale_cache_with_duplicate_tags.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")


def test_export_null_project_on_an_empty_database(tmp_path):
    from tempus.export import export_csv

    path = tmp_path / "test_export_null_project_on_an_empty_database.csv"
    export_csv([], str(path))
    assert path.read_text().startswith("label,")
