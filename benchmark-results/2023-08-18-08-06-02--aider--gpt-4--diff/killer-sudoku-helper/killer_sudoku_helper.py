def combinations(target, size, exclude):
    if size == 1:
        return [[target]] if 1 <= target <= 9 and target not in exclude else []
    result = []
    for digit in range(1, 10):
        if digit not in exclude:
            for combination in combinations(target - digit, size - 1, exclude + [digit]):
                result.append([digit] + combination)
    return result
