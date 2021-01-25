# CLI reference

| Command | Description |
| --- | --- |
| `start <label>` | Start a timer, optionally with `--project` and `--tags`. |
| `stop` | Stop the running timer. |
| `status` | Print the running entry. |
| `list` | Show the ten most recent entries. |
| `add <label> --duration 1h30m` | Record an entry after the fact. |
| `edit <index> --label ...` | Change an existing entry. |
| `delete <index>` | Remove an entry. |
| `report --days 7` | Totals for the last seven days. |
| `report --from 2021-05-01 --to 2021-06-01` | Totals for a date range. |
| `week` | One line per day. |
| `summary --days 7` | JSON totals for scripts. |
| `export --format csv out.csv` | Export entries. |
| `import out.json` | Import entries. |
| `config` | Print resolved configuration. |
| `migrate` | Move JSON entries into SQLite. |

Exit codes are 0 on success and 1 on user error, so the commands compose well in
shell scripts.
