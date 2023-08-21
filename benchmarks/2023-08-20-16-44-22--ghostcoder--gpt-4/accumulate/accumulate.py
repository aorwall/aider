def accumulate(collection, operation):
    result = []
    for x in collection:
        result.append(operation(x))
    return result