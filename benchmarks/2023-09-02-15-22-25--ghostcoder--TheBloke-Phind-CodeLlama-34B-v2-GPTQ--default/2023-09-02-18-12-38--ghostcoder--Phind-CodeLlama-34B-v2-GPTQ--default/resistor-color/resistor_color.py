def color_code(color):
    """Return the numeric value of a color"""
    colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    if color in colors:
        return colors.index(color)
    else:
        raise ValueError("Unknown color")


def colors():
    """Return all colors that are recognized"""
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
