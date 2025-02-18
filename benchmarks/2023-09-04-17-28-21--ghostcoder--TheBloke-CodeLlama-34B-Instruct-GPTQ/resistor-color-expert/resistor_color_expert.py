def resistor_label(colors):
    # Create a dictionary to map the colors to their numerical values
    color_map = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'gray': 8,
        'white': 9
    }

    # Initialize variables to store the numerical values of each color
    val1 = None
    val2 = None
    val3 = None
    multiplier = None
    tolerance = None

    # Iterate through the list of colors and assign them to the appropriate variable
    for i, color in enumerate(colors):
        if i == 0:
            val1 = color_map[color]
        elif i == 1:
            val2 = color_map[color]
        elif i == 2:
            val3 = color_map[color]
        elif i == 3:
            multiplier = color_map[color]
        else:
            tolerance = color_map[color]

    # Calculate the resistance value based on the values of the first three colors
    resistance = int((val1 * 10 + val2) * 10 ** multiplier)

    # Determine the tolerance percentage based on the value of the fourth color
    if tolerance == 0:
        tolerance_percentage = 0.05
    elif tolerance == 1:
        tolerance_percentage = 0.1
    elif tolerance == 2:
        tolerance_percentage = 0.25
    elif tolerance == 3:
        tolerance_percentage = 0.5
    elif tolerance == 4:
        tolerance_percentage = 1
    elif tolerance == 5:
        tolerance_percentage = 2
    elif tolerance == 6:
        tolerance_percentage = 5
    else:
        tolerance_percentage = 10

    # Format the output string
    if resistance >= 1000000:
        resistance /= 1000000
        unit = 'megaohms'
    elif resistance >= 1000:
        resistance /= 1000
        unit = 'kiloohms'
    else:
        unit = 'ohms'

    output = f'{resistance} {unit} ±{tolerance_percentage}%'

    return output
