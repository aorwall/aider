from itertools import permutations

def combinations(target, size, exclude):
    """Return all unique combinations of numbers that add up to target with given size without excluding any number."""
    if size == 1:
        return [[x] for x in range(1, target + 1) if x != exclude]
    else:
        result = []
        for i in range(1, target - (size - 1)):
            sub_result = combinations(target - i, size - 1, exclude)
            for combo in sub_result:
                combo.append(i)
                result.append(sorted([*combo]) if i != exclude else sorted(set(combo)))
        return result