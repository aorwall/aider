def can_chain(dominoes):

  # Check for empty input
  if not dominoes:
    return []

  # Get all values
  values = []
  for domino in dominoes:
    values.extend(domino)

  # Check if any duplicates
  values_set = set(values)
  if len(values_set) != len(values):
    # Handle duplicates
    counts = {}
    for value in values_set:
      counts[value] = 0
    for domino in dominoes:
      counts[domino[0]] += 1
      counts[domino[1]] += 1

    max_count = max(counts.values())
    if max_count > len(dominoes):
      return False

  # Check if first and last values match    
  start = dominoes[0][0]
  end = dominoes[-1][1]

  return start == end
