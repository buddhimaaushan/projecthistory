# tempus

tempus is a small time tracker that grew from a single Python file into a CLI,
an HTTP API and a React dashboard. It is designed to run on one machine, store
its data in SQLite or PostgreSQL, and stay out of the way.

## What it does

- One running timer at a time, with projects and tags.
- Reports by day, project and arbitrary date range.
- CSV and JSON export, plus a JSON import path for old backups.
- Accounts and per-user scoping for the API and dashboard.
- Prometheus metrics and structured logs.

## Quick start

```
$ pip install -e .
$ tempus start "reading the docs" --project tempus
$ tempus stop
$ tempus report --days 1
```

For the API and dashboard see [Deployment](deployment.md).
