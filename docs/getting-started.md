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


## Importing from other tools

Importing from other tools follows the same rule everywhere: one canonical representation on disk, formatting only at the edges. When importing from other tools misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get.


## Dependency policy

A short note on dependency policy: prefer the documented flags over editing the database by hand. Hand edits are supported but easy to get wrong. If you are upgrading from an older version, check dependency policy before importing years of history. The importer is deliberately strict.


## Monitoring alerts

Keep monitoring alerts in mind when writing scripts: the defaults are chosen for interactive use, not for unattended runs. When monitoring alerts misbehaves, print the resolved settings first with `tempus config`. Precedence problems explain most of the reports we get.
