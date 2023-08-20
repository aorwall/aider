def is_armstrong_number(number):
    # Convert the number to a string
    str_num = str(number)
    num_digits = len(str_num)

    # Calculate the sum of each digit raised to the power of the number of digits
    total = sum(int(digit) ** num_digits for digit in str_num)

    # Check if the total is equal to the original number
    return total == number
