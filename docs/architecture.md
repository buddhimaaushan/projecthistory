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
