def decode(string):
    result = ''
    i = 0
    while i < len(string):
        count = ''
        while i < len(string) and string[i].isdigit():
            count += string[i]
            i += 1
        if count == '':
            count = '1'
        result += string[i] * int(count)
        i += 1
    return result

def encode(string):
    result = ''
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i+1]:
            i += 1
            count += 1
        if count == 1:
            result += string[i]
        else:
            result += str(count) + string[i]
        i += 1
    return result
