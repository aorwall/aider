def flatten(iterable):
  """Flattens an arbitrarily-deep nested list-like structure.

  Args:
    iterable: An iterable object.

  Returns:
    A flattened list.
  """
  result = []
  for value in iterable:
    if value is None:
      continue
    if isinstance(value, list):
      result.extend(flatten(value))
    else:
      result.append(value)
  return result
