from __future__ import annotations

import turtle

from snake_game.application.game_application import GameApplication
from snake_game.domain.config import TICK_MS
from snake_game.ui.app_actions import AppActions
from snake_game.ui.app_controller import AppController
from snake_game.ui.constants import TITLE
from snake_game.ui.input_bindings import bind_inputs
from snake_game.ui.turtle_renderer import TurtleRenderer
from snake_game.ui.turtle_window import configure_window


class TurtleSnakeApp:
    def __init__(self, application: GameApplication) -> None:
        self.window = turtle.Screen()
        configure_window(self.window, TITLE)
        self.renderer = TurtleRenderer(self.window, application)
        self.controller = AppController(application, self.renderer, self.window)
        self.actions = AppActions(self.controller)

    def run(self) -> None:
        bind_inputs(self.window, self.controller, self.actions)
        self.window.update()
        self.window.ontimer(self.render, 0)
        self.window.ontimer(self.tick, TICK_MS)
        self.window.mainloop()

    def tick(self) -> None:
        self.controller.tick()
        self.render()
        self.window.ontimer(self.tick, TICK_MS)

    def render(self) -> None:
        self.controller.render()
