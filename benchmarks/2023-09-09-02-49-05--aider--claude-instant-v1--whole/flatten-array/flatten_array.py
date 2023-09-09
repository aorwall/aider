def flatten(iterable):
    flattened = []
    
    for item in iterable:
        if item is not None:
            if isinstance(item, list):
                flattened.extend(flatten(item))
            else:
                flattened.append(item)
                
    return flattened
