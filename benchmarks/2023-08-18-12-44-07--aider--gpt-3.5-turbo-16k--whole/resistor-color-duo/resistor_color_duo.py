def value(colors):
    color_values = {
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

    # Get the first two colors from the input
    first_color = colors[0]
    second_color = colors[1]

    # Get the corresponding values for the first two colors
    first_value = color_values[first_color]
    second_value = color_values[second_color]

    # Combine the values to get the final result
    result = int(str(first_value) + str(second_value))

    return result
