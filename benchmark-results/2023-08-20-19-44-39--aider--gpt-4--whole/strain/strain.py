def keep(sequence, predicate):
    result = []
    for element in sequence:
        if predicate(element):
            result.append(element)
    return result


def discard(sequence, predicate):
    result = []
    for element in sequence:
        if not predicate(element):
            result.append(element)
    return result
