def encode(number):
    result = []
    while True:
        byte = number & 0x7f
        number >>= 7
        if number != 0:
            byte |= 0x80
        result.append(byte)
        if number == 0:
            break
    return result
def encode(numbers):
    result = []
    for number in numbers:
        while True:
            byte = number & 0x7f
            number >>= 7
            if number != 0:
                byte |= 0x80
            result.append(byte)
            if number == 0:
                break
    return result[::-1]

def decode(bytes_):
    numbers = []
    num = 0
    shift = 0
    index = len(bytes_) - 1
    while index >= 0:
        byte = bytes_[index]
        if byte & 0x80:
            num += (byte & 0x7f) << shift
            shift += 7
        else:
            num += byte << shift
            numbers.insert(0,num)
            num = 0
            shift = 0
        index -= 1
    return numbers
