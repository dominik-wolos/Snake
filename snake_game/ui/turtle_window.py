from __future__ import annotations

import turtle

from snake_game.domain.config import WINDOW_SIZE


def configure_window(window: turtle.Screen, title: str) -> None:
    window.title(title)
    window.bgcolor("black")
    window.setup(width=WINDOW_SIZE, height=WINDOW_SIZE)
    window.screensize(canvwidth=WINDOW_SIZE, canvheight=WINDOW_SIZE, bg="black")
    window.setworldcoordinates(
        -WINDOW_SIZE / 2,
        -WINDOW_SIZE / 2,
        WINDOW_SIZE / 2,
        WINDOW_SIZE / 2,
    )
    window.tracer(0)

    canvas = window.getcanvas()
    root = canvas.winfo_toplevel()
    root.title(title)
    root.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}")
    root.resizable(False, False)
    canvas.configure(
        width=WINDOW_SIZE,
        height=WINDOW_SIZE,
        bg="black",
        highlightthickness=0,
    )
    canvas.xview_moveto(0)
    canvas.yview_moveto(0)
