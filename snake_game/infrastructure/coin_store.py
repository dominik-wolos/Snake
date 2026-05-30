from __future__ import annotations

import sqlite3
from pathlib import Path

from snake_game.infrastructure.sqlite_connection import connect
from snake_game.infrastructure.user_store import UserStore


class CoinStore:
    def __init__(self, db_path: Path, users: UserStore) -> None:
        self.db_path = db_path
        self.users = users

    def add(self, identifier: str, amount: int):
        with connect(self.db_path) as connection:
            connection.execute(
                "UPDATE users SET coins = coins + ? WHERE identifier = ?",
                (amount, identifier),
            )
        return self.users.get_or_create(identifier)

    def spend(self, identifier: str, amount: int) -> bool:
        connection = connect(self.db_path)
        try:
            return self._spend_in_transaction(connection, identifier, amount)
        finally:
            connection.close()

    def _spend_in_transaction(
        self,
        connection: sqlite3.Connection,
        identifier: str,
        amount: int,
    ) -> bool:
        connection.execute("BEGIN IMMEDIATE")
        row = connection.execute(
            "SELECT coins FROM users WHERE identifier = ?",
            (identifier,),
        ).fetchone()

        if row is None or row["coins"] < amount:
            connection.rollback()
            return False

        connection.execute(
            "UPDATE users SET coins = coins - ? WHERE identifier = ?",
            (amount, identifier),
        )
        connection.commit()
        return True
