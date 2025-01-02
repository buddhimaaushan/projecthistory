"""HTTP API for tempus."""

from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .. import __version__
from ..logging import configure_logging
from .middleware import RequestContextMiddleware
from .routers import auth, entries, projects, reports, tags
from sqlalchemy import text
from sqlalchemy.orm import Session

from .deps import get_db
from .schemas import HealthRead

configure_logging()

app = FastAPI(
    title="tempus",
    version=__version__,
    description="A small self-hosted time tracker.",
)

app.add_middleware(RequestContextMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, prefix="/api")
app.include_router(entries.router, prefix="/api")
app.include_router(projects.router, prefix="/api")
app.include_router(tags.router, prefix="/api")
app.include_router(reports.router, prefix="/api")


@app.get("/health", response_model=HealthRead, tags=["meta"])
def health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "ok", "version": __version__}


@app.exception_handler(Exception)
async def unhandled_exception(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "internal server error", "path": request.url.path},
    )
