# tempus

A small, self-hosted time tracker. It started as a single Python file and now
ships a CLI, an HTTP API and a small web dashboard.

## Features

- Start/stop timers from the terminal, with projects and tags.
- Reports by day, project or arbitrary date range.
- CSV and JSON export/import.
- SQLite storage with a JSON fallback for old installs.
- Weekly targets and a compact JSON summary for status bars.
- Test suite, type checking and linting in CI.

## Install

```
$ python -m venv .venv
$ . .venv/bin/activate
$ pip install -e ".[dev]"
```

## Usage

```
$ tempus start "writing docs" --project tempus --tags docs
$ tempus stop
$ tempus report --days 7 --by-project
$ tempus export --format csv ~/Downloads/tempus.csv
```

See [docs/cli.md](docs/cli.md) for the full command list, or the published
documentation site for the longer guides.

## HTTP API

```
$ uvicorn tempus.api.main:app --reload
$ curl localhost:8000/api/reports/summary
```

The API shares the SQLAlchemy models with the CLI through the `tempus.db`
package. See [docs/api.md](docs/api.md).

## Layout

| Path | Purpose |
| --- | --- |
| `tempus/` | Core package and CLI |
| `tempus/api/` | FastAPI application |
| `web/` | React dashboard |
| `deploy/` | Reverse proxy and backup scripts |
| `migrations/` | Alembic revisions |
| `tests/` | pytest suite |
| `docs/` | Hand written documentation |
| `scripts/` | Maintenance scripts |

## License

MIT
