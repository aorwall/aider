def encode(number):
    """Encode a single 32-bit unsigned integer using variable-length quantity."""
    encoded = []

    while True:
        # Extract the next 7 bits of the number
        byte = number & 0x7f

        # Set the high bit if there are more bytes after this one
        if len(encoded) > 0 or byte >= 0x40:
            byte |= 0x80

        # Add the encoded byte to the list
        encoded.append(byte)

        # Shift the remaining bits right by 7
        number >>= 7

        # If there are no more bits left, break out of the loop
        if number == 0:
            break

    return encoded


def encode(numbers):
    encoded = []
    for num in numbers:
        encoded.extend(encode(num))
    return encoded


def decode(bytes_):
    """Decode a variable-length quantity into a single 32-bit unsigned integer."""
    result = 0
    shift = 0

    for byte in bytes_:
        # Check if the high bit is set
        if byte < 0x80:
            # No more bytes left, so add the final value and return
            result |= byte << shift
            break
        else:
            # Add the lower seven bits to the result
            result |= (byte & 0x7f) << shift
            shift += 7

            # Check if the next byte has been truncated
            if shift >= 32:
                raise ValueError("incomplete sequence")

    return result
