import math

def encode(plain_text, a, b):
  """
  Encrypts the given plain text using the affine cipher.

  Args:
    plain_text: The text to be encrypted.
    a: The first key of the affine cipher.
    b: The second key of the affine cipher.

  Returns:
    The encrypted text.
  """

  # Check that a and m are coprime.
  if not math.gcd(a, 26) == 1:
    raise ValueError("a and m must be coprime.")

  # Convert the plain text to its numeric equivalent.
  numeric_text = [ord(c) - ord('a') for c in plain_text]

  # Encrypt the numeric text using the affine cipher.
  encrypted_text = [(ai + b) % 26 for ai in numeric_text]

  # Convert the encrypted text back to characters.
  encrypted_text = [chr(ai + ord('a')) for ai in encrypted_text]

  # Return the encrypted text.
  return ''.join(encrypted_text)


def decode(ciphered_text, a, b):
  """
  Decrypts the given ciphered text using the affine cipher.

  Args:
    ciphered_text: The text to be decrypted.
    a: The first key of the affine cipher.
    b: The second key of the affine cipher.

  Returns:
    The decrypted text.
  """

  # Check that a and m are coprime.
  if not math.gcd(a, 26) == 1:
    raise ValueError("a and m must be coprime.")

  # Convert the ciphered text to its numeric equivalent.
  numeric_text = [ord(c) - ord('a') for c in ciphered_text]

  # Decrypt the numeric text using the affine cipher.
  decrypted_text = [(ai - b) % 26 for ai in numeric_text]

  # Convert the decrypted text back to characters.
  