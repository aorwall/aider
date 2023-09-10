def encode(numbers):
    """Encodes a list of numbers into a variable length quantity.

    Args:
        numbers: A list of numbers to encode.

    Returns:
        A string of bytes representing the encoded numbers.
    """
    encoded_bytes = []
    for number in numbers:
        encoded_byte = number & 0x7F
        if number > 127:
            encoded_byte |= 0x80
        encoded_bytes.append(encoded_byte)

    return bytes(encoded_bytes)


def decode(bytes_):
    """Decodes a variable length quantity into a list of numbers.

    Args:
        bytes_: A string of bytes representing the encoded numbers.

    Returns:
        A list of numbers decoded from the bytes.
    """
    numbers = []
    index = 0
    while index < len(bytes_):
        encoded_byte = bytes_[index]
        number = encoded_byte & 0x7F
        if encoded_byte & 0x80:
            number |= (0x1 << 7)
            number <<= 1
            while index < len(bytes_) and bytes_[index] & 0x80:
                number |= (bytes_[index] & 0x7F) << 1
                index += 1
        numbers.append(number)
        index += 1

    return numbers
