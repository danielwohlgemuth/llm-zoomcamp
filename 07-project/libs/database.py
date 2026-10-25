import os
from contextlib import contextmanager
from decimal import Decimal
from enum import Enum

import psycopg
from dotenv import load_dotenv
from pgvector.psycopg import register_vector
from psycopg.conninfo import make_conninfo
from psycopg.types.json import Jsonb
from psycopg_pool import ConnectionPool

from libs.embedder import Embedder

load_dotenv()


RECIPROCAL_RANK_FUSION_K = 60
SYSTEM_PROMPT = """You are a knowlegde support agent for an IaaS provider called Orion Outer Orbit (OOO).
Respond to the users question based on the documents from the knowledge base.
Use the available tool to search for relevant documents.
If the documents don't answer the users question, say that you don't know.
"""
DEFAULT_MODEL = "claude-haiku-5-5"
DOCUMENT_CHUNK_SIZE = 1024
CONVERSATION_LIMIT = {
    "max_tokens": 10_000,
    "max_cost": "0.1",
    "max_turns": 10,
    "max_tool_iterations": 5,
}


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
        SettingMigration(self.db).run()
        ExampleQuestionMigration(self.db).run()


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
        self.setting = Setting(db)

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
            WHERE chunk_size = %(chunk_size)s
            ORDER BY embedding <=> %(embedding)s::vector
            LIMIT 20
        ),
        keyword_search AS (
            SELECT id, RANK () OVER (ORDER BY ts_rank_cd(to_tsvector('english', content), query) DESC)
            FROM document, plainto_tsquery('english', %(query)s) query
            WHERE to_tsvector('english', content) @@ query
            AND chunk_size = %(chunk_size)s
            ORDER BY ts_rank_cd(to_tsvector('english', content), query) DESC
            LIMIT 20
        ),
        combined AS (
            SELECT
                COALESCE(semantic_search.id, keyword_search.id) AS id,
                COALESCE(1.0 / (%(rrf_k)s + semantic_search.rank), 0.0) +
                COALESCE(1.0 / (%(rrf_k)s + keyword_search.rank), 0.0) AS score
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
                sql,
                {
                    "embedding": embedding.tolist(),
                    "query": query,
                    "rrf_k": self.setting.get("reciprocal_rank_fusion_k"),
                    "chunk_size": self.setting.get("document_chunk_size"),
                },
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

    def get_all_by_conversation(self, conversation_id: str) -> list[dict]:
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT request_messages, response FROM message "
                "WHERE conversation_id = %s ORDER BY created_at",
                (conversation_id,),
            )
            return [{"request": row[0], "response": row[1]} for row in cur]

    def get_usage_by_conversation(self, conversation_id: str) -> dict:
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT "
                "   COALESCE(SUM(m.input_tokens * mo.input_price_per_million_tokens / 1000000 + m.output_tokens * mo.output_price_per_million_tokens / 1000000), 0), "
                "   COUNT(*), "
                "   COALESCE(SUM(m.input_tokens + m.output_tokens), 0) "
                "FROM message AS m "
                "   JOIN model AS mo ON (mo.name = m.model)"
                "WHERE m.conversation_id = %s",
                (conversation_id,),
            )
            row = cur.fetchone()
            return {"cost": row[0], "turns": row[1], "tokens": row[2]}


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
            "ALTER TABLE model DROP COLUMN IF EXISTS price_per_million_tokens",
            "ALTER TABLE model ADD COLUMN IF NOT EXISTS input_price_per_million_tokens numeric",
            "ALTER TABLE model ADD COLUMN IF NOT EXISTS output_price_per_million_tokens numeric",
        ]

        with self.db.connection() as conn, conn.cursor() as cur:
            for migration in migrations:
                cur.execute(migration)

            models = [
                {
                    "name": "claude-haiku-5-5",
                    "input_price_per_million_tokens": "0.1",
                    "output_price_per_million_tokens": "0.5",
                }
            ]

            cur.executemany(
                "INSERT INTO model (name, input_price_per_million_tokens, output_price_per_million_tokens) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
                [
                    (
                        model["name"],
                        model["input_price_per_million_tokens"],
                        model["output_price_per_million_tokens"],
                    )
                    for model in models
                ],
            )


class Model:
    def __init__(self, db: Database):
        self.db = db

    def insert(
        self,
        name: str,
        input_price_per_million_tokens: Decimal,
        output_price_per_million_tokens: Decimal,
    ) -> str:
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO model (name, input_price_per_million_tokens, output_price_per_million_tokens) VALUES (%s, %s, %s) RETURNING id",
                (name, input_price_per_million_tokens, output_price_per_million_tokens),
            )
            return cur.fetchone()[0]

    def get_price(self, name: str) -> dict | None:
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT input_price_per_million_tokens, output_price_per_million_tokens FROM model WHERE name = (%s)",
                (name,),
            )
            if cur.rowcount:
                model = cur.fetchone()
                return {
                    "input_price_per_million_tokens": model[0],
                    "output_price_per_million_tokens": model[1],
                }
            return None


class SettingMigration:
    def __init__(self, db: Database):
        self.db = db

    def run(self):
        migrations = [
            """
            CREATE TABLE IF NOT EXISTS setting (
                name text NOT NULL,
                value jsonb
            )
            """,
            "CREATE UNIQUE INDEX IF NOT EXISTS uniq_setting_name ON setting (name)",
        ]

        with self.db.connection() as conn, conn.cursor() as cur:
            for migration in migrations:
                cur.execute(migration)

            settings = [
                ("default_model", DEFAULT_MODEL),
                ("system_prompt", SYSTEM_PROMPT),
                ("reciprocal_rank_fusion_k", RECIPROCAL_RANK_FUSION_K),
                ("document_chunk_size", DOCUMENT_CHUNK_SIZE),
                ("conversation_limit", CONVERSATION_LIMIT),
            ]
            cur.executemany(
                """
                INSERT INTO setting (name, value) VALUES (%s, %s)
                ON CONFLICT (name) DO UPDATE SET value = EXCLUDED.value
                """,
                [(name, Jsonb(value)) for name, value in settings],
            )


class Setting:
    def __init__(self, db: Database):
        self.db = db
        self.cache = {}

    def get(self, name: str):
        if name in self.cache:
            return self.cache[name]

        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute("SELECT value FROM setting WHERE name = %s", (name,))
            if cur.rowcount:
                value = cur.fetchone()[0]
                self.cache[name] = value
                return value
            return None


class ExampleQuestionMigration:
    def __init__(self, db: Database):
        self.db = db

    def run(self):
        with self.db.connection() as conn, conn.cursor() as cur:
            migrations = [
                """
                CREATE TABLE IF NOT EXISTS example_question (
                    id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
                    question text NOT NULL
                )
                """,
                "CREATE UNIQUE INDEX IF NOT EXISTS uniq_example_question_question ON example_question (question)",
            ]

            for migration in migrations:
                cur.execute(migration)

            questions = [
                "What kinds of use cases can I use Galactic Cargo Hold for?",
                "What determines the hardware available to a Modular Starship Hull instance when I launch it?",
                "How long can Quantum Particle Flash Sparks MicroVMs retain state?",
                "What kind of database is Singularity Vault, and what performance does it deliver?",
                "What message delivery guarantees do standard queues and FIFO queues in Pneumatic Docking Tubes offer?",
                "What kinds of endpoints can subscribe to a Red Alert Broadcaster topic?",
                "What happens when content isn't cached at the edge location closest to the user?",
                "What three main functions does Subspace Beacon Routing perform?",
                "What does Orbiting Sentinel monitor, and which tools does it offer for observability?",
            ]

            cur.executemany(
                "INSERT INTO example_question (question) VALUES (%s) ON CONFLICT DO NOTHING",
                [(question,) for question in questions],
            )


class ExampleQuestion:
    def __init__(self, db: Database):
        self.db = db

    def get_questions(self, top_n: int = 3):
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT question FROM example_question ORDER BY RANDOM() LIMIT %s",
                (top_n,),
            )
            return [row[0] for row in cur]
