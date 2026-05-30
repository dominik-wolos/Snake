from __future__ import annotations

import turtle

from snake_game.domain.config import COLOR_OPTIONS
from snake_game.domain.models import Direction
from snake_game.ui.app_actions import AppActions
from snake_game.ui.app_controller import AppController


def bind_inputs(
    window: turtle.Screen,
    controller: AppController,
    actions: AppActions,
) -> None:
    window.listen()
    window.onscreenclick(actions.handle_click)
    window.onkeypress(lambda: actions.set_direction(Direction.UP), "Up")
    window.onkeypress(lambda: actions.set_direction(Direction.DOWN), "Down")
    window.onkeypress(lambda: actions.set_direction(Direction.LEFT), "Left")
    window.onkeypress(lambda: actions.set_direction(Direction.RIGHT), "Right")
    window.onkeypress(controller.start_or_restart, "Return")
    window.onkeypress(controller.toggle_pause, "p")
    window.onkeypress(controller.toggle_pause, "P")
    window.onkeypress(controller.stop_game, "s")
    window.onkeypress(controller.stop_game, "S")
    window.onkeypress(controller.open_pause_menu, "Escape")
    window.onkeypress(controller.revive, "r")
    window.onkeypress(controller.revive, "R")
    window.onkeypress(actions.cycle_color, "c")
    window.onkeypress(actions.cycle_color, "C")
    window.onkeypress(actions.ask_display_name, "n")
    window.onkeypress(actions.ask_display_name, "N")
    window.onkeypress(controller.open_settings, "comma")

    for index in range(len(COLOR_OPTIONS)):
        window.onkeypress(
            lambda selected=index: actions.pick_color(selected),
            str(index + 1),
        )
