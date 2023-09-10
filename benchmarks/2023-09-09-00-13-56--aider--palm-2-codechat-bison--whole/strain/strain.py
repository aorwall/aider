def keep(sequence, predicate):
  """Returns a new collection containing those elements of the given sequence
  for which the predicate is true.

  Args:
    sequence: A sequence of elements.
    predicate: A function that takes an element of the sequence and returns a
      boolean.

  Returns:
    A new collection containing those elements of the given sequence for which
    the predicate is true.
  """

  result = []
  for element in sequence:
    if predicate(element):
      result.append(element)
  return result


def discard(sequence, predicate):
  """Returns a new collection containing those elements of the given sequence
  for which the predicate is false.

  Args:
    sequence: A sequence of elements.
    predicate: A function that takes an element of the sequence and returns a
      boolean.

  Returns:
    A new collection containing those elements of the given sequence for which
    the predicate is false.
  """

  result = []
  for element in sequence:
    if not predicate(element):
      result.append(element)
  return result
