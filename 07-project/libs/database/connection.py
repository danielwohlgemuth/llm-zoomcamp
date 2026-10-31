import os
from contextlib import contextmanager

import psycopg
from dotenv import load_dotenv
from pgvector.psycopg import register_vector
from psycopg.conninfo import make_conninfo
from psycopg_pool import ConnectionPool

load_dotenv()


class Database:
    def __init__(self, min_size=1, max_size=10):
        conninfo = make_conninfo(
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            host=os.environ.get("POSTGRES_HOST", "localhost"),
            port=os.environ.get("POSTGRES_PORT", "5432"),
        )
        with psycopg.connect(conninfo, autocommit=True) as conn:
            conn.execute("CREATE EXTENSION IF NOT EXISTS vector")

        self._pool = ConnectionPool(
            conninfo=make_conninfo(
                dbname=os.environ["POSTGRES_DB"],
                user=os.environ["POSTGRES_USER"],
                password=os.environ["POSTGRES_PASSWORD"],
                host=os.environ.get("POSTGRES_HOST", "localhost"),
                port=os.environ.get("POSTGRES_PORT", "5432"),
            ),
            min_size=min_size,
            max_size=max_size,
            configure=register_vector,
            open=True,
        )

    @contextmanager
    def connection(self):
        with self._pool.connection() as conn:
            yield conn

    def close(self):
        self._pool.close()
