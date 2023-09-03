def keep(sequence, predicate):
    return [item for item in sequence if predicate(item)]


def discard(sequence, predicate):
    return [item for item in sequence if not predicate(item)]
