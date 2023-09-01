def encode(numbers):
    result = []
    for number in numbers:
        result.append(number & 0x7f)
        while number > 0x7f:
            number >>= 7
            result.append((number & 0x7f) | 0x80)
    return result


def decode(bytes_):
    result = 0
    for byte in bytes_:
        result = (result << 7) | (byte & 0x7f)
        if byte & 0x80 == 0:
            break
    return result
