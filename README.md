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
