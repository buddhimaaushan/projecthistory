"""Aggregation helpers shared by the CLI, exporters and the API."""

from collections import defaultdict
from datetime import date, datetime, timedelta
from typing import Dict, Iterable, List, Optional

from .models import Entry


def filter_entries(entries, start=None, end=None, project=None, tags=None):
    """Return entries inside the given range, project and tag filters."""
    result = []
    for entry in entries:
        if start is not None and entry.start < start:
            continue
        if end is not None and entry.start >= end:
            continue
        if project is not None and entry.project != project:
            continue
        if tags and not set(tags).issubset(set(entry.tags)):
            continue
        result.append(entry)
    return result


def summarise(entries: Iterable[Entry]) -> Dict[str, object]:
    entries = list(entries)
    total = sum((entry.duration for entry in entries), timedelta())
    return {
        "entries": len(entries),
        "total_seconds": int(total.total_seconds()),
        "first": min((entry.start for entry in entries), default=None),
        "last": max((entry.start for entry in entries), default=None),
    }


def group_by_day(entries: Iterable[Entry]):
    groups = defaultdict(list)
    for entry in entries:
        groups[entry.start.date()].append(entry)
    return dict(sorted(groups.items()))


def group_by_project(entries: Iterable[Entry]):
    totals = defaultdict(timedelta)
    for entry in entries:
        totals[entry.project or "unassigned"] += entry.duration
    return {name: int(value.total_seconds()) for name, value in sorted(totals.items())}


def week_bounds(day: date, starts_on: str = "monday"):
    if starts_on == "sunday":
        offset = (day.weekday() + 1) % 7
    else:
        offset = day.weekday()
    start = day - timedelta(days=offset)
    return start, start + timedelta(days=6)
