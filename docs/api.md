# HTTP API

Start the API with `uvicorn tempus.api.main:app --reload` and open
`/docs` for the generated OpenAPI interface.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| GET | `/health` | Liveness probe with the package version. |
| GET | `/api/entries` | List entries, newest first. |
| POST | `/api/entries` | Create an entry. |
| POST | `/api/entries/start` | Start a timer, refusing when one is running. |
| POST | `/api/entries/{id}/stop` | Stop a timer. |
| PATCH | `/api/entries/{id}` | Change the label, project or tags. |
| DELETE | `/api/entries/{id}` | Remove an entry. |
| GET | `/api/projects` | List active projects. |
| POST | `/api/projects` | Create a project. |
| POST | `/api/projects/{id}/archive` | Archive a project. |
| GET | `/api/tags` | List tag names. |
| GET | `/api/reports/summary` | Totals grouped by project and day. |

Listing endpoints accept `limit` and `offset`. `limit` is capped at 200 so a
sleeping browser tab cannot ask for the entire history at once.
