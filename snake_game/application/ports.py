from __future__ import annotations

from typing import List, Optional, Protocol

from snake_game.domain.models import ScoreEntry, UserProfile


class GameRepository(Protocol):
    def get_or_create_user(self, identifier: str) -> UserProfile:
        ...

    def get_user(self, identifier: str) -> Optional[UserProfile]:
        ...

    def set_display_name(self, identifier: str, display_name: str) -> UserProfile:
        ...

    def update_settings(
        self,
        identifier: str,
        snake_color: Optional[str] = None,
        background_color: Optional[str] = None,
        language: Optional[str] = None,
    ) -> UserProfile:
        ...

    def add_coins(self, identifier: str, amount: int) -> UserProfile:
        ...

    def spend_coins(self, identifier: str, amount: int) -> bool:
        ...

    def save_score(self, identifier: str, score: int, coins_earned: int) -> None:
        ...

    def top_scores(self, limit: int = 5) -> List[ScoreEntry]:
        ...
