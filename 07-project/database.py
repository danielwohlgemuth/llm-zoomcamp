import os
from contextlib import contextmanager
from decimal import Decimal
from enum import Enum

import psycopg
from dotenv import load_dotenv
from pgvector.psycopg import register_vector
from psycopg.conninfo import make_conninfo
from psycopg_pool import ConnectionPool

from embedder import Embedder

load_dotenv()


RRF_K = 60

# Index and constraint naming conventions
# idx_{table}_{column}
# uniq_{table}_{column}
# fk_{table}_{column}_{ref_table}
# chk_{table}_{column}
# tr_{table}_{timing: [b]efore/[a]fter [i]nsert/[u]pdate/[d]elete}_{purpose}
# fn_{table}_{timing: [b]efore/[a]fter [i]nsert/[u]pdate/[d]elete}_{purpose}


class MessageStatus(Enum):
    InProgress = "In Progress"
    Completed = "Completed"
    Failed = "Failed"


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


class Migration:
    def __init__(self, db: Database):
        self.db = db

    def run(self):
        DocumentMigration(self.db).run()
        DescriptionMigration(self.db).run()
        ConversationMigration(self.db).run()
        MessageMigration(self.db).run()
        ModelMigration(self.db).run()


class DocumentMigration:
    def __init__(self, db: Database):
        self.db = db

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
            "CREATE INDEX IF NOT EXISTS idx_document_content ON document USING GIN (to_tsvector('english', content))",
            "CREATE UNIQUE INDEX IF NOT EXISTS uniq_document_file_name_chunk_size_chunk_index ON document (file_name, chunk_size, chunk_index) NULLS NOT DISTINCT",
        ]

        with self.db.connection() as conn, conn.cursor() as cur:
            for migration in migrations:
                cur.execute(migration)


class Document:
    def __init__(self, db: Database, embedder: Embedder):
        self.db = db
        self.embedder = embedder

    def insert(
        self, file_name: str, chunk_size: int, chunk_index: int, content: str
    ) -> None:
        embedding = self.embedder.encode(content)
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO document (file_name, chunk_size, chunk_index, content, embedding) VALUES (%s, %s, %s, %s, %s)",
                (file_name, chunk_size, chunk_index, content, embedding.tolist()),
            )

    def search(self, query: str) -> list[str]:
        embedding = self.embedder.encode(query)
        sql = """
        WITH semantic_search AS (
            SELECT id, RANK () OVER (ORDER BY embedding <=> %(embedding)s::vector) AS rank
            FROM document
            WHERE chunk_size = 1024
            ORDER BY embedding <=> %(embedding)s::vector
            LIMIT 20
        ),
        keyword_search AS (
            SELECT id, RANK () OVER (ORDER BY ts_rank_cd(to_tsvector('english', content), query) DESC)
            FROM document, plainto_tsquery('english', %(query)s) query
            WHERE to_tsvector('english', content) @@ query
            AND chunk_size = 1024
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

        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                sql, {"embedding": embedding.tolist(), "query": query, "k": RRF_K}
            )

            return [
                {"file_name": row[0], "content": row[1], "score": row[2]} for row in cur
            ]

    def get_all(self):
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT file_name FROM document WHERE chunk_size = 0 ORDER BY file_name"
            )

            return [{"file_name": row[0]} for row in cur]

    def get_by_file_name(self, file_name):
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT file_name, content FROM document WHERE chunk_size = 0 AND file_name = %s",
                (file_name,),
            )

            return [{"file_name": row[0], "content": row[1]} for row in cur]


class DescriptionMigration:
    def __init__(self, db: Database):
        self.db = db

    def run(self):
        migrations = [
            """
            CREATE TABLE IF NOT EXISTS description (
                id bigserial PRIMARY KEY,
                name text,
                content text
            )
            """,
            "CREATE UNIQUE INDEX IF NOT EXISTS uniq_description_name ON description (name)",
        ]

        with self.db.connection() as conn, conn.cursor() as cur:
            for migration in migrations:
                cur.execute(migration)


class Description:
    def __init__(self, db: Database):
        self.db = db

    def insert(self, name: str, description: str) -> None:
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO description (name, content) VALUES (%s, %s)",
                (name, description),
            )

    def list(self, name: str | None = None) -> list[str]:
        with self.db.connection() as conn, conn.cursor() as cur:
            if name:
                cur.execute(
                    "SELECT name, content FROM description WHERE name ILIKE %s ORDER BY name",
                    ("%" + name + "%",),
                )
            else:
                cur.execute("SELECT name, content FROM description ORDER BY name")
            return [{"name": row[0], "content": row[1]} for row in cur]

    def search(self, name: str) -> str | None:
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute("SELECT content FROM description WHERE name = %s", (name,))
            if cur.rowcount:
                return cur.fetchone()[0]
            else:
                return None


class ConversationMigration:
    def __init__(self, db: Database):
        self.db = db

    def run(self):
        migrations = [
            'CREATE EXTENSION IF NOT EXISTS "uuid-ossp"',
            """
            CREATE TABLE IF NOT EXISTS conversation (
                id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
                description text
            )
            """,
            "ALTER TABLE conversation ADD COLUMN IF NOT EXISTS created_at timestamptz DEFAULT now()",
            "ALTER TABLE conversation ADD COLUMN IF NOT EXISTS updated_at timestamptz DEFAULT now()",
        ]

        with self.db.connection() as conn, conn.cursor() as cur:
            for migration in migrations:
                cur.execute(migration)


class Conversation:
    def __init__(self, db: Database):
        self.db = db

    def insert(self, description: str) -> str:
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO conversation (description) VALUES (%s) RETURNING id",
                (description,),
            )
            return str(cur.fetchone()[0])

    def get_all(self) -> list[dict]:
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT id, description FROM conversation ORDER BY updated_at DESC"
            )
            return [{"id": str(row[0]), "description": row[1]} for row in cur]


class MessageMigration:
    def __init__(self, db: Database):
        self.db = db

    def run(self):
        migrations = [
            'CREATE EXTENSION IF NOT EXISTS "uuid-ossp"',
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
            "ALTER TABLE message ADD COLUMN IF NOT EXISTS conversation_id uuid",
            """
            DO $$ 
            BEGIN
                IF NOT EXISTS (
                    SELECT 1 FROM pg_constraint 
                    WHERE conname = 'chk_message_status' 
                    AND conrelid = 'message'::regclass
                ) THEN
                    ALTER TABLE message
                    ADD CONSTRAINT chk_message_status
                    CHECK (status IN ('In Progress', 'Completed', 'Failed'));
                END IF;
            END $$;
            """,
            """
            DO $$ 
            BEGIN
                IF NOT EXISTS (
                    SELECT 1 FROM pg_constraint 
                    WHERE conname = 'fk_conversation_conversation_id_conversation' 
                    AND conrelid = 'message'::regclass
                ) THEN
                    ALTER TABLE message
                    ADD CONSTRAINT fk_conversation_conversation_id_conversation
                    FOREIGN KEY (conversation_id)
                    REFERENCES conversation (id)
                    ON DELETE CASCADE;
                END IF;
            END $$;
            """,
            "ALTER TABLE message ADD COLUMN IF NOT EXISTS created_at timestamptz DEFAULT now()",
            """
            CREATE OR REPLACE FUNCTION fn_message_ai_au_touch_conversation() RETURNS trigger AS $$
            BEGIN
                UPDATE conversation
                SET updated_at = now()
                WHERE id = NEW.conversation_id;
                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;
            """,
            "DROP TRIGGER IF EXISTS tr_message_ai_au_touch_conversation ON message",
            """
            CREATE TRIGGER tr_message_ai_au_touch_conversation
            AFTER INSERT OR UPDATE ON message
            FOR EACH ROW EXECUTE FUNCTION fn_message_ai_au_touch_conversation()
            """,
            """
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT 1 FROM information_schema.columns
                    WHERE table_name = 'message' AND column_name = 'result_message'
                ) THEN
                    ALTER TABLE message RENAME COLUMN result_message TO response;
                END IF;
            END $$;
            """,
        ]

        with self.db.connection() as conn, conn.cursor() as cur:
            for migration in migrations:
                cur.execute(migration)


class Message:
    def __init__(self, db: Database):
        self.db = db

    def add(self, conversation_id: str, model: str, messages: str) -> str:
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO message (conversation_id, model, request_messages, status) "
                "VALUES (%s, %s, %s, 'In Progress') "
                "RETURNING id",
                (conversation_id, model, messages),
            )
            return str(cur.fetchone()[0])

    def update(
        self, id: str, message: str, status: str, input_tokens: int, output_tokens: int
    ) -> None:
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "UPDATE message "
                "SET response = (%s), status = (%s), input_tokens = (%s), output_tokens = (%s) "
                "WHERE id = (%s)",
                (message, status, input_tokens, output_tokens, id),
            )

    def get_by_conversation(self, conversation_id: str) -> list[dict]:
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT request_messages, response FROM message "
                "WHERE conversation_id = %s ORDER BY created_at",
                (conversation_id,),
            )
            return [{"request": row[0], "response": row[1]} for row in cur]


class ModelMigration:
    def __init__(self, db: Database):
        self.db = db

    def run(self):
        migrations = [
            """
            CREATE TABLE IF NOT EXISTS model (
                id bigserial PRIMARY KEY,
                name text,
                price_per_million_tokens numeric
            )
            """,
            "CREATE UNIQUE INDEX IF NOT EXISTS uniq_model_name ON model (name)",
        ]

        with self.db.connection() as conn, conn.cursor() as cur:
            for migration in migrations:
                cur.execute(migration)


class Model:
    def __init__(self, db: Database):
        self.db = db

    def insert(self, name: str, price_per_million_tokens: Decimal) -> str:
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO model (name, price_per_million_tokens) VALUES (%s, %s) RETURNING id",
                (name, price_per_million_tokens),
            )
            return cur.fetchone()[0]

    def get_price(self, id: str) -> Decimal:
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT price_per_million_tokens FROM model WHERE id = (%s)", (id,)
            )
            return cur.fetchone()[0]
