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
