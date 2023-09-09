import re

def abbreviate(words):
  words = re.sub(r'[^a-zA-Z0-9 -]', '', words)
  
  # Split on whitespace and hyphens
  words = re.split(r'[-\s]', words)
  
  abbrev = ''.join(word[0] for word in words if word)
  return abbrev.upper()
