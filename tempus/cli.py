"""Command line interface for tempus."""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from typing import List, Optional

from . import __version__
from .config import Config
from .models import Entry
from .reports import filter_entries, group_by_day, group_by_project, summarise
from .storage import JsonStorage, SqliteStorage
from .utils import format_duration, parse_date, parse_duration

DEFAULT_PATH = os.environ.get("TEMPUS_FILE", os.path.expanduser("~/.tempus.json"))


def get_storage():
    config = Config.load()
    if os.path.exists(config.database):
        return SqliteStorage(config.database)
    return JsonStorage(DEFAULT_PATH)


def format_delta(delta):
    return format_duration(delta.total_seconds())


def start(label: str, tags: str = "", project: Optional[str] = None) -> int:
    storage = get_storage()
    entries = storage.all()
    if entries and entries[-1].is_running:
        print("already tracking: %s" % entries[-1].label)
        return 1
    storage.add(
        Entry(
            label=label,
            project=project or Config.load().default_project or None,
            tags=[tag.strip() for tag in tags.split(",") if tag.strip()],
            start=datetime.now(),
        )
    )
    print("started: %s" % label)
    return 0


def stop() -> int:
    storage = get_storage()
    entries = storage.all()
    if not entries or not entries[-1].is_running:
        print("nothing to stop")
        return 1
    entry = entries[-1]
    entry.end = datetime.now()
    storage.update(entry)
    print("stopped: %s (%s)" % (entry.label, format_delta(entry.duration)))
    return 0


def status() -> int:
    entries = get_storage().all()
    if not entries:
        print('no entries yet - try: tempus start "something"')
        return 0
    entry = entries[-1]
    if entry.is_running:
        print("%s (running %s)" % (entry.label, format_delta(entry.duration)))
    else:
        print("%s (last entry, %s)" % (entry.label, entry.start.strftime("%Y-%m-%d %H:%M")))
    return 0


def list_entries(limit: int = 10) -> int:
    entries = get_storage().all()
    for entry in entries[-limit:]:
        print(
            "%s  %-30s %-10s %s"
            % (
                entry.start.strftime("%Y-%m-%d %H:%M"),
                entry.label,
                format_delta(entry.duration),
                "running" if entry.is_running else "",
            )
        )
    return 0


def delete(index: int) -> int:
    storage = get_storage()
    entries = storage.all()
    try:
        removed = entries[index]
    except IndexError:
        print("no entry at index %d" % index)
        return 1
    storage.delete(removed.id if removed.id is not None else index)
    print("deleted: %s" % removed.label)
    return 0


def edit(index: int, label: Optional[str] = None, project: Optional[str] = None) -> int:
    storage = get_storage()
    entries = storage.all()
    try:
        entry = entries[index]
    except IndexError:
        print("no entry at index %d" % index)
        return 1
    if label:
        entry.label = label
    if project is not None:
        entry.project = project
    storage.update(entry)
    print("updated entry %d" % index)
    return 0


def add_manual(label: str, duration: str, start: Optional[str] = None, project: Optional[str] = None) -> int:
    storage = get_storage()
    length = parse_duration(duration)
    started = datetime.fromisoformat(start) if start else datetime.now() - length
    storage.add(Entry(label=label, project=project, start=started, end=started + length))
    print("added: %s (%s)" % (label, duration))
    return 0


def report(days: int = 1, by_project: bool = False, as_json: bool = False) -> int:
    entries = filter_entries(get_storage().all(), start=datetime.now() - timedelta(days=days))
    if as_json:
        print(json.dumps(summarise(entries), default=str, indent=2))
        return 0
    if by_project:
        for name, seconds in group_by_project(entries).items():
            print("%-30s %s" % (name, format_duration(seconds)))
    else:
        for entry in entries:
            print("%-30s %s" % (entry.label, format_delta(entry.duration)))
    summary = summarise(entries)
    print("-" * 40)
    print("%-30s %s" % ("total", format_duration(summary["total_seconds"])))
    return 0


def today() -> int:
    return report(days=1)


def week() -> int:
    for day, entries in group_by_day(get_storage().all()).items():
        print("%s  %s" % (day, format_duration(summarise(entries)["total_seconds"])))
    return 0


def show_config() -> int:
    config = Config.load()
    print("database = %s" % config.database)
    print("default_project = %s" % config.default_project)
    print("week_starts_on = %s" % config.week_starts_on)
    print("weekly_target = %s" % config.weekly_target)
    return 0


def migrate() -> int:
    source = JsonStorage(DEFAULT_PATH)
    target = SqliteStorage(Config.load().database)
    count = 0
    for entry in source.all():
        target.add(entry)
        count += 1
    print("migrated %d entries to %s" % (count, target.connection))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tempus", description="Track time from the terminal")
    parser.add_argument("--version", action="version", version="tempus " + __version__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_start = sub.add_parser("start", help="start a new entry")
    p_start.add_argument("label")
    p_start.add_argument("--tags", default="")
    p_start.add_argument("--project", default=None)

    sub.add_parser("stop", help="stop the running entry")
    sub.add_parser("status", help="show the running entry")
    sub.add_parser("list", help="show the most recent entries")
    sub.add_parser("today", help="report for the current day")
    sub.add_parser("week", help="totals for every recorded day")
    sub.add_parser("config", help="print the resolved configuration")
    sub.add_parser("migrate", help="move entries from JSON to SQLite")

    p_add = sub.add_parser("add", help="record an entry after the fact")
    p_add.add_argument("label")
    p_add.add_argument("--duration", required=True)
    p_add.add_argument("--at", default=None)
    p_add.add_argument("--project", default=None)

    p_delete = sub.add_parser("delete", help="remove an entry by index")
    p_delete.add_argument("index", type=int)

    p_edit = sub.add_parser("edit", help="change an existing entry")
    p_edit.add_argument("index", type=int)
    p_edit.add_argument("--label")
    p_edit.add_argument("--project")

    p_report = sub.add_parser("report", help="show totals for the last N days")
    p_report.add_argument("--days", type=int, default=1)
    p_report.add_argument("--by-project", action="store_true")
    p_report.add_argument("--json", action="store_true")

    return parser


HANDLERS = {
    "start": lambda args: start(args.label, args.tags, args.project),
    "stop": lambda args: stop(),
    "status": lambda args: status(),
    "list": lambda args: list_entries(),
    "delete": lambda args: delete(args.index),
    "edit": lambda args: edit(args.index, args.label, args.project),
    "add": lambda args: add_manual(args.label, args.duration, args.at, args.project),
    "report": lambda args: report(args.days, args.by_project, args.json),
    "today": lambda args: today(),
    "week": lambda args: week(),
    "config": lambda args: show_config(),
    "migrate": lambda args: migrate(),
}


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return HANDLERS[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
