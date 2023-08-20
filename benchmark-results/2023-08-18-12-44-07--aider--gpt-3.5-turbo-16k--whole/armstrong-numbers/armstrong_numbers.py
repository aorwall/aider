def is_armstrong_number(number):
    # Convert the number to a string to iterate over its digits
    number_str = str(number)
    
    # Get the number of digits in the number
    num_digits = len(number_str)
    
    # Calculate the sum of the digits raised to the power of the number of digits
    digit_sum = sum(int(digit) ** num_digits for digit in number_str)
    
    # Check if the calculated sum is equal to the original number
    return digit_sum == number
