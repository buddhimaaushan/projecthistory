# Getting started

## Install

```
$ python -m venv .venv
$ . .venv/bin/activate
$ pip install -e .
```

The first time you run `tempus`, entries are stored in the legacy JSON file. Run
`tempus migrate` once to move them into SQLite.

## A normal day

```
$ tempus start "review pull requests" --project tempus --tags review
$ tempus stop
$ tempus today
```

If you forget to stop a timer, `tempus edit` lets you fix the label but the end
time still has to come from `tempus stop`. Manual entries are easier:

```
$ tempus add "writing notes" --duration 45m
```

## Where is my data?

- SQLite database: `~/.tempus.db` (override with `TEMPUS_DB`).
- JSON fallback: `~/.tempus.json` (override with `TEMPUS_FILE`).
- Config: `~/.config/tempus/config.ini`.
