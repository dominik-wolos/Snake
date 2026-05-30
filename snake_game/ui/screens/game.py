from __future__ import annotations

from snake_game.application.game_application import GameApplication
from snake_game.domain.config import REVIVE_COST
from snake_game.domain.models import GameStatus
from snake_game.ui.drawing import Drawing
from snake_game.ui.screens.leaderboard import draw_leaderboard
from snake_game.ui.sprites import SpriteLayer


def draw_game(application: GameApplication, drawing: Drawing, sprites: SpriteLayer) -> None:
    session = application.session
    if session is None:
        return

    drawing.overlay_pen.clear()
    drawing.leaderboard_pen.clear()
    sprites.draw()
    _draw_hud(application, drawing)

    if session.status == GameStatus.PAUSED:
        draw_pause_menu(drawing)
    elif session.status == GameStatus.GAME_OVER:
        draw_game_over(application, drawing)


def draw_pause_menu(drawing: Drawing) -> None:
    drawing.center_message("Paused", y=85)
    drawing.draw_button("Resume", "resume", 0, 35, 170, 34)
    drawing.draw_button("Settings", "settings", 0, -10, 170, 34)
    drawing.draw_button("Main Menu", "main_menu", 0, -55, 170, 34)


def draw_game_over(application: GameApplication, drawing: Drawing) -> None:
    drawing.center_message("Game over", y=95)

    if application.user.coins >= REVIVE_COST:
        drawing.draw_button(f"Revive ({REVIVE_COST} coins)", "revive", 0, 35, 190, 34)
    else:
        drawing.overlay_pen.goto(0, 35)
        drawing.overlay_pen.write(
            f"Need {REVIVE_COST} coins to revive",
            align="center",
            font=("Arial", 13, "normal"),
        )

    drawing.draw_button("Save and Start Again", "start", 0, -15, 220, 34)
    drawing.draw_button("Main Menu", "main_menu", 0, -65, 160, 34)
    draw_leaderboard(application, drawing, -135)


def _draw_hud(application: GameApplication, drawing: Drawing) -> None:
    session = application.session
    if session is None:
        return

    drawing.hud_pen.clear()
    drawing.hud_pen.goto(0, 268)
    drawing.hud_pen.write(
        "   ".join(
            [
                f"Score: {session.score}",
                f"Coins: {application.user.coins}",
                f"Earned: {session.coins_earned}",
            ]
        ),
        align="center",
        font=("Arial", 13, "normal"),
    )
