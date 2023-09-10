def get_matching_bracket(bracket):
  """
  Returns the matching bracket for the given bracket.

  Args:
    bracket: The bracket to get the matching bracket for.

  Returns:
    The matching bracket.
  """

  if bracket == "[":
    return "]"
  elif bracket == "{":
    return "}"
  elif bracket == "(":
    return ")"
  else:
    raise ValueError("Invalid bracket: " + bracket)


def is_paired(input_string):
  """
  Given a string containing brackets `[]`, braces `{}`, and parentheses `()`,
  verify that any and all pairs are matched and nested correctly.

  The string may also contain other characters, which for the purposes of this
  exercise should be ignored.

  Args:
    input_string: The string to be checked.

  Returns:
    True if all of the brackets are paired and nested correctly, and False
    otherwise.
  """

  # Create a stack to keep track of the open brackets.
  stack = []

  # Iterate over the characters in the input string.
  for character in input_string:
    # If the character is an open bracket, push it onto the stack.
    if character in ["[", "{", "("]:
      stack.append(character)

    # If the character is a closing bracket, pop the top item off of the stack.
    # If the stack is empty, or if the top item is not the matching open bracket,
    # then the brackets are not paired correctly.
    elif character in ["]", "}", ")"]:
      if len(stack) == 0:
        return False
      top_item = stack.pop()
      if top_item != get_matching_bracket(character):
        return False

  # If the stack is empty, then all of the brackets are paired correctly.
  if len(stack) == 0:
    return True
  else:
    return False

