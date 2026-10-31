from decimal import Decimal

from libs.database.connection import Database


class Model:
    def __init__(self, db: Database):
        self.db = db
        self.cache = {}

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

    def get_price(self, name: str) -> dict:
        if name in self.cache:
            self.cache[name]

        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT input_price_per_million_tokens, output_price_per_million_tokens FROM model WHERE name = (%s)",
                (name,),
            )
            if cur.rowcount:
                model = cur.fetchone()
                value = {
                    "input_price_per_million_tokens": model[0],
                    "output_price_per_million_tokens": model[1],
                }
                self.cache[name] = value
                return value

            raise ValueError(f"Price for model {name} does not exist.")

    def get_usage_by_conversation(self, conversation_id: str) -> dict:
        if not conversation_id:
            return {
                "cost": 0,
                "turns": 0,
                "input_tokens": 0,
                "output_tokens": 0,
            }

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

    def get_message_cost(self, model: str, input_tokens: int, output_tokens: int):
        price = self.get_price(model)
        return (
            input_tokens * price["input_price_per_million_tokens"] / 1_000_000
            + output_tokens * price["output_price_per_million_tokens"] / 1_000_000
        )
