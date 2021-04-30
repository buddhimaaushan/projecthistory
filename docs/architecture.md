# Architecture

The project is intentionally layered so the same core can serve the CLI today
and a small API later.

```
tempus/
  models.py     dataclasses, no I/O
  storage.py    persistence (JSON and SQLite)
  reports.py    pure aggregation helpers
  export.py     CSV/JSON adapters
  config.py     configuration precedence
  cli.py        argument parsing and presentation
```

Rules of thumb:

- `models`, `reports` and `export` must not print or read argv.
- Storage backends expose `all`, `add`, `update` and `delete`.
- The CLI converts exceptions into exit codes; it never raises for user error.

The SQLite schema is deliberately boring. Timestamps are stored as ISO strings
in local time so they stay readable when debugging by hand.


## Search and filters

Keep search and filters in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs. Most search and filters questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock.


## Request lifecycle

Request lifecycle follows the same rule everywhere: one canonical representation on disk, formatting only at the edges. There is no background process. Everything related to request lifecycle happens when a command runs, which keeps the data model predictable.


## CORS

Most cors questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock. There is no background process. Everything related to cors happens when a command runs, which keeps the data model predictable.
