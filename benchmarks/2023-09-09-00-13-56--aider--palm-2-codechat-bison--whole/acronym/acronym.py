def abbreviate(words):
  """Convert a phrase to its acronym.

  Techies love their TLA (Three Letter Acronyms)!

  Help generate some jargon by writing a program that converts a long name like Portable Network Graphics to its acronym (PNG).

  Punctuation is handled as follows: hyphens are word separators (like whitespace); all other punctuation can be removed from the input.

  Args:
    words: A string containing the phrase to be abbreviated.

  Returns:
    A string containing the acronym of the input phrase.
  """

  # Remove all punctuation from the input phrase.
  words = re.sub("[^a-zA-Z]", "", words)

  # Split the input phrase into words.
  words = words.split()

  # Initialize the acronym.
  acronym = ""

  # Iterate over the words in the input phrase.
  for word in words:
    # Add the first letter of the word to the acronym.
    acronym += word[0]

  # Return the acronym.
  return acronym.upper()
