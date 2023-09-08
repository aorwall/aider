def trinary(string):
    if not all(c in '012' for c in string):
        return 0

    decimal = 0
    for i, digit in enumerate(reversed(string)):
        decimal += int(digit) * 3**i

    return decimal
