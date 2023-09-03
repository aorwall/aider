def combinations(target, size, exclude):
    """Return all valid combinations of digits that add up to target with a given size and excluding numbers in exclude."""
    def backtrack(start, current, remaining_sum, current_comb):
        if remaining_sum == 0:
            yield list(current)
        elif remaining_sum > 0 and len(current) < size - 1:
            for i in range(start + 1, 10):
                if i not in exclude:
                    new_exclude = set()
                    if i == 9:
                        new_exclude = {i} | exclude
                    else:
                        new_exclude = {i - 1, i + 1} | exclude
                    yield from backtrack(i, current + [i], remaining_sum - i, new_exclude)
    
    return sorted([c for c in backtrack(0, [], target, set())])

class KillerSudokuHelper:
    @staticmethod
    def find_valid_combinations(cage_sum, max_digits, used_numbers=None):
        """Find all valid combinations of digits that add up to cage_sum with at most max_digits."""
        if used_numbers is None:
            used_numbers = []
        
        return [sorted(combo) for combo in combinations(cage_sum, max_digits, set(used_numbers))]