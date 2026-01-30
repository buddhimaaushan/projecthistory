# Release checklist

1. Run the full suite: `pytest` in the root and `npm test` in `web/`.
2. Check `ruff check tempus tests` and `npm run lint`.
3. Update `CHANGELOG.md` and bump `tempus/__init__.py`.
4. Run the migrations against a copy of production data.
5. Tag the release: `git tag -a vX.Y.Z -m "vX.Y.Z"` and push the tag.
6. Confirm the container image appears in GHCR.
7. Deploy, then check `/health` and the dashboard login.
