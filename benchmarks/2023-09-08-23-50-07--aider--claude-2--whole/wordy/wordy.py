import re

def answer(question):
  """Parse and evaluate simple math word problems returning the answer as an integer."""

  # Convert the question to lowercase
  question = question.lower()

  # Look for numbers
  numbers = re.findall(r'\d+', question)
  if not numbers:
    raise ValueError("No numbers found in question")

  # Look for operations
  if 'plus' in question:
    op = '+' 
  elif 'minus' in question:
    op = '-'
  elif 'multiplied by' in question:
    op = '*'
  elif 'divided by' in question:
    op = '/'
  else:
    raise ValueError("No valid operation found in question")

  # Evaluate simple expressions
  if len(numbers) == 1:
    return int(numbers[0])

  if len(numbers) == 2:
    a, b = int(numbers[0]), int(numbers[1])
    if op == '+':
      return a + b
    elif op == '-':
      return a - b  
    elif op == '*':
      return a * b
    elif op == '/':
      return a // b

  # Evaluate longer expressions left-to-right
  total = int(numbers[0])
  for i in range(1, len(numbers)):
    if op == '+':
      total += int(numbers[i])
    elif op == '-':
      total -= int(numbers[i])
    elif op == '*':  
      total *= int(numbers[i])
    elif op == '/':
      total //= int(numbers[i])

  return total
