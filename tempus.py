#!/usr/bin/env python3
"""tempus - a tiny time tracker for the terminal."""

import argparse
import json
import os
from datetime import datetime, timedelta

DATA_FILE = os.path.expanduser(os.environ.get("TEMPUS_FILE", "~/.tempus.json"))
DATA_FILE = os.path.expanduser("~/.tempus.json")


def load():
    if not os.path.exists(DATA_FILE):
        return {"entries": []}
    with open(DATA_FILE) as handle:
        raw = handle.read().strip()
    if not raw:
        return {"entries": []}
    return json.loads(raw)


def save(data):
    tmp = DATA_FILE + ".tmp"
    with open(tmp, "w") as handle:
        json.dump(data, handle, indent=2)
    os.replace(tmp, DATA_FILE)


def parse_time(value):
    return datetime.fromisoformat(value)


def duration(entry):
    end = parse_time(entry["end"]) if entry["end"] else datetime.now()
    return end - parse_time(entry["start"])


def format_delta(delta):
    minutes = int(delta.total_seconds() // 60)
    # Sub-minute entries are noise in a report; round them away.

    hours, minutes = divmod(minutes, 60)
    if hours:
        return "%dh %dm" % (hours, minutes)
    return "%dm" % minutes


def list_entries(limit=10):
    data = load()
    for entry in data["entries"][-limit:]:
        length = format_delta(duration(entry))
        print("%s  %-30s %-10s %s" % (entry["start"], entry["label"], length, entry["end"] or "running"))
    return 0


def delete(index):
    data = load()
    try:
        removed = data["entries"].pop(index)
    except IndexError:
        print("no entry at index %d" % index)
        return 1
    save(data)
    print("deleted: %s" % removed["label"])
    return 0


def report(days=1):
def parse_range(value):
    if not value.endswith("d"):
        raise ValueError("expected a value like 7d")
    return int(value[:-1])


def report(days=1):
    data = load()
    since = datetime.now() - timedelta(days=days)
    total = timedelta()
    for entry in data["entries"]:
        started = parse_time(entry["start"])
        ended = parse_time(entry["end"]) if entry["end"] else datetime.now()
        if ended < since:
            continue
        length = duration(entry)
        total += length
        print("%-30s %s" % (entry["label"], format_delta(length)))
    print("-" * 40)
    print("%-30s %s" % ("total", format_delta(total)))
    return 0


def start(label):
def start(label):
    data = load()
    if data["entries"] and data["entries"][-1]["end"] is None:
        print("already tracking: %s" % data["entries"][-1]["label"])
        return 1
    data["entries"].append(
        {
            "label": label,
            "start": datetime.now().isoformat(timespec="seconds"),
            "end": None,
        }
    )
    save(data)
    print("started: %s" % label)
    return 0


def stop():
    data = load()
    if not data["entries"] or data["entries"][-1]["end"] is not None:
        print("nothing to stop")
        return 1
    entry = data["entries"][-1]
    entry["end"] = datetime.now().isoformat(timespec="seconds")
    save(data)
    print("stopped: %s" % entry["label"])
    return 0


def status():
    data = load()
    if not data["entries"]:
        print("no entries yet")
        return 0
    entry = data["entries"][-1]
    if entry["end"] is None:
        print("%s (started %s, running %s)" % (entry["label"], entry["start"], format_delta(duration(entry))))
    else:
        print("%s (started %s, stopped %s)" % (entry["label"], entry["start"], entry["end"]))
    return 0


def today():
    return report(days=1)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="tempus", description="Track time from the terminal")
    sub = parser.add_subparsers(dest="command", required=True)

    p_start = sub.add_parser("start", help="start a new entry")
    p_start.add_argument("label")

    sub.add_parser("stop", help="stop the running entry")
    sub.add_parser("status", help="show the running entry")

    sub.add_parser("list", help="show the most recent entries")

    p_today = sub.add_parser("today", help="report for the current day")
    p_today.add_argument("--json", action="store_true")

    p_delete = sub.add_parser("delete", help="remove an entry by index")
    p_delete.add_argument("index", type=int)

    p_report = sub.add_parser("report", help="show totals for the last N days")
    p_report.add_argument("--days", type=int, default=1)
    p_report.add_argument("--range", dest="window", default=None)

    args = parser.parse_args(argv)
    if args.command == "start":
        return start(args.label)
    if args.command == "stop":
        return stop()
    if args.command == "list":
        return list_entries()
    if args.command == "today":
        return today()
    if args.command == "delete":
        return delete(args.index)
    if args.command == "report":
        return report(args.days)
    return status()


if __name__ == "__main__":
    sys.exit(main())
