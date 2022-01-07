"""ORM models for the HTTP API."""

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .base import Base

entry_tags = Table(
    "entry_tags",
    Base.metadata,
    Column("entry_id", ForeignKey("entries.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
)


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False, unique=True)
    colour = Column(String(7), nullable=False, default="#4f46e5")
    archived = Column(Boolean, nullable=False, default=False)

    entries = relationship("TimeEntry", back_populates="project")

    def __repr__(self):
        return "<Project %s>" % self.name


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False, unique=True)

    entries = relationship("TimeEntry", secondary=entry_tags, back_populates="tags")


class TimeEntry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    label = Column(String(200), nullable=False)
    start = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
    end = Column(DateTime, nullable=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=True, index=True)

    project = relationship("Project", back_populates="entries")
    tags = relationship("Tag", secondary=entry_tags, back_populates="entries")

    @property
    def is_running(self):
        return self.end is None

    @property
    def duration_seconds(self):
        end = self.end or datetime.utcnow()
        return max(0, int((end - self.start).total_seconds()))
