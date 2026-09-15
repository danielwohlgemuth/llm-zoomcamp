#!/usr/bin/env bash

source .env
docker exec -ti 07-project-postgres-1 psql -U $POSTGRES_USER -d $POSTGRES_DB
