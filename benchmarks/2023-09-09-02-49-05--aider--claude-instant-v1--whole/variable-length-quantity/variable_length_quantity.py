import math

def encode(numbers):
    encoded = b""
    for number in numbers:
        encoded += _encode_number(number)
        if encoded[-1] != 127:
            encoded += bytes([0])
    return encoded


def _encode_number(number):
    encoded = b""
    while number > 0:
        byte = number & 127
        number >>= 7 
        if number > 0:
            byte |= 128
        encoded += bytes([byte])
    return encoded


def decode(bytes_):
    decoded = []
    while bytes_:
        if bytes_ == b"":
            raise ValueError("incomplete sequence")
        number, length = _decode_number(bytes_)
        decoded.append(number)
        bytes_ = bytes_[length:]
    return decoded


def _decode_number(bytes_):
    number = 0
    shift = 0
    length = 0
    while True:
        if bytes_ == b"":
            raise ValueError("incomplete sequence")
        byte = bytes_[0]
        number |= (byte & 127) << shift
        length += 1
        if byte < 128:
            break
        shift += 7
        bytes_ = bytes_[1:]
    return number, length
