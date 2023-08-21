def flatten(iterable):
    flattened_list = []
    for item in iterable:
        if isinstance(item, list):
            flattened_list.extend(flatten(item))
        elif item is not None:
            flattened_list.append(item)
    return flattened_list