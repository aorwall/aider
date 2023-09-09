def hexa(hex_string):
  decimal = 0
  for power, digit in enumerate(reversed(hex_string)):
    decimal += int(digit, 16) * (16 ** power)
  return decimal
