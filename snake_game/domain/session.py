from __future__ import annotations

from typing import List, Optional

from snake_game.domain.board import Board
from snake_game.domain.config import (
    BOARD_RADIUS,
    BONUS_COIN_CHANCE,
    BONUS_COIN_REWARD,
    FOOD_COIN_REWARD,
    FOOD_SCORE,
)
from snake_game.domain.models import Direction, GameEvent, GameStatus, Position, Snake
from snake_game.domain.spawn import blocked_positions, should_spawn_bonus_coin


class SnakeGame:
    def __init__(self, board_radius: int = BOARD_RADIUS) -> None:
        self.board = Board(board_radius)
        self.score = 0
        self.coins_earned = 0
        self.status = GameStatus.RUNNING
        self.snake = Snake(Position(0, 0), [], Direction.RIGHT)
        self.food: Optional[Position] = None
        self.bonus_coin: Optional[Position] = None
        self.food = self._random_free_position()

    def change_direction(self, direction: Direction) -> None:
        if self.status != GameStatus.RUNNING:
            return
        if self.snake.direction != Direction.STOP and direction.is_opposite(self.snake.direction):
            return
        self.snake.queued_direction = direction

    def toggle_pause(self) -> None:
        if self.status == GameStatus.RUNNING:
            self.status = GameStatus.PAUSED
        elif self.status == GameStatus.PAUSED:
            self.status = GameStatus.RUNNING

    def revive(self) -> None:
        if self.status != GameStatus.GAME_OVER:
            return
        self.snake = Snake(Position(0, 0), [], Direction.RIGHT)
        self.status = GameStatus.RUNNING

    def step(self) -> List[GameEvent]:
        self.snake.apply_queued_direction()

        if self.status != GameStatus.RUNNING or self.snake.direction == Direction.STOP:
            return []

        new_head = self.snake.head.move(self.snake.direction)

        if self.board.is_outside(new_head):
            self.status = GameStatus.GAME_OVER
            return [GameEvent("game_over")]

        will_eat = new_head == self.food
        body_collision_zone = self.snake.body if will_eat else self.snake.body[:-1]

        if new_head in body_collision_zone:
            self.status = GameStatus.GAME_OVER
            return [GameEvent("game_over")]

        old_head = self.snake.head
        new_body = [old_head] + self.snake.body

        if not will_eat:
            new_body = new_body[:-1]

        self.snake.head = new_head
        self.snake.body = new_body

        events: List[GameEvent] = []

        if will_eat:
            self.score += FOOD_SCORE
            self.coins_earned += FOOD_COIN_REWARD
            events.append(GameEvent("food_eaten", FOOD_SCORE, FOOD_COIN_REWARD))
            self.food = self._random_free_position()
            self._maybe_spawn_bonus_coin()

        if self.bonus_coin == new_head:
            self.bonus_coin = None
            self.coins_earned += BONUS_COIN_REWARD
            events.append(GameEvent("coin_collected", 0, BONUS_COIN_REWARD))

        return events

    def _maybe_spawn_bonus_coin(self) -> None:
        if self.bonus_coin is None and should_spawn_bonus_coin(BONUS_COIN_CHANCE):
            self.bonus_coin = self._random_free_position()

    def _random_free_position(self) -> Position:
        return self.board.random_free_position(
            blocked_positions(self.snake, self.food, self.bonus_coin)
        )
