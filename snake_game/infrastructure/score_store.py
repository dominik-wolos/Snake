from __future__ import annotations

from pathlib import Path
from typing import List

from snake_game.domain.models import ScoreEntry
from snake_game.infrastructure.sqlite_connection import connect, utc_now


class ScoreStore:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path

    def save(self, identifier: str, score: int, coins_earned: int) -> None:
        with connect(self.db_path) as connection:
            connection.execute(
                """
                INSERT INTO scores (user_identifier, score, coins_earned, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (identifier, score, coins_earned, utc_now()),
            )

    def top(self, limit: int = 5) -> List[ScoreEntry]:
        with connect(self.db_path) as connection:
            rows = connection.execute(
                """
                SELECT users.display_name, scores.score, scores.coins_earned,
                    scores.created_at
                FROM scores
                JOIN users ON users.identifier = scores.user_identifier
                ORDER BY scores.score DESC, scores.created_at ASC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()

        return [
            ScoreEntry(
                display_name=row["display_name"],
                score=row["score"],
                coins_earned=row["coins_earned"],
                created_at=row["created_at"],
            )
            for row in rows
        ]
