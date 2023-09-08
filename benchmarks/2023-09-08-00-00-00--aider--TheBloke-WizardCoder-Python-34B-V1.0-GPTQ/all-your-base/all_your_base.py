def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    # Convert to decimal.
    n = 0
    for d in digits:
        n = n * input_base + d
    
    # Convert to output base.
    result = []
    while n > 0:
        n, d = divmod(n, output_base)
        result.append(d)
    
    return result[::-1]
