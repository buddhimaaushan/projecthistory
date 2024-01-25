from typing import List, Optional

from sqlalchemy.orm import Session

from ..db.models import Project


def list_projects(db: Session, user_id: int, include_archived: bool = False) -> List[Project]:
    query = db.query(Project).filter(Project.user_id == user_id).order_by(Project.name)
    if not include_archived:
        query = query.filter(Project.archived.is_(False))
    return query.all()


def create_project(db: Session, data, user_id: int) -> Project:
    project = Project(name=data.name, colour=data.colour, archived=data.archived, user_id=user_id)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_project(db: Session, project_id: int, user_id: int) -> Optional[Project]:
    return db.query(Project).filter(Project.id == project_id, Project.user_id == user_id).one_or_none()


def archive_project(db: Session, project: Project) -> Project:
    project.archived = True
    db.commit()
    db.refresh(project)
    return project
