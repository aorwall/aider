def answer(question):
  """
  Parse and evaluate a simple math word problem returning the answer as an integer.

  Args:
    question: A string containing a math word problem.

  Returns:
    The answer to the math word problem as an integer.

  Raises:
    ValueError: If the question is malformed or invalid, or contains an unknown operation.
  """

  # Split the question into words.
  words = question.split()

  # Check if the question contains any unknown operations.
  for word in words:
    if word not in ["plus", "minus", "multiplied by", "divided by"]:
      raise ValueError("unknown operation")

  # Evaluate the expression from left-to-right, ignoring the typical order of operations.
  result = 0
  for word in words:
    if word == "plus":
      result += int(words[words.index(word) + 1])
    elif word == "minus":
      result -= int(words[words.index(word) + 1])
    elif word == "multiplied by":
      result *= int(words[words.index(word) + 1])
    elif word == "divided by":
      result /= int(words[words.index(word) + 1])

  return result
