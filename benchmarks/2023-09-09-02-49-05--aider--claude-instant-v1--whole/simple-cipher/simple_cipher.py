def encode(self, text, key):
  return self._substitute(text, key)

def decode(self, text, key):
  return self._substitute(text, key, decode=True) 
