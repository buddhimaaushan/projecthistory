"""Storage backends for tempus."""

import json
import os
from datetime import datetime

from .models import Entry


def _parse(value):
    if value is None:
        return None
    return datetime.fromisoformat(value)


class JsonStorage:
    def __init__(self, path):
        self.path = path

    def _read(self):
        if not os.path.exists(self.path):
            return []
        with open(self.path) as handle:
            raw = handle.read().strip()
        if not raw:
            return []
        return json.loads(raw).get("entries", [])

    def _write(self, entries):
        tmp = self.path + ".tmp"
        with open(tmp, "w") as handle:
            json.dump({"entries": entries}, handle, indent=2)
        os.replace(tmp, self.path)

    def all(self):
        return [
            Entry(
                start=_parse(row["start"]),
                end=_parse(row.get("end")),
                label=row.get("label", ""),
                project=row.get("project"),
                tags=row.get("tags") or [],
            )
            for row in self._read()
        ]

    def add(self, entry):
        rows = self._read()
        rows.append(
            {
                "label": entry.label,
                "project": entry.project,
                "tags": list(entry.tags),
                "start": entry.start.isoformat(timespec="seconds"),
                "end": entry.end.isoformat(timespec="seconds") if entry.end else None,
            }
        )
        self._write(rows)
        return entry

    def update(self, entry):
        rows = self._read()
        index = entry.id if entry.id is not None else len(rows) - 1
        rows[index] = {
            "label": entry.label,
            "project": entry.project,
            "tags": list(entry.tags),
            "start": entry.start.isoformat(timespec="seconds"),
            "end": entry.end.isoformat(timespec="seconds") if entry.end else None,
        }
        self._write(rows)
        return entry

    def delete(self, entry_id):
        rows = self._read()
        del rows[entry_id]
        self._write(rows)
