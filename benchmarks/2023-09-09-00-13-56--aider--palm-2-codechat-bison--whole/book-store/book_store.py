def total(basket):
  """
  Calculates the total cost of a basket of books.

  The basket is a list of books, where each book is a string.

  The cost of a single book is $8.

  If you buy two different books, you get a 5% discount on those two books.

  If you buy 3 different books, you get a 10% discount.

  If you buy 4 different books, you get a 20% discount.

  If you buy all 5, you get a 25% discount.

  Note that if you buy four books, of which 3 are different titles, you get a 10% discount on the 3 that form part of a set, but the fourth book still costs $8.

  Args:
    basket: A list of books.

  Returns:
    The total cost of the basket.
  """

  # First, we need to count the number of different books in the basket.
  # We do this by creating a set of all the books in the basket.

  books = set(basket)

  # Now, we need to calculate the discount for each group of books.
  # We do this by iterating over the groups of books, and calculating the discount for each group.

  discounts = []

  for i in range(1, len(books) + 1):
    for j in range(i + 1, len(books) + 1):
      discounts.append(_calculate_discount(i, j))

  # Now, we need to find the maximum discount.

  max_discount = max(discounts)

  # Finally, we can calculate the total cost of the basket.

  total_cost = 0

  for book in basket:
    total_cost += 8

  total_cost *= (100 - max_discount) / 100

  return total_cost

def _calculate_discount(n, m):
  """
  Calculates the discount for a group of books.

  Args