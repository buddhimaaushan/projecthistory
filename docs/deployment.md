# Deployment

The smallest sensible production setup is docker compose with PostgreSQL and a
reverse proxy that terminates TLS.

1. Copy `docker-compose.prod.yml` and create `.env` with `POSTGRES_PASSWORD`
   and a random `TEMPUS_SECRET_KEY`.
2. Start the stack with `docker compose -f docker-compose.prod.yml up -d`.
3. Put the nginx sample from `deploy/nginx.conf` in front of ports 3000 and 8000.
4. Schedule `deploy/backup.sh` daily. It keeps thirty days of dumps.

## Upgrades

Run `alembic upgrade head` before restarting the API container. The compose
command already does this, which is fine for a single node deployment.

## Secrets

Never ship the default `TEMPUS_SECRET_KEY`. Rotating it invalidates every
issued token, which is the intended way to force a re-login after a leak.
