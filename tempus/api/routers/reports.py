from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...services.reports import summary
from ..deps import get_db
from ..schemas import SummaryRead

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/summary", response_model=SummaryRead)
def get_summary(since: Optional[datetime] = None, until: Optional[datetime] = None, db: Session = Depends(get_db)):
    return summary(db, since, until)
