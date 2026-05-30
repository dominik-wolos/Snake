import sqlite3
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from snake_game.domain.config import DEFAULT_BACKGROUND_COLOR
from snake_game.infrastructure.database import SQLiteGameRepository


class SQLiteGameRepositoryTests(unittest.TestCase):
    def test_existing_database_gets_background_column(self) -> None:
        with TemporaryDirectory(dir="/private/tmp") as temporary_directory:
            db_path = Path(temporary_directory) / "leaderboard.db"

            with sqlite3.connect(db_path) as connection:
                connection.execute(
                    """
                    CREATE TABLE users (
                        identifier TEXT PRIMARY KEY,
                        display_name TEXT NOT NULL,
                        coins INTEGER NOT NULL DEFAULT 0,
                        snake_color TEXT NOT NULL,
                        language TEXT NOT NULL,
                        created_at TEXT NOT NULL
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE scores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_identifier TEXT NOT NULL,
                        score INTEGER NOT NULL,
                        coins_earned INTEGER NOT NULL,
                        created_at TEXT NOT NULL
                    )
                    """
                )

            repository = SQLiteGameRepository(db_path)
            user = repository.get_or_create_user("existing-player")

            self.assertEqual(DEFAULT_BACKGROUND_COLOR, user.background_color)


if __name__ == "__main__":
    unittest.main()
