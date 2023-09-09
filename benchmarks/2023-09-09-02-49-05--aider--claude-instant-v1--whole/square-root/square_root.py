import math

def square_root(number):
  if not isinstance(number, int) or number < 0:
    raise ValueError("The radicand must be a positive integer.")

  root = 0
  for current in range(number+1):
    if current**2 == number:
      root = current
      break
    elif current**2 > number:
      break

  return root
