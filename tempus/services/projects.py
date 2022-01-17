from typing import List, Optional

from sqlalchemy.orm import Session

from ..db.models import Project


def list_projects(db: Session, include_archived: bool = False) -> List[Project]:
    query = db.query(Project).order_by(Project.name)
    if not include_archived:
        query = query.filter(Project.archived.is_(False))
    return query.all()


def create_project(db: Session, data) -> Project:
    project = Project(name=data.name, colour=data.colour, archived=data.archived)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_project(db: Session, project_id: int) -> Optional[Project]:
    return db.query(Project).get(project_id)


def archive_project(db: Session, project: Project) -> Project:
    project.archived = True
    db.commit()
    db.refresh(project)
    return project
