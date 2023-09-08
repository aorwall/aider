def encode(numbers):
    """
    Encode a list of numbers using VLQ.

    :param numbers: List of numbers to encode.
    :return: Encoded bytes.
    """
    encoded = bytearray()
    for number in numbers:
        while True:
            byte = number & 0x7F
            number >>= 7
            if number == 0:
                encoded.append(byte)
                break
            else:
                encoded.append(byte | 0x80)
    return encoded