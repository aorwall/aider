def encode(numbers):
    result = []
    for number in numbers:
        bytes_ = []
        while True:
            bytes_.insert(0, number & 0x7F)
            if number < 128:
                break
            number = number >> 7
        bytes_[-1] &= 0x7F
        result.extend(bytes_)
    return result


def decode(bytes_):
    numbers = []
    number = 0
    for byte in bytes_:
        number = (number << 7) | (byte & 0x7F)
        if not byte & 0x80:
            numbers.append(number)
            number = 0
    if number != 0:
        raise ValueError("incomplete sequence")
    return numbers
