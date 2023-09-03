def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    sum = 0
    for i, c in enumerate(isbn):
        if i == 9 and c == "X":
            sum += 10
        elif c.isdigit():
            sum += (10 - i) * int(c)
        else:
            return False
    return sum % 11 == 0
