from __future__ import annotations

import turtle

from snake_game.domain.config import BACKGROUND_OPTIONS, COLOR_OPTIONS


def option_name(value: str, options: tuple) -> str:
    for option in options:
        if option.value == value:
            return option.name
    return value


def snake_color_name(value: str) -> str:
    return option_name(value, COLOR_OPTIONS)


def background_name(value: str) -> str:
    return option_name(value, BACKGROUND_OPTIONS)


def apply_background(window: turtle.Screen, color: str) -> None:
    window.bgcolor(color)
    window.screensize(bg=color)
    window.getcanvas().configure(bg=color)
