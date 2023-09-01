def combinations(target, size, exclude):
    result = []
    for i in range(1, target + 1):
        if i not in exclude:
            result.append([i])
    return result