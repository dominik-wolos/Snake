# Snake

Python turtle version of Snake.

## Run

```bash
uv sync
uv run python snake.py
```

The terminal stays busy because the Turtle window runs an event loop.
Click the game window, then press `Enter` to start.
Close the window to return to the terminal prompt.

The project uses a local `.venv` managed by `uv`.
Runtime modules are from the Python standard library, so there are no external package dependencies.
The project is pinned to Python 3.12 because the newer Homebrew Python builds on this machine do not include Tk support required by Turtle.

## Controls

- Click `Start Game` or press `Enter` to start.
- Arrow keys move the snake.
- `P` pauses or resumes and shows the pause view.
- `Esc` opens the pause view.
- The pause view contains `Resume`, `Settings`, and `Main Menu`.
- `Settings` changes name, snake color, or background color.
- On game over, click `Revive` or press `R` if the player has enough coins.
- `C` cycles snake color, `1` to `5` picks a snake color directly.
- `N` changes the displayed player name.

## Data

The game uses SQLite from the Python standard library.

- `leaderboard.db` stores users, scores, coins, selected snake color, and selected background.
- The player is identified by a hashed device identifier.
- If a hardware identifier cannot be read, the game creates `.player_id` and uses that.
- IP address is not used.

## Code Layout

- `snake.py` starts the app.
- `snake_game/domain` contains game rules and domain models.
- `snake_game/application` connects the game rules with saved user state and repository ports.
- `snake_game/infrastructure` contains SQLite schema, stores, repository facade, and player identification.
- `snake_game/ui/turtle_app.py` owns the Turtle app shell.
- `snake_game/ui/app_controller.py` handles screen flow and game lifecycle actions.
- `snake_game/ui/app_actions.py` handles clickable and keyboard-triggered UI actions.
- `snake_game/ui/input_bindings.py` wires keyboard and mouse input.
- `snake_game/ui/navigation.py` contains UI screen and button models.
- `snake_game/ui/screens` contains screen-specific drawing code.
- `snake_game/ui/turtle_renderer.py` dispatches rendering to screen modules.
- `snake_game/ui/turtle_window.py` configures the Turtle window.

## Tests

```bash
uv run python -m unittest discover -s tests
```

## Notes

Food gives score and coins.
Bonus coins can appear on the board.
Revive costs coins and keeps the current score.
