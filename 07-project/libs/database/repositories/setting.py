from libs.database.connection import Database


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
