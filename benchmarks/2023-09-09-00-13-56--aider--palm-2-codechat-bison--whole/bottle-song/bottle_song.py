def recite(start, take=1):
  """
  Recite the lyrics to that popular children's repetitive song: Ten Green Bottles.

  Note that not all verses are identical.

  Args:
    start: The number of green bottles to start with.
    take: The number of verses to recite.

  Returns:
    A string containing the lyrics to the song.
  """

  bottles = start
  verses = []

  while bottles > 0 and take > 0:
    verses.append(_get_verse(bottles))
    bottles -= 1
    take -= 1

  return "\n".join(verses)

def _get_verse(bottles):
  """
  Get a single verse of the song.

  Args:
    bottles: The number of green bottles.

  Returns:
    A string containing the lyrics to the verse.
  """

  bottles_str = str(bottles)
  bottles_str = "{} green bottle{}".format(bottles_str, "s" if bottles > 1 else "")

  verse = """{} green bottles hanging on the wall,
{} green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be {} green bottles hanging on the wall.
""".format(bottles_str, bottles_str, bottles_str)

  return verse
