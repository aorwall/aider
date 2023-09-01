def value(colors):
    color_map = {
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
    resistance = 0
    for color in colors[:2]:
        resistance = resistance * 10 + color_map[color]
    return resistance