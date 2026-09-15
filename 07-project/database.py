import os

import psycopg2
from dotenv import load_dotenv
from pgvector.psycopg2 import register_vector

from embedder import Embedder

load_dotenv()


RRF_K = 60


class BaseConnection:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            host=os.environ.get("POSTGRES_HOST", "localhost"),
            port=os.environ.get("POSTGRES_PORT", "5432"),
        )
        self.connection.autocommit = True

class Migration:
    def run(self):
        DocumentMigration.run()
        DescriptionMigration.run()
        ConversationMigration.run()
        MessageMigration.run()
        ModelMigration.run()

class DocumentMigration(BaseConnection):
    def run(self):
        migrations = [
            """
            CREATE TABLE IF NOT EXISTS document (
                id bigserial PRIMARY KEY,
                file_name text,
                chunk_size int,
                chunk_index int,
                content text,
                embedding vector(384)
            )
            """,
            "CREATE INDEX IF NOT EXISTS document_idx ON document USING GIN (to_tsvector('english', content))",
            "CREATE UNIQUE INDEX IF NOT EXISTS unique_chunk_idx ON document (file_name, chunk_size, chunk_index) NULLS NOT DISTINCT",
        ]

        with self.connection.cursor() as cursor:
            cursor.execute("CREATE EXTENSION IF NOT EXISTS vector")
            register_vector(cursor)

            for migration in migrations:
                cursor.execute(migration)

class Document(BaseConnection):
    def __init__(self):
        super()
        self.model = Embedder()

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
            cursor.execute(sql, {"embedding": embedding, "query": query, "k": RRF_K})

            return [{"file_name": row[0], "content": row[1]} for row in cursor]

class DescriptionMigration(BaseConnection):
    def run(self):
        migrations = [
            """
            CREATE TABLE IF NOT EXISTS description (
                id bigserial PRIMARY KEY,
                name text,
                content text
            )
            """,
            "CREATE UNIQUE INDEX IF NOT EXISTS unique_description_idx ON description (name)"
        ]

        with self.connection.cursor() as cursor:
            for migration in migrations:
                cursor.execute(migration)

class Description(BaseConnection):
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

class ConversationMigration(BaseConnection):
    def run(self):
        migrations = [
            """
            CREATE TABLE IF NOT EXISTS conversation (
                id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
                description text,
            )
            """
        ]

        with self.connection.cursor() as cursor:
            for migration in migrations:
                cursor.execute(migration)

class Conversation(BaseConnection):
    def insert(self) -> str:
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO conversation returning id")
            return cursor[0]

    def upsert(self, id: str, description: str):
        with self.connection.cursor() as cursor:
            cursor.execute("UPDATE conversation SET description = (%s) WHERE id = (%s)", (description, id))

class MessageMigration(BaseConnection):
    def run(self):
        migrations = [
            "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\"",
            """
            CREATE TABLE IF NOT EXISTS message (
                id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
                model text,
                request_messages jsonb,
                result_message jsonb,
                status text,
                input_tokens int,
                output_tokens int
            )
            """,
            "ALTER TABLE message ADD CONSTRAINT IF NOT EXISTS chk_status CHECK (status IN ('In Progress', 'Completed', 'Failed'))",
            "ALTER TABLE message ADD COLUMN IF NOT EXISTS conversation_id INT",
            # "ALTER TABLE message DROP CONSTRAINT IF EXISTS fk_conversation",
            # "ALTER TABLE message ADD CONSTRAINT fk_conversation FOREIGN KEY (conversation_id) REFERENCES conversation (id) ON DELETE CASCADE",
            """
            DO $$ 
            BEGIN
                IF NOT EXISTS (
                    SELECT 1 FROM pg_constraint 
                    WHERE conname = 'constraint_name' 
                    AND conrelid = 'table_name'::regclass
                ) THEN
                    ALTER TABLE message ADD CONSTRAINT fk_conversation FOREIGN KEY (conversation_id) REFERENCES conversation (id) ON DELETE CASCADE;
                END IF;
            END $$;
            """,
        ]

        with self.connection.cursor() as cursor:
            for migration in migrations:
                cursor.execute(migration)

class Message(BaseConnection):
    def add(self, model: str, messages: str) -> str:
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO message (model, request_messages) VALUES (%s, %s) RETURNING id", (model, messages))
            return cursor[0]
    
    def update(self, id: str, message: str, status: str) -> str:
        with self.connection.cursor() as cursor:
            cursor.execute("UPDATE message SET response_message = (%s), status = (%s) WHERE id = (%s)", (message, status, id))

class ModelMigration(BaseConnection):
    def run(self):
        migrations = [
            """
            CREATE TABLE IF NOT EXISTS model (
                id bigserial PRIMARY KEY,
                name text,
                price_per_million_tokens double
            )
            """,
            "CREATE UNIQUE INDEX IF NOT EXISTS unique_model_name_idx ON model (name) NULL NOT DISTINCT",
        ]

        with self.connection.cursor() as cursor:
            for migration in migrations:
                cursor.execute(migration)

class Model(BaseConnection):
    def insert(self, name: str, price_per_million_tokens: float) -> str:
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO model (name, price_per_million_tokens) VALUES (%s, %s) RETURNING id", (name, price_per_million_tokens))
            return cursor[0]

    def get_price(self, id: str) -> float:
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT price_per_million_tokens FROM model WHERE id = (%s)", (id,))
            return cursor[0]