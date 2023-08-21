def trinary(string):
    if not all(char in '012' for char in string):
        return 0
    result = 0
    for i, char in enumerate(string[::-1]):
        result += int(char) * (3 ** i)
    return result
