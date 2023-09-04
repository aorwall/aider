def encode(numbers):
    result = []
    for num in numbers:
        while num > 0:
            result.append(num & 0x7f)
            num >>= 7
        else:
            result[-1] |= 0x80
    return result


def decode(bytes_):
    result = []
    num = 0
    for b in bytes_:
        num <<= 7
        num += b & 0x7f
        if not (b & 0x80):
            result.append(num)
            num = 0
    if num != 0:
        raise ValueError("incomplete sequence")
    return result
