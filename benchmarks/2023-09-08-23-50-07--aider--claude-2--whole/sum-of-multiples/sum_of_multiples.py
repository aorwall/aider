def sum_of_multiples(limit, multiples):
  result = set()

  for base in multiples:
    if base != 0:
      for i in range(1, limit//base + 1):
        result.add(base * i)

  return sum(result)
