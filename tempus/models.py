"""Domain objects shared by the CLI and the storage layer."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Entry:
    start: datetime
    label: str = ""
    end: Optional[datetime] = None
    project: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    id: Optional[int] = None

    @property
    def is_running(self):
        return self.end is None

    @property
    def duration(self):
        if self.end is None:
            return datetime.now() - self.start
        return self.end - self.start

    def overlaps(self, other):
        end = self.end or datetime.now()
        other_end = other.end or datetime.now()
        return self.start < other_end and other.start < end
