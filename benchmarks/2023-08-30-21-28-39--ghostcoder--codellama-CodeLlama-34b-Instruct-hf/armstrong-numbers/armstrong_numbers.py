def is_armstrong_number(number):
    # Calculate the number of digits in the number
    num_digits = len(str(number))

    # Initialize a variable to store the sum of the digits
    digit_sum = 0

    # Loop through each digit in the number
    for digit in str(number):
        # Calculate the power of the digit
        digit_power = int(digit) ** num_digits

        # Add the power of the digit to the sum
        digit_sum += digit_power

    # Check if the sum is equal to the original number
    if digit_sum == number:
        return True
    else:
        return False
