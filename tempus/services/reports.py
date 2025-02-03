from collections import defaultdict
from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session, joinedload

from ..db.models import Project, TimeEntry
from .cache import summary_cache


def summary(db: Session, user_id: int, since: Optional[datetime] = None, until: Optional[datetime] = None):
    key = (user_id, since.isoformat() if since else None, until.isoformat() if until else None)
    cached = summary_cache.get(key)
    if cached is not None:
        return cached
    query = db.query(TimeEntry).options(joinedload(TimeEntry.project)).filter(TimeEntry.user_id == user_id)
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
    result = {
        "entries": len(entries),
        "total_seconds": total,
        "by_project": dict(sorted(by_project.items())),
        "by_day": dict(sorted(by_day.items())),
    }
    summary_cache.set(key, result)
    return result
