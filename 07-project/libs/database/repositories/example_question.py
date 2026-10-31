from libs.database.connection import Database


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
