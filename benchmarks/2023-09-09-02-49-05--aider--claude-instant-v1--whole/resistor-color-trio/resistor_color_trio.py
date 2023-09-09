def color_code(color):
  if color == 'black':
    return 0
  elif color == 'brown':
    return 1
  elif color == 'red': 
    return 2
  elif color == 'orange':
    return 3
  elif color == 'yellow':
    return 4
  elif color == 'green':
    return 5
  elif color == 'blue':
    return 6
  elif color == 'violet':
    return 7 
  elif color == 'grey':
    return 8
  elif color == 'white':
    return 9

def label(colors):
  first = color_code(colors[0])
  second = color_code(colors[1])
  value = (first * 10) + second

  third = color_code(colors[2])
  if third == 0:
    label = f"{value} ohms"
  elif third == 1:
    label = f"{value}0 ohms"
  elif third == 2: 
    label = f"{value}00 ohms"
  elif third == 3:
    label = f"{value}000 ohms" 
  elif third >= 4 and value >= 1000:
    if value >= 1000000:
      label = f"{value/1000000} gigaohms"
    elif value >= 1000:  
      label = f"{value/1000} kiloohms"

  return label
