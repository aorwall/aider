def encode(message, rails):
  rail_strings = [""] * rails
  for i in range(len(message)):
    rail_index = i % rails
    rail_strings[rail_index] += message[i]
  
  return "".join(rail_strings)


def decode(encoded_message, rails):
  rail_length = len(encoded_message) // rails
  
  decoded = []
  for i in range(rail_length):
    decoded.append("")
  
  rail_index = 0
  for char in encoded_message:
    decoded[rail_index] += char
    if rail_index >= rails - 1:
      increment = -1
    else:
      increment = 1
    rail_index += increment
  
  return "".join(decoded)
