#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 \
    -v read_only_user="${GRAFANA_READ_ONLY_USER}" \
    -v read_only_password="${GRAFANA_READ_ONLY_PASSWORD}" \
    --username "${POSTGRES_USER}" --dbname "${POSTGRES_DB}" <<'EOF'
CREATE ROLE :"read_only_user" LOGIN PASSWORD :'read_only_password';
GRANT CONNECT ON DATABASE :"DBNAME" TO :"read_only_user";
GRANT USAGE ON SCHEMA public TO :"read_only_user";
GRANT SELECT ON ALL TABLES IN SCHEMA public TO :"read_only_user";
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO :"read_only_user";
EOF