def value(colors):
    # Define the numeric value for each color
    color_dict = {
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

    # Convert the colors to numbers and calculate the value
    val = int("".join([str(color_dict[c]) for c in colors[:2]]))

    return val
