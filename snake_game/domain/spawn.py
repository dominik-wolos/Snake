from __future__ import annotations

import random
from typing import Optional, Set

from snake_game.domain.models import Position, Snake


def blocked_positions(
    snake: Snake,
    food: Optional[Position],
    bonus_coin: Optional[Position],
) -> Set[Position]:
    blocked = set(snake.occupied_positions())
    if food is not None:
        blocked.add(food)
    if bonus_coin is not None:
        blocked.add(bonus_coin)
    return blocked


def should_spawn_bonus_coin(chance: float) -> bool:
    return random.random() < chance
