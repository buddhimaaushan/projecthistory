from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from ...services import entries as service
from ..deps import get_current_user, get_db
from ..schemas import EntryCreate, EntryRead, EntryUpdate

router = APIRouter(prefix="/entries", tags=["entries"])


@router.get("", response_model=List[EntryRead])
def list_entries(
    limit: int = Query(50, ge=0, le=200),
    offset: int = Query(0, ge=0),
    project: Optional[str] = None,
    since: Optional[datetime] = None,
    until: Optional[datetime] = None,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return service.list_entries(
        db, user.id, limit=limit, offset=offset, project=project, since=since, until=until
    )


@router.post("", response_model=EntryRead, status_code=status.HTTP_201_CREATED)
def create_entry(payload: EntryCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return service.create_entry(db, payload, user.id)


@router.post("/start", response_model=EntryRead, status_code=status.HTTP_201_CREATED)
def start_timer(payload: EntryCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    current = service.running_entry(db, user.id)
    if current is not None:
        raise HTTPException(status_code=409, detail="a timer is already running")
    if payload.end is not None:
        raise HTTPException(status_code=422, detail="cannot start a finished entry")
    return service.create_entry(db, payload, user.id)


@router.post("/{entry_id}/stop", response_model=EntryRead)
def stop_timer(entry_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    entry = service.get_entry(db, entry_id, user.id)
    if entry is None:
        raise HTTPException(status_code=404, detail="entry not found")
    return service.stop_entry(db, entry)


@router.get("/{entry_id}", response_model=EntryRead)
def get_entry(entry_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    entry = service.get_entry(db, entry_id, user.id)
    if entry is None:
        raise HTTPException(status_code=404, detail="entry not found")
    return entry


@router.patch("/{entry_id}", response_model=EntryRead)
def update_entry(
    entry_id: int,
    payload: EntryUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    entry = service.get_entry(db, entry_id, user.id)
    if entry is None:
        raise HTTPException(status_code=404, detail="entry not found")
    return service.update_entry(db, entry, payload, user.id)


@router.delete("/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_entry(entry_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    entry = service.get_entry(db, entry_id, user.id)
    if entry is None:
        raise HTTPException(status_code=404, detail="entry not found")
    service.delete_entry(db, entry)
