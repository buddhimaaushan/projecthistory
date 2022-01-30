"""Create a little history so the dashboard has something to show."""

import random
from datetime import datetime, timedelta

from tempus.db.base import SessionLocal
from tempus.db.models import Project, Tag, TimeEntry

PROJECTS = ["tempus", "website", "reading"]
LABELS = ["writing docs", "reviewing code", "pairing", "debugging", "planning"]


def main():
    db = SessionLocal()
    projects = {name: Project(name=name) for name in PROJECTS}
    tags = {name: Tag(name=name) for name in ["deep-work", "review", "meeting"]}
    db.add_all(list(projects.values()) + list(tags.values()))
    db.flush()

    start = datetime.utcnow() - timedelta(days=30)
    for index in range(120):
        offset = timedelta(days=index // 4, hours=random.randint(0, 8), minutes=random.randint(0, 59))
        length = timedelta(minutes=random.choice([25, 45, 50, 90]))
        db.add(
            TimeEntry(
                label=random.choice(LABELS),
                project=projects[random.choice(PROJECTS)],
                tags=[random.choice(list(tags.values()))],
                start=start + offset,
                end=start + offset + length,
            )
        )

    db.commit()
    print("seeded 120 entries")


if __name__ == "__main__":
    main()
