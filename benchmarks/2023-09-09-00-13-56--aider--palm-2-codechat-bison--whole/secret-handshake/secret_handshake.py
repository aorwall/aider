def commands(binary_str):
  """
  Converts a binary string to a sequence of actions in the secret handshake.

  The sequence of actions is chosen by looking at the rightmost five digits of the number once it's been converted to binary.
  Start at the right-most digit and move left.

  The actions for each number place are:

  00001 = wink
  00010 = double blink
  00100 = close your eyes
  01000 = jump
  10000 = Reverse the order of the operations in the secret handshake.

  Args:
    binary_str: A binary string representing the number to convert.

  Returns:
    A list of strings representing the actions in the secret handshake.
  """

  # Convert the binary string to a number.
  number = int(binary_str, 2)

  # Get the rightmost five digits of the number.
  rightmost_five_digits = number % (2 ** 5)

  # Create a list of actions.
  actions = []

  # Add an action for each of the rightmost five digits.
  for digit in rightmost_five_digits:
    if digit == 1:
      actions.append("wink")
    elif digit == 2:
      actions.append("double blink")
    elif digit == 4:
      actions.append("close your eyes")
    elif digit == 8:
      actions.append("jump")
    elif digit == 16:
      actions.append("reverse")

  # Reverse the order of the actions if necessary.
  if rightmost_five_digits & 16:
    actions.reverse()

  # Return the list of actions.
  return actions
