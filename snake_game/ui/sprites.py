from __future__ import annotations

import turtle
from typing import List, Optional

from snake_game.application.game_application import GameApplication
from snake_game.domain.config import CELL_SIZE
from snake_game.domain.models import Position


class SpriteLayer:
    def __init__(self, application: GameApplication) -> None:
        self.application = application
        self.head = self._make_turtle("square", application.user.snake_color)
        self.food = self._make_turtle("circle", "red")
        self.coin = self._make_turtle("circle", "gold")
        self.body: List[turtle.Turtle] = []

    def draw(self) -> None:
        session = self.application.session
        if session is None:
            return

        self.head.color(self.application.user.snake_color)
        self._show_at(self.head, session.snake.head)
        self._show_at(self.food, session.food)
        self._show_at(self.coin, session.bonus_coin)
        self._sync_body()

    def hide(self) -> None:
        self.head.hideturtle()
        self.food.hideturtle()
        self.coin.hideturtle()
        for segment in self.body:
            segment.hideturtle()

    def _sync_body(self) -> None:
        session = self.application.session
        if session is None:
            return

        while len(self.body) < len(session.snake.body):
            self.body.append(self._make_turtle("square", self.application.user.snake_color))

        for index, position in enumerate(session.snake.body):
            segment = self.body[index]
            segment.color(self.application.user.snake_color)
            self._show_at(segment, position)

        for index in range(len(session.snake.body), len(self.body)):
            self.body[index].hideturtle()

    def _show_at(self, turtle_obj: turtle.Turtle, position: Optional[Position]) -> None:
        if position is None:
            turtle_obj.hideturtle()
            return

        turtle_obj.goto(position.x * CELL_SIZE, position.y * CELL_SIZE)
        turtle_obj.showturtle()

    def _make_turtle(self, shape: str, color: str) -> turtle.Turtle:
        turtle_obj = turtle.Turtle()
        turtle_obj.speed(0)
        turtle_obj.shape(shape)
        turtle_obj.color(color)
        turtle_obj.penup()
        turtle_obj.hideturtle()
        return turtle_obj
