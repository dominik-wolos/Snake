from snake_game.domain.models import ColorOption


def next_option_value(current_value: str, options: tuple[ColorOption, ...]) -> str:
    values = [option.value for option in options]

    try:
        current_index = values.index(current_value)
    except ValueError:
        current_index = 0

    return values[(current_index + 1) % len(values)]
