def is_pangram(sentence):
  """
  This function checks if a sentence is a pangram.

  A pangram is a sentence that contains all 26 letters of the English alphabet.

  Args:
    sentence: The sentence to check.

  Returns:
    A boolean value, indicating whether or not the sentence is a pangram.
  """

  # Create a set of all 26 letters of the English alphabet.
  alphabet = set('abcdefghijklmnopqrstuvwxyz')

  # Convert the sentence to lowercase.
  sentence = sentence.lower()

  # Create a set of all the letters in the sentence.
  sentence_letters = set(sentence)

  # Check if the sentence contains all 26 letters of the alphabet.
  return len(sentence_letters) == len(alphabet)
