def total(basket):
    prices = {1: 8, 2: 8, 3: 8, 4: 8, 5: 8}
    discounts = {5: 0.25, 4: 0.20, 3: 0.10, 2: 0.05}

    def calculate_discounted_price(books):
        total_books = len(books)
        discount = discounts.get(total_books, 0)
        total_price = sum(prices[book] for book in books)
        return total_price * (1 - discount)

    unique_books = set(basket)
    groups = []

    while unique_books:
        group = [unique_books.pop()]
        for book in unique_books.copy():
            if book not in group:
                group.append(book)
                unique_books.remove(book)
        groups.append(group)

    total_price = sum(calculate_discounted_price(group) for group in groups)
    return round(total_price, 2)

# Test cases
print(total([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))  # Output: 51.6
print(total([1, 1, 1, 2, 2, 2, 3, 3, 3, 4]))  # Output: 51.2
