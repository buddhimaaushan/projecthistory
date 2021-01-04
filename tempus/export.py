"""Import and export helpers for recorded entries."""

import csv
import json
from datetime import datetime
from typing import Dict, Iterable, List

from .models import Entry

FIELDS = ["label", "project", "tags", "start", "end"]


def as_row(entry: Entry) -> Dict[str, str]:
    return {
        "label": entry.label,
        "project": entry.project or "",
        "tags": ",".join(entry.tags),
        "start": entry.start.isoformat(timespec="seconds"),
        "end": entry.end.isoformat(timespec="seconds") if entry.end else "",
    }


def export_csv(entries: Iterable[Entry], path: str) -> str:
    with open(path, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for entry in entries:
            writer.writerow(as_row(entry))
    return path


def export_json(entries: Iterable[Entry]) -> str:
    return json.dumps([as_row(entry) for entry in entries], indent=2)


def entry_from_row(row: Dict[str, str]) -> Entry:
    return Entry(
        label=row.get("label", ""),
        project=row.get("project") or None,
        tags=[tag for tag in (row.get("tags") or "").split(",") if tag],
        start=datetime.fromisoformat(row["start"]),
        end=datetime.fromisoformat(row["end"]) if row.get("end") else None,
    )


def import_json(payload: str) -> List[Entry]:
    return [entry_from_row(row) for row in json.loads(payload)]
