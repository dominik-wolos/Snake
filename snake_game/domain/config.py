from snake_game.domain.models import ColorOption


BOARD_RADIUS = 14
CELL_SIZE = 20
WINDOW_SIZE = 600
FOOD_SCORE = 10
FOOD_COIN_REWARD = 1
BONUS_COIN_REWARD = 5
BONUS_COIN_CHANCE = 0.3
REVIVE_COST = 10
TICK_MS = 110
DEFAULT_LANGUAGE = "en"

COLOR_OPTIONS = (
    ColorOption("Green", "green"),
    ColorOption("Blue", "dodger blue"),
    ColorOption("Yellow", "gold"),
    ColorOption("Purple", "medium purple"),
    ColorOption("White", "white"),
)

DEFAULT_SNAKE_COLOR = COLOR_OPTIONS[0].value

BACKGROUND_OPTIONS = (
    ColorOption("Charcoal", "#050607"),
    ColorOption("Graphite", "#111315"),
    ColorOption("Slate", "#171b20"),
    ColorOption("Blue Gray", "#121a24"),
    ColorOption("Muted Plum", "#1b151d"),
)

DEFAULT_BACKGROUND_COLOR = BACKGROUND_OPTIONS[0].value
