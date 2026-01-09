from datetime import datetime
from typing import Optional

import csv
import io

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from ...services.reports import summary
from ..deps import get_current_user, get_db
from ..schemas import SummaryRead

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/summary", response_model=SummaryRead)
def get_summary(
    since: Optional[datetime] = None,
    until: Optional[datetime] = None,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return summary(db, user.id, since, until)


@router.get("/export.csv", response_class=Response)
def export_entries(db: Session = Depends(get_db), user=Depends(get_current_user)):
    from ...services.entries import list_entries

    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["label", "project", "start", "end", "seconds"])
    for entry in list_entries(db, user.id, limit=10000):
        writer.writerow(
            [
                entry.label,
                entry.project.name if entry.project else "",
                entry.start.isoformat(timespec="seconds"),
                entry.end.isoformat(timespec="seconds") if entry.end else "",
                entry.duration_seconds,
            ]
        )
    return Response(
        content=buffer.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="tempus-export.csv"'},
    )
