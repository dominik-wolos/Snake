from __future__ import annotations

from snake_game.application.game_application import GameApplication
from snake_game.ui.constants import TITLE
from snake_game.ui.drawing import Drawing
from snake_game.ui.screens.leaderboard import draw_leaderboard


def draw_menu(application: GameApplication, drawing: Drawing) -> None:
    drawing.hud_pen.clear()
    drawing.overlay_pen.clear()
    drawing.leaderboard_pen.clear()

    drawing.overlay_pen.goto(0, 180)
    drawing.overlay_pen.write(
        TITLE,
        align="center",
        font=("Arial", 28, "bold"),
    )

    drawing.draw_button("Start Game", "start", 0, 125, 190, 36)
    drawing.draw_button("Settings", "settings", 0, 78, 190, 36)

    lines = [
        f"Name: {application.user.display_name}",
        f"Coins: {application.user.coins}",
        "Arrow keys move. P or Esc opens pause menu.",
    ]
    drawing.write_lines(drawing.overlay_pen, lines, 28, 20, 12)
    draw_leaderboard(application, drawing, -100)
