"""Configuration loading.

Precedence: command line flag > environment variable > config file > default.
"""

import configparser
import os
from dataclasses import dataclass

DEFAULT_CONFIG = os.path.expanduser("~/.config/tempus/config.ini")


@dataclass
class Config:
    database: str
    default_project: str = ""
    week_starts_on: str = "monday"
    weekly_target: int = 0

    @classmethod
    def load(cls, path=None):
        path = path or os.environ.get("TEMPUS_CONFIG", DEFAULT_CONFIG)
        parser = configparser.ConfigParser()
        parser.read(path)
        database = parser.get(
            "storage",
            "database",
            fallback=os.environ.get("TEMPUS_DB", os.path.expanduser("~/.tempus.db")),
        )
        return cls(
            database=database,
            default_project=parser.get("general", "default_project", fallback=""),
            week_starts_on=parser.get("general", "week_starts_on", fallback="monday"),
            weekly_target=parser.getint("general", "weekly_target", fallback=0),
        )
