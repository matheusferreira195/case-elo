#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER elo;
    CREATE DATABASE dw_elo;
    GRANT ALL PRIVILEGES ON DATABASE dw_elo TO elo;
    \connect dw_elo elo
    CREATE SCHEMA trs;
EOSQL