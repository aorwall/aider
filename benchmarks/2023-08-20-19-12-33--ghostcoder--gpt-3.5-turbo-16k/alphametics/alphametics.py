from itertools import permutations

def solve(puzzle):
    words = puzzle.split()
    unique_letters = set(''.join(words))
    leading_letters = set(word[0] for word in words)
    letters = leading_letters.union(unique_letters - leading_letters)
    letters = sorted(letters)
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if all(mapping[word[0]] != 0 for word in words):
            nums = [int(''.join(str(mapping[ch]) for ch in word)) for word in words]
            if sum(nums[:-1]) == nums[-1]:
                return mapping
    return {}