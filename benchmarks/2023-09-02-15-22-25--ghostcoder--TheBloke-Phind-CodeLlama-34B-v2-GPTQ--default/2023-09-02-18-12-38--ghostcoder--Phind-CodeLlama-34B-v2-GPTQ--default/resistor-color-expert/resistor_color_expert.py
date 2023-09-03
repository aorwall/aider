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
        'white': 9,
        'gold': 0.1,
        'silver': 0.01
    }

    multiplier_codes = {
        1: 100,
        10: 1000,
        100: 10000,
        1000: 100000,
        10000: 1000000,
        100000: 10000000,
        1000000: 100000000,
        100000000: 10**9,
        0.1: 10**-2,
        0.01: 10**-3
    }

    value_1 = color_codes[colors[0]] * 10
    value_2 = color_codes[colors[1]]
    multiplier = multiplier_codes[value_2] if len(colors) == 4 else multiplier_codes[color_codes[colors[2]]]
    tolerance = color_codes[colors[-1]] if len(colors) == 5 else None

    resistance = (value_1 + value_2) / multiplier

    unit = "ohms"
    if resistance >= 1000:
        resistance /= 1000
        unit = "kiloohms"
    elif resistance >= 1000000:
        resistance /= 1000000
        unit = "megaohms"

    label = f"{resistance} {unit}"
    if tolerance is not None:
        label += f" ±{tolerance}%"

    return label
