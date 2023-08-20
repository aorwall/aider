def decode(string):
    count = ''
    result = ''
    for char in string:
        if char.isdigit():
            count += char
        else:
            result += char * int(count or '1')
            count = ''
    return result


def encode(string):
    if not string:
        return ''
    count = 1
    result = ''
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            result += (str(count) if count > 1 else '') + string[i - 1]
            count = 1
    result += (str(count) if count > 1 else '') + string[-1]
    return result
