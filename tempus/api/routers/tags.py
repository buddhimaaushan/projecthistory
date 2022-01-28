from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...db.models import Tag
from ..deps import get_db

router = APIRouter(prefix="/tags", tags=["tags"])


@router.get("", response_model=List[str])
def list_tags(db: Session = Depends(get_db)):
    return [tag.name for tag in db.query(Tag).order_by(Tag.name).all()]
