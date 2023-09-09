def triplets_with_sum(number):
  triplets = []

  for a in range(1, number//3 + 1):
    for b in range(a + 1, number//2 + 1):
      c = number - a - b
      if a*a + b*b == c*c:
        triplets.append([a, b, c])

  return triplets
