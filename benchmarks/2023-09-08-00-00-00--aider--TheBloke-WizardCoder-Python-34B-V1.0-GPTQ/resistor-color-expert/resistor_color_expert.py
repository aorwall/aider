def resistor_label(colors):
    # Define the color codes
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
        "white": 9,
    }

    # Define the tolerance codes
    tolerance_codes = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        # "gold": 5,  # Gold is not used in the 4-band resistor
        # "silver": 10,  # Silver is not used in the 4-band resistor
    }

    # Calculate the resistance value
    if len(colors) == 1:
        resistance = 0
    elif len(colors) == 4:
        value_1 = color_codes[colors[0]]
        value_2 = color_codes[colors[1]]
        multiplier = 10 ** color_codes[colors[2]]
        tolerance = tolerance_codes[colors[3]]
        resistance = (value_1 * 10 + value_2) * multiplier
    elif len(colors) == 5:
        value_1 = color_codes[colors[0]]
        value_2 = color_codes[colors[1]]
        value_3 = color_codes[colors[2]]
        multiplier = 10 ** color_codes[colors[3]]
        tolerance = tolerance_codes[colors[4]]
        resistance = (value_1 * 100 + value_2 * 10 + value_3) * multiplier
    else:
        raise ValueError("Invalid number of colors")

    # Calculate the tolerance value
    tolerance_value = resistance * tolerance / 100

    # Create the label
    if resistance >= 1000000:
        label = f"{resistance / 1000000:.2f} Megaohms ±{tolerance_value / 1000000:.2f}%"
    elif resistance >= 1000:
        label = f"{resistance / 1000:.2f} Kiloohms ±{tolerance_value / 1000:.2f}%"
    else:
        label = f"{resistance:.2f} ohms ±{tolerance_value:.2f}%"

    return label
