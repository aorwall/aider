def keep(sequence, predicate):
    return [x for x in sequence if predicate(x)]

def discard(sequence, predicate):
    return [x for x in sequence if not predicate(x)]
