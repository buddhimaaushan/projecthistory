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


## Load testing

Load testing follows the same rule everywhere: one canonical representation on disk, formatting only at the edges. A short note on load testing: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong.


## Caching

Keep caching in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs. Caching is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test.


## Background jobs

Background jobs is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test. There is no background process. Everything related to background jobs happens when a command runs, which keeps the data model predictable.


## Webhook payloads

A short note on webhook payloads: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong. Webhook payloads is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test.


## Webhook retries

Most webhook retries questions come down to the difference between local time and stored time. The CLI always stores what you saw on the clock. There is no background process. Everything related to webhook retries happens when a command runs, which keeps the data model predictable.


## Workspace roles

There is no background process. Everything related to workspace roles happens when a command runs, which keeps the data model predictable. Keep workspace roles in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs.


## Inviting users

A short note on inviting users: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong. Keep inviting users in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs.


## Single sign-on

There is no background process. Everything related to single sign-on happens when a command runs, which keeps the data model predictable. Single sign-on is handled at the boundary. The CLI validates input before anything reaches the storage layer, which keeps the core easy to test.
