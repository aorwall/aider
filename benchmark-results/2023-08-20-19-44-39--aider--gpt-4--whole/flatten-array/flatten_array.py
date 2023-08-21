def flatten(iterable):
    flattened = []
    for i in iterable:
        if isinstance(i, list):
            flattened.extend(flatten(i))
        elif i is not None:
            flattened.append(i)
    return flattened
