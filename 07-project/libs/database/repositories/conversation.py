from libs.database.connection import Database


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
