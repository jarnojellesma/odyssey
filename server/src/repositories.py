""" Contains interfaces between database tables. """
from src import models, db


class _Repository:
    def __init__(self, table):
        self.table = table


class _UserRepository(_Repository):
    @staticmethod
    def _row_to_model(row):
        return models.User(row["id"], row["email"], row["password"], row["created_at"])

    def get_by_email(self, email):
        with db.connect() as conn:
            row = conn.execute(
                f"SELECT * FROM {self.table} WHERE email = ?", (email,)
            ).fetchone()

        if not row:
            return

        return self._row_to_model(row)

    def get_by_id(self, user_id):
        with db.connect() as conn:
            row = conn.execute(
                f"SELECT * FROM {self.table} WHERE id = ?", (user_id,)
            ).fetchone()

        if not row:
            return

        return self._row_to_model(row)

    def get_all(self):
        with db.connect() as conn:
            rows = conn.execute(
                f"SELECT * FROM {self.table}"
            ).fetchall()
        return [self._row_to_model(row) for row in rows]

    def create(self, email, password_hash):
        with db.connect() as conn:
            conn.execute(
                f"INSERT INTO {self.table} (email, password) VALUES (?, ?)",
                (email, password_hash))
            conn.commit()

    def delete_by_id(self, id):
        with db.connect() as conn:
            conn.execute(
                f"DELETE FROM {self.table} WHERE id = ?", id)
            conn.commit()


users = _UserRepository("users")
