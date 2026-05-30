from __future__ import annotations

import turtle
from typing import List

from snake_game.ui.navigation import UiButton


class Drawing:
    def __init__(self, buttons: List[UiButton]) -> None:
        self.buttons = buttons
        self.hud_pen = self.make_pen()
        self.overlay_pen = self.make_pen()
        self.leaderboard_pen = self.make_pen()
        self.button_pen = self.make_pen()

    def clear_all(self) -> None:
        self.hud_pen.clear()
        self.overlay_pen.clear()
        self.leaderboard_pen.clear()
        self.button_pen.clear()

    def write_lines(
        self,
        pen: turtle.Turtle,
        lines: List[str],
        start_y: int,
        gap: int,
        font_size: int,
    ) -> None:
        for index, line in enumerate(lines):
            pen.goto(0, start_y - index * gap)
            pen.write(line, align="center", font=("Arial", font_size, "normal"))

    def center_message(self, message: str, y: int = 20) -> None:
        self.overlay_pen.goto(0, y)
        self.overlay_pen.write(
            message,
            align="center",
            font=("Arial", 24, "bold"),
        )

    def draw_button(
        self,
        label: str,
        action: str,
        x: float,
        y: float,
        width: float,
        height: float,
        font_size: int = 12,
    ) -> None:
        self.buttons.append(UiButton(action, label, x, y, width, height))

        left = x - width / 2
        bottom = y - height / 2
        self.button_pen.goto(left, bottom)
        self.button_pen.setheading(0)
        self.button_pen.color("#8a8a8a", "#222222")
        self.button_pen.begin_fill()

        for distance in (width, height, width, height):
            self.button_pen.forward(distance)
            self.button_pen.left(90)

        self.button_pen.end_fill()
        self.button_pen.goto(x, y - font_size / 2)
        self.button_pen.color("white")
        self.button_pen.write(
            label,
            align="center",
            font=("Arial", font_size, "bold"),
        )

    def make_pen(self) -> turtle.Turtle:
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        return pen
