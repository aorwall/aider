def factors(value):
  """
  Compute the prime factors of a given natural number.

  A prime number is only evenly divisible by itself and 1.

  Note that 1 is not a prime number.

  Args:
    value: The natural number to compute the prime factors of.

  Returns:
    A list of the prime factors of `value`.
  """

  # Initialize an empty list to store the prime factors.
  factors = []

  # Iterate over all natural numbers from 2 to the square root of `value`.
  for i in range(2, int(value ** 0.5) + 1):
    # While `i` divides evenly into `value`, add it to the list of prime factors.
    while value % i == 0:
      factors.append(i)
      value = value // i

  # If `value` is not divisible by any number from 2 to its square root, it is
  # prime and should be added to the list of prime factors.
  if value > 1:
    factors.append(value)

  # Return the list of prime factors.
  return factors
