from decimal import Decimal

from libs.database.connection import Database


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
