from __future__ import annotations

from pathlib import Path
from typing import List, Optional

from snake_game.domain.models import ScoreEntry, UserProfile
from snake_game.infrastructure.coin_store import CoinStore
from snake_game.infrastructure.score_store import ScoreStore
from snake_game.infrastructure.sqlite_connection import DEFAULT_DB_PATH, connect
from snake_game.infrastructure.sqlite_schema import create_tables
from snake_game.infrastructure.user_store import UserStore


class SQLiteGameRepository:
    def __init__(self, db_path: Optional[Path] = None) -> None:
        self.db_path = db_path or DEFAULT_DB_PATH
        self._create_tables()
        self.users = UserStore(self.db_path)
        self.coins = CoinStore(self.db_path, self.users)
        self.scores = ScoreStore(self.db_path)

    def get_or_create_user(self, identifier: str) -> UserProfile:
        return self.users.get_or_create(identifier)

    def get_user(self, identifier: str) -> Optional[UserProfile]:
        return self.users.get(identifier)

    def set_display_name(self, identifier: str, display_name: str) -> UserProfile:
        return self.users.set_display_name(identifier, display_name)

    def update_settings(
        self,
        identifier: str,
        snake_color: Optional[str] = None,
        background_color: Optional[str] = None,
        language: Optional[str] = None,
    ) -> UserProfile:
        return self.users.update_settings(
            identifier,
            snake_color=snake_color,
            background_color=background_color,
            language=language,
        )

    def add_coins(self, identifier: str, amount: int) -> UserProfile:
        return self.coins.add(identifier, amount)

    def spend_coins(self, identifier: str, amount: int) -> bool:
        return self.coins.spend(identifier, amount)

    def save_score(self, identifier: str, score: int, coins_earned: int) -> None:
        self.scores.save(identifier, score, coins_earned)

    def top_scores(self, limit: int = 5) -> List[ScoreEntry]:
        return self.scores.top(limit)

    def _create_tables(self) -> None:
        with connect(self.db_path) as connection:
            create_tables(connection)
