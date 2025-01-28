"""Business logic for time entries, kept out of the routers."""

from datetime import datetime
from typing import List, Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, joinedload

from ..db.models import Project, Tag, TimeEntry
from .cache import summary_cache


def get_project(db: Session, name: Optional[str], user_id: int) -> Optional[Project]:
    if not name:
        return None
    project = db.query(Project).filter(Project.name == name, Project.user_id == user_id).one_or_none()
    if project is None:
        project = Project(name=name, user_id=user_id)
        db.add(project)
        try:
            db.flush()
        except IntegrityError:
            db.rollback()
            project = db.query(Project).filter(Project.name == name, Project.user_id == user_id).one()
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
    user_id: int,
    limit: int = 50,
    offset: int = 0,
    project: Optional[str] = None,
    since: Optional[datetime] = None,
    until: Optional[datetime] = None,
) -> List[TimeEntry]:
    query = (
        db.query(TimeEntry)
        .options(joinedload(TimeEntry.project))
        .filter(TimeEntry.user_id == user_id)
        .order_by(TimeEntry.start.desc())
    )
    if project:
        query = query.join(Project).filter(Project.name == project, Project.user_id == user_id)
    if since:
        query = query.filter(TimeEntry.start >= since)
    if until:
        query = query.filter(TimeEntry.start < until)
    return query.offset(offset).limit(limit).all()


def get_entry(db: Session, entry_id: int, user_id: int) -> Optional[TimeEntry]:
    return db.query(TimeEntry).filter(TimeEntry.id == entry_id, TimeEntry.user_id == user_id).one_or_none()


def create_entry(db: Session, data, user_id: int) -> TimeEntry:
    entry = TimeEntry(
        label=data.label,
        start=data.start or datetime.utcnow(),
        end=data.end,
        user_id=user_id,
        project=get_project(db, data.project, user_id),
        tags=sync_tags(db, data.tags),
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    summary_cache.invalidate()
    return entry


def stop_entry(db: Session, entry: TimeEntry) -> TimeEntry:
    if entry.end is None:
        entry.end = datetime.utcnow()
        db.commit()
        db.refresh(entry)
        summary_cache.invalidate()
    return entry


def update_entry(db: Session, entry: TimeEntry, data, user_id: int) -> TimeEntry:
    if data.label is not None:
        entry.label = data.label
    if data.project is not None:
        entry.project = get_project(db, data.project, user_id)
    if data.tags is not None:
        entry.tags = sync_tags(db, data.tags)
    db.commit()
    db.refresh(entry)
    summary_cache.invalidate()
    return entry


def delete_entry(db: Session, entry: TimeEntry) -> None:
    db.delete(entry)
    db.commit()
    summary_cache.invalidate()


def running_entry(db: Session, user_id: int) -> Optional[TimeEntry]:
    return (
        db.query(TimeEntry)
        .filter(TimeEntry.end.is_(None), TimeEntry.user_id == user_id)
        .order_by(TimeEntry.start.desc())
        .first()
    )
