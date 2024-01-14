"""Request and response models."""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, validator


class UserCreate(BaseModel):
    email: str = Field(..., regex="^[^@]+@[^@]+\\.[^@]+$")
    password: str = Field(..., min_length=8, max_length=128)
    display_name: str = Field("", max_length=120)


class UserRead(BaseModel):
    id: int
    email: str
    display_name: str
    is_active: bool

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    colour: str = Field("#4f46e5", regex="^#[0-9a-fA-F]{6}$")
    archived: bool = False


class ProjectRead(ProjectCreate):
    id: int

    class Config:
        orm_mode = True


class EntryBase(BaseModel):
    label: str = Field(..., min_length=1, max_length=200)
    project: Optional[str] = Field(None, max_length=120)
    tags: List[str] = Field(default_factory=list)
    start: Optional[datetime] = None
    end: Optional[datetime] = None

    @validator("tags")
    def normalise_tags(cls, value):
        return sorted({tag.strip().lower() for tag in value if tag.strip()})

    @validator("end")
    def end_after_start(cls, value, values):
        start = values.get("start")
        if value and start and value < start:
            raise ValueError("end must be after start")
        return value


class EntryCreate(EntryBase):
    pass


class EntryUpdate(BaseModel):
    label: Optional[str] = Field(None, min_length=1, max_length=200)
    project: Optional[str] = None
    tags: Optional[List[str]] = None


class EntryRead(EntryBase):
    id: int
    duration_seconds: int
    is_running: bool

    class Config:
        orm_mode = True
        json_encoders = {datetime: lambda value: value.replace(microsecond=0).isoformat() + "Z"}


class SummaryRead(BaseModel):
    entries: int
    total_seconds: int
    by_project: dict
    by_day: dict


class HealthRead(BaseModel):
    status: str
    version: str
