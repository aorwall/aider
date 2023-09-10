def encode(message, rails):
  """
  Encodes the message using the rail fence cipher.

  Args:
    message: The message to be encoded.
    rails: The number of rails to use.

  Returns:
    The encoded message.
  """

  # Check that the number of rails is valid.
  if rails < 1:
    raise ValueError("The number of rails must be greater than 0.")

  # Create the rail fence.
  fence = []
  for i in range(rails):
    fence.append([])

  # Add the message to the rail fence.
  for i in range(len(message)):
    fence[i % rails].append(message[i])

  # Zig-zag through the rail fence to create the encoded message.
  encoded_message = []
  for i in range(rails):
    for j in range(i, len(fence[i]), rails):
      encoded_message.append(fence[i][j])

  return "".join(encoded_message)


def decode(encoded_message, rails):
  """
  Decodes the encoded message using the rail fence cipher.

  Args:
    encoded_message: The encoded message to be decoded.
    rails: The number of rails used to encode the message.

  Returns:
    The decoded message.
  """

  # Check that the number of rails is valid.
  if rails < 1:
    raise ValueError("The number of rails must be greater than 0.")

  # Create the rail fence.
  fence = []
  for i in range(rails):
    fence.append([])

  # Add the encoded message to the rail fence.
  for i in range(len(encoded_message)):
    fence[i % rails].append(encoded_message[i])

  # Zig-zag through the rail fence to create the decoded message.
  decoded_message = []
  for i in range(rails):
    for j in range(i, len(fence[i]), rails):
