def value(colors):
    color_values = {
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
    
    # Join the colors into a single string
    colors_str = '-'.join(colors)
    
    # Split the colors into a list
    color_list = colors_str.split('-')
    
    # Get the value of the first two colors
    first_color = color_list[0]
    second_color = color_list[1]
    
    # Get the numeric value of the first two colors
    first_value = color_values[first_color]
    second_value = color_values[second_color]
    
    # Combine the numeric values into a two-digit number
    result = int(str(first_value) + str(second_value))
    
    return result