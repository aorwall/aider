def calculate_discount(n):
    if n == 1:
        return 0
    elif n == 2:
        return 0.05
    elif n == 3:
        return 0.10
    elif n == 4:
        return 0.20
    else:
        return 0.25
def total(basket):
    # Initialize total price as zero
    total_price = 0

    # Count number of different books in the basket
    unique_books = len(set(basket))

    # Group books by their counts
    grouped_books = {}
    for book in basket:
        if book in grouped_books:
            grouped_books[book] += 1
        else:
            grouped_books[book] = 1

    # Calculate total price based on group sizes and apply discounts
    for count in grouped_books.values():
        total_price += (calculate_discount(unique_books) * count + unique_books - 1) * 8 / unique_books

    return round(total_price, 2)
