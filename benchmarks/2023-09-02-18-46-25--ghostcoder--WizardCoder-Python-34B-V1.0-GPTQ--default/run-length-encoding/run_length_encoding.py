def decode(string):
    """Decode a RLE compressed string."""
    result = ""
    index = 0
    while index < len(string):
        if string[index].isdigit():
            count = int(string[index])
            char = string[index + 1]
            result += char * count
            index += 2
        else:
            result += string[index]
            index += 1
    return result


def encode(string):
    """Encode a string using RLE."""
    result = ""
    prev_char = None
    count = 1
    for char in string:
        if char == prev_char:
            count += 1
        else:
            if prev_char is not None:
                result += str(count) + prev_char
            prev_char = char
            count = 1
    if prev_char is not None:
        result += str(count) + prev_char
    return result
