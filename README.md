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
