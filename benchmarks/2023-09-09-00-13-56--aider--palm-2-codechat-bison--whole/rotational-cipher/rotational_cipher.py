def rotate(text, key):
  """
  Rotates the letters in the given text by the given key.

  Args:
    text: The text to rotate.
    key: The amount to rotate the letters by.

  Returns:
    The rotated text.
  """

  # Check that the key is a valid integer.

  if not isinstance(key, int):
    raise ValueError("Key must be an integer.")

  # Check that the key is between 0 and 26.

  if key < 0 or key > 26:
    raise ValueError("Key must be between 0 and 26.")

  # Create a mapping from the letters of the alphabet to their rotated counterparts.

  alphabet = "abcdefghijklmnopqrstuvwxyz"
  rotated_alphabet = alphabet[key:] + alphabet[:key]

  # Rotate the letters in the text.

  rotated_text = ""
  for letter in text:
    if letter in alphabet:
      rotated_text += rotated_alphabet[alphabet.index(letter)]
    else:
      rotated_text += letter

  return rotated_text
