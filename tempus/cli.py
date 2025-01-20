"""Command line interface for tempus."""

import json
import os
from datetime import datetime, timedelta
from typing import List, Optional

import typer
from rich.console import Console
from rich.table import Table

from . import __version__
from .config import Config
from .export import export_csv, export_json, import_json
from .models import Entry
from .reports import filter_entries, group_by_day, group_by_project, summarise, week_bounds
from .storage import JsonStorage, SqliteStorage, add_many
from .utils import format_duration, parse_date, parse_duration

app = typer.Typer(help="Track time from the terminal.", no_args_is_help=True)
console = Console()

DEFAULT_PATH = os.environ.get("TEMPUS_FILE", os.path.expanduser("~/.tempus.json"))


def get_storage():
    config = Config.load()
    if os.path.exists(config.database):
        return SqliteStorage(config.database)
    return JsonStorage(DEFAULT_PATH)


def format_delta(delta):
    return format_duration(delta.total_seconds())


def _version_callback(value: bool) -> None:
    if value:
        typer.echo("tempus " + __version__)
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, "--version", callback=_version_callback, is_eager=True, help="Show the version and exit."
    ),
) -> None:
    """Small self-hosted time tracker."""


@app.command("start")
def start(
    label: str = typer.Argument(..., help="What are you working on?"),
    project: Optional[str] = typer.Option(None, "--project", "-p"),
    tags: str = typer.Option("", "--tags", "-t", help="Comma separated tags."),
) -> None:
    """Start a timer."""
    storage = get_storage()
    entries = storage.all()
    if entries and entries[-1].is_running:
        console.print("already tracking: %s" % entries[-1].label, style="yellow")
        raise typer.Exit(code=1)
    storage.add(
        Entry(
            label=label,
            project=project or Config.load().default_project or None,
            tags=[tag.strip() for tag in tags.split(",") if tag.strip()],
            start=datetime.now(),
        )
    )
    console.print("started: %s" % label, style="green")


@app.command("stop")
def stop() -> None:
    """Stop the running timer."""
    storage = get_storage()
    entries = storage.all()
    if not entries or not entries[-1].is_running:
        console.print("nothing to stop", style="yellow")
        raise typer.Exit(code=1)
    entry = entries[-1]
    entry.end = datetime.now()
    storage.update(entry)
    console.print("stopped: %s (%s)" % (entry.label, format_delta(entry.duration)), style="green")


@app.command("status")
def status() -> None:
    """Show the running entry."""
    entries = get_storage().all()
    if not entries:
        console.print('no entries yet - try: tempus start "something"', style="yellow")
        return
    entry = entries[-1]
    if entry.is_running:
        console.print("%s (running %s)" % (entry.label, format_delta(entry.duration)))
    else:
        console.print("%s (last entry, %s)" % (entry.label, entry.start.strftime("%Y-%m-%d %H:%M")))


@app.command("list")
def list_entries(limit: int = typer.Option(10, "--limit", "-n")) -> None:
    """Show the most recent entries."""
    entries = get_storage().all()[-limit:]
    table = Table("Start", "Label", "Project", "Duration", "Running")
    for entry in entries:
        table.add_row(
            entry.start.strftime("%Y-%m-%d %H:%M"),
            entry.label,
            entry.project or "",
            format_delta(entry.duration),
            "yes" if entry.is_running else "",
        )
    console.print(table)


@app.command("add")
def add_manual(
    label: str,
    duration: str = typer.Option(..., "--duration", "-d"),
    at: Optional[str] = typer.Option(None, "--at"),
    project: Optional[str] = typer.Option(None, "--project", "-p"),
) -> None:
    """Record an entry after the fact."""
    length = parse_duration(duration)
    started = datetime.fromisoformat(at) if at else datetime.now() - length
    get_storage().add(Entry(label=label, project=project, start=started, end=started + length))
    console.print("added: %s (%s)" % (label, duration), style="green")


@app.command("delete")
def delete(index: int) -> None:
    """Remove an entry by index."""
    storage = get_storage()
    entries = storage.all()
    try:
        removed = entries[index]
    except IndexError:
        console.print("no entry at index %d" % index, style="red")
        raise typer.Exit(code=1)
    storage.delete(removed.id if removed.id is not None else index)
    console.print("deleted: %s" % removed.label)


@app.command("report")
def report(
    days: int = typer.Option(1, "--days", "-n"),
    by_project: bool = typer.Option(False, "--by-project"),
    since: Optional[str] = typer.Option(None, "--from"),
    until: Optional[str] = typer.Option(None, "--to"),
    as_json: bool = typer.Option(False, "--json"),
) -> None:
    """Totals for a range of days."""
    start = parse_date(since) if since else datetime.now() - timedelta(days=days)
    end = parse_date(until) if until else None
    entries = filter_entries(get_storage().all(), start=start, end=end)
    if as_json:
        typer.echo(json.dumps(summarise(entries), default=str))
        return
    table = Table("Label", "Project", "Duration")
    for entry in entries:
        if not by_project:
            table.add_row(entry.label, entry.project or "", format_delta(entry.duration))
    if by_project:
        for name, seconds in group_by_project(entries).items():
            table.add_row(name, "", format_duration(seconds))
    console.print(table)
    console.print("total: %s" % format_duration(summarise(entries)["total_seconds"]), style="bold")


@app.command("week")
def week() -> None:
    """One line per recorded day."""
    config = Config.load()
    table = Table("Day", "Total")
    for day, entries in group_by_day(get_storage().all()).items():
        table.add_row(str(day), format_duration(summarise(entries)["total_seconds"]))
    console.print(table)
    start, end = week_bounds(datetime.now().date(), config.week_starts_on)
    console.print("week %s..%s" % (start, end))


@app.command("summary")
def summary(days: int = typer.Option(7, "--days", "-n")) -> None:
    """Compact JSON totals for scripts."""
    entries = filter_entries(get_storage().all(), start=datetime.now() - timedelta(days=days))
    data = summarise(entries)
    target = Config.load().weekly_target
    if target:
        data["target_seconds"] = target * 3600
        data["remaining_seconds"] = max(0, target * 3600 - data["total_seconds"])
    typer.echo(json.dumps(data, default=str))


@app.command("export")
def export(
    path: str,
    fmt: str = typer.Option("csv", "--format", "-f"),
) -> None:
    """Write entries to a file."""
    entries = get_storage().all()
    if fmt == "csv":
        export_csv(entries, path)
    else:
        with open(path, "w") as handle:
            handle.write(export_json(entries))
    console.print("exported %d entries to %s" % (len(entries), path), style="green")


@app.command("import")
def import_entries(path: str) -> None:
    """Load entries from a JSON export."""
    with open(path) as handle:
        entries = import_json(handle.read())
    count = add_many(get_storage(), entries)
    console.print("imported %d entries from %s" % (count, path), style="green")


@app.command("config")
def show_config() -> None:
    """Print the resolved configuration."""
    config = Config.load()
    for key, value in (
        ("database", config.database),
        ("default_project", config.default_project),
        ("week_starts_on", config.week_starts_on),
        ("weekly_target", config.weekly_target),
    ):
        console.print("%s = %s" % (key, value))


@app.command("migrate")
def migrate() -> None:
    """Move entries from JSON to SQLite."""
    target = SqliteStorage(Config.load().database)
    count = add_many(target, JsonStorage(DEFAULT_PATH).all())
    console.print("migrated %d entries" % count, style="green")


@app.command("api")
def api(
    host: str = typer.Option("127.0.0.1", "--host"),
    port: int = typer.Option(8000, "--port"),
    reload: bool = typer.Option(False, "--reload"),
) -> None:
    """Run the HTTP API with uvicorn."""
    import uvicorn

    uvicorn.run("tempus.api.main:app", host=host, port=port, reload=reload)
