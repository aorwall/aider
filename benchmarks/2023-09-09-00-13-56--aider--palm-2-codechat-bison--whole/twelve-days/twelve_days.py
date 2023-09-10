def recite(start_verse, end_verse):
  """
  Given a start and end verse number, return the lyrics for those verses of
  "The Twelve Days of Christmas".

  Args:
    start_verse: The verse number to start with (1-12).
    end_verse: The verse number to end with (1-12).

  Returns:
    A string containing the lyrics for the given verses.
  """

  # Initialize the verses.
  verses = []

  # Add the first verse.
  verses.append(_get_first_verse())

  # Add the remaining verses.
  for verse_number in range(start_verse, end_verse + 1):
    verses.append(_get_next_verse(verse_number, verses[-1]))

  # Return the verses.
  return "\n".join(verses)

def _get_first_verse():
  """
  Returns the lyrics for the first verse of "The Twelve Days of Christmas".

  Returns:
    A string containing the lyrics for the first verse.
  """

  return (
      "On the first day of Christmas my true love gave to me: a Partridge in a "
      "Pear Tree."
  )

def _get_next_verse(verse_number, previous_verse):
  """
  Returns the lyrics for the next verse of "The Twelve Days of Christmas".

  Args:
    verse_number: The verse number to get.
    previous_verse: The lyrics for the previous verse.

  Returns:
    A string containing the lyrics for the next verse.
  """

  # Get the gifts for this verse.
  gifts = _get_gifts_for_verse(verse_number)

  # Get the beginning of the verse.
  beginning = _get_beginning_of_verse(verse_number, previous_verse)

  # Get the end of the verse.
  end = _get_end_of_verse(gifts)

  # Return the