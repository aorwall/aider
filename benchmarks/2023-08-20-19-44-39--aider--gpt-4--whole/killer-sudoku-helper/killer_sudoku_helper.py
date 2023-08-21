def combinations(target, size, exclude):
    def helper(target, size, exclude, start=1, combination=[]):
        if size == 0 and target == 0:
            return [combination]
        elif size == 0 or target == 0:
            return []
        else:
            result = []
            for i in range(start, 10):
                if i not in exclude and i <= target:
                    result += helper(target - i, size - 1, exclude, i + 1, combination + [i])
            return result

    return sorted(helper(target, size, exclude))
