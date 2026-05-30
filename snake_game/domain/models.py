from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple


class Direction(Enum):
    STOP = "stop"
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

    def vector(self) -> Tuple[int, int]:
        vectors = {
            Direction.STOP: (0, 0),
            Direction.UP: (0, 1),
            Direction.DOWN: (0, -1),
            Direction.LEFT: (-1, 0),
            Direction.RIGHT: (1, 0),
        }
        return vectors[self]

    def is_opposite(self, other: "Direction") -> bool:
        return (
            (self == Direction.UP and other == Direction.DOWN)
            or (self == Direction.DOWN and other == Direction.UP)
            or (self == Direction.LEFT and other == Direction.RIGHT)
            or (self == Direction.RIGHT and other == Direction.LEFT)
        )


class GameStatus(Enum):
    RUNNING = "running"
    PAUSED = "paused"
    GAME_OVER = "game_over"


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def move(self, direction: Direction) -> "Position":
        dx, dy = direction.vector()
        return Position(self.x + dx, self.y + dy)


@dataclass
class Snake:
    head: Position
    body: List[Position]
    direction: Direction = Direction.STOP
    queued_direction: Direction = Direction.STOP

    def occupied_positions(self) -> List[Position]:
        return [self.head] + self.body

    def apply_queued_direction(self) -> None:
        if self.queued_direction == Direction.STOP:
            return
        self.direction = self.queued_direction
        self.queued_direction = Direction.STOP


@dataclass(frozen=True)
class ColorOption:
    name: str
    value: str


@dataclass
class UserProfile:
    identifier: str
    display_name: str
    coins: int
    snake_color: str
    background_color: str
    language: str


@dataclass(frozen=True)
class ScoreEntry:
    display_name: str
    score: int
    coins_earned: int
    created_at: str


@dataclass(frozen=True)
class GameEvent:
    name: str
    score_delta: int = 0
    coin_delta: int = 0
