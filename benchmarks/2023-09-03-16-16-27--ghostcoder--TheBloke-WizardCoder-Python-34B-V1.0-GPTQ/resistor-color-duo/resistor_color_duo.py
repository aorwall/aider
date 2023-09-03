def value(colors):
    # Create a dictionary mapping color codes to numbers
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

    # Convert the list of colors into a string with only the first two elements
    code = ''.join([str(color_codes[c]) for c in colors[:2]])

    # Return the corresponding numerical value
    return int(code)
