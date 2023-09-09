def value(colors):
    color_codes = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4',
                   'green': '5', 'blue': '6', 'grey': '8', 'white': '9'}
    
    if len(colors) == 2:
        first = color_codes[colors[0]] 
        second = color_codes[colors[1]]
        return int(first + second)
    else:
        return "00"
