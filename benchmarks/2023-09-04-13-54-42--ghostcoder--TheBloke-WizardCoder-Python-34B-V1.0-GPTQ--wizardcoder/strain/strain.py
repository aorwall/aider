def keep(sequence, predicate):
    kept = []
    for element in sequence:
        if predicate(element):
            kept.append(element)
    return kept


def discard(sequence, predicate):
    discarded = []
    for element in sequence:
        if not predicate(element):
            discarded.append(element)
    return discarded
