def trinary(string):
    valid_chars = set('012')
    if any((c not in valid_chars) for c in string):
        return 0

    total = 0
    for digit, power in zip(reversed(string), range(len(string))):
        total += int(digit) * (3 ** power)

    return total
