def resistor_label(colors):
    # Check the number of colors
    num_colors = len(colors)
    
    # Define the color code dictionary
    color_codes = {
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
    
    # Calculate the resistance value based on the number of colors
    if num_colors == 1:
        resistance = color_codes[colors[0]]
    elif num_colors == 4:
        resistance = (color_codes[colors[0]] * 10 + color_codes[colors[1]]) * (10 ** color_codes[colors[2]])
    elif num_colors == 5:
        resistance = (color_codes[colors[0]] * 100 + color_codes[colors[1]] * 10 + color_codes[colors[2]]) * (10 ** color_codes[colors[3]])
    else:
        raise ValueError("Invalid number of colors")
    
    # Check if the resistance is in kiloohms or megaohms
    if resistance >= 1000000:
        resistance_label = f"{resistance / 1000000:.2f} megaohms"
    elif resistance >= 1000:
        resistance_label = f"{resistance / 1000:.2f} kiloohms"
    else:
        resistance_label = f"{resistance} ohms"
    
    # Check the tolerance color and calculate the tolerance value
    tolerance_colors = ["grey", "violet", "blue", "green", "brown", "red", "gold", "silver"]
    tolerance_values = [0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10]
    
    if num_colors == 4:
        tolerance_color = colors[3]
    elif num_colors == 5:
        tolerance_color = colors[4]
    else:
        tolerance_color = None
    
    if tolerance_color:
        tolerance = tolerance_values[tolerance_colors.index(tolerance_color)]
        tolerance_label = f"±{tolerance}%"
    else:
        tolerance_label = ""
    
    # Return the resistance label
    return f"{resistance_label} {tolerance_label}"
