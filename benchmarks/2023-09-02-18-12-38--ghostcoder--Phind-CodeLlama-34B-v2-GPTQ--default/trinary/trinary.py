def trinary(string):
    if not set(string).issubset('012'):
        return 0

    digits = [int(digit) for digit in string]
    base_three = [1, 3, 9]

    return sum([digits[i]*base_three[len(string)-i-2] for i in range(len(string)-1)])
