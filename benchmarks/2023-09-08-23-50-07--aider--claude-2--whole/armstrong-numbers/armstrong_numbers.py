def is_armstrong_number(number):
  # Convert the number to a string
  number_str = str(number)
  
  # Initialize sum to 0
  sum = 0
  
  # Raise each digit to the power of the length
  # and add to the sum
  for digit in number_str:
    sum += int(digit) ** len(number_str)
    
  # Return true if the sum equals the number
  return sum == number
