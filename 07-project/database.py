import os

import psycopg2
from dotenv import load_dotenv
from pgvector.psycopg2 import register_vector

from embedder import Embedder

load_dotenv()


rrf_k = 60

class Database:
    def __init__(self):
        self.model = Embedder()
        self.conn = psycopg2.connect(
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            host=os.environ.get("POSTGRES_HOST", "localhost"),
            port=os.environ.get("POSTGRES_PORT", "5432"),
        )
        self.conn.autocommit = True
        with self.conn.cursor() as cur:
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
            register_vector(cur)
            cur.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id bigserial PRIMARY KEY,
                content text,
                embedding vector(384)
            )
            """)
            cur.execute("CREATE INDEX IF NOT EXISTS documents_idx ON documents USING GIN (to_tsvector('english', content))")
    
    def insert(self, content: str):
        embedding = self.model.encode(content)
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO documents (content, embedding) VALUES (%s, %s)", (content, embedding))

    def search(self, query: str) -> list[str]:
        embedding = self.model.encode(query)
        sql = """
        WITH semantic_search AS (
            SELECT id, RANK () OVER (ORDER BY embedding <=> %(embedding)s) AS rank
            FROM documents
            ORDER BY embedding <=> %(embedding)s
            LIMIT 20
        ),
        keyword_search AS (
            SELECT id, RANK () OVER (ORDER BY ts_rank_cd(to_tsvector('english', content), query) DESC)
            FROM documents, plainto_tsquery('english', %(query)s) query
            WHERE to_tsvector('english', content) @@ query
            ORDER BY ts_rank_cd(to_tsvector('english', content), query) DESC
            LIMIT 20
        )
        SELECT
            COALESCE(semantic_search.id, keyword_search.id),
            COALESCE(1.0 / (%(k)s + semantic_search.rank), 0.0) +
            COALESCE(1.0 / (%(k)s + keyword_search.rank), 0.0) AS score
        FROM semantic_search
        FULL OUTER JOIN keyword_search ON semantic_search.id = keyword_search.id
        ORDER BY score DESC
        LIMIT 5
        """

        with self.conn.cursor() as cur:
            cur.execute(sql, { "embedding": embedding, "query": query, "k": rrf_k })

            document_ids = [row[0] for row in cur]
            print('document_ids', document_ids)

            cur.execute("SELECT id, content FROM documents WHERE id = ANY(%s) ORDER BY array_position(%s, id)", (document_ids, document_ids))
            return [row[1] for row in cur]
