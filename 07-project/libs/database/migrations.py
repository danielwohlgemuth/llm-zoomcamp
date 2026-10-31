from psycopg.types.json import Jsonb

from libs.database.connection import Database

RECIPROCAL_RANK_FUSION_K = 60
COSINE_DISTANCE = 0.7
SYSTEM_PROMPT = """You are a knowlegde support agent for an IaaS provider called Orion Outer Orbit (OOO).
Respond to the users question based on the documents from the knowledge base.
Use the available tool to search for relevant documents.
If the documents don't answer the users question, say that you don't know.
"""
DEFAULT_MODEL = "claude-haiku-5-5"
DOCUMENT_CHUNK_SIZE = 1024
CONVERSATION_LIMIT = {
    "max_input_tokens": 20_000,
    "max_output_tokens": 4_000,
    "max_cost": "0.1",
    "max_turns": 10,
    "max_tool_iterations": 5,
}

# Migrations
DOCUMENT_MIGRATIONS = [
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
DESCRIPTION_MIGRATION = [
    """
    CREATE TABLE IF NOT EXISTS description (
        id bigserial PRIMARY KEY,
        name text,
        content text
    )
    """,
    "CREATE UNIQUE INDEX IF NOT EXISTS uniq_description_name ON description (name)",
]
CONVERSATION_MIGRATION = [
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
MESSAGE_MIGRATION = [
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
MODEL_MIGRATION = [
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
MODEL_PRICINGS_STATEMENT = "INSERT INTO model (name, input_price_per_million_tokens, output_price_per_million_tokens) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING"
MODEL_PRICINGS = [
    {
        "name": "claude-haiku-5-5",
        "input_price_per_million_tokens": "0.1",
        "output_price_per_million_tokens": "0.5",
    }
]
SETTING_MIGRATION = [
    """
    CREATE TABLE IF NOT EXISTS setting (
        name text NOT NULL,
        value jsonb
    )
    """,
    "CREATE UNIQUE INDEX IF NOT EXISTS uniq_setting_name ON setting (name)",
]
SETTINGS_STATEMENT = """
INSERT INTO setting (name, value) VALUES (%s, %s)
ON CONFLICT (name) DO UPDATE SET value = EXCLUDED.value
"""
SETTINGS = [
    ("default_model", DEFAULT_MODEL),
    ("system_prompt", SYSTEM_PROMPT),
    ("reciprocal_rank_fusion_k", RECIPROCAL_RANK_FUSION_K),
    ("cosine_distance", COSINE_DISTANCE),
    ("document_chunk_size", DOCUMENT_CHUNK_SIZE),
    ("conversation_limit", CONVERSATION_LIMIT),
]
EXAMPLE_QUESTION_MIGRATION = [
    """
    CREATE TABLE IF NOT EXISTS example_question (
        id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
        question text NOT NULL
    )
    """,
    "CREATE UNIQUE INDEX IF NOT EXISTS uniq_example_question_question ON example_question (question)",
]
EXAMPLE_QUESTIONS_STATEMENT = (
    "INSERT INTO example_question (question) VALUES (%s) ON CONFLICT DO NOTHING"
)
EXAMPLE_QUESTIONS = [
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


class Migration:
    def __init__(self, db: Database):
        self.db = db

    def execute(self, migrations):
        with self.db.connection() as conn, conn.cursor() as cur:
            for migration in migrations:
                cur.execute(migration)

    def execute_many(self, statement, migrations):
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.executemany(statement, migrations)

    def run(self):
        self.execute(DOCUMENT_MIGRATIONS)
        self.execute(DESCRIPTION_MIGRATION)
        self.execute(CONVERSATION_MIGRATION)
        self.execute(MESSAGE_MIGRATION)
        self.execute(MODEL_MIGRATION)
        self.execute_many(
            MODEL_PRICINGS_STATEMENT,
            [
                (
                    model["name"],
                    model["input_price_per_million_tokens"],
                    model["output_price_per_million_tokens"],
                )
                for model in MODEL_PRICINGS
            ],
        )
        self.execute(SETTING_MIGRATION)
        self.execute_many(
            SETTINGS_STATEMENT, [(name, Jsonb(value)) for name, value in SETTINGS]
        )
        self.execute(EXAMPLE_QUESTION_MIGRATION)
        self.execute_many(
            EXAMPLE_QUESTIONS_STATEMENT, [(question,) for question in EXAMPLE_QUESTIONS]
        )


if __name__ == "__main__":
    db = Database()
    try:
        migration = Migration(db)
        migration.run()
    finally:
        db.close()
