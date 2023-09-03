def is_armstrong_number(number):
    if number < 0 or number > 10**7: # check for invalid input
        return False
    digits = [int(d) for d in str(number)]
    n = len(digits)
    total = sum([d ** n for d in digits])
    return total == number
