color_codes = {
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
    """Return the numeric value of a given color code.
    
    Args:
        color (str): The color code to lookup.
    
    Returns:
        int: The corresponding numeric value for the color code.
    """
    return color_codes[color]


def colors():
    """Return all possible color codes."""
    return list(color_codes.keys())
