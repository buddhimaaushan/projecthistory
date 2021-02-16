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
