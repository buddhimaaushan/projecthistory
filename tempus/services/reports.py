from collections import defaultdict
from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from ..db.models import Project, TimeEntry


def summary(db: Session, since: Optional[datetime] = None, until: Optional[datetime] = None):
    query = db.query(TimeEntry)
    if since:
        query = query.filter(TimeEntry.start >= since)
    if until:
        query = query.filter(TimeEntry.start < until)
    entries = query.all()
    by_project = defaultdict(int)
    by_day = defaultdict(int)
    total = 0
    for entry in entries:
        total += entry.duration_seconds
        by_project[entry.project.name if entry.project else "unassigned"] += entry.duration_seconds
        by_day[entry.start.date().isoformat()] += entry.duration_seconds
    return {
        "entries": len(entries),
        "total_seconds": total,
        "by_project": dict(sorted(by_project.items())),
        "by_day": dict(sorted(by_day.items())),
    }
