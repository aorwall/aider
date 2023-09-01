def trinary(string):
    if not is_valid_trinary(string):
        return 0
    result = 0
    for i, char in enumerate(string):
        result += int(char) * 3 ** (len(string) - i - 1)
    return result

def is_valid_trinary(string):
    return all(char in '012' for char in string)
