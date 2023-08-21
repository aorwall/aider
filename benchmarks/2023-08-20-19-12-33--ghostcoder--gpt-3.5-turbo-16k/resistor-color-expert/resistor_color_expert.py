def resistor_label(colors):
    value_dict = {
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

    multiplier_dict = {
        "black": 1,
        "brown": 10,
        "red": 100,
        "orange": 1000,
        "yellow": 10000,
        "green": 100000,
        "blue": 1000000,
        "violet": 10000000,
        "grey": 100000000,
        "white": 1000000000
    }

    tolerance_dict = {
        "brown": 1,
        "red": 2,
        "green": 0.5,
        "blue": 0.25,
        "violet": 0.1,
        "grey": 0.05,
        "gold": 5,
        "silver": 10
    }

    if len(colors) == 1:
        value = value_dict[colors[0]]
        return f"{value} ohms"

    elif len(colors) == 4:
        value = (value_dict[colors[0]] * 10 + value_dict[colors[1]]) * multiplier_dict[colors[2]]
        tolerance = tolerance_dict[colors[3]]
        if value >= 1000 and value < 1000000:
            value = value / 1000
            return f"{value} kiloohms ±{tolerance}%"
        elif value >= 1000000:
            value = value / 1000000
            return f"{value} megaohms ±{tolerance}%"
        else:
            return f"{value} ohms ±{tolerance}%"

    elif len(colors) == 5:
        value = (value_dict[colors[0]] * 100 + value_dict[colors[1]] * 10 + value_dict[colors[2]]) * multiplier_dict[colors[3]]
        tolerance = tolerance_dict[colors[4]]
        if value >= 1000 and value < 1000000:
            value = value / 1000
            return f"{value} kiloohms ±{tolerance}%"
        elif value >= 1000000:
            value = value / 1000000
            return f"{value} megaohms ±{tolerance}%"
        else:
            return f"{value} ohms ±{tolerance}%"