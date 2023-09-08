def value(colors):
    band_colors = {
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

    if len(colors) > 2:
        colors = colors[:2]

    return int(band_colors[colors[0]] * 10 + band_colors[colors[1]])
