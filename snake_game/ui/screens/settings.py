from __future__ import annotations

from snake_game.application.game_application import GameApplication
from snake_game.domain.config import BACKGROUND_OPTIONS, COLOR_OPTIONS
from snake_game.ui.drawing import Drawing
from snake_game.ui.palette import background_name, snake_color_name


def draw_settings(application: GameApplication, drawing: Drawing) -> None:
    drawing.hud_pen.clear()
    drawing.overlay_pen.clear()
    drawing.leaderboard_pen.clear()
    _draw_title_and_summary(application, drawing)
    _draw_color_controls(drawing)
    _draw_background_controls(drawing)
    drawing.draw_button("Back", "back", -65, -205, 110, 34)
    drawing.draw_button("Main Menu", "main_menu", 70, -205, 130, 34)


def _draw_title_and_summary(application: GameApplication, drawing: Drawing) -> None:
    drawing.overlay_pen.goto(0, 215)
    drawing.overlay_pen.write("Settings", align="center", font=("Arial", 26, "bold"))

    lines = [
        f"Name: {application.user.display_name}",
        f"Coins: {application.user.coins}",
        f"Snake color: {snake_color_name(application.user.snake_color)}",
        f"Background: {background_name(application.user.background_color)}",
    ]
    drawing.write_lines(drawing.overlay_pen, lines, 202, 17, 11)

    if application.session is not None:
        drawing.overlay_pen.goto(0, -158)
        drawing.overlay_pen.write(
            "Current game is paused while settings are open.",
            align="center",
            font=("Arial", 11, "normal"),
        )


def _draw_color_controls(drawing: Drawing) -> None:
    drawing.draw_button("Change Name", "change_name", 0, 118, 190, 30)
    drawing.draw_button("Next Color", "cycle_color", 0, 78, 190, 30)
    drawing.overlay_pen.goto(0, 42)
    drawing.overlay_pen.write("Color Options", align="center", font=("Arial", 12, "bold"))

    for index, option in enumerate(COLOR_OPTIONS):
        x = -160 + index * 80
        drawing.draw_button(option.name, f"color:{index}", x, 6, 68, 28, 10)


def _draw_background_controls(drawing: Drawing) -> None:
    drawing.draw_button("Next Background", "cycle_background", 0, -38, 190, 30)
    drawing.overlay_pen.goto(0, -74)
    drawing.overlay_pen.write(
        "Background Options",
        align="center",
        font=("Arial", 12, "bold"),
    )

    for index, option in enumerate(BACKGROUND_OPTIONS):
        x = -160 + index * 80
        drawing.draw_button(option.name, f"background:{index}", x, -110, 74, 28, 9)
