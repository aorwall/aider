def transform(legacy_data):
  """
  This function transforms the legacy data format to the new data format.

  The legacy data format is a list of lists, where each inner list contains
  the letters that have the same point value. For example, the legacy data
  for the letters that are worth 1 point would be:

  [['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']]

  The new data format is a dictionary, where the keys are the letters and the
  values are their point values. For example, the new data for the letters
  that are worth 1 point would be:

  {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 'r': 1, 's': 1, 't': 1}

  Args:
    legacy_data: The legacy data to be transformed.

  Returns:
    The new data format.
  """

  new_data = {}
  for score, letters in legacy_data.items():
    for letter in letters:
      new_data[letter.lower()] = score

  return new_data
