import re

def convert(input_grid):
  if not isinstance(input_grid, list):
    raise TypeError("Input must be a list")
  
  lines = input_grid

  if len(lines) % 4 != 0:
    raise ValueError("Number of input lines is not a multiple of four")

  digits = []
  for i in range(0, len(lines), 4):
    digit = _convert_digit(lines[i:i+4])
    if digit == '?':
      raise ValueError("Number not recognizable")
    digits.append(digit)
  
  return ','.join(digits)

def _convert_digit(lines):
  patterns = {
    (' _ ',
     '| |',
     '|_|',
     '   '): '0',

    ('   ',
     '  |', 
     '  |',
     '   '): '1',

    (' _ ',
     ' _|',
     '|_ ',
     '   '): '2',

    (' _ ',
     ' _|',
     ' _|',
     '   '): '3',

    ('   ',
     '|_|',
     '  |',
     '   '): '4',

    (' _ ',
     '|_ ',
     ' _|',
     '   '): '5',

    (' _ ',
     '|_ ',
     '|_|',
     '   '): '6',

    (' _ ',
     '  |',
     '  |',
     '   '): '7',

    (' _ ',
     '|_|',
     '|_|',
     '   '): '8',

    (' _ ',
     '|_|',
     ' _|',
     '   '): '9'
  }

  digit = []
  for line in lines:
    digit.append(line[0] + line[1] + line[2])
  
  if tuple(digit) in patterns:
    return patterns[tuple(digit)]

  return '?'
