def label(colors):
    # Initialize the resistance value to 0
    resistance = 0

    # Iterate through the colors and calculate the resistance value
    for color in colors:
        # Convert the color to a number
        number = color_to_number(color)

        # Add the number to the resistance value
        resistance += number

    # Calculate the number of zeros to add to the resistance value
    zeros = len(colors) - 1

    # Add the zeros to the resistance value
    resistance *= 10 ** zeros

    # Return the resistance value as a string with the unit "ohms"
    return f"{resistance} ohms"

def color_to_number(color):
    # Convert the color to a number
    if color == "black":
        return 0
    elif color == "brown":
        return 1
    elif color == "red":
        return 2
    elif color == "orange":
        return 3
    elif color == "yellow":
        return 4
    elif color == "green":
        return 5
    elif color == "blue":
        return 6
    elif color == "violet":
        return 7
    elif color == "grey":
        return 8
    elif color == "white":
        return 9
    else:
        raise ValueError("Invalid color")
