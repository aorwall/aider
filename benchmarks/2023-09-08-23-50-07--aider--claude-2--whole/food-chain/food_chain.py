animals = [
  "fly",
  "spider", 
  "bird",
  "cat",
  "dog",
  "goat",
  "cow",
  "horse"
]

reasons = [
  "I don't know why she swallowed the fly. Perhaps she'll die.",
  "It wriggled and jiggled and tickled inside her.",
  "How absurd to swallow a bird!",
  "Imagine that, to swallow a cat!",
  "What a hog, to swallow a dog!",
  "Just opened her throat and swallowed a goat!",
  "I don't know how she swallowed a cow!",
  "She's dead, of course!"
]

reactions = [
  "I don't know why she swallowed the fly. Perhaps she'll die.",
  "She swallowed the spider to catch the fly.",
  "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
  "She swallowed the cat to catch the bird.",
  "She swallowed the dog to catch the cat.",
  "She swallowed the goat to catch the dog.", 
  "She swallowed the cow to catch the goat.",
  "She swallowed the horse to catch the cow."
]

def verse(n):
  output = f"I know an old lady who swallowed a {animals[n]}.\n{reasons[n]}"
  
  for i in range(n-1, -1, -1):
    output += f"\n{reactions[i]}"
  
  return output

def verses(start, end):
  return "\n".join([verse(i) for i in range(start, end)])

def sing():
  return verses(0, len(animals)-1)

def recite(start_verse, end_verse):
  return verses(start_verse, end_verse-1)
