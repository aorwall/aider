def recite(start, take=1):
  """
  Recite the lyrics to that beloved classic, that field-trip favorite: 99 Bottles of Beer on the Wall.

  Note that not all verses are identical.

  Args:
    start: The number of bottles of beer that start the song.
    take: The number of bottles to take each time through the song.

  Returns:
    A string containing the lyrics to the song.
  """

  bottles = start
  while bottles > 0:
    verse = _get_verse(bottles, take)
    bottles -= take
    yield verse

def _get_verse(bottles, take):
  """
  Get a single verse of the 99 Bottles of Beer song.

  Args:
    bottles: The number of bottles of beer in the verse.
    take: The number of bottles to take each time through the song.

  Returns:
    A string containing the lyrics to the verse.
  """

  verse = ""
  verse += f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.\n"
  verse += f"Take one down and pass it around, {bottles - take} bottles of beer on the wall.\n"
  if bottles == 1:
    verse += "Go to the store and buy some more, 99 bottles of beer on the wall."
  else:
    verse += "Take one down and pass it around, {bottles - take} bottles of beer on the wall."
  return verse
