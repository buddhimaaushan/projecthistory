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

Configuration precedence is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. If you are upgrading from an older version, check configuration precedence before importing years of history. The importer is deliberately strict.


## Choosing a database location

Keep choosing a database location in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs. A short note on choosing a database location: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong.


## Working with tags

When working with tags misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get. Working with tags is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test.


## Grouping by project

There is no background process. Everything related to grouping by project happens when a command runs, which keeps the data model predictable. Grouping by project is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test.


## Date ranges in reports

There is no background process. Everything related to date ranges in reports happens when a command runs, which keeps the data model predictable. Date ranges in reports is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test.


## Exporting to CSV

If you are upgrading from an older version, check exporting to csv before importing years of history. The importer is deliberately strict. Exporting to CSV follows the same rule everywhere: one canonical representation on disk, formatting only at the edges.


## Importing JSON exports

Importing JSON exports is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. Most importing json exports questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## Weekly targets

Most weekly targets questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock. Keep weekly targets in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs.


## Time zone handling

Time zone handling follows the same rule everywhere: one canonical representation on disk, formatting only at the edges. There is no background process. Everything related to time zone handling happens when a command runs, which keeps the data model predictable.


## Backup and restore

If you are upgrading from an older version, check backup and restore before importing years of history. The importer is deliberately strict. A short note on backup and restore: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong.


## Running on a server

If you are upgrading from an older version, check running on a server before importing years of history. The importer is deliberately strict. A short note on running on a server: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong.
