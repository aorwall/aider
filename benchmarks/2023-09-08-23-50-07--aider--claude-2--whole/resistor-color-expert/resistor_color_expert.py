def resistor_label(colors):
    value_1 = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 
               'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}.get(colors[0], 0)
    value_2 = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 
               'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}.get(colors[1], 0)
    if len(colors) == 1:
        return '0 ohms'
    elif len(colors) == 2:
        return f'{(value_1 * 10) + value_2} ohms'
    elif len(colors) == 3:
        multiplier = {'black': 1, 'brown': 10, 'red': 100, 'orange': 1000, 
                      'yellow': 10000, 'green': 100000, 'blue': 1000000, 
                      'violet': 10000000, 'grey': 100000000, 'white': 1000000000}.get(colors[2], 1)
        return f'{(value_1 * 10) + value_2} ohms' if multiplier == 1 else f'{(value_1 * 10) + value_2} kiloohms'
    else:
        tolerance = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5, 
                     'brown': 1, 'red': 2, 'gold': 5, 'silver': 10}.get(colors[3], 0)
        multiplier = {'black': 1, 'brown': 10, 'red': 100, 'orange': 1000, 
                      'yellow': 10000, 'green': 100000, 'blue': 1000000, 
                      'violet': 10000000, 'grey': 100000000, 'white': 1000000000}.get(colors[2], 1)
        value = (value_1 * 10) + value_2
        unit = 'ohms' if multiplier == 1 else 'kiloohms' if multiplier == 1000 else 'megaohms'
        return f'{value} {unit}