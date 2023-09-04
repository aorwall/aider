from collections import Counter
import math

def total(basket):
    # Calculate number of unique books
    num_unique_books = len(set([book for book in basket]))

    # If there's only one type of book in the basket
    if num_unique_books == 1:
        return len(basket) * 8

    # Group the books by their count
    counter = Counter(basket)
    groups = [list(group) for group in counter.items()]

    # Sort the groups by size descending
    sorted_groups = sorted(groups, key=lambda x: -x[1])

    # Apply the discounts
    total = 0
    while len(sorted_groups) > 0:
        if len(sorted_groups) >= 5:
            total += 25/100 * sum([book[1] for book in sorted_groups[:5]])
            sorted_groups = sorted_groups[5:]
        elif len(sorted_groups) >= 4:
            total += 20/100 * sum([book[1] for book in sorted_groups[:4]])
            sorted_groups = sorted_groups[4:]
        elif len(sorted_groups) >= 3:
            total += 10/100 * sum([book[1] for book in sorted_groups[:3]])
            sorted_groups = sorted_groups[3:]
        else:
            total += 8 * sum([book[1] for book in sorted_groups])
            sorted_groups = []

    return round(total, 2)
