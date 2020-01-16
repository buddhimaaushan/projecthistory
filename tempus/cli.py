"""Command line interface for tempus."""

import argparse
import os
import sys
from datetime import datetime, timedelta

from . import __version__
from .models import Entry
from .storage import JsonStorage

DEFAULT_PATH = os.environ.get("TEMPUS_FILE", os.path.expanduser("~/.tempus.json"))


def get_storage():
    return JsonStorage(DEFAULT_PATH)


def format_delta(delta):
    minutes = int(delta.total_seconds() // 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return "%dh %dm" % (hours, minutes)
    return "%dm" % minutes


def start(label):
    storage = get_storage()
    entries = storage.all()
    if entries and entries[-1].is_running:
        print("already tracking: %s" % entries[-1].label)
        return 1
    storage.add(Entry(label=label, start=datetime.now()))
    print("started: %s" % label)
    return 0


def stop():
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


def status():
    entries = get_storage().all()
    if not entries:
        print("no entries yet - try: tempus start \"something\"")
        return 0
    entry = entries[-1]
    if entry.is_running:
        print("%s (running %s)" % (entry.label, format_delta(entry.duration)))
    else:
        print("%s (last entry)" % entry.label)
    return 0


def list_entries(limit=10):
    entries = get_storage().all()
    for entry in entries[-limit:]:
        print("%s  %-30s %-10s %s" % (
            entry.start.strftime("%Y-%m-%d %H:%M"),
            entry.label,
            format_delta(entry.duration),
            "running" if entry.is_running else "",
        ))
    return 0


def delete(index):
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


def report(days=1):
    entries = get_storage().all()
    now = datetime.now()
    since = now - timedelta(days=days)
    total = timedelta()
    for entry in entries:
        if entry.end is not None and entry.end < since:
            continue
        if entry.start > now:
            continue
        total += entry.duration
        print("%-30s %s" % (entry.label, format_delta(entry.duration)))
    print("-" * 40)
    print("%-30s %s" % ("total", format_delta(total)))
    return 0


def today():
    return report(days=1)


def week():
    entries = get_storage().all()
    totals = {}
    for entry in entries:
        key = entry.start.strftime("%Y-%m-%d")
        totals[key] = totals.get(key, timedelta()) + entry.duration
    for key in sorted(totals):
        print("%s  %s" % (key, format_delta(totals[key])))
    return 0


def build_parser():
    parser = argparse.ArgumentParser(prog="tempus", description="Track time from the terminal")
    parser.add_argument("--version", action="version", version="tempus " + __version__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_start = sub.add_parser("start", help="start a new entry")
    p_start.add_argument("label")

    sub.add_parser("stop", help="stop the running entry")
    sub.add_parser("status", help="show the running entry")
    sub.add_parser("list", help="show the most recent entries")
    sub.add_parser("today", help="report for the current day")

    p_delete = sub.add_parser("delete", help="remove an entry by index")
    p_delete.add_argument("index", type=int)

    p_report = sub.add_parser("report", help="show totals for the last N days")
    p_report.add_argument("--days", type=int, default=1)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    handlers = {
        "start": lambda: start(args.label),
        "stop": stop,
        "status": status,
        "list": list_entries,
        "delete": lambda: delete(args.index),
        "report": lambda: report(args.days),
        "today": today,
    }
    return handlers[args.command]()


if __name__ == "__main__":
    sys.exit(main())
