def label(colors):
    resistance = 0
    for color in colors:
        if color == "black":
            resistance += 0
        elif color == "brown":
            resistance += 1
        elif color == "red":
            resistance += 2
        elif color == "orange":
            resistance += 3
        elif color == "yellow":
            resistance += 4
        elif color == "green":
            resistance += 5
        elif color == "blue":
            resistance += 6
        elif color == "violet":
            resistance += 7
        elif color == "grey":
            resistance += 8
        elif color == "white":
            resistance += 9
    return f"{resistance} ohms"
