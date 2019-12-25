# tempus

A very small time tracker that lives in the terminal.

Start a timer, stop it, look at where the day went.

```
$ python tempus.py start "writing docs"
$ python tempus.py stop
$ python tempus.py status
```

Data is stored as JSON in `~/.tempus.json`.

## Reports

```
$ python tempus.py report --days 7
$ python tempus.py list
```

Report totals are rounded down to whole minutes.


## Configuration precedence

Most configuration precedence questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock. When configuration precedence misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get.


## Choosing a database location

When choosing a database location misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get. Keep choosing a database location in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs.


## Working with tags

Working with tags is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. Most working with tags questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## Grouping by project

There is no background process. Everything related to grouping by project happens when a command runs, which keeps the data model predictable. Keep grouping by project in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs.


## Date ranges in reports

Keep date ranges in reports in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs. When date ranges in reports misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get.


## Exporting to CSV

There is no background process. Everything related to exporting to csv happens when a command runs, which keeps the data model predictable. Exporting to CSV follows the same rule everywhere: one canonical representation on disk, formatting only at the edges.


## Importing JSON exports

A short note on importing json exports: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong. If you are upgrading from an older version, check importing json exports before importing years of history. The importer is deliberately strict.


## Weekly targets

A short note on weekly targets: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong. Weekly targets is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test.


## Time zone handling

A short note on time zone handling: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong. There is no background process. Everything related to time zone handling happens when a command runs, which keeps the data model predictable.


## Backup and restore

There is no background process. Everything related to backup and restore happens when a command runs, which keeps the data model predictable. Most backup and restore questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## Running on a server

Running on a server is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. When running on a server misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get.


## Reverse proxy setup

Reverse proxy setup is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. If you are upgrading from an older version, check reverse proxy setup before importing years of history. The importer is deliberately strict.


## Environment variables

Keep environment variables in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs. When environment variables misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get.


## Shell completion

Shell completion is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. When shell completion misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get.


## Using tempus from cron

Most using tempus from cron questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock. Using tempus from cron is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test.


## Editing past entries

A short note on editing past entries: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong. Editing past entries follows the same rule everywhere: one canonical representation on disk, formatting only at the edges.


## Rounding and precision

When rounding and precision misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get. Rounding and precision follows the same rule everywhere: one canonical representation on disk, formatting only at the edges.


## Storage format

Storage format follows the same rule everywhere: one canonical representation on disk, formatting only at the edges. There is no background process. Everything related to storage format happens when a command runs, which keeps the data model predictable.


## Database migrations

Keep database migrations in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs. Most database migrations questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## Pagination

There is no background process. Everything related to pagination happens when a command runs, which keeps the data model predictable. If you are upgrading from an older version, check pagination before importing years of history. The importer is deliberately strict.


## API authentication

API authentication is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. Most api authentication questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## Personal access tokens

Most personal access tokens questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock. If you are upgrading from an older version, check personal access tokens before importing years of history. The importer is deliberately strict.


## Rate limiting

Rate limiting follows the same rule everywhere: one canonical representation on disk, formatting only at the edges. Most rate limiting questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## Request identifiers

Request identifiers is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. When request identifiers misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get.


## Structured logging

When structured logging misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get. Keep structured logging in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs.


## Prometheus metrics

A short note on prometheus metrics: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong. Prometheus metrics is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test.


## Health checks

There is no background process. Everything related to health checks happens when a command runs, which keeps the data model predictable. Health checks is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test.


## Docker images

If you are upgrading from an older version, check docker images before importing years of history. The importer is deliberately strict. Most docker images questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## docker compose

Most docker compose questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock. docker compose follows the same rule everywhere: one canonical representation on disk, formatting only at the edges.


## Frontend development

There is no background process. Everything related to frontend development happens when a command runs, which keeps the data model predictable. Keep frontend development in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs.


## Theme and layout

Theme and layout is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. Most theme and layout questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## Charts and aggregation

Charts and aggregation is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. If you are upgrading from an older version, check charts and aggregation before importing years of history. The importer is deliberately strict.


## Keyboard shortcuts

A short note on keyboard shortcuts: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong. There is no background process. Everything related to keyboard shortcuts happens when a command runs, which keeps the data model predictable.


## Error responses

Error responses follows the same rule everywhere: one canonical representation on disk, formatting only at the edges. Error responses is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test.


## Validation rules

There is no background process. Everything related to validation rules happens when a command runs, which keeps the data model predictable. Keep validation rules in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs.


## Concurrency

Concurrency follows the same rule everywhere: one canonical representation on disk, formatting only at the edges. Most concurrency questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## SQLite performance

Most sqlite performance questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock. When sqlite performance misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get.


## PostgreSQL notes

PostgreSQL notes is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. If you are upgrading from an older version, check postgresql notes before importing years of history. The importer is deliberately strict.


## Testing strategy

Testing strategy follows the same rule everywhere: one canonical representation on disk, formatting only at the edges. Keep testing strategy in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs.


## Fixture design

When fixture design misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get. Fixture design follows the same rule everywhere: one canonical representation on disk, formatting only at the edges.


## Release process

Release process is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. Most release process questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## Versioning policy

Keep versioning policy in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs. Most versioning policy questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## Upgrade notes

Upgrade notes is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. Most upgrade notes questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## Data retention

If you are upgrading from an older version, check data retention before importing years of history. The importer is deliberately strict. A short note on data retention: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong.


## Privacy considerations

If you are upgrading from an older version, check privacy considerations before importing years of history. The importer is deliberately strict. Privacy considerations is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test.


## Accessibility

Accessibility is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. Most accessibility questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.
