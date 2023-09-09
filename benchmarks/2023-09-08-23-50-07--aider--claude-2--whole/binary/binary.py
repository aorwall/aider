def parse_binary(binary_string):
  if not set(binary_string).issubset({'0', '1'}):
    raise ValueError("Invalid binary literal: " + binary_string)
  
  decimal = 0
  for i, digit in enumerate(reversed(binary_string)):
    decimal += int(digit) * (2 ** i)

  return decimal
