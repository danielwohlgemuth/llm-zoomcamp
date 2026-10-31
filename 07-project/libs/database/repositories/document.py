from libs.database.connection import Database
from libs.database.repositories.setting import Setting
from libs.embedder import Embedder


class Document:
    def __init__(self, db: Database, embedder: Embedder, setting: Setting):
        self.db = db
        self.embedder = embedder
        self.setting = setting

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
            AND embedding <=> %(embedding)s::vector < %(cosine_distance)s
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
        LIMIT 3
        """

        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                sql,
                {
                    "embedding": embedding.tolist(),
                    "query": query,
                    "rrf_k": self.setting.get("reciprocal_rank_fusion_k"),
                    "chunk_size": self.setting.get("document_chunk_size"),
                    "cosine_distance": self.setting.get("cosine_distance"),
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
