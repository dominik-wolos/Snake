from __future__ import annotations

from typing import Iterable, List, Optional

from snake_game.application.ports import GameRepository
from snake_game.application.preferences import next_option_value
from snake_game.domain.config import BACKGROUND_OPTIONS, COLOR_OPTIONS, REVIVE_COST
from snake_game.domain.models import Direction, GameEvent, GameStatus, ScoreEntry, UserProfile
from snake_game.domain.session import SnakeGame


class GameApplication:
    def __init__(self, repository: GameRepository, player_identifier: str) -> None:
        self.repository = repository
        self.user = repository.get_or_create_user(player_identifier)
        self.session: Optional[SnakeGame] = None
        self.score_saved = True

    def start_new_game(self) -> None:
        self.finalize_current_game()
        self.session = SnakeGame()
        self.score_saved = False

    def stop_game(self) -> None:
        self.finalize_current_game()
        self.session = None

    def change_direction(self, direction: Direction) -> None:
        if self.session is not None:
            self.session.change_direction(direction)

    def toggle_pause(self) -> None:
        if self.session is not None:
            self.session.toggle_pause()

    def handle_events(self, events: Iterable[GameEvent]) -> None:
        for event in events:
            if event.coin_delta > 0:
                self.user = self.repository.add_coins(self.user.identifier, event.coin_delta)

    def revive(self) -> bool:
        if self.session is None or self.session.status != GameStatus.GAME_OVER:
            return False

        if not self.repository.spend_coins(self.user.identifier, REVIVE_COST):
            return False

        self.user = self.repository.get_or_create_user(self.user.identifier)
        self.session.revive()
        return True

    def finalize_current_game(self) -> None:
        if self.session is None or self.score_saved or self.session.score <= 0:
            return

        self.repository.save_score(
            self.user.identifier,
            self.session.score,
            self.session.coins_earned,
        )
        self.score_saved = True

    def choose_next_color(self) -> None:
        self.user = self.repository.update_settings(
            self.user.identifier,
            snake_color=next_option_value(self.user.snake_color, COLOR_OPTIONS),
        )

    def set_snake_color(self, color: str) -> None:
        self.user = self.repository.update_settings(
            self.user.identifier,
            snake_color=color,
        )

    def choose_next_background(self) -> None:
        self.user = self.repository.update_settings(
            self.user.identifier,
            background_color=next_option_value(
                self.user.background_color,
                BACKGROUND_OPTIONS,
            ),
        )

    def set_background_color(self, color: str) -> None:
        self.user = self.repository.update_settings(
            self.user.identifier,
            background_color=color,
        )

    def set_display_name(self, display_name: str) -> None:
        clean_name = display_name.strip()
        if clean_name:
            self.user = self.repository.set_display_name(self.user.identifier, clean_name[:24])

    def top_scores(self, limit: int = 5) -> List[ScoreEntry]:
        return self.repository.top_scores(limit)
