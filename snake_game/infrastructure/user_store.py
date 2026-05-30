from __future__ import annotations

from pathlib import Path
from typing import Optional

from snake_game.domain.config import (
    DEFAULT_BACKGROUND_COLOR,
    DEFAULT_LANGUAGE,
    DEFAULT_SNAKE_COLOR,
)
from snake_game.domain.models import UserProfile
from snake_game.infrastructure.sqlite_connection import connect, utc_now


USER_SELECT = """
SELECT identifier, display_name, coins, snake_color, background_color, language
FROM users
WHERE identifier = ?
"""


class UserStore:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path

    def get_or_create(self, identifier: str) -> UserProfile:
        with connect(self.db_path) as connection:
            connection.execute(
                """
                INSERT OR IGNORE INTO users (
                    identifier, display_name, coins, snake_color, background_color,
                    language, created_at
                )
                VALUES (?, ?, 0, ?, ?, ?, ?)
                """,
                (
                    identifier,
                    f"Player-{identifier[:6]}",
                    DEFAULT_SNAKE_COLOR,
                    DEFAULT_BACKGROUND_COLOR,
                    DEFAULT_LANGUAGE,
                    utc_now(),
                ),
            )

        user = self.get(identifier)
        if user is None:
            raise RuntimeError("Could not load user profile.")
        return user

    def get(self, identifier: str) -> Optional[UserProfile]:
        with connect(self.db_path) as connection:
            row = connection.execute(USER_SELECT, (identifier,)).fetchone()

        if row is None:
            return None
        return self._to_profile(row)

    def set_display_name(self, identifier: str, display_name: str) -> UserProfile:
        with connect(self.db_path) as connection:
            connection.execute(
                "UPDATE users SET display_name = ? WHERE identifier = ?",
                (display_name, identifier),
            )
        return self.get_or_create(identifier)

    def update_settings(
        self,
        identifier: str,
        snake_color: Optional[str] = None,
        background_color: Optional[str] = None,
        language: Optional[str] = None,
    ) -> UserProfile:
        user = self.get_or_create(identifier)
        with connect(self.db_path) as connection:
            connection.execute(
                """
                UPDATE users
                SET snake_color = ?, background_color = ?, language = ?
                WHERE identifier = ?
                """,
                (
                    snake_color or user.snake_color,
                    background_color or user.background_color,
                    language or user.language,
                    identifier,
                ),
            )
        return self.get_or_create(identifier)

    def _to_profile(self, row) -> UserProfile:
        return UserProfile(
            identifier=row["identifier"],
            display_name=row["display_name"],
            coins=row["coins"],
            snake_color=row["snake_color"],
            background_color=row["background_color"],
            language=row["language"],
        )
