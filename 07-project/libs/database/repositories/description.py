from libs.database.connection import Database


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
