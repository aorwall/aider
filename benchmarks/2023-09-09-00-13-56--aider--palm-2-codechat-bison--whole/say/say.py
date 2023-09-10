def say(number):
  """
  Given a number from 0 to 999,999,999,999, spell out that number in English.

  If the number is negative, raise a ValueError with the message "input out of range".
  If the number is larger than 999,999,999,999, raise a ValueError with the message "input out of range".

  Args:
    number: The number to spell out.

  Returns:
    The English spelling of the number.
  """

  # Check if the number is negative.
  if number < 0:
    raise ValueError("input out of range")

  # Check if the number is larger than 999,999,999,999.
  if number > 9999999999999:
    raise ValueError("input out of range")

  # Break the number up into chunks of thousands.
  chunks = []
  while number > 0:
    chunks.append(number % 1000)
    number //= 1000

  # Reverse the order of the chunks.
  chunks.reverse()

  # Spell out each chunk.
  words = []
  for chunk in chunks:
    if chunk == 0:
      words.append("zero")
    elif chunk < 20:
      words.append(_UNDER_TWENTY[chunk])
    else:
      words.append(_TENS[chunk // 10])
      if chunk % 10 != 0:
        words.append(_UNDER_TWENTY[chunk % 10])

  # Add the appropriate scale word between each chunk.
  for i in range(len(words) - 1):
    if i == 0:
      continue
    elif i == 1:
      words[i] += " thousand"
    elif i == 3:
      words[i] += " million"
    