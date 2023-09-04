def trinary(string):
    if not all(c in '012' for c in string):
        return 0

    decimal = 0
    for index, digit in enumerate(reversed(string)):
        decimal += int(digit) * (3 ** index)

    return decimal
