def resistor_label(colors):
    # Create dictionaries for each color code and their corresponding values
    multipliers = {"black": 1, "brown": 10, "red": 100, "orange": 10**2, "yellow": 10**3, "green": 10**4, "blue": 10**5, "violet": 10**6, "gray": 10**7, "white": 10**8, "gold": 0.1, "silver": 0.01}
    tolerances = {"none": "+/- 20%", "brown": "+/- 1%", "red": "+/- 2%", "green": "+/- 0.5%", "blue": "+/- 0.25%", "violet": "+/- 0.1%", "gold": "+/- 0.05%", "silver": "+/- 0.025%"}
    tolerance_value = {"none": "", "brown": " ±1%", "red": " ±2%", "green": " ±0.5%", "blue": " ±0.25%", "violet": " ±0.1%", "gold": " ±0.05%", "silver": " ±0.025%"}

    def get_tolerance(tolerance_code):
        if len(tolerance_code) == 2:
            return tolerances[tolerance_code]
        else:
            return ""

    def get_multiplier(multiplier_codes):
        result = 1
        for code in multiplier_codes:
            result *= multipliers[code]
        return result

    def get_value(value_codes):
        value = int("".join([str(multipliers[c]) for c in value_codes]))
        return value

    # Extract information from the bands
    tolerance_code = colors[-1][:-1]
    multiplier_codes = colors[:-1]
    value_codes = colors[:-2]

    # Calculate the resistance value and tolerance
    resistance = str(get_value(value_codes)) + (" k" if len(value_codes) > 3 else "") + " ohms"
    tolerance = tolerance_value[tolerance_code]
    multiplier = get_multiplier(multiplier_codes)

    # Return the final label
    return f"{resistance}{tolerance}"
