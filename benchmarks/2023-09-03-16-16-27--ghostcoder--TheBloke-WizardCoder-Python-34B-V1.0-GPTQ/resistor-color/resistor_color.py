def color_code(band_color):
    """Return the numerical value of a given color."""
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
    if band_color in color_codes:
        return color_codes[band_color]
    else:
        raise ValueError("Invalid color")
def color_code(color):
    pass

def colors():
    """List all available colors."""
    return list(color_codes.keys())
