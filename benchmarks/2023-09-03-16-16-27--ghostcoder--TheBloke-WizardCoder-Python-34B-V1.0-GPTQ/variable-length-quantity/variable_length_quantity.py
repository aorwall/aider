def encode(number):
    """Encode a number into a byte string using VLQ format"""
    bytes_ = []
    while True:
        # extract the last seven bits of the number
        byte = (number & 0x7f)

        # set the high bit if there are more bytes to come
        if len(bytes_) > 0:
            byte |= 0x80
        else:
            byte &= 0x7f

        # add the current byte to the result list
        bytes_.insert(0, byte)

        # shift right by seven bits to continue with the next byte
        number >>= 7

        # check if we have processed all the bytes
        if number == 0:
            break

    return bytes(bytes_)
def encode(numbers):
    pass


def decode(bytes_):
    """Decode a byte string into a number using VLQ format"""
    num = 0
    for i, byte in enumerate(bytes_):
        # clear the high bit to get the value of the lower seven bits
        masked_byte = byte & 0x7f

        # shift left by 7 * position and add the value of the current byte
        num += masked_byte << (i*7)

        # check if this is the last byte
        if byte < 0x80:
            break

    # check if the input was valid
    if byte >= 0x80 and i == len(bytes_)-1:
        raise ValueError("incomplete sequence")

    return num
