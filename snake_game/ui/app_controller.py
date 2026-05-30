from __future__ import annotations

import turtle

from snake_game.application.game_application import GameApplication
from snake_game.domain.models import GameStatus
from snake_game.ui.navigation import UiScreen
from snake_game.ui.turtle_renderer import TurtleRenderer


class AppController:
    def __init__(
        self,
        application: GameApplication,
        renderer: TurtleRenderer,
        window: turtle.Screen,
    ) -> None:
        self.application = application
        self.renderer = renderer
        self.window = window
        self.screen = UiScreen.MAIN_MENU

    def tick(self) -> None:
        session = self.application.session
        if session is not None and session.status == GameStatus.RUNNING:
            events = session.step()
            self.application.handle_events(events)

    def render(self) -> None:
        self.renderer.render(self.screen)

    def start_or_restart(self) -> None:
        session = self.application.session
        if session is None or session.status == GameStatus.GAME_OVER:
            self.application.start_new_game()
            self.screen = UiScreen.GAME
            self.render()

    def stop_game(self) -> None:
        self.application.stop_game()
        self.screen = UiScreen.MAIN_MENU
        self.render()

    def open_main_menu(self) -> None:
        self.application.stop_game()
        self.screen = UiScreen.MAIN_MENU
        self.render()

    def open_settings(self) -> None:
        session = self.application.session
        if session is not None and session.status == GameStatus.RUNNING:
            self.application.toggle_pause()
        self.screen = UiScreen.SETTINGS
        self.render()

    def go_back(self) -> None:
        if self.application.session is None:
            self.screen = UiScreen.MAIN_MENU
        else:
            self.screen = UiScreen.GAME
        self.render()

    def toggle_pause(self) -> None:
        if self.screen == UiScreen.SETTINGS:
            self.go_back()
            return
        self.application.toggle_pause()
        self.screen = UiScreen.GAME
        self.render()

    def open_pause_menu(self) -> None:
        session = self.application.session
        if session is None:
            self.screen = UiScreen.MAIN_MENU
        elif session.status == GameStatus.RUNNING:
            self.application.toggle_pause()
            self.screen = UiScreen.GAME
        elif session.status == GameStatus.PAUSED:
            self.screen = UiScreen.GAME
        self.render()

    def resume_game(self) -> None:
        session = self.application.session
        if session is not None and session.status == GameStatus.PAUSED:
            self.application.toggle_pause()
        self.screen = UiScreen.GAME
        self.render()

    def revive(self) -> None:
        if self.application.revive():
            self.screen = UiScreen.GAME
            self.render()
