def color_code(color):
    """
    Return the numerical value of the given color band.
    The color band is represented by a letter, as per the electronic color code standard.
    :param color: The color band to convert to a number.
    :return: The numerical value of the color band.
    """
    # Create a dictionary to map color codes to their corresponding numerical values
    color_map = {
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

    # Use the dictionary to lookup the numerical value of the given color band
    return color_map[color.lower()]


def colors():
    """
    Returns a list of all available color codes.
    :return: A list of all available color codes.
    """
    # Create a list of all available color codes
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
