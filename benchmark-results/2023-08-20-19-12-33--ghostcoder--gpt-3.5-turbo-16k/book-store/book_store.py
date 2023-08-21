def total(basket):
    # Create a dictionary to store the count of each book
    book_count = {}
    for book in basket:
        if book in book_count:
            book_count[book] += 1
        else:
            book_count[book] = 1

    # Calculate the total price
    total_price = 0
    while book_count:
        # Calculate the discount based on the number of different books in the basket
        discount = 0
        num_books = len(book_count)
        if num_books == 2:
            discount = 0.05
        elif num_books == 3:
            discount = 0.10
        elif num_books == 4:
            discount = 0.20
        elif num_books == 5:
            discount = 0.25

        # Calculate the price for the current group of books
        group_price = 8 * num_books * (1 - discount)

        # Add the price to the total
        total_price += group_price

        # Reduce the count of each book in the current group from the book_count dictionary
        for book in list(book_count.keys()):
            book_count[book] -= 1
            if book_count[book] == 0:
                del book_count[book]

    return total_price