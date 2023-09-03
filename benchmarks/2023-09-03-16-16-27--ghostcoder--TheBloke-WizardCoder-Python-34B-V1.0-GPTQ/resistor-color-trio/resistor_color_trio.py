def label(colors):
    values = {
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

    def decode_value(band_colors):
        result = 0
        for i, color in enumerate(reversed(band_colors)):
            result += values[color] * (10 ** i)
        return result

    def format_label(main_value, zero_count):
        suffixes = ['', 'k', 'M', 'G'] # Add more here if needed (up to 'T')
        power = max(zero_count // 3 - 1, 0)
        multiplier = 10**(-power) if power > 0 else 1
        value = main_value * multiplier
        suffix = suffixes[power] + ' ohms' if power > 0 else ' ohms'
        return f"{value:.2f}{suffix}"

    first_two = colors[:2]
    last = colors[-1]
    decimal_places = last.count('0')
    main_value = decode_value(first_two)
    return format_label(main_value, decimal_places)
