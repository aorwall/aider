def factors(value):
  factors = []
  
  # Keep dividing value by numbers from 2 up
  # Append each number that divides cleanly into factors
  # Stop when we can no longer divide by anything
  
  i = 2
  while i <= value:
    if value % i == 0:
      factors.append(i)
      value = value / i
    else:
      i += 1
      
  return factors
