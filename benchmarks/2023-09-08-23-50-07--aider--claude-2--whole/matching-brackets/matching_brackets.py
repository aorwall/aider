def is_paired(input_string):
  open_brackets = ['[','{','(']
  close_brackets = [']','}',')']

  stack = []

  for char in input_string:
    if char in open_brackets:
      stack.append(char)
    elif char in close_brackets:
      if not stack:
        return False
      last_open = stack.pop()
      if open_brackets.index(last_open) != close_brackets.index(char):
        return False

  return not stack
