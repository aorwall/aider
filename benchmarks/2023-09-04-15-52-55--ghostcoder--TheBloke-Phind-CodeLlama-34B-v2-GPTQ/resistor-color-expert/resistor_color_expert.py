from decimal import Decimal

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
TOLERANCE_CODES = {
    'grey': 0.05,
    'violet': 0.1,
    'blue': 0.25,
    'green': 0.5,
    'brown': 1,
    'red': 2,
    'gold': 5,
    'silver': 10
}

def resistor_label(colors):
    multipliers = {'gold': 10**4, 'silver': 10**5}
    value_codes = [COLOR_CODES[c] for c in colors[:-1]]
    value = int(''.join([str(d) for d in value_codes]))
    multiplier = 10 ** (value_codes[-1]) if len(value_codes) == 4 else 1
    tolerance = TOLERANCE_CODES[colors[-1]]
    ohms = value * multiplier
    prefixes = ['', 'kilo', 'mega']
    i = 0
    while ohms >= 1000 and i < len(prefixes)-1:
        ohms /= 1000
        i += 1
    ohms_str = '{:.1f}'.format(Decimal(ohms).quantize(Decimal('0'), rounding=ROUND_DOWN)) if not Decimal(ohms).is_integer() else str(int(ohms))
    return f"{ohms_str} {prefixes[i]}ohms ±{tolerance}%"
