def label(colors):
    bands = {
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

    def get_resistance_value(colors):
        value = 0
        for color in colors:
            value = value * 10 + bands[color]
        return value

    def get_ohms_value(resistance):
        if resistance >= 1 and resistance < 10:
            return f"{resistance} ohms"
        elif resistance >= 10:
            return f"{resistance // 10} kiloohms"
        else:
            return "Invalid resistance value"

    main_value = get_resistance_value(colors[:2])
    zeros = bands["grey"] * 10 ** (len(colors) - 2)
    total_resistance = main_value * zeros

    return get_ohms_value(total_resistance)
