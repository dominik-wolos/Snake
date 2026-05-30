from __future__ import annotations

from snake_game.domain.config import BACKGROUND_OPTIONS, COLOR_OPTIONS
from snake_game.domain.models import Direction
from snake_game.ui.app_controller import AppController
from snake_game.ui.constants import TITLE
from snake_game.ui.navigation import UiScreen


class AppActions:
    def __init__(self, controller: AppController) -> None:
        self.controller = controller

    def cycle_color(self) -> None:
        self.controller.application.choose_next_color()
        self.controller.render()

    def pick_color(self, index: int) -> None:
        if index < len(COLOR_OPTIONS):
            self.controller.application.set_snake_color(COLOR_OPTIONS[index].value)
            self.controller.render()

    def cycle_background(self) -> None:
        self.controller.application.choose_next_background()
        self.controller.render()

    def pick_background(self, index: int) -> None:
        if index < len(BACKGROUND_OPTIONS):
            self.controller.application.set_background_color(
                BACKGROUND_OPTIONS[index].value
            )
            self.controller.render()

    def ask_display_name(self) -> None:
        name = self.controller.window.textinput(TITLE, "Display name")
        if name:
            self.controller.application.set_display_name(name)
            self.controller.render()

    def set_direction(self, direction: Direction) -> None:
        if self.controller.screen == UiScreen.SETTINGS:
            return
        self.controller.application.change_direction(direction)

    def handle_click(self, x: float, y: float) -> None:
        action = self.controller.renderer.action_at(x, y)
        if action is None:
            return

        if action == "start":
            self.controller.start_or_restart()
        elif action == "main_menu":
            self.controller.open_main_menu()
        elif action == "settings":
            self.controller.open_settings()
        elif action == "back":
            self.controller.go_back()
        elif action == "resume":
            self.controller.resume_game()
        elif action == "revive":
            self.controller.revive()
        elif action == "cycle_color":
            self.cycle_color()
        elif action == "cycle_background":
            self.cycle_background()
        elif action == "change_name":
            self.ask_display_name()
        elif action.startswith("color:"):
            self.pick_color(int(action.split(":", 1)[1]))
        elif action.startswith("background:"):
            self.pick_background(int(action.split(":", 1)[1]))
