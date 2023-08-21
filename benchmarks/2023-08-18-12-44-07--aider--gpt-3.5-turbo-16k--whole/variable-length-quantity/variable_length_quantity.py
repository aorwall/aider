def encode(numbers):
    encoded_bytes = []
    for number in numbers:
        # Check if the number is within the valid range
        if number < 0 or number > 0xFFFFFFFF:
            raise ValueError("Number out of range: {}".format(number))
        
        # Encode the number into variable length quantity
        while True:
            # Get the least significant 7 bits of the number
            byte = number & 0x7F
            number >>= 7
            
            # Set the most significant bit if there are more bytes to follow
            if number > 0:
                byte |= 0x80
            
            # Add the byte to the encoded bytes list
            encoded_bytes.append(byte)
            
            # Break the loop if all bytes of the number have been encoded
            if number == 0:
                break
    
    return bytes(encoded_bytes)


def decode(bytes_):
    numbers = []
    number = 0
    for byte in bytes_:
        # Get the least significant 7 bits of the byte
        value = byte & 0x7F
        
        # Shift the number to the left by 7 bits and add the value
        number = (number << 7) | value
        
        # Check if the most significant bit is set
        if byte & 0x80 == 0:
            # Add the decoded number to the list
            numbers.append(number)
            number = 0
    
    return numbers
