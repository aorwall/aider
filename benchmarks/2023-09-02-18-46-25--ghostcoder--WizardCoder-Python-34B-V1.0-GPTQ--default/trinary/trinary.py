def trinary(string):
    if not all(c in '012' for c in string):
        return 0
    decimal_value = 0
    for i, digit in enumerate(reversed(string)):
        decimal_value += int(digit) * (3 ** i)
    return decimal_value
