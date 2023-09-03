def is_armstrong_number(number):
    # Convert the number into string to easily get individual digits
    str_num = str(number)

    # Calculate the number of digits in the number
    num_digits = len(str_num)

    # Initialize sum variable
    sum = 0

    # For each digit in the number
    for digit in str_num:
        # Add the power of the digit to the sum
        sum += int(digit) ** num_digits

    # Check if the calculated sum equals the original number
    return sum == number
