def resistor_label(colors):
    if len(colors) == 1:
        value = {"black": 0}
        tolerance = {None: 0}
    elif len(colors) == 4 or len(colors) == 5:
        value = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
        multiplier = {"black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 1e+3, "green": 1e+4, "blue": 1e+5, "violet": 1e+6, "grey": 1e+7, "white": 1e+8}
        tolerance = {"brown": 0.1, "violet": 0.05, "blue": 0.25, "green": 0.5, "gold": 1, "silver": 2, "none": None}
    else:
        raise ValueError("Invalid number of colors")

    main_value = sum([value[color] for color in colors[:-2]]) * (multiplier[colors[-2]] if len(colors) > 2 else 1)
    tolerance_value = tolerance[colors[-1] if len(colors) > 3 and colors[-1] in tolerance else "none"]
    resistance = main_value
    prefixes = ["", "kilo", "mega", "giga", "tera", "peta"]
    exp = int((len(str(resistance)) - 1) // 3)
    resistance /= (10 ** (exp * 3))
    tolerance_percentage = tolerance_value * 100 if tolerance_value is not None else ""
    return f"{resistance:.2f}{prefixes[exp]}ohms {tolerance_percentage}%"
