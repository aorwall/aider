def decode(string):
    decoded = ''
    i = 0
    while i < len(string):
        count = int(string[i]) if i < len(string) and string[i].isdigit() else 1
        char = string[i+1] if i + 1 < len(string) else ''
        decoded += char * count
        i += 2
    return decoded


def encode(string):
    encoded = ''
    prev = ''
    count = 1
    for char in string:
        if char != prev:
            if prev:
                encoded += str(count) + prev
            count = 1
            prev = char
        else:
            count += 1
    if prev:
        encoded += str(count) + prev
    return encoded
