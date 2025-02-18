def rebase(input_base, digits, output_base):
    # Check if input_base and output_base are valid.
    if input_base < 2 or output_base < 2:
        raise ValueError("Input and Output bases must be greater than or equal to 2.")

    # Convert digits list to integer value in input_base.
    num = sum([digits[i] * input_base ** (len(digits)-1 - i) for i in range(len(digits))])

    # Initialize the new digits list.
    new_digits = []

    while num > 0:
        remainder = num % output_base

        # Append the remainder to the new digits list.
        new_digits.append(remainder)

        # Update the num variable.
        num //= output_base

    # Reverse the order of the new digits list.
    new_digits.reverse()

    return new_digits
