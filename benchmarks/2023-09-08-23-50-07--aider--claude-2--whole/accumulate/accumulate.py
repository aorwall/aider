def accumulate(collection, operation):
    accumulated = []
    for item in collection:
        accumulated.append(operation(item))
    return accumulated
