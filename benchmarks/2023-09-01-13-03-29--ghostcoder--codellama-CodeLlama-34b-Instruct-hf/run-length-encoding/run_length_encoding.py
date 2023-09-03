def decode(string):
    result = ""
    i = 0
    while i < len(string):
        if string[i].isdigit():
            count = int(string[i])
            result += string[i+1] * count
            i += 2
        else:
            result += string[i]
            i += 1
    return result


def encode(string):
    result = ""
    i = 0
    while i < len(string):
        count = 1
        while i + count < len(string) and string[i] == string[i + count]:
            count += 1
        result += str(count) + string[i]
        i += count
    return result