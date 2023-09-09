def total(basket):

    books = {}
    for book in basket:
        books[book] = books.get(book, 0) + 1

    groups = {}
    for book, count in books.items():
        existing_group = groups.get(count, None)
        if existing_group:
            existing_group.append(book)
        else:
            groups[count] = [book]

    discounts = {
        5: 0.25,
        4: 0.20, 
        3: 0.10,
        2: 0.05
    }

    total_price = 0
    for count, books in groups.items():
        discount = discounts.get(len(books), 0)
        price = count * 8 * (1 - discount)
        total_price += price

    return round(total_price, 2)
