from enum import Enum

from libs.database.connection import Database


class MessageStatus(Enum):
    InProgress = "In Progress"
    Completed = "Completed"
    Failed = "Failed"


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
                "   COALESCE(SUM(m.input_tokens), 0), "
                "   COALESCE(SUM(m.output_tokens), 0) "
                "FROM message AS m "
                "   JOIN model AS mo ON (mo.name = m.model)"
                "WHERE m.conversation_id = %s",
                (conversation_id,),
            )
            row = cur.fetchone()
            return {
                "cost": row[0],
                "turns": row[1],
                "input_tokens": row[2],
                "output_tokens": row[3],
            }
