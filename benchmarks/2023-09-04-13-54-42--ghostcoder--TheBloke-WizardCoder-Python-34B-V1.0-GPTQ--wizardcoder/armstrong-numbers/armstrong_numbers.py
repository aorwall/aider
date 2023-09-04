def is_armstrong_number(number):
    num_digits = len(str(number))
    digit_sum = 0

    for digit in str(number):
        digit_sum += int(digit) ** num_digits

    return digit_sum == number
