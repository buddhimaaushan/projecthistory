"""Small parsing and formatting helpers."""

import re
from datetime import date, datetime, timedelta

DURATION_RE = re.compile(r"^(?:(?P<hours>\d+)h)?(?:(?P<minutes>\d+)m)?$")


def parse_duration(value):
    match = DURATION_RE.match(value.strip())
    if not match or not value.strip():
        raise ValueError("expected a duration like 1h30m")
    hours = int(match.group("hours") or 0)
    minutes = int(match.group("minutes") or 0)
    return timedelta(hours=hours, minutes=minutes)


def format_duration(seconds):
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes = remainder // 60
    if hours:
        return "%dh %dm" % (hours, minutes)
    return "%dm" % minutes


def parse_date(value):
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        raise ValueError("expected an ISO date such as 2021-05-04")
