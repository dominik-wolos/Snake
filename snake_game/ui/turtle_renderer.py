from __future__ import annotations

import turtle
from typing import List, Optional

from snake_game.application.game_application import GameApplication
from snake_game.ui.constants import TITLE
from snake_game.ui.drawing import Drawing
from snake_game.ui.navigation import UiButton, UiScreen
from snake_game.ui.palette import apply_background
from snake_game.ui.screens.game import draw_game
from snake_game.ui.screens.menu import draw_menu
from snake_game.ui.screens.settings import draw_settings
from snake_game.ui.sprites import SpriteLayer


class TurtleRenderer:
    def __init__(self, window: turtle.Screen, application: GameApplication) -> None:
        self.window = window
        self.application = application
        self.buttons: List[UiButton] = []
        self.drawing = Drawing(self.buttons)
        self.sprites = SpriteLayer(application)

    def render(self, screen: UiScreen) -> None:
        self.window.title(TITLE)
        self.window.getcanvas().winfo_toplevel().title(TITLE)
        apply_background(self.window, self.application.user.background_color)
        self.buttons.clear()
        self.drawing.button_pen.clear()

        if screen == UiScreen.SETTINGS:
            self.sprites.hide()
            draw_settings(self.application, self.drawing)
        elif self.application.session is None:
            self.sprites.hide()
            draw_menu(self.application, self.drawing)
        else:
            draw_game(self.application, self.drawing, self.sprites)

        self.window.update()

    def action_at(self, x: float, y: float) -> Optional[str]:
        for button in reversed(self.buttons):
            if button.contains(x, y):
                return button.action
        return None
