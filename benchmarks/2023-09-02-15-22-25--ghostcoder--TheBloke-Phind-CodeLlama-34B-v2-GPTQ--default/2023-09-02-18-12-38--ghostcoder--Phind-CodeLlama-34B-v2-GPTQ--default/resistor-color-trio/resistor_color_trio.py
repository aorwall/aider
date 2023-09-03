COLOR_CODES = {
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
def label(colors):
    value = int("".join([str(COLOR_CODES[color]) for color in colors[:2]]))
    zeros = COLOR_CODES[colors[2]] if len(colors)>=3 else 0

    if zeros == 0:
        result = f"{value} ohms"
    elif zeros >= 1 and zeros <= 6:
        result = f"{value * (10 ** zeros)} {['', 'kilo', 'mega', 'giga', 'tera', 'peta'][zeros - 1]}ohms"
    else: # this will handle zeros > 6 or any invalid values
        result = f"{value * (10 ** min(zeros, 6))} exaohms"

    return result
