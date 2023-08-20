def total(basket):
    # Create a dictionary to store the count of each book
    book_counts = {}
    for book in basket:
        if book in book_counts:
            book_counts[book] += 1
        else:
            book_counts[book] = 1
    
    # Calculate the total price
    total_price = 0
    while book_counts:
        # Calculate the maximum discount for the current set of books
        max_discount = 0
        for count in book_counts.values():
            if count > 0:
                max_discount += 1
        discount = max_discount * 5
        
        # Calculate the price for the current set of books
        price = (8 * len(book_counts)) * (1 - discount / 100)
        total_price += price
        
        # Reduce the count of books in the current set
        books_to_remove = []
        for book in book_counts:
            book_counts[book] -= 1
            if book_counts[book] == 0:
                books_to_remove.append(book)
        
        for book in books_to_remove:
            del book_counts[book]
    
    return total_price
