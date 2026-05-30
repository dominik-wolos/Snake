import unittest

from snake_game.domain.models import Direction, GameStatus, Position, Snake
from snake_game.domain.session import SnakeGame


class SnakeDirectionTests(unittest.TestCase):
    def test_new_game_moves_on_first_tick(self) -> None:
        game = SnakeGame()
        game.food = Position(5, 5)
        game.bonus_coin = None

        game.step()

        self.assertEqual(GameStatus.RUNNING, game.status)
        self.assertEqual(Direction.RIGHT, game.snake.direction)
        self.assertEqual(Position(1, 0), game.snake.head)

    def test_second_keypress_cannot_reverse_before_next_tick(self) -> None:
        game = SnakeGame()
        game.snake = Snake(
            head=Position(0, 0),
            body=[Position(0, -1), Position(0, -2), Position(0, -3)],
            direction=Direction.UP,
        )
        game.food = Position(5, 5)
        game.bonus_coin = None

        game.change_direction(Direction.RIGHT)
        game.change_direction(Direction.DOWN)
        events = game.step()

        self.assertEqual([], events)
        self.assertEqual(GameStatus.RUNNING, game.status)
        self.assertEqual(Direction.RIGHT, game.snake.direction)
        self.assertEqual(Position(1, 0), game.snake.head)

    def test_direct_reverse_is_ignored(self) -> None:
        game = SnakeGame()
        game.snake = Snake(
            head=Position(0, 0),
            body=[Position(0, -1), Position(0, -2)],
            direction=Direction.UP,
        )
        game.food = Position(5, 5)
        game.bonus_coin = None

        game.change_direction(Direction.DOWN)
        game.step()

        self.assertEqual(GameStatus.RUNNING, game.status)
        self.assertEqual(Direction.UP, game.snake.direction)
        self.assertEqual(Position(0, 1), game.snake.head)


if __name__ == "__main__":
    unittest.main()
