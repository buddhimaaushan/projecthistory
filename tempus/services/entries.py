"""Business logic for time entries, kept out of the routers."""

from datetime import datetime
from typing import List, Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..db.models import Project, Tag, TimeEntry


def get_project(db: Session, name: Optional[str]) -> Optional[Project]:
    if not name:
        return None
    project = db.query(Project).filter(Project.name == name).one_or_none()
    if project is None:
        project = Project(name=name)
        db.add(project)
        try:
            db.flush()
        except IntegrityError:
            db.rollback()
            project = db.query(Project).filter(Project.name == name).one()
    return project


def sync_tags(db: Session, names: List[str]) -> List[Tag]:
    tags = []
    for name in names:
        tag = db.query(Tag).filter(Tag.name == name).one_or_none()
        if tag is None:
            tag = Tag(name=name)
            db.add(tag)
            db.flush()
        tags.append(tag)
    return tags


def list_entries(
    db: Session,
    limit: int = 50,
    offset: int = 0,
    project: Optional[str] = None,
    since: Optional[datetime] = None,
    until: Optional[datetime] = None,
) -> List[TimeEntry]:
    query = db.query(TimeEntry).order_by(TimeEntry.start.desc())
    if project:
        query = query.join(Project).filter(Project.name == project)
    if since:
        query = query.filter(TimeEntry.start >= since)
    if until:
        query = query.filter(TimeEntry.start < until)
    return query.offset(offset).limit(limit).all()


def get_entry(db: Session, entry_id: int) -> Optional[TimeEntry]:
    return db.query(TimeEntry).get(entry_id)


def create_entry(db: Session, data) -> TimeEntry:
    entry = TimeEntry(
        label=data.label,
        start=data.start or datetime.utcnow(),
        end=data.end,
        project=get_project(db, data.project),
        tags=sync_tags(db, data.tags),
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def stop_entry(db: Session, entry: TimeEntry) -> TimeEntry:
    if entry.end is None:
        entry.end = datetime.utcnow()
        db.commit()
        db.refresh(entry)
    return entry


def update_entry(db: Session, entry: TimeEntry, data) -> TimeEntry:
    if data.label is not None:
        entry.label = data.label
    if data.project is not None:
        entry.project = get_project(db, data.project)
    if data.tags is not None:
        entry.tags = sync_tags(db, data.tags)
    db.commit()
    db.refresh(entry)
    return entry


def delete_entry(db: Session, entry: TimeEntry) -> None:
    db.delete(entry)
    db.commit()


def running_entry(db: Session) -> Optional[TimeEntry]:
    return db.query(TimeEntry).filter(TimeEntry.end.is_(None)).order_by(TimeEntry.start.desc()).first()
