def encode(string):
    encoded = ""
    count = 1
    prev_char = string[0]
    for char in string[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded += str(count) + prev_char
            count = 1
            prev_char = char
    encoded += str(count) + prev_char
    return encoded