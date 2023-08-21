def resistor_label(colors):
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
        'grey': 0.05,
        'violet': 0.1,
        'blue': 0.25,
        'green': 0.5,
        'brown': 1,
        'red': 2,
        'gold': 5,
        'silver': 10
    }

    if len(colors) == 1:
        return "0 ohms"

    elif len(colors) == 4:
        value = (color_codes[colors[0]] * 10 + color_codes[colors[1]]) * (10 ** color_codes[colors[2]])
        tolerance = tolerance_codes[colors[3]]

    elif len(colors) == 5:
        value = (color_codes[colors[0]] * 100 + color_codes[colors[1]] * 10 + color_codes[colors[2]]) * (10 ** color_codes[colors[3]])
        tolerance = tolerance_codes[colors[4]]

    if value >= 10**6:
        value /= 10**6
        unit = "megaohms"
    elif value >= 10**3:
        value /= 10**3
        unit = "kiloohms"
    else:
        unit = "ohms"

    # Convert value to integer if it's an integer
    if value.is_integer():
        value = int(value)

    return f"{value} {unit} ±{tolerance}%"
