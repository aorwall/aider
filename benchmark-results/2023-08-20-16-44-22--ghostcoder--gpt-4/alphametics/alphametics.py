from itertools import permutations

def solve(puzzle):
    words = [word for word in puzzle.split(" ") if word.isalpha()]
    unique_chars = set(''.join(words))
    assert len(unique_chars) <= 10, "Too many letters"
    first_letters = [word[0] for word in words]
    n = len(first_letters)
    sorted_chars = ''.join(first_letters + list(unique_chars - set(first_letters)))
    for perm in permutations('0123456789', len(unique_chars)):
        if '0' not in perm[:n]:
            trans = str.maketrans(sorted_chars, ''.join(perm))
            translated_puzzle = puzzle.translate(trans)
            left, right = translated_puzzle.split(" == ")
            if sum(int(num) for num in left.split(" + ")) == int(right):
                return dict(zip(sorted_chars, perm))