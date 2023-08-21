def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * input_base + digit
    
    output_digits = []
    if decimal_value == 0:
        output_digits.append(0)
    else:
        while decimal_value > 0:
            output_digits.insert(0, decimal_value % output_base)
            decimal_value //= output_base
    
    return output_digits
