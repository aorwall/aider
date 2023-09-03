def trinary(string):
    if not set(string).issubset({'0', '1', '2'}):
        return 0  # Invalid characters found, return 0

    decimal_value = 0
    for index, digit in enumerate(reversed(string)):
        decimal_value += int(digit) * 3**index

    return decimal_value
