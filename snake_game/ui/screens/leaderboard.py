from __future__ import annotations

from snake_game.application.game_application import GameApplication
from snake_game.ui.drawing import Drawing


def draw_leaderboard(
    application: GameApplication,
    drawing: Drawing,
    start_y: int,
) -> None:
    scores = application.top_scores()
    pen = drawing.leaderboard_pen
    pen.clear()
    pen.goto(0, start_y)
    pen.write("Leaderboard", align="center", font=("Arial", 15, "bold"))

    if not scores:
        drawing.write_lines(pen, ["No saved scores yet"], start_y - 28, 18, 12)
        return

    lines = [
        f"{index}. {entry.display_name}: {entry.score} (+{entry.coins_earned})"
        for index, entry in enumerate(scores, start=1)
    ]
    drawing.write_lines(pen, lines, start_y - 28, 18, 12)
