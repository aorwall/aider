def response(hey_bob):
  """Returns Bob's response to hey_bob."""

  if hey_bob.endswith("?"):
    return "Sure."
  elif hey_bob.isupper():
    return "Whoa, chill out!"
  elif hey_bob.endswith("!"):
    return "Calm down, I know what I'm doing!"
  elif hey_bob.strip() == "":
    return "Fine. Be that way!"
  else:
    return "Whatever."
