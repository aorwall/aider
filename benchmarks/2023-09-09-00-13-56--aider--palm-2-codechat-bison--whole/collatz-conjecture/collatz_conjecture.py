def steps(number):
  """
  Given a positive integer n, return the number of steps required to reach 1.

  The Collatz Conjecture states that no matter which number you start with, you will always reach 1 eventually.

  Args:
    number: A positive integer.

  Returns:
    The number of steps required to reach 1.

  Raises:
    ValueError: If the given value is not a positive integer.
  """

  if number <= 0:
    raise ValueError("Only positive integers are allowed")

  steps = 0
  while number != 1:
    if number % 2 == 0:
      number = number // 2
    else:
      number = 3 * number + 1
    steps += 1

  return steps
