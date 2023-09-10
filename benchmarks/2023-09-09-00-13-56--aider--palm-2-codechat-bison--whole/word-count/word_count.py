import re

def count_words(sentence):
  """Counts the number of times each word occurs in a sentence.

  The words are case insensitive.

  Args:
    sentence: A string containing the sentence to be analyzed.

  Returns:
    A dictionary mapping each word to the number of times it occurs in the
    sentence.
  """

  # Split the sentence into words.
  words = re.split("[\\W_]", sentence.lower())

  # Count the number of times each word occurs.
  word_counts = {}
  for word in words:
    if word not in word_counts:
      word_counts[word] = 0
    word_counts[word] += 1

  return word_counts
