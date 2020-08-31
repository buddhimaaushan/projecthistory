# Changelog

## Unreleased

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
