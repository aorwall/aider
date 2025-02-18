def encode(number):
    """Encode an integer using Variable Length Quantity encoding."""
    result = []
    while number >= 0x80:
        result.append((number & 0x7F) | 0x80)
        number >>= 7
    result.append(number)
    return bytes(result)
def encode(numbers):
    pass


def decode(bytes_):
    """Decode a VLQ encoded byte array into an integer."""
    result = 0
    shift = 0
    for b in reversed(bytes_):
        if not (b & 0x80):   # last byte
            result += int.from_bytes([b], 'big') << shift
            break
        else:
            result += int.from_bytes([b & ~0x80], 'big') << shift
            shift += 7
    if len(bytes_) == 1 and bytes_[0] & 0x80:
        raise ValueError("Incomplete sequence")
    return result
