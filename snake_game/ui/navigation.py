from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class UiScreen(Enum):
    MAIN_MENU = "main_menu"
    GAME = "game"
    SETTINGS = "settings"


@dataclass(frozen=True)
class UiButton:
    action: str
    label: str
    x: float
    y: float
    width: float
    height: float

    def contains(self, point_x: float, point_y: float) -> bool:
        half_width = self.width / 2
        half_height = self.height / 2
        return (
            self.x - half_width <= point_x <= self.x + half_width
            and self.y - half_height <= point_y <= self.y + half_height
        )
