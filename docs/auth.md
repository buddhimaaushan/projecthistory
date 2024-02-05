# Authentication

The API issues a signed JWT from `POST /api/auth/login`. Send it as
`Authorization: Bearer <token>` on every other request.

- Passwords are hashed with bcrypt; the plain text never reaches the database.
- Tokens expire after twelve hours by default (`TEMPUS_TOKEN_TTL_MINUTES`).
- There is no refresh token yet. The dashboard simply asks you to sign in again.
- `GET /api/auth/me` is useful for checking a token without side effects.

The token secret lives in `TEMPUS_SECRET_KEY`. Rotating it signs everyone out,
which is the quickest response to a leaked token.
