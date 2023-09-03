def commands(binary_str):
    codes = {
        1: 'wink',
        2: 'double blink',
        4: 'close your eyes',
        8: 'jump'
    }

    # Convert the binary string into a list of integers.
    bits = [int(bit) for bit in binary_str]

    # Reverse the order if the most significant bit is set.
    if bits[0] == 1:
        bits = bits[::-1][:-1] + [0]

    # Create a list with the corresponding actions based on the remaining bits.
    result = []
    for i, bit in enumerate(bits):
        if bit != 0 and str(2**i) in codes:
            result.append(codes[2**i])

    return result
