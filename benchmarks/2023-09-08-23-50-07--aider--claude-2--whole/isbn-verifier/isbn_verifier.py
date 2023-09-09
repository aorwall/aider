def is_valid(isbn):
  """Check if ISBN-10 is valid"""

  # Remove hyphens
  isbn = isbn.replace('-', '')

  # Check if isbn is empty
  if isbn == '':
    return False
  
  # Extract digits
  digits = [c for c in isbn if c.isdigit()]

  # Extract check digit
  if len(digits) > 0:
    check_digit = digits[-1]
  else:
    return False

  # Extract other digits
  if len(digits) > 1:  
    digits = digits[:-1]
  else:
    return False

  # Define weights
  weights = [10,9,8,7,6,5,4,3,2]

  # Calculate sum of digits multiplied by weights
  if len(digits) > 0:
    sum_ = sum([int(d)*w for d,w in zip(digits, weights[:len(digits)])])
  else:
    return False

  # Take modulo 11
  check = sum_ % 11

  # Verify check digit
  if check_digit == 'X':
    return check == 10
  else:
    return check == int(check_digit)
