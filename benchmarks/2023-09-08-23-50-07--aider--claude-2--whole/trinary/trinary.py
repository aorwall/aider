def trinary(string):
  result = 0
  exponent = len(string) - 1
  for char in string:
    digit = int(char)
    if digit > 2 or digit < 0:
      return 0
    result += digit * (3 ** exponent)
    exponent -= 1
  return result
