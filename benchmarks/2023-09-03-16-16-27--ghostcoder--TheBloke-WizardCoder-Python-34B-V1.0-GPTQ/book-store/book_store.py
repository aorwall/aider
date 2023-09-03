from collections import Counter
import math

def total(basket):
    # Count how many times each book appears in the basket and sort them by price from high to low.
    counts = sorted([(price, count)
                   for price, count in Counter(basket).items()], reverse=True)

    # Initialize variables to keep track of the discounted prices and remaining books after applying group offers.
    discounted_prices = []
    remaining_books = sum(counts)

    while remaining_books >= 4:
        # Apply the offer for groups of four or more books with the highest price first.
        num_discounted_groups = remaining_books // 4
        discounted_prices += [num_discounted_groups * price]
        remaining_books -= num_discounted_groups * 4

    if remaining_books > 0:
        # If there are any remaining books, apply the offer for groups of two or three.
        num_pairs = remaining_books // 2
        remaining_books %= 2
        discounted_prices += [num_pairs * price for price, _ in counts[:num_pairs]]

        num_triplets = remaining_books // 3
        remaining_books %= 3
        discounted_prices += [num_triplets * price for price, _ in counts[num_pairs:num_pairs+num_triplets]]

        discounted_prices += [remaining_books * counts[-1][0]]

    return sum(discounted_prices)
