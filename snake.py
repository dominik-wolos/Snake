import os

os.environ.setdefault("TK_SILENCE_DEPRECATION", "1")

from snake_game.application.game_application import GameApplication
from snake_game.infrastructure.database import SQLiteGameRepository
from snake_game.infrastructure.player_identity import get_player_identifier
from snake_game.ui.turtle_app import TurtleSnakeApp


def main() -> None:
    print("Opening Snake window. Click the game window and press Enter to start.", flush=True)
    repository = SQLiteGameRepository()
    player_identifier = get_player_identifier()
    application = GameApplication(repository, player_identifier)
    TurtleSnakeApp(application).run()


if __name__ == "__main__":
    main()
