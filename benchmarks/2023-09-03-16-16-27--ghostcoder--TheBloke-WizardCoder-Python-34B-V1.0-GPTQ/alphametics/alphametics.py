import re
from itertools import permutations

def valid(assignment, puzzle):
    if len(set(assignment)) != 10: # check if all digits are used
        return False
    for word in puzzle.split():
        try:
            eval(word.translate(str.maketrans(assignment)) % 10000, {}, {})
        except ZeroDivisionError:
            return False
    return True

def search(assignment):
    if len(assignment) == len(set(assignment)):
        return assignment
    for i in range(len(assignment)):
        new_assignment = assignment.copy()
        for d in range(10):
            if chr(i+ord('A')) not in new_assignment:
                new_assignment[chr(i+ord('A')] = d
                if valid(new_assignment, puzzle):
                    res = search(new_assignment)
                    if res is not None:
                        return res
    return None

def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_chars = set(''.join(words))
    assert len(unique_chars) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_words = sorted(words, key=lambda w: len(w), reverse=True)
    chars = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:n]
    digits = tuple(range(10))
    start = {c: d for c, d in zip(sorted(unique_chars - set(chars), digits)}
    for perm in permutations(digits, len(unique_chars)-len(start)):
        assignment = dict(zip(chars, perm))
        assignment.update(start)
        if valid(assignment, puzzle):
            res = search({k: str(v) for k, v in assignment.items()})
            if res is not None:
                return res
    return None

print(solve("A + B = C"))
print(solve("SEND + MORE = MONEY"))
print(solve("TWO + TWO = FOUR"))
print(solve("THIS + IS + NOT + A + PUZZLE"))