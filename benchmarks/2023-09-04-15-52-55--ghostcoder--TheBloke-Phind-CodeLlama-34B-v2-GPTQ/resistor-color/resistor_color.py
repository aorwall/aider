colors_map = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}


def color_code(color):
    """Return the numeric value of a color."""
    try:
        return colors_map[color]
    except KeyError:
        raise ValueError('Invalid color')


def colors():
    """List the colors and their corresponding codes."""
    return [(name, code) for name, code in colors_map.items()]
