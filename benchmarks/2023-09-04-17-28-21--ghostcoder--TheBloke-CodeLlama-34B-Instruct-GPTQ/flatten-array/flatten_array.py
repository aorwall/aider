def flatten(iterable):
    flat_list = []
    for element in iterable:
        if hasattr(element, '__iter__') and not isinstance(element, str):
            flat_list += flatten(element)
        elif element is not None:
            flat_list.append(element)
    return flat_list
