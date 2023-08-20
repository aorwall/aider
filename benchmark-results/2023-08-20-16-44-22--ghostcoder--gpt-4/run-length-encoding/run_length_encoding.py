def decode(string):
    count = ''
    decoded = ''
    for char in string:
        if char.isdigit():
            count += char
        else:
            decoded += char * int(count or '1')
            count = ''
    return decoded


def encode(string):
    encoded = ''
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i+1]:
            i += 1
            count += 1
        if count > 1:
            encoded += str(count) + string[i]
        else:
            encoded += string[i]
        i += 1
    return encoded