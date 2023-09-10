def two_fer(name):
  """Returns a string saying what to say when giving away an extra cookie.

  Args:
    name: The name of the person you are giving the cookie to.

  Returns:
    A string saying what to say.
  """

  if name is None:
    return "One for you, one for me."
  else:
    return "One for {} one for me.".format(name)
