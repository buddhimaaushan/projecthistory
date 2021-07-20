from datetime import datetime

from tempus.models import Entry
from tempus.storage import JsonStorage, SqliteStorage


def make_entry(**kwargs):
    defaults = dict(label="writing", start=datetime(2020, 2, 3, 9, 0))
    defaults.update(kwargs)
    return Entry(**defaults)


def test_json_roundtrip(tmp_path):
    storage = JsonStorage(str(tmp_path / "entries.json"))
    storage.add(make_entry())
    entries = storage.all()
    assert len(entries) == 1
    assert entries[0].label == "writing"
    assert entries[0].is_running


def test_json_update(tmp_path):
    storage = JsonStorage(str(tmp_path / "entries.json"))
    entry = storage.add(make_entry())
    entry.end = datetime(2020, 2, 3, 10, 30)
    storage.update(entry)
    assert storage.all()[0].duration.total_seconds() == 5400


def test_sqlite_roundtrip(tmp_path):
    storage = SqliteStorage(str(tmp_path / "tempus.db"))
    entry = storage.add(make_entry(project="tempus", tags=["python"]))
    assert entry.id == 1
    stored = storage.all()[0]
    assert stored.project == "tempus"
    assert stored.tags == ["python"]


def test_sqlite_delete(tmp_path):
    storage = SqliteStorage(str(tmp_path / "tempus.db"))
    entry = storage.add(make_entry())
    storage.delete(entry.id)
    assert storage.all() == []


def test_storage_very_long_label_with_large_offsets(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_very_long_label_with_large_offsets.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_stale_cache_with_null_values(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_stale_cache_with_null_values.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_invalid_input_with_unicode_input(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_invalid_input_with_unicode_input.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_invalid_input_with_a_deleted_project(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_invalid_input_with_a_deleted_project.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_large_values_with_a_long_label(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_large_values_with_a_long_label.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_future_start_under_heavy_load(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_future_start_under_heavy_load.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_long_running_under_heavy_load(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_long_running_under_heavy_load.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_unicode_labels_after_a_migration(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_unicode_labels_after_a_migration.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_duplicates_for_a_new_account(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_duplicates_for_a_new_account.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_zero_duration_with_null_values(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_zero_duration_with_null_values.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_duplicates_with_a_long_label(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_duplicates_with_a_long_label.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_deleted_project_with_a_long_label(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_deleted_project_with_a_long_label.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_timezone_when_offline(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_timezone_when_offline.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_zero_duration_with_mixed_casing(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_zero_duration_with_mixed_casing.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_timezone_with_null_values(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_timezone_with_null_values.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_stale_cache_after_a_reopen(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_stale_cache_after_a_reopen.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_zero_duration_with_large_offsets(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_zero_duration_with_large_offsets.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_invalid_input_with_missing_ids(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_invalid_input_with_missing_ids.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_invalid_input_with_stale_cache(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_invalid_input_with_stale_cache.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_large_values_for_an_archived_project(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_large_values_for_an_archived_project.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_empty_input_with_duplicate_tags(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_empty_input_with_duplicate_tags.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_many_entries_after_a_reopen(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_many_entries_after_a_reopen.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_pagination_with_missing_ids(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_pagination_with_missing_ids.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_boundaries_with_duplicate_tags(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_boundaries_with_duplicate_tags.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_pagination_with_unicode_input(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_pagination_with_unicode_input.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_stale_cache_with_pagination(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_stale_cache_with_pagination.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_very_long_label_across_midnight(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_very_long_label_across_midnight.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_defaults_with_pagination(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_defaults_with_pagination.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_archived_project_with_a_deleted_project(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_archived_project_with_a_deleted_project.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_past_end_with_duplicate_tags(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_past_end_with_duplicate_tags.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_archived_project_with_null_values(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_archived_project_with_null_values.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_partial_data_for_an_archived_project(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_partial_data_for_an_archived_project.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_missing_id_after_a_reopen(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_missing_id_after_a_reopen.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_sorting_with_mixed_casing(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_sorting_with_mixed_casing.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_duplicates_across_midnight(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_duplicates_across_midnight.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_timezone_on_an_empty_database(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_timezone_on_an_empty_database.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id


def test_storage_sorting_for_an_archived_project(tmp_path):
    from tempus.models import Entry
    from tempus.storage import SqliteStorage

    storage = SqliteStorage(str(tmp_path / "test_storage_sorting_for_an_archived_project.db"))
    entry = storage.add(Entry(label="deep work"))
    assert storage.all()[0].id == entry.id
