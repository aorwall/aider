def is_isogram(string):
  string = string.lower()
  seen_letters = set()

  for char in string:
    if char.isalpha():
      if char in seen_letters:
        return False
      seen_letters.add(char)

  return True
