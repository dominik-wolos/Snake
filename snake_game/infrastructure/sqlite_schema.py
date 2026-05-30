from __future__ import annotations

import sqlite3


def create_tables(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            identifier TEXT PRIMARY KEY,
            display_name TEXT NOT NULL,
            coins INTEGER NOT NULL DEFAULT 0,
            snake_color TEXT NOT NULL,
            background_color TEXT NOT NULL DEFAULT '#050607',
            language TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_identifier TEXT NOT NULL,
            score INTEGER NOT NULL,
            coins_earned INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_identifier) REFERENCES users(identifier)
        )
        """
    )
    ensure_user_columns(connection)


def ensure_user_columns(connection: sqlite3.Connection) -> None:
    columns = {
        row["name"]
        for row in connection.execute("PRAGMA table_info(users)").fetchall()
    }

    if "background_color" not in columns:
        connection.execute(
            "ALTER TABLE users ADD COLUMN background_color "
            "TEXT NOT NULL DEFAULT '#050607'"
        )
