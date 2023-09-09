def decode(string):
  decoded = ""
  current_char = "" 
  count = 0

  for char in string:
    if char.isdigit():
      count = int(char)
    else:
      decoded += current_char * count  
      current_char = char
      count = 1

  decoded += current_char * count

  return decoded


def encode(string):
  if not string:
    return ""

  encoded = ""
  current_char = string[0]
  count = 1

  for i in range(len(string)):
    if i + 1 < len(string) and string[i] == string[i+1]:
      count += 1
    else: 
      encoded += str(count) + current_char
      current_char = string[i+1] if i + 1 < len(string) else ""
      count = 1

  return encoded
