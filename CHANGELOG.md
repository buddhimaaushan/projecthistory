# Changelog

## 1.0.0

Seven years after the first commit, tempus is feature complete for its original
purpose: one person, one timer, a readable history.

- CLI with projects, tags, ranges, exports and weekly targets.
- FastAPI backend with accounts, scoped data, caching and metrics.
- React dashboard with a weekly chart, dark mode and mobile layout.
- SQLite for local use, PostgreSQL for the compose stack.
- Documentation site, release checklist and security policy.

Earlier releases:

## 0.8.0

- JSON logging, request ids, Prometheus metrics and a fixed window rate limiter.
- Report summaries are cached for thirty seconds and invalidated on writes.
- CLI rewritten with typer and rich, including an `api` command.
- Playwright end-to-end tests cover login and the timer.

## 0.7.0

- Email and password accounts with JWT access tokens.
- Entries, projects and reports are scoped to the signed in user.
- Login screen and protected routes in the dashboard.
- PostgreSQL compose stack, reverse proxy sample and backup script.

## 0.6.0

- React and TypeScript dashboard with a weekly chart.
- Typed API client, hooks and unit tested formatting helpers.
- nginx image and automated web build.

## 0.5.0

- HTTP API built on FastAPI and SQLAlchemy.
- Alembic migrations, Docker image and compose file.
- Start/stop endpoints enforce a single running timer.

## 0.4.0

- `reports` and `export` modules keep the CLI thin.
- CSV and JSON export, JSON import, date ranges and weekly targets.

## 0.3.0

- Manual entries, editing, tags and per-project totals.

## 0.2.0

- Package layout, SQLite storage, configuration and pytest.

## 0.1.0

- Initial CLI with start, stop, status and report.
