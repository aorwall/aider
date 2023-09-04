def flatten(lst):
    result = []

    def helper(x):
        if x is None:
            return
        elif isinstance(x, list):
            for i in x:
                helper(i)
        else:
            result.append(x)

    helper(lst)
    return result