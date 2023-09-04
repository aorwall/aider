from itertools import filterfalse

def keep(sequence, predicate):
    return list(filter(predicate, sequence))


def discard(sequence, predicate):
    return list(filterfalse(predicate, sequence))
