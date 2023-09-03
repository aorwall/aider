def flatten(iterable):
    """
    Flattens a nested list-like structure into a flat list.
    Removes all None values from the resulting list.
    """
    result = []
    for item in iterable:
        if type(item) == list:
            result += flatten(item)
        elif item != None:
            result.append(item)
    return result
