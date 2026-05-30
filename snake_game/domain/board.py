from __future__ import annotations

import random
from typing import Set

from snake_game.domain.models import Position


class Board:
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def is_outside(self, position: Position) -> bool:
        return (
            position.x < -self.radius
            or position.x > self.radius
            or position.y < -self.radius
            or position.y > self.radius
        )

    def random_free_position(self, blocked: Set[Position]) -> Position:
        for _ in range(1000):
            position = Position(
                random.randint(-self.radius, self.radius),
                random.randint(-self.radius, self.radius),
            )
            if position not in blocked:
                return position

        for x in range(-self.radius, self.radius + 1):
            for y in range(-self.radius, self.radius + 1):
                position = Position(x, y)
                if position not in blocked:
                    return position

        raise RuntimeError("No free board cells left.")
