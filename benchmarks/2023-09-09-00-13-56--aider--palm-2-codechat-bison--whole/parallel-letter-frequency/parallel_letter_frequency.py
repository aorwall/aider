def calculate(text_input):
  """
  Count the frequency of letters in texts using parallel computation.

  Args:
    text_input: A list of strings.

  Returns:
    A dictionary mapping each letter to its frequency.
  """

  # Split the text into individual letters.
  letters = []
  for text in text_input:
    for letter in text:
      letters.append(letter)

  # Count the frequency of each letter.
  letter_frequencies = {}
  for letter in letters:
    if letter not in letter_frequencies:
      letter_frequencies[letter] = 0
    letter_frequencies[letter] += 1

  # Return the total frequency of each letter.
  return letter_frequencies
