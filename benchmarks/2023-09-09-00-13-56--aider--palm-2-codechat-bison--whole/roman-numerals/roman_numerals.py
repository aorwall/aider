def roman(number):
  """Converts an integer to a Roman numeral."""

  if number < 1 or number > 3999:
    raise ValueError("Number must be between 1 and 3999")

  roman_numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
  values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

  result = ""
  for i in range(len(values)):
    while number >= values[i]:
      result += roman_numerals[i]
      number -= values[i]

  return result
