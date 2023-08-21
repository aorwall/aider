import re
from itertools import permutations

def solve(puzzle):
    # Extract all unique letters from the puzzle
    letters = ''.join(set(re.findall('[A-Z]', puzzle)))
    
    # Generate all permutations of the digits 0-9 for the number of unique letters
    for perm in permutations('0123456789', len(letters)):
        # Create a mapping of letters to digits
        trans = str.maketrans(letters, ''.join(perm))
        
        # Substitute the letters in the puzzle with the corresponding digits
        new_puzzle = puzzle.translate(trans)
        
        # Split the puzzle into the addition part and the result part
        add, result = new_puzzle.split('=')
        add_parts = add.split(' + ')
        
        # Check if the sum of the addition part equals the result part
        if sum(int(part) for part in add_parts) == int(result):
            # Check if any number starts with zero
            if not any(part[0] == '0' for part in add_parts + [result]):
                # Return a dictionary mapping of letters to digits
                return dict(zip(letters, perm))
    return None
