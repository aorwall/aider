def keep(sequence, predicate):
  kept = []
  for item in sequence:
    if predicate(item):
      kept.append(item)
  return kept


def discard(sequence, predicate):
  discarded = []
  for item in sequence:
    if not predicate(item):
      discarded.append(item)
  return discarded
