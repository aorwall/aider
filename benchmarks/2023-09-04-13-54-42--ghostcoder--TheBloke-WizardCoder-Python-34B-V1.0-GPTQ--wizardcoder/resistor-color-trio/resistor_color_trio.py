def label(colors):
    # Create a dictionary mapping color codes to numbers
    color_codes = {
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

    # Extract the digits from the color codes
    digits = [str(color_codes[color]) for color in colors]

    # Calculate the resistance value and the required suffix
    value = int(''.join(digits)) * pow(10, len(digits)-1)
    suffix = ''
    if value >= 1e6:
        value /= 1e6
        suffix = 'M'
    elif value >= 1e3:
        value /= 1e3
        suffix = 'k'

    # Return the formatted string
    return f"{value}{suffix} ohms"
