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
