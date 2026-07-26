import os

import psycopg2
from dotenv import load_dotenv
from pgvector.psycopg2 import register_vector

from embedder import Embedder

load_dotenv()


rrf_k = 60


class Document:
    def __init__(self):
        self.model = Embedder()
        self.connection = psycopg2.connect(
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            host=os.environ.get("POSTGRES_HOST", "localhost"),
            port=os.environ.get("POSTGRES_PORT", "5432"),
        )
        self.connection.autocommit = True
        with self.connection.cursor() as cursor:
            cursor.execute("CREATE EXTENSION IF NOT EXISTS vector")
            register_vector(cursor)
            sql = """
            CREATE TABLE IF NOT EXISTS document (
                id bigserial PRIMARY KEY,
                file_name text,
                chunk_size int,
                chunk_index int,
                content text,
                embedding vector(384)
            )
            """
            cursor.execute(sql)
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS document_idx ON document USING GIN (to_tsvector('english', content))"
            )
            cursor.execute(
                "CREATE UNIQUE INDEX IF NOT EXISTS unique_chunk_idx ON document (file_name, chunk_size, chunk_index) NULLS NOT DISTINCT"
            )

    def insert(
        self, file_name: str, chunk_size: int, chunk_index: int, content: str
    ) -> None:
        embedding = self.model.encode(content)
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO document (file_name, chunk_size, chunk_index, content, embedding) VALUES (%s, %s, %s, %s, %s)",
                (file_name, chunk_size, chunk_index, content, embedding),
            )

    def search(self, query: str) -> list[str]:
        embedding = self.model.encode(query)
        sql = """
        WITH semantic_search AS (
            SELECT id, RANK () OVER (ORDER BY embedding <=> %(embedding)s) AS rank
            FROM document
            ORDER BY embedding <=> %(embedding)s
            LIMIT 20
        ),
        keyword_search AS (
            SELECT id, RANK () OVER (ORDER BY ts_rank_cd(to_tsvector('english', content), query) DESC)
            FROM document, plainto_tsquery('english', %(query)s) query
            WHERE to_tsvector('english', content) @@ query
            ORDER BY ts_rank_cd(to_tsvector('english', content), query) DESC
            LIMIT 20
        ),
        combined AS (
            SELECT
                COALESCE(semantic_search.id, keyword_search.id) AS id,
                COALESCE(1.0 / (%(k)s + semantic_search.rank), 0.0) +
                COALESCE(1.0 / (%(k)s + keyword_search.rank), 0.0) AS score
            FROM semantic_search
            FULL OUTER JOIN keyword_search ON semantic_search.id = keyword_search.id
        )
        SELECT
            document.file_name,
            document.content,
            combined.score
        FROM combined
        JOIN document ON document.id = combined.id
        ORDER BY combined.score DESC
        LIMIT 5
        """

        with self.connection.cursor() as cursor:
            cursor.execute(sql, {"embedding": embedding, "query": query, "k": rrf_k})

            return [{"file_name": row[0], "content": row[1]} for row in cursor]


class Description:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            host=os.environ.get("POSTGRES_HOST", "localhost"),
            port=os.environ.get("POSTGRES_PORT", "5432"),
        )
        self.connection.autocommit = True
        with self.connection.cursor() as cursor:
            sql = """
            CREATE TABLE IF NOT EXISTS description (
                id bigserial PRIMARY KEY,
                name text,
                content text
            )
            """
            cursor.execute(sql)
            cursor.execute(
                "CREATE UNIQUE INDEX IF NOT EXISTS unique_description_idx ON description (name)"
            )

    def insert(self, name: str, description: str) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO description (name, content) VALUES (%s, %s)",
                (name, description),
            )

    def search(self, name: str) -> str | None:
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT content FROM description WHERE name = %s", (name,))
            if cursor.rowcount:
                return cursor.fetchone()[0]
            else:
                return None
