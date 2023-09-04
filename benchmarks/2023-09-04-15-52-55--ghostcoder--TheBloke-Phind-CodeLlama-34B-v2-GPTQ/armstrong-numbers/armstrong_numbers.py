def is_armstrong_number(number):
    # Convert the number into a list of digits
    digits = map(int, str(number))

    # Calculate the total number of digits (i.e., length of 'digits')
    num_digits = len(list(digits))

    # Compute the sum of each digit raised to the power of the total number of digits
    sums = sum([digit**num_digits for digit in digits])

    # Check if the number equals this sum
    return number == sums
