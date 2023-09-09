def parse_octal(digits):
  if not digits.isdecimal():
    raise ValueError("Invalid octal digit(s)")

  decimal = 0
  place = 1
  for digit in reversed(digits):
    if int(digit) > 7:
      raise ValueError("Digit must be between 0 and 7")
    decimal += int(digit) * place
    place *= 8
  return decimal
