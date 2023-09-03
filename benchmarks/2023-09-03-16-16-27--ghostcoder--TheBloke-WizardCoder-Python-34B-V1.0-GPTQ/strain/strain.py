def keep(sequence, predicate):
    kept = []
    for x in sequence:
        if predicate(x):
            kept.append(x)
    return kept


def discard(sequence, predicate):
    discarded = []
    for x in sequence:
        if not predicate(x):
            discarded.append(x)
    return discarded
