def score(word):
  """Return the Scrabble score for a word."""
  score = 0
  for letter in word:
    score += letter_scores[letter.lower()]
  return score

