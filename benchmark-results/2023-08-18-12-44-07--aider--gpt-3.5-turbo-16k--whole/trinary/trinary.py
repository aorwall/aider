def trinary(string):
    decimal = 0
    power = len(string) - 1

    for digit in string:
        if digit not in ['0', '1', '2']:
            return 0
        decimal += int(digit) * (3 ** power)
        power -= 1

    return decimal
