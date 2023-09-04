def value(colors):
    # Create a dictionary to map color names to numbers
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

    # Initialize the total value to 0
    total_value = 0

    # Iterate over the list of colors
    for color in colors:
        # Get the corresponding numerical value for the current color
        color_value = color_map[color]

        # Add the current color value to the total value
        total_value *= 10
        total_value += color_value

    # Return the final total value
    return total_value
