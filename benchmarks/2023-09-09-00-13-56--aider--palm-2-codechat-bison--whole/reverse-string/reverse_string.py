def reverse(text):
  """Reverses a string.

  Args:
    text: The string to reverse.

  Returns:
    The reversed string.
  """
  # Create an empty list to store the reversed characters.
  reversed_text = []

  # Iterate over the characters in the input string in reverse order.
  for i in range(len(text) - 1, -1, -1):
    # Add the current character to the reversed list.
    reversed_text.append(text[i])

  # Join the characters in the reversed list to form a string.
  reversed_text = "".join(reversed_text)

  # Return the reversed string.
  return reversed_text
