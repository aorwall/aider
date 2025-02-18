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

PREFIXES = ["", "kilo"]

def label(colors):
    value = int(''.join([str(COLOR_CODES[c]) for c in colors[:2]]))

    multiplier = COLOR_CODES[colors[-1]]
    prefix = PREFIXES[(multiplier // 10) - 1] if (multiplier // 10) > 0 else ""

    ohmage = value * (10 ** (multiplier % 10))

    return f"{ohmage} {prefix}ohms"
