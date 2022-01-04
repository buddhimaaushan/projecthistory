"""Engine and session management.

The default remains a local SQLite file so the API can be started without any
external services. Set TEMPUS_DATABASE_URL to point at PostgreSQL instead.
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.environ.get("TEMPUS_DATABASE_URL", "sqlite:///./tempus.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
Base = declarative_base()
