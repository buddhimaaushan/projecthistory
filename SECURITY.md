# Security policy

## Reporting

Please report vulnerabilities privately using GitHub's security advisory form
rather than a public issue. Include the version, a minimal reproduction and the
impact you expect.

## Supported versions

Only the latest minor release receives fixes. The API is intended for a single
trusted network unless you put it behind TLS and a reverse proxy.

## Defaults worth knowing

- `TEMPUS_SECRET_KEY` falls back to a development value. Always set it in
  production; rotating it invalidates every token.
- Passwords are hashed with bcrypt. There is no password reset flow yet, so keep
  a copy of the database before experimenting with accounts.
- The rate limiter is per process and best effort.
