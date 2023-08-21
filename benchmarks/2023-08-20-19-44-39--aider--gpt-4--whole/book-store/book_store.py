def total(basket):
    discounts = [0, 0, 0.05, 0.1, 0.2, 0.25]
    total = 0
    while len(basket) > 0:
        unique_books = set(basket)
        discount = discounts[len(unique_books)]
        total += len(unique_books) * 8 * (1 - discount)
        for book in unique_books:
            basket.remove(book)
    return total * 100
