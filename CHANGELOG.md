# Changelog

## 0.7.0

- Email and password accounts with JWT access tokens.
- Entries, projects and reports are scoped to the signed in user.
- Login screen and protected routes in the dashboard.
- PostgreSQL compose stack, reverse proxy sample and backup script.


## 0.6.0

- React and TypeScript dashboard with a weekly chart.
- Typed API client, hooks and unit tested formatting helpers.
- nginx image and automated web build.


## 0.5.0

- Read-only AND writing HTTP API built on FastAPI and SQLAlchemy.
- Alembic migrations, Docker image and compose file.
- Start/stop endpoints enforce a single running timer.
- Report summaries grouped by project and day.


## 0.4.0

- `reports` and `export` modules keep the CLI thin.
- CSV and JSON export, JSON import.
- Date range filters, `summary` command and weekly targets.
- Type hints, mypy, tox and pre-commit.
- `weekly_target` is shown as remaining time in `summary`.


## Unreleased

- Note the request id header.
- Mention the structured log format.
- Describe the metrics endpoint output.
- Record the new rate limit default.
- Note the Postgres image version.
- Mention the backup script path.
- Describe the compose health check.
- Add a note about the API worker count.
- Note the lazy chart import.
- Mention the reduced bundle size.
- Describe the sign out behaviour.
- Record the login error message.
- Note the skeleton placeholders.
- Mention the offline banner.
- Describe the mobile table layout.
- Note the new chart empty state.
- Document the release checklist.
- Record the migration to Python 3.12 in CI.
- Note the security policy contact.
- Mention the new issue templates.
- Describe the dependabot grouping.
- Note the docs publishing step.
- Document the new CI workflow.
- Record the Playwright browser version.
- Note the removed flake8 config.
- Mention the ruff configuration.
- Describe the Vite 6 migration.
- Add a note about the React upgrade.
- Note the new error boundary behaviour.
- Mention the web theme persistence.
- Describe the CSV endpoint filename.
- Note the new total count header.
- Document the project rename endpoint.
- Record the token lifetime default.
- Note the updated export columns.
- Mention the new health check output.
- Describe the connection pooling change.
- Add a note about the SQLite WAL mode.
- Note the renamed environment variables.
- Mention the new cache invalidation rules.
- Describe the slower first request after boot.
- Note the new request validation errors.
- Mention the backup retention default.
- Record the nginx configuration update.
- Note the log format change.
- Document the new metrics.
- Add the deployment checklist item.
- Note the stricter password policy.
- Mention the new audit log fields.
- Describe the token refresh flow.
- Note the changed login redirect.
- Add the browser support matrix.
- Note the CSS variable rename.
- Describe the new settings page.
- Record the upgrade to React 19.
- Note the offline warning banner.
- Document the chart grouping options.
- Mention the new keyboard shortcut.
- Add a note about webhook ordering.
- Describe the workspace invite flow.
- Note the updated node requirement.
- Record the switch to ruff.
- Mention the reduced image size.
- Note the new backup script.
- Describe the change to soft deletes.
- Add the request id to the log notes.
- Note the rate limit headers.
- Document the new CORS defaults.
- Mention the faster entry listing.
- Record the deprecation of /api/v1/reports.
- Call out the new export filename.
- Note the timezone fix in reports.
- Describe the change to tag matching.
- Add the migration revision to the notes.
- Document the health endpoint changes.
- Mention the new cache headers.
- Note the minimum Python version.
- Record the docker image rename.
- Add a note about token expiry.
- Describe the new pagination parameters.
- Mention the SQLite schema change.
- Note the stricter validation on start.
- Document the new report filters.
- Call out the changed default port.
- Record the removal of the legacy flag.
- Add the missing weekly target flag.
- Describe the new summary output.
- Clarify the exit code on user errors.
- Note that --days accepts zero.
- Mention the JSON importer in the upgrade guide.

## 0.3.0

- Manual entries with `add --duration`.
- `edit` command and tags on the command line.
- Report totals grouped by project.


## 0.2.0

- Package layout with a console entry point.
- SQLite storage backend and a `migrate` command.
- Configuration file support.
- Test suite runs on pytest.

## 0.1.0

- Initial CLI with start, stop, status and report.
