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
