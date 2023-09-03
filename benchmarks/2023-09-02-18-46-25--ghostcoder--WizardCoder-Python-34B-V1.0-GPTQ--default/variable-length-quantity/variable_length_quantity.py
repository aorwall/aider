def encode(number):
    """Encode an unsigned integer into VLQ format"""
    bytes_ = []
    while number >= 0x80:
        bytes_.append((number & 0x7F) | 0x80)
        number >>= 7
    bytes_.append(number)
    return bytes_[::-1]
def encode(numbers):
    pass


def decode(bytes_):
    """Decode a VLQ encoded list of integers"""
    if not all(isinstance(byte, int) for byte in bytes_) or any(byte < 0 for byte in bytes_):
        raise ValueError("Invalid input")

    result = 0
    for i, byte in enumerate(reversed(bytes_)):
        continuation = (byte & 0x80) != 0
        masked_byte = byte & 0x7F
        result += masked_byte << (i * 7)
        if not continuation:
            break

    # Check if the decoded value is within the range of a 32-bit unsigned integer
    if result > 2**32 - 1:
        raise ValueError("Value out of range")
    return result

def test():
    assert encode([0]) == [0]
    assert encode([40]) == [40]
    assert encode([127]) == [127]
    assert encode([128]) == [128 + 0x80, 0]
    assert encode([32767]) == [127 + 0x80, 127]
    assert encode([32768]) == [0x81, 0x80, 0]
    assert encode([5964607] + [2**32 - 1]) == [0xBF, 0xFF, 0xFF, 0xFF, 0x7F]

    assert decode([0]) == 0
    assert decode([40]) == 40
    assert decode([127]) == 127
    assert decode([128, 0]) == 128
    assert decode([0xC0, 0x80, 0]) == 32768
    assert decode([0xBF, 0xFF, 0xFF, 0xFF, 0x7F]) == 2 ** 32 - 1
