import re

def solve(puzzle):
  # Find all the unique letters in the puzzle
  letters = set(re.findall(r'[A-Z]', puzzle))
  
  # Map letters to numbers
  letter_to_num = {}
  
  for letter in letters:
    # Assign a unique number to each letter
    if letter not in letter_to_num:
      for num in range(10):
        if num not in letter_to_num.values():
          letter_to_num[letter] = num
          break
          
  # Replace letters with numbers
  puzzle = re.sub(r'[A-Z]', lambda m: str(letter_to_num[m.group(0)]), puzzle)

  # Split into words
  words = puzzle.split()

  # Convert words to numbers
  equations = []
  for word in words:
    if word.isalpha():
      # Convert letter words to numbers
      equations.append(int(re.sub(r'[A-Z]', lambda m: str(letter_to_num[m.group(0)]), word)))
    else:
      # Keep non-letter characters like + and = unchanged
      equations.append(word)
        
  # Check if it satisfies the puzzle
  if len(equations) == 3 and isinstance(equations[1], int) and equations[1] + equations[0] == equations[2]:
    return letter_to_num
  else:
    raise Exception("No solution found")
