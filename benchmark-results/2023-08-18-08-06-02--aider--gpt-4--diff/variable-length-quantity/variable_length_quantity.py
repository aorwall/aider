def encode(numbers):
    result = []
    for number in numbers:
        chunks = [bin(number)[2:].zfill(7)[i:i+7] for i in range(0, len(bin(number)[2:].zfill(7)), 7)][::-1]
        for i in range(len(chunks) - 1):
            chunks[i] = '1' + chunks[i]
        chunks[-1] = '0' + chunks[-1]
        result.extend([int(chunk, 2) for chunk in chunks][::-1])
    return result


def decode(bytes_):
    result = []
    number = ''
    for byte in bytes_:
        if byte >> 7 == 1:
            number += bin(byte & 0b01111111)[2:].zfill(7)
        else:
            number += bin(byte)[2:].zfill(7)
            result.append(int(number, 2))
            number = ''
    if number != '':
        raise ValueError("incomplete sequence")
    return result
