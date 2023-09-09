def sum_of_multiples(limit, multiples):
  total = 0
  seen = set()
  for factor in multiples:
    if factor != 0:
      for i in range(factor, limit+1, factor):
        if i not in seen:
          seen.add(i)
          total += i
  return total
