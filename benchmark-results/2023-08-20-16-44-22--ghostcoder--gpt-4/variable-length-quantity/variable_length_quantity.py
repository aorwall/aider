def encode(numbers):
    result = []
    for number in numbers:
        bytes_ = []
        while number > 0:
            bytes_.insert(0, 128 | (number & 127))
            number >>= 7
        bytes_[0] &= 127
        result.extend(bytes_)
    return result


def decode(bytes_):
    result = []
    number = 0
    for byte in bytes_:
        number = (number << 7) | (byte & 127)
        if byte < 128:
            result.append(number)
            number = 0
    if number != 0:
        raise ValueError("incomplete sequence")
    return result