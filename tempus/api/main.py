"""HTTP API for tempus."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .. import __version__
from .schemas import HealthRead

app = FastAPI(
    title="tempus",
    version=__version__,
    description="A small self-hosted time tracker.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", response_model=HealthRead, tags=["meta"])
def health():
    return {"status": "ok", "version": __version__}
