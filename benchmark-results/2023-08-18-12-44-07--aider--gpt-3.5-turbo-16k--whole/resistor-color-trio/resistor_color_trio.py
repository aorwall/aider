def label(colors):
    color_values = {
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

    main_value = color_values[colors[0]] * 10 + color_values[colors[1]]
    zeros = "0" * color_values[colors[2]]
    magnitude = ""

    if main_value >= 1000:
        main_value /= 1000
        magnitude = "kilo"
    elif main_value >= 1000000:
        main_value /= 1000000
        magnitude = "mega"

    return f"{int(main_value)} {magnitude}ohms"
