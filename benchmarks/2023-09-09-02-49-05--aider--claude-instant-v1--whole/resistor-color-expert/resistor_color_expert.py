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
  if len(colors) == 1:
    return '0 ohms'

  value = int(''.join([str(COLOR_CODES[color]) for color in colors[:3]]))

  multiplier = COLOR_CODES[colors[3]] if len(colors) > 3 else 1

  tolerance = TOLERANCE_CODES[colors[-1]] if len(colors) > 3 else None

  if len(colors) == 4:
    value = value * 10 ** multiplier
    label = f'{value} ohms ±{tolerance}%'

  else:  
    value = value * 10 ** multiplier
    if value >= 1000:
      value = value/1000
      label = f'{value} kiloohms ±{tolerance}%'
    elif value >= 1000000:  
      value = value/1000000
      label = f'{value} megaohms ±{tolerance}%'
    else:
      label = f'{value} ohms ±{tolerance}%'

  return label
