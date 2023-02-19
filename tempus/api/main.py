"""HTTP API for tempus."""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .. import __version__
from .middleware import RequestContextMiddleware
from .routers import entries, projects, reports, tags
from .schemas import HealthRead

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


app.include_router(entries.router, prefix="/api")
app.include_router(projects.router, prefix="/api")
app.include_router(tags.router, prefix="/api")
app.include_router(reports.router, prefix="/api")


@app.get("/health", response_model=HealthRead, tags=["meta"])
def health():
    return {"status": "ok", "version": __version__}


@app.exception_handler(Exception)
async def unhandled_exception(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "internal server error", "path": request.url.path},
    )
