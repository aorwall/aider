def parse_octal(octal_str):

  if any(digit > '7' for digit in octal_str):
    raise ValueError

  decimal = 0 
  power = 0

  for digit in octal_str[::-1]:
    decimal += int(digit) * (8 ** power)
    power += 1

  return decimal
