"""Quick and dirty benchmark used while tuning bulk inserts."""

import random
import tempfile
import time
from datetime import datetime, timedelta

from tempus.models import Entry
from tempus.storage import SqliteStorage


def build_entries(count):
    start = datetime(2021, 1, 1, 9, 0)
    for index in range(count):
        offset = timedelta(minutes=random.randint(0, 600))
        yield Entry(
            label="entry %d" % index,
            project=random.choice(["tempus", "docs", None]),
            start=start + timedelta(days=index // 8, minutes=offset),
            end=start + timedelta(days=index // 8, minutes=offset + 30),
        )


def main():
    with tempfile.TemporaryDirectory() as tmp:
        storage = SqliteStorage(tmp + "/bench.db")
        started = time.perf_counter()
        for entry in build_entries(5000):
            storage.add(entry)
        elapsed = time.perf_counter() - started
        print("inserted 5000 entries in %.2fs" % elapsed)
        started = time.perf_counter()
        rows = storage.all()
        print("read %d entries in %.2fs" % (len(rows), time.perf_counter() - started))


if __name__ == "__main__":
    main()
