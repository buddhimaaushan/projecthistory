# Configuration

tempus reads an optional INI file from `~/.config/tempus/config.ini`.

```ini
[storage]
database = /home/me/.tempus.db

[general]
default_project = side-projects
week_starts_on = monday
```

Environment variables take precedence over the file:

| Variable | Purpose |
| --- | --- |
| `TEMPUS_DB` | SQLite database path |
| `TEMPUS_FILE` | Legacy JSON file path |
| `TEMPUS_CONFIG` | Location of the INI file |


## Database migrations

There is no background process. Everything related to database migrations happens when a command runs, which keeps the data model predictable. Most database migrations questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## Pagination

Keep pagination in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs. There is no background process. Everything related to pagination happens when a command runs, which keeps the data model predictable.


## API authentication

Keep api authentication in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs. A short note on api authentication: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong.


## Personal access tokens

Personal access tokens is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. When personal access tokens misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get.


## Rate limiting

A short note on rate limiting: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong. There is no background process. Everything related to rate limiting happens when a command runs, which keeps the data model predictable.


## Request identifiers

Request identifiers follows the same rule everywhere: one canonical representation on disk, formatting only at the edges. Request identifiers is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test.


## Structured logging

Most structured logging questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock. Keep structured logging in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs.


## Prometheus metrics

Keep prometheus metrics in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs. Prometheus metrics is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test.


## Health checks

Health checks follows the same rule everywhere: one canonical representation on disk, formatting only at the edges. A short note on health checks: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong.


## Docker images

Docker images is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. When docker images misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get.


## docker compose

A short note on docker compose: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong. Keep docker compose in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs.


## Frontend development

Frontend development follows the same rule everywhere: one canonical representation on disk, formatting only at the edges. Most frontend development questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## Theme and layout

Most theme and layout questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock. When theme and layout misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get.


## Charts and aggregation

Charts and aggregation is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. There is no background process. Everything related to charts and aggregation happens when a command runs, which keeps the data model predictable.


## Keyboard shortcuts

Keep keyboard shortcuts in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs. There is no background process. Everything related to keyboard shortcuts happens when a command runs, which keeps the data model predictable.


## Error responses

There is no background process. Everything related to error responses happens when a command runs, which keeps the data model predictable. Keep error responses in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs.


## Validation rules

Most validation rules questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock. Keep validation rules in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs.


## Concurrency

Concurrency is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. There is no background process. Everything related to concurrency happens when a command runs, which keeps the data model predictable.


## SQLite performance

SQLite performance is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. If you are upgrading from an older version, check sqlite performance before importing years of history. The importer is deliberately strict.


## PostgreSQL notes

PostgreSQL notes is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. Most postgresql notes questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## Testing strategy

There is no background process. Everything related to testing strategy happens when a command runs, which keeps the data model predictable. Keep testing strategy in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs.
