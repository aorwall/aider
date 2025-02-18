import math

def label(colors):
    # Convert each color to its numerical equivalent
    values = [
        {'black': 0},
        {'brown': 1},
        {'red': 2},
        {'orange': 3},
        {'yellow': 4},
        {'green': 5},
        {'blue': 6},
        {'violet': 7},
        {'grey': 8},
        {'white': 9}
    ]

    resistance = 0
    multiplier = 1
    for i in range(len(colors)):
        resistance += values[i][colors[i]] * multiplier
        multiplier *= 10

    # Determine the metric prefix based on the number of leading zeros
    num_zeros = len(colors) - 2
    if num_zeros > 0:
        prefixes = ['', 'kilo', 'mega', 'giga']
        prefix = prefixes[num_zeros // 3]
    else:
        prefix = ''

    # Return the formatted label
    return f"{resistance} {prefix}ohms"
