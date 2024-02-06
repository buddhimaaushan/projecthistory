#!/usr/bin/env bash
set -euo pipefail

: "${TEMPUS_BACKUP_DIR:=/var/backups/tempus}"
: "${TEMPUS_DATABASE_URL:?set TEMPUS_DATABASE_URL}"

mkdir -p "$TEMPUS_BACKUP_DIR"
stamp=$(date +%Y%m%d-%H%M%S)

if [[ "$TEMPUS_DATABASE_URL" == postgresql* ]]; then
  pg_dump --no-owner --format=custom "$TEMPUS_DATABASE_URL" > "$TEMPUS_BACKUP_DIR/tempus-$stamp.dump"
else
  sqlite3 "${TEMPUS_DATABASE_URL#sqlite:///}" ".backup '$TEMPUS_BACKUP_DIR/tempus-$stamp.db'"
fi

find "$TEMPUS_BACKUP_DIR" -type f -mtime +30 -delete
echo "wrote $TEMPUS_BACKUP_DIR/tempus-$stamp"
