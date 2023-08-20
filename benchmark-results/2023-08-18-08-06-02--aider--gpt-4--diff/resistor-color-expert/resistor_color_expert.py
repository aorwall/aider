def resistor_label(colors):
    color_values = {
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

    tolerance_values = {
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
        resistance = color_values[colors[0]]
        unit = 'ohms'
        tolerance = None
    elif len(colors) == 4:
        resistance = color_values[colors[0]] * 10 + color_values[colors[1]]
        resistance *= 10 ** color_values[colors[2]]
        tolerance = tolerance_values[colors[3]]
    elif len(colors) == 5:
        resistance = (color_values[colors[0]] * 100 +
                      color_values[colors[1]] * 10 +
                      color_values[colors[2]])
        resistance *= 10 ** color_values[colors[3]]
        tolerance = tolerance_values[colors[4]]

    if resistance >= 10**6:
        resistance /= 10**6
        unit = 'megaohms'
    elif resistance >= 10**3:
        resistance /= 10**3
        unit = 'kiloohms'
    else:
        unit = 'ohms'

    if resistance.is_integer():
        resistance = int(resistance)
    if tolerance is not None:
        return f"{resistance} {unit} ±{tolerance}%"
    else:
        return f"{resistance} {unit}"
