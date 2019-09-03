#!/usr/bin/env python3
"""tempus - a tiny time tracker for the terminal."""

import argparse
import json
import os
from datetime import datetime

DATA_FILE = os.path.expanduser(os.environ.get("TEMPUS_FILE", "~/.tempus.json"))
DATA_FILE = os.path.expanduser("~/.tempus.json")


def load():
    if not os.path.exists(DATA_FILE):
        return {"entries": []}
    with open(DATA_FILE) as handle:
        return json.load(handle)


def save(data):
    with open(DATA_FILE, "w") as handle:
        json.dump(data, handle, indent=2)


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
    print("%s (started %s)" % (entry["label"], entry["start"]))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(prog="tempus", description="Track time from the terminal")
    sub = parser.add_subparsers(dest="command", required=True)

    p_start = sub.add_parser("start", help="start a new entry")
    p_start.add_argument("label")

    sub.add_parser("stop", help="stop the running entry")
    sub.add_parser("status", help="show the running entry")

    args = parser.parse_args(argv)
    if args.command == "start":
        return start(args.label)
    if args.command == "stop":
        return stop()
    return status()


if __name__ == "__main__":
    sys.exit(main())
