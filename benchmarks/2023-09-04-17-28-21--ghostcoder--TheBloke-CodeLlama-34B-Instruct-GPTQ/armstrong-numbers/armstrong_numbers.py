def is_armstrong_number(number):
    # Calculate the number of digits in the number
    num_digits = len(str(number))

    # Initialize a variable to store the sum of the digits
    digit_sum = 0

    # Loop through each digit in the number
    for digit in str(number):
        # Calculate the digit raised to the power of the number of digits
        digit_power = int(digit) ** num_digits

        # Add the result to the running total
        digit_sum += digit_power

    # Check if the sum is equal to the original number
    return digit_sum == number
