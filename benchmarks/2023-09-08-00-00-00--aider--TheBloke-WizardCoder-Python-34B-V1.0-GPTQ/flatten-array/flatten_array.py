def flatten(iterable):
    """
    Flatten a nested list-like structure.

    Args:
        iterable: A list-like structure that may contain other list-like structures.

    Returns:
        A flattened list with all values except nil/null.
    """
    result = []
    for item in iterable:
        if isinstance(item, list):
            result.extend(flatten(item))
        elif item is not None:
            result.append(item)
    return result
