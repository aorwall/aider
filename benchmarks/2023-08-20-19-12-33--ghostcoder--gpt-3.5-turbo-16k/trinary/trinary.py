import re

def trinary(string):
    if not re.match(r'^[0-2]+$', string):
        return 0

    decimal = 0
    power = 0
    for digit in string[::-1]:
        decimal += int(digit) * (3 ** power)
        power += 1

    return decimal