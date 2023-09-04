def resistor_label(colors):
    # Create dictionaries for color codes and tolerances
    color_codes = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9
    }

    tolerance_codes = {
        'gold': 5,
        'silver': 10,
        'red': 2,
        'green': 0.5,
        'blue': 0.25,
        'violet': 0.1,
        'none': 0.05
    }

    # Extract values from colors list
    try:
        value_1 = color_codes[colors[0]]
        value_2 = color_codes[colors[1]]
    except IndexError:
        raise ValueError("Incorrect number of bands provided.")

    multiplier = int(str(value_1) + str(value_2)) * (10 ** len(colors[2]))
    tolerance = tolerance_codes[colors[-1]]

    # Calculate resistance and tolerance percentage
    resistance = round((multiplier + value_2) / 10**len(colors[2]), 1)
    tolerance_percentage = abs(round((resistance * tolerance) / resistance * 100, 2))

    # Determine suffix based on resistance value
    suffix = ''
    if resistance >= 1e+6:
        suffix = 'M ohms'
        resistance /= 1e+6
    elif resistance >= 1e+3:
        suffix = 'k ohms'
        resistance /= 1e+3
    else:
        suffix = ' ohms'

    # Return formatted string
    return f"{resistance}{suffix} ±{tolerance_percentage}%"
