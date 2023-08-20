def is_armstrong_number(number):
    # Convert the number to string
    str_num = str(number)
    # Calculate the power
    power = len(str_num)
    # Calculate the sum of each digit raised to the power
    sum_of_digits = sum(int(digit) ** power for digit in str_num)
    # Check if the sum equals the original number
    return sum_of_digits == number