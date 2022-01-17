from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ...services import projects as service
from ..deps import get_db
from ..schemas import ProjectCreate, ProjectRead

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("", response_model=List[ProjectRead])
def list_projects(include_archived: bool = False, db: Session = Depends(get_db)):
    return service.list_projects(db, include_archived)


@router.post("", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db)):
    return service.create_project(db, payload)


@router.post("/{project_id}/archive", response_model=ProjectRead)
def archive_project(project_id: int, db: Session = Depends(get_db)):
    project = service.get_project(db, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="project not found")
    return service.archive_project(db, project)
