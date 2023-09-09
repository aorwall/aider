COLOR_CODE = {
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

METRIC_PREFIXES = {
    0: '',
    1: 'kilo',
    2: 'mega',
    3: 'giga',
    4: 'tera',
    5: 'peta',
    6: 'exa',
    7: 'zetta',
    8: 'yotta',
    9: 'bronto'    
}

def label(colors):
    first_digit = COLOR_CODE[colors[0]]
    second_digit = COLOR_CODE[colors[1]]
    exponent = COLOR_CODE[colors[2]]
    
    value = int(str(first_digit) + str(second_digit))
    if exponent > len(METRIC_PREFIXES) - 1:
        prefix = 'bronto'
    else:
        prefix = METRIC_PREFIXES[exponent]
    
    if prefix:
        return f"{value} {prefix}ohms"
    else:
        return f"{value} ohms"
