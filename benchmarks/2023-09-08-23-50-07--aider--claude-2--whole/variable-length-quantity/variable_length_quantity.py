def encode(numbers):
    encoded = []
    for number in numbers:
        # Handle negative numbers
        if number < 0:
            number = (1 << 32) + number
        
        # Break number into 7-bit chunks
        chunks = []
        while number:
            chunks.append(number & 0x7F)
            number >>= 7
        
        # Set the high bit on all chunks except the last
        for i in range(len(chunks) - 1):
            chunks[i] |= 0x80
        
        # Concatenate and add to encoded list
        encoded.extend(chunks[::-1])
    
    return bytes(encoded)


def decode(bytes_):
    decoded = []
    number = 0
    for byte in bytes_:
        # Check high bit to see if this is the last byte
        if byte & 0x80 == 0:
            # Last byte
            number = (number << 7) | byte
            decoded.append(number)
            number = 0
        else:
            # More bytes to come
            number = (number << 7) | (byte & 0x7F)
    
    if number != 0:
        # Leftover bits at end
        raise ValueError("incomplete sequence")
    
    return decoded
